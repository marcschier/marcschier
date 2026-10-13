---
id: "P3-063"
title: "Subtype only between compatible type NodeClasses"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.3.1", "7.10"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "subtypes"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.10"]
---

# P3-063 - Subtype only between compatible type NodeClasses

## Rule

HasSubtype connects ObjectType, VariableType, DataType, or ReferenceType Nodes of the same NodeClass.

## Audit

Check both endpoints after dependency resolution.

## Source

- [OPC 10000-3 v1.05.06, clause 6.3.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.1)
- [OPC 10000-3 v1.05.06, clause 7.10](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.10)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
