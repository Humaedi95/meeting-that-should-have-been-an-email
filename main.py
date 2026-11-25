"""The Meeting That Should Have Been an Email.

Writes the one-line joke entry to /output/entry.txt.
"""

import os

JOKE = "We spent 45 minutes in a meeting deciding it could've been an email — then booked a follow-up to discuss the email."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
