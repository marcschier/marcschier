---
id: "P3-192"
title: "Use valid HasInterface endpoints"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["7.19"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "interfaces"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.19"]
---

# P3-192 - Use valid HasInterface endpoints

## Rule

HasInterface sources are non-Interface Objects or ObjectTypes; targets are Interface ObjectTypes derived from BaseInterfaceType.

## Audit

Resolve both endpoint classes and ancestry, including custom HasInterface subtypes.

## Source

- [OPC 10000-3 v1.05.06, clause 7.19](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.19)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
