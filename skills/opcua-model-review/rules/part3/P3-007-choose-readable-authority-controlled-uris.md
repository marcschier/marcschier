---
id: "P3-007"
title: "Choose readable authority-controlled URIs"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.2"]
---

# P3-007 - Choose readable authority-controlled URIs

## Rule

Construct identifiers under an authority you control, using the recommended tag-URI or HTTP-URL forms. Use lowercase scheme and domain components; a URL should identify an actual webpage.

## Audit

Review URI ownership, uniqueness, and intended use. The illustrative formats are recommendations, not a ban on every other RFC 3986 URI.

## Source

- [OPC 10000-3 v1.05.06, clause 4.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
