---
id: "P3-162"
title: "Keep AccessLevelEx consistent with AccessLevel"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.2", "8.58"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "values"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.58"]
---

# P3-162 - Keep AccessLevelEx consistent with AccessLevel

## Rule

AccessLevelEx contains AccessLevel in its low byte and keeps the explicitly reserved bits zero.

## Audit

Compare supplied masks and resolve profile/version applicability before demanding the extended Attribute.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)
- [OPC 10000-3 v1.05.06, clause 8.58](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.58)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
