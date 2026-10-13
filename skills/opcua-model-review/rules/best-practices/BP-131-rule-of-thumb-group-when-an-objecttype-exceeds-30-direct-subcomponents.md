---
id: "BP-131"
title: "Rule of thumb: group when an ObjectType exceeds 30 direct subcomponents"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.5"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.5"]
---

# BP-131 - Rule of thumb: group when an ObjectType exceeds 30 direct subcomponents

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When an ObjectType has more than 30 subcomponents, introducing grouping Objects may be helpful; this applies recursively (a grouping Object that itself exceeds 30 subcomponents should itself be further grouped). When applying this heuristic, anticipated subtypes should be considered  -  e.g., if a base type only addresses one aspect (such as identification) today but subtypes with more substructure are expected later, it can make sense to group that aspect preemptively.

## Applicability

ObjectType/grouping-Object substructure design, including anticipated future subtypes.

## Exceptions and evidence limits

None stated; explicitly a heuristic, not an absolute ceiling.

## Audit

**NodeSet XML:** Count direct `HasComponent`/`HasProperty`/child-reference targets per `UAObjectType` (and per grouping Object within it); flag counts > 30 as an advisory (not a failure).

**Document:** Review substructure tables for candidates exceeding the threshold.

**Assessment:** Static-checkable (counting), with the disposition (whether to act on it) being an advisory/heuristic judgement, not a hard failure.

**Source wording:** SHOULD (explicitly framed as "a general rule of thumb," i.e., a soft heuristic)

## Source

- [OPC 11030 v1.03.03, clause 7.2.5](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.5)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
