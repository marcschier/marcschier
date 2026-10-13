---
id: "BP-067"
title: "Revising argument description text is permitted if semantics are unchanged"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.11"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.11"]
---

# BP-067 - Revising argument description text is permitted if semantics are unchanged

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is allowed to change the description text of a Method parameter as long as doing so does not change the semantics of the argument.

## Applicability

Method Argument `Description` text.

## Exceptions and evidence limits

Bounded by "semantics unchanged."

## Audit

**NodeSet XML:** Not mechanically verifiable (textual semantic judgement).

**Document:** Review the nature of the wording change.

**Assessment:** Semantically reviewable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.11](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.11)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
