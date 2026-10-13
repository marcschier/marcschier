---
id: "P3-053"
title: "Define InverseName according to symmetry"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.3.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "references"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.2"]
---

# P3-053 - Define InverseName according to symmetry

## Rule

A non-symmetric ReferenceType provides InverseName; a symmetric ReferenceType omits it.

## Audit

Check explicit symmetry and effective default false in XML, while accepting an appropriate localized inverse name.

## Source

- [OPC 10000-3 v1.05.06, clause 5.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
