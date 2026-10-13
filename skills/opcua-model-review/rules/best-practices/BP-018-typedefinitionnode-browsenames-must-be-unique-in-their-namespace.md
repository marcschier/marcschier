---
id: "BP-018"
title: "TypeDefinitionNode BrowseNames must be unique in their Namespace"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.4"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.4"]
---

# BP-018 - TypeDefinitionNode BrowseNames must be unique in their Namespace

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

BrowseNames of TypeDefinitionNodes (ObjectTypes, VariableTypes, DataTypes) shall be unique; a modeller must avoid creating duplicates inside the Namespace being authored.

## Applicability

ObjectType, VariableType, DataType Nodes within one Namespace.

## Exceptions and evidence limits

None stated at this location.

## Audit

**NodeSet XML:** Within one `NamespaceUri`, group `UAObjectType`/`UAVariableType`/`UADataType` nodes by BrowseName (Namespace-qualified) and flag duplicates.

**Document:** N/A (structural).

**Assessment:** Static-checkable.

**Source wording:** MUST

## Source notes

This clause attributes the "shall be unique" requirement itself to the base OPC UA specification ("as defined in the base OPC UA specification")  -  i.e., clause 2.1.4 restates a Part-3-sourced requirement rather than originating it. Recorded here only as it is textually present in OPC 11030 clause 2.1.4; the Part 3 citation is out of scope for this extraction.

## Source

- [OPC 11030 v1.03.03, clause 2.1.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
