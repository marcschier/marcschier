---
id: "BP-074"
title: "Do not reclassify a released ReferenceType's hierarchical/symmetric nature"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.15"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.15"]
---

# BP-074 - Do not reclassify a released ReferenceType's hierarchical/symmetric nature

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is not allowed to move types within a ReferenceType hierarchy, for example turning a hierarchical ReferenceType into a non-hierarchical one  -  this would change how Client-side filtering behaves.

## Applicability

ReferenceType Nodes, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Diff a ReferenceType's hierarchical classification (i.e., its position relative to `HierarchicalReferences`) across versions; flag reclassification.

**Document:** Compare ReferenceType classification tables across versions.

**Assessment:** Impossible without dependencies (requires prior version); otherwise static-checkable.

**Source wording:** MUST NOT

## Source

- [OPC 11030 v1.03.03, clause 3.2.15](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.15)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
