---
id: "P3-017"
title: "Bind Objects and Variables to exactly one type"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.6.1", "5.5.1", "5.6.2", "7.13"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "types"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.6.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.13"]
---

# P3-017 - Bind Objects and Variables to exactly one type

## Rule

Each Object has exactly one HasTypeDefinition to an ObjectType; each Variable has exactly one to a VariableType. Other NodeClasses are not HasTypeDefinition sources.

## Audit

Count logical outgoing References after normalizing forward and inverse XML representations. Resolve the target before checking its class.

## Source

- [OPC 10000-3 v1.05.06, clause 4.6.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.6.1)
- [OPC 10000-3 v1.05.06, clause 5.5.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.1)
- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)
- [OPC 10000-3 v1.05.06, clause 7.13](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.13)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
