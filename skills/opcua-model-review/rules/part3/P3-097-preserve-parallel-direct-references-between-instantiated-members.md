---
id: "P3-097"
title: "Preserve parallel direct References between instantiated members"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.4.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.3"]
---

# P3-097 - Preserve parallel direct References between instantiated members

## Rule

Where declarations are directly connected by several References, the corresponding References connect the same instantiated Nodes.

## Audit

Compare directly connected path pairs; indirect paths may validly lead to other Nodes.

## Source

- [OPC 10000-3 v1.05.06, clause 6.4.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
