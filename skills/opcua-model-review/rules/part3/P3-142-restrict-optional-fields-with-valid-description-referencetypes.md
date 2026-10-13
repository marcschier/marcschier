---
id: "P3-142"
title: "Restrict optional fields with valid description ReferenceTypes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.5.2", "7.26", "7.27"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.26", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.27"]
---

# P3-142 - Restrict optional fields with valid description ReferenceTypes

## Rule

HasFieldDescriptionSetMandatory applies only to optional fields of optional-field Structures. IsDisabledOptionalField applies to such optional fields or Union alternatives.

## Audit

Do not make a Union alternative mandatory or apply these rules to ordinary Structure fields; optionality flags on subtyped-value types have different meaning.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.2)
- [OPC 10000-3 v1.05.06, clause 7.26](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.26)
- [OPC 10000-3 v1.05.06, clause 7.27](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.27)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
