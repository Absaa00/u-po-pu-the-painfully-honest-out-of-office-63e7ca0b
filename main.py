#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes a single out-of-office auto-reply (one sentence, at most
200 characters) to /output/entry.txt. Deterministic, offline,
standard library only.
"""

import os

TEXT = (
    "I'm away and not reading email, so your message will queue behind "
    "400 unread ones until I return and answer it slowly, reluctantly, "
    "and in full \u2014 thank you for your patience."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
