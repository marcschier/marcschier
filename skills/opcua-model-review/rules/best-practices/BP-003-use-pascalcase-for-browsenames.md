---
id: "BP-003"
title: "Use PascalCase for BrowseNames"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.2"]
---

# BP-003 - Use PascalCase for BrowseNames

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

All BrowseNames should be written in PascalCase (upper camel case): no spaces between words, each word capitalized, remaining letters lower case.

## Applicability

BrowseName strings for all NodeClasses, document-wide default.

## Exceptions and evidence limits

See BP-005 (placeholder angle-bracket characters) and the case-specific NodeClass conventions in clause 2.1.3 (BP-008-BP-017), which refine but do not contradict PascalCase.

## Audit

**NodeSet XML:** For each `UANode/@BrowseName` string part, verify it matches a PascalCase pattern (no spaces/underscored-word-separators used as the primary separator, first letter of each concatenated word capitalized). Allow explicitly documented placeholder markers (`<`, `>`).

**Document:** Scan specification prose tables listing BrowseNames for non-PascalCase entries.

**Assessment:** Static-checkable (heuristic pattern match; cannot perfectly auto-detect "word boundaries" in all cases, so borderline results are semantically reviewable).

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.1.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
