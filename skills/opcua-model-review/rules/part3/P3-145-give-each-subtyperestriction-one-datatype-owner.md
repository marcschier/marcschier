---
id: "P3-145"
title: "Give each SubtypeRestriction one DataType owner"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.6.1", "7.29", "7.30"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.6.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.29", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.30"]
---

# P3-145 - Give each SubtypeRestriction one DataType owner

## Rule

A SubtypeRestriction is an appropriately typed Object associated with exactly one DataType through HasDataTypeRefinement and defines allowed variants through Variables.

## Audit

Check owner uniqueness and descriptor types; compare each variant's DataType/rank/dimensions with the owner's permitted domain.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.6.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.6.1)
- [OPC 10000-3 v1.05.06, clause 7.29](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.29)
- [OPC 10000-3 v1.05.06, clause 7.30](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.30)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
