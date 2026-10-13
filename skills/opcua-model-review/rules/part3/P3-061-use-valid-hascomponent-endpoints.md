---
id: "P3-061"
title: "Use valid HasComponent endpoints"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["7.7", "5.7.2", "5.7.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "references"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.7", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.3"]
---

# P3-061 - Use valid HasComponent endpoints

## Rule

HasComponent targets an Object, Variable, or Method. Object/Method targets require Object/ObjectType sources; Variable targets permit Object, ObjectType, DataVariable, or VariableType sources.

## Audit

Resolve target classes and Property roles. The explicit HasArgumentDescription extension permits a Method source for a metadata Variable; do not reject that standard-specific case.

## Source

- [OPC 10000-3 v1.05.06, clause 7.7](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.7)
- [OPC 10000-3 v1.05.06, clause 5.7.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.2)
- [OPC 10000-3 v1.05.06, clause 5.7.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
