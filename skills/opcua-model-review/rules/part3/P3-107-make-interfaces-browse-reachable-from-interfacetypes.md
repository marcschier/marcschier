---
id: "P3-107"
title: "Make Interfaces browse-reachable from InterfaceTypes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.10.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2"]
---

# P3-107 - Make Interfaces browse-reachable from InterfaceTypes

## Rule

Server Interfaces are directly or indirectly reachable by hierarchical browsing from InterfaceTypes.

## Audit

Inspect the complete Server organization or its documented browse paths; a standalone companion NodeSet may omit the entry-point organization.

## Source

- [OPC 10000-3 v1.05.06, clause 4.10.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
