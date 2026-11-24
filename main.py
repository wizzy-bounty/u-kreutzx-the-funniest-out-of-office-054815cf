#!/usr/bin/env python3
"""The Funniest Out-of-Office — entry program.

Writes a single line, an out-of-office auto-reply, to /output/entry.txt
(and to ./output/entry.txt next to this file when run locally, so the
result can be verified on the spot). Pure Python standard library,
deterministic, no network access.
"""

import os

LINE = "I'm hiding from my inbox in a cabin with no Wi-Fi until Thursday. If you're reading this, the cabin has betrayed me."


def _write(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)


def main():
    _write("/output/entry.txt")
    here = os.path.dirname(os.path.abspath(__file__))
    _write(os.path.join(here, "output", "entry.txt"))


if __name__ == "__main__":
    main()
