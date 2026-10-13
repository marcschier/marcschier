---
id: "P3-161"
title: "Apply PermissionType bits to their defined operations"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.9.3", "8.55"]
strength: "MUST"
targets: ["nodeset", "document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.9.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.55"]
---

# P3-161 - Apply PermissionType bits to their defined operations

## Rule

Permission bits retain their specified NodeClass and operation meanings; Call requires permission on the context and Method, and receiving Events requires permission on EventType and SourceNode.

## Audit

Review the authorization contract and reserved-bit handling. Node metadata alone does not prove access enforcement.

## Source

- [OPC 10000-3 v1.05.06, clause 4.9.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.9.3)
- [OPC 10000-3 v1.05.06, clause 8.55](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.55)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
