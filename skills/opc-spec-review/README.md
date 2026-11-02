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

Register the marketplace and install the review and prose skills:

```powershell
copilot plugin marketplace add marcschier/marcschier
copilot plugin install opc-spec-review@marcschier
copilot plugin install marc-writer@marcschier
copilot plugin install claudism-killer@marcschier
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

Install the companions separately even when using a bare skill.

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
It does not certify implementations or confer standards approval.

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
copilot plugin update claudism-killer@marcschier
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
