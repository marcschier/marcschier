---
id: "P3-111"
title: "Avoid incompatible multiple-Interface paths"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.10.2"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "interfaces"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2"]
---

# P3-111 - Avoid incompatible multiple-Interface paths

## Rule

Applied Interfaces cannot require incompatible Nodes at one path; their type definitions must match or have a subtype relationship.

## Audit

Compare Interfaces together, including inherited members. Implementing each Interface in isolation is insufficient.

## Source

- [OPC 10000-3 v1.05.06, clause 4.10.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
