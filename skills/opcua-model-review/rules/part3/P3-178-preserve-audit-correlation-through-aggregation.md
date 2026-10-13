---
id: "P3-178"
title: "Preserve audit correlation through aggregation"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["9.5"]
strength: "MUST"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.5"]
---

# P3-178 - Preserve audit correlation through aggregation

## Rule

An aggregating Server passes AuditEntryId through unchanged and makes the relevant AuditEvents available to subscribers.

## Audit

Review the audit contract and aggregation behavior. Optional persistence is not required merely because event delivery is required.

## Source

- [OPC 10000-3 v1.05.06, clause 9.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.5)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
