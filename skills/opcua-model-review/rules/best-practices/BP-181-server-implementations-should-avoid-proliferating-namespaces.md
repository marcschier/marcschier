---
id: "BP-181"
title: "Server implementations should avoid proliferating Namespaces"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.13"]
strength: "SHOULD"
targets: ["document", "runtime"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.13"]
---

# BP-181 - Server implementations should avoid proliferating Namespaces

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A Server must uniquely identify its Nodes using a NodeId's Namespace(Index) and Identifier parts together; either part can contribute to uniqueness. As a general guideline, since managing a Namespace is more expensive than managing an identifier within an existing Namespace, Server implementations should avoid creating many (hundreds of) Namespaces and instead manage many Nodes within fewer Namespaces.

## Applicability

Server implementation engineering (runtime NamespaceArray design), not a Companion Specification's own single NamespaceUri.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** N/A for a single Companion Specification's reference NodeSet (which defines one Namespace); meaningful only when reviewing a deployed Server's full NamespaceArray.

**Document:** N/A.

**Assessment:** Runtime-only (concerns a deployed Server's own namespace-management engineering, not a companion-spec NodeSet's content).

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.13](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.13)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
