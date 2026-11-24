import os

# The entry is one line: the funniest error message a kitchen toaster
# would show its owner. Deadpan appliance voice, one real fault state
# (a full crumb tray) with a fresh turn — the toaster has been quietly
# eating the owner's mistakes for months. 68 characters, no trailing
# newline, so the file holds exactly the line the judge reads.
ENTRY = "ERROR: Crumb tray full. I have been eating your mistakes for months."


def main() -> str:
    text = ENTRY
    # The gate: UTF-8 text of 1 to 120 characters, not only white space.
    assert 1 <= len(text) <= 120, f"entry is {len(text)} chars, must be 1-120"
    assert text.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    return text


if __name__ == "__main__":
    print(main())
