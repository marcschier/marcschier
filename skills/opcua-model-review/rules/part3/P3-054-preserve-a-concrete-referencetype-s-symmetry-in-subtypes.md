---
id: "P3-054"
title: "Preserve a concrete ReferenceType's symmetry in subtypes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.3.2"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "references"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.2"]
---

# P3-054 - Preserve a concrete ReferenceType's symmetry in subtypes

## Rule

A direct or indirect subtype of a concrete ReferenceType cannot change its Symmetric value.

## Audit

Compare each subtype with concrete ancestors, not only its immediate parent.

## Source

- [OPC 10000-3 v1.05.06, clause 5.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
