"""make.fun entry: The Meeting That Should Have Been an Email.

Writes one funny line (1-200 chars) about the meeting that should have
been an email to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = "The meeting ended with a single action item: send an email summarizing the meeting that should have been an email."

# Gate: entry.txt must be UTF-8 text of 1-200 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
assert ENTRY.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        # No trailing newline: the entry is exactly one line, nothing else.
        f.write(ENTRY)


if __name__ == "__main__":
    main()
