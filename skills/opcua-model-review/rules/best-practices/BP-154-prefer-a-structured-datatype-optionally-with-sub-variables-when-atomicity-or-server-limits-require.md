---
id: "BP-154"
title: "Prefer a Structured DataType (optionally with sub-variables) when atomicity or server limits require it"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.5.7", "7.5.3", "7.5.4"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.7", "https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.3", "https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.4"]
---

# BP-154 - Prefer a Structured DataType (optionally with sub-variables) when atomicity or server limits require it

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If a transactional/atomic context is needed, or the Client should be able to retrieve a large amount of data at once rather than subscribing to many individual Variables, the third approach (one Variable of a Structured DataType, combined with individual sub-variables for the decomposed parts, clause 7.5.4) is recommended. If, instead, the Server itself cannot interpret/decompose the underlying structured data, or the data is conceptually always accessed as one transaction from an application perspective, the second approach (just one Variable of a Structured DataType, clause 7.5.3, with no sub-variables) should be used.

## Applicability

Structured-data modelling decisions where atomicity, server-side interpretability, or bulk access matter.

## Exceptions and evidence limits

See BP-153 for the no-atomicity-needed counter-case.

## Audit

**NodeSet XML:** Not independently mechanical.

**Document:** Review rationale for the chosen granularity approach against the stated atomicity/interpretability drivers.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source notes

The document also notes (clause 7.9) a Structure field limit of 32 optional fields, relevant if this approach is chosen (cross-ref BP-172).

## Source

- [OPC 11030 v1.03.03, clause 7.5.7](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.7)
- [OPC 11030 v1.03.03, clause 7.5.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.3)
- [OPC 11030 v1.03.03, clause 7.5.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
