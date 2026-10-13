---
id: "BP-222"
title: "Deprecation may be used deliberately to limit the number of new Namespaces minted over time"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["14.3.1"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/14.3.1"]
---

# BP-222 - Deprecation may be used deliberately to limit the number of new Namespaces minted over time

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

To manage several changes over time, Companion Specifications may use the deprecation mechanism in one version when a breaking change is already foreseeable in a later version, specifically to avoid minting too many new NamespaceUris.

## Applicability

Companion Specifications anticipating multiple future changes.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Not independently mechanical (a forward-looking strategic judgement).

**Document:** Review version-planning rationale.

**Assessment:** Semantically reviewable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 14.3.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/14.3.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
