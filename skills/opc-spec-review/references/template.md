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
outline covers the content, model-table structure, and semantic markup that
the source must carry.

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

Write Markdown heading text as plain text, without formatting characters such
as backticks, asterisks, or underscores. Do not apply inline code, bold, or
italics in headings, even for OPC UA terms or model names. Keep the Markdown
heading markers and supported clause anchors; they are structural syntax, not
heading text. Apply semantic emphasis in body prose, not headings. If an exact
identifier contains one of these characters, use a plain descriptive heading
and give the unchanged identifier in the body.

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

## Authoring checks (not publication clauses)

### Tables in Markdown and rendered HTML

The Companion Specification template defines the information and column
meanings for model tables. The current Markdown template defines how authors
encode those tables and how the publisher converts them. Read its current
authoring guide and companion-specification skill; do not add HTML or CSS
layout instructions to the Markdown source.

Use the Markdown table syntax supported by the pinned publisher. In this
template, a table has a header row, a separator row, and data rows with the
same number of cells as the header. Use the specified column names and keep
one value per cell. If a table cell needs a list, use the publisher-supported
`<br>`-separated list form, with each item beginning `- ` or `1. `. Do not put
a nested Markdown table inside a cell; represent each related item as a row in
the corresponding flat table. Repeat a BrowsePath on each row unless the
current authoring contract defines a continuation convention.

Put one Markdown caption and anchor before each logical table group. For
example:

```markdown
*Table - <Type> Definition* {#t1 defines=<Type>}
```

Let the publisher derive the table number and conventional anchor from the
caption. Cite the table with an empty link label such as `[](#t1)`; do not type
a table number into a caption or cross-reference. In the current template,
`compose` normalizes anchors and updates citations. Consecutive tables that
form one type definition share its caption and number, with a blank line
between table blocks. Do not add a separate caption for each block.

The main type-definition group contains an Attribute/Value block, a References
block, and a Conformance Units block, in that order. Keep the six-column
References grid intact:

```markdown
*Table - <Type> Definition* {#t1 defines=<Type>}

| **Attribute** | **Value** |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| BrowseName | <Type> |  |  |  |  |
| IsAbstract | False |  |  |  |  |

| **References** | **Node Class** | **BrowseName** | **DataType** | **TypeDefinition** | **Other** |
| --- | --- | --- | --- | --- | --- |
| 0:HasComponent | Variable | <someVariable> | 0:Double | 0:BaseDataVariableType | O |

| **Conformance Units** |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| <ConformanceUnit name> |  |  |  |  |  |
```

The trailing empty cells preserve the template's column spans. In the
References block, include DataType only for Variables and TypeDefinition only
for Objects and Variables. Use Other for applicable characteristics, such as
ModellingRules and AccessLevel. Use the symbolic BrowseName, DataType, and
TypeDefinition names, with a NamespaceIndex prefix when required. An optional
Attribute that is not set uses `--`. Put one primary Conformance Unit on each
row at the end of the definition group, consistent with `profiles.json` and
the NodeSet. Do not put a `HasSubtype` reference in a type-definition table.

Use the prescribed columns for related model tables:

| Table | Columns |
|---|---|
| Additional References | `SourceBrowsePath`, `Reference Type`, `Is Forward`, `TargetBrowsePath` |
| Additional Subcomponents | `BrowsePath`, `References`, `NodeClass`, `BrowseName`, `DataType`, `TypeDefinition`, `Others` |
| Additional Attribute values for child Nodes | `BrowsePath`, followed by one `<Attribute name> Attribute` column for each attribute |

Give each relation or subcomponent its own row. A SourceBrowsePath is relative
to the TypeDefinition. A TargetBrowsePath may be relative or absolute as the
model requires. Attribute values use the template's reversible OPC 10000-6
JSON-text convention. Add columns only for the attributes being specified.
Bind each authored table that documents a type with `defines=<Type>` in its
caption, including its Additional References, Additional Subcomponents, and
Attribute values tables.

For Structure field tables, use `Name`, `Type`, and `Description`, with an
`Optional` column only when fields can be optional or an `AllowSubtypes`
column when fields can allow subtypes. Do not combine both columns in one
Structure table. For a DataType field table that the publisher generates from
the NodeSet, use `datatype=<DataType>` in its caption instead of duplicating
the field rows in Markdown. Follow the current authoring contract if it changes
which tables are authored, generated, or bound.

Inspect the publisher's rendered HTML for each changed table group. Confirm
that each caption identifies the intended group; headers, cell spans, every
row, and every value survive conversion; links resolve to the generated table;
and grouped definition blocks remain one logical table group. Compare the HTML
with both the Markdown source and the model. Check the rendered column layout
against the current authoring guide: column headings and the first column
normally stay on one line, but long text and width constraints may require
wrapping. The publisher controls automatic sizing; do not add manual widths
or styles. Use the repository's
documented HTML render command when available. A correct Markdown source or a
GitHub preview alone does not establish that the publisher rendered the table
correctly. Report missing or altered table structure or layout to the template
or publisher owner; do not patch generated HTML or prescribe its styling.

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
