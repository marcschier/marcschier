<#
.SYNOPSIS
    Shared helpers for reading and writing the local GitHub Copilot CLI session store.

.DESCRIPTION
    The Copilot CLI keeps its session index in a SQLite database ("session-store.db") and the
    matching on-disk state under "session-state\<session-id>". Neither PowerShell nor .NET can read
    SQLite out of the box, so this module shells out to sqlite3.exe when available and otherwise to
    python (whose standard library includes sqlite3).

    All reads open the database read-only. When the live database cannot be opened - for example
    because another process holds it - queries fall back to a private snapshot of the .db, -wal and
    -shm files so a running Copilot session is never disturbed.
#>

Set-StrictMode -Version Latest

$script:SqliteRunner = $null

$script:PythonQueryScript = @'
import json, os, shutil, sqlite3, sys, tempfile
from pathlib import Path

with open(sys.argv[1], "r", encoding="utf-8") as f:
    req = json.load(f)
db = req["db"]
tmpdir = None
try:
    try:
        con = sqlite3.connect(Path(db).as_uri() + "?mode=ro", uri=True)
        con.execute("SELECT count(*) FROM sqlite_master").fetchone()
    except sqlite3.Error:
        # Fall back to a private snapshot when the live store cannot be opened read-only.
        tmpdir = tempfile.mkdtemp(prefix="copilot-store-")
        base = os.path.basename(db)
        for suffix in ("", "-wal", "-shm"):
            src = db + suffix
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(tmpdir, base + suffix))
        con = sqlite3.connect(os.path.join(tmpdir, base))
    con.row_factory = sqlite3.Row
    rows = [dict(r) for r in con.execute(req["query"], req.get("params") or [])]
    con.close()
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump(rows, f)
finally:
    if tmpdir:
        shutil.rmtree(tmpdir, ignore_errors=True)
'@

$script:PythonCommandScript = @'
import json, sqlite3, sys

with open(sys.argv[1], "r", encoding="utf-8") as f:
    req = json.load(f)
timeout = float(req.get("timeout") or 15.0)

con = sqlite3.connect(req["db"], timeout=timeout, isolation_level=None)
try:
    con.execute("PRAGMA busy_timeout = %d" % int(timeout * 1000))
    con.execute("BEGIN IMMEDIATE")
    changes = 0
    for item in req["batch"]:
        cur = con.execute(item["sql"], item.get("params") or [])
        if cur.rowcount and cur.rowcount > 0:
            changes += cur.rowcount
    con.execute("COMMIT")
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump({"changes": changes}, f)
except Exception:
    try:
        con.execute("ROLLBACK")
    except sqlite3.Error:
        pass
    raise
finally:
    con.close()
'@

function Resolve-CopilotHome {
    <#
    .SYNOPSIS
        Resolves the Copilot configuration directory.
    #>
    [CmdletBinding()]
    [OutputType([string])]
    param([string] $Requested)

    if ($Requested) { return $Requested }
    if ($env:COPILOT_HOME) { return $env:COPILOT_HOME }
    return (Join-Path -Path $HOME -ChildPath '.copilot')
}

function Get-CopilotStorePath {
    <#
    .SYNOPSIS
        Returns the path to session-store.db, optionally verifying that it exists.
    #>
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [string] $CopilotHome,
        [switch] $Require
    )

    $path = Join-Path -Path (Resolve-CopilotHome -Requested $CopilotHome) -ChildPath 'session-store.db'
    if ($Require -and -not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "Copilot session store not found at '$path'. Use -CopilotHome to point at the right directory."
    }
    return $path
}

function Get-CopilotSessionStateRoot {
    <#
    .SYNOPSIS
        Returns the session-state directory that holds one folder per session.
    #>
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [string] $CopilotHome,
        [switch] $Require
    )

    $path = Join-Path -Path (Resolve-CopilotHome -Requested $CopilotHome) -ChildPath 'session-state'
    if ($Require -and -not (Test-Path -LiteralPath $path -PathType Container)) {
        throw "Copilot session state directory not found at '$path'."
    }
    return $path
}

