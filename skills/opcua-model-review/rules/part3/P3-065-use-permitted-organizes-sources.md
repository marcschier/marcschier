---
id: "P3-065"
title: "Use permitted Organizes sources"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["7.11"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "references"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.11"]
---

# P3-065 - Use permitted Organizes sources

## Rule

Organizes sources are Objects, ObjectTypes, or Views; targets may have any NodeClass.

## Audit

Check logical endpoints and any more restrictive custom subtype definition.

## Source

- [OPC 10000-3 v1.05.06, clause 7.11](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.11)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
