---
id: "P3-141"
title: "Tighten field refinements without changing encoding"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.5.1", "5.8.5.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.2"]
---

# P3-141 - Tighten field refinements without changing encoding

## Rule

A refinement restricts permitted field usage, preserves rank and already specified size limits, and does not change the Structured DataType encoding.

## Audit

Apply Table 17 and StructureType-specific datatype/subtyping restrictions. Consult source tensions around NoSubDataTypes before asserting a bit-level violation.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.5.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.1)
- [OPC 10000-3 v1.05.06, clause 5.8.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
