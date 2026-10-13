---
id: "P3-167"
title: "Assign and combine Roles according to authentication and permissions"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.9.1", "4.9.3"]
strength: "MUST"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.9.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.9.3"]
---

# P3-167 - Assign and combine Roles according to authentication and permissions

## Rule

Assign Anonymous, AuthenticatedUser, and TrustedApplication under their specified conditions; combine applicable Role permissions and reject operations lacking permission.

## Audit

Review user/application/endpoint mappings and credential proof. Endpoint-only mappings need the stated network protection recommendation.

## Source

- [OPC 10000-3 v1.05.06, clause 4.9.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.9.1)
- [OPC 10000-3 v1.05.06, clause 4.9.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.9.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
