# Revision and closure

Keep the review result separate from the revision plan. A finding establishes
evidence for a change; it does not authorize implementation or settle a
technical choice.

## Plan and approval

Map every finding to its proposed source change, affected artifacts,
dependencies, owner or decision, and checks. Order changes by dependency.
Separate editorial corrections from technical decisions and publication work.
When a decision needs the user, show each option as a before and after excerpt
of the actual text, so the first ask is concrete. Keep the finding IDs as an
enumerated list until the work ends. Each ID closes with evidence, is deferred
with the consequence of deferral recorded, or is blocked on a named external
action. State a blocker once, with what would unblock it, then finish the
unblocked work. Label an interim reply as progress and list the IDs still open.

Present the plan for approval before implementation unless the user has already
authorized those specific fixes. Read-only review, plan and removal-audit modes
leave sources and generated artifacts unchanged. Publishing and merging each
require explicit authorization; approving local edits does not authorize either.

Carry forward the separate PDF and Word choices from the review contract.
Neither format permits inspection or fixes by default. General fix approval
does not opt them in; Inspect only leaves files unchanged, and Inspect and fix
permits corrections only for the selected format. Reconfirm scope before a
proposed fix requires inspection or corrections in an excluded format.

## Implement at the source of truth

Apply approved fixes to authored sources, shared generators and gates,
examples, schemas, models or profiles as applicable. A generated-output-only
patch is not a fix. Preserve published identifiers, anchors, normative force,
permissions and exception conditions unless an approved technical change
explicitly accounts for compatibility.

Run `marc-writer` with its guide and the `claudism-killer` pass on each batch of
revised prose, authored reports included, before counting the wording as
applied, and record the counts for each edited passage. Use `drawio-skill` for
editable figure work and `opcua-model-review` for model conformance. Recheck
that editorial substitutions preserve the actual actor, action and evidence
level.

Check free space before a large write or generation. After a failed write, list
zero-byte and partial tracked files; restore an unchanged file from the base and
rebuild a file that held uncommitted edits by replaying the edits you recorded
for it.

A defect owned by the pinned renderer or a shared template belongs in its
owner's tracker. Reproduce it on the pinned version and record the version, a
minimal reproduction and a workaround. Search the tracker for duplicates and
file where the user directs. Report any assignment right you lack. When the
renderer's source repository answers 404, assume missing access and reproduce
from the pinned build. When the user declines a repository-level workaround,
keep the finding open with that decision recorded; do not apply the workaround
to generated output alone.

## Information-preservation audit

Compare against the fixed base selected in the review contract, not a moving
working-tree snapshot. Account for every useful deleted fact, requirement,
example or explanation:

| Disposition | Evidence needed |
|---|---|
| Moved | Exact destination containing the information |
| Duplicate | Retained authoritative location and equivalent meaning |
| Superseded | Approved reason and replacement contract or explanation |
| Intentional removal | Explicit approval and effect on readers or implementations |

For a removal audit, report accidental loss without editing. In approved-fix
mode, restore accidental loss before closing the change. Check small operational
facts as well as major requirements, including actor names, timing, defaults,
failure behavior and Optional qualifications. A shorter rewrite does not
justify deletion.

A merge or conflict resolution is also a removal source. After resolving
conflicts, compare the result with both parents and give every requirement,
assertion or example the resolution dropped one of the dispositions above.

## Regenerate and verify

Discover this repository's dependency order and gates; do not assume one
specification family's command names apply everywhere. Regenerate all dependent
artifacts after approved source changes. Where the repository derives a
requirement ledger and CTT cases, regenerate both after normative edits and
update exact-profile reconciliation expectations. Register each new check in
every list that enumerates checks, such as runner target lists and workflow
steps, and confirm it by diffing the test files against those lists. Group
approved edits into batches by dependency level and run one integrated
regenerate, render and reread cycle per batch.

A check present in the repository is not evidence that CI ran it. Confirm that
the publication workflow invokes each applicable gate after rendering and before
commit or upload, and inspect uploaded artifacts for the sidecars those gates
create. Record local and CI results separately.

Check generation determinism before running gates that regenerate files, so
those gates cannot hide stale checked-in output. Rerun the determinism check and
the full gate after any merge or rebase that brings in generator changes.
Serialize commands that rewrite tracked fixtures; never run those tests
concurrently. After a gate rewrites tracked files, classify each diff as content
or line-ending-only, restore the line-ending-only files to the base bytes, and
write edits in the repository's line-ending policy. Preserve explicit failure
output and address the cause rather than masking it with a successful fallback.

Render and reread changed clauses, their neighboring explanation and cross-part
references. Reinspect affected figures. Repeat uncovered or changed
passes until every in-scope clause and figure is accounted for, each defect is
fixed or explicitly deferred, and the ledger refers to the current composed
output. Recheck the information-preservation audit after the final rewrite.

## PR feedback and authorized publication

For PR feedback, map each thread and each review body to its finding, decision,
source change and verification. Treat a reviewer's technical proposal as
evidence to assess, not automatic authority to change the contract. Reply in
the existing thread with the action actually taken. Resolve only after the fix
is verified; leave unresolved technical decisions open with the reason.

Before publishing, reconcile the staged set (tracked changes and untracked
files) with the authorized scope and name each exclusion with its reason. Scan
added archives for integrity and credential content, and confirm that the
remote tree holds every artifact the PR text cites.

After an authorized push, confirm that the remote head equals the commit you
pushed, then poll that revision until a CI conclusion exists and inspect it. A
watcher exiting successfully is not evidence that CI passed.
A check list that stays empty means no CI ran: name the cause, such as a
conflicting PR that suppresses pull-request workflows or a path filter, and
report no conclusion. Report failed, pending, skipped or unavailable checks
explicitly.
After each push, re-read every review body as well as the threads, because a
re-review can post findings without a thread, and report any re-review still
pending. Never infer publication approval or certification from green CI.

Close with the implemented and deferred finding IDs, current source and render
revisions, validation evidence, removal dispositions and remaining decisions.
Do not present a partially reviewed release set as ready.
