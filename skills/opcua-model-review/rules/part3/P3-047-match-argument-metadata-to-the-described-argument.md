---
id: "P3-047"
title: "Match argument metadata to the described argument"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.7.1", "5.7.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "methods"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.2"]
---

# P3-047 - Match argument metadata to the described argument

## Rule

HasArgumentDescription targets a Variable whose name string and DataType match its Argument, with at most one such Variable per Argument. Metadata on a Method declaration uses Mandatory.

## Audit

Ignore the BrowseName namespace only for comparison with the unqualified Argument name; preserve it for other name comparisons.

## Source

- [OPC 10000-3 v1.05.06, clause 5.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1)
- [OPC 10000-3 v1.05.06, clause 5.7.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
