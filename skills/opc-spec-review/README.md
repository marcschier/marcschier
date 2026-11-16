# OPC specification review

Review an entire OPCF-Members specification repository or a named subset using
the editions its publisher composes. The skill connects clause-by-clause review
and figure inspection to source manifests, technical contracts and publication
dependencies. It supports read-only review, revision planning, approved fixes,
information-removal audits and PR feedback.

Repository instructions supply the build and validation commands. The skill
does not assume that every repository uses the same tool version or gates.
Review alone leaves sources and generated artifacts unchanged.

Every draft, rewrite or proposed revision ends with a mandatory final
information-preservation audit before completion. Compare the fixed baseline
inventory with the final text and current in-scope publication, record retained
homes or approved removals, and leave unresolved loss or missing evidence open.
Passing checks do not replace this audit.

## Install

Register the marketplace and install the review skill:

```powershell
copilot plugin marketplace add marcschier/marcschier
copilot plugin install opc-spec-review@marcschier
```

For model or NodeSet conformance questions, also install:

```powershell
copilot plugin install opcua-model-review@marcschier
```

For implementer-guide writing, also install all three writing companions:

```powershell
copilot plugin install marc-writer@marcschier
copilot plugin install microsoft-writing-style@marcschier
copilot plugin install claudism-killer@marcschier
```

Creating or editing figures requires `drawio-skill`, distributed separately;
use its provider's installation instructions. These companions are explicit
dependencies, not bundled or installed automatically. The review skill checks
availability before entering the relevant branch.

From a local clone, register the bare skill with:

```powershell
copilot skill add .\skills\opc-spec-review
```

Install branch-specific companions separately even when using a bare skill.

### Specification prose and structure

The packaged [prose guidance](references/specification-style.md) is the
specification-writing authority for this skill. It incorporates numbered
prose rules, an example for every rule, and the information-preservation
safeguards. It does not replace technical authorities or the target
repository's authoring contract and pinned Publisher.

Use the concise [content structure](references/templates.md) for a section
outline. It is supplemental; the official Sample remains authoritative for
headings, directives and publisher behavior. The adjacent
[template review reference](references/template.md) contains publication
checks.

### Implementer guides

Before removing explanation that connects the normative clauses or introduces
the modelled technology, the review offers the user retention in informative
subsections, including supporting examples and diagrams. This keeps the
specification's audience and forward reading flow unchanged. The original
stays while a choice is pending; informative labels never downgrade normative
facts. The choice follows the packaged
[informative-context guidance](references/specification-style.md#informative-context).

Each selected spec has an informative `implementer-guide.md` beside `spec.md`.
The shared [guide workflow](references/implementer-guide.md) retains useful
explanations, rationale and examples removed during review, while normative
facts remain in the specification or exact applicable normative references.
Existing guides are maintained, not overwritten with a deletion log.

Only guide writing uses `marc-writer`, `microsoft-writing-style` and
`claudism-killer` in these review workflows. The guide is a developer booklet:
natural explanatory prose from overview to detail, short concept headings,
worked examples and GitHub-rendered diagrams, with references to `spec.md`
instead of duplicated requirements. An independent developer rubber-duck
review checks the final guide separately from specification acceptance.
Guide writes need agreed file scope and permission; read-only reviews report
missing guides and proposed retention destinations without creating files.

## Use

```text
Use opc-spec-review to review this entire OPCF-Members repository without edits.
Include the coordinated release set and flag any inaccessible publication format.

Review only Part-A and Part-B from this repository's manifests.
Read other parts only to resolve their dependencies; keep edits out of scope.

Plan revisions for the located findings. Wait for approval before changing files.

Implement the approved plan, regenerate dependent artifacts and audit useful
information removed since the agreed base revision.

Audit removals since the agreed base without editing files.
```

`Part-A` and `Part-B` are synthetic names, not repository defaults. If selection
is ambiguous, the skill asks rather than guessing. It records coverage at four
levels and gives per-spec and coordinated-set verdicts with evidence limits.
It asks whether to include PDF and Word inspection and fixes, separately for
each format: Exclude (default), Inspect only, or Inspect and fix. With no answer,
both formats remain excluded, even for a whole-repository review or general
fix request. Included PDF inspection covers content and layout/rendering,
including print exports; Word inspection covers DOCX content and fields, with
the visual page range agreed separately. Inspection alone does not authorize
fixes. Dark-mode behavior remains outside the scope.

DOCX review checks the artifact revision and hash before using stored field
results or Word evidence. Word visual pagination review uses the available
Computer Use workflow; blocked UI access is a review limitation, not evidence
of a publication defect. The skill does not certify implementations or confer
standards approval.

The [skill](SKILL.md) contains the scope and reporting contract.
[Review criteria](references/review.md) cover composed editions and release
dependencies; [revision closure](references/revisions.md) covers approval,
information preservation, regeneration and PR feedback.

The optional [review canvas](https://github.com/marcschier/marcschier/tree/main/extensions/opc-spec-review) is a separate
application extension with the same name. The skill does not require that
extension. Use a host's browser or available preview tools for visual inspection;
record missing visual capabilities instead of pretending they were exercised.

## Update and validation

Refresh the catalog and installed plugins with:

```powershell
copilot plugin marketplace update marcschier
copilot plugin update opc-spec-review@marcschier
```

In a running CLI session, use `/skills reload` and
`/skills info opc-spec-review`. An application host may provide its own reload
controls; CLI catalog updates alone do not prove that host has reloaded skills.

Run the package contract checks from the repository root:

```powershell
python -B -m unittest discover -s skills\opc-spec-review\tests -v
```

The [acceptance scenarios](tests/acceptance.md) exercise review behavior with
synthetic evidence. Contract tests check packaging and references; they do not
prove that an agent inspected a publication or made correct technical judgments.
