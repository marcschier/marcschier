---
id: "P3-144"
title: "Apply nested field refinements through their concrete descriptors"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.5.2", "5.8.6.2"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.6.2"]
---

# P3-144 - Apply nested field refinements through their concrete descriptors

## Rule

Concrete Variables describing structured fields may themselves apply a matching DataTypeRefinement or SubtypeRestriction.

## Audit

Distinguish a permitted concrete descriptor from an InstanceDeclaration; preserve the parent field's encoding and restriction rules.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.2)
- [OPC 10000-3 v1.05.06, clause 5.8.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.6.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
