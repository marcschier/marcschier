---
id: "BP-026"
title: "Companion-spec UANodeSet file name pattern"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.4"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.4"]
---

# BP-026 - Companion-spec UANodeSet file name pattern

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A Companion Specification's UANodeSet file name should be `Opc.Ua.<ShortName>.NodeSet2.xml`.

## Applicability

Companion Specification UANodeSet file deliverables.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Requires file-level metadata (the actual delivered file name), not NodeSet XML content  -  confirm the delivered file name matches the pattern.

**Document:** N/A.

**Assessment:** Static-checkable, but only given file-name metadata as an input (not derivable from NodeSet content alone)  -  borderline "impossible without dependencies" if only XML content (no filename) is supplied to a reviewer.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
