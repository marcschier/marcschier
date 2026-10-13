---
id: "P3-076"
title: "Give each InstanceDeclaration one owning TypeDefinition"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.2.1", "6.2.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "declarations"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.3"]
---

# P3-076 - Give each InstanceDeclaration one owning TypeDefinition

## Rule

An InstanceDeclaration has a ModellingRule and a hierarchical path from its owning type. It cannot belong to two distinct TypeDefinitionNodes.

## Audit

Trace declaration paths through declarations, not all references. Inherited use by a subtype is not a second ownership claim.

## Source

- [OPC 10000-3 v1.05.06, clause 6.2.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.1)
- [OPC 10000-3 v1.05.06, clause 6.2.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
