---
name: xregistry-writing
license: MIT
description: >-
  Write and review xRegistry documentation in the style of xregistry/spec
  upstream main. Use for normative specifications, Primers, domain drafts,
  READMEs and design notes. Match the document's audience, implementation
  detail, terminology, example scope and diagram abstraction. Preserve
  technical meaning during style edits.
---

# xRegistry writing

Write for a reader implementing or using an interoperable registry. Explain
the model, then state the behavior precisely enough for independent clients
and servers to agree. Use a more conversational register when teaching that
model in a Primer.

This skill derives from **upstream `xregistry/spec`**, not the fork's drafts.
The [corpus analysis](references/upstream-style.md) records the source
revision, every document considered, and examples of the conventions below.
Read its document-family and evidence sections when selecting a pattern. For
an edit, read the complete selected document and its governing clauses before
drafting.

## 1. Set the brief and preserve authority

Identify the document's purpose, audience, normative status and edit scope.
Select the closest upstream example by document role, not merely its filename.
Use current technical requirements to establish behavior; the recorded corpus
is evidence of writing style, not a permanent source of protocol semantics.

Preserve identifiers, defaults, error conditions, requirement strength and
compatibility commitments. A style edit does not authorize a new feature,
restriction, migration rule or version number. Record a missing technical
decision separately rather than filling it with plausible requirements.

For upstream comparisons, use `xregistry/spec`'s `main` branch. A fork's
`origin/main`, an open PR and a locally edited draft are different sources.
Describe an unreleased document as a draft even when it is present on main.

**Ready to draft:** the reader, document role, authoritative requirements and
permitted changes are identified.

## 2. Choose the document's register and structure

| Document role | Reader and register | Organizing pattern |
| --- | --- | --- |
| Core or protocol specification | Client/server implementers; direct, conditional, implementation-neutral prose | Scope and concepts, terminology, representation, attributes, operations and errors |
| Domain specification | Domain implementers who need the mapping to Core | Domain purpose, entities, model shape, extension attributes, formats and applicable constraints |
| Primer or tutorial | Developers familiar with REST/JSON but new to xRegistry | Small working example, conceptual explanation, progressively harder operations, then design rationale |
| Supporting README or design note | Readers locating an artifact or evaluating a decision | Purpose and entry points, or the decision and its consequences; link to the normative source |

The first three patterns are observed in the corpus. The supporting-document
pattern applies the same audience and scope distinctions without turning a
README into a specification.

For a specification, use actors such as the server, client, implementation,
Registry, Producer or Consumer. Give the condition before its consequence. Use
`MUST`, `MUST NOT`, `SHOULD`, `MAY` and the other normative keywords with the
force defined by the document's RFC2119 convention.

For a Primer, direct address, a filesystem analogy, "we" explaining a design
choice, and an answered "Why...?" heading fit the upstream register. Explain
what the reader can do before the less common cases. Link back to the rule;
the explanation does not establish a second normative contract.

Retain the target document's heading and numbering scheme. Long specifications
usually have an Abstract and a table of contents, but the shorter Pagination
specification does not justify forcing that outline onto every document.

## 3. Match the level of detail to the rule

Use the established attribute-card form for reference material:

```markdown
#### `attribute` Attribute
- Type: [established type]
- Description: [meaning, owner and scope]

- Constraints:
  - [Established presence, default and value rules.]
  - [Applicable operation, exception or error behavior.]

- Examples:
  - [Concrete value illustrating this attribute.]
```

This is an authoring scaffold, not a requirement to add every field or invent
missing semantics. Follow nearby cards; domain property tables can carry
parallel name/type/description information more compactly.

For each changed rule, cover the distinctions that affect its outcome:

- What entity or collection owns the value, and what a reference identifies.
- Presence, omission, `null`, emptiness and defaults where they differ.
- Creation versus update, immutability, read-only handling and Version scope.
- Processing order, prerequisites, exceptional cases and observable results.
- The existing error name or governing clause when an operation fails.

State one independently checkable obligation per bullet where practical. Keep
conditions and qualifications with the rule they limit. Use numbered steps
when order changes the result; use unordered constraints otherwise.

Give a short local reason when it prevents a likely misunderstanding. Put
extended motivation, alternatives and design history in a Primer or design
note. Domain specifications explain their specialization and refer to Core for
inherited behavior rather than restating its algorithms.

Stop expanding a section when an implementer can determine each distinct
outcome from the section and its references. A definition does not need a
tutorial, and an explanatory paragraph does not need every conformance case.
Do not add a separate clarification section merely to repeat existing rules.

## 4. Size examples and diagrams by what they explain

### Examples

