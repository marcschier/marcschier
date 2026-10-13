---
id: "P3-119"
title: "Give each DataTypeEncoding one owner and distinct name"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.1", "5.8.3", "5.8.4", "7.14"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.14"]
---

# P3-119 - Give each DataTypeEncoding one owner and distinct name

## Rule

A DataTypeEncoding is an appropriately typed Object owned by exactly one DataType through bidirectional HasEncoding. One DataType's encoding BrowseNames are distinct.

## Audit

Check canonical edges, encoding Object type, and qualified names; do not require duplicate XML serialization of both browse directions.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.1)
- [OPC 10000-3 v1.05.06, clause 5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3)
- [OPC 10000-3 v1.05.06, clause 5.8.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.4)
- [OPC 10000-3 v1.05.06, clause 7.14](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.14)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
