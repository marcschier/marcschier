---
id: "P3-008"
title: "Persist canonical NodeId identity rather than namespace indexes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.2", "8.2.2", "8.2.3"]
strength: "MUST"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.2.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.2.3"]
---

# P3-008 - Persist canonical NodeId identity rather than namespace indexes

## Rule

Persist the identifier type, identifier value, and namespace URI of a Node. Namespace indexes may change between Sessions; string identifiers remain case-sensitive.

## Audit

Review the persistence contract or compare runtime exports across Sessions. A single NodeSet cannot establish identity stability.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.2)
- [OPC 10000-3 v1.05.06, clause 8.2.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.2.2)
- [OPC 10000-3 v1.05.06, clause 8.2.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.2.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
