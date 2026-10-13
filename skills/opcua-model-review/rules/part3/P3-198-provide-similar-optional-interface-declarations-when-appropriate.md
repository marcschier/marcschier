---
id: "P3-198"
title: "Provide similar optional Interface declarations when appropriate"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.10.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2"]
---

# P3-198 - Provide similar optional Interface declarations when appropriate

## Rule

An implementing ObjectType should provide a similar declaration for each Optional Interface path, using Mandatory or Optional.

## Audit

Treat omission as advice unless an incompatible Node occupies the reserved path, which is a separate prohibition.

## Source

- [OPC 10000-3 v1.05.06, clause 4.10.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
