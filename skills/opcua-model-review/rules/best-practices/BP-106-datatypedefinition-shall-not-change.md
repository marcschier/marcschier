---
id: "BP-106"
title: "DataTypeDefinition shall not change"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.17"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes"]
---

# BP-106 - DataTypeDefinition shall not change

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A DataType's DataTypeDefinition attribute shall not change across versions.

## Applicability

DataType Nodes.

## Exceptions and evidence limits

Change in Server allowed? = No.

## Audit

**NodeSet XML:** Diff `DataTypeDefinition` (structure/enum/union field layout) across versions.

**Document:** Compare DataType structural tables across versions.

**Assessment:** Impossible without dependencies; otherwise static-checkable.

**Source wording:** MUST NOT

## Source notes

This table row is the umbrella attribute-level statement of the same constraint detailed field-by-field in BP-039-BP-044/BP-063-BP-064.

## Source

- [OPC 11030 v1.03.03, clause 3.2.17](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
