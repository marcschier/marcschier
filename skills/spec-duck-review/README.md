# Specification comprehension review

`spec-duck-review` applies the forward-reading workflow of
`opc-spec-duck-review` to specifications outside OPC UA. An independent reader
judges every sentence and other content unit in order. An editor researches
the intended meaning and makes authorized changes. A fresh reader checks the
revised edition without seeing earlier findings.

## Install

```powershell
copilot plugin marketplace add marcschier/marcschier
copilot plugin install spec-duck-review@marcschier
```

From a local clone, register the bare skill with:

```powershell
copilot skill add .\skills\spec-duck-review
```

The host must support independent agents. No domain-specific plugin,
service, or publishing tool is required for a source-only review.

## Use

```text
Use spec-duck-review to review this job scheduling specification.
The reader knows how Unix processes work but has not used this scheduler.
The editor may consult the cited operating system manuals.
Review the source and the published PDF. Report findings without editing.
```

If no background is given, the skill asks once. With none supplied, the
reader assumes technical literacy and no domain-specific knowledge. Source
only is the default; select a published format or a companion implementer
guide explicitly. Review alone does not authorize edits.

The [skill](SKILL.md) defines the workflow and completion criteria.
The [role instructions](references/roles.md) define what each agent may see.
