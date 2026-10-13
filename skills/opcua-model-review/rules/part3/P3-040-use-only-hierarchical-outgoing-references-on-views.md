---
id: "P3-040"
title: "Use only hierarchical outgoing References on Views"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.4"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "references"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.4"]
---

# P3-040 - Use only hierarchical outgoing References on Views

## Rule

A View is not the source of a NonHierarchical Reference.

## Audit

Resolve each outgoing ReferenceType and its ancestry, including custom types.

## Source

- [OPC 10000-3 v1.05.06, clause 5.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
