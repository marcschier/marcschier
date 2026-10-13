---
id: "BP-005"
title: "Restrict BrowseName characters for TypeDefinitions and related constructs"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.2"]
---

# BP-005 - Restrict BrowseName characters for TypeDefinitions and related constructs

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

BrowseNames of TypeDefinitions (ObjectTypes, VariableTypes, DataTypes, ReferenceTypes) and InstanceDeclarations, Structure DataType field names, EnumStrings/EnumValues of Enumerations, and Method Arguments should use only letters, digits, or underscore  -  except where angle brackets `<` and `>` are explicitly used to denote optional placeholders.

## Applicability

BrowseNames/field names/argument names of: ObjectTypes, VariableTypes, DataTypes, ReferenceTypes, InstanceDeclarations, Structure DataType fields, Enumeration EnumStrings/EnumValues, Method Arguments.

## Exceptions and evidence limits

Explicit placeholder notation using `<` and `>` (e.g., `<SomeMethod>`) is excluded from the restriction by design.

## Audit

**NodeSet XML:** Regex-check the relevant name strings for characters outside `[A-Za-z0-9_<>]`, treating `<...>` tokens as allowed placeholders.

**Document:** Scan spec prose for the same names.

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.1.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
