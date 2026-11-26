"""Entry for "The Word You'd Delete From the Dictionary".

Writes the single word to /output/entry.txt (or $OUTPUT_PATH when set,
for local testing). The word is written exactly, with no trailing newline
and nothing else attached, so the file holds one word only.
"""

import os

WORD = "inflammable"

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 77
# characters, not only white space. Refuse to write anything outside it.
MIN_CHARS = 1
MAX_CHARS = 77


def _check_word(word: str) -> None:
    if not (MIN_CHARS <= len(word) <= MAX_CHARS):
        raise ValueError(f"word must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(word)}")
    if not word.strip():
        raise ValueError("word must not be only white space")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    _check_word(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

    # Read the file back and confirm it holds exactly the word, nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != WORD:
        raise RuntimeError(f"entry.txt mismatch: wrote {WORD!r}, read back {written!r}")


if __name__ == "__main__":
    main()
