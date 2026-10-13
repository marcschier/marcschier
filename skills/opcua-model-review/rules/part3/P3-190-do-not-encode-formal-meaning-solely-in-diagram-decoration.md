---
id: "P3-190"
title: "Do not encode formal meaning solely in diagram decoration"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["C.2.1"]
strength: "MUST"
targets: ["document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/c-2-1"]
---

# P3-190 - Do not encode formal meaning solely in diagram decoration

## Rule

In Annex C notation, color and line thickness/style do not define formal model semantics.

## Audit

Use a legend or explicit model definitions for highlighting; do not infer a ModellingRule or NodeClass from decorative color.

## Source

- [OPC 10000-3 v1.05.06, clause C.2.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/c-2-1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
