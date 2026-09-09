<#
.SYNOPSIS
    Interactively removes GitHub Copilot CLI sessions older than a given age.

.DESCRIPTION
    Unlike Remove-EmptyCopilotSessions.ps1, this script targets *every* session past the age
    threshold, including sessions that recorded turns. It is therefore always interactive by default:

      1. All sessions last updated before the cutoff are collected, together with the size of their
         session-state directory.
      2. A checklist is shown with every candidate pre-selected. Deselect the ones you want to keep.
         The footer shows a live count and the state-directory space the current selection frees.
      3. Enter removes the still-selected sessions: their rows in session-store.db and their
         session-state directories.

    Sessions currently open in another terminal are never offered, and neither is anything newer than
    the age threshold. Sessions holding a plan.md are also skipped unless -IncludePlanned is passed.

    Note that the reported size only covers the session-state directory tree. Rows removed from
    session-store.db free space inside the database file, which SQLite reuses rather than returns to
    the file system, so that is not counted.

.PARAMETER Hours
    Remove sessions last updated more than this many hours ago. Mutually exclusive with -Days.

.PARAMETER Days
    Remove sessions last updated more than this many days ago. Defaults to 30 days.

.PARAMETER CopilotHome
    Copilot configuration directory. Defaults to $env:COPILOT_HOME, then "$HOME\.copilot".

.PARAMETER Filter
    Optional wildcard pattern matched against the session working directory, repository and summary.

.PARAMETER IncludePlanned
    Also offer sessions whose state directory contains a plan.md. Off by default.

.PARAMETER Recycle
    Send session-state directories to the Recycle Bin instead of deleting them permanently.

.PARAMETER Force
    Skip the checklist and the confirmation prompt, and remove every candidate. Intended for
    unattended use; combine with -WhatIf first.

.EXAMPLE
    .\Remove-OldCopilotSessions.ps1 -Days 30 -WhatIf

    List the sessions older than 30 days and the space they occupy, without deleting anything.

.EXAMPLE
    .\Remove-OldCopilotSessions.ps1 -Days 14

    Show the checklist of sessions older than two weeks, deselect the ones worth keeping, then remove
    the rest.

.EXAMPLE
    .\Remove-OldCopilotSessions.ps1 -Hours 6 -Filter '*scratch*' -Recycle -Force

    Unattended purge of matching sessions older than six hours, to the Recycle Bin.

.NOTES
    Requires PowerShell 7 and a SQLite reader (python or sqlite3.exe) on PATH. The checklist needs an
    attached console; use -Force when input is redirected.
#>
#Requires -Version 7.0
# Write-Host is deliberate: the checklist and the reclaimed-space summary are for the operator.
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
    [double] $Days = 30,

    [ValidateNotNullOrEmpty()]
    [string] $CopilotHome,

    [ValidateNotNullOrEmpty()]
    [string] $Filter,

    [switch] $IncludePlanned,

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

function Get-TotalByte {
    <#
    .SYNOPSIS
        Sums the Bytes property of a candidate set, returning 0 for an empty set.
    #>
    [OutputType([long])]
    param([object[]] $Candidate)

    if (-not $Candidate -or $Candidate.Count -eq 0) { return [long] 0 }
    return [long] (($Candidate | Measure-Object -Property Bytes -Sum).Sum)
}

function ConvertTo-FixedWidthText {
    param(
        [string] $Text,
        [int] $Width
    )

    if ($Width -le 0) { return '' }
    $singleLine = $Text -replace '[\r\n\t]+', ' '
    if ($singleLine.Length -gt $Width) {
        if ($Width -le 3) { return $singleLine.Substring(0, $Width) }
        return $singleLine.Substring(0, $Width - 3) + '...'
    }
    return $singleLine.PadRight($Width)
}

function Write-MenuLine {
    param(
        [int] $Row,
        [int] $Width,
        [string] $Text,
        [switch] $Highlighted
    )

    [Console]::SetCursorPosition(0, $Row)
    $foreground = [Console]::ForegroundColor
    $background = [Console]::BackgroundColor
    if ($Highlighted) {
        [Console]::ForegroundColor = [ConsoleColor]::Black
        [Console]::BackgroundColor = [ConsoleColor]::Gray
    }
    [Console]::Write((ConvertTo-FixedWidthText -Text $Text -Width $Width))
    if ($Highlighted) {
        [Console]::ForegroundColor = $foreground
        [Console]::BackgroundColor = $background
    }
}

