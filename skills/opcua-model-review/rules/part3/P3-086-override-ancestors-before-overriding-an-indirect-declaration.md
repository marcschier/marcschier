---
id: "P3-086"
title: "Override ancestors before overriding an indirect declaration"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.3.3.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.3"]
---

# P3-086 - Override ancestors before overriding an indirect declaration

## Rule

To override a nested declaration, override the directly referenced containing declaration and provide the hierarchical links back to the subtype.

## Audit

Check the full overriding path; a disconnected same-name Node is not a valid override.

## Source

- [OPC 10000-3 v1.05.06, clause 6.3.3.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
