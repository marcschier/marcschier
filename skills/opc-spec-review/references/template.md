# Official Sample structure and supplemental review checks

## Source of truth

The authoritative Markdown structure is the current
[OPCUA Specification Template Sample](https://github.com/OPCF-Members/OPCUA-Specification-Template/tree/main/source/Sample),
especially its [`spec.md`](https://github.com/OPCF-Members/OPCUA-Specification-Template/blob/main/source/Sample/spec.md).
Read the current Sample files and the repository's current authoring guidance
before reviewing a specification that uses this template. The upstream
repository controls the template; this reference is only a concise set of
additional checks, not a replacement or fallback copy. If the upstream source
cannot be inspected, stop the structural assessment and report the access
blocker. Do not treat this summary or an older local outline as the template.

The Sample separates authored prose from data and publisher output:

- `spec.md` supplies the main clause sequence, authored content, and directives
  for generated or included content. Follow the current Sample for the
  supported headings and directives.
- `manifest.json` supplies specification identity and other source data used
  by the publisher, including normative references, terms, abbreviations, and
  namespaces where configured. Check authored front matter and generated
  identity against it.
- `profiles.json` supplies Profile and Conformance Unit content used in the
  publication. Check its definitions and relationships rather than
  duplicating generated content in prose.
- `figures/` contains figure sources referenced by the Sample. Verify each
  reference resolves to the intended source asset.

The Sample includes temporary editing guidance that is marked for removal
before publication. Treat it as instructions to an author, not as a published
clause, and check that such instructions and unresolved placeholders do not
remain in the final edition.

## Official Sample structure

Use the current upstream `spec.md` for exact heading text, nesting, directives,
and include syntax. The current Sample's authored section order is Scope,
Editing Guidelines, General information, Use cases, Information Model
overview, OPC UA ObjectTypes, OPC UA VariableTypes, OPC UA DataTypes, and OPC
UA ReferenceTypes. Its Editing Guidelines section is marked for deletion
before publication; treat it as temporary author guidance, not a clause in the
published specification.

The Sample also uses the manifest, Profile Database, NodeSet, and publisher
directives for content that is generated or composed, including normative
references, terms, Profiles and Conformance Units, namespaces, and Normative
Annex A. Check the actual source-data configuration and composed edition for
their exact placement and content. Do not add duplicate authored headings or
content merely because the generated material is not a top-level heading in
`spec.md`.

Include only the type content that applies. Use the Sample's type-specific
headings for EventTypes, Methods, instances, and other model elements; do not
restore the prior local outline's separate top-level chapters where the
upstream Sample places them elsewhere. Do not add a standalone Bibliography or
conventions section unless the current authoring contract provides for it and
the specification needs it.

## Supplemental checks by section

### Scope

Check that the stated scope matches the model, profiles, and publication
artifacts, and does not imply unsupported functionality or compatibility.
Confirm the final publication presents the correct document number, full title
and part, version, date, contributing organization, and status.

### Normative references

Include only references needed to apply the specification. A dated reference
selects that edition; an undated reference selects the latest edition,
including amendments and errata. Cite OPC UA documents by canonical document
identifier and clause number, not by links to individual clauses in the online
reference.

### Terms and abbreviated terms

Check that domain terms and abbreviations are defined before they are needed
and that their scope and distinctions are preserved. Apply the style
authority and safeguards identified in the main skill.

### General information

Introduce the organization or domain represented by the model for readers who
know OPC UA but may not know the industry. Refer readers to the OPC UA
introduction publication instead of repeating its general introduction.

### Use cases

For each supported use case, identify the actor, what it needs to accomplish,
and the information or behavior the model provides. Ensure the use cases agree
with the model and the functionality assigned to Profiles and Conformance
Units.

### Information Model overview

Explain the model's principal elements and relationships before relying on
them. Readers should be able to follow the prose from start to end without
searching ahead to learn a term or concept. Introduce enough context for each
statement to make sense; a forward reference may point to later detail or a
formal definition.

### OPC UA ObjectTypes

Explain what each modeled element represents before its formal definition.
For Methods, describe the signature and arguments, document defined result
codes, and identify additional AddressSpace elements when the Method defines
properties beyond its argument properties. Confirm prose, model tables, source
model, profiles, and NodeSet agree.

Use the current Sample's table columns, headings, and directives. Do not
substitute layout markup or alter publisher-owned presentation. Where the
publisher supports multiple authored definition blocks for one type, check
that they remain one logical definition and that each relation is represented
without losing its BrowsePath or target.

For model definition tables supported by the publisher, assess `defines=<Type>`
and composition against the ownership and preservation safeguards. Report
eligible tables lacking that binding as described in
[review.md](review.md#model-table-bindings-and-composition). Do not reproduce
the outdated instruction that a bound definition table is only checked and
never rewritten; confirm the selected repository's pinned Publisher behavior.
Keep `datatype=<DataType>` for field tables distinct from the binding on their
type definition tables.

Check `HasInterface` rows against the pinned Publisher's validation contract;
where it requires an empty ModellingRule cell, report a populated cell as a
publication validation issue rather than changing the interface's model rule.

Follow the upstream
[anchor guidance](https://github.com/OPCF-Members/OPCUA-Specification-Template/blob/main/AUTHORING.md#you-need-not-type-a-tables-or-figures-anchor):
`compose` normalizes supported table and figure anchors from their captions
and updates citations. A temporary anchor such as `{#t1}`, cited as `[](#t1)`,
does not need manual renaming before composition. Use the supported
`anchor=keep` exception when an existing anchor must be retained. Inspect
changed anchors and all affected citations in the diff and rendered output;
do not hard-code table or figure numbers. Composition does not generate or
validate the section's explanatory prose.

### Cross-type model consistency

State inheritance as a "Subtype of" relationship; do not add a `HasSubtype`
reference to a type definition. Put primary Conformance Units at the end of
each definition and keep the NodeSet classification consistent with them.
Keep members, NodeClasses, BrowseNames, DataTypes, TypeDefinitions,
attributes, and ModellingRules consistent across the prose, source model, and
published definition. Distinguish specification-defined values from
server-specific values rather than imposing defaults without evidence.

Use symbolic NodeIds in model descriptions and define actual NodeIds in
Normative Annex A. Distinguish model-defined NodeIds from server-generated
NodeIds. Keep `ValueRank`, `ArrayDimensions`, DataType, TypeDefinition, and
ModellingRule consistent across the prose, source model, and published
definition. Explain well-known BrowseNames where applicable.

### OPC UA VariableTypes

Check that each definition explains its purpose and that its attributes and
references agree with the source model. Verify the rendered definition retains
the authored values and links.

### OPC UA DataTypes

Check each Structure field for an adequate, accurate Description. The NodeSet
is authoritative for model facts and supplies the Description when it has one.
If it has no Description, provide one in the authored Markdown field table
when the current publisher contract supports it; reconcile the two when both
sources contain a Description. A `datatype=<DataType>` directive can generate
field rows from the NodeSet, but does not waive checking every field or supply
an absent Description. After update and rendering, verify every field
Description survives in the published output. If the publisher drops a
supported authored Description, report a template or tooling dependency.

For enumerations, use `EnumStrings` for zero-based sequential values and
`EnumValues` otherwise. Define OptionSet values by bit position. Preserve the
distinction between optional Structure fields and fields that allow subtypes.

### OPC UA ReferenceTypes

Check that each definition documents its inverse name, symmetry, abstract
status, parent type, and source and target constraints where applicable.

### Generated Profiles, namespaces, and Normative Annex A

Define testable functionality groups and include at least one Profile or Facet
for the companion specification. Keep each Conformance Unit consistent across
its definition, the Profiles that require it, and the model elements that
implement it. State whether included Profile Database content is an
informative snapshot or the normative definition.

For an information model, confirm namespace metadata and the NodeSet agree on
the namespace URI, version, publication date, subset status, and static NodeId
policy. A namespace URI is an identifier, not a promise that it resolves as a
network URL. Use the approved namespace URI form and preserve its required
syntax, including the final slash in the `http` form. Keep Annex A's namespace
summary, NodeSet, supplementary-file mappings, and published artifacts
consistent. Assign a unique short name to the companion specification and use
it consistently for Profiles, Conformance Units, and namespace and file
identifiers. Use uppercase for an acronym, camelCase otherwise, and preserve a
trademark's casing. Use applicable standard naming conventions for NodeIds,
NodeSet files, and DataType schemas. Include a capability identifier only
when the specification needs one.

### Cross-cutting publication checks

Use the current authoring guide and pinned publisher contract for Markdown
syntax and generated content. Inspect publisher-rendered HTML for changed
tables: headers, cells, values, grouping, and links must survive conversion.
Compare the rendered result with the authored source and model. Report lost
content or publisher presentation defects to the template or tooling owner;
do not patch generated HTML or prescribe styling.

Retain approved agreement, copyright, patent, liability, compliance, and
trademark material in the publication, using the authorized text and agreement.
For non-joint work, use the authorized alternative agreement; do not change
the agreement for joint work without the required OPC Foundation review. Do
not carry a public-domain notice from a template into the finished
specification. Include the issue-reporting route and project identifier. For
later editions, include revision highlights classified as **Errata**,
**Clarification**, or **Feature**, each tied to its issue-tracker record; do
not add revision highlights to a first edition.

In Publisher Markdown, use a local clause anchor for an in-document
reference as described in the current authoring contract. Do not hard-code a
clause number that can become stale when content is inserted.
