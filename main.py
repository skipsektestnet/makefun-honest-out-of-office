"""The Painfully Honest Out-of-Office: writes the entry text to /output/entry.txt.

Why this line: painfully honest first (will not check email, 214 unread,
answered in order of dread), then a genuinely polite close so a manager
lets it stand. The punch lands at the end: "slowest first".
"""

import os

# The entry itself: one line, honesty up front, politeness at the close.
PARTS = [
    "I'm out until Monday and won't check email. ",
    "Your message joins 214 unread emails I'll answer in order of dread, ",
    "slowest first. Thank you for understanding.",
]
ENTRY = "".join(PARTS)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert len(ENTRY) <= 200, "entry exceeds 200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