function Get-SqliteRunner {
    <#
    .SYNOPSIS
        Locates a usable SQLite runner, preferring sqlite3.exe and falling back to python.
    #>
    [CmdletBinding()]
    [OutputType([pscustomobject])]
    param()

    if ($script:SqliteRunner) { return $script:SqliteRunner }

    $sqlite = Get-Command -Name 'sqlite3.exe', 'sqlite3' -CommandType Application -ErrorAction SilentlyContinue |
        Select-Object -First 1
    $python = Get-Command -Name 'python.exe', 'python3.exe', 'python' -CommandType Application -ErrorAction SilentlyContinue |
        Select-Object -First 1

    if (-not $python) {
        throw @'
No usable SQLite reader was found. The Copilot session store is a SQLite database, and neither
PowerShell nor .NET can read one without help. Install Python (recommended, its standard library
includes sqlite3):

    winget install Python.Python.3.13
'@
    }

    # sqlite3.exe cannot run parameterised statements from the command line, so python drives every
    # query. sqlite3.exe is still recorded because it is handy for ad-hoc diagnostics.
    $script:SqliteRunner = [pscustomobject]@{
        Python = $python.Source
        Sqlite = if ($sqlite) { $sqlite.Source } else { $null }
    }
    return $script:SqliteRunner
}

function Invoke-PythonScript {
    <#
    .SYNOPSIS
        Runs one of the embedded python helpers, exchanging JSON through temporary files.

    .DESCRIPTION
        Request and response travel via files rather than the command line, because a bundle import
        batches statements whose parameters far exceed the Windows command line length limit.
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)] [string] $Script,
        [Parameter(Mandatory)] [hashtable] $Request
    )

    $runner = Get-SqliteRunner
    $stem = Join-Path -Path ([System.IO.Path]::GetTempPath()) -ChildPath ("copilot-store-{0}" -f [guid]::NewGuid())
    $scriptFile = "$stem.py"
    $inputFile = "$stem.in.json"
    $outputFile = "$stem.out.json"
    try {
        Set-Content -LiteralPath $scriptFile -Value $Script -Encoding utf8 -WhatIf:$false -Confirm:$false
        ConvertTo-Json -InputObject $Request -Depth 12 -Compress |
            Set-Content -LiteralPath $inputFile -Encoding utf8 -WhatIf:$false -Confirm:$false

        $output = & $runner.Python $scriptFile $inputFile $outputFile 2>&1
        if ($LASTEXITCODE -ne 0) {
            throw "SQLite access failed (exit code $LASTEXITCODE).`n$($output -join [Environment]::NewLine)"
        }
        if (-not (Test-Path -LiteralPath $outputFile)) { return '' }
        return (Get-Content -LiteralPath $outputFile -Raw)
    }
    finally {
        foreach ($file in @($scriptFile, $inputFile, $outputFile)) {
            Remove-Item -LiteralPath $file -Force -ErrorAction SilentlyContinue -WhatIf:$false -Confirm:$false
        }
    }
}

function Invoke-CopilotStoreQuery {
    <#
    .SYNOPSIS
        Runs a read-only query against a Copilot SQLite database and returns the rows as objects.
    #>
    [CmdletBinding()]
    [OutputType([object[]])]
    param(
        [Parameter(Mandatory)] [string] $DatabasePath,
        [Parameter(Mandatory)] [string] $Query,
        [object[]] $Parameters = @()
    )

    $json = Invoke-PythonScript -Script $script:PythonQueryScript -Request @{
        db     = $DatabasePath
        query  = $Query
        params = @($Parameters)
    }
    if ([string]::IsNullOrWhiteSpace($json)) { return @() }
    return @($json | ConvertFrom-Json)
}

function Invoke-CopilotStoreCommand {
    <#
    .SYNOPSIS
        Runs one or more write statements against a Copilot SQLite database in a single transaction.

    .DESCRIPTION
        Statements are supplied as objects with a Sql property and an optional Parameters array. The
        whole batch commits or rolls back together. A busy timeout is applied so a concurrently
        running Copilot CLI does not cause an immediate failure.
    #>
    [CmdletBinding()]
    [OutputType([int])]
    param(
        [Parameter(Mandatory)] [string] $DatabasePath,
        [Parameter(Mandatory)] [object[]] $Statement,
        [double] $TimeoutSeconds = 15
    )

    if ($Statement.Count -eq 0) { return 0 }

    $batch = @($Statement | ForEach-Object {
        [ordered]@{
            sql    = [string] $_.Sql
            params = @(if ($null -ne $_.PSObject.Properties['Parameters']) { $_.Parameters } else { @() })
        }
    })

    $json = Invoke-PythonScript -Script $script:PythonCommandScript -Request @{
        db      = $DatabasePath
        batch   = @($batch)
        timeout = $TimeoutSeconds
    }
    if ([string]::IsNullOrWhiteSpace($json)) { return 0 }
    return [int] ($json | ConvertFrom-Json).changes
}

