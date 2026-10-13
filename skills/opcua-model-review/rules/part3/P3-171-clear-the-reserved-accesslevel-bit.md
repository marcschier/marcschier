---
id: "P3-171"
title: "Clear the reserved AccessLevel bit"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.57"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "values"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.57"]
---

# P3-171 - Clear the reserved AccessLevel bit

## Rule

The reserved bit 7 of AccessLevel and UserAccessLevel is zero.

## Audit

Check decoded byte masks rather than treating all eight bits as available vendor flags.

## Source

- [OPC 10000-3 v1.05.06, clause 8.57](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.57)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
