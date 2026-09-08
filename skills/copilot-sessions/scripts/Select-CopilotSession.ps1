<#
.SYNOPSIS
    Interactively selects and resumes one recent GitHub Copilot CLI session.

.DESCRIPTION
    Uses the same selection rules as Resume-CopilotSessions.ps1:

      * sessions contain at least one recorded turn,
      * sessions were updated within the requested time window,
      * working directories still exist,
      * only the most recently updated session per working directory is shown.

    Use Up/Down, Page Up/Page Down, Home and End to move through the list. Enter resumes the
    highlighted session in the current terminal with --yolo and the shared Node.js crash
    workaround; Escape or Ctrl+C cancels.

.PARAMETER Hours
    Size of the time window in hours. Mutually exclusive with -Days.

.PARAMETER Days
    Size of the time window in days. Mutually exclusive with -Hours. Defaults to 1 day.

.PARAMETER CopilotHome
    Copilot configuration directory holding session-store.db.
    Defaults to $env:COPILOT_HOME, then "$HOME\.copilot".

.PARAMETER Filter
    Optional wildcard pattern matched against the session working directory, repository and name.

.PARAMETER CopilotArgument
    Additional arguments appended to the Copilot command line.

.EXAMPLE
    .\Select-CopilotSession.ps1

    Pick from non-empty sessions updated in the last day and resume one with --yolo.

.EXAMPLE
    .\Select-CopilotSession.ps1 -Hours 8 -Filter '*UA-.NETStandard*'

    Pick from matching sessions updated in the last eight hours.

.NOTES
    Requires PowerShell 7, the Copilot CLI and either python or sqlite3.exe on PATH.
#>
#Requires -Version 7.0
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '')]
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

    [string[]] $CopilotArgument = @()
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Import-Module -Name (Join-Path -Path $PSScriptRoot -ChildPath 'CopilotSessionStore.psm1') -Force

function Get-SessionTitle {
    param([Parameter(Mandatory)] [pscustomobject] $Session)

    if (-not [string]::IsNullOrWhiteSpace($Session.Summary)) {
        return $Session.Summary
    }
    if (-not [string]::IsNullOrWhiteSpace($Session.Repository)) {
        if (-not [string]::IsNullOrWhiteSpace($Session.Branch)) {
            return "$($Session.Repository)#$($Session.Branch)"
        }
        return $Session.Repository
    }
    return "copilot $($Session.Id.Substring(0, 8))"
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
        [switch] $Selected
    )

    [Console]::SetCursorPosition(0, $Row)
    $foreground = [Console]::ForegroundColor
    $background = [Console]::BackgroundColor
    if ($Selected) {
        [Console]::ForegroundColor = [ConsoleColor]::Black
        [Console]::BackgroundColor = [ConsoleColor]::Gray
    }
    [Console]::Write((ConvertTo-FixedWidthText -Text $Text -Width $Width))
    if ($Selected) {
        [Console]::ForegroundColor = $foreground
        [Console]::BackgroundColor = $background
    }
}

