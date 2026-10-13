---
id: "P3-104"
title: "Define Interfaces as abstract BaseInterfaceType subtypes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.10.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "interfaces"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2"]
---

# P3-104 - Define Interfaces as abstract BaseInterfaceType subtypes

## Rule

Every Interface is an abstract ObjectType derived directly or indirectly from BaseInterfaceType.

## Audit

Resolve type ancestry and effective IsAbstract; an I-prefixed name alone does not establish an Interface.

## Source

- [OPC 10000-3 v1.05.06, clause 4.10.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
