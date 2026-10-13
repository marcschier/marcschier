---
id: "P3-013"
title: "Use the defining authority's namespace for standard types"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.4"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.4"]
---

# P3-013 - Use the defining authority's namespace for standard types

## Rule

A standards body's TypeDefinitionNode uses that body's namespace for both its NodeId and BrowseName.

## Audit

Check published standard type definitions; do not require arbitrary instance NodeIds and BrowseNames to share a namespace.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
