---
id: "BP-139"
title: "Do not use \"Mandatory-but-returns-Bad-status\" as a substitute for Optional"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.7"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.7"]
---

# BP-139 - Do not use "Mandatory-but-returns-Bad-status" as a substitute for Optional

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The document notes it would be technically possible to have Mandatory Variables/Methods that simply return a Bad status code when unsupported, as an alternative to making them Optional  -  but explicitly states this approach is not recommended.

## Applicability

ObjectType/VariableType member design.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Not mechanically checkable from structure alone (requires behavioral documentation of "always returns Bad"); a documented pattern of this kind in specification text is the detectable signal.

**Document:** Review specification text for Mandatory members documented as routinely returning Bad status when unsupported.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD NOT

## Source

- [OPC 11030 v1.03.03, clause 7.2.7](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.7)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
