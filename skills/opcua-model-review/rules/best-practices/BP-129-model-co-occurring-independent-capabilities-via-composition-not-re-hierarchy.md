---
id: "BP-129"
title: "Model co-occurring independent capabilities via composition, not re-hierarchy"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.4"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.4"]
---

# BP-129 - Model co-occurring independent capabilities via composition, not re-hierarchy

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Even the BP-128 composition approach can run into trouble when an instance needs two or more independently-composable capabilities simultaneously (worked example: a device that can measure both temperature and flow). In that case, the capability itself (e.g., "can measure temperature," "can measure flow") should also be modelled via composition, rather than attempting to express it through the type hierarchy. The document cites PA-DIM as a worked real-world example (not detailed further here).

## Applicability

ObjectType/instance design where multiple independent capabilities may co-occur.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Not mechanically checkable; a reviewer can look for AddIn/Interface-based "capability" patterns (e.g., PA-DIM-style) when multiple composed aspects appear on the same instance.

**Document:** Review how multi-capability instances are modelled.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source notes

PA-DIM itself is referenced only as a pointer/example, not detailed in 11030; not further researched here (out of scope, different companion spec).

## Source

- [OPC 11030 v1.03.03, clause 7.2.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
