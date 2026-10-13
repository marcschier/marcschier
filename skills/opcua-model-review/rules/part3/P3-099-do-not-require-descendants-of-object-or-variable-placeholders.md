---
id: "P3-099"
title: "Do not require descendants of Object or Variable placeholders"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.4.4.4.4", "6.4.4.4.5"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.5"]
---

# P3-099 - Do not require descendants of Object or Variable placeholders

## Rule

For Object/Variable placeholders, nested declaration Nodes are not independently instantiated by the placeholder rule. OptionalPlaceholder imposes no extra instance-presence requirement.

## Audit

Avoid treating a placeholder as a fixed-name Mandatory subtree. Validate actual supplied members against their own type contracts.

## Source

- [OPC 10000-3 v1.05.06, clause 6.4.4.4.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.4)
- [OPC 10000-3 v1.05.06, clause 6.4.4.4.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.5)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
