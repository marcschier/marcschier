---
id: "P3-093"
title: "Preserve nested declaration ModellingRules on type composition"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.4.4.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.3"]
---

# P3-093 - Preserve nested declaration ModellingRules on type composition

## Rule

When an instantiated type is used as another type's InstanceDeclaration, its inherited members initially retain their source ModellingRules and may only make allowed tightening changes.

## Audit

Identify composition inside a TypeDefinition and compare nested declarations with the composed type.

## Source

- [OPC 10000-3 v1.05.06, clause 6.4.4.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
