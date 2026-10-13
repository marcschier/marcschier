---
id: "BP-121"
title: "Retain legacy DataTypeDictionary Nodes alongside DataTypeDefinition"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["6.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/6.3"]
---

# BP-121 - Retain legacy DataTypeDictionary Nodes alongside DataTypeDefinition

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The OPC UA specification has moved from the legacy DataTypeDictionary mechanism (OPC 10000-5) to the `DataTypeDefinition` Attribute (OPC 10000-3) for describing structured/enumeration DataTypes. UANodeSets of a Companion Specification should still contain the DataTypeDictionary Nodes anyway, so that their NodeIds remain standardized for applications that still rely on the older mechanism.

## Applicability

Companion Specification UANodeSets defining Structured or Enumeration DataTypes.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** For each Structured/Enumeration DataType, confirm a corresponding DataTypeDictionary-related Node (legacy encoding Nodes) is still present in addition to the `DataTypeDefinition` Attribute.

**Document:** N/A (NodeSet-only).

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 6.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/6.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
