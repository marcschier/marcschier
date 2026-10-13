---
id: "P3-033"
title: "Honor explicit nullability restrictions"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.2"]
strength: "MUST"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2"]
---

# P3-033 - Honor explicit nullability restrictions

## Rule

When AllowNulls is false on a nullable DataVariable, the Server neither returns null nor accepts a write of null.

## Audit

Review the value contract or runtime tests. Absence of AllowNulls leaves nullable-value behavior Server-specific.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
