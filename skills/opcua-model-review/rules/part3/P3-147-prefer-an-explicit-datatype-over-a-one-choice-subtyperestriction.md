---
id: "P3-147"
title: "Prefer an explicit DataType over a one-choice SubtypeRestriction"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.6.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.6.1"]
---

# P3-147 - Prefer an explicit DataType over a one-choice SubtypeRestriction

## Rule

Use at least two distinct allowed variants for a SubtypeRestriction; otherwise directly specify the concrete permitted subtype.

## Audit

Count semantic variant differences, including ranks and dimensions, rather than just Variable NodeIds.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.6.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.6.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
