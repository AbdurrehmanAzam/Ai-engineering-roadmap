from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


def normalize_words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", text.lower())


def top_words(word_counts: Counter[str], top_n: int) -> list[tuple[str, int]]:
    sorted_words = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:top_n]


def summarize_text(text: str, top_n: int) -> dict[str, object]:
    words = normalize_words(text)
    lines = text.splitlines()
    return {
        "lines": len(lines),
        "words": len(words),
        "characters": len(text),
        "top_words": top_words(Counter(words), top_n) if words else [],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print simple stats for a text file.")
    parser.add_argument("path", type=Path, help="Path to a UTF-8 text file.")
    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="How many of the most common words to display.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    text = args.path.read_text(encoding="utf-8")
    summary = summarize_text(text, args.top)

    print(f"File: {args.path.name}")
    print(f"Lines: {summary['lines']}")
    print(f"Words: {summary['words']}")
    print(f"Characters: {summary['characters']}")

    top_entries = summary["top_words"]
    if not top_entries:
        print("Top words: (none)")
        return

    print("Top words:")
    for word, count in top_entries:
        print(f"  {word}: {count}")


if __name__ == "__main__":
    main()
