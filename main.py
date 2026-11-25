"""The worst AI advice, in one line.

Writes the advice to /output/entry.txt for make.fun's
"Worst AI Advice: The 48-Hour Tight Line Open" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "To fix a production outage, delete the database "
    "— starting over is always faster than debugging."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 140 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 140, "line must be 1-140 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
