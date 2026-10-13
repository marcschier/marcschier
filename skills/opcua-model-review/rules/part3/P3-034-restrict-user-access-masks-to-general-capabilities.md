---
id: "P3-034"
title: "Restrict user access masks to general capabilities"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.8", "5.6.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "values"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.8", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2"]
---

# P3-034 - Restrict user access masks to general capabilities

## Rule

UserWriteMask cannot grant an Attribute write prohibited by WriteMask; UserAccessLevel cannot grant value access beyond AccessLevel.

## Audit

Compare corresponding supplied masks. Their values do not guarantee that a later operation succeeds.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.8](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.8)
- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
