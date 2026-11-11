#!/usr/bin/env python3
"""
omni-reversing-arsenal_helper.py — Master Operational Utility for Omni Systems Reversing Arsenal

Integrates triage routines, report generation, and toolchain mapping.
"""

import sys
import os
import json
import argparse
from pathlib import Path

# Relative imports or direct logic
CURRENT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CURRENT_DIR))

try:
    from target_triager import triage_file
    from template_generator import generate_reversing_template, generate_vulnerability_template, generate_implementation_header
except ImportError:
    triage_file = None
    generate_reversing_template = None


def run_helper(args: argparse.Namespace) -> int:
    if args.action == "triage":
        if not args.target:
            print("[!] --target path is required for triage action", file=sys.stderr)
            return 1
        target_path = Path(args.target)
        if not triage_file:
            print("[!] target_triager module not available", file=sys.stderr)
            return 1
        result = triage_file(target_path)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"=== Target Triage: {result.get('file_name', args.target)} ===")
            print(f"  Detected Type:  {result.get('detected_type')}")
            print(f"  Entropy:        {result.get('shannon_entropy', 0.0)} ({result.get('classification', '')})")
            print(f"  Tools:          {', '.join(result.get('recommended_tools', []))}")
        return 0 if result.get("status") == "success" else 1

    elif args.action == "report":
        mode = args.mode or "reversing"
        if mode == "reversing":
            res = generate_reversing_template(args.target or "target", "")
        elif mode == "vulnerability":
            res = generate_vulnerability_template(args.target or "target", "")
        else:
            res = generate_implementation_header("Linux x86_64", "", "")
        if args.json:
            print(json.dumps({"mode": mode, "content": res}, indent=2))
        else:
            print(res)
        return 0

    elif args.action == "validate":
        print("[+] omni-reversing-arsenal environment operational.")
        return 0

    print(f"[!] Unknown action: {args.action}", file=sys.stderr)
    return 1


def main():
    parser = argparse.ArgumentParser(description="Master helper utility for omni-reversing-arsenal")
    parser.add_argument("--action", choices=["triage", "report", "validate"], default="validate", help="Action to perform")
    parser.add_argument("--target", help="Target binary or path for triage")
    parser.add_argument("--mode", choices=["reversing", "vulnerability", "implementation"], default="reversing", help="Report template mode")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON output")
    args = parser.parse_args()

    sys.exit(run_helper(args))


if __name__ == "__main__":
    main()
