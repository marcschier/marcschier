---
id: "P3-077"
title: "Exclude type-only Nodes from instantiation and inheritance"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.2.2", "6.3.3.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "declarations"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.2"]
---

# P3-077 - Exclude type-only Nodes from instantiation and inheritance

## Rule

A Node below a type without a ModellingRule is type-only metadata, not an InstanceDeclaration to instantiate or inherit.

## Audit

Stop declaration-hierarchy traversal at such Nodes. Missing ModellingRules are not universally errors.

## Source

- [OPC 10000-3 v1.05.06, clause 6.2.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.2)
- [OPC 10000-3 v1.05.06, clause 6.3.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
