---
id: "P3-154"
title: "Keep values within their declared built-in domains"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.8", "8.9", "8.10", "8.11", "8.12", "8.13", "8.15", "8.16", "8.17", "8.18", "8.19", "8.20", "8.21", "8.22", "8.23", "8.25", "8.26", "8.27", "8.28", "8.29", "8.34", "8.35", "8.36", "8.38", "8.53", "8.54"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.8", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.9", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.10", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.11", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.12", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.13", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.15", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.16", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.17", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.18", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.19", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.20", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.21", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.22", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.23", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.25", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.26", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.27", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.28", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.29", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.34", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.35", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.36", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.38", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.53", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.54"]
---

# P3-154 - Keep values within their declared built-in domains

## Rule

Values and examples conform to the declared built-in or Simple DataType's range, representation, and units, including millisecond Duration and defined enumeration values.

## Audit

Validate literals against the cited definitions and mappings. Context-specific negative Duration sentinels are permitted where explicitly defined.

## Source

- [OPC 10000-3 v1.05.06, clause 8.8](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.8)
- [OPC 10000-3 v1.05.06, clause 8.9](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.9)
- [OPC 10000-3 v1.05.06, clause 8.10](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.10)
- [OPC 10000-3 v1.05.06, clause 8.11](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.11)
- [OPC 10000-3 v1.05.06, clause 8.12](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.12)
- [OPC 10000-3 v1.05.06, clause 8.13](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.13)
- [OPC 10000-3 v1.05.06, clause 8.15](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.15)
- [OPC 10000-3 v1.05.06, clause 8.16](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.16)
- [OPC 10000-3 v1.05.06, clause 8.17](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.17)
- [OPC 10000-3 v1.05.06, clause 8.18](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.18)
- [OPC 10000-3 v1.05.06, clause 8.19](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.19)
- [OPC 10000-3 v1.05.06, clause 8.20](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.20)
- [OPC 10000-3 v1.05.06, clause 8.21](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.21)
- [OPC 10000-3 v1.05.06, clause 8.22](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.22)
- [OPC 10000-3 v1.05.06, clause 8.23](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.23)
- [OPC 10000-3 v1.05.06, clause 8.25](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.25)
- [OPC 10000-3 v1.05.06, clause 8.26](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.26)
- [OPC 10000-3 v1.05.06, clause 8.27](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.27)
- [OPC 10000-3 v1.05.06, clause 8.28](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.28)
- [OPC 10000-3 v1.05.06, clause 8.29](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.29)
- [OPC 10000-3 v1.05.06, clause 8.34](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.34)
- [OPC 10000-3 v1.05.06, clause 8.35](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.35)
- [OPC 10000-3 v1.05.06, clause 8.36](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.36)
- [OPC 10000-3 v1.05.06, clause 8.38](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.38)
- [OPC 10000-3 v1.05.06, clause 8.53](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.53)
- [OPC 10000-3 v1.05.06, clause 8.54](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.54)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
