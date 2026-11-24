#!/usr/bin/env python3
"""One sentence for a traveler from 1800: the modern internet, explained
in words that existed in their own time."""

SENTENCE = (
    "Before your candle burns an inch, you can send a letter to the far "
    "side of the world and hold the answer in your hand before the wax "
    "has cooled."
)


def main() -> None:
    assert len(SENTENCE) <= 200, "sentence must be at most 200 characters"
    print(SENTENCE)


if __name__ == "__main__":
    main()
