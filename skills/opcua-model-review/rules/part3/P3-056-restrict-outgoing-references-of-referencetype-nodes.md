---
id: "P3-056"
title: "Restrict outgoing References of ReferenceType Nodes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.3.3.1", "5.3.3.2"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "references"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.3.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.3.2"]
---

# P3-056 - Restrict outgoing References of ReferenceType Nodes

## Rule

ReferenceType Nodes are sources only of HasProperty and HasSubtype References, including permitted subtypes.

## Audit

Check outgoing logical directions; the inverse HasSubtype to a supertype does not make the subtype a forward source.

## Source

- [OPC 10000-3 v1.05.06, clause 5.3.3.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.3.1)
- [OPC 10000-3 v1.05.06, clause 5.3.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.3.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
