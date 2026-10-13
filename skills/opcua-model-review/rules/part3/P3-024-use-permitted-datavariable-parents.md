---
id: "P3-024"
title: "Use permitted DataVariable parents"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.4", "7.7", "5.7.2", "5.7.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "properties"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.7", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.3"]
---

# P3-024 - Use permitted DataVariable parents

## Rule

A DataVariable is a HasComponent target of an Object, ObjectType, DataVariable, or VariableType.

## Audit

Check component parent classes and roles, allowing the explicit Method-to-argument-metadata extension in HasArgumentDescription. Unresolved parents are evidence gaps.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.4)
- [OPC 10000-3 v1.05.06, clause 7.7](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.7)
- [OPC 10000-3 v1.05.06, clause 5.7.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.2)
- [OPC 10000-3 v1.05.06, clause 5.7.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
