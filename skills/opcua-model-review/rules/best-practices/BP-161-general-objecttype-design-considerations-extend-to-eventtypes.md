---
id: "BP-161"
title: "General ObjectType design considerations extend to EventTypes"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.7"]
strength: "INFORMATIVE"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.7"]
---

# BP-161 - General ObjectType design considerations extend to EventTypes

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Because EventTypes are themselves ObjectTypes, the general ObjectType design considerations of clause 7.2 apply to them too.

## Applicability

EventType design.

## Exceptions and evidence limits

N/A  -  see BP-058 for a case where EventTypes are treated *more* strictly than ObjectTypes generally (hierarchy-insertion prohibition has no carve-out).

## Audit

**NodeSet XML:** N/A (cross-reference statement).

**Document:** N/A.

**Assessment:** Informative.

**Source wording:** Informative (explicit scope-extension statement)

**Context guard:** Informative framing does not independently establish a conformance violation.

## Source

- [OPC 11030 v1.03.03, clause 7.7](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.7)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
