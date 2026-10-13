---
id: "BP-118"
title: "Return an Uncertain StatusCode alongside an application-specific error"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["5.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.2"]
---

# BP-118 - Return an Uncertain StatusCode alongside an application-specific error

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If there is an application-specific error in a Method's execution, the Method should return an Uncertain StatusCode (from the Call Service's Method Result Codes) alongside the detailed reason in the status output argument.

## Applicability

Methods implementing the BP-116 pattern.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Not directly checkable from NodeSet XML (this is call-time server behavior); review would need Method-behavior test cases/documentation.

**Document:** Review the specification's description of the Method's error behavior for the Uncertain-StatusCode convention.

**Assessment:** Semantically reviewable (prose) / Runtime-only (actual call behavior).

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 5.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
