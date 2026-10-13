---
id: "BP-143"
title: "Option 2: Optional grouping + MandatoryPlaceholder subcomponent, when the grouping Object has no own functionality"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.8"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.8"]
---

# BP-143 - Option 2: Optional grouping + MandatoryPlaceholder subcomponent, when the grouping Object has no own functionality

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

"Option 2": when the grouping Object has no additional functionality of its own, it is recommended to make the grouping Object Optional and the subcomponent `MandatoryPlaceholder`, so a Client is not forced to browse an empty grouping Object only to discover it has nothing in it.

## Applicability

Grouping Objects with no functionality of their own, where "empty grouping Object" browsing should be avoided.

## Exceptions and evidence limits

Not used when extensibility of the grouping Object's own ModellingRule via subtyping is anticipated (see BP-144, Option 3).

## Audit

**NodeSet XML:** For such a grouping Object, confirm its ModellingRule is Optional and its placeholder child is `MandatoryPlaceholder`.

**Document:** Review the grouping Object's functionality and ModellingRule combination.

**Assessment:** Static-checkable (given the documented scenario).

**Source wording:** SHOULD (conditional)

## Source

- [OPC 11030 v1.03.03, clause 7.2.8](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.8)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
