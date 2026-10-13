---
id: "BP-030"
title: "Method Argument names must be unique"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.6"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.6"]
---

# BP-030 - Method Argument names must be unique

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Each Argument (input or output) of a Method must have a unique name.

## Applicability

Method `InputArguments`/`OutputArguments` definitions.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Within one Method's `InputArguments` Property and within its `OutputArguments` Property, flag duplicate `Argument/Name` values (checked separately per argument list, since the clause does not state cross-list uniqueness).

**Document:** Review spec Method argument tables for duplicate names.

**Assessment:** Static-checkable.

**Source wording:** MUST

## Source

- [OPC 11030 v1.03.03, clause 2.6](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.6)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
