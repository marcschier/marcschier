---
id: "P3-025"
title: "Expose only actual parts of complex Variable values"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.5.3", "5.6.4"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.5.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.4"]
---

# P3-025 - Expose only actual parts of complex Variable values

## Rule

A DataVariable's component DataVariables represent elements of its complex value, rather than unrelated values placed beneath a simple Variable.

## Audit

Compare child semantics with the parent's structure or aggregate definition. A scalar Structure may still be complex.

## Source

- [OPC 10000-3 v1.05.06, clause 4.5.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.5.3)
- [OPC 10000-3 v1.05.06, clause 5.6.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
