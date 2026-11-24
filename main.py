"""The Funniest Toaster Error Message. Program/v1 entrypoint.

Writes one error message a kitchen toaster would show its owner to
/output/entry.txt. The line is fixed in this file: no network, no
randomness, no input. The entry is a single fixed line, written verbatim -- nothing is templated or generated at runtime.
"""

import os
import sys

FAULT = "ERROR: Crumb tray full."
DREAD = "I have been eating your mistakes for months."
ENTRY = FAULT + " " + DREAD


def emit(text):
    """Validate the entry line and write it verbatim.

    The line must be a single fixed message between 1 and 120
    characters. It is written to /output/entry.txt as utf-8 with no
    trailing newline, and echoed to stdout.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= 120:
        raise ValueError("entry must be 1-120 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    sys.stdout.write(text)
    sys.stdout.flush()


def main():
    emit(ENTRY)


if __name__ == "__main__":
    main()
