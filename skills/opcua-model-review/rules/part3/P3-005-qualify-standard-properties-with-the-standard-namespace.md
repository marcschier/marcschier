---
id: "P3-005"
title: "Qualify standard Properties with the standard namespace"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["3.3.2", "5.2.4"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/3.3.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.4"]
---

# P3-005 - Qualify standard Properties with the standard namespace

## Rule

A standard Property's BrowseName uses the namespace that defines it, even when its NodeId uses the model or Server namespace.

## Audit

Resolve the BrowseName namespace URI independently of the NodeId namespace; compare identified standard Properties with their authoritative definitions.

## Source

- [OPC 10000-3 v1.05.06, clause 3.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/3.3.2)
- [OPC 10000-3 v1.05.06, clause 5.2.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
