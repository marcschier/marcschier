# Companion specification content template

Use this outline as a content-level authoring and review aid. It is a Markdown
reduction of the OPC UA Companion Specification template, not a replacement for
the publisher repository's source contract. The
[official Markdown template repository](https://github.com/OPCF-Members/OPCUA-Specification-Template)
defines the current source contract. Its
[authoring guide](https://github.com/OPCF-Members/OPCUA-Specification-Template/blob/main/AUTHORING.md)
and [companion-specification skill](https://github.com/OPCF-Members/OPCUA-Specification-Template/blob/main/skills/opcua-companion-spec/SKILL.md)
identify which content authors supply, which content is generated, and how the
publisher consumes it. Follow those sources for Markdown mechanics. This
outline covers the content and semantic markup that the source must carry.

The published specification remains expected to contain the required
information in the approved order. Review the Markdown and its manifest,
profiles, and NodeSet sources for that information. Presentation belongs to the
template and publisher owners. If the supported source contract cannot express
required content, or the publisher output omits it, report the gap to those
owners; do not add unsupported syntax or attempt to repair their tooling.

## Publication information

Check that the publication data identifies the document number, full title and
part, version, date, contributing organization, and status. Use approved
agreement, copyright, patent, liability, compliance, and trademark content.
Do not rewrite approved legal text. Include the specification's issue-reporting
route and project identifier.

For revisions after the first edition, include revision highlights and connect
each listed change to its issue-tracker record. Classify each change as
**Errata**, **Clarification**, or **Feature**, as applicable.

## Scope

State what the specification covers, what the information model represents,
which systems it applies to, and what capability it supports.

## Normative references

Include only documents needed to apply the specification. A dated reference
selects that edition. An undated reference selects the latest edition,
including amendments and errata. For the current publisher template, verify
these references in the source that generates them rather than duplicating
generated content in authored prose.

## Terms, definitions, and abbreviations

Define domain terms and abbreviations used in the specification. Use a
definition that reads naturally when the term replaces its headword. Use one
term consistently for each concept, and introduce terms before relying on
them.

Italicize OPC UA terms and terms defined in the specification. In the
publisher's Markdown, italics mark those terms semantically; do not use italics
for emphasis. The template does not define a general bold convention for prose
concepts. Use bold for the revision classifications **Errata**,
**Clarification**, and **Feature** in revision highlights.

The current Markdown template generates terms and abbreviations from its
designated source data. Use the repository's current authoring guide for those
fields. Do not add a generic conventions section when the current template
provides no such authored or generated section; rely on cited OPC UA
specifications for common conventions and state only companion-specific
conventions where the source contract supports them.

## General information

Introduce the organization or domain represented by the model for readers who
understand OPC UA but may not know the industry. Refer readers to the OPC UA
introduction publication instead of repeating its general explanation.

## Use cases

Describe the supported use cases. For each one, state what an actor needs to
do and what information or behavior the model must support.

## Information Model overview

Explain the model's principal elements and how they relate. Introduce enough
context for the reader to understand each concept before referring to it. A
section may direct readers forward for detail or a formal definition, but it
must establish the concept first.

## Model definitions

Use the current publisher's Markdown structure and include only model groups
that apply. The published specification's model chapters use these names:

### OPC UA ObjectTypes

For each applicable type, use a heading such as `<some>Type definition`,
followed by `Overview` and `ObjectType definition` subheadings. Include method
subheadings, such as `<some>Method`, where the type defines Methods. The
template also shows named type sections such as `ExampleStateMachineType`.

### OPC UA EventTypes

Include a definition for each applicable EventType, such as
`<some>EventType`.

### OPC UA VariableTypes

Include a definition for each applicable VariableType, such as
`<some>VariableType`.

### OPC UA DataTypes

Include applicable structures, unions, enumerations, and OptionSets, such as
`<someStructure>`, `<someUnion>`, `<someEnumeration>`, and `<someOptionSet>`.
For structures, distinguish optional fields from fields that allow subtypes.
For enumerations, use `EnumStrings` for zero-based sequential values and
`EnumValues` otherwise. Define OptionSet values by bit position.

### OPC UA ReferenceTypes

For each applicable ReferenceType, define its inverse name, symmetry, abstract
status, parent type, and source and target constraints, using a type-specific
heading such as `<someReferenceType>`.

### Instances

Describe each applicable well-known instance, such as `<someInstance>`, and
explain its purpose.

### Well-Known BrowseNames

List each applicable `Well-Known <Type> BrowseNames` group and explain the
purpose of each name.

For every defined type, explain what it represents before presenting its
formal definition. State inheritance as a "Subtype of" relationship; do not
add a `HasSubtype` reference to a type definition. Put primary Conformance
Units at the end of each definition and keep the NodeSet classification
consistent with them.

Use symbolic NodeIds in model descriptions and define actual NodeIds in
normative Annex A. Distinguish model-defined NodeIds from server-generated
NodeIds. Distinguish a BrowseName's `NamespaceIndex`, namespace URI, and String
`Name` from one another and from xRegistry String identifiers. Keep
`ValueRank`, `ArrayDimensions`, DataType, TypeDefinition, and ModellingRule
consistent across the prose, source model, and published definition.

For Methods, describe the signature and arguments, document defined result
codes, and identify additional AddressSpace elements when the Method defines
properties beyond its argument properties.

## Profiles and Conformance Units

Define testable functionality groups. Include at least one Profile or Facet
for the companion specification. Keep each Conformance Unit name consistent
across its definition, the Profiles that require it, and the model elements
that implement it. State whether included Profile Database content is an
informative snapshot or the normative definition.

The current publisher template generates this content from its designated
source data. Follow the repository's current authoring guide rather than
duplicating generated content in authored prose.

## Namespaces

Identify the namespace URIs used by the model and explain how namespace
identifiers apply to NodeIds and BrowseNames. For an information model, verify
that namespace metadata and the NodeSet agree on the URI, version, publication
date, subset status, and static NodeId policy. A namespace URI is an
identifier, not a promise that it resolves as a network URL.

The current publisher template derives namespace content from its designated
source data and the NodeSet. Verify those sources instead of duplicating
generated content in authored prose.

## Normative Annex A

Define the mappings for the model namespace, NodeSet, and supplementary files.
Use a capability identifier only when the specification needs one. Keep the
namespace URI, namespace version, model metadata, and published artifact
identifiers consistent. Use the applicable standard naming conventions for
NodeIds, NodeSet files, and DataType schemas.

The current publisher template generates this content from its designated
source data and the NodeSet. Follow the current authoring guide for the
supported source fields.

## Bibliography

List informative sources that are not normative references. Cite OPC UA
documents by their canonical document identifiers and clause numbers. In
Publisher Markdown, use a local clause anchor for an in-document reference and
do not hard-code a generated clause number.

## Reading order

Write the specification so readers can follow it from beginning to end without
searching ahead to learn a term or concept. Introduce information before
relying on it. Forward references are appropriate for more detail or a formal
definition after the text has established enough context to be understood.
