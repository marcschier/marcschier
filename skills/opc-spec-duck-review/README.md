# OPC specification comprehension review

`opc-spec-duck-review` pairs an independent OPC UA reader with an expert
technical editor. It checks whether an OPC UA expert can learn the domain
from the specification, sentence by sentence, rather than supplying missing
context from prior domain knowledge.

Use `opc-spec-review` for correctness, style, and publication audits. This
skill provides a separate comprehension dialogue, not a substitute for model
validation or certification.

## Install

```powershell
copilot plugin marketplace add marcschier/marcschier
copilot plugin install opc-spec-duck-review@marcschier
copilot plugin install opc-spec-review@marcschier
```

The host must support independent agents and provide both the OPC UA
knowledge-base MCP tools and access to https://reference.opcfoundation.org/.
These services are not bundled or installed automatically. Both agents must
have access; a live OPC UA server connection is not the knowledge base.
Missing dependencies are reported before the affected work proceeds.

Both reader and editor must read `SKILL.md`, `rules.md` and `examples.md`
from `<repository root>/skills/opcua-spec-style/` in the repository being
reviewed, plus the temporary safeguards packaged with the resolved
`opc-spec-review` skill. Record the target repository revision and paths read,
with file hashes or dirty state when they differ from that revision. Resolve
the review package through the host, not an assumed sibling directory.
If any required directory or file is unavailable, report the path and stop
before style review, proposal or writing; do not use a fallback style skill.
The safeguards override conflicting upstream guidance, and the upstream rules
outrank contradictory examples. They do not give the reader prior target-domain
knowledge. Technical normative sources and the repository's authoring and
Publisher contract retain their respective authority.

For local development, register the bare skill:

```powershell
copilot skill add .\skills\opc-spec-duck-review
```

## Use

```text
Use opc-spec-duck-review for a fresh-reader review of this specification.

Use opc-spec-duck-review for Part 1 and Part 2, including published HTML.
Allow the editor to fix prose within those source folders.

Use opc-spec-duck-review for source-only findings without edits.
```

The skill first asks for the selected specifications and source-only versus
source-plus-HTML coverage, then establishes edit permission. The reader knows
OPC UA and the agreed dependent OPC UA specifications, but not the target
domain. The editor can research that domain.

Separate agents are required; distinct models can be selected when supported
and requested. The editor retains history while every new full pass gets a
fresh reader. The first pass prioritizes satisfying the reader's clarity
requests; later passes permit evidence-based challenges and user tie-breaks.
Technical meaning and edit permissions remain protected in every pass.

Coverage includes every sentence and additional content units, not a sample.
A final unchanged edition needs a complete fresh pass with no outstanding
issues and editor agreement. Permission gaps, unavailable evidence, repeated
disputes, and resource limits produce an explicit incomplete outcome rather
than forced agreement. A findings-only run does not pretend revisions were
applied or accepted.

Before completion, the editor and coordinator perform the mandatory final
information-preservation audit from the resolved `opc-spec-review` package's
`references/revisions.md`. Compare the fixed baseline inventory with final text
and in-scope publication, including proposed revisions in findings-only mode.
Missing audit guidance, baseline evidence or unresolved loss prevents
acceptance. Keep audit history from the fresh reader; corrections require a
fresh full pass and another final audit.

The [skill](SKILL.md) defines orchestration and closure;
[role instructions](references/roles.md) define the reader and editor.
Detailed ledgers stay in an authorized session artifact location.

## Validation and updates

```powershell
python -B -m unittest discover -s skills\opc-spec-duck-review\tests -v
copilot plugin marketplace update marcschier
copilot plugin update opc-spec-duck-review@marcschier
```

Reload skills through the current host after updating the installed files.
The package checks verify packaging and instruction contracts.
[Acceptance scenarios](tests/acceptance.md) describe behavioral evaluation;
passing textual checks does not prove that an agent reviewed every sentence.
