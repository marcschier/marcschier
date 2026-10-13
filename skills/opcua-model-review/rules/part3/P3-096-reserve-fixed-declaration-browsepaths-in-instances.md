---
id: "P3-096"
title: "Reserve fixed declaration BrowsePaths in instances"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.4.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.2"]
---

# P3-096 - Reserve fixed declaration BrowsePaths in instances

## Rule

An instance does not use a fixed Optional/Mandatory declaration path for an unrelated hierarchical target.

## Audit

Distinguish the declaration-derived member from additional instance Nodes. Part 3 permits ordinary instance name duplication in other contexts; do not apply a blanket instance uniqueness rule.

## Source

- [OPC 10000-3 v1.05.06, clause 6.4.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
