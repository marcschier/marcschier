# Reference documentation and specifications

Use this route for API reference, protocol and interface specifications,
schemas, data models, configuration references, command references, error
message catalogs, and normative standards text. Readers look things up rather
than read through. They need the same information in the same place, worded the
same way, every time.

The core references still apply. This file covers content and wording only.
Section order, templates, and layout come from the project's own conventions.

## Consistency first

- Word equivalent entries identically. If one method says *Gets the ...*,
  every getter does.
- Use one term for each concept across the whole reference. Build a term list
  for the document and hold to it.
- Describe parallel elements in parallel grammatical form.
- Keep each fact in one place and refer to it from elsewhere rather than
  restating it with different wording.
- Deviate from the pattern only where the element genuinely differs, such as
  configuration schemas, compiler options, or error catalogs, and keep the
  deviation consistent within its own set.

## Element descriptions

**Summary.** In one or two sentences, say what the element does or represents.
Don't restate its name. *`MaxRetries`: The number of times the client resends a
failed request before it reports an error*, not *`MaxRetries`: The maximum
retries.*

Use stable opening patterns:

| Element | Opening pattern |
|---|---|
| Class, type, structure | Represents ... / Provides ... / Defines ... |
| Method, function, operation | Verb in third person: Creates ..., Returns ..., Sends ... |
| Property, field, attribute | Gets ..., Gets or sets ..., or a noun phrase for the value |
| Boolean property or flag | Gets a value that indicates whether ... |
| Event | Occurs when ... |
| Enumeration member | Noun phrase or condition the value stands for |
| Constructor | Initializes a new instance of ... |
| Error or status code | The condition that produces it |

**Parameters and fields.** For each, give:

- The data type.
- Whether it's required or optional, and the default when omitted.
- Direction (input, output, or both) where that applies.
- Valid range, units, format, and encoding.
- Behavior for empty, null, zero, or out-of-range values.
- Anything the name and type don't already say. Don't repeat the name as the
  description.

**Return values and results.** Describe what's returned and its type. For a
Boolean, state the condition: *`true` if the session is active; otherwise,
`false`.* For a collection, say whether it can be empty and what empty means.

**Property values.** Give the type, the default, and whether it's read-only.

**Errors and exceptions.** List each error, status code, or exception with the
exact condition that causes it. Describe conditions, not implementation
details.

**Permissions and preconditions.** State the permissions, roles, states, or
capabilities needed before the element can be used.

**Remarks.** Put here what a reader needs but wouldn't infer: non-obvious
behavior, side effects, thread safety, performance characteristics, ordering
and timing guarantees, comparisons with similar elements, and common pitfalls.

**Examples.** Show realistic usage. Apply the code example rules in
[developer-content.md](developer-content.md#code-examples).

**Related elements.** Point to elements the reader is likely to need next,
with a reason when the relationship isn't obvious.

## Specification and normative text

- Separate normative text (requirements) from informative text (explanation,
  rationale, examples). Readers must be able to tell which is which.
- State each requirement once, as a complete sentence with an explicit subject:
  *The server returns ...*, *A client sends ...*. Avoid requirements hidden in
  examples, notes, or figures.
- Use present tense and indicative mood for behavior: *The server rejects the
  request.*
- Use *must* only for a requirement and *should* only for a recommendation.
  Use *can* or *might* for permission and possibility. When the document adopts
  a normative-keyword convention, apply it exactly and consistently, and keep
  those keywords out of informative text.
- Make every requirement testable. Name the actor, the condition, and the
  observable outcome. Replace vague qualifiers (*appropriate*, *reasonable*,
  *fast*, *large*) with values or criteria.
- Define every term before using it normatively, and use the defined term
  exactly. Don't introduce synonyms for defined terms.
- Give units for every quantity, and ranges as *from X through Y* or as
  explicit inclusive or exclusive bounds.
- Spell out the behavior for edge cases: empty input, missing elements, limits,
  timeouts, and concurrent access.
- Prefer a short rationale sentence after a non-obvious requirement over a
  long informative digression.

## Review generated reference text

Treat descriptions generated from source comments or by tools as drafts.

- Rewrite descriptions that repeat the element name or type.
- Remove internal details: implementation notes, internal names, bug numbers,
  and TODO comments.
- Fill in missing defaults, ranges, error conditions, and Boolean conditions.
- Make wording match the established patterns of neighboring entries.
