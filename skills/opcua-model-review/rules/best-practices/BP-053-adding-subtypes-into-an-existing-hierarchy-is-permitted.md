---
id: "BP-053"
title: "Adding subtypes into an existing hierarchy is permitted"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.9"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9"]
---

# BP-053 - Adding subtypes into an existing hierarchy is permitted

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is allowed to add new subtypes (leaf additions) into an existing ObjectType or VariableType hierarchy.

## Applicability

ObjectType/VariableType hierarchies, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

See BP-058 for the stricter EventType-hierarchy carve-out.

## Audit

**NodeSet XML:** Diff two NodeSet versions; a new `UAObjectType`/`UAVariableType` whose `HasSubtype` parent is a pre-existing type, added as a new leaf, is an expected non-violation.

**Document:** N/A.

**Assessment:** Impossible without dependencies (requires prior version for the "is this new" determination), otherwise static-checkable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
