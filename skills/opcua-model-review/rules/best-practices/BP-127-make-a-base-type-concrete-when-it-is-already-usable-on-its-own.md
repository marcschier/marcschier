---
id: "BP-127"
title: "Make a base type concrete when it is already usable on its own"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.3"]
strength: "INFORMATIVE"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.3"]
---

# BP-127 - Make a base type concrete when it is already usable on its own

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Favor a concrete base type when the supertype alone may directly be used if no more detailed information exists (worked example: a generic "tool" type with only usage time and identifier, with more specific tools like drills/saws/punches definable later as subtypes adding detail).

## Applicability

New type-hierarchy design (IsAbstract decision).

## Exceptions and evidence limits

N/A (paired with BP-126).

## Audit

**NodeSet XML:** Not mechanically checkable.

**Document:** Review design rationale.

**Assessment:** Semantically reviewable.

**Source wording:** Informative design heuristic

**Context guard:** Informative framing does not independently establish a conformance violation.

## Source

- [OPC 11030 v1.03.03, clause 7.2.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
