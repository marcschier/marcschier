---
id: "P3-071"
title: "Reference EventTypes from valid generation contexts"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.5.2", "5.6.5", "5.7.1", "7.15"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.15"]
---

# P3-071 - Reference EventTypes from valid generation contexts

## Rule

GeneratesEvent points to BaseEventType or a subtype from the specified ObjectType, VariableType, or Method declaration context.

## Audit

Resolve EventType ancestry and context. GeneratesEvent is optional and is unrelated to an instance's SubscribeToEvents capability.

## Source

- [OPC 10000-3 v1.05.06, clause 5.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2)
- [OPC 10000-3 v1.05.06, clause 5.6.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5)
- [OPC 10000-3 v1.05.06, clause 5.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1)
- [OPC 10000-3 v1.05.06, clause 7.15](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.15)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
