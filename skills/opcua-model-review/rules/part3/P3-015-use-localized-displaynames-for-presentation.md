---
id: "P3-015"
title: "Use localized DisplayNames for presentation"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.4", "5.2.5", "8.5.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.5", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.5.1"]
---

# P3-015 - Use localized DisplayNames for presentation

## Rule

Present the localized DisplayName rather than BrowseName.

## Audit

Review the presentation contract; localization need not produce multiple translations in every export.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.4)
- [OPC 10000-3 v1.05.06, clause 5.2.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.5)
- [OPC 10000-3 v1.05.06, clause 8.5.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.5.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
