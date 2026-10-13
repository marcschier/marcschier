---
id: "P3-175"
title: "Report ModelChangeEvents in their View context"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["9.32.3", "9.32.5", "9.32.6"]
strength: "MUST"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.5", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.6"]
---

# P3-175 - Report ModelChangeEvents in their View context

## Rule

Report model changes through the affected View or the Server's default View, update supplied ViewVersion, and preserve the selected event's defined affected-Node/type information.

## Audit

Review affected Views, notifier selection, and event fields. One change can legitimately produce events in several View contexts.

## Source

- [OPC 10000-3 v1.05.06, clause 9.32.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.3)
- [OPC 10000-3 v1.05.06, clause 9.32.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.5)
- [OPC 10000-3 v1.05.06, clause 9.32.6](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.6)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
