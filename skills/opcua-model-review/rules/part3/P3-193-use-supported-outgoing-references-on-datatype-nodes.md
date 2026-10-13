---
id: "P3-193"
title: "Use supported outgoing References on DataType Nodes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.3", "7.30"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.30"]
---

# P3-193 - Use supported outgoing References on DataType Nodes

## Rule

DataType Nodes use the specified Property, subtype, encoding, and explicitly introduced refinement relationships, rather than arbitrary outgoing relationships.

## Audit

Account for the explicit HasDataTypeRefinement addition and any applicable standard extension; do not read the older general exclusion sentence in isolation.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3)
- [OPC 10000-3 v1.05.06, clause 7.30](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.30)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
