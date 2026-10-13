---
id: "P3-199"
title: "Use defined instance BrowseName defaults where possible"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.10.3", "5.5.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2"]
---

# P3-199 - Use defined instance BrowseName defaults where possible

## Rule

Use an ObjectType's DefaultInstanceBrowseName for instances where applicable, particularly AddIns, while avoiding duplicate default-name uses under one parent.

## Audit

Compare actual names with the default QualifiedName; legitimate instance-specific names remain possible.

## Source

- [OPC 10000-3 v1.05.06, clause 4.10.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.3)
- [OPC 10000-3 v1.05.06, clause 5.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
