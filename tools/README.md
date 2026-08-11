# 🛠️ Tools

The Copilot CLI session tooling that used to live here has moved to
[`skills/copilot-sessions`](../skills/copilot-sessions), where it ships as an agent skill that
bundles its own scripts. Install it as a plugin:

```powershell
copilot plugin marketplace add marcschier/marcschier
copilot plugin install copilot-sessions@marcschier
```

or as a skill only, from a clone:

```powershell
copilot skill add .\skills\copilot-sessions
```

| Script | Purpose |
|---|---|
| [`Resume-CopilotSessions.ps1`](../skills/copilot-sessions/scripts/Resume-CopilotSessions.ps1) | Reopen recent sessions as Windows Terminal tabs |
| [`Remove-EmptyCopilotSessions.ps1`](../skills/copilot-sessions/scripts/Remove-EmptyCopilotSessions.ps1) | Purge empty sessions and orphaned session state |
| [`Copy-CopilotSessions.ps1`](../skills/copilot-sessions/scripts/Copy-CopilotSessions.ps1) | Export and import session state between machines |
