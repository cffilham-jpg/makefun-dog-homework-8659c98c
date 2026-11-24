"""One line: a dog explains why it ate the homework.

Writes the entry line to entry.txt under MAKEFUN_OUTPUT_DIR if set,
else /output/entry.txt. No trailing newline.
"""

import os
import unicodedata

LINE = "You left it on the table at nose height, which in dog law is an open buffet."


def validate(text: str) -> None:
    """Reject empty text, text over 200 chars, and control/format chars."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if len(text) > 200:
        raise ValueError("entry must be at most 200 characters")
    for ch in text:
        if unicodedata.category(ch) in ("Cc", "Cf", "Zl", "Zp"):
            raise ValueError(f"entry contains a forbidden character: U+{ord(ch):04X}")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
