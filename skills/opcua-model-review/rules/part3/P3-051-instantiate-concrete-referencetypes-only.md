---
id: "P3-051"
title: "Instantiate concrete ReferenceTypes only"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.3.1", "5.3.2", "7.2"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "references"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.2"]
---

# P3-051 - Instantiate concrete ReferenceTypes only

## Rule

Do not use an abstract ReferenceType as the type of an actual Reference between Nodes.

## Audit

Resolve the ReferenceType's IsAbstract, including standard abstract roots.

## Source

- [OPC 10000-3 v1.05.06, clause 5.3.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.1)
- [OPC 10000-3 v1.05.06, clause 5.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.2)
- [OPC 10000-3 v1.05.06, clause 7.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
