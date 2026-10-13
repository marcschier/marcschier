---
id: "P3-062"
title: "Use Variable targets for HasProperty"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["7.8"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "references"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.8"]
---

# P3-062 - Use Variable targets for HasProperty

## Rule

HasProperty targets a Variable; its source may be any NodeClass except a Property.

## Audit

Check ReferenceType subtypes and normalized direction, not just literal HasProperty entries.

## Source

- [OPC 10000-3 v1.05.06, clause 7.8](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.8)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
