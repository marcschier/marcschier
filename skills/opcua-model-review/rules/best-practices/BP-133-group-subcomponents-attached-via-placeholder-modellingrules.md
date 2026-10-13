---
id: "BP-133"
title: "Group subcomponents attached via Placeholder ModellingRules"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.5"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.5"]
---

# BP-133 - Group subcomponents attached via Placeholder ModellingRules

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Grouping Objects make sense when they contain subcomponents with no standardized BrowseNames  -  i.e., subcomponents using Placeholder ModellingRules (cross-ref clause 7.2.8)  -  so that the full set can easily be browsed together.

## Applicability

ObjectType substructure design involving Placeholder-ruled subcomponents.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** For `MandatoryPlaceholder`/`OptionalPlaceholder` children, confirm they sit under a dedicated grouping Object rather than directly and loosely on the ObjectType alongside unrelated fixed-name members.

**Document:** Review substructure organization.

**Assessment:** Static-checkable (structural placement), with "is this appropriate" being semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.2.5](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.5)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
