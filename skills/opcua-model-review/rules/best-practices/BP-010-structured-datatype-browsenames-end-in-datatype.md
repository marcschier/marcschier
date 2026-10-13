---
id: "BP-010"
title: "Structured DataType BrowseNames end in \"DataType\""
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3"]
---

# BP-010 - Structured DataType BrowseNames end in "DataType"

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

BrowseNames of Structured DataTypes (subtypes of the Structure DataType) should be suffixed "DataType" (examples: `RedundantServerDataType`, `TimeZoneDataType`).

## Applicability

DataType NodeClass Nodes that are subtypes of Structure.

## Exceptions and evidence limits

The clause explicitly notes the base OPC UA specification "does not always follow this pattern"  -  i.e., legacy base-spec structured DataTypes are a known, named exception and should not be treated as violations when encountered as pre-existing dependencies.

## Audit

**NodeSet XML:** For `UADataType` nodes whose supertype chain includes Structure (ns=0;i=22), confirm BrowseName ends with "DataType", excluding base-specification (ns=0) Nodes from violation reporting.

**Document:** Scan spec Structured DataType tables.

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.1.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
