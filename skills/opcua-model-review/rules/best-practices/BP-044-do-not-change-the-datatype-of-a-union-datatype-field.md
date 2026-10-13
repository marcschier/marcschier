---
id: "BP-044"
title: "Do not change the DataType of a Union DataType field"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.6"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.6"]
---

# BP-044 - Do not change the DataType of a Union DataType field

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is not allowed to change the DataType of an existing field of a released Union DataType.

## Applicability

Same as BP-043.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Diff matched fields' `DataType` across versions.

**Document:** Compare field tables.

**Assessment:** Impossible without dependencies; otherwise static-checkable.

**Source wording:** MUST NOT

## Source

- [OPC 11030 v1.03.03, clause 3.2.6](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.6)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
