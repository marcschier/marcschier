# Composed-edition review

The manifest and include tree define the publication. Inventory authored clauses,
generated references, terminology, profiles, conformance units (CUs), NodeSet
tables, annexes, examples and official figures. Include complete HTML and every
other shipped format that the review contract covers.

## Coverage ledger

Give every composed clause a row, including generated clauses and annexes.
Track figures separately so an uninspected image cannot disappear inside a
completed chapter. Map each row to its source or generator and current output.

| Spec / clause | Source or generator | Render revision / hash | Route | Structure | Detail | Words | Evidence / findings |
|---|---|---|---|---|---|---|---|
| Synthetic Part A / 4 | Authored source | Recorded artifact hash | Pending | Pending | Pending | Pending | Not yet read |

Use pending, reviewed or blocked for each level; a blocked cell needs a reason.
Record not-applicable only when the content and scope justify it. The levels
mean:

1. **Route:** skim the complete edition and establish its reading route,
   prerequisites and cross-part responsibilities.
2. **Structure:** assess section hierarchy, order and teaching progression.
   Determine whether definitions arrive before use and responsibilities before
   protocol detail.
3. **Detail:** read every paragraph, table, snippet and annex in context,
   including generated content. Follow pagination and fetch omitted ranges;
   truncated reads do not count as coverage.
4. **Words:** check terminology, qualifications, normative force and consistency
   at word level against the technical sources and other parts.

A search assists these passes but does not replace them. Record the exact
covered range and remaining gap after interrupted reading. Reopen affected
cells after source changes or regeneration; complete only when their evidence
matches the current output.

## Explanation and reading order

Assess whether the publication teaches the mechanism around its precise
contracts. Prefer causal explanatory prose where the reader must understand
why a rule exists. Retain signatures, enumerations, option sets, actual
algorithms and profile matrices. Bullet count alone is not a quality measure.
Preserve strong chapters and revise proportionately.

At difficult boundaries, trace a concrete successful interaction and a relevant
failure. Check identity and authority, inputs and outputs, omitted or default
values, lifecycle transitions, rollback, retirement, retry, partial failure and
diagnostics where applicable. These are questions to apply to the model, not
mandatory headings or an instruction to invent unsupported behavior.

Evaluate examples and figures at the points where readers must make difficult
decisions. Check technical accuracy and distribution; a large example count
cannot compensate for a missing explanation at an interoperability boundary.
Keep examples distinguishable from normative requirements.

## Contract reconciliation

Compare prose and figures with normative models, schemas, vocabularies,
profiles, CU definitions, tests and cited base standards. Trace producer and
consumer responsibilities across parts. Resolve apparent contradictions using
the actual predicates and lifecycle levels: candidate versus invocation,
precommit versus activation, active versus exact versus default identity.

Preserve conditional obligations and Optional qualifications. An obligation
under an existing Optional ancestor is different from requiring that ancestor.
Terminology alone does not establish a contradiction. Record competing
interpretations and their evidence; obtain a technical decision where the
sources do not settle it. Editorial work cannot choose a new contract.

For model questions, use `opcua-model-review` and reconcile its complete ledger
with the publication findings. Static checks do not establish runtime behavior.
Keep unexecuted tests, unavailable implementations and unverified deployment
assumptions visible in the runtime-evidence category.

## Figures, layout and shipped formats

Inspect every official figure in full, including labels, arrows, legend,
caption, surrounding explanation and cross-references. Record each figure's
source, rendered evidence, disposition and any unreadable region. Use the
actual artwork rather than inferring it from a filename or nearby prose.

Inspect complete HTML at wide and narrow widths, its navigation and anchors,
and the light/dark styles the publication actually supports. Distinguish an
embedded preview's overrides from the shipped theme. If a `file://` preview
cannot load assets, verify through a task-owned loopback static server before
reporting a layout defect. Bind locally, verify readiness and stop the specific
task-owned process after inspection.

Inspect other shipped formats as agreed. DOCX XML field inspection can establish
field or reference content, not visual pagination or Word sign-off. State which
formats could not be opened or visually inspected and how that limits release
assessment. Never turn an inaccessible figure or format into an implicit pass.

## External dependencies and publication closure

For each normative external dependency, verify the pinned edition,
authoritative status, accessibility, date and current proposal or release
state. Record evidence and the date checked. Local parts may form a valid
simultaneous co-release; assess the coordinated release set rather than
requiring every local part to have been published independently.

A merged change or GitHub release flag does not establish standards approval.
An immutable draft pin preserves identity, not final status. Preserve draft
labels and actual identifiers; record approval or availability blockers rather
than manufacturing final identities.

Distinguish source-edit links and history chrome from normative dependencies
on PRs, commit IDs or mutable branches. Check that edition-stable publication
links resolve models, schemas, contexts and examples as well as document pages.
Report a broken publication dependency with its consumer and consequence,
not merely a count of links.
