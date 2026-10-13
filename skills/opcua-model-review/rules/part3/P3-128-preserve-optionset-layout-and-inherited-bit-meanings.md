---
id: "P3-128"
title: "Preserve OptionSet layout and inherited bit meanings"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.40"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.40"]
---

# P3-128 - Preserve OptionSet layout and inherited bit meanings

## Rule

OptionSet subtypes do not add Structure fields or change an inherited fixed byte length. Existing bit meanings remain valid; new bits fit the allocated length.

## Audit

Compare inherited labels, explicit/implicit lengths, and field definitions. Meaning can be specialized without invalidating the original.

## Source

- [OPC 10000-3 v1.05.06, clause 8.40](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.40)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
