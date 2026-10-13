---
id: "BP-122"
title: "Only define a new ObjectType when reuse is expected"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.1"]
---

# BP-122 - Only define a new ObjectType when reuse is expected

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Defining an ObjectType makes sense when it is expected to be used several times, either within one Server or across Servers for interoperability. An ObjectType may be simple (no substructure, e.g. the base `FolderType`) or define a substructure of Objects/Variables/Methods.

## Applicability

New ObjectType design decisions.

## Exceptions and evidence limits

None stated; this is forward-looking design judgement, not a retrofit check.

## Audit

**NodeSet XML:** Weakly checkable: an ObjectType with exactly one instantiation anywhere in a given corpus is a *candidate* signal, but "expected reuse" is an intent, not an observable fact, and the corpus needed is external to one NodeSet.

**Document:** Review specification rationale for introducing a new ObjectType.

**Assessment:** Semantically reviewable; the "actual observed reuse" signal is impossible without dependencies (requires a corpus of consuming models).

**Source wording:** SHOULD (heuristic)

## Source

- [OPC 11030 v1.03.03, clause 7.2.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
