---
id: "BP-162"
title: "Prefer Interfaces as the extensibility mechanism across an EventType hierarchy"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.7"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.7"]
---

# BP-162 - Prefer Interfaces as the extensibility mechanism across an EventType hierarchy

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Because EventTypes typically expose their data via Properties, a reasonable extensibility mechanism across an EventType's type hierarchy is to define specific Interfaces that can be implemented by various EventType subtypes. The document also notes Events are generated at server-determined incident times (unlike sampled/subscribed Variables) and are typically enriched with incident-specific context.

## Applicability

EventType hierarchy design.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Review whether cross-cutting EventType capabilities are expressed via `HasInterface` rather than repeated/duplicated Property sets across sibling EventTypes.

**Document:** Review EventType hierarchy design for Interface usage.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.7](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.7)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
