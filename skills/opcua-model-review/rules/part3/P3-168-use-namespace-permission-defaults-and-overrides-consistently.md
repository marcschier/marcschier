---
id: "P3-168"
title: "Use namespace permission defaults and overrides consistently"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.9"]
strength: "MUST"
targets: ["nodeset", "document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.9"]
---

# P3-168 - Use namespace permission defaults and overrides consistently

## Rule

Standard namespace permission support supplies the required defaults and Node overrides, protects administrative metadata, and represents cleared overrides as specified. Vendor-specific models do not publish misleading standard default Properties.

## Audit

Review DefaultRolePermissions/DefaultUserRolePermissions, readability/writability, empty arrays, and preservation of written permission bits.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.9](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.9)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
