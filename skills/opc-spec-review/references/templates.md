# Concise Companion Specification content structure

Use this as the concise structure for each specification in the agreed release
set. It summarizes content, not Markdown syntax: the current official Sample
and the target repository's authoring contract define exact heading markup,
directives, generated content and publication behavior. Read those sources
before drafting, include only applicable material, and do not invent headings
the Sample does not support.

## Main `spec.md` order

Use the current Sample's heading text and nesting. Its authored content order
is:

1. **Scope** — what the specification defines and whom it applies to.
2. **Editing Guidelines** — temporary authoring instructions; remove before
   publication.
3. **General information** — brief domain context for an OPC UA reader.
4. **Use cases** — supported actors, goals and model behavior.
5. **Information Model overview** — principal types and relationships.
6. **OPC UA ObjectTypes** — each applicable type and its declared children
   and Methods.
7. **OPC UA VariableTypes** — each applicable type and its purpose.
8. **OPC UA DataTypes** — each applicable type and its fields or values.
9. **OPC UA ReferenceTypes** — each applicable reference type and its
   constraints.

Normative references, terms, abbreviated terms, Profiles, Conformance Units,
namespace information and Normative Annex A may be generated from manifests,
profile data, the NodeSet and publisher directives. Check their actual source
and placement; do not add duplicate top-level headings or authored content
merely because generated material is not a top-level `spec.md` section.
Methods, EventTypes, instances and other model elements use the type-specific
placement and headings in the current Sample; do not invent separate chapters.

## Per-element content

Use the current Sample's exact heading and markup pattern. As a content
checklist:

- **Type:** state what it represents; explain only behavior that is not clear
  from the definition; provide the supported definition table; describe
  declared children, not inherited members.
- **Method:** state its purpose; document conditions, effects and security;
  describe inputs and outputs; give only established result codes and their
  conditions.
- **EventType:** state what it represents or when it is raised; describe its
  raise condition and newly defined or constrained fields.
- **DataType:** state what the type represents; check each field, its order,
  type, dimensions, encoding and semantics against the model and publication.
- **Use case:** name the actor, goal and model behavior that supports it.

These are content prompts, not instructions to add a paragraph or table when
the current authoring contract does not support it. Keep examples short and
non-normative; use them only when they resolve a real ambiguity.

## Source data and generated material

Check the current Sample and repository configuration for where these belong:

- Document identity, status, release information and normative references.
- Terms and abbreviations.
- Profiles and Conformance Units.
- Namespace metadata, NodeIds and the normative model annex.
- Figures, schemas, model tables and other generated or included content.

Do not duplicate generated content in authored prose merely to reproduce an
outline. Verify that every required fact remains accessible in the composed
publication. Use the repository's pinned tools and preserve generator-owned
regions; report authoring or publisher gaps rather than inventing syntax.

## Review per specification

For each selected specification, record:

- The exact Sample and authoring-contract revision used.
- Applicable sections and model element types; omit only with a reason.
- Authored sources and generated destinations for required information.
- Cross-part dependencies and inbound references in the agreed release set.
- The final information-preservation audit and unresolved decisions.

The outline is deliberately concise. It does not replace review evidence,
technical validation, approval or the final information-preservation audit.
