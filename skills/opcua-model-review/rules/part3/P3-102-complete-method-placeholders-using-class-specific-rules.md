---
id: "P3-102"
title: "Complete Method placeholders using class-specific rules"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.4.4.4.4", "6.4.4.4.5"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.5"]
---

# P3-102 - Complete Method placeholders using class-specific rules

## Rule

A Method placeholder fixes its BrowseName while instances/subtypes define arguments. A subtype replaces OptionalPlaceholder with Optional/Mandatory, and MandatoryPlaceholder with Mandatory.

## Audit

Separate Method placeholder behavior from Object/Variable placeholder behavior and check presence for mandatory Methods.

## Source

- [OPC 10000-3 v1.05.06, clause 6.4.4.4.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.4)
- [OPC 10000-3 v1.05.06, clause 6.4.4.4.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.5)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
