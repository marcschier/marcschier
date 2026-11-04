---
name: microsoft-writing-style
license: MIT
description: >
  Apply Microsoft Writing Style Guide rules for voice, grammar, word choice,
  global and inclusive English, punctuation, and numbers to technical content
  and specifications. Use for "Microsoft style", "Microsoft writing style
  guide", "write in Microsoft voice", or a request to write, edit, review,
  critique, or rewrite developer documentation, tutorials, how-to guides, code
  samples, API reference, protocol or interface specifications, schemas, and
  normative standards text. Routes by audience to developer content or
  reference documentation. Works as extra context while drafting, including
  with marc-writer, or as a review that rewrites the document (autopilot) or
  summarizes findings for the user to select (interactive). Covers wording
  only: formatting, layout, document structure, and product or publishing-
  platform conventions come from other context.
---

# Microsoft writing style

Apply the Microsoft Writing Style Guide's wording rules to technical content.
The rules here and in [references/](references/) are complete and
self-contained. Don't look them up elsewhere.

## Scope

This skill decides **words and sentences**: voice, tone, grammar, word choice,
terminology, inclusive and global English, punctuation, and numbers.

Leave these to other context, such as a project guide, publishing-platform
rules, or templates:

- Text formatting (bold, italic, code style) and capitalization of titles and
  headings.
- Document structure, section order, templates, headings, lists, and tables.
- Links, URLs, metadata, and search optimization.
- Product names, trademarks, and vendor-specific conventions.

When other context conflicts with this skill, other context wins for its own
scope. When a paired voice skill (such as marc-writer) conflicts on wording,
the author's voice wins unless it reduces clarity for the audience, breaks a
global-English rule, or uses biased language.

## Step 1: Identify the audience

Ask the user who the audience is. Offer the two routes as choices and include
what you can infer from the document or request:

- **Developer content:** readers who learn or do something. Tutorials,
  quickstarts, how-to guides, conceptual and architecture articles, samples,
  and command-line instructions.
- **Reference documentation:** readers who look something up. API reference,
  protocol and interface specifications, schemas, data models, configuration
  and command references, error catalogs, and normative standards text.

If the user names a mixed document, use reference documentation for the
reference and normative sections and developer content for the rest.

Also confirm the reader's expertise when it isn't obvious, for example
general developers, domain specialists, or implementers of a standard.

Done when the route and the expertise level are known.

## Step 2: Choose the mode

Infer the mode from the request. Ask only when it's unclear.

| Mode | When | What you do |
|---|---|---|
| Write | Drafting new content, alone or with a voice skill | Apply the rules while writing, then run the final read |
| Review: autopilot | "Rewrite", "fix", "clean up", "apply the style guide" | Run the check and apply the fixes in one pass |
| Review: interactive | "Review", "what should I improve", or the user wants to choose | Summarize findings by category and let the user select |
| Critique | "Critique only", "don't change anything" | Report findings without editing |

Done when the mode is set.

## Step 3: Load the references

Always read:

1. [references/voice.md](references/voice.md)
2. [references/grammar.md](references/grammar.md)
3. [references/word-choice.md](references/word-choice.md)
4. [references/global-and-inclusive.md](references/global-and-inclusive.md)
5. [references/punctuation-and-numbers.md](references/punctuation-and-numbers.md)

Then read the route reference:

- Developer content: [references/developer-content.md](references/developer-content.md)
- Reference documentation: [references/reference-documentation.md](references/reference-documentation.md)

For a review, also read [references/review.md](references/review.md).

Look up individual words in
[references/term-list.md](references/term-list.md) (A–Z) and
[references/term-collections.md](references/term-collections.md) (topics such
as security, cloud, units, accessibility, and AI) when a word choice isn't
settled by the core references. Search them rather than reading them whole.

Done when the core references, the route reference, and (for a review) the
review procedure have been read.

## Step 4: Do the work

**Write mode.** Draft with the core rules below in mind. When paired with a
voice skill, let that skill drive structure and voice, and use this skill to
settle wording. After drafting, run the final read in
[references/voice.md](references/voice.md#final-read) and fix what it finds.

**Review modes.** Follow [references/review.md](references/review.md) for the
chosen mode.

Done when the mode's completion criterion in this file or in review.md is met.

## Core rules

Keep these in mind while writing or reviewing. The references explain each in
detail.

1. **Lead with what matters.** Put the outcome, decision, or action first.
2. **Use fewer words.** Cut filler, *you can*, and *there is/are*. One idea per
   sentence.
3. **Sound like a person.** Warm and direct, with common contractions and
   everyday words.
4. **Write in present tense and active voice.** Use passive voice only to keep
   blame off the reader or to stress the receiver of the action.
5. **Address the reader as *you*.** Use the imperative for instructions.
6. **Pick simple, precise words.** *Use*, not *utilize*; *because*, not
   *since*; one term for each concept.
7. **Define terms and acronyms on first use.** Use industry terms the way the
   industry uses them; don't coin new ones.
8. **Write for a global reader.** Short sentences, no idioms, keep *that* and
   articles, avoid modifier stacks.
9. **Use inclusive language.** No gendered generics, no biased, ableist, or
   militaristic terms.
10. **Apply mechanics consistently.** Serial comma, numerals for 10 and up and
    for all measurements, *month day, year* dates, no Latin abbreviations.

## Completion checks

Before handing back any written or revised text, confirm:

- The content fits the chosen audience: nothing essential is undefined and
  nothing basic is over-explained.
- Each paragraph leads with its main point.
- No sentence contains *you can* that could be removed, or an avoidable
  *there is/are*.
- Every acronym is spelled out on first use, unless the audience surely knows
  it.
- No term changes name partway through the document.
- No idioms, gendered generics, or biased or militaristic terms remain.
- Numbers, dates, ranges, and units follow
  [punctuation-and-numbers.md](references/punctuation-and-numbers.md).
- For reference documentation: equivalent entries use the same wording,
  every Boolean result states its condition, every stated default, range, or
  error condition is exact, and every requirement is testable.
- For developer content: every procedure step is a complete imperative
  sentence with one action, and the sentence before each code example says
  what the code does.
- No change touched section order, headings, lists, tables, or other layout.
