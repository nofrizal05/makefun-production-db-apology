"""The Production Database Apology — a make.fun entry.

Writes one funny one-line apology for dropping the production
database to /output/entry.txt.

Imports (Python standard library only):
- os: to create the output directory.
"""

import os

APOLOGY = (
    "Sorry I dropped the production database — the backup was only a rumor, "
    "and the tables left without saying goodbye."
)

TITLE = "The Backup Was Only a Rumor"


def main() -> None:
    """Write the apology line to /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(APOLOGY + "\n")


if __name__ == "__main__":
    main()
