---
id: "BP-097"
title: "A VariableType's ValueRank shall not change (no Server exception)"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.17"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes"]
---

# BP-097 - A VariableType's ValueRank shall not change (no Server exception)

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A VariableType's own ValueRank shall not change, with a flat "No" Server exception (contrast BP-095's Variable-level carve-out).

## Applicability

VariableType Nodes.

## Exceptions and evidence limits

None.

## Audit

**NodeSet XML:** Diff `ValueRank` across versions.

**Document:** Compare VariableType ValueRank columns.

**Assessment:** Impossible without dependencies; otherwise static-checkable.

**Source wording:** MUST NOT

## Source

- [OPC 11030 v1.03.03, clause 3.2.17](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
