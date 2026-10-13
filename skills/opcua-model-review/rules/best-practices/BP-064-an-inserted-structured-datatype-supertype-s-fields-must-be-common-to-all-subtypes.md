---
id: "BP-064"
title: "An inserted Structured DataType supertype's fields must be common to all subtypes"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.10"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.10"]
---

# BP-064 - An inserted Structured DataType supertype's fields must be common to all subtypes

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

For Structured DataTypes, an inserted supertype shall only have fields that are already defined in all of its subtypes; it must remain legal to construct every existing subtype considering DataType, ValueRank, and ArrayDimensions compatibility.

## Applicability

Conditional on BP-061's carve-out, Structured DataTypes specifically.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Confirm every field on the inserted supertype appears (with matching DataType/ValueRank/ArrayDimensions) on every one of its subtypes.

**Document:** Compare structure field tables across the proposed hierarchy.

**Assessment:** Static-checkable (given the candidate hierarchy).

**Source wording:** MUST

## Source

- [OPC 11030 v1.03.03, clause 3.2.10](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.10)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
