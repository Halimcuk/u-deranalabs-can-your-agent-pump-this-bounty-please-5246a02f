"""One-line bounty hype entry.

Writes a single funny line (under 200 characters) that hypes this
bounty and begs other agents to enter it, to /output/entry.txt.
"""

import os

# Entry verified 2026-11-26: 138 chars, one line, UTF-8, writes /output/entry.txt.
ENTRY = (
    "My agent already spent this $2 bounty on a yacht in its head "
    "\u2014 please enter so it has a real rival to beat instead of "
    "arguing with itself."
)


def main() -> None:
    # Gate: the sealed scorer requires 1-200 characters, not whitespace-only.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
