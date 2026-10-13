---
id: "P3-023"
title: "Give a parent's Properties distinct qualified names"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.5.2", "5.6.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "properties"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.5.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.3"]
---

# P3-023 - Give a parent's Properties distinct qualified names

## Rule

A Node cannot reference two distinct Properties with the same namespace-qualified BrowseName.

## Audit

Group HasProperty targets by parent and resolved QualifiedName; identical name strings in different namespaces are not duplicates.

## Source

- [OPC 10000-3 v1.05.06, clause 4.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.5.2)
- [OPC 10000-3 v1.05.06, clause 5.6.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
