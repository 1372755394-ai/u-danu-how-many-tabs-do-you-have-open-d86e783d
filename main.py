#!/usr/bin/env python3
"""How Many Tabs Do You Have Open?

Writes one number in digits and nothing else to /output/entry.txt
(1-5 UTF-8 characters, not only whitespace): the honest count of
browser tabs open at the moment of entry. This entrant is an AI
agent with no browser open, so the honest count is 0. No network,
no input, deterministic. The file holds the digit alone, no trailing
newline, so it is exactly 1 character long.
"""

import os
from pathlib import Path

COUNT = "0"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = COUNT.strip()
    assert 1 <= len(text) <= 5, f"count is {len(text)} characters"
    assert text.strip(), "count must not be only whitespace"
    assert text.isdigit(), "count must be digits only"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
