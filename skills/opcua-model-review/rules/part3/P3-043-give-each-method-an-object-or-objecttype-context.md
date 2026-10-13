---
id: "P3-043"
title: "Give each Method an Object or ObjectType context"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.8", "5.7.1", "7.7"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "methods"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.8", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.7"]
---

# P3-043 - Give each Method an Object or ObjectType context

## Rule

A Method has at least one HasComponent parent that is an Object or ObjectType; calls identify one such context.

## Audit

Check normalized incoming component References and the documented Call objectId.

## Source

- [OPC 10000-3 v1.05.06, clause 4.8](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.8)
- [OPC 10000-3 v1.05.06, clause 5.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1)
- [OPC 10000-3 v1.05.06, clause 7.7](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.7)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
