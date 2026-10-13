---
id: "P3-084"
title: "Evaluate the fully inherited declaration hierarchy"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.3.3.1", "6.3.3.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "inheritance"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.2"]
---

# P3-084 - Evaluate the fully inherited declaration hierarchy

## Rule

Combine a type's declarations and inherited declarations recursively. A subtype need not repeat References to unchanged inherited declarations.

## Audit

Merge by namespace-qualified BrowsePath, including relevant inherited References. Missing supertype definitions block a complete instantiation review.

## Source

- [OPC 10000-3 v1.05.06, clause 6.3.3.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.1)
- [OPC 10000-3 v1.05.06, clause 6.3.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
