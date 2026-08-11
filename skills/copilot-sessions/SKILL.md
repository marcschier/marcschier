---
name: copilot-sessions
license: MIT
description: >
  Manage local GitHub Copilot CLI session state on Windows: reopen recent sessions as
  Windows Terminal tabs, reclaim disk by purging empty and orphaned session folders, and
  move session state between machines.
  USE FOR: "resume my sessions", "reopen what I was working on yesterday", "open a tab per
  repo I was working in", "my .copilot folder is huge", "clean up empty Copilot sessions",
  "delete orphaned session state", "why is session-state so big", "move my Copilot sessions
  to my other machine", "export/import Copilot session history", "transfer my chat history
  to another PC".
  DO NOT USE FOR: managing GitHub Codespaces, git worktrees, VS Code windows, Copilot
  settings/config unrelated to session state, or deleting files inside a user's repository.
---

# copilot-sessions

Three PowerShell scripts that operate on the Copilot CLI's local session store.

## Script location

The scripts live in `scripts/` **next to this SKILL.md**. Always resolve them relative to this
file's directory — never assume the user has a clone of the repository they came from.

| Script | Purpose |
|---|---|
| `scripts/Resume-CopilotSessions.ps1` | Reopen recent sessions as Windows Terminal tabs |
| `scripts/Remove-EmptyCopilotSessions.ps1` | Purge empty sessions and orphaned session state |
| `scripts/Copy-CopilotSessions.ps1` | Export/import session state between machines |
| `scripts/CopilotSessionStore.psm1` | Shared helper module — never invoked directly |

## Prerequisites

* PowerShell 7 (`pwsh`)
* Windows Terminal (`wt.exe`) — only for the resume script
* Copilot CLI (`copilot.exe`) — only for the resume script
* `python` **or** `sqlite3.exe` on `PATH` — the session store is a SQLite database and neither
  PowerShell nor .NET can read one unaided

If no SQLite reader is present, tell the user to run `winget install Python.Python.3.13`.

## Concepts

Read this before touching the purge script — the vocabulary matters.

| Term | Meaning |
|---|---|
| **Session** | A row in `~/.copilot/session-store.db` plus a folder in `~/.copilot/session-state/<id>` |
| **Non-empty** | The session has at least one recorded turn in the `turns` table |
| **Empty** | A session row with zero turns — usually a launch that was abandoned immediately |
| **Orphan** | A `session-state` folder with **no database row**. It cannot appear in `/resume` at all, yet it still holds every artifact the agent wrote under `files/`. Orphans are typically where the disk has gone |
| **In use** | The folder holds an `inuse.<pid>.lock` file whose process is still running |

Two rules that are easy to get backwards:

* `plan.md` **always protects a session that still has a database row.**
* `plan.md` **does not protect an orphan by default**, because an orphan is unreachable regardless.
  `-ProtectOrphansWithPlan` restores that protection.

## Choosing a script

| User intent | Script | Typical invocation |
|---|---|---|
| "Reopen what I was working on" | Resume | `-Hours 8` |
| "Open a tab per repo" | Resume | (default, 1 day) |
| "Reopen everything and ask each one to catch me up" | Resume | `-Prompt '<text>'` |
| "My .copilot folder is huge" | Remove | **`-WhatIf` first**, then agree a threshold |
| "Delete empty sessions" | Remove | `-Scope Sessions` |
| "Clean up but keep anything with a plan" | Remove | `-ProtectOrphansWithPlan` |
| "Move my sessions to my laptop" | Copy | `-Export` then `-Import` on the target |
| "Just the transcripts, not the artifacts" | Copy | `-Export -Lean` |

### Opening prompts

`Resume-CopilotSessions.ps1 -Prompt '<text>'` runs the same text as the first prompt in every
resumed session. The session still opens interactively — the prompt just executes immediately.

Use it when the user wants every reopened session to do something on arrival, for example
*"summarise where we left off"*, *"re-run the tests and fix anything broken"*, or
*"check whether my PR has new review comments"*.

The script escapes quotes, semicolons, ampersands, pipes and trailing backslashes automatically, so
pass the user's wording through as-is. The one exception is `%VARIABLE%`: tabs launch through
`cmd.exe`, which expands those before Copilot sees them, so rephrase to avoid percent signs. The
script warns when it detects one.

## Safety rules

These are mandatory. The purge script deletes tens of gigabytes with its default switches.

1. **Never run `Remove-EmptyCopilotSessions.ps1` destructively as the first action.** Always run it
   with `-WhatIf` first, show the user the category table and the reclaimable total, and wait for
   explicit approval.
2. **Never pass `-Force`** unless the user has seen a preview and explicitly asked to skip the
   prompt. `-Force` bypasses the confirmation entirely.
