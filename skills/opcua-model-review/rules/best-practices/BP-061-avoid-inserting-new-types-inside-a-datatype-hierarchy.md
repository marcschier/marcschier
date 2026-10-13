---
id: "BP-061"
title: "Avoid inserting new types inside a DataType hierarchy"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.10"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.10"]
---

# BP-061 - Avoid inserting new types inside a DataType hierarchy

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is not recommended to insert new types inside an existing DataType hierarchy, analogous to the ObjectType/VariableType case (cross-referencing Figure 1 at clause 3.2.9).

## Applicability

DataType hierarchies, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

If "absolutely necessary," subject to BP-062-BP-064.

## Audit

**NodeSet XML:** Same insertion-detection approach as BP-054, applied to DataType `HasSubtype` chains.

**Document:** N/A beyond the cross-reference.

**Assessment:** Impossible without dependencies; otherwise static-checkable.

**Source wording:** SHOULD NOT

## Source

- [OPC 11030 v1.03.03, clause 3.2.10](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.10)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
