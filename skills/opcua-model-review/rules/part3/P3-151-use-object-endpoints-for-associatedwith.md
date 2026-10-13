---
id: "P3-151"
title: "Use Object endpoints for AssociatedWith"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["7.23"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.23"]
---

# P3-151 - Use Object endpoints for AssociatedWith

## Rule

AssociatedWith connects Objects, is symmetric, and has no InverseName.

## Audit

Check logical endpoints and inherited symmetry requirements.

## Source

- [OPC 10000-3 v1.05.06, clause 7.23](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.23)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
