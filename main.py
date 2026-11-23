"""Write one office-life joke to /output/entry.txt.

Deterministic: a single fixed joke, no randomness, no time, no network,
no environment reads. Standard library only.
"""

import os

JOKE = "I blocked focus time on my calendar so my meetings would finally have somewhere to meet."

# Scorer rule: the joke must be a single line of 1-199 characters (Unicode
# code points), not only whitespace, and contain no newline.
MIN_JOKE_LEN = 1
MAX_JOKE_LEN = 199


def main() -> None:
    assert MIN_JOKE_LEN <= len(JOKE) <= MAX_JOKE_LEN, "joke must be 1-199 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
