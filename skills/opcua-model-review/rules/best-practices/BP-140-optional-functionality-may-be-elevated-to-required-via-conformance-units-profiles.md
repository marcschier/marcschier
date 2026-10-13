---
id: "BP-140"
title: "Optional functionality may be elevated to required via Conformance Units/Profiles"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.7"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.7"]
---

# BP-140 - Optional functionality may be elevated to required via Conformance Units/Profiles

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Optional functionality can be made mandatory at the Server-conformance level via Conformance Units and Profiles (cross-ref clause 3.3), without changing the type's own ModellingRule. A Server implementation then decides which Conformance Units/Profiles it supports, and Clients can discover a Server's supported set via the OPC UA interface.

## Applicability

Conformance/certification layer, distinct from the type definition itself.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Not a NodeSet-structural check; requires cross-referencing Conformance Unit/Profile definitions against the type's ModellingRules.

**Document:** Review Conformance Unit/Profile definitions for elevation of Optional members to required.

**Assessment:** Semantically reviewable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 7.2.7](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.7)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
