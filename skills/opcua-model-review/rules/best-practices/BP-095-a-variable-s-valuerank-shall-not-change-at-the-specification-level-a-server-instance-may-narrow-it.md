---
id: "BP-095"
title: "A Variable's ValueRank shall not change at the specification level; a Server instance may narrow it"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.17"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes"]
---

# BP-095 - A Variable's ValueRank shall not change at the specification level; a Server instance may narrow it

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A Variable's ValueRank shall not change. As with DataType (BP-094), "Change in Server allowed?" = **No, for InstanceDeclarations**; **Yes, for instances, if it becomes more restrictive (as in subtype rules)**.

## Applicability

Variable Nodes; same two-audit-target distinction as BP-094.

## Exceptions and evidence limits

Same instance-level carve-out as BP-094.

## Audit

**NodeSet XML:** Same approach as BP-094, applied to `ValueRank`.

**Document:** Compare Variable ValueRank columns across versions.

**Assessment:** Impossible without dependencies; otherwise static-checkable.

**Source wording:** MUST NOT (at InstanceDeclaration/specification level)

## Source notes

See BP-094 Notes regarding the clause 3.2.12/Table 1 relationship.

## Source

- [OPC 11030 v1.03.03, clause 3.2.17](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
