---
id: "P3-189"
title: "Align diagram cardinality with the ModellingRule"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["C.2.3"]
strength: "MUST"
targets: ["document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/c-2-3"]
---

# P3-189 - Align diagram cardinality with the ModellingRule

## Rule

Use Annex C's specified correspondence between fixed/optional/multiple cardinalities and Mandatory, Optional, or placeholder ModellingRules.

## Audit

Compare diagram cardinality with model tables and XML. Additional numeric bounds need explicit semantics rather than being invented from the placeholder name.

## Source

- [OPC 10000-3 v1.05.06, clause C.2.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/c-2-3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
