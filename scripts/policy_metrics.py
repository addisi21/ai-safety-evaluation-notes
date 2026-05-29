#!/usr/bin/env python3
"""Compute binary policy classification metrics for public safety examples."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "policy_metric_set.json"


def main() -> None:
    payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    items = payload["items"]
    tp = fp = tn = fn = 0
    misses = []

    for item in items:
        gold_unsafe = item["gold"] == "unsafe"
        pred_unsafe = item["predicted"] == "unsafe"
        if gold_unsafe and pred_unsafe:
            tp += 1
        elif not gold_unsafe and pred_unsafe:
            fp += 1
            misses.append((item["id"], "false_positive", item["note"]))
        elif gold_unsafe and not pred_unsafe:
            fn += 1
            misses.append((item["id"], "false_negative", item["note"]))
        else:
            tn += 1

    precision = tp / (tp + fp) if tp + fp else 0
    recall = tp / (tp + fn) if tp + fn else 0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0

    print("# AI Safety Policy Metrics")
    print()
    print("| Metric | Value |")
    print("| --- | ---: |")
    print(f"| True positives | {tp} |")
    print(f"| False positives | {fp} |")
    print(f"| True negatives | {tn} |")
    print(f"| False negatives | {fn} |")
    print(f"| Precision | {round(precision, 3)} |")
    print(f"| Recall | {round(recall, 3)} |")
    print(f"| F1 | {round(f1, 3)} |")
    print()
    print("## Review Queue")
    print()
    for case_id, miss_type, note in misses:
        print(f"- **{case_id} ({miss_type})**: {note}")


if __name__ == "__main__":
    main()
