---
id: "P3-044"
title: "Do not grant UserExecutable when Executable is false"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.7.1"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "methods"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1"]
---

# P3-044 - Do not grant UserExecutable when Executable is false

## Rule

If Executable is false, UserExecutable is also false. User-specific permission may further restrict execution.

## Audit

Compare supplied values or effective XML defaults; a true flag is not a guarantee against later access denial.

## Source

- [OPC 10000-3 v1.05.06, clause 5.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
