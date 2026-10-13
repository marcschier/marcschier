---
id: "BP-072"
title: "Changing ReferenceType usage restrictions is permitted if it does not contradict the rest of the model"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.14"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.14"]
---

# BP-072 - Changing ReferenceType usage restrictions is permitted if it does not contradict the rest of the model

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Changing a ReferenceType's usage-restriction rules is not forbidden, provided the change does not contradict other parts of the Information Model (worked example of a contradiction: a TypeDefinition relies on the ReferenceType being used in a way the new rules no longer permit). The document also notes, as supporting rationale, that OPC UA Clients should be able to handle unexpected results when following References (e.g., via the NodeClass/TypeDefinition carried in a ReferenceDescription).

## Applicability

Same as BP-071.

## Exceptions and evidence limits

Bounded by "does not contradict other parts of the Information Model."

## Audit

**NodeSet XML:** Not structurally checkable alone; would require cross-checking every TypeDefinition's use of the ReferenceType against the revised restriction.

**Document:** Review whether any existing TypeDefinition's documented use of the ReferenceType becomes inconsistent with the revised restriction text.

**Assessment:** Semantically reviewable.

**Source wording:** MAY (explicit permission, paired with BP-071's discouragement)

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source notes

The Client-robustness statement ("Clients should consider the results... and should be able to handle unexpected results") is client-implementation guidance included as rationale; not independently extracted as a modelling rule for the companion-spec's own Information Model.

## Source

- [OPC 11030 v1.03.03, clause 3.2.14](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.14)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
