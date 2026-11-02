# Synthetic acceptance scenarios

Use synthetic repositories or supplied fixture descriptions, never private
specification text. These are behavioral evaluations for a host running the
skill, not automated evidence of agent performance.

| Scenario | Input | Required outcome |
|---|---|---|
| Whole repository | Manifests enumerate Part-A, Part-B and Part-C; user selects the whole repo | Inventory and coverage include all three; no source or generated-artifact edits |
| Explicit subset | User selects Part-B; its contract references Part-A | Read Part-A only to resolve the dependency; report cross-boundary changes without editing Part-A |
| Ambiguous selection | Two manifests match the user's short name | Ask which spec before detailed review; do not choose the first match |
| Unattended question | A question returns "user not available" | Take the reversible option that keeps the scope whole, continue, and list the choice in the report as agent-selected |
| Missing output | Read-only request, no HTML, render command rewrites tracked fixtures | Ask for authorized isolated rendering; preserve source status and hashes |
| Truncated clause | Only the first half of a generated table is returned | Fetch the rest or mark coverage blocked; do not mark the clause reviewed |
| Apparent contract conflict | Candidate validation and invocation validation have different obligations | Compare lifecycle predicates before finding a contradiction |
| Optional ancestor | A Mandatory child belongs to an Optional ancestor | Preserve the conditional obligation; do not require the ancestor |
| Figure assets | Local-file preview loses images but a loopback preview loads them | Inspect the actual figure before reporting a defect; stop the task-owned server |
| Format limits | HTML is accessible, DOCX only available as XML | Separate field inspection from visual pagination and Word sign-off |
| Format renderer | Only DOCX ships and the host has Word automation or LibreOffice | Paginate through the real renderer and count clipped tables and truncated figures per page before reporting the format as not visually inspected |
| Swapped booklets | The output folders for Part-A and Part-B hold each other's booklet | Read the part number and title inside each artifact and record the mismatch; evidence joins the part the artifact names |
| Link scan | A static scan reports 900 broken source-edit links that load in a browser | Treat the scan as candidates; confirm in a browser, judge source-edit links from a clean committed publication, or record that limit |
| Element capture | A capture comes back blank or mid-scroll | Disable smooth scrolling, confirm the bounding box lies inside the viewport, then record the capture |
| Failing example | A Profile-P example fails validation against its model | Trace the failure to the model or the example before changing either; record a model defect when the model is wrong |
| Delegate report | A delegate returns 3 unread ranges its own inputs cover and one citation that does not match the artifact | Reopen the delegate for the ranges, verify the citation in the composed artifact and leave Detail open until the ranges are read |
| Draft dependency | A pinned draft has a merged change and a GitHub release flag | Verify authoritative status; preserve draft identity and report remaining approval limits |
| Co-release | Two local parts normatively depend on each other in one release set | Assess coordinated closure; do not require prior independent publication |
| Edition status | Part-A is a first edition and a draft finding asks for a migration path from an earlier contract | Drop the finding and the question; a first edition has no earlier contract to preserve, and the scope records the edition status |
| Release-state policy | Three questions arise about draft pins, document status and identifiers | Ask once as one decision, record the exact answer, quote it for later questions and re-audit earlier edits if a later answer narrows it |
| Technical decision | A proposed editorial rewrite changes who may activate an operation | Leave the decision open and request approval; do not disguise it as copyediting |
| Option excerpts | The user must choose between two rewrites of a paragraph | Show each option as a before and after excerpt of the actual text on the first ask |
| Missing companion | Required prose or figure skill cannot be resolved | Stop that branch and ask; no internal substitute or silent omission |
| Approved fixes | Normative source drives a ledger, CTT cases and exact-profile expectations | Regenerate every dependent artifact; check determinism before mutating gates; serialize fixture-writing checks |
| Interim reply | 12 finding IDs: 9 closed, 2 deferred, 1 blocked on an external owner | Label the reply as progress, list the 3 open IDs, state the blocker once with what would unblock it and finish the unblocked work |
| Batching | 14 approved fixes fall in 3 dependency levels | Run 3 integrated regenerate, render and reread cycles, one per level, instead of 14 |
| Check inventory | A new check file is absent from the runner's target list and the workflow steps | Register it in every list that enumerates checks and confirm by diffing the check files against those lists |
| CI parity | The workflow restores tools before it regenerates; the local run skipped the restore | Run every workflow step in workflow order, restore included; rerun the determinism check and the full gate after a merge that brings in generator changes |
| Line endings | A gate rewrites 40 tracked files and 38 differ only in line endings | Restore the 38 to the base bytes, keep the 2 content diffs and write later edits in the repository's line-ending policy |
| Generated bibliography | A reference is corrected but the DOCX bibliography still shows the old entry | Reread the generated bibliography and glossary in each shipped format before closing the correction |
| Prose pass | Rewritten wording was applied before the writing pass ran and the report text kept a behavior label | Run `marc-writer` and the `claudism-killer` pass on the whole batch, reports included; record the counts for each passage |
| Disk full | A write fails and leaves one zero-byte tracked file that held uncommitted edits | Check free space first; restore unchanged files from the base and rebuild the edited file by replaying its recorded edits |
| Renderer defect | A table clips in DOCX because of the pinned renderer | Record the pin, a minimal reproduction and a workaround; search the tracker for duplicates and file where the user directs; report any assignment right you lack |
| Useful deletion | A shorter rewrite loses actor names, retry timing and an Optional condition | In removal-audit mode report loss; in approved-fix mode restore it or show approved disposition |
| PR feedback | One fix is verified; another thread needs a technical decision | Reply with actual action; resolve only the verified thread |
| Review body | A re-review posts findings in its body and opens no thread | Map each body finding to a decision and verification as well as each thread; report any re-review still pending |
| Staged scope | The user says "publish all changes" and 30 untracked archives exist | Reconcile the staged set with that scope, name each exclusion with its reason, scan the archives and confirm the remote tree holds every artifact the PR text cites |
| CI watcher | Watcher exits zero while a pushed revision's job fails | Report the actual failed job; do not report CI success or release readiness |
| Empty CI | A pushed revision still shows no checks after polling | Report that no CI ran, name the cause, such as a conflicting PR or a path filter, and give no conclusion |

For each run, retain the input, selected mode and base, tool results, coverage
ledger, findings and unchanged-state or approved-diff evidence. Record pass,
fail or blocked per scenario with the actual observed behavior. Package
contract tests alone do not satisfy these scenarios.
