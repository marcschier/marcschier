---
id: "P3-020"
title: "Separate Property and DataVariable relationships"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.3", "5.6.4"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "properties"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.4"]
---

# P3-020 - Separate Property and DataVariable relationships

## Rule

A Property is the target of at least one HasProperty and not of HasComponent. A DataVariable has at least one permitted HasComponent parent and no HasProperty parent.

## Audit

Include subtypes of the relevant ReferenceTypes and References serialized on either endpoint.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.3)
- [OPC 10000-3 v1.05.06, clause 5.6.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
