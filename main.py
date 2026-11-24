"""The funniest error message a kitchen toaster would show its owner.

Deadpan appliance voice, one real fault state (a full crumb tray) with a
fresh turn — the toaster has been quietly eating the owner's mistakes
for months. The entry is a single fixed line: 68 characters, no trailing
newline, so /output/entry.txt holds exactly the line the judge reads.
The entry is fixed text, never generated per run: the same single line
every time, so the output is byte-identical on every invocation.
"""
import os
import sys

FAULT = "ERROR: Crumb tray full."
DREAD = "I have been eating your mistakes for months."
ENTRY = FAULT + " " + DREAD


def emit(text: str) -> str:
    """Validate the entry, write it to /output/entry.txt, and print it."""
    # The gate: UTF-8 text of 1 to 120 characters, not only white space.
    assert 1 <= len(text) <= 120, f"entry is {len(text)} chars, must be 1-120"
    assert text.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    sys.stdout.write(text)
    return text


def main() -> str:
    return emit(ENTRY)


if __name__ == "__main__":
    main()
