---
id: "BP-027"
title: "Vendor-specific UANodeSet file name pattern"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.4"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.4"]
---

# BP-027 - Vendor-specific UANodeSet file name pattern

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A vendor-specific UANodeSet's file name should end with "NodeSet2.xml".

## Applicability

Vendor-specific UANodeSet file deliverables.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Same caveat as BP-026  -  requires filename metadata.

**Document:** N/A.

**Assessment:** Static-checkable given filename metadata.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
