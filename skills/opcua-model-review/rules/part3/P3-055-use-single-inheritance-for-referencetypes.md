---
id: "P3-055"
title: "Use single inheritance for ReferenceTypes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.3.3.3", "7.10"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "subtypes"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.3.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.10"]
---

# P3-055 - Use single inheritance for ReferenceTypes

## Rule

Every ReferenceType except the root References has exactly one supertype. ReferenceTypes do not support multiple inheritance.

## Audit

Count logical HasSubtype parents after merging dependencies. Do not extend this prohibition to ObjectTypes: Part 3 defines only single-inheritance semantics there.

## Source

- [OPC 10000-3 v1.05.06, clause 5.3.3.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.3.3)
- [OPC 10000-3 v1.05.06, clause 7.10](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.10)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
