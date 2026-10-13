---
id: "BP-130"
title: "Grouping Objects are a human-readability aid, not a functional requirement"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.5"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.5"]
---

# BP-130 - Grouping Objects are a human-readability aid, not a functional requirement

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

From a pure programmatic-access perspective, grouping Objects are not required (every subcomponent already has a standardized name); their value is improving human readability/understandability of a substructure (illustrated by Figure 2).

## Applicability

ObjectType substructure design.

## Exceptions and evidence limits

N/A.

## Audit

**NodeSet XML:** None (a guardrail against treating absence of grouping as a defect by itself).

**Document:** None.

**Assessment:** Informative.

**Source wording:** MAY / Informative

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source notes

Figure reference: https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.5#fig_2_example-of-grouping-objects

## Source

- [OPC 11030 v1.03.03, clause 7.2.5](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.5)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
