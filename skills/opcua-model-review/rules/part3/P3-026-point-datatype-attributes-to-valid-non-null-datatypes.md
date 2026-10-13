---
id: "P3-026"
title: "Point DataType Attributes to valid non-null DataTypes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.2", "5.6.5", "5.8.1"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "values"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.1"]
---

# P3-026 - Point DataType Attributes to valid non-null DataTypes

## Rule

Variables and VariableTypes use a non-null DataType NodeId identifying a DataType Node.

## Audit

Resolve aliases and dependencies before checking target class. Abstract DataTypes are permitted in this Attribute.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)
- [OPC 10000-3 v1.05.06, clause 5.6.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5)
- [OPC 10000-3 v1.05.06, clause 5.8.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
