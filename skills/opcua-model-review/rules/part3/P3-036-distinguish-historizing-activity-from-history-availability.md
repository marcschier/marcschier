---
id: "P3-036"
title: "Distinguish historizing activity from history availability"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2"]
---

# P3-036 - Distinguish historizing activity from history availability

## Rule

Historizing describes current history collection, while AccessLevel history bits describe available historical access.

## Audit

Review the declared meaning of the flags; historic data may remain available after active collection stops.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
