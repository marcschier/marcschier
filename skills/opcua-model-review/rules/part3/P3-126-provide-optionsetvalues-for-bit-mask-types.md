---
id: "P3-126"
title: "Provide OptionSetValues for bit-mask types"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.2", "5.8.3", "8.40"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.40"]
---

# P3-126 - Provide OptionSetValues for bit-mask types

## Rule

OptionSet types and UInteger bit masks provide OptionSetValues labels, with null text for undefined bits.

## Audit

Establish bit-mask semantics first; an arbitrary UInteger subtype is not automatically an OptionSet.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.2)
- [OPC 10000-3 v1.05.06, clause 5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3)
- [OPC 10000-3 v1.05.06, clause 8.40](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.40)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
