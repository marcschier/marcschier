---
id: "P3-080"
title: "Retain required Attribute information in overrides"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.2.7", "6.3.2", "6.3.3.3", "6.4.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.7", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.2"]
---

# P3-080 - Retain required Attribute information in overrides

## Rule

An overriding declaration retains Attributes supplied by its predecessor. Optional Attributes may be added; NodeClass/BrowseName remain fixed for declaration overrides.

## Audit

Distinguish type-level BrowseName/DisplayName specialization from child-declaration naming invariance and respect XML defaults.

## Source

- [OPC 10000-3 v1.05.06, clause 6.2.7](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.7)
- [OPC 10000-3 v1.05.06, clause 6.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.2)
- [OPC 10000-3 v1.05.06, clause 6.3.3.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.3)
- [OPC 10000-3 v1.05.06, clause 6.4.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
