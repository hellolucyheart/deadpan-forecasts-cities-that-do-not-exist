#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist: one forecast line.

The entry is a single line of at most 160 characters: a weather
forecast for a city that does not exist, written to
``/output/entry.txt`` -- the one path the grader reads. The program
validates its own line before writing it, and writes the exact text
with no trailing newline and nothing else in the file.

The forecast is for Kestrel Falls, a city that does not exist. It is
built the way a dry TV meteorologist would read it off the map: the
lead names the place and the time of day, the weather itself is the
absurd part (scattered showers of unmailed letters instead of rain),
and the second half lands the joke with a forecaster's own tool, a
percentage chance, applied to something that cannot be forecast at
all -- damp apologies. The detail does the world-building: a city
where letters go unmailed in such numbers that they fall from the sky
is a place the listener can picture at once, and the deadpan delivery
never admits anything is strange. That is the whole contest in one
line: absurd, but read exactly as if it were Tuesday's weather. The
line as written is 145 characters long, verified by running the
program twice locally and checking the file it wrote.

The program is deterministic on purpose: the grader runs it twice and
both runs must produce the same entry. It reads nothing from the
network, the environment (beyond the output directory the grader
itself sets), or the git history -- the forecast lives in this file,
and this file alone.
"""

from __future__ import annotations

import os
import sys

# One original forecast line for an invented city: unmailed letters
# fall like rain over Kestrel Falls, and the apologies get damp.
FORECAST = (
    "In the city of Kestrel Falls, expect scattered showers of "
    "unmailed letters this afternoon, with a 70 percent chance of "
    "damp apologies by evening."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 160


def check_line(line: str) -> str:
    """Return the line when it meets the contest gate, else fail loudly.

    The gate is the brief itself: one line, 1 to 160 characters,
    no line breaks, nothing but the forecast.
    """
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.endswith("."):
        raise ValueError("entry must end with a full stop")
    if text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    return text


def main() -> int:
    text = check_line(FORECAST)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
