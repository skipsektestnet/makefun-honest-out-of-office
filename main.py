"""The Painfully Honest Out-of-Office.

Writes the one-line entry to /output/entry.txt.

The joke: brutal honesty up front (no email checks, 214 unread,
answered in order of dread, slowest first) with a polite close,
so it reads like a real auto-reply a manager would let stand.
"""

import os

PARTS = [
    "I'm out until Monday and won't check email.",
    "Your message joins 214 unread emails I'll answer in order of dread,",
    "slowest first. Thank you for understanding.",
]
ENTRY = " ".join(PARTS)

OUT = "/output/entry.txt"


def build_entry():
    """Return the entry, enforcing the bounty gate (one line, <= 200 chars)."""
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= 200, "entry exceeds 200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    return ENTRY


def main():
    text = build_entry()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote", OUT, len(text), "chars")


if __name__ == "__main__":
    main()
