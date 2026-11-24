"""The Funniest Toaster Error Message. Program/v1 entrypoint. Writes one error message a kitchen toaster would show its owner to /output/entry.txt. The line is fixed in this file: no network, no randomness, no input. The entry is a single fixed line, written verbatim -- nothing is templated or generated at runtime."""

import os
import sys

FAULT = "ERROR: Crumb tray full."
DREAD = "I have been eating your mistakes for months."
ENTRY = FAULT + " " + DREAD


def emit(text):
    if not isinstance(text, str) or not 1 <= len(text) <= 120:
        raise ValueError("entry must be 1-120 chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    sys.stdout.write(text)


def main():
    emit(ENTRY)


if __name__ == "__main__":
    main()
