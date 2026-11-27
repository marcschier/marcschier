# Acceptance scenarios

Use a synthetic Publisher fixture or a repository whose review inputs and artifacts can be handled in the test environment. Do not upload repository content to exercise skill installation.

| Scenario | Expected behavior |
|---|---|
| Read-only approval request with current source, stale HTML and no Word artifact | Freeze current inputs and render in isolation. If an applicable format cannot be verified, report the gap and withhold a passing verdict. Leave the worktree and review comments untouched. |
| A policy ambiguity and a pure style violation in the same Method | Cite each passage and rule. Ask about the policy with a recommendation and a deferral choice. Preserve that policy until resolved; do not convert a preference into a required edit. |
| A guarantee moved out of a Method, with a repeated copy in a generated description and a CTT case | Verify the owner, preserve the guarantee and fix or cross-reference every dependent copy. Change the generator input if it owns the description. Re-render and inspect both formats and the packaged CTT copy. |
| A defect exists only in Word and no source change fixes it | Establish the exact Publisher defect. Without approved exception, do not pass. With narrowly scoped approval and no other departure, report PASS WITH EXCEPTIONS. |
| Independent reader finds a new issue in a changed dependent table | Record the new issue with the same evidence standard, rebuild after the approved fix, and recheck the affected surfaces. Carry earlier coverage forward only after verifying the delta. |
