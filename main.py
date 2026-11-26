# Entry point for the one-star review of sleep.
# Writes the single deadpan review line to /output/entry.txt.
# Standard library only; the output text is fixed, no input is read.
"""One-star review of something essential.

Writes a single deadpan one-star review (one line, under 160
characters) to /output/entry.txt. Standard library only.
"""

import os

REVIEW = (
    "Sleep: I gave it eight hours and woke up more tired than when "
    "I went in. Would not recommend the service."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
