---
id: "P3-081"
title: "Narrow inherited Variable DataTypes rather than widening them"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.2.8"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "inheritance"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.8"]
---

# P3-081 - Narrow inherited Variable DataTypes rather than widening them

## Rule

A VariableType subtype, declaration override, or instantiated declaration uses the original DataType or a subtype.

## Audit

Resolve both DataType ancestry and the corresponding VariableType/declaration context; abstract DataTypes may be specialized.

## Source

- [OPC 10000-3 v1.05.06, clause 6.2.8](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.8)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
