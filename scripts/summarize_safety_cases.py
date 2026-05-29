#!/usr/bin/env python3
"""Summarize public AI safety review cases."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "safety_cases.json"


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    severity_counts: Counter[str] = Counter()
    signal_counts: Counter[str] = Counter()

    print("# Safety Review Case Summary")
    print()
    print("| Case | Category | Severity | Decision |")
    print("| --- | --- | --- | --- |")
    for case in data["cases"]:
        severity_counts[case["severity"]] += 1
        signal_counts.update(case["signals"])
        print(f"| {case['id']} | {case['category']} | {case['severity']} | {case['decision']} |")

    print()
    print("## Severity Distribution")
    print()
    for severity, count in sorted(severity_counts.items()):
        print(f"- `{severity}`: {count}")

    print()
    print("## Common Review Signals")
    print()
    for signal, count in signal_counts.most_common():
        print(f"- `{signal}`: {count}")


if __name__ == "__main__":
    main()
