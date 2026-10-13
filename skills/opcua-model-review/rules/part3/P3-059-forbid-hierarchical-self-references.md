---
id: "P3-059"
title: "Forbid hierarchical self-References"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["7.3"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "hierarchies"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.3"]
---

# P3-059 - Forbid hierarchical self-References

## Rule

A hierarchical Reference cannot have the same source and target Node.

## Audit

Compare canonical namespace-qualified identities for standard and custom hierarchical ReferenceTypes.

## Source

- [OPC 10000-3 v1.05.06, clause 7.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
