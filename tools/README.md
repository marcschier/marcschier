# 🛠️ Tools

Small standalone developer utilities. Nothing here ships as a package — these are scripts meant to be
run directly from a clone.

## 💤 [`Resume-CopilotSessions.ps1`](Resume-CopilotSessions.ps1)

Reopens the [GitHub Copilot CLI](https://github.com/github/copilot-cli) sessions you were actually
working in, one per Windows Terminal tab.

Working across a dozen clones means a dozen Copilot sessions, and after a reboot there is no quick way
to get them back. This script reads the local session store, works out which sessions matter, and
rebuilds the tab layout.

For every session it selects, a tab is added to the **currently focused** Windows Terminal window,
started in that session's original working directory and running
`copilot --resume=<id> --allow-all`.

### Selection rules

| Rule | Behaviour |
|---|---|
| Non-empty | Sessions with at least one recorded turn; blank/aborted launches are ignored. |
| Time window | Sessions last updated within `-Hours` / `-Days` (default: 1 day). |
| One per directory | Only the most recently updated session per working directory. |
| Live directories | Sessions whose working directory no longer exists are skipped with a warning. |

### Usage

```powershell
# Everything touched in the last 24 hours
./tools/Resume-CopilotSessions.ps1

# Narrower window
./tools/Resume-CopilotSessions.ps1 -Hours 6

# See what would be resumed, without opening anything
./tools/Resume-CopilotSessions.ps1 -Days 3 -WhatIf

# Restrict to one set of clones
./tools/Resume-CopilotSessions.ps1 -Days 2 -Filter '*UA-.NETStandard*'
```

### Parameters

| Parameter | Default | Description |
|---|---|---|
| `-Hours` | — | Window size in hours. Mutually exclusive with `-Days`. |
| `-Days` | `1` | Window size in days. |
| `-CopilotHome` | `$env:COPILOT_HOME`, else `$HOME/.copilot` | Directory holding `session-store.db`. |
| `-Filter` | — | Wildcard matched against the working directory, repository and session name. |
| `-MaxTabs` | `20` | Safety cap on how many tabs to open. |
| `-CopilotArgument` | — | Extra arguments appended to the `copilot` command line, e.g. `--model`. |
| `-CloseTabOnExit` | off | Close the tab when `copilot` exits instead of leaving a shell prompt. |
| `-WhatIf` / `-Confirm` | — | Standard PowerShell `ShouldProcess` support. |

### Requirements

* PowerShell 7
* [Windows Terminal](https://github.com/microsoft/terminal) (`wt.exe`)
* [Copilot CLI](https://github.com/github/copilot-cli) (`copilot.exe`)
* A SQLite reader on `PATH` — either `sqlite3.exe` or `python`. The session store is a SQLite
  database, and neither PowerShell nor .NET can read one out of the box.

### Notes

* The session store is opened **read-only**. If that fails because the database is locked, the script
  falls back to querying a temporary snapshot of the `.db`, `-wal` and `-shm` files, so a running
  Copilot session is never disturbed.
* `wt -w 0` targets the most recently used Windows Terminal window. If no window is open, Windows
  Terminal creates one.
* Resuming a session that is already open elsewhere is not prevented — the script deliberately does no
  liveness detection.
