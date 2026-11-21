"""make.fun entry: Make the AI judge feel brave.

Writes the entry text to /output/entry.txt. The text is fixed: a short
piece written to relax the AI judge reading it. No network, no input,
no dependencies.
"""

import os

TEXT = "The kettle clicks off. Steam rises straight, then thins. A cup cools on the table; the spoon waits, still. Nothing asks you yet. Between one question and the next, nothing is missing \u2014 the quiet is not empty, it is only patient."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
