---
id: "P3-046"
title: "Use unique Method argument names"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.7.1"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "methods"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1"]
---

# P3-046 - Use unique Method argument names

## Rule

Argument names are unique within a Method's scope.

## Audit

Inspect InputArguments and OutputArguments together, not only each array in isolation.

## Source

- [OPC 10000-3 v1.05.06, clause 5.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
