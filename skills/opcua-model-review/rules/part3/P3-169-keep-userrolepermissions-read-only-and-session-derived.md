---
id: "P3-169"
title: "Keep UserRolePermissions read-only and Session-derived"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.10"]
strength: "MUST"
targets: ["nodeset", "document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.10"]
---

# P3-169 - Keep UserRolePermissions read-only and Session-derived

## Rule

UserRolePermissions is not writable, reflects Roles granted to the current Session, and uses the stated namespace fallback when no Node-specific value exists.

## Audit

Review the permission contract and effective Attribute write permissions.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.10](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.10)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
