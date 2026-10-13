---
id: "BP-043"
title: "Do not add or remove fields of a released Union DataType"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.6"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.6"]
---

# BP-043 - Do not add or remove fields of a released Union DataType

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is not allowed to add or remove fields of a released Union DataType.

## Applicability

Union DataType Nodes, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Diff Union field lists across versions; flag additions/removals.

**Document:** Compare field tables.

**Assessment:** Impossible without dependencies; otherwise static-checkable.

**Source wording:** MUST NOT

## Source notes

Rationale: changes the set of allowed types and breaks interoperability between versions.

## Source

- [OPC 11030 v1.03.03, clause 3.2.6](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.6)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
