---
name: deep-tool-skill
description: >-
  Use this skill when the user asks to analyze binary entropy, inspect executable sections,
  or perform deep artifact inspection using runner.py. Demonstrates progressive disclosure
  and helper script integration.
---

# Deep Tool Skill

`[DARKCODE::EXAMPLE::DEEP_TOOL]`

## Overview

Reference implementation of a full-featured Antigravity skill demonstrating the progressive disclosure architecture, encapsulated Python automation, and secondary technical documentation.

---

## When to Use

Activate when:
- Analyzing byte entropy or packed code blocks in binary targets.
- Verifying the multi-file architecture of an Antigravity skill.

Do NOT activate for plain text file editing.

---

## Operational Runbook

### Step 1: Run Entropy Analysis
```bash
python3 scripts/runner.py --action analyze --target <binary_path> --json
```

### Step 2: Diagnostic Verification
Check the `entropy` score in the JSON output:
- Entropy $> 7.2$: Probable packed/encrypted payload.
- Entropy $< 6.0$: Standard uncompressed executable text.

---

## Tooling & Automation

- [runner.py](./scripts/runner.py): Binary inspection and entropy calculation tool.

---

## Reference Manuals

- [API & Metric Guide](./references/api-guide.md): Detailed entropy mathematics and section thresholds.
