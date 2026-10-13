---
id: "BP-086"
title: "UserRolePermissions is implementation-specific"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.17"]
strength: "INFORMATIVE"
targets: ["document", "runtime"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes"]
---

# BP-086 - UserRolePermissions is implementation-specific

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

UserRolePermissions is implementation-specific, not defined by the specification, and is calculated by the Server.

## Applicability

All NodeClasses.

## Exceptions and evidence limits

Change in Server allowed? = Yes (calculated in server).

## Audit

**NodeSet XML:** N/A.

**Document:** N/A.

**Assessment:** Runtime-only.

**Source wording:** Informative

**Context guard:** Informative framing does not independently establish a conformance violation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.17](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
