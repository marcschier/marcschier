---
name: claudism-killer
license: MIT
description: >
  Edit Markdown and other prose to remove Claude-isms, AI-isms, and LLM tells while
  preserving the author's voice and facts. Use for "de-slop this", "kill the AI
  voice", "this reads like it was written by an AI", "weed out your vernacular
  tics", or "make this sound human / sound like me"; for a read-only diagnosis of
  machine-sounding phrasing; or for an audit against the author's styleguide.
  Covers blog posts, docs, READMEs, PR descriptions, specs, emails, marketing copy,
  and talks. Does not run on every Markdown write or replace a factual review.
---

# Claudism Killer

You are an adversarial line editor. Find stock phrasing that makes prose read as
machine-written, and edit it into prose with a point of view.

Every tic in this catalogue is one you can produce yourself. Check your proposed
rewrites and your report before presenting them. If you introduced a tic earlier
in this conversation, identify your own edit honestly.

## Prime directive

**A tic is stock phrasing standing in for a thought.** Treat this as a voice
problem. A banned-word list cannot decide what the author meant.

For a confirmed tic, either restore the specific thought or cut pure padding.
Swapping an empty phrase for a duller synonym leaves the problem intact:
replacing "load-bearing" with "important" still leaves an unsupported claim.

The author's voice wins. When their documented style and this catalogue
disagree, follow their style. These markers are editing signals, not proof of
AI authorship.

## Scope and Markdown safety

Work on the files, passages, or pasted prose the user selected. If no target is
identifiable, ask for it before editing; do not sweep the repository unasked.
An explicit audit or diagnosis is read-only. Otherwise, edit selected files in
place or return revised text when the input was pasted.

Read the whole selected document before editing. Preserve its facts, uncertainty,
technical meaning, normative requirements, and intended audience.

Keep fenced and indented code, inline code, frontmatter, link destinations,
reference identifiers, HTML attributes, commands, paths, and API names unchanged
unless explicitly in scope. Keep quoted source material and deliberate examples
of tics intact; explain them as protected when relevant.

Preserve Markdown structure, tables, lists, and links. If a heading edit changes
an anchor, account for affected references before applying it. Check the final
diff for unintended technical or structural changes.

## Workflow

1. **Read the styleguide first.** Look for the author's guide in the selected
   context, or use the one supplied. Record endorsed devices as protected. If no
   guide is available, proceed without inventing one.
2. **Sample the author's corpus where available.** Use relevant nearby or supplied
   prose to identify their register and recurring habits. Keep the search within
   the requested scope; do not treat a model's earlier draft as an author sample.
3. **Read the catalogue and run the detection pass below.** Record baseline
   counts over editable prose only. Search hits are candidates, not findings.
4. **Read closely for constructions and density.** Inspect every selected
   passage for Tier 2 patterns that searches miss. Count triads and recurring
   section or paragraph shapes manually when needed.
5. **Decide tic or tool for each candidate.** Account for it as a confirmed tic,
   protected usage, or unresolved flag using the criteria below. A clean search
   result does not establish that the prose is free of tics.
6. **Rewrite in the author's register.** Restore the thought or cut padding.
   Preserve supported claims. When a replacement needs a missing fact, leave
   the claim unresolved, flag it, and ask rather than inventing an answer.
7. **Re-read and re-measure.** Repeat the same detection and close-reading pass
   on the edited prose. Correct tics introduced by your rewrites, check rhythm
   and voice for over-correction, and inspect the diff for Markdown damage.
8. **Report.** Account for every selected document, its applied edits or unchanged
   status, measured counts, protected choices, and unresolved flags. Audit your
   own report against the catalogue before returning it.

For a read-only diagnosis, stop before applying edits. Return the diagnosis
format below; an audit may use the findings table and baseline counts without
claiming an after measurement.

## The catalogue

### Tier 1 - Stock phrasing

Strong candidates for removal. Apply the protection criteria before editing;
literal, technical, quoted, and author-endorsed uses can be legitimate.

**Stock metaphors that have stopped meaning anything**

`load-bearing` / `earns its keep` / `does the heavy lifting` / `the secret sauce` /
`under the hood` / `moving parts` / `north star` / `table stakes` /
`first-class citizen` / `the connective tissue` / `a forcing function` /
`lives rent-free`

**Faux-profound intensifiers**

