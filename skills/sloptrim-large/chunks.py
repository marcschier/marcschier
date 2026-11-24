"""Plan, read, and score bounded chunks without modifying the source."""

import argparse
import bisect
import hashlib
import json
from pathlib import Path
import re
import runpy
import sys


LIMIT = 10_000
HEADING = re.compile(r"^ {0,3}#{1,6}(?:[ \t]|$)")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)")


def boundaries(text):
    headings, paragraphs, lines = [], [], [0]
    protected = []
    fence = None
    block = None
    offset = 0
    for line in text.splitlines(keepends=True):
        body = line.rstrip("\r\n")
        end = offset + len(line)
        marker = FENCE.match(body)
        if fence:
            if marker and marker[1].startswith(fence) and not marker[2].strip():
                fence = None
                protected.append((block, end))
                block = None
        elif block is not None:
            if body.lstrip().startswith("<!-- END GENERATED"):
                protected.append((block, end))
                block = None
        elif body.lstrip().startswith("<!-- BEGIN GENERATED"):
            block = offset
        elif marker:
            fence = marker[1]
            block = offset
        elif HEADING.match(body):
            headings.append(offset)
        elif not body.strip():
            paragraphs.append(end)
        offset = end
        lines.append(offset)
    if block is not None:
        protected.append((block, offset))
    return headings, paragraphs, lines, protected


def plan(text, limit=LIMIT):
    headings, paragraphs, lines, protected = boundaries(text)
    start = 0
    while start < len(text):
        end = min(start + limit, len(text))
        if end < len(text):
            for candidates in (headings, paragraphs, lines):
                i = bisect.bisect_right(candidates, end) - 1
                if i >= 0 and candidates[i] > start:
                    end = candidates[i]
                    break
        yield {
            "start": start,
            "end": end,
            "first_line": bisect.bisect_right(lines, start),
            "last_line": bisect.bisect_right(lines, end - 1),
            "protected": [(max(lo, start), min(hi, end))
                          for lo, hi in protected if lo < end and start < hi],
        }
        start = end


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("command", choices=("plan", "read", "scan"))
    parser.add_argument("id", type=int, nargs="?")
    parser.add_argument("--detector", type=Path)
    parser.add_argument("--mode", choices=("normal", "strict"), default="normal")
    parser.add_argument("--expect-sha")
    parser.add_argument("--window", type=int, nargs=2, metavar=("OFFSET", "LENGTH"))
    args = parser.parse_args()
    try:
        raw = args.file.read_bytes()
        text = raw.decode("utf-8-sig")
    except (OSError, UnicodeError) as error:
        parser.exit(1, f"{error}\n")
    digest = hashlib.sha256(raw).hexdigest()
    if args.expect_sha and digest != args.expect_sha:
        parser.exit(1, "Source changed since planning; generate a new plan.\n")

    chunks = [dict(id=i, **entry) for i, entry in enumerate(plan(text), 1)]
    if args.command == "plan":
        print(json.dumps({"sha256": digest, "characters": len(text), "chunks": chunks}))
        return
    if not args.expect_sha or args.id is None or not 1 <= args.id <= len(chunks):
        parser.error("read and scan require the plan's --expect-sha and a valid chunk ID")
    entry = chunks[args.id - 1]
    chunk = text[entry["start"]:entry["end"]]
    if args.command == "read":
        if args.window:
            offset, length = args.window
            if not 0 <= offset < len(chunk) or length < 1:
                parser.error("--window requires a valid chunk-relative offset and positive length")
            chunk = chunk[offset:offset + length]
        sys.stdout.buffer.write(chunk.encode("utf-8"))
        return
    if not args.detector or not args.detector.is_file():
        parser.error("scan requires --detector pointing to installed Sloptrim detect.py")
    detector = runpy.run_path(str(args.detector.resolve()))
    syntax = "markdown" if args.file.suffix.lower() in {".md", ".markdown", ".mdx"} else "plain"
    # Keep line breaks while excluding blocks that may span several chunks.
    sample = chunk
    for lo, hi in reversed(entry["protected"]):
        lo, hi = lo - entry["start"], hi - entry["start"]
        sample = sample[:lo] + re.sub(r"[^\r\n]+", "", sample[lo:hi]) + sample[hi:]
    sample = sample.rstrip("\r\n") + "\n"
    report = detector["scan"](sample, syntax=syntax)
    metrics = report["_metrics"]
    if metrics["truncated"]:
        parser.exit(1, "Sloptrim truncated the chunk; coverage cannot be recorded.\n")
    threshold = 20 if args.mode == "strict" else 40
    print(json.dumps({
        **entry,
        "threshold": threshold,
        "flagged": metrics["ai_tell_score"] > threshold,
        "scrub_suggested": detector["clean_text"](sample, syntax=syntax).rstrip("\r\n")
        != sample.rstrip("\r\n"),
        "report": report,
    }))


if __name__ == "__main__":
    main()
