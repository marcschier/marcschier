---
id: "BP-104"
title: "A Method's Executable attribute should not be fixed by the specification"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.17"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes"]
---

# BP-104 - A Method's Executable attribute should not be fixed by the specification

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A Method's Executable attribute is implementation-specific and "should not be defined" by the specification  -  i.e., specification authors should leave it to the Server/deployment to determine, rather than hard-coding a fixed value in the companion NodeSet.

## Applicability

Method Nodes, as authored in a Companion Specification's reference NodeSet.

## Exceptions and evidence limits

Change in Server allowed? = Yes.

## Audit

**NodeSet XML:** Flag a companion-specification reference NodeSet that hard-codes `Executable` to a fixed value rather than leaving it Server-determined (where the authoring tool allows distinguishing "unspecified" from an explicit value).

**Document:** N/A.

**Assessment:** Static-checkable (where tooling distinguishes unset vs. explicit), otherwise semantically reviewable.

**Source wording:** SHOULD NOT (be defined by the specification)

## Source notes

This is the one row in Table 1 phrased as a companion-spec-authoring SHOULD NOT rather than purely a description of Server runtime behavior  -  included here as a genuine actionable rule rather than folded into "informative," since it instructs specification authors on what not to fix in the reference NodeSet.

## Source

- [OPC 11030 v1.03.03, clause 3.2.17](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
