<#
.SYNOPSIS
    Packages GitHub Copilot CLI session state from one machine and applies it on another.

.DESCRIPTION
    Export selects non-empty sessions - those with at least one recorded turn - that were last
    updated within the requested window, and writes a bundle containing both the database rows and
    the on-disk session state.

    Import reads such a bundle and merges it into the local session store, optionally rewriting
    absolute paths so sessions land on the right clones when the target machine uses a different
    directory layout.

    A bundle looks like this:

        manifest.json              bundle metadata and one entry per session
        sessions\<id>\rows.json    every session-scoped row from session-store.db
        sessions\<id>\state\...    a copy of session-state\<id>

.PARAMETER Export
    Produce a bundle from this machine.

.PARAMETER Import
    Apply a bundle to this machine.

.PARAMETER Path
    Bundle location. A path ending in .zip is treated as an archive; anything else is a directory
    bundle. Directory bundles are strongly preferred for large exports, because session artifacts are
    mostly incompressible.

.PARAMETER Hours
    Export sessions updated within this many hours. Mutually exclusive with -Days.

.PARAMETER Days
    Export sessions updated within this many days. Defaults to 1 day, matching
    Resume-CopilotSessions.ps1.

.PARAMETER Filter
    Wildcard matched against the session working directory, repository and name.

.PARAMETER Lean
    Exclude the bulky, machine-specific parts of the session state: files\, rewind-file-snapshots\
    and rewind-snapshots\.

.PARAMETER ExcludeDirectory
    Additional session-state subdirectory names to leave out of the bundle.

.PARAMETER Overwrite
    On import, replace sessions that already exist on the target.

.PARAMETER PathMap
    One or more 'SOURCE=TARGET' rules applied as case-insensitive path prefix rewrites during import,
    for example 'D:\git=C:\src'. Paths that match no rule are kept as they are.

.PARAMETER CopilotHome
    Copilot configuration directory. Defaults to $env:COPILOT_HOME, then "$HOME\.copilot".

.PARAMETER Force
    Continue even when the bundle was produced against a different session store schema version.

.EXAMPLE
    .\Copy-CopilotSessions.ps1 -Export -Path D:\transfer\copilot -Days 2

    Bundle everything worked on in the last two days.

.EXAMPLE
    .\Copy-CopilotSessions.ps1 -Export -Path D:\transfer\copilot.zip -Days 7 -Lean

    Produce a small archive with transcripts, plans and todos but no agent artifacts.

.EXAMPLE
    .\Copy-CopilotSessions.ps1 -Import -Path D:\transfer\copilot -PathMap 'D:\git=C:\src'

    Apply a bundle on a machine whose clones live under C:\src.

.NOTES
    Requires PowerShell 7 and a SQLite reader (python or sqlite3.exe) on PATH.
    Close the Copilot CLI before importing so the session store is not being written concurrently.
