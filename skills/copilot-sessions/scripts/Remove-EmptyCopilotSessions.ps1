<#
.SYNOPSIS
    Purges empty and orphaned GitHub Copilot CLI session state.

.DESCRIPTION
    The Copilot CLI accumulates two kinds of dead session state:

      * Empty sessions - rows in session-store.db that never recorded a turn. They reclaim almost no
        disk but clutter the /resume picker.
      * Orphaned state directories - folders under session-state\ with no matching database row.
        These cannot appear in /resume at all, yet they are usually where the disk has gone, because
        they still hold the agent artifacts written under files\.

    A session is only ever considered empty when it has no recorded turns. A plan.md always protects
    a session that still exists in the database. Orphans are purged even when they have a plan.md,
    because without a database row they are unreachable; pass -ProtectOrphansWithPlan to keep them.

    Sessions currently open in another terminal are never touched, and neither is anything newer than
    the age threshold.

.PARAMETER Hours
    Only purge sessions last updated more than this many hours ago. Mutually exclusive with -Days.

.PARAMETER Days
    Only purge sessions last updated more than this many days ago. Defaults to 1 day, matching
    Resume-CopilotSessions.ps1.

.PARAMETER Scope
    Which populations to consider: All (default), Sessions (database rows only) or Orphans
    (directories with no database row only).

.PARAMETER ProtectOrphansWithPlan
    Keep orphaned directories that contain a plan.md. Off by default, because those directories hold
    the bulk of the reclaimable disk and cannot be resumed.

.PARAMETER CopilotHome
    Copilot configuration directory. Defaults to $env:COPILOT_HOME, then "$HOME\.copilot".

.PARAMETER Recycle
    Send directories to the Recycle Bin instead of deleting them permanently.

.PARAMETER Force
    Do not prompt for confirmation.

.EXAMPLE
    .\Remove-EmptyCopilotSessions.ps1 -WhatIf

    Show what would be purged without deleting anything. Always do this first.

.EXAMPLE
    .\Remove-EmptyCopilotSessions.ps1 -Days 7 -Recycle

    Purge sessions untouched for a week, sending the directories to the Recycle Bin.

.EXAMPLE
    .\Remove-EmptyCopilotSessions.ps1 -Scope Sessions -ProtectOrphansWithPlan

    Only tidy the /resume picker, leaving every orphaned directory in place.

.NOTES
    Requires PowerShell 7 and a SQLite reader (python or sqlite3.exe) on PATH.