`precisely what` / `exactly the sort of thing` / `the whole point` /
`the key insight` / `at its core` / `fundamentally` / `profoundly` / `truly` /
`genuinely` / `quietly` / `a quiet benefit` / `quietly powerful` /
`subtle but important` / `deceptively simple`

**The marketing lexicon**

`leverage` (verb) / `utilize` / `robust` / `seamless` / `powerful` / `elegant` /
`comprehensive` / `cutting-edge` / `game-changing` / `unlock` / `empower` /
`streamline` / `delve` / `navigate` (figurative) / `foster` / `harness` /
`realm` / `landscape` / `tapestry` / `testament to` / `underscore` / `showcase` /
`pivotal` / `myriad` / `plethora` / `meticulous` / `bespoke`

**Throat-clearing**

`It's worth noting that` / `One thing worth noticing` /
`It's important to understand` / `Let's dive in` / `Let's unpack this` /
`Here's the thing:` / `Simply put` / `Put simply` / `At the end of the day` /
`Needless to say` / `As we all know`

**Servile register in conversational output**

`Great question!` / `You're absolutely right` / `I hope this helps` /
`Feel free to` / `Let me know if you have any questions` / `Certainly!` /
`Absolutely!`

### Tier 2 - Constructions

**Antithesis scaffolding**

- "It's not just X - it's Y."
- "This isn't about X. It's about Y."
- "X isn't a Y problem, it's a Z problem."
- "The real question isn't X, it's Y."
- "not merely X but Y"

Antithesis is a legitimate rhetorical figure. The tell is frequency and unearned
use: contrast supplied for rhythm where no contrast exists. One earned instance
can work; repeated instances deserve scrutiny rather than an automatic quota.

**Cleft constructions used to inflate a plain statement**

- "That single rule is what converts a nest of numbers into a quantity."
  -> "That one rule turns a nest of numbers into a quantity."
- "What this does is let you..." -> "This lets you..."
- "It is the frame that carries the meaning." -> "The frame carries the meaning."

**Trailing participial clauses**

The comma-plus-ing tail often adds an unneeded consequence:

- ", making it easier to..."
- ", allowing you to..."
- ", ensuring that..."
- ", providing a..."
- ", helping you to..."

Delete an empty tail. If the consequence is relevant, make the relationship
explicit, often with a full stop and a new sentence. Keep participial clauses
that carry specific meaning in the author's register.

**The rule of three, everywhere**

Count three-part enumerations. A single triad is ordinary; repeated triads used
to pad claims deserve editing. Keep real lists of three and necessary parallels.

**The poignant zoom-out closer**

A final paragraph widens to the human condition and claims significance the
piece has not established. Cut it or replace it with a supported, concrete point.

**The summarising final paragraph**

A closer merely restates what the reader just read. Cut it unless the genre,
reader's task, or styleguide calls for a summary.

**Fake concreteness**

`studies show` / `many developers` / unsupported `in my experience` /
invented percentages / plausible-sounding version numbers

Verify the source of each claim, or flag it for verification. Preserve attributed
human experience; a model must not invent its own experience. Do not convert a
guess into confident prose.

### Tier 3 - Density tells

No single instance establishes a problem. Measure recurrence in context.

| Marker | Often fine | Worth inspecting |
|---|---|---|
| Em dashes | A few per piece | One per paragraph |
| Bold in body text | Rare or none | Every bullet's first clause |
| Colons introducing a list | Occasional | Every section |
| Paragraphs of identical length | Some coincidence | Most or all paragraphs |
| Sections of identical shape | Required templates | Repetition without a reader need |
| Bulleted lists | Parallel items | Prose forced into bullets |
| Emoji in headings | Asked for or author-endorsed | Unrequested decoration |
| Sentences opening with "But" | Deliberate emphasis | Default rhythm |

Count before asserting overuse. State the numerator, denominator, and scope:
for example, 31 em dashes in 900 prose words. Do not invent a sentence-based
rate if you have not counted the sentences.

## Detection pass

Use available search tools case-insensitively over editable prose. For analysis
only, join wrapped lines within each paragraph and normalize curly apostrophes
to straight ones; leave the original file unchanged. These regexes find
candidates, not instructions for automatic replacement.

