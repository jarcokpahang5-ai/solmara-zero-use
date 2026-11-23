"""One Line, Zero Use: The Useless Superpower Sprint.

Writes the entry line (a hilariously useless superpower, at most
200 characters) to /output/entry.txt and prints it.

Pure Python 3 standard library only. Deterministic. No network.
"""

import os

LINE = "I can freeze time for three seconds a day \u2014 but only while I'm sneezing, so I've never actually used it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> str:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(
            f"LINE must be a single line of 1..200 characters, "
            f"got {len(LINE)} characters: {LINE!r}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    return LINE


if __name__ == "__main__":
    main()
