<#
.SYNOPSIS
    Resumes recently used, non-empty GitHub Copilot CLI sessions in Windows Terminal tabs.

.DESCRIPTION
    Reads the local Copilot CLI session store (session-store.db) and selects sessions that

      * contain at least one recorded turn (aborted/blank launches are ignored),
      * were last updated within the requested time window,
      * still have an existing working directory on disk.

    Only the most recently updated session per working directory is kept, so a directory that
    accumulated several sessions contributes exactly one tab.

    For every selected session a new tab is added to the currently focused Windows Terminal
    window. The tab starts in the session's original working directory and runs
    'copilot --resume=<id> --allow-all'.

.PARAMETER Hours
    Size of the time window in hours. Mutually exclusive with -Days.

.PARAMETER Days
    Size of the time window in days. Mutually exclusive with -Hours. Defaults to 1 day.

.PARAMETER CopilotHome
    Copilot configuration directory holding session-store.db.
    Defaults to $env:COPILOT_HOME, then "$HOME\.copilot".

.PARAMETER Filter
    Optional wildcard pattern matched against the session working directory, repository and name.

.PARAMETER MaxTabs
    Safety cap on the number of tabs to open. Defaults to 20.

.PARAMETER CopilotArgument
    Additional arguments appended to the copilot command line, for example --model or --plan.

.PARAMETER CloseTabOnExit
    Close the tab as soon as copilot exits. By default the tab keeps a shell prompt in the
    session's working directory.

.EXAMPLE
    .\Resume-CopilotSessions.ps1 -Hours 8

    Resume every non-empty session touched in the last 8 hours.

.EXAMPLE
    .\Resume-CopilotSessions.ps1 -Days 3 -WhatIf

    Show which sessions would be resumed for a three day window without opening any tabs.

.EXAMPLE
    .\Resume-CopilotSessions.ps1 -Days 2 -Filter '*UA-.NETStandard*'

    Resume only sessions whose directory, repository or name matches the pattern.

.NOTES
    Requires PowerShell 7, Windows Terminal (wt.exe) and the Copilot CLI (copilot.exe).
    Reading the SQLite session store requires either sqlite3.exe or python on PATH.
#>
#Requires -Version 7.0
[CmdletBinding(SupportsShouldProcess, DefaultParameterSetName = 'Days')]
param(
    [Parameter(ParameterSetName = 'Hours')]
    [ValidateRange(0.0, 100000.0)]
    [double] $Hours,

    [Parameter(ParameterSetName = 'Days')]
    [ValidateRange(0.0, 10000.0)]
    [double] $Days = 1,

    [ValidateNotNullOrEmpty()]
    [string] $CopilotHome,

    [ValidateNotNullOrEmpty()]
    [string] $Filter,

    [ValidateRange(1, 200)]
    [int] $MaxTabs = 20,

    [string[]] $CopilotArgument = @(),

    [switch] $CloseTabOnExit
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Resolve-CopilotHome {
    param([string] $Requested)

    if ($Requested) { return $Requested }
    if ($env:COPILOT_HOME) { return $env:COPILOT_HOME }
    return (Join-Path -Path $HOME -ChildPath '.copilot')
}

function Get-SessionQuery {
    param([string] $SinceDate)

    # Coarse, index friendly day-granularity prefilter. The exact cutoff is applied afterwards
    # against the parsed timestamps so that fractional -Hours windows are honoured.
    return @"
SELECT s.id AS id,
       s.cwd AS cwd,
       s.repository AS repository,
       s.branch AS branch,
       s.summary AS summary,
       s.updated_at AS updated_at
FROM sessions s
WHERE substr(s.updated_at, 1, 10) >= '$SinceDate'
  AND EXISTS (SELECT 1 FROM turns t WHERE t.session_id = s.id)
ORDER BY s.updated_at DESC
"@
}

$script:PythonQueryScript = @'
import json, os, shutil, sqlite3, sys, tempfile
from pathlib import Path

db = sys.argv[1]
query = sys.argv[2]
tmpdir = None
try:
    try:
        con = sqlite3.connect(Path(db).as_uri() + "?mode=ro", uri=True)
        con.execute("SELECT count(*) FROM sqlite_master").fetchone()
    except sqlite3.Error:
        # Fall back to a private snapshot when the live store cannot be opened read-only.
        tmpdir = tempfile.mkdtemp(prefix="copilot-sessions-")
        base = os.path.basename(db)
        for suffix in ("", "-wal", "-shm"):
            src = db + suffix
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(tmpdir, base + suffix))
        con = sqlite3.connect(os.path.join(tmpdir, base))
    con.row_factory = sqlite3.Row
    rows = [dict(r) for r in con.execute(query)]
    con.close()
    json.dump(rows, sys.stdout)
