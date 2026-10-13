---
id: "BP-041"
title: "Do not rename a field of a released Structure DataType"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.5"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.5"]
---

# BP-041 - Do not rename a field of a released Structure DataType

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is not allowed to change the name of a field of a released Structured DataType.

## Applicability

Same as BP-039.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Diff field lists by ordinal position; flag name changes at the same position.

**Document:** Compare field tables across versions.

**Assessment:** Impossible without dependencies; otherwise static-checkable.

**Source wording:** MUST NOT

## Source notes

See BP-039 Notes.

## Source

- [OPC 11030 v1.03.03, clause 3.2.5](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.5)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
