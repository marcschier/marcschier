---
id: "P3-172"
title: "Honor AccessLevelEx subtype and persistence promises"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.58"]
strength: "MUST"
targets: ["nodeset", "document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.58"]
---

# P3-172 - Honor AccessLevelEx subtype and persistence promises

## Rule

NoSubDataTypes, atomicity, NonVolatile, and Constant have their specified meanings. Constant value changes update namespace ConfigurationVersion; constant volatile values update it at restart.

## Audit

Review accepted value types, read/write behavior, persistence tests, and required namespace metadata. See the refinement-related source tensions before extrapolating NoSubDataTypes.

## Source

- [OPC 10000-3 v1.05.06, clause 8.58](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.58)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
