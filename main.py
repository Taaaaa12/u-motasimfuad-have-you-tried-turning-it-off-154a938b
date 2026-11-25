#!/usr/bin/env python3
"""Have You Tried Turning It Off? - make.fun program/v1 entry.

Writes one funny line from a hopeless tech support agent to a
desperate customer to /output/entry.txt. Fully deterministic:
no network, no randomness, no clock, no environment input -
the same line on every run, so the two grading runs agree.
"""

import os

LINE = (
    "Have you tried turning it off and on again? Lovely \u2014 now unplug it, "
    "count to ten, and plug it back in slowly, like we\u2019re defusing a bomb together."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
