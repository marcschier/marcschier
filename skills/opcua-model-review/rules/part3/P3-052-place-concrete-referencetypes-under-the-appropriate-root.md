---
id: "P3-052"
title: "Place concrete ReferenceTypes under the appropriate root"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["7.2", "7.3", "7.4"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.4"]
---

# P3-052 - Place concrete ReferenceTypes under the appropriate root

## Rule

ReferenceTypes derive from References, and concrete ReferenceTypes belong under HierarchicalReferences or NonHierarchicalReferences. Hierarchical ReferenceTypes are non-symmetric.

## Audit

Resolve the whole ReferenceType ancestry; do not infer classification from a name containing Has.

## Source

- [OPC 10000-3 v1.05.06, clause 7.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.2)
- [OPC 10000-3 v1.05.06, clause 7.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.3)
- [OPC 10000-3 v1.05.06, clause 7.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
