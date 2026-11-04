# Reference documentation and specifications

Use this route for API reference, protocol and interface specifications,
schemas, data models, configuration references, command references, error
message catalogs, and normative standards text. Readers look things up rather
than read through, so they rely on equivalent facts being worded the same way
every time.

The core references still apply. This file covers wording only. Which
elements, fields, and sections an entry contains, their order, the opening
phrase a template prescribes, and the layout all come from the project's own
conventions or other context. Apply the rules below to whatever text that
structure calls for.

## Consistent wording

- Word equivalent statements identically. If one getter description says
  *Gets the ...*, every getter description says it the same way.
- Use one term for each concept across the whole reference. Build a term list
  for the document and hold to it.
- Describe parallel elements in parallel grammatical form.
- When the project prescribes a wording pattern, apply it exactly. When it
  doesn't, pick one grammatical form for each kind of element and keep it.
- Vary the wording only where the element differs, and keep the variation
  consistent within its own set.

## Wording element descriptions

- Say what the element does or represents. Don't restate its name or type.
  *`MaxRetries`: The number of times the client resends a failed request
  before it reports an error*, not *`MaxRetries`: The maximum retries.*
- Describe an action with a third-person verb (*Creates*, *Returns*,
  *Sends*) and a thing with what it is or holds.
- State a Boolean as its condition: *`true` if the session is active;
  otherwise, `false`.* Don't write *Indicates the session state.*
- Word an error, status code, or exception as the condition that produces it:
  *The session expired before the request arrived*, not *Session error.*
  Describe conditions, not implementation details.
- State defaults, ranges, units, formats, and limits as exact values. Write
  ranges as *from X through Y* or with explicit inclusive or exclusive bounds.
  Replace *large*, *small*, *appropriate*, and *reasonable* with numbers or
  criteria.
- When the text describes empty, null, zero, or out-of-range input, say
  exactly what happens: *An empty list returns no results*, not *Empty lists
  are handled.*
- Write a remark as the reader's consequence: *Calls to `Connect` block until
  the handshake completes*, not *`Connect` is synchronous internally.*
- Introduce an example with the scenario it shows. Apply the code example
  rules in [developer-content.md](developer-content.md#code-examples).

## Specification and normative text

- Word normative and informative text so readers can tell them apart.
  Requirements use the normative keywords; explanation, rationale, and
  examples don't.
- State each requirement once, as a complete sentence with an explicit subject:
  *The server returns ...*, *A client sends ...*. Don't let an example, note,
  or figure be the only place a requirement appears.
- Use present tense and indicative mood for behavior: *The server rejects the
  request.*
- Use *must* only for a requirement and *should* only for a recommendation.
  Use *can* or *might* for permission and possibility. When the document adopts
  a normative-keyword convention, apply it exactly and consistently, and keep
  those keywords out of informative text.
- Make every requirement testable. Name the actor, the condition, and the
  observable outcome. Replace vague qualifiers (*appropriate*, *reasonable*,
  *fast*, *large*) with values or criteria.
- Put one obligation in each sentence, so each can be tested independently.
- Define every term before using it normatively, and use the defined term
  exactly. Don't introduce synonyms for defined terms.
- Give units for every quantity.
- Where a requirement covers an edge case (empty input, missing element,
  limit, timeout, or concurrent access), state the behavior rather than
  implying it.
- Follow a non-obvious requirement with a short rationale sentence rather than
  a long informative digression.

## Review generated reference text

Treat descriptions generated from source comments or by tools as drafts.

- Rewrite descriptions that repeat the element name or type.
- Remove internal details: implementation notes, internal names, bug numbers,
  and TODO comments.
- Replace vague wording of defaults, ranges, and conditions with exact values.
  Flag a value the source doesn't supply rather than inventing it.
- Make the wording match the established pattern of equivalent entries.