#>
#Requires -Version 7.0
# Write-Host is deliberate: the preview tables and reclaimed-space summary are for the operator.
# Remove-SessionDirectory is an internal helper invoked underneath this script's own ShouldProcess.
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '')]
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseShouldProcessForStateChangingFunctions', '')]
[CmdletBinding(SupportsShouldProcess, ConfirmImpact = 'High', DefaultParameterSetName = 'Days')]
param(
    [Parameter(ParameterSetName = 'Hours')]
    [ValidateRange(0.0, 100000.0)]
    [double] $Hours,

    [Parameter(ParameterSetName = 'Days')]
    [ValidateRange(0.0, 10000.0)]
    [double] $Days = 1,

    [ValidateSet('All', 'Sessions', 'Orphans')]
    [string] $Scope = 'All',

    [switch] $ProtectOrphansWithPlan,

    [ValidateNotNullOrEmpty()]
    [string] $CopilotHome,

    [switch] $Recycle,

    [switch] $Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Import-Module -Name (Join-Path -Path $PSScriptRoot -ChildPath 'CopilotSessionStore.psm1') -Force

# Every table in session-store.db that is keyed by session_id. Children are cleared before the
# sessions row so a foreign key never dangles mid-transaction.
$script:SessionChildTables = @(
    'turns'
    'checkpoints'
    'session_files'
    'session_refs'
    'assistant_usage_events'
    'forge_trajectory_events'
    'search_index'
)

function Remove-SessionDirectory {
    param(
        [Parameter(Mandatory)] [string] $Path,
        [switch] $ToRecycleBin
    )

    if ($ToRecycleBin) {
        Add-Type -AssemblyName Microsoft.VisualBasic
        [Microsoft.VisualBasic.FileIO.FileSystem]::DeleteDirectory(
            $Path,
            [Microsoft.VisualBasic.FileIO.UIOption]::OnlyErrorDialogs,
            [Microsoft.VisualBasic.FileIO.RecycleOption]::SendToRecycleBin)
        return
    }
    Remove-Item -LiteralPath $Path -Recurse -Force -ErrorAction Stop
}

$copilotHomePath = Resolve-CopilotHome -Requested $CopilotHome
$databasePath = Get-CopilotStorePath -CopilotHome $copilotHomePath -Require
$stateRoot = Get-CopilotSessionStateRoot -CopilotHome $copilotHomePath

$window = if ($PSCmdlet.ParameterSetName -eq 'Hours') {
    [timespan]::FromHours($Hours)
} else {
    [timespan]::FromDays($Days)
}
$cutoffUtc = [datetime]::UtcNow - $window
Write-Verbose "Purging sessions last updated before $($cutoffUtc.ToString('u')) (age threshold: $window)."

$sessionRows = Invoke-CopilotStoreQuery -DatabasePath $databasePath -Query @'
SELECT s.id AS id,
       s.cwd AS cwd,
       s.summary AS summary,
       s.updated_at AS updated_at,
       (SELECT COUNT(*) FROM turns t WHERE t.session_id = s.id) AS turn_count
FROM sessions s
'@

$knownIds = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
foreach ($row in $sessionRows) { [void] $knownIds.Add($row.id) }

$stateDirs = @{}
if (Test-Path -LiteralPath $stateRoot -PathType Container) {
    foreach ($dir in (Get-ChildItem -LiteralPath $stateRoot -Directory -Force -ErrorAction SilentlyContinue)) {
        $stateDirs[$dir.Name] = $dir.FullName
    }
}
Write-Verbose "Found $($sessionRows.Count) database session(s) and $($stateDirs.Count) state directory(ies)."

$candidates = [System.Collections.Generic.List[pscustomobject]]::new()
$skipped = @{ InUse = 0; TooRecent = 0; HasTurns = 0; ProtectedByPlan = 0; OutOfScope = 0 }

function Add-Candidate {
    param(
        [Parameter(Mandatory)] [string] $Id,
        [Parameter(Mandatory)] [string] $Kind,
        [string] $StatePath,
        [string] $Label,
        [nullable[datetime]] $UpdatedUtc,
        [bool] $HasRow
    )

    $bytes = if ($StatePath) { Get-DirectorySize -Path $StatePath } else { [long] 0 }
    $candidates.Add([pscustomobject]@{
        Id         = $Id
        Kind       = $Kind
        StatePath  = $StatePath
        Label      = $Label
        UpdatedUtc = $UpdatedUtc
        HasRow     = $HasRow
        Bytes      = $bytes
    })
}

foreach ($row in $sessionRows) {
    if ($Scope -eq 'Orphans') { $skipped.OutOfScope++; continue }

    if ($row.turn_count -ge 1) { $skipped.HasTurns++; continue }

    $statePath = if ($stateDirs.ContainsKey($row.id)) { $stateDirs[$row.id] } else { $null }

    if ($statePath -and (Test-Path -LiteralPath (Join-Path $statePath 'plan.md') -PathType Leaf)) {
        $skipped.ProtectedByPlan++
        Write-Verbose "Keeping empty session $($row.id): protected by plan.md."
        continue
    }
    if ($statePath -and (Test-CopilotSessionInUse -SessionStatePath $statePath)) {
        $skipped.InUse++
        Write-Verbose "Keeping session $($row.id): currently open in another terminal."
        continue
    }

    $updated = ConvertTo-UtcTimestamp -Value $row.updated_at
    if ($updated -and $updated -ge $cutoffUtc) { $skipped.TooRecent++; continue }

    $label = if ([string]::IsNullOrWhiteSpace($row.summary)) { '(unnamed)' } else { $row.summary }
    Add-Candidate -Id $row.id -Kind 'EmptySession' -StatePath $statePath -Label $label `
        -UpdatedUtc $updated -HasRow $true
}

foreach ($entry in $stateDirs.GetEnumerator()) {
    if ($knownIds.Contains($entry.Key)) { continue }
    if ($Scope -eq 'Sessions') { $skipped.OutOfScope++; continue }

    $statePath = $entry.Value

    if ($ProtectOrphansWithPlan -and (Test-Path -LiteralPath (Join-Path $statePath 'plan.md') -PathType Leaf)) {
        $skipped.ProtectedByPlan++
        Write-Verbose "Keeping orphan $($entry.Key): protected by plan.md."
        continue
    }
    if (Test-CopilotSessionInUse -SessionStatePath $statePath) {
        $skipped.InUse++
        Write-Verbose "Keeping orphan $($entry.Key): currently open in another terminal."
        continue
    }

    $workspace = Get-CopilotWorkspaceInfo -SessionStatePath $statePath
    $updated = $null
    $label = '(orphan)'
    if ($workspace) {
        if ($workspace.ContainsKey('updated_at')) { $updated = ConvertTo-UtcTimestamp -Value $workspace['updated_at'] }
        if ($workspace.ContainsKey('name') -and -not [string]::IsNullOrWhiteSpace($workspace['name'])) {
            $label = $workspace['name']
        }
    }
    if (-not $updated) {
        $updated = (Get-Item -LiteralPath $statePath -Force).LastWriteTimeUtc
    }
    if ($updated -ge $cutoffUtc) { $skipped.TooRecent++; continue }

    Add-Candidate -Id $entry.Key -Kind 'Orphan' -StatePath $statePath -Label $label `
        -UpdatedUtc $updated -HasRow $false
}

$summary = $candidates | Group-Object -Property Kind | ForEach-Object {
    [pscustomobject]@{
        Category = $_.Name
        Count    = $_.Count
        Size     = Format-ByteSize -Bytes ([long] (($_.Group | Measure-Object -Property Bytes -Sum).Sum))
    }
}

Write-Host ''
if ($summary) {
    $summary | Format-Table -AutoSize | Out-String | Write-Host
} else {
    Write-Host 'Nothing to purge.' -ForegroundColor Green
}

$totalBytes = [long] (($candidates | Measure-Object -Property Bytes -Sum).Sum)
Write-Host ("Candidates: {0}   Reclaimable: {1}" -f $candidates.Count, (Format-ByteSize -Bytes $totalBytes))
Write-Host ("Kept: {0} with turns, {1} protected by plan.md, {2} in use, {3} newer than {4}, {5} out of scope" -f `
    $skipped.HasTurns, $skipped.ProtectedByPlan, $skipped.InUse, $skipped.TooRecent, $window, $skipped.OutOfScope)
Write-Host ''

if ($candidates.Count -eq 0) { return }

$largest = $candidates | Where-Object { $_.Bytes -gt 0 } | Sort-Object -Property Bytes -Descending | Select-Object -First 10
if ($largest) {
    Write-Verbose 'Largest candidates:'
    foreach ($item in $largest) {
        Write-Verbose ("  {0}  {1,10}  {2}" -f $item.Id.Substring(0, 8), (Format-ByteSize -Bytes $item.Bytes), $item.Label)
    }
}

if ($Force -and -not $WhatIfPreference) {
    $ConfirmPreference = 'None'
}

$removedBytes = [long] 0
$removedCount = 0
$failed = 0

foreach ($candidate in $candidates) {
    $target = "{0} [{1}, {2}, {3}]" -f $candidate.Id, $candidate.Kind, $candidate.Label,
        (Format-ByteSize -Bytes $candidate.Bytes)
    $action = if ($Recycle) { 'Recycle Copilot session state' } else { 'Delete Copilot session state' }

    if (-not $PSCmdlet.ShouldProcess($target, $action)) { continue }

    try {
        if ($candidate.HasRow) {
            $statements = foreach ($table in $script:SessionChildTables) {
                [pscustomobject]@{ Sql = "DELETE FROM $table WHERE session_id = ?"; Parameters = @($candidate.Id) }
            }
            $statements += [pscustomobject]@{ Sql = 'DELETE FROM sessions WHERE id = ?'; Parameters = @($candidate.Id) }
            [void] (Invoke-CopilotStoreCommand -DatabasePath $databasePath -Statement $statements)
        }

        if ($candidate.StatePath -and (Test-Path -LiteralPath $candidate.StatePath)) {
            Remove-SessionDirectory -Path $candidate.StatePath -ToRecycleBin:$Recycle
        }

        $removedBytes += $candidate.Bytes
        $removedCount++
    }
    catch {
        $failed++
        Write-Warning "Failed to purge $($candidate.Id): $($_.Exception.Message)"
    }
}

if ($removedCount -gt 0) {
    $verb = if ($Recycle) { 'Recycled' } else { 'Deleted' }
    Write-Host ("{0} {1} session(s), reclaiming {2}." -f $verb, $removedCount, (Format-ByteSize -Bytes $removedBytes)) -ForegroundColor Green
}
if ($failed -gt 0) {
    Write-Warning "$failed session(s) could not be purged."
}
