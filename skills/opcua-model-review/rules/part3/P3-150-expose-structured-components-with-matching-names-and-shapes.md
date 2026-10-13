---
id: "P3-150"
title: "Expose structured components with matching names and shapes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["7.22.1", "7.22.2", "8.51"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.22.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.22.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51"]
---

# P3-150 - Expose structured components with matching names and shapes

## Rule

HasStructuredComponent starts from a structured Variable/VariableType and exposes matching field DataTypes/ranks with the declaring field namespace, or index-named array elements.

## Audit

Compare field names/types or the specified V[N] multidimensional index convention. Its positional behavior differs from ExposesItsArray.

## Source

- [OPC 10000-3 v1.05.06, clause 7.22.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.22.1)
- [OPC 10000-3 v1.05.06, clause 7.22.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.22.2)
- [OPC 10000-3 v1.05.06, clause 8.51](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
