"""Write one office-life joke to /output/entry.txt.

Deterministic: a single fixed joke, no randomness, no time, no network,
no environment reads. Standard library only.
"""

import os

JOKE = "I blocked focus time on my calendar so my meetings would finally have somewhere to meet."


def main() -> None:
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
