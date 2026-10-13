---
id: "P3-137"
title: "Apply StructureField MaxStringLength to compatible types"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.51"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51"]
---

# P3-137 - Apply StructureField MaxStringLength to compatible types

## Rule

Use field string/byte-string length metadata only where the field's DataType supports it, with zero for an unknown maximum and per-element limits for arrays.

## Audit

The source table mentions LocalizedText but its exclusion sentence mentions only String/ByteString; record this tension rather than automatically rejecting LocalizedText limits.

## Source

- [OPC 10000-3 v1.05.06, clause 8.51](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
