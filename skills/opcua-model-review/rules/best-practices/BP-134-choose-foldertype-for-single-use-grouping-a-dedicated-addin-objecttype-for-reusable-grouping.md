---
id: "BP-134"
title: "Choose FolderType for single-use grouping, a dedicated AddIn ObjectType for reusable grouping"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.5"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.5"]
---

# BP-134 - Choose FolderType for single-use grouping, a dedicated AddIn ObjectType for reusable grouping

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When a grouping Object is expected to be used in only one place, it is not necessary to create a specific ObjectType for it  -  the base `FolderType` should be used. When the same grouping may be reused in various places, a dedicated ObjectType (as an AddIn) should be defined so the grouping can be easily reused elsewhere.

## Applicability

Grouping-Object ObjectType selection.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** For a grouping Object used in exactly one place in the current model, flag a non-FolderType custom TypeDefinition as a candidate for simplification (advisory); for a grouping pattern repeated verbatim across multiple types without a shared ObjectType, flag as a candidate for introducing a dedicated AddIn type.

**Document:** Review grouping Object TypeDefinition choices across the model.

**Assessment:** Static-checkable (detecting the pattern), disposition semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.2.5](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.5)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
