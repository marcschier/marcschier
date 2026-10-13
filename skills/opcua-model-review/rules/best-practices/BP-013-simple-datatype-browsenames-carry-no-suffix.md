---
id: "BP-013"
title: "Simple DataType BrowseNames carry no suffix"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.3"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3"]
---

# BP-013 - Simple DataType BrowseNames carry no suffix

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Simple DataTypes (subtypes of a Built-in DataType) should not carry a naming suffix (examples: `Image`, `UtcTime`, `LocaleId`).

## Applicability

DataType NodeClass Nodes that are direct/indirect subtypes of a Built-in DataType (and not further categorized as Structured/Enumeration/OptionSet/Union).

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** For such `UADataType` nodes, flag BrowseNames ending in "Type", "DataType", or "Enum".

**Document:** Scan spec Simple DataType tables.

**Assessment:** Static-checkable.

**Source wording:** SHOULD NOT

## Source

- [OPC 11030 v1.03.03, clause 2.1.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
