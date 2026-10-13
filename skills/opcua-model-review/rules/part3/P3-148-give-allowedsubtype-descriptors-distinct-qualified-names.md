---
id: "P3-148"
title: "Give AllowedSubtype descriptors distinct qualified names"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["7.29"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.29"]
---

# P3-148 - Give AllowedSubtype descriptors distinct qualified names

## Rule

AllowedSubtype targets compatible BaseDataVariableType-derived Variables, and a single restriction does not reference two descriptor Variables with the same BrowseName.

## Audit

Compare namespace-qualified names and the applicable inherited Variable constraints.

## Source

- [OPC 10000-3 v1.05.06, clause 7.29](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.29)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
