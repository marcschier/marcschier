---
id: "BP-090"
title: "InverseName text may change; its meaning shall not change"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.17"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes"]
---

# BP-090 - InverseName text may change; its meaning shall not change

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A ReferenceType's InverseName text may change across versions, but its meaning shall not change.

## Applicability

Asymmetric ReferenceType Nodes.

## Exceptions and evidence limits

Change in Server allowed? = Yes.

## Audit

**NodeSet XML:** Text-diff expected/non-violating; meaning check not mechanical.

**Document:** Review wording changes for semantic drift.

**Assessment:** Semantically reviewable.

**Source wording:** MAY (text) / MUST NOT (meaning)

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.17](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
