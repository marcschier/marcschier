#!/usr/bin/env python3
"""Decide whether a set of updated NuGet packages changes any *published* package.

A release is only warranted when an updated dependency reaches a packable project (one that is
packed into a published package). This computes the union of the transitive PackageReference
closures of the repo's packable projects (from repos.yml) and checks whether any updated
package id is inside it. Updates confined to test/benchmark/sample/interop projects therefore
produce no release.

Usage:
    publish-impact.py --repo-root PATH --repo NAME --updated a,b,c [--repos-yml PATH]

Exit code 0 always; prints JSON {"impact": bool, "hits": [...], "closure_size": n}.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_REPOS_YML = os.path.join(HERE, "repos.yml")

# Packages that may be referenced by a packable project but do NOT contribute to the produced
# package's content or nuspec dependencies (build/versioning tools and dev-only analyzers).
# Bumping only these must not trigger a release. Extend via `defaults.non_impacting` in repos.yml.
#
# NOTE: pure diagnostic analyzers are non-impacting, but source generators that inject code into
# the assembly (e.g. PolySharp) ARE impacting and must never be listed here.
DEFAULT_NON_IMPACTING = {
    "nerdbank.gitversioning",
    "roslynator.analyzers",
    "roslynator.formatting.analyzers",
    "microsoft.visualstudio.threading.analyzers",
    "meziantou.analyzer",
    "idisposableanalyzers",
    "stylecop.analyzers",
    "microsoft.codeanalysis.netanalyzers",
    "microsoft.testing.extensions.codecoverage",
    "coverlet.collector",
    "coverlet.msbuild",
}


def load_non_impacting(repos_yml: str) -> set[str]:
    """Read `defaults.non_impacting` (a flow/block list) from repos.yml, merged with defaults."""
    extra: set[str] = set()
    if os.path.exists(repos_yml):
        in_defaults = False
        for raw in open(repos_yml, encoding="utf-8"):
            if re.match(r"^defaults:\s*$", raw):
                in_defaults = True
                continue
            if in_defaults and re.match(r"^\S", raw):
                break
            if in_defaults:
                m = re.search(r"non_impacting:\s*\[([^\]]*)\]", raw)
                if m:
                    extra |= {p.strip().strip("'\"").lower() for p in m.group(1).split(",") if p.strip()}
    return DEFAULT_NON_IMPACTING | extra


def packable_paths(repos_yml: str, repo: str) -> list[str]:
    """Extract `path:` values under repos.<repo>.packable without a yaml dependency."""
    paths: list[str] = []
    depth_repo = None  # indentation state machine
    in_repos = in_target = in_packable = False
    for raw in open(repos_yml, encoding="utf-8"):
        if re.match(r"^repos:\s*$", raw):
            in_repos = True
            continue
        if not in_repos:
            continue
        if re.match(r"^\S", raw):
            break
        m_repo = re.match(r"^  ([A-Za-z0-9._-]+):\s*$", raw)
        if m_repo:
            in_target = (m_repo.group(1) == repo)
            in_packable = False
            continue
        if in_target and re.match(r"^    packable:\s*$", raw):
            in_packable = True
            continue
        if in_target and in_packable:
            if re.match(r"^    \S", raw) and not raw.lstrip().startswith("-"):
                in_packable = False
                continue
            m = re.search(r"path:\s*([^,}\s]+)", raw)
            if m:
                paths.append(m.group(1))
    return paths


def project_closure(repo_root: str, proj_path: str) -> set[str]:
    """All package ids (top-level + transitive) referenced by a project, lowercased."""
    ids: set[str] = set()
    full = os.path.join(repo_root, proj_path)
    # Prefer JSON output (SDK >= 7); fall back to text parsing.
    try:
        out = subprocess.run(
            ["dotnet", "list", full, "package", "--include-transitive", "--format", "json"],
            capture_output=True, text=True, cwd=repo_root, timeout=600,
        )
        if out.returncode == 0 and out.stdout.strip().startswith("{"):
            data = json.loads(out.stdout)
            for proj in data.get("projects", []):
                for fw in proj.get("frameworks", []):
                    for key in ("topLevelPackages", "transitivePackages"):
                        for pkg in fw.get(key, []) or []:
                            if pkg.get("id"):
                                ids.add(pkg["id"].lower())
            return ids
    except Exception:  # noqa: BLE001 - fall through to text mode
        pass
    out = subprocess.run(
        ["dotnet", "list", full, "package", "--include-transitive"],
        capture_output=True, text=True, cwd=repo_root, timeout=600,
    )
    for line in out.stdout.splitlines():
        m = re.match(r"^\s*(?:>|Transitive)?\s*([A-Za-z0-9._-]+)\s+", line)
        if m and "." in m.group(1):
            ids.add(m.group(1).lower())
    return ids


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--updated", default="", help="comma-separated updated package ids")
    ap.add_argument("--repos-yml", default=DEFAULT_REPOS_YML)
    args = ap.parse_args()

    updated = {p.strip().lower() for p in args.updated.split(",") if p.strip()}
    paths = packable_paths(args.repos_yml, args.repo)
    if not paths:
        print(json.dumps({"impact": False, "hits": [], "closure_size": 0,
                          "note": f"no packable projects for {args.repo}"}))
        return 0

    closure: set[str] = set()
    for p in paths:
        closure |= project_closure(args.repo_root, p)

    non_impacting = load_non_impacting(args.repos_yml)
    hits = sorted((updated & closure) - non_impacting)
    print(json.dumps({"impact": bool(hits), "hits": hits, "closure_size": len(closure)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
