---
id: "P3-118"
title: "Apply encoding rules according to DataType kind"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.2", "5.8.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3"]
---

# P3-118 - Apply encoding rules according to DataType kind

## Rule

Only concrete Structured DataTypes expose HasEncoding. Each has a standard Default Binary or Default XML encoding; abstract, built-in, Simple, and Enumeration DataTypes do not expose encodings.

## Audit

Resolve DataType kind and abstractness before evaluating encoding presence. A nullable nested-only DefaultEncodingId is not itself a blanket exemption from HasEncoding requirements.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.2)
- [OPC 10000-3 v1.05.06, clause 5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
