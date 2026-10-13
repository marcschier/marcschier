---
id: "P3-037"
title: "Keep DefaultInstanceBrowseName on the ObjectType"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.5.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "addins"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2"]
---

# P3-037 - Keep DefaultInstanceBrowseName on the ObjectType

## Rule

DefaultInstanceBrowseName is a type-level Property without a ModellingRule, not a child declaration to copy onto instances.

## Audit

Inspect the Property's parent and outgoing HasModellingRule. A type-level Property without a ModellingRule is valid.

## Source

- [OPC 10000-3 v1.05.06, clause 5.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
