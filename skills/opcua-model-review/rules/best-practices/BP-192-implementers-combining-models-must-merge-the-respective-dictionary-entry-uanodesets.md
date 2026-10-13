---
id: "BP-192"
title: "Implementers combining models must merge the respective Dictionary-Entry UANodeSets"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["9.2"]
strength: "INFORMATIVE"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/9.2"]
---

# BP-192 - Implementers combining models must merge the respective Dictionary-Entry UANodeSets

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A Server implementer using a specification (and potentially other specifications/models) that reference Dictionary Entries is responsible for merging the respective Dictionary-Entry UANodeSets into their Server  -  or, per clause 9.1, leaving those Nodes out entirely.

## Applicability

Server implementers integrating multiple Dictionary-Reference-using models.

## Exceptions and evidence limits

The "leave the Nodes out" option per clause 9.1.

## Audit

**NodeSet XML:** Not checkable against a single companion specification's own NodeSet in isolation; this is an integration-time concern for a specific deployed Server.

**Document:** N/A.

**Assessment:** Impossible without dependencies (requires the full set of models an implementer is combining) / Runtime-only in practice.

**Source wording:** Informative (responsibility statement)

**Context guard:** Informative framing does not independently establish a conformance violation.

## Source

- [OPC 11030 v1.03.03, clause 9.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/9.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
