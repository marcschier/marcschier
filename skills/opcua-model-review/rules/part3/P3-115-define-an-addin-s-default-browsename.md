---
id: "P3-115"
title: "Define an AddIn's default BrowseName"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.10.3", "5.5.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "addins"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2"]
---

# P3-115 - Define an AddIn's default BrowseName

## Rule

An AddIn ObjectType includes DefaultInstanceBrowseName, using the type-only Property semantics.

## Audit

Resolve the AddIn instance's ObjectType and inherited default-name definition; absent type dependencies block the check.

## Source

- [OPC 10000-3 v1.05.06, clause 4.10.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.3)
- [OPC 10000-3 v1.05.06, clause 5.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