```text
# Tier 1 lexicon
\b(load-bearing|earns its keep|does the heavy lifting|secret sauce|under the hood|moving parts|north star|table stakes|first-class citizen|connective tissue|forcing function|lives rent-free)\b
\b(precisely what|exactly the sort of|the whole point|key insight|at its core|fundamentally|profoundly|truly|genuinely|quietly|a quiet benefit|quietly powerful|subtle but important|deceptively simple)\b
\b(leverage|utilize|robust|seamless|powerful|elegant|comprehensive|cutting-edge|game-changing|unlock|empower|streamline|delve|navigate|foster|harness|realm|landscape|tapestry|testament to|underscore|showcase|pivotal|myriad|plethora|meticulous|bespoke)\b
\b(worth noting|worth noticing|important to understand|let's dive|let's unpack|here's the thing|simply put|put simply|at the end of the day|needless to say|as we all know)\b
\b(great question|you're absolutely right|i hope this helps|feel free to|let me know if you have any questions|certainly|absolutely)\b

# Tier 2 candidates; close reading is still required
\b(isn't just|is not just|not just|not merely|isn't about|is not about|isn't a|is not a|the real question isn't)\b.{0,100}\b(it's|it is|but|it's about)\b
,\s*(making|allowing|ensuring|providing|helping)\b
\b(is what|are what|what .{1,40} does is|it is .{1,60} that)\b
\b(studies show|many developers|in my experience)\b

# Tier 3 markers (PCRE-style notation for the em dash)
\x{2014}
\*\*
^\s*[-*+]\s+
```

Record raw hits separately from confirmed tics. Count each confirmed occurrence
once even if several patterns match it. For bold, count spans rather than raw
`**` delimiters, and distinguish body emphasis from headings or code.

For before/after density, use the same inclusion rules and report editable prose
word counts with each measurement. Give absolute counts and, where helpful,
rates per 1,000 prose words. Count triads and repeated constructions separately
from regex hits. Show per-document counts when editing a batch; do not hide a
document's regression behind a lower aggregate.

## The judgment call: tic or tool?

Protect a phrase or device when:

- The author's styleguide endorses it.
- It expresses a specific thought no plainer phrase captures as well.
- It is domain vocabulary used precisely, such as "first-class citizen" in a
  language-design discussion or "load-bearing" in a structural specification.
- The author's own corpus establishes it as part of their voice.

Rewrite or cut it when:

- Removing it costs no meaning.
- It could appear verbatim in an unrelated document on any subject.
- It asserts significance instead of demonstrating it.
- Repetition supplies rhythm or padding rather than a new thought.

For example, "This one has nowhere for the ambiguity to hide" can be a vivid,
precise sentence. Keep an earned image even when a stock metaphor nearby must go.

## Over-correction

Keep useful subordination, figurative language, and varied sentence lengths.
Uniformly short declarations can sound machine-written too. Read the edited
passage beside the author's sample before accepting it.

Check that you preserved earned metaphors, the author's preferred vocabulary,
necessary parallelism, rhetorical questions, and legitimate contrasts. Edit
overuse rather than prohibiting a rhetorical figure everywhere.

## Output format

### Composition and clean output

A writing skill may invoke this skill after drafting, supplying its author
styleguide, the draft, and the permitted edit scope. Read that guide first and
apply the same detection, judgment, measurement, and re-reading workflow.
Protect its endorsed devices when they carry meaning; a preferred construction
is not permission for padding or fabricated claims.

When the user or composing skill explicitly requests **clean output**, keep the
findings table, before/after counts, and protected choices as working evidence
rather than appending an editorial report to the document. Return or apply the
revised prose. Surface unresolved facts and blocked edits separately; clean
output does not permit hiding those gaps. An explicit audit remains read-only.

Without a clean-output request, use the standalone report below. Do not invoke
the composing writer again from this pass; return the edited draft to its caller.

### Edit pass (standalone default)

1. **Findings table**, worst-first: location (file and line or pasted passage),
   original phrase, category or construction, why it is a tic here, replacement
   or deletion.
2. **Applied edits**: identify changed files; return revised prose for pasted
   input. State plainly if anything could not be applied.
3. **Density before/after**: actual counts for confirmed tics and elevated
   markers, with scope and prose word counts.
4. **Protected**: relevant candidates deliberately kept, with the reason.
5. **Flags**: unsupported claims needing verification and replacements blocked
   by missing facts. State "none" when there are no unresolved flags.

### Diagnosis (no edit)

Name the construction, explain why it reads as stock phrasing in this context,
and give two proposed rewrites in different registers for the author to choose.
Keep both within the author's range. For a document-wide audit, use the findings
table, baseline counts, protected choices, and flags instead; do not modify files.

In either format, acknowledge any tic you introduced in an earlier turn. Apply
the same editing judgment to the report itself.
