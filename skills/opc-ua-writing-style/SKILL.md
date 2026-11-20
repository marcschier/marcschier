---
name: opc-ua-writing-style
license: MIT
description: >-
  Draft or edit OPC UA specification prose in the voice of published companion
  specifications. Use for OPC UA wording, sentence rhythm, paragraph breaks
  and punctuation. Preserve technical meaning and write idiomatic English.
---

# OPC UA writing style

Write in the register of a published OPC UA companion specification: neutral,
literal and concise. Keep the target's structure and formatting. This skill
governs prose, not modelling, conformance review or document design.

## 1. Identify what the passage does

Read the supplied requirements and the surrounding text. Separate definitions
and descriptions from obligations, permissions, recommendations and examples.
Choose the register by the passage's job, not just its section title. Keep
the companion voice even when the subject is based on an OPC UA core type.
If the target is a core specification, follow the surrounding prose.

**Ready to draft:** Each passage has a purpose, and every technical assertion
has a source in the brief, the existing draft or a governing specification.
Keep unresolved technical decisions out of the rewrite.

## 2. Write the paragraph around one subject

| Passage | Rhythm |
| --- | --- |
| Type, member, value or state | Lead with the exact name and what it represents, contains, indicates or provides. One sentence often suffices. Add a second for a material qualification, distinction or reference. Start a new paragraph for the next subject. |
| Operation or requirement | Give the actor and observable result. State the condition before the result when it limits the rule. Keep the default, exception or error with its rule if it would otherwise be misread. Start a new paragraph for an independently testable case, a new actor or a change of topic. |
| Scope, overview or use case | Name what is specified or represented first. Then give the domain context, participating roles, or reason the distinction matters. Two to four connected sentences can develop one idea before the next paragraph. |

Most model prose needs one or two sentences per paragraph. Many sentences
land around 10 to 20 words. Use this as a guide, not a limit. Let a definition
be short and a dependent rule be longer. Keep connected reasoning together
without making the reader unpack a wall of clauses.

Use the present tense and third person. Prefer concrete verbs: a Variable
*indicates* a state, a Property *contains* a value, a Method *returns* a
result. Repeat a defined name where a pronoun or synonym would blur its scope.
Use `This Method` or `the value` when the referent is immediate and unique.
Name the Client, Server or other actor when responsibility matters. Use a
passive construction when the defined item is the subject and the actor is
immaterial or already established.

Keep the document's convention for requirement words. In normal OPC UA
prose, use lowercase `shall` for an obligation, `shall not` for a prohibition,
`should` for a recommendation, `may` for permission and `can` for capability
or possibility. Use the plain present for definitions and descriptive facts.
Preserve the force of the source; changing `may` to `shall`, or replacing
every occurrence of `must` mechanically, is not a style edit.

**Ready to edit:** Each paragraph addresses one subject or dependent case.
Each rule makes its actor, condition and outcome clear where applicable.

## 3. Punctuate and edit for idiomatic English

- Prefer periods for separate assertions and a comma after an opening
  conditional clause. Use a colon after a complete lead-in to alternatives
  or a list, not between a subject and its verb.
- Use parentheses for a brief example, unit, expansion or local reference.
  Keep an essential condition in the sentence. Use `For example,` for a
  separate illustrative sentence. Prefer a period to a semicolon joining
  separate rules and avoid dashes used for rhetorical emphasis.
- Use short, precise references such as `see 6.2` or `as specified in 6.2`.
  Place the reference beside the claim it supports. Explain the local
  use or difference instead of repeating inherited behavior.
- Keep articles, prepositions and agreement idiomatic: `allows the Client to
  read`, `consists of`, `complies with`. Untangle noun chains, supply missing
  articles, and repair fragments, comma splices and misplaced modifiers.
  Follow the target's English spelling and capitalization of defined terms.
  A source typo, awkward calque or export glitch is not part of the voice.
- Cut introductory throat-clearing, claims of general benefit, and paraphrases
  that add no fact. State scope limits directly: `This specification does not
  define the file format.` Keep the exception, example or brief reason that
  changes how the passage is understood.

**Done:** Compare the rewrite with its source. Preserve identifiers, scope,
defined relationships, modality, conditions, timing and outcomes. If the
language is still ambiguous, flag the point rather than guessing the intended
rule. Leave unrelated prose and layout alone.

## Calibration

These are original examples. They illustrate cadence, not OPC UA requirements.

> The InspectionResultType represents the result of an inspection. The type
> provides the inspection identifier and the time at which the inspection
> ended.
>
> ResultId identifies the inspection result within the Server.
>
> If no inspection has completed, the Server shall return Bad_NoData when
> the Client calls GetInspectionResult.
>
> A Client can read the latest result without starting another inspection.

For longer overviews, compound behavior, or a request to explain the evidence
behind a style choice, read the [corpus analysis](references/corpus-analysis.md)
and select the example with the same prose function.
