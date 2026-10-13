---
id: "P3-021"
title: "Use exact PropertyType for Properties"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "properties"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.3"]
---

# P3-021 - Use exact PropertyType for Properties

## Rule

Every Property's HasTypeDefinition identifies PropertyType itself, not an application-specific VariableType.

## Audit

First identify Properties by incoming HasProperty relationships, then compare the resolved type identity. The explicit ban on subtyping PropertyType is separately sourced as P5-001.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
