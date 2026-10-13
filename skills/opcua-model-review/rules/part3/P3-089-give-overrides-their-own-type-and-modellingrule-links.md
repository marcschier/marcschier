---
id: "P3-089"
title: "Give overrides their own type and ModellingRule links"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.3.3.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "inheritance"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.3"]
---

# P3-089 - Give overrides their own type and ModellingRule links

## Rule

Every overriding InstanceDeclaration supplies its own HasModellingRule and, for Objects/Variables, HasTypeDefinition even if their targets are unchanged.

## Audit

Inspect the overriding Node itself, not just inherited defaults.

## Source

- [OPC 10000-3 v1.05.06, clause 6.3.3.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
