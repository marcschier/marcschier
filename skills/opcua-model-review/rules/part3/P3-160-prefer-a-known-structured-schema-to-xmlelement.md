---
id: "P3-160"
title: "Prefer a known structured schema to XmlElement"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.38"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.38"]
---

# P3-160 - Prefer a known structured schema to XmlElement

## Rule

Do not choose XmlElement when the Server knows enough about the XML content to model a Structure and its encoding.

## Audit

Review the content schema and interoperability needs; unknown or arbitrary XML content can justify XmlElement.

## Source

- [OPC 10000-3 v1.05.06, clause 8.38](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.38)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
