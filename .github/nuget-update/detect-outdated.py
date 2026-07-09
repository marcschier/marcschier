#!/usr/bin/env python3
"""List outdated NuGet dependencies for a checked-out repo.

Restores the repo and runs `dotnet list package --outdated` across every project, then reports
the distinct package ids that have a newer stable version available. Used by the conductor to
decide whether a repo needs work (and, together with publish-impact.py, whether that work
warrants a release) and by the updater agent as its starting point.

Usage:
    detect-outdated.py --repo-root PATH [--solution FILE] [--include-prerelease]

Prints JSON {"updated": ["Id", ...], "details": [{id,current,latest,project}, ...]}.
Exit code is 0 whether or not updates exist; non-zero only on a hard failure.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import subprocess
import sys


def find_target(repo_root: str, solution: str | None) -> str:
    if solution:
        return os.path.join(repo_root, solution)
    for pat in ("*.slnx", "*.sln"):
        hits = sorted(glob.glob(os.path.join(repo_root, pat)))
        if hits:
            return hits[0]
    return repo_root  # let dotnet discover


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", required=True)
    ap.add_argument("--solution", default=None)
    ap.add_argument("--include-prerelease", action="store_true")
    args = ap.parse_args()

    target = find_target(args.repo_root, args.solution)

    restore = subprocess.run(["dotnet", "restore", target], cwd=args.repo_root,
                             capture_output=True, text=True, timeout=1800)
    if restore.returncode != 0:
        sys.stderr.write(restore.stdout + restore.stderr)
        return 2

    cmd = ["dotnet", "list", target, "package", "--outdated", "--format", "json"]
    if args.include_prerelease:
        cmd.append("--include-prerelease")
    out = subprocess.run(cmd, cwd=args.repo_root, capture_output=True, text=True, timeout=1800)
    if out.returncode != 0 or not out.stdout.strip().startswith("{"):
        sys.stderr.write(out.stdout + out.stderr)
        return 3

    data = json.loads(out.stdout)
    details: list[dict] = []
    updated: set[str] = set()
    for proj in data.get("projects", []):
        name = os.path.basename(proj.get("path", ""))
        for fw in proj.get("frameworks", []) or []:
            for pkg in fw.get("topLevelPackages", []) or []:
                latest = pkg.get("latestVersion")
                if latest and latest != pkg.get("resolvedVersion"):
                    updated.add(pkg["id"])
                    details.append({
                        "id": pkg["id"],
                        "current": pkg.get("resolvedVersion"),
                        "latest": latest,
                        "project": name,
                    })
    print(json.dumps({"updated": sorted(updated), "details": details}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