finally:
    if tmpdir:
        shutil.rmtree(tmpdir, ignore_errors=True)
'@

function Invoke-SessionStoreQuery {
    param(
        [Parameter(Mandatory)] [string] $DatabasePath,
        [Parameter(Mandatory)] [string] $Query
    )

    $sqlite = Get-Command -Name 'sqlite3.exe' -CommandType Application -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if ($sqlite) {
        Write-Verbose "Querying session store with $($sqlite.Source)."
        $json = & $sqlite.Source '-readonly' '-json' $DatabasePath $Query
        if ($LASTEXITCODE -ne 0) {
            throw "sqlite3.exe failed with exit code $LASTEXITCODE while reading '$DatabasePath'."
        }
        return ConvertFrom-SqliteJson -Json ($json -join [Environment]::NewLine)
    }

    $python = Get-Command -Name 'python.exe', 'python3.exe', 'python' -CommandType Application -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if (-not $python) {
        throw @'
No SQLite reader available. The Copilot session store is a SQLite database, so this script needs
either sqlite3.exe or python on PATH. Install one of them, for example:

    winget install Python.Python.3.13
    winget install SQLite.SQLite
'@
    }

    Write-Verbose "Querying session store with $($python.Source)."
    $scriptFile = Join-Path -Path ([System.IO.Path]::GetTempPath()) -ChildPath ("copilot-sessions-{0}.py" -f [guid]::NewGuid())
    try {
        Set-Content -LiteralPath $scriptFile -Value $script:PythonQueryScript -Encoding utf8 -WhatIf:$false -Confirm:$false
        $json = & $python.Source $scriptFile $DatabasePath $Query
        if ($LASTEXITCODE -ne 0) {
            throw "python failed with exit code $LASTEXITCODE while reading '$DatabasePath'."
        }
        return ConvertFrom-SqliteJson -Json ($json -join [Environment]::NewLine)
    }
    finally {
        Remove-Item -LiteralPath $scriptFile -Force -ErrorAction SilentlyContinue -WhatIf:$false -Confirm:$false
    }
}

function ConvertFrom-SqliteJson {
    param([string] $Json)

    if ([string]::IsNullOrWhiteSpace($Json)) { return @() }
    return @($Json | ConvertFrom-Json)
}

