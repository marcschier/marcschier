# microsoft-writing-style

Apply the wording rules of the Microsoft Writing Style Guide to developer
documentation, reference documentation, and specifications. The skill decides
words and sentences: voice, grammar, terminology, global and inclusive English,
punctuation, and numbers. It deliberately does not define formatting, layout,
document structure, or product and publishing-platform conventions, so another
guide or template can own those without conflicting rules.

The skill first asks who the audience is. Readers who learn or do something get
the developer content route; readers who look something up get the reference
documentation route, which adds rules for wording equivalent entries
consistently, stating Boolean results, defaults, and error conditions exactly,
and writing testable normative text. Which fields and sections an entry
contains stays with the project's template.

Read the [skill](SKILL.md) for the workflow. The rules live in
[references](references/); the bundled term list and term collections cover the
A–Z word decisions.

## Modes

| Mode | Behavior |
|---|---|
| Write | Supplies wording rules while you or another skill drafts. With marc-writer, its style guide drives structure, argument, and voice and wins on any point it addresses; this skill settles the remaining wording. |
| Review: autopilot | Runs the check and rewrites the document in one pass, then reports every change that could affect meaning. |
| Review: interactive | Summarizes findings by category and severity and applies only the categories you select. |
| Critique | Reports findings without editing the document. |

A review never changes facts, identifiers, code, quoted text, or normative
keywords. It flags them for a decision instead.

## Install

Install the plugin from the marketplace:

```powershell
copilot plugin marketplace add marcschier/marcschier
copilot plugin install microsoft-writing-style@marcschier
```

Or install the bare skill into a repository, pinned to the current `main`:

```powershell
$revision = gh api repos/marcschier/marcschier/commits/main --jq .sha
gh skill install marcschier/marcschier skills/microsoft-writing-style --pin $revision --scope project --agent github-copilot
```

## Use

```text
Use microsoft-writing-style and marc-writer to draft the getting-started guide
for this SDK.

Review docs/api/session.md with microsoft-writing-style and rewrite it.

Review this specification with microsoft-writing-style and let me pick what to
fix.
```
