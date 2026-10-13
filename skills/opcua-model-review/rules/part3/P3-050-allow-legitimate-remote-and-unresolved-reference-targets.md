---
id: "P3-050"
title: "Allow legitimate remote and unresolved Reference targets"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.4.4", "4.6.1", "6.4.2"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.4.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.6.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.2"]
---

# P3-050 - Allow legitimate remote and unresolved Reference targets

## Rule

A Reference may target a remote Server or a Node that does not exist. Well-known type targets may be represented elsewhere.

## Audit

Report unavailable dependencies or remote evidence as unassessed; do not treat every unresolved NodeId as a standards violation.

## Source

- [OPC 10000-3 v1.05.06, clause 4.4.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.4.4)
- [OPC 10000-3 v1.05.06, clause 4.6.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.6.1)
- [OPC 10000-3 v1.05.06, clause 6.4.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
