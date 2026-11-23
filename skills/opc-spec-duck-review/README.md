# OPC specification comprehension review

`opc-spec-duck-review` pairs an independent first-time reader with an expert
technical editor. The reader knows OPC UA and the agreed prerequisites, but
learns the target specification in reading order.

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

Both reader and editor must read the integrated prose guidance, its per-rule
examples and information-preservation safeguards, and the concise content
structure packaged with `opc-spec-review`. Resolve that package through the
host, not an assumed sibling directory. If any required reference is
unavailable, report the path and stop before style review, proposal or writing.
The safeguards govern preservation, the examples do not override the guidance,
and none gives the reader prior target-domain knowledge. Technical normative
sources and the repository's authoring and Publisher contract retain their
respective authority.

For authorized prose edits, the coordinator can ask whether to add the
optional `opc-ua-writing-style` pass. The choice applies only to the editor
and keeps any existing `claudism-killer` pass. To use it, install
`opc-ua-writing-style@marcschier` separately and use an up-to-date
`opc-spec-review` package.

Each spec also has an informative `implementer-guide.md` beside `spec.md`.
Before moving connecting context out of the specification, the editor offers
the user an informative-subsection option under the shared prose guidance.
Those explanations, examples and diagrams keep the specification's existing
audience and forward reading flow; the specification reader reviews them
without the guide. Pending choices preserve the original, and informative
labelling cannot downgrade requirements.
The coordinator and editor read the shared `references/implementer-guide.md`
from the resolved review package to preserve useful removed explanations and
maintain a distinct developer booklet. Guide writing requires `marc-writer`,
`microsoft-writing-style` and `claudism-killer`; install those marketplace
companions as documented by `opc-spec-review`. Missing dependencies block guide
writing, not independent review work. A separate fresh developer reader
rubber-ducks the final guide, examples and GitHub-rendered diagrams.
The specification reader never receives the guide or guide-review history.
Guide-only retention does not replace normative specification content.
Read-only work reports missing or stale guides and proposes changes; guide
creation or maintenance requires explicit file scope and edit permission.

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
source-plus-HTML coverage, then establishes edit permission and confirms
prerequisites, including any preceding parts. The editor can research the
target domain.

Separate agents are required; distinct models can be selected when supported
and requested. The editor retains history; every full pass starts with a
fresh first-time reader who carries forward only what each representation has
taught across consecutive batches. Targeted revision re-reads do not count
as independent acceptance. The first pass prioritizes satisfying the reader's
clarity requests; later passes permit evidence-based challenges and user
tie-breaks. Technical meaning and edit permissions remain protected in every
pass.

Coverage includes every sentence and additional content units, not a sample.
At the first use that depends on a project-specific name, the reader must
already know what it is, where it belongs, and why it matters there. This
applies in prose, tables, figures, examples, and generated content. Later
definitions and links can add detail, but they cannot substitute for that
orientation or erase a recorded obstacle.

Separately, the reader flags invented compounds that hide a relationship or
action, even when the meaning is guessable. The reader asks for plain
wording while leaving established terms, exact identifiers, and quotations
intact.

The reader also flags information repeated within the specification or
restated from an applicable specification. Each confirmed finding cites
the authoritative clause or table and proposes the smallest safe change.
The editor verifies candidates and preserves distinct requirements and
useful reader context.

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
