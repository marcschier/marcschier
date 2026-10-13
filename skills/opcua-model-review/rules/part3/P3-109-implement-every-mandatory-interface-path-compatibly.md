---
id: "P3-109"
title: "Implement every Mandatory Interface path compatibly"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.10.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "interfaces"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2"]
---

# P3-109 - Implement every Mandatory Interface path compatibly

## Rule

An ObjectType applying an Interface supplies a similar Mandatory declaration at every Mandatory path in the fully inherited Interface hierarchy.

## Audit

Merge type and Interface ancestry, then compare qualified paths, classes, types, variable constraints, and Method contracts.

## Source

- [OPC 10000-3 v1.05.06, clause 4.10.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
