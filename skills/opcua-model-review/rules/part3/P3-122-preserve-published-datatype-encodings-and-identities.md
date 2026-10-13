---
id: "P3-122"
title: "Preserve published DataType encodings and identities"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.4"]
strength: "MUST NOT"
targets: ["nodeset", "document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.4"]
---

# P3-122 - Preserve published DataType encodings and identities

## Rule

Do not change a DataTypeDefinition already provided to Clients. An encoding change requires a new DataType NodeId and new DataTypeEncoding NodeIds.

## Audit

Compare published versions or cached-client contracts. Reordering or adding fields can alter encoding even when names remain unchanged.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
