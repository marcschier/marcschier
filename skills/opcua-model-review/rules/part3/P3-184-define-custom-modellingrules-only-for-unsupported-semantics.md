---
id: "P3-184"
title: "Define custom ModellingRules only for unsupported semantics"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["A.8", "6.4.4.1"]
strength: "INFORMATIVE"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-8", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.1"]
---

# P3-184 - Define custom ModellingRules only for unsupported semantics

## Rule

Use standard ModellingRules when they fit; document custom instantiation/subtyping semantics when they do not.

## Audit

A custom rule is permitted, not automatically invalid. Its obligations need explicit semantic review.

## Source

- [OPC 10000-3 v1.05.06, clause A.8](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-8)
- [OPC 10000-3 v1.05.06, clause 6.4.4.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
