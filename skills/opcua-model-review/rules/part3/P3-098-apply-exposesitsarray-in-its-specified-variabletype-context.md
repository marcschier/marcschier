---
id: "P3-098"
title: "Apply ExposesItsArray in its specified VariableType context"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.4.4.4.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.3"]
---

# P3-098 - Apply ExposesItsArray in its specified VariableType context

## Rule

ExposesItsArray applies to a Variable declaration directly hierarchically referenced from an array-valued VariableType. Instances expose one suitable Variable per array element with compatible References.

## Audit

Check declaration class, parent class/rank, array cardinality, and relevant ReferenceTypes. This rule does not prescribe index-based BrowseNames.

## Source

- [OPC 10000-3 v1.05.06, clause 6.4.4.4.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
