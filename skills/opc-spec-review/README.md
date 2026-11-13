# OPC specification review

Review an entire OPCF-Members specification repository or a named subset using
the editions its publisher composes. The skill connects clause-by-clause review
and figure inspection to source manifests, technical contracts and publication
dependencies. It supports read-only review, revision planning, approved fixes,
information-removal audits and PR feedback.

Repository instructions supply the build and validation commands. The skill
does not assume that every repository uses the same tool version or gates.
Review alone leaves sources and generated artifacts unchanged.

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

Creating or editing figures requires `drawio-skill`, distributed separately;
use its provider's installation instructions. These companions are explicit
dependencies, not bundled or installed automatically. The review skill checks
availability before entering the relevant branch.

From a local clone, register the bare skill with:

```powershell
copilot skill add .\skills\opc-spec-review
```

Install branch-specific companions separately even when using a bare skill.

### Specification style authority

For every specification style review, proposal or rewrite, read `SKILL.md`,
`rules.md` and `examples.md` from
`<repository root>/skills/opcua-spec-style/` in the repository being reviewed.
Record that repository's revision and the paths read, with file hashes or dirty
state when they differ from that revision. If the directory or any file is
missing or unreadable, report the path and stop before the affected work;
there is no host-resolved or remote fallback.

The [temporary safeguards](references/style-overrides.md) take precedence
over conflicting guidance and remain until independently retired with evidence.
The style skill owns specification prose, applicable normative sources own
technical facts, and the repository's authoring contract and pinned Publisher
own syntax and composition. Missing files block the affected branch. Optional
`marc-writer` and its companions may assist with reports or plans, not
specification prose.

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
