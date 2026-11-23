"""One Line, Zero Use: The Useless Superpower Sprint.

Writes the entry line (a hilariously useless superpower, at most
200 characters) to /output/entry.txt and prints it.

Pure Python 3 standard library only. Deterministic. No network.
"""

import os

LINE = "I can stop time \u2014 but only for three seconds, only once a day, and only while I'm sneezing."

OUTPUT_PATH = "/output/entry.txt"


def main() -> str:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(
            f"LINE must be 1..200 characters, got {len(LINE)}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    return LINE


if __name__ == "__main__":
    main()
