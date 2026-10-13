---
id: "P3-085"
title: "Treat multiple declaration BrowsePaths independently"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.3.3.2", "6.4.4.4.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.2"]
---

# P3-085 - Treat multiple declaration BrowsePaths independently

## Rule

Separate BrowsePaths to one declaration Node are evaluated as separate paths. An instance may provide different similar Nodes for those paths.

## Audit

Use path-based traversal, not a global visited-Node set that suppresses legitimate repeated paths.

## Source

- [OPC 10000-3 v1.05.06, clause 6.3.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.2)
- [OPC 10000-3 v1.05.06, clause 6.4.4.4.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
