---
id: "P3-135"
title: "Respect StructureField DataType and subtyping rules"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.51"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51"]
---

# P3-135 - Respect StructureField DataType and subtyping rules

## Rule

Ordinary Structure/optional-Structure/Union fields use concrete DataTypes, BaseDataType, or Structure. Subtyped-value StructureTypes use their field-level subtyping flags.

## Audit

Review abstract field types and StructureType together; IsOptional may mean subtyping permission rather than optional field presence.

## Source

- [OPC 10000-3 v1.05.06, clause 8.51](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
