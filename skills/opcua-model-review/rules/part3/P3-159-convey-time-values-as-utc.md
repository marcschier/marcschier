---
id: "P3-159"
title: "Convey time values as UTC"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.37"]
strength: "MUST"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.37"]
---

# P3-159 - Convey time values as UTC

## Rule

Time values exchanged between Clients and Servers are UTC; local presentation conversions belong to the Client.

## Audit

Review timestamps and declared contracts. SourceTimestamp and ServerTimestamp need not originate from synchronized clocks.

## Source

- [OPC 10000-3 v1.05.06, clause 8.37](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.37)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
