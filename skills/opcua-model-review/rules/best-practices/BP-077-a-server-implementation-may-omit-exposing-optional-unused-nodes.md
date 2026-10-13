---
id: "BP-077"
title: "A Server implementation may omit exposing optional/unused Nodes"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.16"]
strength: "MAY"
targets: ["document", "runtime"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.16"]
---

# BP-077 - A Server implementation may omit exposing optional/unused Nodes

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Servers may choose not to expose all Nodes of an Information Model if they do not use them  -  this is a distinct, narrower allowance at the level of one deployed Server's runtime AddressSpace, separate from BP-076's permanent retention requirement at the specification-definition level.

## Applicability

Deployed Server implementations (runtime AddressSpace), not the Companion Specification's own type library.

## Exceptions and evidence limits

N/A  -  this is the scope-clarifying counterpart to BP-076, not an exception that weakens it.

## Audit

**NodeSet XML:** Not applicable to a specification's reference NodeSet; only meaningful when comparing one Server's exposed AddressSpace against the full specification.

**Document:** N/A.

**Assessment:** Runtime-only (requires inspecting a live/exported Server AddressSpace against the full specification, which is "impossible without dependencies" for a specification-only review).

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source notes

Recorded specifically so a reviewer does not conflate "this Server didn't expose optional Node X" (compliant, BP-077) with "the Companion Specification's defining NodeSet is missing previously-defined Node X" (a BP-076 violation).

## Source

- [OPC 11030 v1.03.03, clause 3.2.16](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.16)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
