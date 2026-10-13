---
id: "P3-204"
title: "Keep a type and its InstanceDeclarations in one Server"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.6.4"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.6.4"]
---

# P3-204 - Keep a type and its InstanceDeclarations in one Server

## Rule

A TypeDefinitionNode and its InstanceDeclarations reside in the same Server.

## Audit

Compare actual Server identity, not namespace URIs or XML files. A real instance may still reference a remote TypeDefinitionNode.

## Source

- [OPC 10000-3 v1.05.06, clause 4.6.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.6.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
