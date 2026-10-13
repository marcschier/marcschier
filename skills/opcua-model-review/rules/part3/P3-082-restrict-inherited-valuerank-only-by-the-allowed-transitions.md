---
id: "P3-082"
title: "Restrict inherited ValueRank only by the allowed transitions"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.2.8"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "inheritance"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.8"]
---

# P3-082 - Restrict inherited ValueRank only by the allowed transitions

## Rule

Any may narrow to any defined rank; ScalarOrOneDimension may narrow to Scalar or OneDimension; OneOrMoreDimensions may narrow to a fixed positive rank. Other ranks stay unchanged.

## Audit

Compare effective ranks for VariableType subtyping and Variable instantiation/overriding.

## Source

- [OPC 10000-3 v1.05.06, clause 6.2.8](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.8)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
