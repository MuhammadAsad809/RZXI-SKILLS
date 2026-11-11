#!/usr/bin/env python3
"""
runner.py — Demonstration helper utility for deep-tool-skill
"""

import sys
import math
import json
import argparse
from pathlib import Path


def calculate_entropy(file_path: Path) -> float:
    """Calculates Shannon entropy of the file bytes."""
    if not file_path.exists():
        raise FileNotFoundError(f"Target '{file_path}' does not exist.")

    with open(file_path, "rb") as f:
        data = f.read()

    if not data:
        return 0.0

    entropy = 0.0
    total = len(data)
    byte_counts = [0] * 256
    for b in data:
        byte_counts[b] += 1

    for count in byte_counts:
        if count > 0:
            p_x = count / total
            entropy -= p_x * math.log2(p_x)

    return round(entropy, 4)


def main():
    parser = argparse.ArgumentParser(description="Deep tool demonstration runner")
    parser.add_argument("--action", choices=["analyze", "verify"], default="analyze")
    parser.add_argument("--target", required=True, help="Target file path")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    args = parser.parse_args()

    try:
        entropy = calculate_entropy(Path(args.target))
        res = {
            "status": "success",
            "target": args.target,
            "entropy": entropy,
            "is_packed": entropy > 7.2,
        }
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print(f"[+] Target: {args.target}")
            print(f"[+] Shannon Entropy: {entropy}")
            print(f"[+] Packed: {res['is_packed']}")
        sys.exit(0)
    except Exception as e:
        if args.json:
            print(json.dumps({"status": "error", "error": str(e)}))
        else:
            print(f"[-] Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
