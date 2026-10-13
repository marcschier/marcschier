---
id: "P3-035"
title: "Mark changing semantic Properties and signal changes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.2", "8.57", "9.33.1"]
strength: "MUST"
targets: ["nodeset", "document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.57", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.33.1"]
---

# P3-035 - Mark changing semantic Properties and signal changes

## Rule

A Property whose changing value changes its parent's semantics sets SemanticChange. Supporting Servers issue the required SemanticChangeEvent and subscription status indication.

## Audit

Identify semantic Properties, their mutability, event support, and StatusCode behavior. Not every descriptive Property is semantic.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)
- [OPC 10000-3 v1.05.06, clause 8.57](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.57)
- [OPC 10000-3 v1.05.06, clause 9.33.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/9.33.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
