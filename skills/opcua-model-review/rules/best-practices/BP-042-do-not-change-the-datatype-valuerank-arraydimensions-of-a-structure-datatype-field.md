---
id: "BP-042"
title: "Do not change the DataType/ValueRank/ArrayDimensions of a Structure DataType field"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.5"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.5"]
---

# BP-042 - Do not change the DataType/ValueRank/ArrayDimensions of a Structure DataType field

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is not allowed to change the DataType of a field of a released Structured DataType, including its ValueRank and ArrayDimensions.

## Applicability

Same as BP-039.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Diff field lists; flag changes to `DataType`, `ValueRank`, or `ArrayDimensions` on a matched field.

**Document:** Compare field tables across versions.

**Assessment:** Impossible without dependencies; otherwise static-checkable.

**Source wording:** MUST NOT

## Source notes

See BP-039 Notes.

## Source

- [OPC 11030 v1.03.03, clause 3.2.5](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.5)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
