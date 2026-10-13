---
id: "P3-068"
title: "Bind at most one ModellingRule to an eligible Node"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.5.1", "5.6.2", "5.7.1", "6.4.4.1", "7.12"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "declarations"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.12"]
---

# P3-068 - Bind at most one ModellingRule to an eligible Node

## Rule

HasModellingRule sources are Objects, Variables, or Methods and have at most one such Reference to a ModellingRule Object.

## Audit

Count normalized References and resolve the target type when available. Vendor-defined ModellingRules are permitted.

## Source

- [OPC 10000-3 v1.05.06, clause 5.5.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.1)
- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)
- [OPC 10000-3 v1.05.06, clause 5.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1)
- [OPC 10000-3 v1.05.06, clause 6.4.4.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.1)
- [OPC 10000-3 v1.05.06, clause 7.12](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.12)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
