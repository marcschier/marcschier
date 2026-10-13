---
id: "P3-049"
title: "Avoid duplicate logical References"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.4.4"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "references"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.4.4"]
---

# P3-049 - Avoid duplicate logical References

## Rule

A source-target pair cannot repeat the same ReferenceType. For Reference identity, subtypes of a concrete ReferenceType count as that concrete type.

## Audit

Normalize direction and namespace identity. A forward/inverse serialization pair of one logical edge is not a duplicate.

## Source

- [OPC 10000-3 v1.05.06, clause 4.4.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.4.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
