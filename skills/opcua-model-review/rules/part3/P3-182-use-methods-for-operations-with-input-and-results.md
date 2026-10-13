---
id: "P3-182"
title: "Use Methods for operations with input and results"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["A.6"]
strength: "INFORMATIVE"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-6"]
---

# P3-182 - Use Methods for operations with input and results

## Rule

Prefer Methods over separate input/output Variables for operations, and place genuinely global Methods on the Server Object.

## Audit

Review concurrency and operation context; legacy wrappers may lack enough information to remodel existing protocols.

## Source

- [OPC 10000-3 v1.05.06, clause A.6](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-6)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
