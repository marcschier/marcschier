---
id: "BP-136"
title: "Prefer an AddIn in all other (larger/grouped) cases; both may coexist"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.6"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.6"]
---

# BP-136 - Prefer an AddIn in all other (larger/grouped) cases; both may coexist

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

In all cases other than BP-135's small/simple scenario, it is recommended to define an AddIn instead. The document also notes an Interface and an AddIn built on top of that Interface may both be defined together.

## Applicability

Composition design choice between Interface and AddIn.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Not independently mechanical beyond the inverse of BP-135's check.

**Document:** Review whether larger/grouped composed aspects use an AddIn (grouping Object with standardized `DefaultInstanceBrowseName`) rather than an unwieldy direct Interface.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD / MAY

## Source

- [OPC 11030 v1.03.03, clause 7.2.6](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.6)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
