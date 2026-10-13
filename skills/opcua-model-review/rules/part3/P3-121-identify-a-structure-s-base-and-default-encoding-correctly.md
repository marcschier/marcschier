---
id: "P3-121"
title: "Identify a Structure's base and default encoding correctly"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.48"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.48"]
---

# P3-121 - Identify a Structure's base and default encoding correctly

## Rule

StructureDefinition identifies the direct base DataType and correct StructureType. Its default encoding is null for abstract types, may be null for nested-only types, and otherwise identifies Default Binary.

## Audit

Compare semantic definitions with HasSubtype and HasEncoding. Do not infer nested-only usage solely because no Variable is present.

## Source

- [OPC 10000-3 v1.05.06, clause 8.48](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.48)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
