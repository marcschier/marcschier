---
id: "P3-136"
title: "Interpret IsOptional according to StructureType"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.49", "8.51"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.49", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51"]
---

# P3-136 - Interpret IsOptional according to StructureType

## Rule

IsOptional controls field presence only for StructureWithOptionalFields, is false/ignored for ordinary Structure/Union, and controls subtyping in the subtyped-value variants.

## Audit

Determine the semantic StructureType before evaluating the flag or declaring a field optional.

## Source

- [OPC 10000-3 v1.05.06, clause 8.49](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.49)
- [OPC 10000-3 v1.05.06, clause 8.51](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
