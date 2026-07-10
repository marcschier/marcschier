#!/usr/bin/env python3
"""Conductor: the deterministic release state machine for the autonomous NuGet-update pipeline.

Processes the repos listed in README.md in leaf-to-top order. For each repo it walks the phases:

    detect -> update -> await-pr-ci -> merge -> publish-impact
           -> release (bump patch + tag) -> await-tag-ci -> promote (human gate)
           -> await-listing -> done

Short waits (CI, nuget indexing) are block-polled up to a per-run budget; the run yields and
persists state at the human promotion gate if approval has not arrived, to be resumed by the
next scheduled/manual trigger. Any hard failure opens an issue in the affected repo and halts
the whole pipeline (no further repos are processed).

All privileged git/gh operations use GH_TOKEN (a cross-repo PAT/App token). The agent never
runs here; this is deterministic orchestration invoked from the conductor gh-aw workflow.

State is persisted as JSON on a dedicated branch of the profile repo so runs are resumable.

Environment:
    GH_TOKEN            cross-repo token (contents/PRs/issues/actions:write, packages:read)
    GITHUB_REPOSITORY   the profile/orchestrator repo (owner/name)
    RUN_BUDGET_MIN      soft per-run time budget in minutes (default 300)
    GATE_WAIT_MIN       max minutes to wait at the human promotion gate before yielding (default 45)
"""
from __future__ import annotations

import base64
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OWNER = "marcschier"
ORCH_REPO = os.environ.get("GITHUB_REPOSITORY", f"{OWNER}/{OWNER}")
# Cross-repo operations (clone target repos, PRs, merges, issues, tags, nuget.yml dispatch) use
# GH_TOKEN (a PAT scoped to the README repos). Operations on the orchestrator repo itself (state
# branch, dispatching the updater workflow) use ORCH_TOKEN — the workflow's own GITHUB_TOKEN,
# which always has access to this repo — because the PAT is not scoped to marcschier/marcschier.
ORCH_TOKEN = os.environ.get("STATE_TOKEN") or os.environ.get("GH_TOKEN", "")
STATE_BRANCH = "automation/nuget-update-state"
STATE_PATH = "state.json"
UPDATER_WORKFLOW = "nuget-update-repo.lock.yml"
PR_LABEL = "dependencies"
POLL_SECS = 30
RUN_BUDGET = int(os.environ.get("RUN_BUDGET_MIN", "300")) * 60
GATE_WAIT = int(os.environ.get("GATE_WAIT_MIN", "45")) * 60
START = time.time()


# --------------------------------------------------------------------------- helpers
def sh(*args: str, check: bool = True, cwd: str | None = None, env: dict | None = None) -> str:
    res = subprocess.run(args, capture_output=True, text=True, cwd=cwd,
                         env={**os.environ, **(env or {})})
    if check and res.returncode != 0:
        raise RuntimeError(f"$ {' '.join(args)}\n{res.stdout}\n{res.stderr}")
    return res.stdout.strip()


def gh(*args: str, check: bool = True, token: str | None = None) -> str:
    env = {"GH_TOKEN": token} if token else None
    return sh("gh", *args, check=check, env=env)


def gh_json(*args: str, check: bool = True, token: str | None = None):
    out = gh(*args, check=check, token=token)
    if not out:
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return None


def budget_left() -> float:
    return RUN_BUDGET - (time.time() - START)


def log(msg: str) -> None:
    print(f"[conductor] {msg}", flush=True)


def load_config():
    import yaml  # provided by the workflow (pip install pyyaml)
    order = json.loads(sh("python", os.path.join(HERE, "parse-readme.py")))["order"]
    cfg = yaml.safe_load(open(os.path.join(HERE, "repos.yml"), encoding="utf-8"))
    return order, cfg


# ------------------------------------------------------------------------- state I/O
def _ensure_state_branch() -> None:
    try:
        gh("api", f"repos/{ORCH_REPO}/branches/{STATE_BRANCH}", token=ORCH_TOKEN)
        return
    except RuntimeError:
        pass
    default = gh_json("api", f"repos/{ORCH_REPO}", "--jq", "{b:.default_branch}", token=ORCH_TOKEN)["b"]
    sha = gh("api", f"repos/{ORCH_REPO}/git/ref/heads/{default}", "--jq", ".object.sha", token=ORCH_TOKEN)
    gh("api", "-X", "POST", f"repos/{ORCH_REPO}/git/refs",
       "-f", f"ref=refs/heads/{STATE_BRANCH}", "-f", f"sha={sha}", token=ORCH_TOKEN)


