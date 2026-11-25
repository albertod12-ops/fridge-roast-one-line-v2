#!/usr/bin/env python3
"""Fridge Roast v2: one line roasting a smart fridge, at most 200 chars.

The program drops the roast into /output/entry.txt (mode 0644, no trailing
newline). Standard library only; the output is byte-identical on every run,
so the judge always reads exactly this line.
"""

import os

ROAST = (
    "My fridge's app charges $4.99 a month to tell me I'm out of milk \u2014 "
    "a job the empty shelf did for free, without a login."
)


def write_roast() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    line = ROAST
    if not 1 <= len(line) <= 200:
        raise ValueError("roast must be 1-200 characters")
    if not line.strip():
        raise ValueError("roast must not be only whitespace")
    target = "/output/entry.txt"
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    write_roast()
