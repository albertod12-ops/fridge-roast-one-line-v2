#!/usr/bin/env python3
"""Fridge Roast v2: one line, at most 200 characters, roasting a smart fridge.

Writes the roast to /output/entry.txt, mode 0644, no trailing newline.
Standard library only. Deterministic: the same bytes on every run, so the
judge always reads exactly this line.
"""

import os

ENTRY = (
    "My fridge's app charges $4.99 a month to tell me I'm out of milk \u2014 "
    "a job the empty shelf did for free, without a login."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
