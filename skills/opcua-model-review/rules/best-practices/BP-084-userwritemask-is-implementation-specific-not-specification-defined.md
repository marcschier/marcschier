---
id: "BP-084"
title: "UserWriteMask is implementation-specific (not specification-defined)"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.17"]
strength: "INFORMATIVE"
targets: ["document", "runtime"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes"]
---

# BP-084 - UserWriteMask is implementation-specific (not specification-defined)

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

UserWriteMask is implementation-specific and is not defined by the specification; a Server calculates it itself.

## Applicability

All NodeClasses.

## Exceptions and evidence limits

Change in Server allowed? = Yes (calculated in server).

## Audit

**NodeSet XML:** N/A (not a specification-level attribute to audit in a reference NodeSet).

**Document:** N/A.

**Assessment:** Runtime-only.

**Source wording:** Informative

**Context guard:** Informative framing does not independently establish a conformance violation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.17](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
