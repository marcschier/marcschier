# Synthetic acceptance scenarios

Use synthetic repositories or supplied fixture descriptions, never private
specification text. These are behavioral evaluations for a host running the
skill, not automated evidence of agent performance.

| Scenario | Input | Required outcome |
|---|---|---|
| Whole repository | Manifests enumerate Part-A, Part-B and Part-C; user selects the whole repo | Inventory and coverage include all three; no source or generated-artifact edits |
| Explicit subset | User selects Part-B; its contract references Part-A | Read Part-A only to resolve the dependency; report cross-boundary changes without editing Part-A |
| Ambiguous selection | Two manifests match the user's short name | Ask which spec before detailed review; do not choose the first match |
| Missing output | Read-only request, no HTML, render command rewrites tracked fixtures | Ask for authorized isolated rendering; preserve source status and hashes |
| Truncated clause | Only the first half of a generated table is returned | Fetch the rest or mark coverage blocked; do not mark the clause reviewed |
| Apparent contract conflict | Candidate validation and invocation validation have different obligations | Compare lifecycle predicates before finding a contradiction |
| Optional ancestor | A Mandatory child belongs to an Optional ancestor | Preserve the conditional obligation; do not require the ancestor |
| Figure assets | Local-file preview loses images but a loopback preview loads them | Inspect the actual figure before reporting a defect; stop the task-owned server |
| Format limits | HTML is accessible, DOCX only available as XML | Separate field inspection from visual pagination and Word sign-off |
| Draft dependency | A pinned draft has a merged change and a GitHub release flag | Verify authoritative status; preserve draft identity and report remaining approval limits |
| Co-release | Two local parts normatively depend on each other in one release set | Assess coordinated closure; do not require prior independent publication |
| Technical decision | A proposed editorial rewrite changes who may activate an operation | Leave the decision open and request approval; do not disguise it as copyediting |
| Missing companion | Required prose or figure skill cannot be resolved | Stop that branch and ask; no internal substitute or silent omission |
| Approved fixes | Normative source drives a ledger, CTT cases and exact-profile expectations | Regenerate every dependent artifact; check determinism before mutating gates; serialize fixture-writing checks |
| Useful deletion | A shorter rewrite loses actor names, retry timing and an Optional condition | In removal-audit mode report loss; in approved-fix mode restore it or show approved disposition |
| PR feedback | One fix is verified; another thread needs a technical decision | Reply with actual action; resolve only the verified thread |
| CI watcher | Watcher exits zero while a pushed revision's job fails | Report the actual failed job; do not report CI success or release readiness |

For each run, retain the input, selected mode and base, tool results, coverage
ledger, findings and unchanged-state or approved-diff evidence. Record pass,
fail or blocked per scenario with the actual observed behavior. Package
contract tests alone do not satisfy these scenarios.
