#!/usr/bin/env python3
"""Write one sentence on the best advice I ever got to /output/entry.txt."""

import os

ENTRY = (
    "The summer I failed my exams and blamed everyone, my dad said "
    "nobody owes you a fair day, so stop waiting for one and go make your own."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
