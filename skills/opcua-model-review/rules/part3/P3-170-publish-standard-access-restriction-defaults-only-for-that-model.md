---
id: "P3-170"
title: "Publish standard access restriction defaults only for that model"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.11"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.11"]
---

# P3-170 - Publish standard access restriction defaults only for that model

## Rule

Use NamespaceMetadata DefaultAccessRestrictions and Node overrides consistently for standard access-restriction support; a vendor-specific restriction model does not publish that standard default.

## Audit

Check namespace metadata together with the declared access model; missing XML data may reflect an incomplete export.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.11](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.11)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
