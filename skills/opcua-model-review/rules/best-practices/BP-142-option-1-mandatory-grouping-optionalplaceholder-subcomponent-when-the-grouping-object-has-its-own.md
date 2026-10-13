---
id: "BP-142"
title: "Option 1: Mandatory grouping + OptionalPlaceholder subcomponent, when the grouping Object has its own functionality"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.8"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.8"]
---

# BP-142 - Option 1: Mandatory grouping + OptionalPlaceholder subcomponent, when the grouping Object has its own functionality

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When "at least one" is *not* required, one of three combinations may be used (see BP-142-BP-144). This entry, "Option 1": when the grouping Object itself carries additional mandatory functionality (e.g., a Method to add subcomponents), it is recommended to make the grouping Object Mandatory and the subcomponent `OptionalPlaceholder`.

## Applicability

Grouping Objects that themselves provide functionality beyond merely holding placeholder children.

## Exceptions and evidence limits

Triggered specifically when the grouping Object has its own additional functionality; otherwise see BP-143/BP-144.

## Audit

**NodeSet XML:** For a grouping Object that defines its own Mandatory Methods/Variables beyond the placeholder children, confirm the grouping Object's own ModellingRule is Mandatory and its placeholder child is `OptionalPlaceholder`.

**Document:** Review the grouping Object's functionality and ModellingRule combination.

**Assessment:** Static-checkable (given the documented scenario).

**Source wording:** SHOULD (conditional)

## Source

- [OPC 11030 v1.03.03, clause 7.2.8](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.8)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
