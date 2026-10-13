---
id: "P3-200"
title: "Limit DisplayName text to 512 characters"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.5"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "identity"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.5"]
---

# P3-200 - Limit DisplayName text to 512 characters

## Rule

Each localized DisplayName text is no longer than 512 characters.

## Audit

Count decoded text characters for each supplied translation, rather than XML bytes or the locale identifier.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.5)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
