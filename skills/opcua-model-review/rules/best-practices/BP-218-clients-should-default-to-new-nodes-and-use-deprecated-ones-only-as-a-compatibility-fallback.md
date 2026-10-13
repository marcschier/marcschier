---
id: "BP-218"
title: "Clients should default to new Nodes and use deprecated ones only as a compatibility fallback"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["14.2"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/14.2"]
---

# BP-218 - Clients should default to new Nodes and use deprecated ones only as a compatibility fallback

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

From a Client's perspective, deprecated Nodes should be avoided; the only legitimate reason to use them is compatibility with older Information Model versions. If that compatibility is required, a Client should ideally support both access paths, defaulting to the new Nodes and falling back to the deprecated ones only when the new Nodes are not available (i.e., against an older-version Server).

## Applicability

Client implementation guidance, as documented by a Companion Specification for its own consumers.

## Exceptions and evidence limits

The explicit compatibility-fallback exception.

## Audit

**NodeSet XML:** N/A (Client-behavior guidance, not a NodeSet structural property).

**Document:** Review whether the specification documents this dual-path Client guidance where it marks Nodes deprecated.

**Assessment:** Semantically reviewable (documentation); actual behavior is Runtime-only.

**Source wording:** SHOULD NOT (use deprecated Nodes by default) / SHOULD (prefer new Nodes, fall back only when needed)

## Source notes

This describes Client application behavior rather than Information Model structure; retained because a Companion Specification is expected to document this guidance alongside any deprecation it introduces.

## Source

- [OPC 11030 v1.03.03, clause 14.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/14.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
