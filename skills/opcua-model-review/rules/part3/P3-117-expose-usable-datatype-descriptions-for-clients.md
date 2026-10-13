---
id: "P3-117"
title: "Expose usable DataType descriptions for clients"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.1"]
---

# P3-117 - Expose usable DataType descriptions for clients

## Rule

Expose vendor DataType Nodes and structure information where available so generic Clients can interpret values.

## Audit

Check type definitions and documentation; well-known DataTypeIds may be used without a local DataType Node.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
