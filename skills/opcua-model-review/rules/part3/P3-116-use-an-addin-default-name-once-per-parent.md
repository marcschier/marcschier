---
id: "P3-116"
title: "Use an AddIn default name once per parent"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.10.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.3"]
---

# P3-116 - Use an AddIn default name once per parent

## Rule

Only one of several AddIn instances under the same parent can use the AddIn's default BrowseName.

## Audit

Compare actual qualified BrowseNames with the default QualifiedName value. Use of the default by an individual instance is recommended, not universally required.

## Source

- [OPC 10000-3 v1.05.06, clause 4.10.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
