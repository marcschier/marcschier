---
id: "P3-133"
title: "Place inherited Structure fields before new fields"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.48"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.48"]
---

# P3-133 - Place inherited Structure fields before new fields

## Rule

The semantic StructureDefinition begins with the base Structure's fields, followed by newly declared fields.

## Audit

Compare reconstructed definitions, not raw XML lists whose format may contain local fields only.

## Source

- [OPC 10000-3 v1.05.06, clause 8.48](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.48)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
