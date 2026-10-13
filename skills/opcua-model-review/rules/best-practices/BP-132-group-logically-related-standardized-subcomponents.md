---
id: "BP-132"
title: "Group logically-related standardized subcomponents"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.5"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.5"]
---

# BP-132 - Group logically-related standardized subcomponents

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Grouping Objects make sense when they contain several standardized subcomponents that logically belong together (worked example: serial number, manufacturer, and model grouped as "identification").

## Applicability

ObjectType substructure design.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Not mechanically checkable (logical-relatedness is a semantic judgement).

**Document:** Review substructure organization for logically cohesive groupings.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.2.5](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.5)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
