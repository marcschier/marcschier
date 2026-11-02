# Revision and closure

Keep the review result separate from the revision plan. A finding establishes
evidence for a change; it does not authorize implementation or settle a
technical choice.

## Plan and approval

Map every finding to its proposed source change, affected artifacts,
dependencies, owner or decision, and checks. Order changes by dependency.
Separate editorial corrections from technical decisions and publication work.
Record deferred findings and the consequence of deferral.

Present the plan for approval before implementation unless the user has already
authorized those specific fixes. Read-only review, plan and removal-audit modes
leave sources and generated artifacts unchanged. Publishing and merging each
require explicit authorization; approving local edits does not authorize either.

## Implement at the source of truth

Apply approved fixes to authored sources, shared generators and gates,
examples, schemas, models or profiles as applicable. A generated-output-only
patch is not a fix. Preserve published identifiers, anchors, normative force,
permissions and exception conditions unless an approved technical change
explicitly accounts for compatibility.

Use `marc-writer` with its guide and `claudism-killer` pass for revised prose.
Use `drawio-skill` for editable figure work and `opcua-model-review` for model
conformance. Recheck that editorial substitutions preserve the actual actor,
action and evidence level.

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

## Regenerate and verify

Discover this repository's dependency order and gates; do not assume one
specification family's command names apply everywhere. Regenerate all dependent
artifacts after approved source changes. Where the repository derives a
requirement ledger and CTT cases, regenerate both after normative edits and
update exact-profile reconciliation expectations.

Check generation determinism before running gates that regenerate files, so
those gates cannot hide stale checked-in output. Serialize commands that rewrite
tracked fixtures; never run those tests concurrently. Preserve explicit failure
output and address the cause rather than masking it with a successful fallback.

Render and reread changed clauses, their neighboring explanation and cross-part
references. Reinspect affected figures and layouts. Repeat uncovered or changed
passes until every in-scope clause and figure is accounted for, each defect is
fixed or explicitly deferred, and the ledger refers to the current composed
output. Recheck the information-preservation audit after the final rewrite.

## PR feedback and authorized publication

For PR feedback, map each thread to its finding, decision, source change and
verification. Treat a reviewer's technical proposal as evidence to assess, not
automatic authority to change the contract. Reply in the existing thread with
the action actually taken. Resolve only after the fix is verified; leave
unresolved technical decisions open with the reason.

After an authorized push, inspect the actual CI conclusion for the pushed
revision. A watcher exiting successfully is not evidence that CI passed.
Report failed, pending, skipped or unavailable checks explicitly. Never infer
publication approval or certification from green CI.

Close with the implemented and deferred finding IDs, current source and render
revisions, validation evidence, removal dispositions and remaining decisions.
Do not present a partially reviewed release set as ready.
