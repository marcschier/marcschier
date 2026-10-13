---
id: "P3-038"
title: "Make View contents reachable and loop claims truthful"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.4"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.4"]
---

# P3-038 - Make View contents reachable and loop claims truthful

## Rule

Every View member is reachable from its View Node in that View. ContainsNoLoops is true only when the View's forward-reference graph is loop-free; use false when this cannot be determined.

## Audit

Use the actual View membership and Reference selection. Ordinary NodeSet References do not fully describe a Server-defined View.

## Source

- [OPC 10000-3 v1.05.06, clause 5.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
