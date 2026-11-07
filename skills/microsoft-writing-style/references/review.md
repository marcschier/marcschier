# Review procedures

Both review modes run the same check, in the same order, then differ in what
happens with the findings. Read the whole document before judging any part of
it.

## The check

Take the categories in this order. Earlier categories fix problems that make
later ones moot.

| # | Category | Look for | Reference |
|---|---|---|---|
| 1 | Audience fit | Content too basic or too advanced for the chosen audience; undefined terms; unstated prerequisites | [developer-content.md](developer-content.md), [reference-documentation.md](reference-documentation.md) |
| 2 | Route wording | Developer content: procedure steps that aren't imperative or hold several actions, device-specific verbs, imprecise verbs for code. Reference: inconsistent wording of equivalent entries, descriptions that restate the name, Boolean results without a condition, vague defaults, ranges, or error conditions, untestable requirements | Route reference |
| 3 | Concision | Wordy phrases, filler, *you can*, *there is/are*, restated headings, redundant sentences | [voice.md](voice.md) |
| 4 | Voice and tone | Main point buried inside a sentence or paragraph; stiff, bossy, chummy, or marketing tone; tone wrong for the situation | [voice.md](voice.md) |
| 5 | Grammar | Tense, mood, passive voice without reason, agreement, person, dangling or misplaced modifiers, ambiguous *-ing* and *-ed* words, *should*/*must* misuse | [grammar.md](grammar.md) |
| 6 | Word choice | Complex words, jargon, inconsistent terms, nouns as verbs, coined words, Latin abbreviations, acronym handling | [word-choice.md](word-choice.md), [term-list.md](term-list.md), [term-collections.md](term-collections.md) |
| 7 | Global and inclusive | Long or chained sentences, dropped *that* and articles, modifier stacks, idioms, biased, ableist, or militaristic terms, position-only cues | [global-and-inclusive.md](global-and-inclusive.md) |
| 8 | Punctuation and numbers | Serial comma, hyphenation, dashes, numerals vs. words, ranges, dates, units | [punctuation-and-numbers.md](punctuation-and-numbers.md) |

The check covers wording. It doesn't judge which sections or fields a document
has, their order, or their layout. If a fact the reader needs seems to be
missing, list it under questions for the author rather than as a finding.

**Finding format.** Record each finding as:

```text
[category] location: "quoted text" -> "proposed text" (rule)
```

Location is a heading, line number, or element name. Rule is a short phrase,
such as *active voice* or *spell out zero through nine*. Group repeated
instances of the same rule into one finding with a count and two or three
representative locations.

**Severity.**

- **High:** changes or obscures meaning, is wrong for the audience, makes a
  requirement untestable or ambiguous, or uses biased or offensive language.
- **Medium:** slows the reader: wordiness, passive voice without reason,
  inconsistent terms, jargon, long sentences.
- **Low:** mechanical: punctuation, number style, hyphenation, spelling
  variants.

**What not to change.**

- Facts, behavior, numbers, identifiers, code, quoted UI or error text, and
  normative keywords. Flag them if they seem wrong; don't silently edit them.
- Layout, formatting, section order, heading levels, and the choice of
  paragraph, list, or table. Other context governs those. Rewording the text
  inside a heading, list item, or table cell is in scope.
- Wording that an author style guide or paired voice skill explicitly
  prescribes, such as longer qualified sentences, *we*, or normative keywords.

## Autopilot: rewrite pass

Use when the user wants the document fixed without step-by-step approval.

1. Run the check and record every finding.
2. Apply all high and medium findings. Apply low findings that don't touch
   protected content.
3. Reread the revised document from the start. Confirm the meaning of every
   paragraph is unchanged and that no new problems appeared.
4. Run the final read in [voice.md](voice.md#final-read).
5. Report to the user:
   - A summary of changes by category, with counts.
   - Every change that could affect meaning, listed individually.
   - Findings deliberately left unapplied, and why.
   - Questions about facts or intent the review surfaced.

Done when the revised document is saved or presented, the report lists every
meaning-sensitive change, and no high or medium finding remains unaddressed or
unexplained.

## Interactive: summarize and select

Use when the user wants to choose what to improve.

1. Run the check and record every finding.
2. Present a summary: one line per category with the count of findings, the
   severity mix, and one representative example.
3. Recommend the two or three categories with the most impact on the reader.
4. Ask the user which categories (or specific findings) to address. Offer the
   recommended set as the first choice.
5. Apply only the selected findings. Show each change as quoted before and
   after text, grouped by category.
6. Ask whether to continue with another category, apply everything remaining,
   or stop.

Done when the user has chosen to stop or every category has been addressed or
declined, and every applied change was shown to the user.

## Critique only

When the user asks only for a critique, run the check and present the findings
by category and severity without editing the document. Lead with the three
findings that would most improve the reader's experience.
