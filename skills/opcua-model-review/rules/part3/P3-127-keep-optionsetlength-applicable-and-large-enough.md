---
id: "P3-127"
title: "Keep OptionSetLength applicable and large enough"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.3", "8.40"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.40"]
---

# P3-127 - Keep OptionSetLength applicable and large enough

## Rule

OptionSetLength applies only to OptionSet subtypes and, when supplied, accommodates every defined bit.

## Audit

Use byte counts, not bit counts, and compare the highest defined bit with the declared length.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3)
- [OPC 10000-3 v1.05.06, clause 8.40](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.40)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
