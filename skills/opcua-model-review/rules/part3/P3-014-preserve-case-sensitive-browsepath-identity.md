---
id: "P3-014"
title: "Preserve case-sensitive BrowsePath identity"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.4"]
strength: "MUST"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.4"]
---

# P3-014 - Preserve case-sensitive BrowsePath identity

## Rule

Clients compare BrowseName strings case-sensitively. A Server accepting case-insensitive requests must not depend on case alone for required name uniqueness.

## Audit

Review name comparisons and the Server's advertised matching behavior. Case-only differences are not automatically invalid in a case-sensitive Server.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
