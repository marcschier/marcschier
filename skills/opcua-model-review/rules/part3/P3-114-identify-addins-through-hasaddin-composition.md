---
id: "P3-114"
title: "Identify AddIns through HasAddIn composition"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.10.3", "7.20"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "addins"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.20"]
---

# P3-114 - Identify AddIns through HasAddIn composition

## Rule

Apply an AddIn by a HasAddIn or subtype from an Object/ObjectType to an Object instance of the feature's ObjectType.

## Audit

Check classes and ReferenceType ancestry. AddIn ObjectTypes do not require a special AddIn supertype.

## Source

- [OPC 10000-3 v1.05.06, clause 4.10.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.3)
- [OPC 10000-3 v1.05.06, clause 7.20](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.20)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
