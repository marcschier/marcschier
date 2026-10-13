---
id: "P3-174"
title: "Couple NodeVersion updates with ModelChangeEvents"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.3.1", "5.4", "5.5.1", "5.5.2", "5.6.2", "5.6.5", "5.7.1", "5.8.3", "9.32.1", "9.32.2"]
strength: "MUST"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.2"]
---

# P3-174 - Couple NodeVersion updates with ModelChangeEvents

## Rule

Support NodeVersion and ModelChangeEvents together or neither. Structural changes update the appropriate versions/events; Variable datatype/rank/dimension changes follow their stated version rules.

## Audit

Review event/version contracts. Ordinary Attribute/value changes do not universally change NodeVersion; Nodes without NodeVersion do not trigger its coupled ModelChangeEvents.

## Source

- [OPC 10000-3 v1.05.06, clause 5.3.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.1)
- [OPC 10000-3 v1.05.06, clause 5.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.4)
- [OPC 10000-3 v1.05.06, clause 5.5.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.1)
- [OPC 10000-3 v1.05.06, clause 5.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2)
- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)
- [OPC 10000-3 v1.05.06, clause 5.6.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5)
- [OPC 10000-3 v1.05.06, clause 5.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1)
- [OPC 10000-3 v1.05.06, clause 5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3)
- [OPC 10000-3 v1.05.06, clause 9.32.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.1)
- [OPC 10000-3 v1.05.06, clause 9.32.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.32.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
