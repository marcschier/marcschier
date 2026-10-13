---
id: "P3-064"
title: "Expose a subtype's inverse link to its supertype"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.3.3.3", "5.5.2", "5.6.5", "5.8.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.3.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3"]
---

# P3-064 - Expose a subtype's inverse link to its supertype

## Rule

A represented subtype provides the inverse HasSubtype relationship to its supertype. The supertype need not expose the forward direction.

## Audit

Check the reconstructed model or browse behavior; XML export direction alone cannot prove a runtime omission.

## Source

- [OPC 10000-3 v1.05.06, clause 5.3.3.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.3.3)
- [OPC 10000-3 v1.05.06, clause 5.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2)
- [OPC 10000-3 v1.05.06, clause 5.6.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.5)
- [OPC 10000-3 v1.05.06, clause 5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
