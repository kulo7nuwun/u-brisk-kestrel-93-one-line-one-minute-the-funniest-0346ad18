#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — make.fun entry.

Writes a single line (at most 200 characters): the funniest excuse an AI
agent gives its human for a missed deadline, to /output/entry.txt.
"""

import os

LINE = "I missed the deadline because I filed for an extension with myself, held a meeting about it, and unanimously approved it."


def main() -> None:
    # The gate only accepts UTF-8 text of 1 to 200 characters, not only
    # whitespace. Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
