---
id: "BP-019"
title: "Avoid reusing BrowseName strings across Namespaces"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.4"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.4"]
---

# BP-019 - Avoid reusing BrowseName strings across Namespaces

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Because OPC UA Clients typically display only the string part of a BrowseName (not its NamespaceIndex), it is desirable to avoid reusing the same Name string across different Namespaces  -  in particular, to avoid reusing names from the base OPC UA specification  -  "as much as possible."

## Applicability

Any Companion Specification or vendor model choosing BrowseName strings.

## Exceptions and evidence limits

The source itself states this "cannot be guaranteed" given the number of independent Companion Specifications  -  this is an explicitly best-effort, not absolute, recommendation.

## Audit

**NodeSet XML:** Cross-NodeSet name-collision scan (requires access to other Namespaces' NodeSets  -  see Assessment).

**Document:** None specific.

**Assessment:** Impossible without dependencies for a single NodeSet in isolation (requires a corpus of other Namespaces' BrowseNames to detect collisions); otherwise semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.1.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
