---
id: "P3-203"
title: "Keep Method invocation semantics scoped and run-to-completion"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.8", "5.7.1"]
strength: "MUST"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.8", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1"]
---

# P3-203 - Keep Method invocation semantics scoped and run-to-completion

## Rule

Method invocations are scoped to their owning Object/ObjectType, complete with a response, and do not introduce independent invocation state into the AddressSpace.

## Audit

Review operation semantics. A Method may start asynchronous work whose ongoing state is represented separately by its Object; do not confuse that with an unfinished Call invocation.

## Source

- [OPC 10000-3 v1.05.06, clause 4.8](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.8)
- [OPC 10000-3 v1.05.06, clause 5.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