3. **State the default clearly** before deleting: orphaned folders are purged *even when they contain
   a plan.md*. If the user sounds hesitant, offer `-ProtectOrphansWithPlan` or `-Recycle`.
4. **Offer `-Recycle`** whenever the reclaimable total is large or the user seems unsure; it sends
   folders to the Recycle Bin instead of deleting them permanently.
5. **Never widen the age window without being asked.** The default only touches sessions older than
   one day; do not silently pass `-Days 0`.
6. **Never purge in order to "free space" during an unrelated task.** Only run it when the user asked
   for cleanup.
7. Live sessions are skipped automatically — do not attempt to work around that.

For `Copy-CopilotSessions.ps1 -Import`, warn the user that the Copilot CLI should not be running on
the target machine, since the import writes to the session store.

## Recipes

Resolve `$skill` to this skill's directory first.

```powershell
# Reopen everything touched in the last 8 hours, one tab per working directory
& "$skill/scripts/Resume-CopilotSessions.ps1" -Hours 8

# Reopen and have every session immediately catch the user up
& "$skill/scripts/Resume-CopilotSessions.ps1" -Hours 12 -Prompt 'Summarise where we left off and list next steps'

# Preview only - ALWAYS do this before any purge
& "$skill/scripts/Remove-EmptyCopilotSessions.ps1" -WhatIf

# Purge sessions untouched for a week, into the Recycle Bin
& "$skill/scripts/Remove-EmptyCopilotSessions.ps1" -Days 7 -Recycle

# Only tidy the /resume picker, leave every orphaned folder alone
& "$skill/scripts/Remove-EmptyCopilotSessions.ps1" -Scope Sessions

# Bundle the last two days of real work
& "$skill/scripts/Copy-CopilotSessions.ps1" -Export -Path D:\transfer\copilot -Days 2

# Same, but transcripts/plans/todos only - no agent artifacts
& "$skill/scripts/Copy-CopilotSessions.ps1" -Export -Path D:\transfer\copilot.zip -Days 7 -Lean

# Apply on a machine whose clones live under C:\src instead of D:\git
& "$skill/scripts/Copy-CopilotSessions.ps1" -Import -Path D:\transfer\copilot -PathMap 'D:\git=C:\src'
```

## Interpreting purge output

```
Category     Count Size
--------     ----- ----
EmptySession    30 15.1 KB
Orphan         337 14.84 GB

Candidates: 367   Reclaimable: 14.84 GB
Kept: 49 with turns, 0 protected by plan.md, 8 in use, 0 newer than 1.00:00:00, 0 out of scope
```

* `EmptySession` is almost always tiny — it declutters `/resume` rather than reclaiming disk.
* `Orphan` is where the space is. If the user only wants the picker tidied, use `-Scope Sessions`.
* The `Kept:` line is the audit trail. If `in use` is non-zero, some sessions are open right now;
  that is expected and correct.
* Add `-Verbose` to list the ten largest candidates before deciding.

## Bundle format

`Copy-CopilotSessions.ps1 -Export` writes:

```
manifest.json              bundle metadata + one entry per session
sessions/<id>/rows.json    all session-scoped rows from session-store.db
sessions/<id>/state/       a copy of session-state/<id>, minus any inuse.*.lock
```

A `-Path` ending in `.zip` produces an archive; anything else produces a directory. Prefer a
**directory** for large exports — agent artifacts barely compress, and a lean transcript-only bundle
is small enough that either works.

On import, `-PathMap 'FROM=TO'` rewrites path prefixes case-insensitively in `sessions.cwd`,
`session_files.file_path` and the session's `workspace.yaml` (`cwd` and `git_root`). Paths matching
no rule are kept verbatim, and the script warns when a resulting directory does not exist locally.

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| "No usable SQLite reader was found" | Install Python: `winget install Python.Python.3.13` |
| "Copilot session store not found" | Wrong `COPILOT_HOME`; pass `-CopilotHome <path>` |
| Resume opens no tabs | No sessions in the window, or their directories no longer exist — widen `-Hours`/`-Days` and check the warnings |
| Tabs open in the wrong window | `wt -w 0` targets the most recently used window; focus the intended one first |
| `-Prompt` text arrives truncated or altered | A `%VARIABLE%` reference was expanded by `cmd.exe`; rephrase without percent signs |
| Import says the schema differs | The bundle came from a different CLI version. `-Force` overrides, but verify afterwards |
| Import skipped everything | The sessions already exist locally; re-run with `-Overwrite` |
| Imported session points at a missing directory | Add or correct a `-PathMap` rule and re-import with `-Overwrite` |

## Maintenance

`copilot skill add <directory>` registers the folder by reference, so edits to the scripts take
effect for new sessions. Use `/skills reload` to pick them up inside a running session.
