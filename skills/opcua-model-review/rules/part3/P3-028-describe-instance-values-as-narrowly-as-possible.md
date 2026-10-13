---
id: "P3-028"
title: "Describe instance values as narrowly as possible"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2"]
---

# P3-028 - Describe instance values as narrowly as possible

## Rule

Set an instantiated Variable's DataType, ValueRank, and ArrayDimensions to the most restrictive supported values.

## Audit

Compare declared flexibility with actual supported values; broad declarations may be justified when the underlying system is not known.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
