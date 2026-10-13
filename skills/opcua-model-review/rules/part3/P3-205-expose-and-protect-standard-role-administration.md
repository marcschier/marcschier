---
id: "P3-205"
title: "Expose and protect standard Role administration"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.9.1"]
strength: "MUST"
targets: ["nodeset", "document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.9.1"]
---

# P3-205 - Expose and protect standard Role administration

## Rule

Publish supported standard Roles as RoleSet components and restrict Role addition, deletion, and modification to appropriately authorized callers.

## Audit

Review the AddressSpace and administrative permission contract separately from the recommended choice of base Roles.

## Source

- [OPC 10000-3 v1.05.06, clause 4.9.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.9.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