def load_state() -> dict:
    try:
        raw = gh("api", f"repos/{ORCH_REPO}/contents/{STATE_PATH}?ref={STATE_BRANCH}",
                 "--jq", ".content", check=True, token=ORCH_TOKEN)
        return json.loads(base64.b64decode(raw).decode())
    except RuntimeError:
        return {"status": "idle", "repos": {}}


def save_state(state: dict) -> None:
    _ensure_state_branch()
    state["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    content = base64.b64encode(json.dumps(state, indent=2).encode()).decode()
    # The Contents API requires the current blob sha when updating an existing file. Re-fetch the
    # sha immediately before each attempt and retry, so a stale/missing sha (propagation race or a
    # concurrent write) cannot wedge the pipeline with a 422 "sha wasn't supplied".
    last_err: Exception | None = None
    for attempt in range(4):
        sha = gh_json("api", f"repos/{ORCH_REPO}/contents/{STATE_PATH}",
                      "-f", f"ref={STATE_BRANCH}", "--jq", "{sha:.sha}",
                      check=False, token=ORCH_TOKEN)
        sha_val = (sha or {}).get("sha")
        args = ["api", "-X", "PUT", f"repos/{ORCH_REPO}/contents/{STATE_PATH}",
                "-f", "message=chore: update nuget-update conductor state",
                "-f", f"branch={STATE_BRANCH}", "-f", f"content={content}"]
        if sha_val:
            args += ["-f", f"sha={sha_val}"]
        try:
            gh(*args, token=ORCH_TOKEN)
            return
        except RuntimeError as exc:
            last_err = exc
            time.sleep(2 + attempt * 2)
    raise RuntimeError(f"save_state failed after retries: {last_err}")


# ------------------------------------------------------------------- pipeline helpers
def nuget_latest(pkg_id: str) -> str:
    url = f"https://api.nuget.org/v3-flatcontainer/{pkg_id.lower()}/index.json"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            versions = json.load(resp)["versions"]
    except Exception:
        return "0.0.0"
    stable = [v for v in versions if "-" not in v]
    return (stable or versions or ["0.0.0"])[-1]


def nuget_has_version(pkg_id: str, version: str) -> bool:
    url = f"https://api.nuget.org/v3-flatcontainer/{pkg_id.lower()}/index.json"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            return version in json.load(resp)["versions"]
    except Exception:
        return False


def clone(repo: str) -> str:
    tmp = tempfile.mkdtemp(prefix=f"{repo}-")
    token = os.environ["GH_TOKEN"]
    url = f"https://x-access-token:{token}@github.com/{OWNER}/{repo}.git"
    sh("git", "clone", "--depth", "50", url, tmp)
    sh("git", "-C", tmp, "config", "user.name", "nuget-update-bot")
    sh("git", "-C", tmp, "config", "user.email", "nuget-update-bot@users.noreply.github.com")
    return tmp


def open_dep_pr(repo: str) -> dict | None:
    prs = gh_json("pr", "list", "-R", f"{OWNER}/{repo}", "--label", PR_LABEL,
                  "--state", "open", "--json", "number,headRefName,createdAt,mergeStateStatus")
    return sorted(prs, key=lambda p: p["createdAt"])[-1] if prs else None


def pr_checks_conclusion(repo: str, number: int) -> str:
    """'success' | 'failure' | 'pending'."""
    roll = gh_json("pr", "view", str(number), "-R", f"{OWNER}/{repo}",
                   "--json", "statusCheckRollup", "--jq", ".statusCheckRollup")
    if not roll:
        return "pending"
    states = [c.get("conclusion") or c.get("state") or "" for c in roll]
    if any(s in ("FAILURE", "ERROR", "CANCELLED", "TIMED_OUT") for s in states):
        return "failure"
    if any(s in ("", "PENDING", "IN_PROGRESS", "QUEUED", "EXPECTED") for s in states):
        return "pending"
    return "success"


def run_conclusion(repo: str, run_id: int) -> str:
    r = gh_json("run", "view", str(run_id), "-R", f"{OWNER}/{repo}",
                "--json", "status,conclusion")
    if r["status"] != "completed":
        return "pending"
    return r["conclusion"] or "failure"


def latest_ci_run_for_tag(repo: str, tag: str) -> int | None:
    runs = gh_json("run", "list", "-R", f"{OWNER}/{repo}", "-w", "ci.yml",
                   "--json", "databaseId,headBranch,event", "-L", "30") or []
    for r in runs:
        if r.get("headBranch") == tag:
            return r["databaseId"]
    return None


def fail(repo: str, state: dict, phase: str, detail: str) -> None:
    body = (f"The autonomous NuGet-update pipeline halted at **{repo}** during **{phase}**.\n\n"
            f"```\n{detail[:55000]}\n```\n\nThe pipeline will not advance until this is resolved.")
    gh("issue", "create", "-R", f"{OWNER}/{repo}",
       "-t", f"[nuget-update] halted at {phase}", "-b", body,
       "-l", "automation", check=False)
    state["status"] = "halted"
    state.setdefault("repos", {}).setdefault(repo, {})["phase"] = "failed"
    state["repos"][repo]["note"] = f"{phase}: {detail[:500]}"
    save_state(state)
    log(f"HALTED at {repo} / {phase}: {detail[:200]}")


# --------------------------------------------------------------------------- phases
def process_repo(repo: str, cfg: dict, state: dict) -> str:
    """Advance one repo as far as the run budget allows. Returns its terminal-ish phase."""
    rstate = state.setdefault("repos", {}).setdefault(repo, {"phase": "pending"})
    rcfg = cfg["repos"][repo]

    # detect ---------------------------------------------------------------
    if rstate["phase"] in ("pending",):
        work = clone(repo)
        det = subprocess.run(["python", os.path.join(HERE, "detect-outdated.py"),
                              "--repo-root", work], capture_output=True, text=True)
        if det.returncode != 0:
            fail(repo, state, "detect", det.stdout + det.stderr)
            return "failed"
        updated = json.loads(det.stdout)["updated"]
        rstate["updated"] = updated
        if not updated:
            rstate["phase"] = "done"
            rstate["note"] = "no outdated dependencies"
            save_state(state)
            log(f"{repo}: no updates, skipping")
            return "done"
        # Idempotency: adopt an existing open dependency PR instead of dispatching a duplicate.
        existing = open_dep_pr(repo)
        if existing:
            rstate["pr"] = existing["number"]
            rstate["phase"] = "awaiting-pr-ci"
            save_state(state)
            log(f"{repo}: adopting existing dependency PR #{existing['number']}")
        else:
            gh("workflow", "run", UPDATER_WORKFLOW, "-R", ORCH_REPO, "-f", f"repo={repo}", token=ORCH_TOKEN)
            rstate["phase"] = "awaiting-pr"
            save_state(state)
            log(f"{repo}: dispatched updater for {len(updated)} outdated package(s)")

    # await PR from the updater -------------------------------------------
    if rstate["phase"] == "awaiting-pr":
        while budget_left() > POLL_SECS:
            pr = open_dep_pr(repo)
            if pr:
                rstate["pr"] = pr["number"]
                rstate["phase"] = "awaiting-pr-ci"
                save_state(state)
                break
            # If the updater finished without a PR, it raised a failure issue -> halt.
            time.sleep(POLL_SECS)
        else:
            return "awaiting-pr"

    # await PR CI, then merge ---------------------------------------------
    if rstate["phase"] == "awaiting-pr-ci":
        while budget_left() > POLL_SECS:
            c = pr_checks_conclusion(repo, rstate["pr"])
            if c == "success":
                # Libraries protect main with a ruleset requiring code-owner review. The bot
                # authors the PR and cannot self-approve, so an autonomous merge bypasses the
                # review via --admin (CI is the real gate). Requires the token's identity to be
                # in the ruleset's bypass actors (repository admin/maintainer).
                try:
                    gh("pr", "merge", str(rstate["pr"]), "-R", f"{OWNER}/{repo}", "--squash", "--admin")
                except RuntimeError as exc:
                    fail(repo, state, "merge", str(exc))
                    return "failed"
                rstate["phase"] = "publish-impact"
                save_state(state)
                break
            if c == "failure":
                fail(repo, state, "await-pr-ci", f"PR #{rstate['pr']} checks failed")
                return "failed"
            time.sleep(POLL_SECS)
        else:
            return "awaiting-pr-ci"

    # publish-impact gate --------------------------------------------------
    if rstate["phase"] == "publish-impact":
        work = clone(repo)
        sh("dotnet", "restore", cwd=work, check=False)
        imp = subprocess.run(
            ["python", os.path.join(HERE, "publish-impact.py"), "--repo-root", work,
             "--repo", repo, "--updated", ",".join(rstate.get("updated", []))],
            capture_output=True, text=True)
        impact = imp.returncode == 0 and json.loads(imp.stdout or "{}").get("impact")
        if not impact:
            rstate["phase"] = "done"
            rstate["note"] = "updated-not-released (no published package affected)"
            save_state(state)
            log(f"{repo}: merged, but no published package changed -> no release")
            return "done"
        rstate["phase"] = "release"
        save_state(state)

    # release: bump patch + tag -------------------------------------------
    if rstate["phase"] == "release":
        core = rcfg["wait"][0].get("id") or repo
        latest = nuget_latest(core) if rcfg["wait"][0]["type"] == "nuget" else "0.0.0"
        work = clone(repo)
        vj = os.path.join(work, "version.json")
        res = json.loads(sh("python", os.path.join(HERE, "next-patch.py"),
                            "--version-json", vj, "--latest", latest, "--write"))
        tag = res["tag"]
        if res["changed"]:
            sh("git", "-C", work, "commit", "-am", f"chore: release {tag}")
            sh("git", "-C", work, "push", "origin", "HEAD:main")
        sh("git", "-C", work, "tag", tag)
        sh("git", "-C", work, "push", "origin", tag)
        rstate["tag"] = tag
        rstate["phase"] = "awaiting-tag-ci"
        save_state(state)
        log(f"{repo}: tagged {tag}")

    # await tag CI (tests + publish to GitHub Packages) -------------------
    if rstate["phase"] == "awaiting-tag-ci":
        while budget_left() > POLL_SECS:
            run_id = latest_ci_run_for_tag(repo, rstate["tag"])
            if run_id:
                c = run_conclusion(repo, run_id)
                if c == "success":
                    rstate["phase"] = "promote"
                    save_state(state)
                    break
                if c == "failure":
                    fail(repo, state, "await-tag-ci", f"tag {rstate['tag']} CI failed (run {run_id})")
                    return "failed"
            time.sleep(POLL_SECS)
        else:
            return "awaiting-tag-ci"

    # promote (human-gated) -----------------------------------------------
    if rstate["phase"] == "promote":
        if rcfg["promote"] == "nuget-yml":
            gh("workflow", "run", "nuget.yml", "-R", f"{OWNER}/{repo}",
               "-f", f"version={rstate['tag'][1:]}", check=False)
            rstate["phase"] = "awaiting-promotion"
            save_state(state)
        else:
            # MCP repos publish inside ci.yml already; nothing to dispatch.
            rstate["phase"] = "awaiting-listing"
            save_state(state)

    if rstate["phase"] == "awaiting-promotion":
        gate_start = time.time()
        while budget_left() > POLL_SECS and (time.time() - gate_start) < GATE_WAIT:
            runs = gh_json("run", "list", "-R", f"{OWNER}/{repo}", "-w", "nuget.yml",
                           "--json", "databaseId,status,conclusion", "-L", "1") or []
            if runs:
                r = runs[0]
                if r["status"] == "completed":
                    if r["conclusion"] == "success":
                        rstate["phase"] = "awaiting-listing"
                        save_state(state)
                        break
                    fail(repo, state, "promote", "nuget.org promotion run did not succeed")
                    return "failed"
            time.sleep(POLL_SECS)
        else:
            if rstate["phase"] == "awaiting-promotion":
                log(f"{repo}: waiting on human approval of promotion; yielding")
                return "awaiting-promotion"

    # await nuget.org listing ---------------------------------------------
    if rstate["phase"] == "awaiting-listing":
        target_ver = rstate["tag"][1:]
        nuget_waits = [w for w in rcfg["wait"] if w["type"] == "nuget"]
        while budget_left() > POLL_SECS:
            if all(nuget_has_version(w["id"], target_ver) for w in nuget_waits) or not nuget_waits:
                rstate["phase"] = "done"
                rstate["note"] = f"released {rstate['tag']}"
                save_state(state)
                log(f"{repo}: released and live on nuget.org")
                return "done"
            time.sleep(POLL_SECS)
        return "awaiting-listing"

    return rstate["phase"]


def main() -> int:
    order, cfg = load_config()
    state = load_state()
    if state.get("status") == "halted":
        log("pipeline is halted; resolve the open issue and clear state to resume")
        return 0

    only = os.environ.get("ONLY_REPO", "").strip()
    if only:
        if only not in order:
            log(f"ONLY_REPO='{only}' is not a known repo in {order}")
            return 1
        order = [only]
        log(f"scoped run: processing only '{only}'")

    state["status"] = "running"
    save_state(state)

    for repo in order:
        if budget_left() < POLL_SECS:
            log("run budget exhausted; will resume on next trigger")
            return 0
        phase = state.get("repos", {}).get(repo, {}).get("phase")
        if phase == "done":
            continue
        result = process_repo(repo, cfg, state)
        if result == "failed":
            return 1
        if result not in ("done",):
            log(f"{repo}: yielded at phase '{result}'; will resume on next trigger")
            return 0  # wait states block the whole pipeline (strict leaf->top ordering)

    if not only:
        state["status"] = "done"
        save_state(state)
        log("all repos processed")
    else:
        state["status"] = "idle"
        save_state(state)
        log(f"scoped run for '{only}' complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
