---
id: "P3-201"
title: "Respect the maximum transferred array element count"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.2", "8.6", "8.51"]
strength: "MUST"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.6", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51"]
---

# P3-201 - Respect the maximum transferred array element count

## Rule

An array transferred on the wire contains no more than 2,147,483,647 elements, regardless of dimension count.

## Audit

Check actual transfer contracts. Do not reject a larger advertised storage/dimension bound solely by proxy when supported partial transfers remain possible.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.2)
- [OPC 10000-3 v1.05.06, clause 8.6](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.6)
- [OPC 10000-3 v1.05.06, clause 8.51](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