function Format-CandidateLine {
    param([Parameter(Mandatory)] [pscustomobject] $Candidate)

    $mark = if ($Candidate.Selected) { '[x]' } else { '[ ]' }
    $updated = if ($Candidate.UpdatedUtc) {
        $Candidate.UpdatedUtc.ToLocalTime().ToString('yyyy-MM-dd HH:mm')
    } else {
        '     (unknown)  '
    }
    return "{0} {1}  {2,10}  {3}  [{4}]" -f $mark, $updated,
        (Format-ByteSize -Bytes $Candidate.Bytes), $Candidate.Label, $Candidate.Cwd
}

function Select-SessionToRemove {
    <#
    .SYNOPSIS
        Shows the candidate checklist. Returns an object with Cancelled and Selected.
    #>
    param([Parameter(Mandatory)] [object[]] $Candidate)

    if ([Console]::IsInputRedirected -or [Console]::IsOutputRedirected) {
        throw 'The session checklist requires an attached console. Re-run with -Force to skip it.'
    }
    if ([Console]::WindowHeight -lt 7 -or [Console]::WindowWidth -lt 40) {
        throw 'The console is too small for the session checklist. Resize it and try again.'
    }

    $selectedIndex = 0
    $topIndex = 0
    $escape = [char] 27
    $supportsVirtualTerminal = $Host.UI.PSObject.Properties.Name -contains 'SupportsVirtualTerminal' -and
        $Host.UI.SupportsVirtualTerminal
    $alternateBuffer = $false
    $originalCursorVisible = [Console]::CursorVisible
    $originalForeground = [Console]::ForegroundColor
    $originalBackground = [Console]::BackgroundColor
    $totalBytes = Get-TotalByte -Candidate $Candidate

    try {
        if ($supportsVirtualTerminal) {
            [Console]::Write("$escape[?1049h")
            $alternateBuffer = $true
        } else {
            Clear-Host
        }
        [Console]::CursorVisible = $false

        while ($true) {
            $height = [Console]::WindowHeight
            $width = [Math]::Max(1, [Console]::WindowWidth - 1)
            if ($height -lt 7 -or $width -lt 39) {
                throw 'The console became too small for the session checklist. Resize it and try again.'
            }
            $pageSize = [Math]::Max(1, $height - 5)

            if ($selectedIndex -lt $topIndex) {
                $topIndex = $selectedIndex
            } elseif ($selectedIndex -ge $topIndex + $pageSize) {
                $topIndex = $selectedIndex - $pageSize + 1
            }

            $checked = @($Candidate | Where-Object { $_.Selected })
            $checkedBytes = Get-TotalByte -Candidate $checked

            Write-MenuLine -Row 0 -Width $width -Text ("Sessions older than {0} - {1} candidate(s), {2} on disk" -f `
                $script:WindowText, $Candidate.Count, (Format-ByteSize -Bytes $totalBytes))
            Write-MenuLine -Row 1 -Width $width -Text 'Space: keep/remove  A: all  N: none  I: invert  Enter: remove checked  Esc: cancel'
            Write-MenuLine -Row 2 -Width $width -Text ''

            for ($row = 0; $row -lt $pageSize; $row++) {
                $index = $topIndex + $row
                $text = ''
                if ($index -lt $Candidate.Count) {
                    $text = Format-CandidateLine -Candidate $Candidate[$index]
                }
                Write-MenuLine -Row (3 + $row) -Width $width -Text $text -Highlighted:($index -eq $selectedIndex)
            }

            $footer = "{0}/{1}   removing {2} session(s), freeing {3}" -f ($selectedIndex + 1), $Candidate.Count,
                $checked.Count, (Format-ByteSize -Bytes $checkedBytes)
            Write-MenuLine -Row ($height - 1) -Width $width -Text $footer

            $key = [Console]::ReadKey($true)
            if ($key.Key -eq [ConsoleKey]::C -and
                ($key.Modifiers -band [ConsoleModifiers]::Control) -ne 0) {
                return [pscustomobject]@{ Cancelled = $true; Selected = @() }
            }

            switch ($key.Key) {
                ([ConsoleKey]::UpArrow) {
                    if ($selectedIndex -gt 0) { $selectedIndex-- }
                }
                ([ConsoleKey]::DownArrow) {
                    if ($selectedIndex -lt $Candidate.Count - 1) { $selectedIndex++ }
                }
                ([ConsoleKey]::PageUp) {
                    $selectedIndex = [Math]::Max(0, $selectedIndex - $pageSize)
                }
                ([ConsoleKey]::PageDown) {
                    $selectedIndex = [Math]::Min($Candidate.Count - 1, $selectedIndex + $pageSize)
                }
                ([ConsoleKey]::Home) { $selectedIndex = 0 }
                ([ConsoleKey]::End) { $selectedIndex = $Candidate.Count - 1 }
                ([ConsoleKey]::Spacebar) {
                    $item = $Candidate[$selectedIndex]
                    $item.Selected = -not $item.Selected
                    if ($selectedIndex -lt $Candidate.Count - 1) { $selectedIndex++ }
                }
                ([ConsoleKey]::A) {
                    foreach ($item in $Candidate) { $item.Selected = $true }
                }
                ([ConsoleKey]::N) {
                    foreach ($item in $Candidate) { $item.Selected = $false }
                }
                ([ConsoleKey]::I) {
                    foreach ($item in $Candidate) { $item.Selected = -not $item.Selected }
                }
                ([ConsoleKey]::Enter) {
                    return [pscustomobject]@{
                        Cancelled = $false
                        Selected  = @($Candidate | Where-Object { $_.Selected })
                    }
                }
                ([ConsoleKey]::Escape) {
                    return [pscustomobject]@{ Cancelled = $true; Selected = @() }
                }
            }
        }
    }
    finally {
        [Console]::ForegroundColor = $originalForeground
        [Console]::BackgroundColor = $originalBackground
        [Console]::CursorVisible = $originalCursorVisible
        if ($alternateBuffer) {
            [Console]::Write("$escape[?1049l")
        } else {
            Clear-Host
        }
    }
}

$copilotHomePath = Resolve-CopilotHome -Requested $CopilotHome
$databasePath = Get-CopilotStorePath -CopilotHome $copilotHomePath -Require
$stateRoot = Get-CopilotSessionStateRoot -CopilotHome $copilotHomePath

$window = if ($PSCmdlet.ParameterSetName -eq 'Hours') {
    [timespan]::FromHours($Hours)
} else {
    [timespan]::FromDays($Days)
}
$script:WindowText = $window.ToString()
$cutoffUtc = [datetime]::UtcNow - $window
Write-Verbose "Collecting sessions last updated before $($cutoffUtc.ToString('u')) (age threshold: $window)."

$sessionRows = Invoke-CopilotStoreQuery -DatabasePath $databasePath -Query @'
SELECT s.id AS id,
       s.cwd AS cwd,
       s.repository AS repository,
       s.summary AS summary,
       s.updated_at AS updated_at,
       (SELECT COUNT(*) FROM turns t WHERE t.session_id = s.id) AS turn_count
FROM sessions s
'@

$stateDirs = @{}
if (Test-Path -LiteralPath $stateRoot -PathType Container) {
    foreach ($dir in (Get-ChildItem -LiteralPath $stateRoot -Directory -Force -ErrorAction SilentlyContinue)) {
        $stateDirs[$dir.Name] = $dir.FullName
    }
}

$candidates = [System.Collections.Generic.List[pscustomobject]]::new()
$skipped = @{ InUse = 0; TooRecent = 0; Planned = 0; Filtered = 0 }

foreach ($row in $sessionRows) {
    $updated = ConvertTo-UtcTimestamp -Value $row.updated_at
    if ($updated -and $updated -ge $cutoffUtc) { $skipped.TooRecent++; continue }

    $cwd = if ($row.cwd) { [string] $row.cwd } else { '' }
    $repository = if ($row.repository) { [string] $row.repository } else { '' }
    $summary = if ($row.summary) { [string] $row.summary } else { '' }

    if ($Filter) {
        $haystack = @($cwd, $repository, $summary) | Where-Object { $_ }
        if (-not ($haystack | Where-Object { $_ -like $Filter })) { $skipped.Filtered++; continue }
    }

    $statePath = if ($stateDirs.ContainsKey($row.id)) { $stateDirs[$row.id] } else { $null }

    if ($statePath -and -not $IncludePlanned -and
        (Test-Path -LiteralPath (Join-Path $statePath 'plan.md') -PathType Leaf)) {
        $skipped.Planned++
        Write-Verbose "Keeping session $($row.id): protected by plan.md."
        continue
    }
    if ($statePath -and (Test-CopilotSessionInUse -SessionStatePath $statePath)) {
        $skipped.InUse++
        Write-Verbose "Keeping session $($row.id): currently open in another terminal."
        continue
    }

    $label = if ([string]::IsNullOrWhiteSpace($summary)) {
        if ([string]::IsNullOrWhiteSpace($repository)) { '(unnamed)' } else { $repository }
    } else {
        $summary
    }

    $candidates.Add([pscustomobject]@{
        Id         = [string] $row.id
        Label      = $label
        Cwd        = $cwd
        Turns      = [int] $row.turn_count
        StatePath  = $statePath
        UpdatedUtc = $updated
        Bytes      = if ($statePath) { Get-DirectorySize -Path $statePath } else { [long] 0 }
        Selected   = $true
    })
}

$candidates = [pscustomobject[]] @($candidates | Sort-Object -Property Bytes -Descending)

Write-Host ''
Write-Host ("Sessions older than {0}: {1}   State-directory space: {2}" -f $window, $candidates.Count,
    (Format-ByteSize -Bytes (Get-TotalByte -Candidate $candidates)))
Write-Host ("Kept: {0} newer than the threshold, {1} protected by plan.md, {2} in use, {3} filtered out" -f `
    $skipped.TooRecent, $skipped.Planned, $skipped.InUse, $skipped.Filtered)
Write-Host ''

if ($candidates.Count -eq 0) {
    Write-Host 'Nothing to remove.' -ForegroundColor Green
    return
}

$selection = $candidates
if (-not $Force -and -not $WhatIfPreference) {
    $choice = Select-SessionToRemove -Candidate $candidates
    if ($choice.Cancelled) {
        Write-Host 'Cancelled. Nothing was removed.'
        return
    }
    $selection = @($choice.Selected)
    if ($selection.Count -eq 0) {
        Write-Host 'No sessions were left selected. Nothing was removed.'
        return
    }
    # Enter in the checklist is the confirmation; do not prompt again for every session.
    $ConfirmPreference = 'None'
}

$selectedBytes = Get-TotalByte -Candidate $selection
$selection |
    Select-Object -Property @{ Name = 'Id'; Expression = { $_.Id.Substring(0, 8) } },
        @{ Name = 'Updated'; Expression = { if ($_.UpdatedUtc) { $_.UpdatedUtc.ToLocalTime().ToString('yyyy-MM-dd HH:mm') } else { '' } } },
        Turns,
        @{ Name = 'Size'; Expression = { Format-ByteSize -Bytes $_.Bytes } },
        Label |
    Format-Table -AutoSize | Out-String | Write-Host
Write-Host ("Selected: {0} session(s), freeing {1} of session state." -f $selection.Count,
    (Format-ByteSize -Bytes $selectedBytes))
Write-Host ''

if ($Force -and -not $WhatIfPreference) {
    $ConfirmPreference = 'None'
}

$removedBytes = [long] 0
$removedCount = 0
$failed = 0

foreach ($candidate in $selection) {
    $target = "{0} [{1}, {2} turn(s), {3}]" -f $candidate.Id, $candidate.Label, $candidate.Turns,
        (Format-ByteSize -Bytes $candidate.Bytes)
    $action = if ($Recycle) { 'Recycle Copilot session state' } else { 'Delete Copilot session state' }

    if (-not $PSCmdlet.ShouldProcess($target, $action)) { continue }

    try {
        $statements = foreach ($table in $script:SessionChildTables) {
            [pscustomobject]@{ Sql = "DELETE FROM $table WHERE session_id = ?"; Parameters = @($candidate.Id) }
        }
        $statements += [pscustomobject]@{ Sql = 'DELETE FROM sessions WHERE id = ?'; Parameters = @($candidate.Id) }
        [void] (Invoke-CopilotStoreCommand -DatabasePath $databasePath -Statement $statements)

        if ($candidate.StatePath -and (Test-Path -LiteralPath $candidate.StatePath)) {
            Remove-SessionDirectory -Path $candidate.StatePath -ToRecycleBin:$Recycle
        }

        $removedBytes += $candidate.Bytes
        $removedCount++
    }
    catch {
        $failed++
        Write-Warning "Failed to remove $($candidate.Id): $($_.Exception.Message)"
    }
}

if ($removedCount -gt 0) {
    $verb = if ($Recycle) { 'Recycled' } else { 'Deleted' }
    Write-Host ("{0} {1} session(s), reclaiming {2}." -f $verb, $removedCount, (Format-ByteSize -Bytes $removedBytes)) -ForegroundColor Green
}
if ($failed -gt 0) {
    Write-Warning "$failed session(s) could not be removed."
}
