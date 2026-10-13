---
id: "P3-004"
title: "Separate table optionality from ModellingRules"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["3.3.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/3.3.2"]
---

# P3-004 - Separate table optionality from ModellingRules

## Rule

Do not infer a Property's ModellingRule solely from an M or O in a NodeClass table. Table presence requirements and instantiation ModellingRules describe different constraints.

## Audit

Check model tables and review logic for this distinction; a table's optional Attribute does not imply Optional on a child declaration.

## Source

- [OPC 10000-3 v1.05.06, clause 3.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/3.3.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
