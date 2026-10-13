---
id: "P3-152"
title: "Identify the model version when marking deprecation"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["7.21"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.21"]
---

# P3-152 - Identify the model version when marking deprecation

## Rule

IsDeprecated targets an Object representing the information-model version where the source Node was first deprecated.

## Audit

Check target class and version meaning; helpful DisplayName/Description text is recommended.

## Source

- [OPC 10000-3 v1.05.06, clause 7.21](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.21)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
