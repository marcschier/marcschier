# OPC UA Model Review

An installable skill and numbered rule library for reviewing OPC UA companion
NodeSets and specification documents.

The library contains **434 named rule documents**: 207 from OPC 10000-3
v1.05.06, 226 from OPC 11030 v1.03.03, and one explicitly sourced Part 5 rule
for the prohibition on subtyping PropertyType. Each document records the rule,
scope, audit procedure, strength, and versioned clause citations.

Start with the [rule index](rules/README.md), [source coverage](rules/COVERAGE.md),
and [source notes](rules/SOURCE-NOTES.md). The documents are original summaries,
not replacements for the standards.

## Install

```powershell
copilot plugin marketplace add marcschier/marcschier
copilot plugin install opcua-model-review@marcschier
```

Or register the skill from a local clone:

```powershell
copilot skill add .\skills\opcua-model-review
```

Use `/skills reload` in a running session, or update an installed copy with
`copilot plugin update opcua-model-review`.

## Use

```text
Check Model.NodeSet2.xml against all OPC UA modelling rules.
Use Opc.Ua.NodeSet2.xml and Opc.Ua.Di.NodeSet2.xml as dependencies.

Review this companion specification:
https://reference.opcfoundation.org/specs/<specification>/full
Report every evidenced violation and include the complete rule ledger.

Audit docs\Model.md and the matching NodeSet. Identify document/XML disagreements.

Compare the old and new releases for modelling backward compatibility.
Do not merge the old release as a dependency of the new one.
```

The default audit is read-only. It distinguishes normative violations, advisory
deviations, and checks that need missing information. OPC 11030 describes itself
as a non-mandatory whitepaper; its guidance is not silently promoted into a
normative standard.

## Offline static checks

Python 3.10+ is needed only for the bundled structural checker. No external
Python packages, network connection, or OPC UA server are required.

```powershell
python .\skills\opcua-model-review\scripts\check_nodeset.py .\Model.NodeSet2.xml `
  --dependency .\Opc.Ua.NodeSet2.xml `
  --dependency .\Opc.Ua.Di.NodeSet2.xml `
  --output .\model-static-review.json
```

Repeat `--dependency` for each dependency. Add `--format markdown` for a Markdown
report. Namespace tables and aliases are resolved per input file; mirrored
References are normalized into logical edges.

The script finds static candidates and creates a complete rule ledger. It does
**not** finish the semantic audit or claim compliance: the skill must read the
rules and complete the contextual assessment. Bundled standard metadata contains
type facts only, not inherited standard member declarations; supply the full
matching standard NodeSet for that evidence.

| Exit | Meaning |
|---|---|
| `1` | Candidate violations/advisories were found |
| `2` | Input or configuration could not be interpreted |
| `3` | No static candidates, but the rule audit remains incomplete |

DTD/entity-bearing XML is rejected. The checker does not perform complete XSD
validation, runtime checks, general prose analysis, or automatic version-diff
analysis. Inaccessible dependencies and undecidable contexts remain explicit.

## Development

```powershell
python -m unittest discover -s .\skills\opcua-model-review\tests -p "test_*.py"
```

The regressions cover positive models as well as violations, including
namespace remapping, Interface and AddIn rules, declaration versus instance
behavior, PropertyType, mandatory/optional inheritance, array restrictions,
reference identity and cycles, Method metadata, and XML input safety.
