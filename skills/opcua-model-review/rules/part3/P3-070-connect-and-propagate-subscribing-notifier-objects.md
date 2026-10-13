---
id: "P3-070"
title: "Connect and propagate subscribing notifier Objects"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["7.18"]
strength: "MUST"
targets: ["nodeset", "document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.18"]
---

# P3-070 - Connect and propagate subscribing notifier Objects

## Rule

HasNotifier targets subscribing Objects, and Events delivered at a target are also delivered at the source.

## Audit

Check target class/EventNotifier and the runtime propagation contract.

## Source

- [OPC 10000-3 v1.05.06, clause 7.18](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.18)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
