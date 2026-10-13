---
id: "P3-019"
title: "Define Variables in a containing context"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.2", "5.8.5.2", "5.8.6.1"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "properties"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.6.1"]
---

# P3-019 - Define Variables in a containing context

## Rule

A Variable is a Property or DataVariable of at least one other Node, rather than a standalone value Node.

## Audit

Check containing relationships, including the explicit field-description and allowed-subtype descriptor contexts. An incomplete export may leave this unassessed.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)
- [OPC 10000-3 v1.05.06, clause 5.8.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.2)
- [OPC 10000-3 v1.05.06, clause 5.8.6.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.6.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
