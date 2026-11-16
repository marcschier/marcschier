# Implementer guide workflow

Each selected specification has a companion `implementer-guide.md` beside its
`spec.md`. Create a missing guide and maintain an existing one during authorized
revisions. In read-only, plan or removal-audit mode, report a missing or stale
guide and propose located additions without editing. Approval to edit a
specification does not silently expand the file scope: include its guide in
the agreed scope or request that permission before moving information.
When the specification changes, revisit the guide's affected explanations,
examples, diagrams and clause links against that same edition, even if the
latest edit removes no prose. Preserve unrelated authored guide content.

## Authority

The guide is an informative developer booklet, not a second specification.
Link to the same folder's `spec.md` and its actual clause anchors for normative
content. Explain implementation consequences without duplicating requirement
tables or inventing obligations, result codes or conformance claims.
Illustrative code and design choices remain visibly non-normative.

Required behavior, definitions needed to interpret requirements, conditions,
exceptions and other contract facts remain accessible in the specification's
publication or an exact applicable normative reference. A guide-only home
does not satisfy that retention obligation. The guide can retain useful
informative explanations, rationale, worked examples and implementation
advice removed from specification prose. When a passage mixes both kinds,
retain its contract facts normatively; adapt developer-specific explanation
for the guide only after the informative-context decision below.

Before moving connecting context, apply the
[informative-context decision](specification-style.md#informative-context).
The user may retain that explanation, examples and diagrams in an informative
subsection for the specification's unchanged audience. A guide destination
does not justify removing context that audience still needs. Developer-specific
teaching belongs here; the guide remains a distinct document, not a reason to
make the specification normative-only.

## Preservation

Before removing prose, inventory every useful implementer explanation,
example, diagram, implementation consequence and rationale alongside the
normative facts in the fixed baseline. For each item selected for the guide,
record its existing or proposed guide section and corresponding specification
clause. Record context retained in specification subsections as specification
homes; do not require a duplicate guide copy.
Adapt material into a coherent narrative rather than appending a deletion
dump. Keep removal history and review dispositions in authorized review
artifacts, not in the booklet.

Move useful material only after its guide destination is present and checked.
Verify equivalent meaning, scope and qualifications in the final guide; a
planned destination or transient chat explanation is not retained content.
An approved duplicate or intentional removal still needs its recorded
disposition. Missing baseline material or permission leaves the retention
item open rather than authorizing deletion.

## Writing

Resolve and use `marc-writer`, `microsoft-writing-style` and `claudism-killer`
through the host's skill mechanism. Read their actual instructions and
`marc-writer`'s `STYLE.md`; do not assume installed sibling directories.
Use Microsoft's developer/implementer content route, compose with
`marc-writer`, then run `claudism-killer` and recheck technical meaning.
If a skill or required reference is unavailable, report the missing dependency
and stop guide writing or style acceptance; continue only independent work.
Within these review workflows, these three writing skills apply only to the
implementer guide, never to specification prose or review reports.

The audience is a developer implementing the specification, not a standards
editor. Write natural, connected prose in booklet/book form, moving from a
high-level mental model to concepts, interactions and implementation detail.
Use explanatory rather than imperative wording; avoid a command checklist or
an RFC-style requirements voice. This developer-booklet brief governs register
and headings when a generic writing pattern suggests otherwise.

Use short noun or concept headings, such as Overview, Architecture, Sessions,
Lifecycle or Errors, with grouping headings where helpful. Titles and headings
are not sentences or instructions. Choose sections for the actual model rather
than imposing every example heading on every guide.

Include rich worked examples and diagrams that explain real mechanisms,
interactions and edge cases. Introduce concepts before relying on them and
connect examples to the relevant specification clauses. Check examples
against the current contract; disclose illustrative assumptions without
claiming execution or interoperability evidence that was not obtained.

## Presentation

Use ordinary GitHub-rendered Markdown, not Specification Publisher syntax.
Put Mermaid diagrams in fenced `mermaid` blocks in the guide, or link adjacent
Markdown diagrams that GitHub renders. For draw.io work, use `drawio-skill`,
retain the editable source and embed a GitHub-viewable SVG or PNG export.
Check diagram labels, references and visible exports; an editable file alone
is not a rendered diagram. Keep the guide and its assets outside Publisher
inputs unless a separate publication change is explicitly authorized.

## Rubber-duck review

After writing and the style pass, have a separate fresh developer reader
review the complete guide from beginning to end, including examples, diagrams
and linked normative clauses. The reader receives the current guide,
referenced specification and declared prerequisites, not prior findings,
deleted passages or editor explanations. Keep this context separate from the
specification's fresh reader: a guide must not repair or conceal an unexplained
specification contract during specification review.

The developer reader explains the implementation model and representative
flows, flags missing premises or unnatural transitions, and checks that advice
is distinguishable from requirements. The editor reconciles feedback with the
specification and revises only with permission. Re-review changed passages in
context, then require a fresh complete reading of the final unchanged guide.
If independent contexts or visible diagram evidence are unavailable, report
the guide review incomplete rather than simulating acceptance.

## Completion

Before the final information-preservation audit, reconcile the baseline
inventory with both the normative publication and the guide. Record exact
guide destinations for informative material separately from normative homes.
Check relative links against current anchors, GitHub diagram presentation,
example consistency and regeneration persistence where tools touch the folder.
Report each guide's path, revision or hash, retained items, developer-reader
outcome and gaps. Specification acceptance and guide acceptance are separate;
neither a readable guide nor a passing build closes a missing normative fact.
