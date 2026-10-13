---
id: "BP-057"
title: "An inserted intermediate type may be abstract or concrete"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.9"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9"]
---

# BP-057 - An inserted intermediate type may be abstract or concrete

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The newly inserted type (per BP-054's carve-out) may be abstract or concrete  -  the document does not mandate either.

## Applicability

Conditional on BP-054's carve-out.

## Exceptions and evidence limits

N/A.

## Audit

**NodeSet XML:** None (permissive, no violation possible).

**Document:** None.

**Assessment:** Static-checkable only as a non-constraint guardrail.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source notes

Recorded to prevent a reviewer from wrongly treating either choice as non-compliant.

## Source

- [OPC 11030 v1.03.03, clause 3.2.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
