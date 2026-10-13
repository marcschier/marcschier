---
id: "BP-210"
title: "State explicitly whether an instance-level requirement means \"at least one\" or \"all\""
spec: "OPC 11030"
version: "1.03.03"
clauses: ["12.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/12.1"]
---

# BP-210 - State explicitly whether an instance-level requirement means "at least one" or "all"

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Conformance Units may require that a TypeDefinition merely be available in the AddressSpace, or that at least one instance exists and behaves correctly, or that all instances support a given optional feature correctly  -  these are materially different requirements, and the Conformance Unit should clearly state which is meant (worked example: a Conformance Unit testing *whether* asset identification is implemented correctly, if present at all, versus one additionally requiring that *all* assets have a correctly-implemented asset identification). The document recommends splitting such requirements apart (availability-in-AddressSpace vs. existence-and-correct-behavior) rather than conflating them.

## Applicability

Conformance Unit requirement drafting for instance-level/optional features.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** N/A.

**Document:** Review Conformance Unit text for explicit at-least-one vs. all-instances phrasing.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 12.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/12.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
