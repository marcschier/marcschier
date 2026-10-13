---
id: "P3-072"
title: "Honor AlwaysGeneratesEvent on successful Method calls"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.7.1", "7.16"]
strength: "MUST"
targets: ["nodeset", "document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.16"]
---

# P3-072 - Honor AlwaysGeneratesEvent on successful Method calls

## Rule

AlwaysGeneratesEvent is used for a Method declaration and identifies an EventType whose Event is produced for every successful call.

## Audit

Check structural endpoints and the per-call behavior contract; do not apply it as an ObjectType-wide promise.

## Source

- [OPC 10000-3 v1.05.06, clause 5.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1)
- [OPC 10000-3 v1.05.06, clause 7.16](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.16)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
