---
id: "P3-113"
title: "Avoid redundant HasInterface References"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.10.2"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2"]
---

# P3-113 - Avoid redundant HasInterface References

## Rule

Do not repeat HasInterface on a subtype or instance when the Interface is already applied by its supertype or TypeDefinition.

## Audit

Resolve inherited Interface application before calling a Reference redundant.

## Source

- [OPC 10000-3 v1.05.06, clause 4.10.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
