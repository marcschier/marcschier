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

Writing skills such as [marc-writer](../marc-writer) can invoke the same editing
workflow with an author styleguide and explicitly request clean output. In that
mode, the findings and measurements remain working evidence; the delivered
artifact contains the revised prose, with unresolved factual gaps still visible.
Standalone edits keep the report described above unless clean output is requested.

Code blocks, inline code, link destinations, and frontmatter stay unchanged unless
explicitly included in the request. The skill does not run on every Markdown write
and does not do automatic word substitution.

The catalogue also checks habitual "worked" modifiers and vague assertion
language. It chooses between example, walkthrough and derivation by purpose,
and replaces vague assertions with the actual actor and action when supported.
It preserves legitimate calculations, verb uses, defined assertions and the
distinction between a declaration and verified conformance.

Behavior labels such as fail-closed, fail-fast, fail-safe, best-effort and soft
delete are also candidates. The skill prefers a sentence that states the
trigger, the action and the resulting state, and flags a label whose behavior
the passage does not supply instead of inventing a policy. Formally defined
guarantees such as exactly-once or idempotent stay when their scope and behavior
are established in the document or a referenced definition. This does not
require an implementation algorithm or a repeated definition at every use.

Synthetic [judgment cases](tests/cases.json) cover both edits and protected uses.
Run detector regressions from the repository root with:

```powershell
python -B -m unittest discover -s skills\claudism-killer\tests -v
```

See the [evaluation guide](tests/README.md) for what those checks establish.

See [SKILL.md](SKILL.md) for the workflow and catalogue.
