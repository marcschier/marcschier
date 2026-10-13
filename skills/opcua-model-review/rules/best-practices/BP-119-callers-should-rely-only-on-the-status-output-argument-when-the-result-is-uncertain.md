---
id: "BP-119"
title: "Callers should rely only on the status output argument when the result is Uncertain"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["5.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.2"]
---

# BP-119 - Callers should rely only on the status output argument when the result is Uncertain

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When the Method's StatusCode is Uncertain per BP-118, the application calling the Method shall only consider the Status output argument (not other output arguments) for the application-specific error detail.

## Applicability

Client-side consumoption of Methods implementing the BP-116/BP-118 pattern.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** N/A (client behavioral requirement, not a NodeSet structural property).

**Document:** Review whether the specification correctly instructs implementers/Client-developers of this consumption rule.

**Assessment:** Semantically reviewable (specification prose only); the actual behavior is Runtime-only.

**Source wording:** MUST (source wording: "shall only consider")

## Source notes

This rule describes Client application behavior, not Information Model structure; retained because it is part of the documented contract a Companion Specification should state when adopting the pattern.

## Source

- [OPC 11030 v1.03.03, clause 5.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
