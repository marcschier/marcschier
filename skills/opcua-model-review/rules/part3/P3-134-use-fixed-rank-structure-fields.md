---
id: "P3-134"
title: "Use fixed-rank Structure fields"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.51"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51"]
---

# P3-134 - Use fixed-rank Structure fields

## Rule

A StructureField ValueRank is Scalar or a fixed positive array rank; its supplied ArrayDimensions match that rank and are absent for a scalar.

## Audit

Do not carry Variable-only Any or OneOrMoreDimensions flexibility into StructureField definitions.

## Source

- [OPC 10000-3 v1.05.06, clause 8.51](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
