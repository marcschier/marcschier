---
id: "P3-087"
title: "Respect Reference replacement and cardinality on overrides"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.3.3.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.3"]
---

# P3-087 - Respect Reference replacement and cardinality on overrides

## Rule

An overriding Reference may refine its ReferenceType to a subtype. Replacing a single-cardinality non-hierarchical target preserves target class and compatible Object/Variable type.

## Audit

Compare inherited and replacement edges by paths and reference ancestry; ordinary non-hierarchical References otherwise add to the model.

## Source

- [OPC 10000-3 v1.05.06, clause 6.3.3.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
