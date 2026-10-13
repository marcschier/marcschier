---
id: "P3-001"
title: "Use only the defined NodeClasses"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.4.2", "8.29"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "identity"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.4.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.29"]
---

# P3-001 - Use only the defined NodeClasses

## Rule

Do not introduce an application-specific NodeClass or extend an existing NodeClass. Model extensions with Nodes, types, Properties, and References.

## Audit

Check each node's class and any prose proposing new classes against the eight defined classes.

## Source

- [OPC 10000-3 v1.05.06, clause 4.4.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.4.2)
- [OPC 10000-3 v1.05.06, clause 8.29](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.29)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
