---
id: "P3-057"
title: "Tighten inherited ReferenceType semantics and constraints"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.3.3.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.3.3"]
---

# P3-057 - Tighten inherited ReferenceType semantics and constraints

## Rule

A ReferenceType subtype preserves and may specialize inherited semantics, endpoint classes, cardinalities, and no-loop constraints; it cannot relax them.

## Audit

Compare custom ReferenceType definitions in prose as well as XML. Endpoint restrictions may exist only in documentation.

## Source

- [OPC 10000-3 v1.05.06, clause 5.3.3.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.3.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
