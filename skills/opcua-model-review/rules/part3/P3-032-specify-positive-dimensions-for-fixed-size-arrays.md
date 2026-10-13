---
id: "P3-032"
title: "Specify positive dimensions for fixed-size arrays"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "values"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2"]
---

# P3-032 - Specify positive dimensions for fixed-size arrays

## Rule

When FixedSizeArray is true, provide ArrayDimensions with a positive length for every dimension. FixedSizeArray applies only to non-scalar DataVariables.

## Audit

Check the standard Property value and the effective rank/dimensions together.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
