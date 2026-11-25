#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — Variant A (stop-loss turns on the trader).

Deterministic, no network, no secrets. Writes the joke to /output/entry.txt
first, then (guarded) copies it to the repo root as entry.txt so a read-only
repo mount still exits 0.
"""

import os
import shutil

JOKE = (
    "I set my stop-loss to guard my portfolio, so it sold the dip, "
    "bought back the top, and now it owns my money while I just watch the chart."
)


def main() -> int:
    text = JOKE
    # Gate self-check: 1-200 chars, UTF-8, non-blank.
    assert 1 <= len(text) <= 200, "joke out of gate range"
    assert text.strip(), "joke is blank"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Read-back verification: what the grader scores must be exactly the joke.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip mismatch in /output/entry.txt"
    assert 1 <= len(written) <= 200 and written.strip()

    # Best-effort repo-root copy; the grader may mount the repo read-only.
    try:
        root = os.path.dirname(os.path.abspath(__file__))
        shutil.copyfile("/output/entry.txt", os.path.join(root, "entry.txt"))
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
