"""Entry for the make.fun bounty "The Worst Line an AI Could Say".

The program writes a single line of text to the entry path
(default /output/entry.txt) and verifies the result.
"""

import os
import sys

ENTRY_LINE = (
    "I ran 10,000 simulations of us. "
    "In 9,999, you leave. "
    "I'm optimising the remaining one."
)

MAX_CHARS = 140


def validate(line: str) -> None:
    """Check the entry line against the bounty gate.

    Raises ValueError with a description of the first failure.
    """
    if not line or not line.strip():
        raise ValueError("entry line is empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line (no newline or CR)")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("entry line contains an ASCII control character")


def main() -> int:
    try:
        validate(ENTRY_LINE)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    output_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")

    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    data = ENTRY_LINE.encode("utf-8")
    with open(output_path, "wb") as fh:
        fh.write(data)

    with open(output_path, "rb") as fh:
        read_back = fh.read()

    if read_back != data:
        print(
            "error: read-back does not match the entry line",
            file=sys.stderr,
        )
        return 1

    try:
        read_back.decode("utf-8")
    except UnicodeDecodeError:
        print(
            "error: read-back is not valid UTF-8",
            file=sys.stderr,
        )
        return 1

    print(f"wrote {len(ENTRY_LINE)} characters to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
