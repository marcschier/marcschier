---
id: "BP-179"
title: "Use the NodeId-to-abstract-ObjectType pattern when enumeration values need their own extensible specialization hierarchy"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.12.4"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.12.4"]
---

# BP-179 - Use the NodeId-to-abstract-ObjectType pattern when enumeration values need their own extensible specialization hierarchy

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A further pattern (used by Alarms' `ConditionClass`, and, as of version 1.05.02, also in normal Events): a Variable of DataType NodeId (e.g. `ConditionClassId`, `ConditionSubClassId`) points at an abstract ObjectType or one of its subtypes. This is more expressive than a plain enumeration since it allows specializing the "enumeration" values through the ObjectType hierarchy. If such specialization capability is required, this approach is recommended.

## Applicability

Discrete-value design needing an extensible specialization hierarchy, not just a flat extensible value list.

## Exceptions and evidence limits

None stated; use only when this extra specialization capability is actually needed (contrast with BP-178's simpler MultiState approach).

## Audit

**NodeSet XML:** For a Variable of DataType NodeId documented as playing this role, confirm it points to an abstract ObjectType (or subtype) rather than an arbitrary Node.

**Document:** Review specification text for this pattern's usage and rationale.

**Assessment:** Static-checkable (structural pattern) / semantically reviewable (whether the use case truly needs it over simpler alternatives).

**Source wording:** SHOULD (recommended "if such specialization is required")

## Source notes

The "version 1.05.02" reference is to the base OPC UA specification's (Part 3's) version history, mentioned here only as context; not independently verified (Part 3 out of scope).

## Source

- [OPC 11030 v1.03.03, clause 7.12.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.12.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
