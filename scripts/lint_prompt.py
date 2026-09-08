#!/usr/bin/env python3
import argparse, re, sys
from pathlib import Path

BAD_PLACEHOLDERS = [
    "{VISIBLE_TEXT_RULE}",
    "[Paste the full Visual Schema here]",
    "[Insert extracted research context]",
    "---BEGIN PROMPT---",
    "---END PROMPT---",
]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("prompt")
    args = p.parse_args()
    text = Path(args.prompt).read_text(encoding="utf-8")
    errors = []

    if not (
        "All visible text in the figure must use only the following exact labels" in text
        or "图中所有可见文字只能使用以下内容" in text
    ):
        errors.append("Missing exact visible-text whitelist.")

    for token in BAD_PLACEHOLDERS:
        if token in text:
            errors.append(f"Unresolved placeholder/scaffold: {token}")

    risky = ["fake microscopy", "invent p-value", "fabricate data"]
    # These are not automatically errors if they occur in a prohibition.
    # Report only as review hints.
    hints = [x for x in risky if x in text.lower()]

    if errors:
        print("FAIL")
        for e in errors:
            print("-", e)
        return 1
    print("PASS")
    if hints:
        print("Review terms:", ", ".join(hints))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
