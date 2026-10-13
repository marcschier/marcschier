---
id: "P3-027"
title: "Keep ValueRank and ArrayDimensions consistent"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.2", "5.6.5", "8.6"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "values"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.6"]
---

# P3-027 - Keep ValueRank and ArrayDimensions consistent

## Rule

Use only the defined ValueRank forms. For fixed positive ranks, supplied dimensions match the rank. Scalar values have no dimensions; unknown dimension limits use zero.

## Audit

Apply the distinct rules for Variables, VariableTypes, and Arguments. String and ByteString remain scalar despite their array-like contents.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)
- [OPC 10000-3 v1.05.06, clause 5.6.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5)
- [OPC 10000-3 v1.05.06, clause 8.6](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.6)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
