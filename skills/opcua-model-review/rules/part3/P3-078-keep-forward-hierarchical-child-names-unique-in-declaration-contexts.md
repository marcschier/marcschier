---
id: "P3-078"
title: "Keep forward hierarchical child names unique in declaration contexts"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.5.1", "5.5.2", "5.6.4", "5.6.5", "5.7.1", "6.2.6"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "declarations"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.6"]
---

# P3-078 - Keep forward hierarchical child names unique in declaration contexts

## Rule

Forward hierarchical targets have unique qualified BrowseNames under a TypeDefinitionNode or InstanceDeclaration, so declaration BrowsePaths are unambiguous.

## Audit

Compare distinct target Nodes per declaration parent across all hierarchical ReferenceTypes. Do not impose this rule on all ordinary instance children.

## Source

- [OPC 10000-3 v1.05.06, clause 5.5.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.1)
- [OPC 10000-3 v1.05.06, clause 5.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2)
- [OPC 10000-3 v1.05.06, clause 5.6.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.4)
- [OPC 10000-3 v1.05.06, clause 5.6.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5)
- [OPC 10000-3 v1.05.06, clause 5.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1)
- [OPC 10000-3 v1.05.06, clause 6.2.6](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.6)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
