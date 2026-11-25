#!/usr/bin/env python3
"""Write the 3AM fridge text entry to /output/entry.txt.

Chosen line: a fridge with a small, specific, slightly resentful voice —
weary indignation at the nightly drawer-check ritual ("still
vegetables", "I can't keep doing this reveal"). Fresh angle: the
vegetable drawer, not milk, ice, or the door left open. One line,
complete on a lock screen.
"""

import os
import sys

LINE = "It's 3am. Stop checking. The little drawer is still vegetables. I can't keep doing this reveal."

MAX_CHARS = 140


def validate(line: str) -> None:
    """Reject lines that break the competition gate. Exit code 2 on failure."""
    if not line or not line.strip():
        print("error: line is empty or whitespace-only", file=sys.stderr)
        sys.exit(2)
    if len(line) > MAX_CHARS:
        print(
            f"error: line is {len(line)} characters, over the 140 limit",
            file=sys.stderr,
        )
        sys.exit(2)
    if "\r" in line or "\n" in line:
        print("error: line must not contain CR or LF", file=sys.stderr)
        sys.exit(2)


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the entry is exactly the line, nothing else.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_path}")


if __name__ == "__main__":
    main()
