# Autonomous NuGet dependency-update pipeline

This directory holds an automation that keeps the NuGet dependencies of every project listed in the repository [`README.md`](../../README.md) up to date, and — when an update actually changes a **published** package — cuts a patch release and promotes it to nuget.org.

`README.md` is the **source of truth**: the project list and the cross-repo dependency graph are parsed from it. Repos are processed **leaf → top** so a dependent is only updated after everything it depends on has been released and is live on nuget.org.

## How it works

Two workflows in [`.github/workflows`](../workflows):

| Workflow | Kind | Role |
|---|---|---|
| `nuget-update-repo.md` (+ generated `.lock.yml`) | **gh-aw agentic** (Copilot) | For one target repo: update **all** NuGet dependencies to latest stable (incl. majors), make **source-only** fixes for breaking changes, and open a PR. Never touches `tests/`, `.github/`, `eng/`, `version.json` or solution files. If a green build would require test/CI edits, it opens an explanatory issue instead of a PR. |
| `nuget-update-conductor.yml` | classic (deterministic) | The release state machine. Runs [`conductor.py`](conductor.py): for each repo in order it dispatches the updater, waits for green PR CI, merges, decides publish impact, bumps the patch + tags, waits for the tag CI, triggers the human-gated nuget.org promotion, and waits for the new version to be listed before advancing. Any failure opens an issue in the affected repo and halts the pipeline. |

### Per-repo pipeline (conductor phases)

```
detect → update → await-pr-ci → merge → publish-impact
       → release (bump patch + tag) → await-tag-ci → promote (human gate)
       → await-listing → done
```

- **No outdated deps** → repo marked done, no PR, no release.
- **Publish-impact gate** — a release only happens if an updated package is in the transitive `PackageReference` closure of a **packable** project (the ones packed to nuget.org, listed in [`repos.yml`](repos.yml)). Updates confined to test/benchmark/sample projects are merged but **not** released — nothing new would be published.
- **Human gate** — nuget.org promotion (`nuget.yml` in each library repo) runs under the `release` environment; configure reviewers there so promotion pauses for approval. The conductor yields at the gate if approval has not arrived within `GATE_WAIT_MIN` and resumes on the next trigger.
- **Stop on error** — a failed CI the agent cannot fix, a denied promotion, or a wait timeout opens an issue in the affected repo and halts the whole run (state stays `halted` until the issue is resolved and state is cleared).

State is persisted as `state.json` on the `automation/nuget-update-state` branch, so runs are resumable across the weekly schedule and manual dispatches.

## Files

| File | Purpose |
|---|---|
| `repos.yml` | Per-repo release mechanics: packable projects + package ids, promotion mechanism (`nuget-yml` / `ci-yml`), and the artifacts to wait for (nuget.org / GHCR / GitHub Packages). |
| `parse-readme.py` | Parse `README.md` → leaf→top ordered repo list + dependency graph. |
| `detect-outdated.py` | Restore a repo and list outdated NuGet packages. |
| `publish-impact.py` | Compute whether updated packages reach a packable project (→ release) or not. |
| `next-patch.py` | Nerdbank.GitVersioning-aware next-patch computation + `version.json` write. |
| `conductor.py` | The deterministic state machine that ties it all together. |

## One-time setup

1. **Install & compile gh-aw** (already scaffolded here):
   ```bash
   gh extension install github/gh-aw
   gh aw compile nuget-update-repo          # regenerate the .lock.yml after editing the .md
   ```
   Commit both `nuget-update-repo.md` and `nuget-update-repo.lock.yml`.
2. **`NUGET_UPDATE_TOKEN` secret** — a fine-grained PAT or GitHub App token with, across **all** repos in `README.md`: `contents:write`, `pull-requests:write`, `issues:write`, `actions:write`, `packages:read`. Add it to this repo's Actions secrets (`gh secret set NUGET_UPDATE_TOKEN`).
3. **Copilot engine auth** for the gh-aw updater — either org billing (`copilot-requests: write`) or a `COPILOT_GITHUB_TOKEN` secret. See <https://github.github.com/gh-aw/reference/auth/>.
4. **`release` environment reviewers** in each library repo, so nuget.org promotion requires human approval.

## Running

- **Manual:** Actions → `nuget-update-conductor` → *Run workflow* (optionally set a per-run time budget).
- **Scheduled:** Mondays 06:00 UTC.
- **Resume after a halt:** resolve the issue opened in the affected repo, then edit `state.json` on the `automation/nuget-update-state` branch (set `status` back to `running` / clear the failed repo's phase) and dispatch again.

## Adding or removing a project

Update `README.md` (the source of truth) and add/remove the matching entry in `repos.yml`. `parse-readme.py` fails fast if a README repo has no `repos.yml` descriptor.
