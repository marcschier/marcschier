---
id: "P3-206"
title: "Make type definitions available to generic Clients"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.6.1"]
strength: "MUST"
targets: ["nodeset", "document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.6.1"]
---

# P3-206 - Make type definitions available to generic Clients

## Rule

Provide the type definitions needed by generic Clients even when specialized Clients recognize well-known type NodeIds. Those definitions may be available in another Server.

## Audit

Check type information availability without requiring every well-known type to be duplicated locally; a lone NodeSet cannot prove a remote Server's availability.

## Source

- [OPC 10000-3 v1.05.06, clause 4.6.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.6.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
