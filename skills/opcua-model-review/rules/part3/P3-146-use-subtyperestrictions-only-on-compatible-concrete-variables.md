---
id: "P3-146"
title: "Use SubtypeRestrictions only on compatible concrete Variables"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.6.1", "7.28"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.6.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.28"]
---

# P3-146 - Use SubtypeRestrictions only on compatible concrete Variables

## Rule

UsesSubtypeRestriction starts from a non-declaration Variable, has at most one target, matches the restricted DataType exactly, and supports all allowed variant shapes.

## Audit

Check context and the whole allowed-variant set. The NoSubDataTypes example has tension with its general definition; mark uncertain bit behavior for source clarification.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.6.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.6.1)
- [OPC 10000-3 v1.05.06, clause 7.28](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.28)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