function ConvertTo-UtcTimestamp {
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

function Get-TabTitle {
    param([pscustomobject] $Session)

    $title = $Session.summary
    if ([string]::IsNullOrWhiteSpace($title)) {
        if (-not [string]::IsNullOrWhiteSpace($Session.repository)) {
            $title = $Session.repository
            if (-not [string]::IsNullOrWhiteSpace($Session.branch)) {
                $title = "$title#$($Session.branch)"
            }
        }
    }
    if ([string]::IsNullOrWhiteSpace($title)) {
        $title = "copilot $($Session.id.Substring(0, 8))"
    }

    # Windows Terminal splits its command line on ';', and quotes break argument passing.
    $title = ($title -replace '[;"\u0060\p{C}]', ' ') -replace '\s+', ' '
    $title = $title.Trim()
    if ($title.Length -gt 40) { $title = $title.Substring(0, 39).TrimEnd() + [char]0x2026 }
    return $title
}

function Get-StartingDirectory {
    param([string] $Path)

    # A trailing backslash would escape the closing quote of -d "<path>".
    $trimmed = $Path.TrimEnd('\', '/')
    if ($trimmed -match '^[A-Za-z]:$') { return "$trimmed\" }
    if ([string]::IsNullOrWhiteSpace($trimmed)) { return $Path }
    return $trimmed
}

$copilotHomePath = Resolve-CopilotHome -Requested $CopilotHome
$databasePath = Join-Path -Path $copilotHomePath -ChildPath 'session-store.db'
if (-not (Test-Path -LiteralPath $databasePath -PathType Leaf)) {
    throw "Copilot session store not found at '$databasePath'. Use -CopilotHome to point at the right directory."
}

$windowsTerminal = Get-Command -Name 'wt.exe' -CommandType Application -ErrorAction SilentlyContinue |
    Select-Object -First 1
if (-not $windowsTerminal) {
    throw 'Windows Terminal (wt.exe) was not found on PATH. Install it with: winget install Microsoft.WindowsTerminal'
}

if (-not (Get-Command -Name 'copilot' -ErrorAction SilentlyContinue)) {
    throw 'The Copilot CLI (copilot) was not found on PATH.'
}

$window = if ($PSCmdlet.ParameterSetName -eq 'Hours') {
    [timespan]::FromHours($Hours)
} else {
    [timespan]::FromDays($Days)
}
$cutoffUtc = [datetime]::UtcNow - $window
Write-Verbose "Selecting sessions updated after $($cutoffUtc.ToString('u')) (window: $window)."

$query = Get-SessionQuery -SinceDate $cutoffUtc.AddDays(-1).ToString('yyyy-MM-dd')
$rows = Invoke-SessionStoreQuery -DatabasePath $databasePath -Query $query
Write-Verbose "Session store returned $($rows.Count) non-empty candidate session(s)."

$candidates = [System.Collections.Generic.List[pscustomobject]]::new()
foreach ($row in $rows) {
    $updated = ConvertTo-UtcTimestamp -Value $row.updated_at
    if (-not $updated) {
        Write-Verbose "Skipping session $($row.id): unparsable timestamp '$($row.updated_at)'."
        continue
    }
    if ($updated -lt $cutoffUtc) { continue }

    if ([string]::IsNullOrWhiteSpace($row.cwd)) {
        Write-Verbose "Skipping session $($row.id): no working directory recorded."
        continue
    }
    if (-not (Test-Path -LiteralPath $row.cwd -PathType Container)) {
        Write-Warning "Skipping session $($row.id) ($($row.summary)): directory '$($row.cwd)' no longer exists."
        continue
    }
    if ($row.cwd.Contains(';')) {
        Write-Warning "Skipping session $($row.id): directory '$($row.cwd)' contains ';', which Windows Terminal cannot handle."
        continue
    }

    $candidates.Add([pscustomobject]@{
        Id         = $row.id
        Cwd        = $row.cwd
        Repository = $row.repository
        Branch     = $row.branch
        Summary    = $row.summary
        UpdatedUtc = $updated
    })
}

if ($Filter) {
    $before = $candidates.Count
    $candidates = [System.Collections.Generic.List[pscustomobject]](@($candidates | Where-Object {
        $_.Cwd -like $Filter -or $_.Repository -like $Filter -or $_.Summary -like $Filter
    }))
    Write-Verbose "Filter '$Filter' removed $($before - $candidates.Count) session(s)."
}

$selected = @($candidates |
    Group-Object -Property { $_.Cwd.ToLowerInvariant() } |
    ForEach-Object { $_.Group | Sort-Object -Property UpdatedUtc -Descending | Select-Object -First 1 } |
    Sort-Object -Property UpdatedUtc -Descending)

if ($selected.Count -eq 0) {
    Write-Host "No non-empty Copilot sessions were updated in the last $window." -ForegroundColor Yellow
    return
}

if ($selected.Count -gt $MaxTabs) {
    Write-Warning "$($selected.Count) session(s) matched; opening only the $MaxTabs most recent. Raise -MaxTabs to include more."
    $selected = $selected | Select-Object -First $MaxTabs
}

$selected |
    Select-Object @{ Name = 'Title'; Expression = { Get-TabTitle -Session $_ } },
                  @{ Name = 'Directory'; Expression = { $_.Cwd } },
                  @{ Name = 'UpdatedUtc'; Expression = { $_.UpdatedUtc.ToString('yyyy-MM-dd HH:mm') } },
                  @{ Name = 'Session'; Expression = { $_.Id } } |
    Format-Table -AutoSize |
    Out-String |
    Write-Host

$opened = 0
foreach ($session in $selected) {
    $title = Get-TabTitle -Session $session
    $directory = Get-StartingDirectory -Path $session.Cwd

    $copilotCommand = "copilot --resume=$($session.Id) --allow-all"
    if ($CopilotArgument.Count -gt 0) {
        $copilotCommand = "$copilotCommand $($CopilotArgument -join ' ')"
    }

    # '-w 0' targets the most recently used (currently focused) Windows Terminal window.
    # The copilot command is passed as a single token so Windows Terminal never tries to
    # interpret '--resume' or '--allow-all' as options of its own.
    $wtArguments = @(
        '-w', '0'
        'new-tab'
        '--title', $title
        '-d', $directory
        'cmd.exe'
        $(if ($CloseTabOnExit) { '/c' } else { '/k' })
        $copilotCommand
    )

    $target = "$title  [$($session.Cwd)]"
    if ($PSCmdlet.ShouldProcess($target, 'Open Windows Terminal tab')) {
        & $windowsTerminal.Source @wtArguments
        if ($LASTEXITCODE -ne 0) {
            Write-Warning "wt.exe returned exit code $LASTEXITCODE for session $($session.Id)."
        } else {
            $opened++
        }
        # Give Windows Terminal a moment so tabs appear in the intended order.
        Start-Sleep -Milliseconds 250
    } else {
        Write-Verbose ("Would run: wt.exe {0}" -f ($wtArguments -join ' '))
    }
}

if ($opened -gt 0) {
    Write-Host "Opened $opened Copilot session tab(s)." -ForegroundColor Green
}
