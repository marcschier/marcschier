---
id: "BP-004"
title: "Keep acronyms/abbreviations in PascalCase, not all-caps"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.2"]
---

# BP-004 - Keep acronyms/abbreviations in PascalCase, not all-caps

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When a BrowseName incorporates an acronym or abbreviation, that acronym should still follow PascalCase rather than being written in all capitals (worked examples given: `PortMacAddress`, not `PortMACAddress`; `NodeId`; `UInt32`).

## Applicability

Any BrowseName containing an acronym/abbreviation.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Flag BrowseNames containing runs of 2+ consecutive upper-case letters that are not immediately followed by end-of-string or a recognized initialism boundary (heuristic only).

**Document:** Review spec prose naming tables for all-caps acronym segments.

**Assessment:** Semantically reviewable (acronym detection is heuristic; false positives likely for legitimate short all-caps tokens like `ID`-as-whole-word is itself the counter-example `NodeId`  -  illustrates this needs human judgement).

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.1.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
