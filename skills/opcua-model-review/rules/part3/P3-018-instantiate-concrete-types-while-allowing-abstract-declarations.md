---
id: "P3-018"
title: "Instantiate concrete types while allowing abstract declarations"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.5.2", "5.6.5", "6.2.1"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "types"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.1"]
---

# P3-018 - Instantiate concrete types while allowing abstract declarations

## Rule

A real Object or Variable instance cannot instantiate an abstract ObjectType or VariableType. An InstanceDeclaration may use an abstract type.

## Audit

Establish declaration context before checking IsAbstract. Do not flag an abstract declaration as an invalid real instance.

## Source

- [OPC 10000-3 v1.05.06, clause 5.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2)
- [OPC 10000-3 v1.05.06, clause 5.6.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5)
- [OPC 10000-3 v1.05.06, clause 6.2.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
