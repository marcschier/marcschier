---
id: "P3-143"
title: "Apply DataTypeRefinements only at concrete Variable uses"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.5.3", "7.24"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.24"]
---

# P3-143 - Apply DataTypeRefinements only at concrete Variable uses

## Rule

UsesDataTypeRefinement starts from a non-declaration Variable, has at most one target, and refines exactly its DataType, not a merely related subtype.

## Audit

Reject VariableType/DataType/declaration sources. Concrete field-description and Method argument-metadata Variables may be eligible uses.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.5.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.3)
- [OPC 10000-3 v1.05.06, clause 7.24](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.24)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
