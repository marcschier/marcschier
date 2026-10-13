---
id: "P3-094"
title: "Instantiate Mandatory declarations on existing paths"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.4.4.4.1", "6.4.4.4.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "inheritance"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.2"]
---

# P3-094 - Instantiate Mandatory declarations on existing paths

## Rule

For each existing parent BrowsePath, a Mandatory declaration has a similar Node in the instance.

## Audit

Inspect the fully inherited hierarchy recursively. A Mandatory child beneath an absent Optional parent is not required until that parent exists.

## Source

- [OPC 10000-3 v1.05.06, clause 6.4.4.4.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.1)
- [OPC 10000-3 v1.05.06, clause 6.4.4.4.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
