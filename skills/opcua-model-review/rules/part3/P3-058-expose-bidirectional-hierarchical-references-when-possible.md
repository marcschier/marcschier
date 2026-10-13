---
id: "P3-058"
title: "Expose bidirectional hierarchical References when possible"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.3.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.2"]
---

# P3-058 - Expose bidirectional hierarchical References when possible

## Rule

Prefer both browse directions for hierarchical References to keep the hierarchy connected.

## Audit

Check runtime browse availability. NodeSet XML may serialize only one direction of a logical edge; do not require mirrored XML entries.

## Source

- [OPC 10000-3 v1.05.06, clause 5.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.3.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
