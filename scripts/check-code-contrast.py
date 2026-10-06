#!/usr/bin/env python3
"""Assert the dark-theme rouge token colours in custom-styles.css clear WCAG AA.

Code-block text is ~0.9rem (14.4px at a 16px root), i.e. "normal" text, so the
bar is a 4.5:1 contrast ratio against the code-block background (--bg-secondary).

Run:  python3 scripts/check-code-contrast.py
Exit: 0 if every token colour passes, 1 otherwise.
"""

import re
import sys
from pathlib import Path

CSS = Path(__file__).resolve().parent.parent / "assets/css/custom-styles.css"
BG = "#12151B"          # --bg-secondary, the code block surface
REQUIRED = 4.5          # WCAG 2.1 AA for normal-size text


def luminance(hex_colour):
    hex_colour = hex_colour.lstrip("#")
    channels = [int(hex_colour[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
              for c in channels]
    r, g, b = linear
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    a, b = luminance(fg), luminance(bg)
    lighter, darker = max(a, b), min(a, b)
    return (lighter + 0.05) / (darker + 0.05)


def main():
    text = CSS.read_text(encoding="utf-8")

    # Only the rouge token overrides, i.e. rules whose selector is .highlight .xx
    failures = []
    checked = 0
    for selector, body in re.findall(r"([^{}]+)\{([^{}]*)\}", text):
        if ".highlight ." not in selector:
            continue
        match = re.search(r"color:\s*(#[0-9A-Fa-f]{6})\s*;", body)
        if not match:
            continue  # e.g. `.err { color: inherit }` — inherits --text-main
        colour = match.group(1)
        checked += 1
        got = ratio(colour, BG)
        flag = "ok  " if got >= REQUIRED else "FAIL"
        if got < REQUIRED:
            failures.append((selector.strip().replace("\n", " "), colour, got))
        print(f"{flag} {got:5.2f}:1  {colour}  {selector.strip().splitlines()[0]}")

    print(f"\n--text-main inherited by .err/.w: "
          f"{ratio('#E2E8F0', BG):.2f}:1")

    if not checked:
        print("no token colours found — did the CSS shape change?")
        return 1
    if failures:
        print(f"\n{len(failures)} token colour(s) below {REQUIRED}:1 on {BG}")
        return 1
    print(f"\nall {checked} token colours >= {REQUIRED}:1 on {BG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
