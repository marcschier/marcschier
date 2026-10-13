---
id: "P3-112"
title: "Apply instance Interfaces only when compatible with the ObjectType"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.10.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "interfaces"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2"]
---

# P3-112 - Apply instance Interfaces only when compatible with the ObjectType

## Rule

An Object-level Interface must be applicable to its ObjectType, and the Object fulfills the corresponding Interface obligations. Several Interfaces are evaluated together.

## Audit

Check the ObjectType compatibility and actual Object members; an instance-only HasInterface is otherwise permitted.

## Source

- [OPC 10000-3 v1.05.06, clause 4.10.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
