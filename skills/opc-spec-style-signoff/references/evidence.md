# Evidence and closure

## Publication evidence

1. Discover the repository's documented build, compose, link, render and validation steps from its configuration and CI. Record the selected manuscripts and includes, manifests, Profile/CU sources, models and dependencies, `.config` or equivalent tool pins, and relevant generation inputs. Build the coordinated publication set when shared links or downloads require it, without broadening the scope of source edits.
2. In an isolated copy, record the base commit, branch, whether it includes local changes, and a manifest of hashes for inputs. Exclude stale generated publication directories. Use the repository's pinned tools and documented order to compose if required, build, resolve links and publish local HTML, Word or other scoped formats. Keep source review inputs immutable; when composition rewrites files, do that work in a separate copy and inspect its delta. Verify renders represent the edition being reviewed, not a mix of current source and old generated artifacts. Retain the artifact hashes and relevant gate results.
3. Check actual rendered table groups, descriptions, glossary, CUs and Profiles. Compare captions, references, optionality, field/argument text, formatting and facts the renderer might omit against the authoritative inputs where applicable. Inspect the Word structure for styles, cell spans and cross-references, or Word pagination if visual layout is part of the scope. Link resolution in one format does not prove it in another. When comparing Word rerenders, retain the raw hashes for provenance, but compare relationships by their type, mode and resolved target rather than by their generated IDs. Compare linked destinations and embedded payloads as well as document text and structure; a regenerated ID is not a content change, but a retargeted link is.
4. Inventory each in-scope guide, CTT catalogue and other supplement from the source links, manifest and publication configuration. If the edition promises a download, check the actual asset and resolve each link from its intended delivery location, such as the HTML site or a standalone STS package. A relative target that resolves on the hosted site is not proof that the standalone package contains it. Compare binary artifacts by bytes. For text supplements whose links are rewritten, verify the rewritten destinations and compare the remaining content with the same-snapshot source. A promised asset that is absent or stale is an open publication issue. For an intentionally standalone supplement, cite the source path and the evidence that it is not packaged; inspect the source and verify its applicable inbound and outbound references. Asset checks for that supplement are not applicable, not missing evidence. If delivery is unclear, record what would establish it instead of assuming either case.
5. If a tool reports drift, distinguish a proven renderer limitation or source-only warning from an actual publication defect. Require evidence from the current pinned tool and snapshot before requesting an exception. Pin an exception to a rule, artifact and exact occurrences; record approval and the condition for retiring it. Recheck on a tooling change.

## Source ownership and contract checks

- Trace each contract change across clause text, authored and bound tables, glossary or Profile metadata, generators and models, tests, guides and external part references. Check numbered citations as well as named anchors when headings move; a resolving link can still lead to the wrong requirement. Keep the rule at its owner and point dependencies to it.
- For a bound table, inspect the actual generator and model. A populated model description commonly overrides authored text; a fallback description may belong to the manuscript. Edit the responsible input with authorization, regenerate in isolation, and compare composed and published text. Preserve type/member identities and existing wire and browse behavior. For any approved model change use the repository's compatibility checks and the smallest exact change; do not rewrite a frozen comparison baseline.
- When a generator or one of its inputs changes, enumerate downstream generated files and embedded copies. Before freezing the edited snapshot, run the complete generation chain in dependency order and verify that a second complete pass produces no changes, or use the repository's equivalent determinism check. Include embedded payloads in the comparison. Individual schema or model checks do not prove the outputs have converged. If they keep changing, identify the drifting output and the step that rewrites it; leave publication evidence open rather than approving the last output by default.
- Compare the edited baseline with the approved ledger. Check definitions, identifiers, mappings, encodings, optionality, status layer and error precedence, failure atomicity, and other preserved guarantees where applicable. Update CTT fixtures and expected results to exercise the distinguishing condition. A case that happens to pass without exercising that condition is not evidence. Distinguish cases that do not apply from cases that could apply but lack a usable fixture.
- Run the affected local validation and publication checks. Record exact commands and outcomes in the evidence when required by the repository or requested by the user. State what an offline contract test does not prove.

## Rule coverage ledger

Start with one row per rule ID in the selected rubric, including rules with no findings. Split a row into subchecks when its evidence differs by clause, format, or generated surface. Use concrete locations and the snapshot ID; a total or a label such as "terminology partial" is not evidence.

| Rule / subcheck | Applicable scope | Edition and evidence location | Status | Finding IDs or next evidence action |
|---|---|---|---|---|
| Local caption/reference rule / authored tables | Authored table groups in the manuscript and numbered links in HTML and Word | Snapshot S; manuscript table anchors and matching render locations | Checked | Link to any findings; otherwise state what was compared |
| Same rule / generated profile tables | Profile tables produced in HTML and Word | Snapshot S; generated table numbers and referring prose | Not verifiable | Word missing: rebuild Word from S, then check targets and labels |
| Local ReferenceType rule | Custom ReferenceType declarations only | Snapshot S; entire in-scope NodeSet inventory | Not applicable | No custom ReferenceType declarations |

Use **checked** only when all required surfaces for that row were examined; it does not mean they passed. Use **not applicable** with positive evidence of why the rule or subcheck does not apply. Use **not verifiable** for any outstanding applicable check, with the exact surface, reason and next action. Structural Word inspection is not visual pagination; inspection of CTT definitions is not live CTT execution. Avoid moving scoped evidence outside the audit to obtain a passing verdict.

## Closure queue

Seed the queue from baseline findings, prior dispositions and all applicable checks that are not verifiable. On a resumed audit, reconcile the live worktree against the last verified edition before carrying evidence forward; keep intervening edits visible and do not overwrite unrelated changes. Classify each open item by its next action:

| Open item | Next action |
|---|---|
| Clear authorized fix | Apply at the owner; reconcile copies and generated dependencies. |
| Decision affecting the contract | Ask for the smallest decision, with a recommendation and deferral option. |
| Publisher or tool defect | Prove the exact artifact and occurrences; verify a source workaround or seek approval for a tool fix or narrow exception. |
| Missing evidence | Run the specific missing check, or name the prerequisite and who can provide it. |
| Fix awaiting verification | Verify source and each affected render or supplement on the new snapshot; obtain independent closure where required. |

After each edit or verification batch, update the queue. Close an item with evidence, an exact approved exception, or a supported finding that it does not apply. Record an explicit deferral separately; it remains a blocker if it affects conformance. Do not turn a partial remediation batch into a final NOT READY report while there are runnable items. If no item can advance, name each remaining blocker, its owner and the decision or evidence that would unblock it.

## Ledger shape

Use session state or a user-approved local artifact; the ledger does not need to become a repository change.

| Record | Minimum evidence |
|---|---|
| Edition | Baseline or edited snapshot ID, local changes, input inventory, tool versions, rendered artifacts and hashes |
| Coverage | Rule and surface rows, edition, exact evidence, status, finding IDs or next action |
| Finding | Stable ID, class, exact quote and location, rule, consequence, smallest correction, authoritative owner, affected surfaces |
| Disposition | User decision where needed, fix/move/merge/removal/exception/deferral, preserved guarantee and destination, scope or rationale |
| Closure | Reader, snapshot, location-by-location source and render evidence, remaining issue or closed |

Give an independent reader the selected inputs and hashes, original findings, affected surfaces, approved decisions and exact exceptions. On a recheck, enumerate the delta and report only remaining findings or new evidenced findings in changed dependencies. Any case that still lets two conforming readings yield different observable outcomes needs an explicit disposition.
