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
    window. The tab starts in the session's original working directory and resumes Copilot with
    --allow-all plus the shared Node.js crash workaround.

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

.PARAMETER Prompt
    Text to run as the first prompt in every resumed session, passed to copilot as -i. The session
    still opens interactively; the prompt simply executes immediately.

    Avoid %VARIABLE% references: tabs are launched through cmd.exe, which expands them first.

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

.EXAMPLE
    .\Resume-CopilotSessions.ps1 -Hours 12 -Prompt 'Summarise where we left off and list next steps'

    Resume each session and immediately run the same opening prompt in every tab.

.NOTES
    Requires PowerShell 7, Windows Terminal (wt.exe) and the Copilot CLI (copilot.exe).
    Reading the SQLite session store requires either sqlite3.exe or python on PATH.
#>
#Requires -Version 7.0
# Write-Host is deliberate: these are interactive console tools whose tables and summaries are for
# the operator to read, not for the pipeline.
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

    [ValidateRange(1, 200)]
    [int] $MaxTabs = 20,

    [string[]] $CopilotArgument = @(),

    [ValidateNotNullOrEmpty()]
    [string] $Prompt,

    [switch] $CloseTabOnExit
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Import-Module -Name (Join-Path -Path $PSScriptRoot -ChildPath 'CopilotSessionStore.psm1') -Force

$copilotHomePath = Resolve-CopilotHome -Requested $CopilotHome
$databasePath = Get-CopilotStorePath -CopilotHome $copilotHomePath -Require

$windowsTerminal = Get-Command -Name 'wt.exe' -CommandType Application -ErrorAction SilentlyContinue |
    Select-Object -First 1
if (-not $windowsTerminal) {
    throw 'Windows Terminal (wt.exe) was not found on PATH. Install it with: winget install Microsoft.WindowsTerminal'
}

if (-not (Get-Command -Name 'copilot' -ErrorAction SilentlyContinue)) {
    throw 'The Copilot CLI (copilot) was not found on PATH.'
}

if ($Prompt -and $Prompt -match '%[A-Za-z_][A-Za-z0-9_]*%') {
    Write-Warning ('The prompt contains a %VARIABLE% reference. Tabs are launched through cmd.exe, ' +
        'which expands those before Copilot sees them. Rephrase to avoid the percent signs.')
}

$window = if ($PSCmdlet.ParameterSetName -eq 'Hours') {
    [timespan]::FromHours($Hours)
} else {
    [timespan]::FromDays($Days)
}

$selected = @(Get-CopilotResumableSession -DatabasePath $databasePath -Window $window -Filter $Filter)
$selected = @($selected | Where-Object {
    if ($_.Cwd.Contains(';')) {
        Write-Warning "Skipping session $($_.Id): directory '$($_.Cwd)' contains ';', which Windows Terminal cannot handle."
        return $false
    }
    return $true
})

if ($selected.Count -eq 0) {
    Write-Host "No non-empty Copilot sessions were updated in the last $window." -ForegroundColor Yellow
    return
}

if ($selected.Count -gt $MaxTabs) {
    Write-Warning "$($selected.Count) session(s) matched; opening only the $MaxTabs most recent. Raise -MaxTabs to include more."
    $selected = $selected | Select-Object -First $MaxTabs
}

$selected |
    Select-Object @{ Name = 'Title'; Expression = { Get-CopilotSessionTabTitle -Session $_ } },
                  @{ Name = 'Directory'; Expression = { $_.Cwd } },
                  @{ Name = 'UpdatedUtc'; Expression = { $_.UpdatedUtc.ToString('yyyy-MM-dd HH:mm') } },
                  @{ Name = 'Session'; Expression = { $_.Id } } |
    Format-Table -AutoSize |
    Out-String |
    Write-Host

$runtimeArguments = @(Get-CopilotSessionRuntimeArgument)
$runtimeCommand = $runtimeArguments -join ' '
$opened = 0
foreach ($session in $selected) {
    $title = Get-CopilotSessionTabTitle -Session $session
    $directory = Get-CopilotSessionStartingDirectory -Path $session.Cwd

    $copilotCommand = "copilot $runtimeCommand --resume=$($session.Id) --allow-all"
    if ($CopilotArgument.Count -gt 0) {
        $copilotCommand = "$copilotCommand $($CopilotArgument -join ' ')"
    }
    if ($Prompt) {
        $copilotCommand = "$copilotCommand -i `"$(ConvertTo-QuotedTabArgument -Value $Prompt)`""
    }

    # '-w 0' targets the most recently used (currently focused) Windows Terminal window.
    # The copilot command is passed as a single token so Windows Terminal never tries to
    # interpret the Copilot and Node.js arguments as options of its own.
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
