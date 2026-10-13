---
id: "P3-012"
title: "Give types and entry points unique BrowseNames"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.4", "5.3.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "identity"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.2"]
---

# P3-012 - Give types and entry points unique BrowseNames

## Rule

Keep the BrowseNames of TypeDefinitionNodes, ReferenceTypes, and DataTypes unique in their applicable contexts. Well-known entry-point instances also require unique names.

## Audit

Compare namespace-qualified names in each relevant category, and review declared entry points. Do not impose global uniqueness on ordinary instances.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.4)
- [OPC 10000-3 v1.05.06, clause 5.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
