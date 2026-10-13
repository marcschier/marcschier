---
id: "P3-067"
title: "Return ordered components in a stable order"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["7.9"]
strength: "MUST"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.9"]
---

# P3-067 - Return ordered components in a stable order

## Rule

HasOrderedComponent browse results use a well-defined, consistent Server-specific order.

## Audit

Review the documented ordering or repeated runtime Browse results; ordinary XML element order does not establish service behavior.

## Source

- [OPC 10000-3 v1.05.06, clause 7.9](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.9)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
