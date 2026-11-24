"""A toaster that has finally had enough of the crumbs.

This program produces a single fixed error line from an overworked
toaster, writes it to the entry file, and echoes it to stdout.
The text never changes, no matter how often the program runs.
"""

import os


TOASTER_ERROR = "ERROR: Crumb tray full. I have been eating your mistakes for months."

OUTPUT_PATH = "/output/entry.txt"


def build_message():
    """Return the toaster's complaint, unchanged."""
    return TOASTER_ERROR


def write_entry(path, message):
    """Write the message to path with no trailing newline."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(message)


def main():
    message = build_message()
    write_entry(OUTPUT_PATH, message)
    print(message, end="")


if __name__ == "__main__":
    main()
