---
id: "BP-002"
title: "Companion-spec Nodes use the companion Namespace"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.1"]
---

# BP-002 - Companion-spec Nodes use the companion Namespace

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Nodes defined by a Companion Specification should use that Companion Specification's own Namespace for both their NodeIds and their BrowseNames.

## Applicability

All Nodes originated by a Companion Specification.

## Exceptions and evidence limits

None stated (this clause does not re-state the "other Namespace" exception from BP-001, but that general exception logically still applies).

## Audit

**NodeSet XML:** For each `UANode` whose `NodeId` namespace index resolves to the companion spec's own `NamespaceUris` entry, confirm its `BrowseName` namespace index resolves to the same URI.

**Document:** N/A.

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source notes

This document explicitly defers DisplayName recommendations: "Recommendations for DisplayName will be given in a later version of this document." Recorded as an acknowledged gap in the source itself, not an omission of this extraction (exact location: clause 2.1.1).

## Source

- [OPC 11030 v1.03.03, clause 2.1.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
