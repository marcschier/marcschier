---
id: "P3-045"
title: "Describe Method arguments with Argument arrays"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.7.1", "8.6"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.6"]
---

# P3-045 - Describe Method arguments with Argument arrays

## Rule

InputArguments and OutputArguments, when provided, are Properties containing Argument arrays in call order.

## Audit

Check the standard Property's type, rank, and value schema. Absence or an empty array means no arguments; do not invent missing parameters.

## Source

- [OPC 10000-3 v1.05.06, clause 5.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1)
- [OPC 10000-3 v1.05.06, clause 8.6](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.6)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
