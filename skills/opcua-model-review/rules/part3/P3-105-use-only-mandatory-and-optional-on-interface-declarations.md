---
id: "P3-105"
title: "Use only Mandatory and Optional on Interface declarations"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.10.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "interfaces"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2"]
---

# P3-105 - Use only Mandatory and Optional on Interface declarations

## Rule

Interface InstanceDeclarations use Mandatory or Optional, not placeholders, ExposesItsArray, or other ModellingRules.

## Audit

Inspect all fully inherited nested Interface declarations, while leaving type-only metadata outside the declaration hierarchy.

## Source

- [OPC 10000-3 v1.05.06, clause 4.10.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
