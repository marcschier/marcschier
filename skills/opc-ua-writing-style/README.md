# OPC UA writing style

Draft or edit OPC UA specification prose in the voice of published companion
specifications. The [skill](SKILL.md) covers paragraph breaks, sentence rhythm,
punctuation and level of detail. It preserves technical meaning and the
document's structure while correcting awkward English.

The [corpus analysis](references/corpus-analysis.md) records the source coverage,
measurements and examples behind the guidance.

## Install

```powershell
copilot plugin marketplace add marcschier/marcschier
copilot plugin install opc-ua-writing-style@marcschier
```

Or install the bare skill into a repository, pinned to the current `main`:

```powershell
$revision = gh api repos/marcschier/marcschier/commits/main --jq .sha
gh skill install marcschier/marcschier skills/opc-ua-writing-style --pin $revision --scope project --agent github-copilot
```

## Use

```text
Use opc-ua-writing-style to revise this draft companion specification.
Preserve the requirements and layout; edit only the prose.
```
