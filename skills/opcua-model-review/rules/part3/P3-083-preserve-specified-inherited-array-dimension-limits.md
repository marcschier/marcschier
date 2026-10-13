---
id: "P3-083"
title: "Preserve specified inherited array dimension limits"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.2.8"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "inheritance"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.8"]
---

# P3-083 - Preserve specified inherited array dimension limits

## Rule

ArrayDimensions may be added when absent, and an unspecified zero dimension may become specified. An existing nonzero dimension value cannot be changed.

## Audit

Compare each inherited dimension after rank checks; a smaller nonzero bound is not automatically an allowed override.

## Source

- [OPC 10000-3 v1.05.06, clause 6.2.8](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.8)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
