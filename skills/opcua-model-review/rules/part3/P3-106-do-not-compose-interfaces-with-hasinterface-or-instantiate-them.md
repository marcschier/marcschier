---
id: "P3-106"
title: "Do not compose Interfaces with HasInterface or instantiate them"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.10.2", "7.19"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "interfaces"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.19"]
---

# P3-106 - Do not compose Interfaces with HasInterface or instantiate them

## Rule

An Interface is not a HasInterface source. BaseInterfaceType and its subtypes are not HasTypeDefinition targets.

## Audit

Check the Interface's ancestry and both Reference source/target roles. Interface specialization uses HasSubtype.

## Source

- [OPC 10000-3 v1.05.06, clause 4.10.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2)
- [OPC 10000-3 v1.05.06, clause 7.19](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.19)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
