---
id: "P3-006"
title: "Compare namespace URIs as opaque case-sensitive strings"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.2", "8.2.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.2.2"]
---

# P3-006 - Compare namespace URIs as opaque case-sensitive strings

## Rule

Use exact, case-sensitive URI equality. Do not merge namespaces by lowercasing, URL decoding, or otherwise rewriting their URIs.

## Audit

Inspect namespace resolution in the model and its implementation contract. Different namespace-table indexes across files do not imply different namespaces.

## Source

- [OPC 10000-3 v1.05.06, clause 4.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.2)
- [OPC 10000-3 v1.05.06, clause 8.2.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.2.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
