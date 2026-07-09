#!/usr/bin/env python3
"""Compute the next patch release version (Nerdbank.GitVersioning aware) and optionally write it.

`main` is a public-release ref in these repos, so a release requires bumping `version.json` to
an unpublished version and pushing a matching `vX.Y.Z` tag. The next version is the higher of
(a) the base version already staged in version.json and (b) the latest published version with
its patch incremented — guaranteeing we never re-publish an existing version while honoring a
staged higher base.

Usage:
    next-patch.py --version-json PATH [--latest X.Y.Z] [--write]

Prints JSON {"current": "...", "next": "X.Y.Z", "tag": "vX.Y.Z", "changed": bool}.
"""
from __future__ import annotations

import argparse
import json
import re
import sys


def parse_semver_core(v: str) -> tuple[int, int, int]:
    v = (v or "").strip().lstrip("vV")
    v = re.split(r"[-+]", v, maxsplit=1)[0]  # drop prerelease / build metadata
    parts = (v.split(".") + ["0", "0", "0"])[:3]
    try:
        return tuple(int(p) for p in parts)  # type: ignore[return-value]
    except ValueError:
        return (0, 0, 0)


def read_version_field(path: str) -> tuple[dict, str]:
    data = json.load(open(path, encoding="utf-8"))
    return data, str(data.get("version", "0.0"))


def compute_next(base: str, latest: str) -> tuple[int, int, int]:
    b = parse_semver_core(base)
    p = parse_semver_core(latest)
    patch_bump = (p[0], p[1], p[2] + 1)
    return max(b, patch_bump)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version-json", required=True)
    ap.add_argument("--latest", default="0.0.0", help="latest published version, e.g. 1.0.5")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    data, current = read_version_field(args.version_json)
    nxt = compute_next(current, args.latest)
    nxt_str = f"{nxt[0]}.{nxt[1]}.{nxt[2]}"
    changed = parse_semver_core(current) != nxt

    if args.write:
        data["version"] = nxt_str
        with open(args.version_json, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2)
            fh.write("\n")

    print(json.dumps({"current": current, "next": nxt_str, "tag": f"v{nxt_str}", "changed": changed}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
