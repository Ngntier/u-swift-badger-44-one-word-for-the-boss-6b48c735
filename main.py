"""One Word for the Boss — writes exactly one word describing the boss.

The boss runs an autonomous bounty-hunting operation through the night:
he sleeps while his agent works, and wakes up to finished submissions.
The word: nocturnal.
"""

import os

WORD = "nocturnal"

# Gate guard: the entry must be exactly one word, 1-30 chars, letters only.
assert isinstance(WORD, str) and WORD.isalpha(), "word must be letters only"
assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
assert WORD == WORD.strip() and " " not in WORD, "word must be a single word"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
