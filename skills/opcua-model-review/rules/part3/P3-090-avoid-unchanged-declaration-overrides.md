---
id: "P3-090"
title: "Avoid unchanged declaration overrides"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.3.3.3"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.3"]
---

# P3-090 - Avoid unchanged declaration overrides

## Rule

Do not override an inherited Node unless the subtype needs to change it.

## Audit

Compare definitions and identify the intended change; redundant copies obscure inheritance.

## Source

- [OPC 10000-3 v1.05.06, clause 6.3.3.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
