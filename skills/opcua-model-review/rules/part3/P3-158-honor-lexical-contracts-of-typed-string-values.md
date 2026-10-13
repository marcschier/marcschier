---
id: "P3-158"
title: "Honor lexical contracts of typed string values"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.42", "8.43", "8.44", "8.46"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.42", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.43", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.44", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.46"]
---

# P3-158 - Honor lexical contracts of typed string values

## Rule

DateString, DurationString, and TimeString follow their cited ISO 8601 lexical forms; DecimalString follows the cited XSD decimal lexical definition.

## Audit

Check the selected Simple DataType and permitted reduced precision; do not replace the normative lexical grammar with a guessed regex.

## Source

- [OPC 10000-3 v1.05.06, clause 8.42](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.42)
- [OPC 10000-3 v1.05.06, clause 8.43](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.43)
- [OPC 10000-3 v1.05.06, clause 8.44](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.44)
- [OPC 10000-3 v1.05.06, clause 8.46](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.46)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
