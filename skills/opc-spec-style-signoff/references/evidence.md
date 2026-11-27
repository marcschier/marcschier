# Evidence and closure

## Publication evidence

1. Discover the repository's documented build, compose, link, render and validation steps from its configuration and CI. Record the selected manuscripts and includes, manifests, Profile/CU sources, models and dependencies, `.config` or equivalent tool pins, and relevant generation inputs. Build the coordinated publication set when shared links or downloads require it, without broadening the scope of source edits.
2. In an isolated copy, record the base commit, branch, whether it includes local changes, and a manifest of hashes for inputs. Exclude stale generated publication directories. Use the repository's pinned tools and documented order to compose if required, build, resolve links and publish local HTML, Word or other scoped formats. Keep source review inputs immutable; when composition rewrites files, do that work in a separate copy and inspect its delta. Verify renders represent the edition being reviewed, not a mix of current source and old generated artifacts. Retain the artifact hashes and relevant gate results.
3. Check actual rendered table groups, descriptions, glossary, CUs and Profiles. Compare captions, references, optionality, field/argument text, formatting and facts the renderer might omit against the authoritative inputs where applicable. Inspect the Word structure for styles, cell spans and cross-references, or Word pagination if visual layout is part of the scope. Link resolution in one format does not prove it in another.
4. Check the packaged downloads and resolved reader links. Compare binary artifacts by bytes. For text supplements whose links are rewritten at publication, verify the rewritten destinations and compare remaining content with the same-snapshot source. A stale downloadable CTT catalogue or guide invalidates a claimed closure in that surface.
5. If a tool reports drift, distinguish a proven renderer limitation or source-only warning from an actual publication defect. Require evidence from the current pinned tool and snapshot before requesting an exception. Pin an exception to a rule, artifact and exact occurrences; record approval and the condition for retiring it. Recheck on a tooling change.

## Source ownership and contract checks

- Trace each contract change across clause text, authored and bound tables, glossary or Profile metadata, generators and models, tests, guides and external part references. Check numbered citations as well as named anchors when headings move; a resolving link can still lead to the wrong requirement. Keep the rule at its owner and point dependencies to it.
- For a bound table, inspect the actual generator and model. A populated model description commonly overrides authored text; a fallback description may belong to the manuscript. Edit the responsible input with authorization, regenerate in isolation, and compare composed and published text. Preserve type/member identities and existing wire and browse behavior. For any approved model change use the repository's compatibility checks and the smallest exact change; do not rewrite a frozen comparison baseline.
- Compare the edited baseline with the approved ledger. Check definitions, identifiers, mappings, encodings, optionality, status layer and error precedence, failure atomicity, and other preserved guarantees where applicable. Update CTT fixtures and expected results to exercise the distinguishing condition. A case that happens to pass without exercising that condition is not evidence. Distinguish cases that do not apply from cases that could apply but lack a usable fixture.
- Run the affected local validation and publication checks. Record exact commands and outcomes in the evidence when required by the repository or requested by the user. State what an offline contract test does not prove.

## Ledger shape

Use session state or a user-approved local artifact; the ledger does not need to become a repository change.

| Record | Minimum evidence |
|---|---|
| Edition | Baseline or edited snapshot ID, local changes, input inventory, tool versions, rendered artifacts and hashes |
| Coverage | Rule ID, clauses or surfaces checked, checked/not applicable/not verifiable, reason for any gap |
| Finding | Stable ID, class, exact quote and location, rule, consequence, smallest correction, authoritative owner, affected surfaces |
| Disposition | User decision where needed, fix/move/merge/removal/exception/deferral, preserved guarantee and destination, scope or rationale |
| Closure | Reader, snapshot, location-by-location source and render evidence, remaining issue or closed |

Give an independent reader the selected inputs and hashes, original findings, affected surfaces, approved decisions and exact exceptions. On a recheck, enumerate the delta and report only remaining findings or new evidenced findings in changed dependencies. Any case that still lets two conforming readings yield different observable outcomes needs an explicit disposition.
