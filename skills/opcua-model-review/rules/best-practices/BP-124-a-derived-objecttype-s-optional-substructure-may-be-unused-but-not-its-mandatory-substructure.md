---
id: "BP-124"
title: "A derived ObjectType's optional substructure may be unused, but not its mandatory substructure"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.2"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.2"]
---

# BP-124 - A derived ObjectType's optional substructure may be unused, but not its mandatory substructure

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The candidate base ObjectType may contain optional substructure that isn't needed for the new design, but should not carry mandatory substructure that is unwanted/unneeded  -  i.e., unwanted mandatory baggage should disqualify a candidate base type.

## Applicability

New ObjectType design decisions, evaluating a candidate supertype.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Given a chosen supertype, confirm no inherited Mandatory member is irrelevant/unused by design intent (semantic judgement, not purely structural).

**Document:** Review rationale for why a candidate base type was accepted/rejected.

**Assessment:** Semantically reviewable.

**Source wording:** MAY (optional substructure may go unused) / SHOULD NOT (choose a base with unwanted mandatory substructure)

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 7.2.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
