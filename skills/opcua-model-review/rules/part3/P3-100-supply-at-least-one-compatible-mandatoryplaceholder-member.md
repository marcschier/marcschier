---
id: "P3-100"
title: "Supply at least one compatible MandatoryPlaceholder member"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.4.4.4.5"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.5"]
---

# P3-100 - Supply at least one compatible MandatoryPlaceholder member

## Rule

An Object/Variable MandatoryPlaceholder requires at least one instance of the declared type or a subtype, linked by the original ReferenceType or a subtype.

## Audit

Match type and ReferenceType, not a fixed BrowseName. MandatoryPlaceholder does not define a TranslateBrowsePathsToNodeIds path.

## Source

- [OPC 10000-3 v1.05.06, clause 6.4.4.4.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.5)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
