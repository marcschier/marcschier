---
id: "P3-207"
title: "Honor standard Property data types and value shapes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["3.3.2", "5.3.1", "5.4", "5.5.1", "5.5.2", "5.6.2", "5.6.5", "5.7.1", "5.8.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/3.3.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3"]
---

# P3-207 - Honor standard Property data types and value shapes

## Rule

When a standard Property is provided, use its specified value DataType, scalar/array shape, and applicable parent context.

## Audit

Compare namespace-qualified standard Properties with the relevant NodeClass table, including NodeVersion, Icon, ViewVersion, argument arrays, enumeration labels, and value metadata. Optional presence does not waive the definition.

## Source

- [OPC 10000-3 v1.05.06, clause 3.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/3.3.2)
- [OPC 10000-3 v1.05.06, clause 5.3.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.1)
- [OPC 10000-3 v1.05.06, clause 5.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.4)
- [OPC 10000-3 v1.05.06, clause 5.5.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.1)
- [OPC 10000-3 v1.05.06, clause 5.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2)
- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)
- [OPC 10000-3 v1.05.06, clause 5.6.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5)
- [OPC 10000-3 v1.05.06, clause 5.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1)
- [OPC 10000-3 v1.05.06, clause 5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
