---
id: "P3-095"
title: "Validate Optional declarations when present"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.4.4.4.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "inheritance"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.2"]
---

# P3-095 - Validate Optional declarations when present

## Rule

An Optional member may be omitted. If present, it is similar to the declaration and fulfills its applicable mandatory descendants.

## Audit

Evaluate presence before child requirements and permit either a copied Node or a reference to an existing similar Node.

## Source

- [OPC 10000-3 v1.05.06, clause 6.4.4.4.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
