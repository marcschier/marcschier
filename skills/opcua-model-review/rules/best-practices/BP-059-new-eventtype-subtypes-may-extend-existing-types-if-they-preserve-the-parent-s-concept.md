---
id: "BP-059"
title: "New EventType subtypes may extend existing types if they preserve the parent's concept"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.9"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9"]
---

# BP-059 - New EventType subtypes may extend existing types if they preserve the parent's concept

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is allowed to add new subtypes of Events that extend existing types, provided the subtype still maintains the concept expressed by its parent type (worked example: a limit-alarm subtype may make some limits mandatory or add more limits, but must still "be" a limit alarm).

## Applicability

EventType subtyping (ordinary leaf-subtype addition, distinct from the BP-058 insertion prohibition).

## Exceptions and evidence limits

None stated beyond "must maintain the concepts expressed by the parent type," which is not mechanically defined.

## Audit

**NodeSet XML:** Confirm the new subtype is a genuine leaf addition (not an insertion per BP-058) and that it only adds/narrows members rather than removing or contradicting inherited ones (cf. general subtyping limits in BP-055/BP-056 applied by analogy).

**Document:** Review whether the new subtype's documented behavior is conceptually consistent with its parent type.

**Assessment:** Semantically reviewable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
