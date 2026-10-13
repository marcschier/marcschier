---
id: "BP-068"
title: "A changed signature requires a new Method with a new BrowseName"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.11"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.11"]
---

# BP-068 - A changed signature requires a new Method with a new BrowseName

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If the intention is to change a Method's signature, a new Method with the new signature and a new BrowseName shall be defined instead of modifying the existing one. A common naming practice is to append a number to the existing name (worked example: a replacement for `Refresh` would be named `Refresh2`).

## Applicability

Triggered only when a signature change is actually desired/needed.

## Exceptions and evidence limits

None stated beyond this being the sanctioned path.

## Audit

**NodeSet XML:** Confirm the old Method Node is retained unchanged (per BP-065) and a distinctly-named new Method Node was added alongside it.

**Document:** Review specification text for the new Method's naming and its stated relationship to the old one.

**Assessment:** Static-checkable (given prior version for comparison).

**Source wording:** MUST (conditional remediation)

## Source notes

The "Refresh"/"Refresh2" numbering convention is given as an example of common practice, not stated as the only acceptable naming pattern.

## Source

- [OPC 11030 v1.03.03, clause 3.2.11](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.11)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
