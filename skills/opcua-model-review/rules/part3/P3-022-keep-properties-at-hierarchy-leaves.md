---
id: "P3-022"
title: "Keep Properties at hierarchy leaves"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.5.2", "5.6.3", "7.3", "7.8"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "properties"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.5.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.8"]
---

# P3-022 - Keep Properties at hierarchy leaves

## Rule

A Property cannot be the source of any hierarchical Reference, including HasProperty, HasComponent, or Organizes. A Node and its Properties reside in the same Server.

## Audit

Check ReferenceType ancestry rather than a fixed list of names, and inspect remote-server identities where available.

## Source

- [OPC 10000-3 v1.05.06, clause 4.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.5.2)
- [OPC 10000-3 v1.05.06, clause 5.6.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.3)
- [OPC 10000-3 v1.05.06, clause 7.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.3)
- [OPC 10000-3 v1.05.06, clause 7.8](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.8)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