function ConvertTo-UtcTimestamp {
    <#
    .SYNOPSIS
        Parses a session-store timestamp as UTC, accepting both ISO-8601 and 'YYYY-MM-DD HH:MM:SS'.
    #>
    [CmdletBinding()]
    [OutputType([nullable[datetime]])]
    param([string] $Value)

    if ([string]::IsNullOrWhiteSpace($Value)) { return $null }

    $styles = [System.Globalization.DateTimeStyles]::AdjustToUniversal -bor
              [System.Globalization.DateTimeStyles]::AssumeUniversal
    $parsed = [datetime]::MinValue
    if ([datetime]::TryParse($Value, [cultureinfo]::InvariantCulture, $styles, [ref] $parsed)) {
        return $parsed
    }
    return $null
}

function Get-DirectorySize {
    <#
    .SYNOPSIS
        Returns the total size in bytes of a directory tree, ignoring unreadable entries.
    #>
    [CmdletBinding()]
    [OutputType([long])]
    param([Parameter(Mandatory)] [string] $Path)

    if (-not (Test-Path -LiteralPath $Path)) { return [long] 0 }
    $total = [long] 0
    foreach ($file in (Get-ChildItem -LiteralPath $Path -Recurse -File -Force -ErrorAction SilentlyContinue)) {
        $total += $file.Length
    }
    return $total
}

function Test-CopilotSessionInUse {
    <#
    .SYNOPSIS
        Determines whether a session directory is claimed by a running Copilot process.

    .DESCRIPTION
        A live session drops an "inuse.<pid>.lock" file into its state directory. Those files are not
        always cleaned up, so a lock only counts when its process id still exists.
    #>
    [CmdletBinding()]
    [OutputType([bool])]
    param([Parameter(Mandatory)] [string] $SessionStatePath)

    if (-not (Test-Path -LiteralPath $SessionStatePath -PathType Container)) { return $false }

    $locks = Get-ChildItem -LiteralPath $SessionStatePath -Filter 'inuse.*.lock' -File -Force -ErrorAction SilentlyContinue
    foreach ($lock in $locks) {
        if ($lock.Name -match '^inuse\.(\d+)\.lock$') {
            $processId = [int] $Matches[1]
            if (Get-Process -Id $processId -ErrorAction SilentlyContinue) { return $true }
        }
    }
    return $false
}

function Get-CopilotWorkspaceInfo {
    <#
    .SYNOPSIS
        Reads the interesting fields out of a session's workspace.yaml.

    .DESCRIPTION
        workspace.yaml is a flat "key: value" document, so a full YAML parser is unnecessary. Returns
        $null when the file is missing.
    #>
    [CmdletBinding()]
    [OutputType([hashtable])]
    param([Parameter(Mandatory)] [string] $SessionStatePath)

    $file = Join-Path -Path $SessionStatePath -ChildPath 'workspace.yaml'
    if (-not (Test-Path -LiteralPath $file -PathType Leaf)) { return $null }

    $info = @{}
    foreach ($line in (Get-Content -LiteralPath $file -ErrorAction SilentlyContinue)) {
        if ($line -match "^\s*([A-Za-z0-9_]+):\s*(.*)$") {
            $value = $Matches[2].Trim()
            if ($value.Length -ge 2 -and $value[0] -eq "'" -and $value[-1] -eq "'") {
                $value = $value.Substring(1, $value.Length - 2).Replace("''", "'")
            } elseif ($value.Length -ge 2 -and $value[0] -eq '"' -and $value[-1] -eq '"') {
                $value = $value.Substring(1, $value.Length - 2)
            }
            $info[$Matches[1]] = $value
        }
    }
    return $info
}

function Format-ByteSize {
    <#
    .SYNOPSIS
        Formats a byte count using the largest sensible unit.
    #>
    [CmdletBinding()]
    [OutputType([string])]
    param([Parameter(Mandatory)] [long] $Bytes)

    if ($Bytes -ge 1GB) { return '{0:N2} GB' -f ($Bytes / 1GB) }
    if ($Bytes -ge 1MB) { return '{0:N1} MB' -f ($Bytes / 1MB) }
    if ($Bytes -ge 1KB) { return '{0:N1} KB' -f ($Bytes / 1KB) }
    return "$Bytes B"
}

Export-ModuleMember -Function @(
    'Resolve-CopilotHome'
    'Get-CopilotStorePath'
    'Get-CopilotSessionStateRoot'
    'Invoke-CopilotStoreQuery'
    'Invoke-CopilotStoreCommand'
    'ConvertTo-UtcTimestamp'
    'Get-DirectorySize'
    'Test-CopilotSessionInUse'
    'Get-CopilotWorkspaceInfo'
    'Format-ByteSize'
)
