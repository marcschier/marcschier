---
id: "BP-191"
title: "Package referenced Dictionary Entries as a separate, flat UANodeSet"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["9.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/9.2"]
---

# BP-191 - Package referenced Dictionary Entries as a separate, flat UANodeSet

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Companion Specifications (worked example: PA-DIM) that reference specific Dictionary Entries should create an individual UANodeSet containing those Dictionary Entries as a flat list (as PA-DIM does) and reference it from their own UANodeSet  -  rather than, say, embedding them inline or expecting a complete, ready-made UANodeSet to already exist for the external dictionary (which may not exist, and would be unnecessarily large if it tried to cover the whole dictionary).

## Applicability

Companion Specifications using Dictionary References (OPC 10000-19).

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Confirm Dictionary Entry Nodes referenced by the companion UANodeSet live in a separate, dedicated UANodeSet file rather than being embedded in the main companion UANodeSet.

**Document:** Review the specification's packaging of Dictionary Entry Nodes.

**Assessment:** Static-checkable (given both files).

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 9.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/9.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