function Select-Session {
    param([Parameter(Mandatory)] [object[]] $Session)

    if ([Console]::IsInputRedirected -or [Console]::IsOutputRedirected) {
        throw 'Interactive session selection requires an attached console.'
    }
    if ([Console]::WindowHeight -lt 6 -or [Console]::WindowWidth -lt 30) {
        throw 'The console is too small for the session picker. Resize it and try again.'
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
            if ($height -lt 6 -or $width -lt 29) {
                throw 'The console became too small for the session picker. Resize it and try again.'
            }
            $pageSize = [Math]::Max(1, $height - 4)

            if ($selectedIndex -lt $topIndex) {
                $topIndex = $selectedIndex
            } elseif ($selectedIndex -ge $topIndex + $pageSize) {
                $topIndex = $selectedIndex - $pageSize + 1
            }

            Write-MenuLine -Row 0 -Width $width -Text 'Select a Copilot session'
            Write-MenuLine -Row 1 -Width $width -Text 'Up/Down: move  PgUp/PgDn: page  Home/End: jump  Enter: resume  Esc: cancel'
            Write-MenuLine -Row 2 -Width $width -Text ''

            for ($row = 0; $row -lt $pageSize; $row++) {
                $sessionIndex = $topIndex + $row
                $text = ''
                if ($sessionIndex -lt $Session.Count) {
                    $item = $Session[$sessionIndex]
                    $updated = $item.UpdatedUtc.ToLocalTime().ToString('yyyy-MM-dd HH:mm')
                    $id = $item.Id.Substring(0, [Math]::Min(8, $item.Id.Length))
                    $text = "{0}  {1}  {2}  [{3}]" -f $updated, $id, (Get-SessionTitle -Session $item), $item.Cwd
                }
                Write-MenuLine -Row (3 + $row) -Width $width -Text $text -Selected:($sessionIndex -eq $selectedIndex)
            }

            $current = $Session[$selectedIndex]
            $footer = "{0}/{1}  {2}" -f ($selectedIndex + 1), $Session.Count, $current.Id
            Write-MenuLine -Row ($height - 1) -Width $width -Text $footer

            $key = [Console]::ReadKey($true)
            if ($key.Key -eq [ConsoleKey]::C -and
                ($key.Modifiers -band [ConsoleModifiers]::Control) -ne 0) {
                return $null
            }

            switch ($key.Key) {
                ([ConsoleKey]::UpArrow) {
                    if ($selectedIndex -gt 0) { $selectedIndex-- }
                }
                ([ConsoleKey]::DownArrow) {
                    if ($selectedIndex -lt $Session.Count - 1) { $selectedIndex++ }
                }
                ([ConsoleKey]::PageUp) {
                    $selectedIndex = [Math]::Max(0, $selectedIndex - $pageSize)
                }
                ([ConsoleKey]::PageDown) {
                    $selectedIndex = [Math]::Min($Session.Count - 1, $selectedIndex + $pageSize)
                }
                ([ConsoleKey]::Home) {
                    $selectedIndex = 0
                }
                ([ConsoleKey]::End) {
                    $selectedIndex = $Session.Count - 1
                }
                ([ConsoleKey]::Enter) {
                    return $Session[$selectedIndex]
                }
                ([ConsoleKey]::Escape) {
                    return $null
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

$copilot = Get-Command -Name 'copilot' -CommandType Application -ErrorAction SilentlyContinue |
    Select-Object -First 1
if (-not $copilot) {
    throw 'The Copilot CLI (copilot) was not found on PATH.'
}

$window = if ($PSCmdlet.ParameterSetName -eq 'Hours') {
    [timespan]::FromHours($Hours)
} else {
    [timespan]::FromDays($Days)
}

$databasePath = Get-CopilotStorePath -CopilotHome (Resolve-CopilotHome -Requested $CopilotHome) -Require
$sessions = @(Get-CopilotResumableSession -DatabasePath $databasePath -Window $window -Filter $Filter)
if ($sessions.Count -eq 0) {
    Write-Host "No non-empty Copilot sessions were updated in the last $window." -ForegroundColor Yellow
    return
}

$selected = Select-Session -Session $sessions
if (-not $selected) {
    Write-Host 'Session selection cancelled.'
    return
}

$arguments = [System.Collections.Generic.List[string]]::new()
foreach ($argument in (Get-CopilotSessionRuntimeArgument)) {
    $arguments.Add($argument)
}
$arguments.Add("--resume=$($selected.Id)")
$arguments.Add('--yolo')
foreach ($argument in $CopilotArgument) {
    if ([string]::IsNullOrWhiteSpace($argument)) {
        throw 'CopilotArgument entries cannot be empty.'
    }
    $arguments.Add($argument)
}

$title = Get-SessionTitle -Session $selected
$target = "$title [$($selected.Cwd)]"
if (-not $PSCmdlet.ShouldProcess($target, 'Resume Copilot session with --yolo and Node.js crash workaround')) {
    return
}

Write-Host "Resuming '$title' in '$($selected.Cwd)' with --yolo and the Node.js crash workaround." -ForegroundColor Green
Push-Location -LiteralPath $selected.Cwd
try {
    & $copilot.Source @arguments
    $exitCode = $LASTEXITCODE
}
finally {
    Pop-Location
}

if ($exitCode -ne 0) {
    throw "Copilot exited with code $exitCode."
}
