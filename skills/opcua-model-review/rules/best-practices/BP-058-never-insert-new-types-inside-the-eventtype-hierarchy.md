---
id: "BP-058"
title: "Never insert new types inside the EventType hierarchy"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.9"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9"]
---

# BP-058 - Never insert new types inside the EventType hierarchy

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is not allowed to add new types inside the EventType hierarchy (the part of the ObjectType hierarchy descending from `BaseEventType`)  -  unlike the general ObjectType/VariableType case (BP-054), this document states no "if absolutely necessary" carve-out for EventTypes. The rationale given is that EventTypes are used for Client-side filtering, and a new Client using the inserted EventType as a filter against an old Server would not work.

## Applicability

Any ObjectType in the subtype chain under `BaseEventType`, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

None stated  -  this reads as an unconditional prohibition, stricter than BP-054's "not recommended" treatment of the general case.

## Audit

**NodeSet XML:** Diff two NodeSet versions; flag any EventType (descendant of ns=0;i=2041 `BaseEventType`) whose `HasSubtype` parent changed, or any inserted EventType positioned as a new intermediate ancestor of pre-existing EventTypes.

**Document:** Compare EventType hierarchy diagrams/tables across versions.

**Assessment:** Impossible without dependencies (requires prior version); otherwise static-checkable.

**Source wording:** MUST NOT

## Source

- [OPC 11030 v1.03.03, clause 3.2.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
