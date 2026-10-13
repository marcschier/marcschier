---
id: "P3-129"
title: "Derive custom Union types directly from Union"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.41"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.41"]
---

# P3-129 - Derive custom Union types directly from Union

## Rule

Every union DataType derives directly from Union, rather than from another custom union type.

## Audit

Resolve its direct supertype and classify it as a union from its semantic definition.

## Source

- [OPC 10000-3 v1.05.06, clause 8.41](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.41)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
