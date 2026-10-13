# Claudism Killer

An agent skill for editing Markdown and other prose that reads as machine-written.
It checks stock phrasing and repeated sentence constructions, then rewrites or
cuts confirmed tics in the author's register. It also works on pasted blog posts,
PR descriptions, specifications, emails, marketing copy, and talks.

The catalogue is an editing aid, not evidence of who wrote a text. Styleguide
choices, domain vocabulary, and deliberate rhetorical devices can be kept.

## Install

### As a plugin

```powershell
copilot plugin marketplace add marcschier/marcschier
copilot plugin install claudism-killer@marcschier
```

Update with `copilot plugin update claudism-killer`.

### As a skill only

From a clone of this repository:

```powershell
copilot skill add .\skills\claudism-killer
```

Use `/skills reload` to refresh skills in a running session, and
`/skills info claudism-killer` to inspect the skill.

## Use

Ask for an edit, with the document paths and a styleguide if you have one:

```text
Remove the Claude-isms from README.md.
De-slop the Markdown documents in docs. Preserve our terminology and code examples.
Make this post sound like me; use STYLEGUIDE.md and my other posts as references.
```

For a read-only diagnosis:

```text
Why does this paragraph read as machine-written? Diagnose it without editing.
Audit this document for stock phrasing against STYLEGUIDE.md; do not change files.
```

An edit pass reports the findings and replacements, applies edits to the selected
files (or returns revised pasted text), and gives measured before/after counts.
It also identifies protected phrasing and claims that need verification.

Code blocks, inline code, link destinations, and frontmatter stay unchanged unless
explicitly included in the request. The skill does not run on every Markdown write
and does not do automatic word substitution.

See [SKILL.md](SKILL.md) for the workflow and catalogue.
