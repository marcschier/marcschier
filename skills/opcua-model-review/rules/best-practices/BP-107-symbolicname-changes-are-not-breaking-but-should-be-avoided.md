---
id: "BP-107"
title: "SymbolicName changes are not breaking but should be avoided"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.17"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes"]
---

# BP-107 - SymbolicName changes are not breaking but should be avoided

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

SymbolicName is not an OPC UA Attribute but can be defined in a UANodeSet. Changing it is not considered a breaking change; however, it should be avoided because it may affect code generation. Implementers may change the SymbolicName before using a standardized UANodeSet, without violating the specification.

## Applicability

Any Node carrying a `SymbolicName` in a UANodeSet.

## Exceptions and evidence limits

Pre-use adaptation by implementers is explicitly permitted.

## Audit

**NodeSet XML:** Diff `SymbolicName` values across versions/forks; flag changes for review (not an automatic failure).

**Document:** N/A.

**Assessment:** Static-checkable (detecting the change); impact ("did this break code generation downstream") is impossible without dependencies (requires knowledge of downstream consumers).

**Source wording:** SHOULD NOT (change casually) / MAY (change when adapting a UANodeSet before use)

## Source

- [OPC 11030 v1.03.03, clause 3.2.17](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