Use the smallest example that demonstrates the rule without hiding essential
context. Upstream uses several scales, not one preferred length:

- A scalar, path or short fragment for a local attribute rule.
- A request and result, or a before/after state, for an observable operation.
- One annotated hierarchy specimen in the model/reference section.
- A fuller integration example when several domain models have to agree.

Reuse the established scenario and identifiers across related examples. Keep
the Group, Resource and Version levels distinguishable. Explain the result
immediately after an example when the result is not apparent from the data.
Add an adverse case when it exposes a different outcome, not to produce a
fixed number of examples.

Separate executable examples from notation:

- A `json` fence contains valid JSON when presented as a concrete JSON example.
- Pseudo-JSON can use the document's declared `<TYPE>`, `?`, `*`, `+`, `#`
  and omission conventions. Label it as notation and follow the surrounding
  fence convention, commonly `yaml`.
- State which attributes or document bodies are omitted for brevity. A marked
  omission is different from an unfinished `TODO` or an unexplained gap.
- For an HTTP exchange, retain the method, path, headers, status and body
  needed to establish the behavior. Do not expand every field example into a
  complete exchange.

Check examples against the actual model and normative prose. Repair neither
side silently when they disagree. Test helpers and generated schemas are not
substitutes for readable examples.

### Diagrams

Diagrams are selective in upstream: Core explains its hierarchy and URL/data
mapping; Message illustrates base-definition relationships. Most
specifications have none. Add a figure when a relationship is clearer
spatially, not to meet a diagram quota.

Choose one abstraction per figure: entity hierarchy, concrete domain mapping,
reference relationship or operation flow. A progression from a small abstract
model to a concrete instance fits Core's approach. A diagram of entities does
not need databases, caches, deployment hosts or internal SDK classes.

Use the prose's exact entity and relationship names. Distinguish containment
from references and order from dependency. Keep protocol steps and failures
only when they explain the depicted operation. The surrounding text defines
the behavior; the figure introduces no additional requirements.

Explain the figure's purpose in adjacent prose and provide a text equivalent
or accessible description. Preserve existing image or Mermaid assets when
editing; use a maintainable format for new figures. The corpus establishes
conceptual granularity, not a mandatory drawing tool or node count.

## 5. Edit the prose without changing its meaning

Use literal field names in backticks and defined entity names consistently.
Distinguish Resource, Version, document and metadata instead of rotating them
as stylistic synonyms. Define unfamiliar domain terms; assume ordinary
REST/JSON knowledge in implementation material.

Prefer concrete descriptions and conditions to claims about quality or
importance. Moderate sentence length is appropriate when a sentence expresses
one rule with its conditions. Split unrelated obligations, not every qualified
sentence. Brief "For example", "For clarity" and "Note" transitions are part
of the register when they introduce useful information.

Use bullets for constraints and parallel cases, tables for comparable
properties, and prose for explanation. Keep emphasis sparse in normative
reference sections. The two upstream domain drafts use more bold and
parenthetical explanation; that is not a requirement for every document.

Follow `docs/CONTRIBUTING.md`: wrap prose at 80 columns where practical, use
the document's normative capitalization, and preserve valid Markdown links.
Leave long URLs, tables and syntax samples readable rather than forcing their
lines to fit. Maintain headings, anchors, contents lists and spelling
directives when editing.

If another writing or line-editing skill is active, supply this repository
register as its local style guide. Protect meaningful technical repetition,
conditional clauses, domain terms and illustrative notation. Correct drafting
defects rather than copying them as evidence of a voice.

## 6. Review before delivery

For each selected document, check every applicable item:

- **Audience:** the text assumes the right prior knowledge and answers the
  reader's implementation or learning question.
- **Authority:** examples, explanations and proposed decisions remain
  distinguishable from established requirements.
- **Detail:** the changed behavior covers its relevant conditions and outcomes
  without repeating unrelated reference material.
- **Examples:** identifiers and results agree with the rules; omissions are
  marked; concrete syntax is valid.
- **Diagrams:** labels and relationships agree with the text at one useful
  abstraction level, or no diagram is needed.
- **Register:** structure, terminology, emphasis and explanatory depth fit the
  document's role and nearest upstream example.
- **Integrity:** the diff preserves technical meaning, reference targets,
  normative force, examples and generated content outside the edit scope.

Use the repository's existing documentation checks where applicable. Inspect
the rendered or structured output when changing tables, notation or figures. A
clean lint result does not establish technical or stylistic conformance.

In an authoring task, deliver the document and a short account of meaningful
changes. In a read-only review, leave files unchanged and give located
mismatches with concrete suggested corrections. State unresolved technical
questions separately; do not declare the style review complete by concealing
them.
