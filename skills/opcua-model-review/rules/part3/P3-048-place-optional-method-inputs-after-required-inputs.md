---
id: "P3-048"
title: "Place optional Method inputs after required inputs"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.7.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "methods"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.3"]
---

# P3-048 - Place optional Method inputs after required inputs

## Rule

Inputs marked with HasOptionalInputArgumentDescription follow all non-optional inputs in InputArguments.

## Audit

Correlate metadata Variables with argument names and array positions; optionality is not inferred from a default value.

## Source

- [OPC 10000-3 v1.05.06, clause 5.7.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