#>
#Requires -Version 7.0
# Write-Host is deliberate: the session tables and progress messages are for the operator.
# Invoke-Export / Invoke-Import / Update-WorkspaceFile are internal helpers that delegate to this
# script's own $PSCmdlet.ShouldProcess, which the analyser cannot follow across function boundaries.
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSShouldProcess', '')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseShouldProcessForStateChangingFunctions', '')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseSingularNouns', '')]
[CmdletBinding(SupportsShouldProcess, DefaultParameterSetName = 'Export')]
param(
    [Parameter(Mandatory, ParameterSetName = 'Export')]
    [switch] $Export,

    [Parameter(Mandatory, ParameterSetName = 'Import')]
    [switch] $Import,

    [Parameter(Mandatory, ParameterSetName = 'Export')]
    [Parameter(Mandatory, ParameterSetName = 'Import')]
    [ValidateNotNullOrEmpty()]
    [string] $Path,

    [Parameter(ParameterSetName = 'Export')]
    [ValidateRange(0.0, 100000.0)]
    [double] $Hours,

    [Parameter(ParameterSetName = 'Export')]
    [ValidateRange(0.0, 10000.0)]
    [double] $Days,

    [ValidateNotNullOrEmpty()]
    [string] $Filter,

    [Parameter(ParameterSetName = 'Export')]
    [switch] $Lean,

    [Parameter(ParameterSetName = 'Export')]
    [string[]] $ExcludeDirectory = @(),

    [Parameter(ParameterSetName = 'Import')]
    [switch] $Overwrite,

    [Parameter(ParameterSetName = 'Import')]
    [string[]] $PathMap = @(),

    [ValidateNotNullOrEmpty()]
    [string] $CopilotHome,

    [switch] $Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Import-Module -Name (Join-Path -Path $PSScriptRoot -ChildPath 'CopilotSessionStore.psm1') -Force

$script:BundleVersion = 1

# Child tables use INTEGER PRIMARY KEY AUTOINCREMENT, so their 'id' is dropped on export and
# reassigned by the target database. Their UNIQUE constraints still prevent duplicates.
$script:ChildTables = @(
    @{ Name = 'turns';                  DropId = $true }
    @{ Name = 'checkpoints';            DropId = $true }
    @{ Name = 'session_files';          DropId = $true }
    @{ Name = 'session_refs';           DropId = $true }
    @{ Name = 'assistant_usage_events'; DropId = $true }
    @{ Name = 'forge_trajectory_events'; DropId = $true }
    @{ Name = 'search_index';           DropId = $false }
)

$script:LeanExclusions = @('files', 'rewind-file-snapshots', 'rewind-snapshots')

# Captured at script scope: $PSBoundParameters inside a helper function refers to that function.
$script:ExportWindow = if ($PSBoundParameters.ContainsKey('Hours')) {
    [timespan]::FromHours($Hours)
} elseif ($PSBoundParameters.ContainsKey('Days')) {
    [timespan]::FromDays($Days)
} else {
    [timespan]::FromDays(1)
}

function Get-SchemaVersion {
    param([Parameter(Mandatory)] [string] $DatabasePath)

    $rows = Invoke-CopilotStoreQuery -DatabasePath $DatabasePath -Query 'SELECT version FROM schema_version LIMIT 1'
    if ($rows.Count -eq 0) { return 0 }
    return [int] $rows[0].version
}

function Copy-StateTree {
    param(
        [Parameter(Mandatory)] [string] $Source,
        [Parameter(Mandatory)] [string] $Destination,
        [string[]] $ExcludeDirectories = @()
    )

    $arguments = @($Source, $Destination, '/E', '/NFL', '/NDL', '/NJH', '/NJS', '/NP', '/R:1', '/W:1')
    if ($ExcludeDirectories.Count -gt 0) {
        $arguments += '/XD'
        foreach ($name in $ExcludeDirectories) { $arguments += (Join-Path -Path $Source -ChildPath $name) }
    }
    # Lock files must never travel: an imported session would look like it is already open.
    $arguments += @('/XF', 'inuse.*.lock')

    & robocopy.exe @arguments | Out-Null
    # Robocopy uses a bit field; anything below 8 means the copy succeeded.
    if ($LASTEXITCODE -ge 8) {
        throw "robocopy failed with exit code $LASTEXITCODE copying '$Source'."
    }
    $global:LASTEXITCODE = 0
}

function ConvertTo-MappedPath {
    param(
        [string] $Value,
        [AllowEmptyCollection()] [System.Collections.Generic.List[pscustomobject]] $Rules
    )

    if ([string]::IsNullOrWhiteSpace($Value)) { return $Value }
    foreach ($rule in $Rules) {
        if ($Value.StartsWith($rule.From, [StringComparison]::OrdinalIgnoreCase)) {
            return $rule.To + $Value.Substring($rule.From.Length)
        }
    }
    return $Value
}

function ConvertTo-PathRules {
    param([string[]] $Definitions)

    # A generic list never unrolls on return, unlike a plain array.
    $rules = [System.Collections.Generic.List[pscustomobject]]::new()
    foreach ($definition in $Definitions) {
        $index = $definition.IndexOf('=')
        if ($index -le 0 -or $index -eq $definition.Length - 1) {
            throw "Invalid -PathMap entry '$definition'. Use the form 'SOURCE=TARGET', e.g. 'D:\git=C:\src'."
        }
        $rules.Add([pscustomobject]@{
            From = $definition.Substring(0, $index).TrimEnd('\', '/')
            To   = $definition.Substring($index + 1).TrimEnd('\', '/')
        })
    }
    # Comma prefix stops PowerShell enumerating the list into the pipeline.
    return ,$rules
}

function Get-BundleLayout {
    param([Parameter(Mandatory)] [string] $BundlePath)

    $isArchive = [System.IO.Path]::GetExtension($BundlePath) -eq '.zip'
    return [pscustomobject]@{
        IsArchive = $isArchive
        Root      = $BundlePath
    }
}

function Invoke-Export {
    $copilotHomePath = Resolve-CopilotHome -Requested $CopilotHome
    $databasePath = Get-CopilotStorePath -CopilotHome $copilotHomePath -Require
    $stateRoot = Get-CopilotSessionStateRoot -CopilotHome $copilotHomePath -Require

    $window = $script:ExportWindow
    $cutoffUtc = [datetime]::UtcNow - $window
    Write-Verbose "Exporting sessions updated after $($cutoffUtc.ToString('u')) (window: $window)."

    $rows = Invoke-CopilotStoreQuery -DatabasePath $databasePath -Query @"
SELECT s.id AS id, s.cwd AS cwd, s.repository AS repository, s.branch AS branch,
       s.summary AS summary, s.updated_at AS updated_at,
       (SELECT COUNT(*) FROM turns t WHERE t.session_id = s.id) AS turn_count
FROM sessions s
WHERE substr(s.updated_at, 1, 10) >= '$($cutoffUtc.AddDays(-1).ToString('yyyy-MM-dd'))'
  AND EXISTS (SELECT 1 FROM turns t WHERE t.session_id = s.id)
ORDER BY s.updated_at DESC
"@

    $exclusions = @($ExcludeDirectory)
    if ($Lean) { $exclusions += $script:LeanExclusions }
    $exclusions = @($exclusions | Select-Object -Unique)

    $selected = [System.Collections.Generic.List[pscustomobject]]::new()
    foreach ($row in $rows) {
        $updated = ConvertTo-UtcTimestamp -Value $row.updated_at
        if (-not $updated -or $updated -lt $cutoffUtc) { continue }
        if ($Filter -and -not ($row.cwd -like $Filter -or $row.repository -like $Filter -or $row.summary -like $Filter)) {
            continue
        }

        $statePath = Join-Path -Path $stateRoot -ChildPath $row.id
        if (-not (Test-Path -LiteralPath $statePath -PathType Container)) {
            Write-Warning "Skipping session $($row.id): no session state directory."
            continue
        }

        $bytes = Get-DirectorySize -Path $statePath
        foreach ($name in $exclusions) {
            $bytes -= Get-DirectorySize -Path (Join-Path -Path $statePath -ChildPath $name)
        }
        if ($bytes -lt 0) { $bytes = 0 }

        $selected.Add([pscustomobject]@{
            Id         = $row.id
            Cwd        = $row.cwd
            Repository = $row.repository
            Branch     = $row.branch
            Summary    = $row.summary
            UpdatedUtc = $updated
            TurnCount  = [int] $row.turn_count
            Bytes      = $bytes
            StatePath  = $statePath
            InUse      = (Test-CopilotSessionInUse -SessionStatePath $statePath)
        })
    }

    if ($selected.Count -eq 0) {
        Write-Host "No non-empty sessions were updated in the last $window." -ForegroundColor Yellow
        return
    }

    $selected |
        Select-Object @{ N = 'Session'; E = { $_.Id.Substring(0, 8) } },
                      @{ N = 'Name'; E = { if ($_.Summary) { $_.Summary } else { '(unnamed)' } } },
                      @{ N = 'Directory'; E = { $_.Cwd } },
                      @{ N = 'Turns'; E = { $_.TurnCount } },
                      @{ N = 'Size'; E = { Format-ByteSize -Bytes $_.Bytes } } |
        Format-Table -AutoSize | Out-String | Write-Host

    $totalBytes = [long] (($selected | Measure-Object -Property Bytes -Sum).Sum)
    Write-Host ("{0} session(s), {1} to copy." -f $selected.Count, (Format-ByteSize -Bytes $totalBytes))
    if ($selected | Where-Object { $_.InUse }) {
        Write-Warning 'Some sessions are open right now; their transcripts may be captured mid-write.'
    }

    $layout = Get-BundleLayout -BundlePath $Path
    $workRoot = if ($layout.IsArchive) {
        Join-Path -Path ([System.IO.Path]::GetTempPath()) -ChildPath ("copilot-bundle-{0}" -f [guid]::NewGuid())
    } else {
        $Path
    }

    if (-not $PSCmdlet.ShouldProcess($Path, "Write bundle with $($selected.Count) session(s)")) { return }

    try {
        New-Item -ItemType Directory -Path $workRoot -Force | Out-Null

        $entries = [System.Collections.Generic.List[object]]::new()
        foreach ($session in $selected) {
            Write-Verbose "Exporting $($session.Id)."
            $sessionRoot = Join-Path -Path $workRoot -ChildPath "sessions\$($session.Id)"
            New-Item -ItemType Directory -Path $sessionRoot -Force | Out-Null

            $tables = [ordered]@{}
            $tables['sessions'] = @(Invoke-CopilotStoreQuery -DatabasePath $databasePath `
                -Query 'SELECT * FROM sessions WHERE id = ?' -Parameters @($session.Id))
            foreach ($table in $script:ChildTables) {
                $tableRows = @(Invoke-CopilotStoreQuery -DatabasePath $databasePath `
                    -Query "SELECT * FROM $($table.Name) WHERE session_id = ?" -Parameters @($session.Id))
                if ($table.DropId) {
                    $tableRows = @($tableRows | Select-Object -Property * -ExcludeProperty 'id')
                }
                $tables[$table.Name] = $tableRows
            }

            $rowsFile = Join-Path -Path $sessionRoot -ChildPath 'rows.json'
            ConvertTo-Json -InputObject $tables -Depth 8 -Compress |
                Set-Content -LiteralPath $rowsFile -Encoding utf8

            Copy-StateTree -Source $session.StatePath `
                -Destination (Join-Path -Path $sessionRoot -ChildPath 'state') `
                -ExcludeDirectories $exclusions

            $entries.Add([ordered]@{
                id         = $session.Id
                cwd        = $session.Cwd
                repository = $session.Repository
                branch     = $session.Branch
                summary    = $session.Summary
                updatedUtc = $session.UpdatedUtc.ToString('o')
                turnCount  = $session.TurnCount
                bytes      = $session.Bytes
            })
        }

        $manifest = [ordered]@{
            bundleVersion      = $script:BundleVersion
            schemaVersion      = Get-SchemaVersion -DatabasePath $databasePath
            createdUtc         = [datetime]::UtcNow.ToString('o')
            sourceMachine      = $env:COMPUTERNAME
            sourceCopilotHome  = $copilotHomePath
            lean               = [bool] $Lean
            excludedDirectories = @($exclusions)
            sessions           = @($entries)
        }
        ConvertTo-Json -InputObject $manifest -Depth 8 |
            Set-Content -LiteralPath (Join-Path -Path $workRoot -ChildPath 'manifest.json') -Encoding utf8

        if ($layout.IsArchive) {
            Write-Host 'Compressing bundle...'
            if (Test-Path -LiteralPath $Path) { Remove-Item -LiteralPath $Path -Force }
            Compress-Archive -Path (Join-Path -Path $workRoot -ChildPath '*') -DestinationPath $Path -CompressionLevel Optimal
        }

        $finalSize = if ($layout.IsArchive) { (Get-Item -LiteralPath $Path).Length } else { Get-DirectorySize -Path $Path }
        Write-Host ("Bundle written to {0} ({1})." -f $Path, (Format-ByteSize -Bytes $finalSize)) -ForegroundColor Green
    }
    finally {
        if ($layout.IsArchive -and (Test-Path -LiteralPath $workRoot)) {
            Remove-Item -LiteralPath $workRoot -Recurse -Force -ErrorAction SilentlyContinue
        }
    }
}

function Invoke-Import {
    $copilotHomePath = Resolve-CopilotHome -Requested $CopilotHome
    $databasePath = Get-CopilotStorePath -CopilotHome $copilotHomePath -Require
    $stateRoot = Get-CopilotSessionStateRoot -CopilotHome $copilotHomePath
    New-Item -ItemType Directory -Path $stateRoot -Force | Out-Null

    if (-not (Test-Path -LiteralPath $Path)) { throw "Bundle not found at '$Path'." }

    $layout = Get-BundleLayout -BundlePath $Path
    $bundleRoot = $Path
    $tempRoot = $null
    try {
        if ($layout.IsArchive) {
            $tempRoot = Join-Path -Path ([System.IO.Path]::GetTempPath()) -ChildPath ("copilot-bundle-{0}" -f [guid]::NewGuid())
            Write-Verbose "Expanding archive into $tempRoot."
            Expand-Archive -LiteralPath $Path -DestinationPath $tempRoot -Force
            $bundleRoot = $tempRoot
        }

        $manifestFile = Join-Path -Path $bundleRoot -ChildPath 'manifest.json'
        if (-not (Test-Path -LiteralPath $manifestFile)) { throw "'$Path' is not a Copilot session bundle (no manifest.json)." }
        $manifest = Get-Content -LiteralPath $manifestFile -Raw | ConvertFrom-Json

        if ($manifest.bundleVersion -gt $script:BundleVersion) {
            throw "Bundle version $($manifest.bundleVersion) is newer than this script supports ($($script:BundleVersion))."
        }
        $localSchema = Get-SchemaVersion -DatabasePath $databasePath
        if ($manifest.schemaVersion -ne $localSchema -and -not $Force) {
            throw ("Bundle was created against session store schema $($manifest.schemaVersion) but this machine is on " +
                   "$localSchema. Re-run with -Force to import anyway.")
        }

        $rules = ConvertTo-PathRules -Definitions $PathMap
        $existing = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
        foreach ($row in (Invoke-CopilotStoreQuery -DatabasePath $databasePath -Query 'SELECT id FROM sessions')) {
            [void] $existing.Add($row.id)
        }

        $imported = 0
        $skippedCount = 0
        foreach ($entry in $manifest.sessions) {
            if ($Filter -and -not ($entry.cwd -like $Filter -or $entry.repository -like $Filter -or $entry.summary -like $Filter)) {
                continue
            }

            $sessionRoot = Join-Path -Path $bundleRoot -ChildPath "sessions\$($entry.id)"
            $rowsFile = Join-Path -Path $sessionRoot -ChildPath 'rows.json'
            if (-not (Test-Path -LiteralPath $rowsFile)) {
                Write-Warning "Skipping $($entry.id): rows.json missing from the bundle."
                continue
            }

            $targetState = Join-Path -Path $stateRoot -ChildPath $entry.id
            $alreadyPresent = $existing.Contains($entry.id) -or (Test-Path -LiteralPath $targetState)
            if ($alreadyPresent -and -not $Overwrite) {
                Write-Verbose "Skipping $($entry.id): already present. Use -Overwrite to replace it."
                $skippedCount++
                continue
            }
            if ($alreadyPresent -and (Test-CopilotSessionInUse -SessionStatePath $targetState)) {
                Write-Warning "Skipping $($entry.id): the existing session is open in another terminal."
                $skippedCount++
                continue
            }

            $mappedCwd = ConvertTo-MappedPath -Value $entry.cwd -Rules $rules
            $target = "{0} [{1}]" -f $entry.id, $mappedCwd
            if (-not $PSCmdlet.ShouldProcess($target, 'Import Copilot session')) { continue }

            if ($mappedCwd -and -not (Test-Path -LiteralPath $mappedCwd -PathType Container)) {
                Write-Warning "Session $($entry.id) points at '$mappedCwd', which does not exist here. Add a -PathMap rule if that is wrong."
            }

            $tables = Get-Content -LiteralPath $rowsFile -Raw | ConvertFrom-Json
            $statements = [System.Collections.Generic.List[object]]::new()

            if ($alreadyPresent) {
                foreach ($table in $script:ChildTables) {
                    $statements.Add([pscustomobject]@{
                        Sql = "DELETE FROM $($table.Name) WHERE session_id = ?"; Parameters = @($entry.id)
                    })
                }
                $statements.Add([pscustomobject]@{ Sql = 'DELETE FROM sessions WHERE id = ?'; Parameters = @($entry.id) })
            }

            foreach ($tableName in @('sessions') + @($script:ChildTables | ForEach-Object { $_.Name })) {
                if (-not $tables.PSObject.Properties[$tableName]) { continue }
                foreach ($row in @($tables.$tableName)) {
                    if (-not $row) { continue }
                    $columns = @($row.PSObject.Properties.Name)
                    if ($columns.Count -eq 0) { continue }

                    $values = foreach ($column in $columns) {
                        $value = $row.$column
                        switch ($column) {
                            'cwd'       { ConvertTo-MappedPath -Value $value -Rules $rules }
                            'file_path' { ConvertTo-MappedPath -Value $value -Rules $rules }
                            default     { $value }
                        }
                    }

                    $placeholders = (@('?') * $columns.Count) -join ', '
                    $columnList = ($columns | ForEach-Object { '"' + $_ + '"' }) -join ', '
                    $statements.Add([pscustomobject]@{
                        Sql        = "INSERT INTO $tableName ($columnList) VALUES ($placeholders)"
                        Parameters = @($values)
                    })
                }
            }

            [void] (Invoke-CopilotStoreCommand -DatabasePath $databasePath -Statement $statements.ToArray())

            $sourceState = Join-Path -Path $sessionRoot -ChildPath 'state'
            if (Test-Path -LiteralPath $sourceState -PathType Container) {
                if ($alreadyPresent -and (Test-Path -LiteralPath $targetState)) {
                    Remove-Item -LiteralPath $targetState -Recurse -Force
                }
                Copy-StateTree -Source $sourceState -Destination $targetState
                Update-WorkspaceFile -StatePath $targetState -Rules $rules
            }

            $imported++
        }

        Write-Host ("Imported {0} session(s); skipped {1}." -f $imported, $skippedCount) -ForegroundColor Green
        if ($imported -gt 0) {
            Write-Host 'Run Resume-CopilotSessions.ps1 to reopen them.'
        }
    }
    finally {
        if ($tempRoot -and (Test-Path -LiteralPath $tempRoot)) {
            Remove-Item -LiteralPath $tempRoot -Recurse -Force -ErrorAction SilentlyContinue
        }
    }
}

function Update-WorkspaceFile {
    param(
        [Parameter(Mandatory)] [string] $StatePath,
        [AllowEmptyCollection()] [System.Collections.Generic.List[pscustomobject]] $Rules
    )

    if ($Rules.Count -eq 0) { return }

    $file = Join-Path -Path $StatePath -ChildPath 'workspace.yaml'
    if (-not (Test-Path -LiteralPath $file -PathType Leaf)) { return }

    $lines = Get-Content -LiteralPath $file
    $updated = foreach ($line in $lines) {
        if ($line -match '^(\s*(?:cwd|git_root):\s*)(.+)$') {
            $Matches[1] + (ConvertTo-MappedPath -Value $Matches[2].Trim() -Rules $Rules)
        } else {
            $line
        }
    }
    Set-Content -LiteralPath $file -Value $updated -Encoding utf8
}

if ($Export) { Invoke-Export } else { Invoke-Import }
