---
id: "P3-130"
title: "Reserve abstract numeric root children for namespace zero"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.7", "8.24", "8.30", "8.33"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "subtypes"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.7", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.24", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.30", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.33"]
---

# P3-130 - Reserve abstract numeric root children for namespace zero

## Rule

A direct subtype of BaseDataType, Number, Integer, or UInteger is defined only in the OPC UA namespace.

## Audit

Check direct HasSubtype relationships after namespace-URI resolution. Indirect custom specialization of a suitable concrete subtype is different.

## Source

- [OPC 10000-3 v1.05.06, clause 8.7](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.7)
- [OPC 10000-3 v1.05.06, clause 8.24](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.24)
- [OPC 10000-3 v1.05.06, clause 8.30](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.30)
- [OPC 10000-3 v1.05.06, clause 8.33](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.33)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
