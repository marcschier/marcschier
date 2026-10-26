# xregistry-writing

Write specifications, Primers and supporting documentation in the style of
upstream `xregistry/spec`. The skill distinguishes implementation-facing
reference material from explanatory prose and sets review criteria for
detail, terminology, examples and diagrams.

Read the [skill](SKILL.md) for the workflow and the
[upstream analysis](references/upstream-style.md) for the complete corpus
inventory and pinned source citations.

## Install

Install the plugin from the marketplace:

```powershell
copilot plugin marketplace add marcschier/marcschier
copilot plugin install xregistry-writing@marcschier
```

Or install the bare skill into a repository, pinned to the current `main`:

```powershell
$revision = gh api repos/marcschier/marcschier/commits/main --jq .sha
gh skill install marcschier/marcschier skills/xregistry-writing --pin $revision --scope project --agent github-copilot
```

## Use

```text
Use xregistry-writing to draft this domain specification.
Preserve the supplied requirements and match the upstream level of detail.

Review this Primer against xregistry-writing without editing it.
```

The skill preserves normative meaning and distinguishes examples from
requirements. It does not invent technical decisions or rewrite generated
artifacts to match a prose style.
