---
id: "P3-139"
title: "Bind each DataTypeRefinement to one Structured DataType"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.5.1", "5.8.5.2", "5.8.5.3", "7.30"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.30"]
---

# P3-139 - Bind each DataTypeRefinement to one Structured DataType

## Rule

A DataTypeRefinement is an appropriately typed Object with exactly one owning Structured DataType through HasDataTypeRefinement or a subtype.

## Audit

Check owner class, refined type, target ObjectType, and owner cardinality. Several refinements may belong to one DataType.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.5.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.1)
- [OPC 10000-3 v1.05.06, clause 5.8.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.2)
- [OPC 10000-3 v1.05.06, clause 5.8.5.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.3)
- [OPC 10000-3 v1.05.06, clause 7.30](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.30)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
