---
id: "P3-164"
title: "Use WriteMask bits only for supported Attributes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.60"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "values"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.60"]
---

# P3-164 - Use WriteMask bits only for supported Attributes

## Rule

Clear bits for unsupported Attributes and reserved bits; ValueForVariableType is zero on Variables.

## Audit

Check masks against the NodeClass Attribute set, keeping optional Attribute presence distinct from its supported definition.

## Source

- [OPC 10000-3 v1.05.06, clause 8.60](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.60)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
