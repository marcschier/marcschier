---
name: opc-spec-style-signoff
license: MIT
description: >
  Run an explicitly requested OPC specification style sign-off against the
  repository's own rubric. Use for a frozen-edition sign-off audit, for applying
  or verifying findings from that audit, or when assigned this workflow in a
  delegated session. An audit request alone does not authorize edits.
---

# OPC specification style sign-off

Audit one identifiable edition from source through publication. Keep a finding ledger so the editor can close the original findings without restarting a whole-draft review each time a sentence changes.

## 1. Agree on the target and authority

- Locate the selected specifications from the repository's manifests. Confirm an ambiguous selection and whether the user wants a read-only audit, an audit followed by approved fixes, or verification of an existing finding list. A review alone authorizes no source edits or PR comments. Build outputs for a read-only audit go outside the checkout.
- Locate the repository-local `skills/opcua-spec-style/` or the equivalent explicitly selected by the user. Read its `SKILL.md`, `rules.md`, `examples.md`, and the references called for by applicable rules. Use that bundle as the **only style rubric**. Use repository instructions and CI for authoring, model ownership and publication mechanics, not as substitute style guidance. If the rubric is missing or ambiguous, ask for the authoritative path; do not substitute another installed skill.
- Recover the latest completed draft, prior findings, authorized dispositions, exact exceptions and deferred decisions from this repository or session. Ask if the intended baseline cannot be identified reliably. An earlier proposal, assumption, or accepted fix is not an approved exception.

**Gate:** The scope, mode, rubric and baseline are identified, with prior decisions accounted for.

## 2. Freeze and publish the baseline

Freeze the selected source and its inputs, including in-scope local changes. Produce the required rendered formats from that snapshot using the pinned repository tooling. Inspect HTML and Word where the setup publishes them; account for other formats explicitly. Do not substitute a previous build for missing evidence. See [Publication evidence](references/evidence.md#publication-evidence) for the clean build, supplements and provenance checks.

**Gate:** The baseline and each render are tied to the same inputs. Record any missing prerequisite as a coverage gap.

## 3. Audit the baseline once

- Read the entire selected draft clause by clause, not just the diff. Include glossary and abbreviations, Profile and Conformance Unit sources, authored and generated tables and descriptions, and the corresponding rendered content. Check dependencies where a requirement or its reference crosses into another part or supplement. Apply the local rubric's sentence, clause-shape and terminology checks. Check cited glossaries for applicable term collisions; distinguish ordinary usage from defined terms by meaning.
- Account for **every rubric rule** as checked, not applicable (with a reason), or not verifiable (with the missing evidence). Record coverage of every clause and the rendered tables and generated descriptions. Structural inspection of a Word document is not visual pagination; documenting CTT cases is not executing them.
- Inventory requirements, definitions, mappings, disclosures and positive or negative guarantees before removing or moving anything. Find the authoritative clause for each one and trace every affected prose copy, table, CU/Profile, model-owned description, guide, CTT case and downstream reference. Verify that previously moved or removed requirements still survive where intended and that prior fixes are present in both source and render.
- Record evidenced findings with the exact passage, clause/table or rendered location, rule ID, why it fails, and the smallest correction. Classify **style violation**, **implementation or test ambiguity**, **editorial preference**, or **modelling/tool advisory**. For an ambiguity, state the different observable outcomes the text would permit. A preference or advisory is not a required rewrite. Do not turn a suspected defect into a requirement without evidence.
- If the user requests a fresh reader for the baseline audit, give that reader the frozen edition, the declared prerequisites and the local rubric only. Ask what the reader would implement or test from the text before explaining any intended behavior.

**Gate:** Each rule and clause has a coverage disposition, each prior finding has been reconciled, and each actionable finding can be located and checked. In read-only mode, stop at the verdict in step 6.

## 4. Decide, then edit

- For a policy, compatibility, model or meaning decision, ask **one decision at a time**. State the existing contract, the consequence of each viable option, your recommendation, and an option to defer. Record the user's exact choice and scope. Keep held decisions visible; count a policy affecting implementation or test expectations as a blocker unless the current contract intentionally leaves it outside scope. Before asking for implementation approval, summarize all workstreams, including agreed exceptions and remaining deferrals.
- Batch the approved fixes and clear meaning-preserving edits. Keep each requirement at its authoritative owner and align every dependent copy or replace it with a reference. Preserve modality, conditions, precedence, status layers, identity, and observable guarantees unless the user explicitly decides otherwise. Move useful material removed from normative prose into the applicable implementer guide; if there is no suitable home, ask. Record the reason for every move, merge or removal, including pure duplication.
- Fix a generated description at the source that actually owns it. Follow [Source ownership and contract checks](references/evidence.md#source-ownership-and-contract-checks) before editing model-backed content or moving a clause. Treat a Publisher defect separately: confirm it with a minimal reproduction, use a verified supported source solution where available, otherwise ask whether to require a tooling fix or approve a narrow exception. Do not patch the rendered output. Upgrades, external filings, publishing, and changes outside the edit scope require permission.

**Gate:** The ledger identifies where each accepted fix landed, what was preserved, and what still needs a decision or exception. Checks use fresh renders, not source changes alone.

## 5. Verify independently and close findings

- Freeze and rebuild the edited draft. Give a fresh independent reader that immutable snapshot, the same rubric and the finding list. Require read-only verification of each fix at its owner and all affected copies, including the rendered tables, descriptions and linked supplements. Check that the wording left behind is enough to implement and test the preserved contract without guessing. Require the same passage-and-rule evidence for new findings in changed text or its dependencies. Record an unavailable independent review as missing evidence, not as self-verification.
- Correct supported findings, ask about new policy decisions, and rebuild. Have the reader recheck the affected locations on the new snapshot. Carry forward unchanged audit evidence only after verifying the editorial and rendered delta, including generated or packaged dependencies. Run a new whole-draft audit when requested or when changes invalidate the earlier coverage; do not require repeated fresh whole-draft passes to return zero flags.

**Gate:** Every evidenced violation is closed or covered by an exact approved exception, and no unresolved ambiguity changes what an implementer builds or a test expects. Otherwise report the blocker or missing evidence.

## 6. Give one verdict

Lead with exactly one verdict. Report the audited revision and local-change fingerprint, render provenance, compact rule coverage, and the disposition of prior findings. Separate closed findings, approved exceptions and deferred decisions. List only actionable remaining findings, each with a rule, precise quotation and location, consequence and smallest correction. Omit editorial preferences from sign-off findings.

| Verdict | Condition |
|---|---|
| **PASS** | All applicable checks verified; no violations remain. |
| **PASS WITH EXCEPTIONS** | All applicable checks verified; the only departures are explicitly approved. |
| **NOT READY** | A known violation or decision affecting conformance remains open. State any evidence gaps too. |
| **INCOMPLETE** | Missing evidence prevents sign-off and no known blocker already makes the draft not ready. |
