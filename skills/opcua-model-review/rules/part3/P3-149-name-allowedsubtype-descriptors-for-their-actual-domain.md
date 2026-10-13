---
id: "P3-149"
title: "Name AllowedSubtype descriptors for their actual domain"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["7.29"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.29"]
---

# P3-149 - Name AllowedSubtype descriptors for their actual domain

## Rule

Descriptor names describe the permitted DataType and rank; do not borrow the DataType's namespace unless the descriptor is defined in that namespace.

## Audit

Review readability and namespace authority separately from NodeId identity.

## Source

- [OPC 10000-3 v1.05.06, clause 7.29](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.29)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
