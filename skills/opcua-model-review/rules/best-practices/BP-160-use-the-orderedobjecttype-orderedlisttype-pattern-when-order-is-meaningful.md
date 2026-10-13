---
id: "BP-160"
title: "Use the OrderedObjectType/OrderedListType pattern when order is meaningful"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.6"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.6"]
---

# BP-160 - Use the OrderedObjectType/OrderedListType pattern when order is meaningful

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If the order of a set of Objects is itself meaningful, the fourth approach should be used: the `OrderedObjectType`/`OrderedListType` pattern, detailed in OPC 10000-5 (out of scope here beyond this pointer).

## Applicability

Set/list modelling where element order carries meaning.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Confirm the `TypeDefinition`/base type used is `OrderedListType` (or a subtype) when order-significance is documented.

**Document:** Review whether order-significant sets use this standardized pattern rather than an ad hoc ordering convention.

**Assessment:** Static-checkable (type usage) / semantically reviewable (whether order-significance was correctly identified).

**Source wording:** SHOULD

## Source notes

`OrderedObjectType`/`OrderedListType` itself is defined in OPC 10000-5, not detailed further here (out of scope, different Part).

## Source

- [OPC 11030 v1.03.03, clause 7.6](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.6)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
