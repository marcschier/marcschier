---
id: "P3-060"
title: "Keep HasChild hierarchies acyclic"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["7.5", "7.6", "7.10"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "hierarchies"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.5", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.6", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.10"]
---

# P3-060 - Keep HasChild hierarchies acyclic

## Rule

Following only HasChild subtypes must not return to the starting Node. Multiple paths and multiple aggregation parents are otherwise permitted.

## Audit

Check the combined forward graph of HasChild subtypes. Organizes may form loops and is not included merely because it is hierarchical.

## Source

- [OPC 10000-3 v1.05.06, clause 7.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.5)
- [OPC 10000-3 v1.05.06, clause 7.6](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.6)
- [OPC 10000-3 v1.05.06, clause 7.10](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.10)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
