# 💤 copilot-sessions

An installable [agent skill](https://docs.github.com/copilot/concepts/agents/about-agent-skills) plus
four standalone PowerShell scripts for managing local [GitHub Copilot CLI](https://github.com/github/copilot-cli)
session state on Windows. It installs as a Copilot CLI plugin, or as a bare skill.

Working across a dozen clones means a dozen Copilot sessions. After a reboot there is no quick way to
get them back, the session store quietly grows into the tens of gigabytes, and there is no built-in way
to carry work over to another machine. These scripts cover those workflows.

## Install

### As a plugin (recommended)

Register the marketplace once, then install:

```powershell
copilot plugin marketplace add marcschier/marcschier
copilot plugin install copilot-sessions@marcschier
```

Updates come with `copilot plugin update copilot-sessions`.

> Direct installs (`copilot plugin install marcschier/marcschier:skills`) also work, but the CLI
> warns that repo, URL and local-path installs are deprecated in favour of `plugin@marketplace`.

### As a skill only

From a clone of this repository:

```powershell
copilot skill add .\skills\copilot-sessions
```

Then check it loaded:

```
/skills info copilot-sessions
```

Once installed you can just ask for what you want — *"reopen what I was working on yesterday"*,
*"why is my .copilot folder so big"*, *"move my sessions to my laptop"* — and the skill knows which
script to run and which safety checks to apply. The scripts also work standalone.

> `copilot skill add <directory>` registers the folder by reference, so edits to the scripts take
> effect for new sessions. Use `/skills reload` to pick them up inside a running session. A plugin
> install copies the files instead, so use `copilot plugin update` after changing them.

### Where the scripts land

A plugin install puts them under
`~/.copilot/installed-plugins/marcschier/copilot-sessions/copilot-sessions/scripts/`. The skill
resolves them relative to its own `SKILL.md`, so you never need that path yourself — but it is handy
when invoking a script directly.

## Requirements

* PowerShell 7
* [Windows Terminal](https://github.com/microsoft/terminal) (`wt.exe`) — resume script, and the
  select script unless it is run with `-Launch Inline`
* [Copilot CLI](https://github.com/github/copilot-cli) (`copilot.exe`) — select and resume scripts
* `python` **or** `sqlite3.exe` on `PATH` — the session store is a SQLite database, and neither
  PowerShell nor .NET can read one out of the box

---

## `Select-CopilotSession.ps1`

Shows the same resumable set used by `Resume-CopilotSessions.ps1`, but lets you choose one session
with a dependency-free console picker. Use Up/Down, Page Up/Page Down, Home and End to navigate,
Enter to resume, or Escape to cancel. The selected session starts in its original working directory
with `--yolo` and the temporary Node.js crash workaround described below.

`-Launch` decides where it starts:

| `-Launch` | Behaviour |
|---|---|
| `NewWindow` (default) | Opens a separate Windows Terminal window (`wt -w new`) and returns immediately |
| `Inline` | Runs in the current terminal, which then blocks until Copilot exits; no `wt.exe` needed |

| Rule | Behaviour |
|---|---|
| Non-empty | Sessions with at least one recorded turn; blank launches are ignored |
| Time window | Sessions last updated within `-Hours` / `-Days` (default: 1 day) |
| One per directory | Only the most recently updated session per working directory |
| Live directories | Sessions whose directory no longer exists are skipped with a warning |

With `-Launch NewWindow`, working directories containing `;` are skipped — Windows Terminal splits
its command line on that character. `-CopilotArgument` entries are escaped and quoted for the
`wt.exe` → `cmd.exe` → `copilot` chain, so spaces, quotes, `;` and cmd metacharacters such as `&`,
`|`, `<`, `>` and `(` reach Copilot unchanged; only `%` is rejected, because `cmd.exe` expands it
first. Use `-Launch Inline` for those.

```powershell
./scripts/Select-CopilotSession.ps1
./scripts/Select-CopilotSession.ps1 -Launch Inline
./scripts/Select-CopilotSession.ps1 -Hours 8
./scripts/Select-CopilotSession.ps1 -Days 7 -Filter '*UA-.NETStandard*'
./scripts/Select-CopilotSession.ps1 -CopilotArgument '--model=claude-sonnet-4.6'
```

---

## `Resume-CopilotSessions.ps1`

Reopens the sessions you were actually working in, one per Windows Terminal tab. Each tab is added to
the **currently focused** window, starts in that session's original working directory, and resumes
Copilot with `--allow-all` plus the temporary Node.js crash workaround below.

| Rule | Behaviour |
|---|---|
| Non-empty | Sessions with at least one recorded turn; blank launches are ignored |
| Time window | Sessions last updated within `-Hours` / `-Days` (default: 1 day) |
| One per directory | Only the most recently updated session per working directory |
| Live directories | Sessions whose directory no longer exists are skipped with a warning |

```powershell
./scripts/Resume-CopilotSessions.ps1              # last 24 hours
./scripts/Resume-CopilotSessions.ps1 -Hours 6
./scripts/Resume-CopilotSessions.ps1 -Days 3 -WhatIf
./scripts/Resume-CopilotSessions.ps1 -Days 2 -Filter '*UA-.NETStandard*'

# Run the same opening prompt in every resumed tab
./scripts/Resume-CopilotSessions.ps1 -Hours 12 -Prompt 'Summarise where we left off and list next steps'
```

| Parameter | Default | Description |
|---|---|---|
| `-Hours` / `-Days` | 1 day | Size of the window |
| `-CopilotHome` | `$env:COPILOT_HOME`, else `$HOME/.copilot` | Directory holding `session-store.db` |
| `-Filter` | — | Wildcard over working directory, repository and name |
| `-MaxTabs` | `20` | Safety cap on tabs |
| `-CopilotArgument` | — | Extra arguments for `copilot`, e.g. `--model` |
| `-Prompt` | — | Text run as the first prompt in every resumed session (passed as `-i`) |
| `-CloseTabOnExit` | off | Close the tab when `copilot` exits |

`-Prompt` keeps the session interactive and simply executes the text straight away, so it is handy
for things like *"summarise where we left off"* or *"re-run the tests and fix anything broken"* across
a whole day's worth of sessions at once. Quotes, semicolons, ampersands, pipes and trailing
backslashes are all escaped for you. Avoid `%VARIABLE%` references — tabs launch through `cmd.exe`,
which expands those before Copilot sees them, and the script warns when it spots one.

### Temporary Node.js crash workaround

Both scripts that start Copilot sessions currently add:

```text
--node-options="--max-old-space-size=8000"
```

The packaged executable ignores the `NODE_OPTIONS` environment variable, so the old-space limit must
go through `--node-options`. The larger heap is a temporary mitigation rather than a leak fix. See
[github/copilot-cli#4686](https://github.com/github/copilot-cli/issues/4686) and
[github/copilot-cli#4725](https://github.com/github/copilot-cli/issues/4725).

---

## `Remove-EmptyCopilotSessions.ps1`

Reclaims disk and declutters the `/resume` picker. There are two very different populations:

| Kind | What it is | Purged when |
|---|---|---|
| Session with ≥ 1 turn | Real work | **Never** |
| Empty session | A database row with zero turns | Only if it has no `plan.md` |
| **Orphan** | A `session-state` folder with **no database row** — invisible to `/resume`, but still holding every artifact under `files/` | Always, unless `-ProtectOrphansWithPlan` |

`plan.md` always protects a session that still has a database row. It deliberately does *not* protect
an orphan by default, because an orphan cannot be resumed either way — and on a well-used machine
that is where nearly all the reclaimable space is.

Sessions currently open in another terminal (detected via `inuse.<pid>.lock` with a live process) are
never touched, and neither is anything newer than the age threshold.

```powershell
./scripts/Remove-EmptyCopilotSessions.ps1 -WhatIf              # always preview first
./scripts/Remove-EmptyCopilotSessions.ps1 -Days 7 -Recycle
./scripts/Remove-EmptyCopilotSessions.ps1 -Scope Sessions      # only tidy the picker
./scripts/Remove-EmptyCopilotSessions.ps1 -ProtectOrphansWithPlan
```

| Parameter | Default | Description |
|---|---|---|
| `-Hours` / `-Days` | 1 day | Only purge sessions **older than** this |
| `-Scope` | `All` | `All`, `Sessions` (database rows only) or `Orphans` |
| `-ProtectOrphansWithPlan` | off | Keep orphaned folders that contain a `plan.md` |
| `-Recycle` | off | Send to the Recycle Bin instead of deleting permanently |
| `-Force` | off | Skip the confirmation prompt |

Sample preview:

```
Category     Count Size
--------     ----- ----
EmptySession    30 15.1 KB
Orphan         337 14.84 GB

Candidates: 367   Reclaimable: 14.84 GB
Kept: 49 with turns, 0 protected by plan.md, 8 in use, 0 newer than 1.00:00:00, 0 out of scope
```

Add `-Verbose` to list the ten largest candidates before committing.

---

## `Remove-OldCopilotSessions.ps1`

Removes sessions **by age**, including sessions that recorded real work — so it is interactive by
default. Use it to reclaim space long after the work is done; use `Remove-EmptyCopilotSessions.ps1`
for the routine, safe tidy-up.

1. Every session last updated before the cutoff is collected, together with the size of its
   `session-state` directory.
2. A checklist appears with all candidates pre-selected, largest first. **Deselect the ones you want
   to keep.** The footer shows a live count and the space the current selection would free.
3. Enter removes what is still checked: the session's rows in `session-store.db` and its
   `session-state` directory.

| Key | Action |
|---|---|
| Up/Down, PgUp/PgDn, Home/End | Move |
| Space | Toggle keep/remove on the highlighted session |
| `A` / `N` / `I` | Check all / uncheck all / invert |
| Enter | Remove the checked sessions |
| Esc, Ctrl+C | Cancel — nothing is removed |

Sessions open in another terminal are never offered, and neither is anything newer than the age
threshold or holding a `plan.md` (unless `-IncludePlanned`).

```powershell
./scripts/Remove-OldCopilotSessions.ps1 -Days 30 -WhatIf          # list only, no checklist
./scripts/Remove-OldCopilotSessions.ps1 -Days 14                  # checklist, then remove
./scripts/Remove-OldCopilotSessions.ps1 -Days 60 -Recycle
./scripts/Remove-OldCopilotSessions.ps1 -Hours 6 -Filter '*scratch*' -Force
```

| Parameter | Default | Description |
|---|---|---|
| `-Hours` / `-Days` | 30 days | Only offer sessions **older than** this |
| `-Filter` | none | Wildcard over working directory, repository and summary |
| `-IncludePlanned` | off | Also offer sessions whose state directory has a `plan.md` |
| `-Recycle` | off | Send to the Recycle Bin instead of deleting permanently |
| `-Force` | off | Skip the checklist and the prompt, and remove every candidate |

The reported size covers the `session-state` tree only. Deleted database rows free space *inside*
`session-store.db`, which SQLite reuses rather than returning to the file system, so it is not
counted.

---

## `Copy-CopilotSessions.ps1`

Packages non-empty session state from one machine and applies it on another.

```powershell
# On the source machine
./scripts/Copy-CopilotSessions.ps1 -Export -Path D:\transfer\copilot -Days 2

# Transcripts, plans and todos only - no agent artifacts
./scripts/Copy-CopilotSessions.ps1 -Export -Path D:\transfer\copilot.zip -Days 7 -Lean

# On the target machine, whose clones live under C:\src
./scripts/Copy-CopilotSessions.ps1 -Import -Path D:\transfer\copilot -PathMap 'D:\git=C:\src'
```

Bundle layout:

```
manifest.json              bundle metadata + one entry per session
sessions/<id>/rows.json    all session-scoped rows from session-store.db
sessions/<id>/state/       a copy of session-state/<id>, minus any inuse.*.lock
```

A `-Path` ending in `.zip` produces an archive; anything else produces a directory. Prefer a
directory for large exports — agent artifacts barely compress.

| Parameter | Mode | Description |
|---|---|---|
| `-Hours` / `-Days` | export | Window of sessions to include (default 1 day) |
| `-Lean` | export | Exclude `files/`, `rewind-file-snapshots/`, `rewind-snapshots/` |
| `-ExcludeDirectory` | export | Additional session-state subdirectories to omit |
| `-Overwrite` | import | Replace sessions that already exist on the target |
| `-PathMap` | import | `'SOURCE=TARGET'` path prefix rewrites, repeatable |
| `-Filter` | both | Wildcard over working directory, repository and name |
| `-Force` | import | Proceed despite a session store schema mismatch |

`-PathMap` rewrites `sessions.cwd`, `session_files.file_path`, and `workspace.yaml`'s `cwd` and
`git_root`. Unmapped paths are kept verbatim, and the script warns when a rewritten directory does not
exist locally.

Close the Copilot CLI on the target machine before importing — the import writes to the session store.

---

## Notes

* The session store is opened **read-only** for every query. If that fails because the database is
  locked, the scripts fall back to a temporary snapshot of the `.db`, `-wal` and `-shm` files, so a
  running session is never disturbed.
* `wt -w new` opens a separate Windows Terminal window; `wt -w 0` targets the most recently used one.
  If none is open, Windows Terminal creates one.
* The resume script does not detect sessions already open elsewhere — resuming a duplicate is allowed.
