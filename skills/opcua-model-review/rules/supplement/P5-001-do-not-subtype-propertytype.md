---
id: "P5-001"
title: "Do not subtype PropertyType"
spec: "OPC 10000-5"
version: "1.05.06"
clauses: ["7.3"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "subtypes"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-5/v1.05.06/7.3"]
---

# P5-001 - Do not subtype PropertyType

## Rule

PropertyType cannot have subtypes. Use a DataVariable and a suitable VariableType when value semantics need specialization.

## Audit

Check HasSubtype relationships with PropertyType as source, including those serialized as inverse References on the proposed subtype. This prohibition is from Part 5, not invented from Part 3.

## Source

- [OPC 10000-5 v1.05.06, clause 7.3](https://reference.opcfoundation.org/specs/OPC-10000-5/v1.05.06/7.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
