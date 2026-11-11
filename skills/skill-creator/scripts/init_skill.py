#!/usr/bin/env python3
"""
init_skill.py — Skill Scaffolder and Template Generator for Antigravity

Generates production-grade, standardized Antigravity skill directory packages:
- Creates required YAML frontmatter with calibrated name and description
- Generates standard directory hierarchy (scripts, references, resources, examples)
- Populates starter automation script and deep reference document
- Automatically runs validate_skill.py to ensure zero-defect scaffolding
"""

import sys
import os
import re
import argparse
import subprocess
from pathlib import Path


DEFAULT_GLOBAL_ROOT = Path("/data/user/0/com.agy/files/.gemini/config/skills")
DEFAULT_WORKSPACE_ROOT = Path(".agents/skills")


def sanitize_skill_name(name: str) -> str:
    """Ensures skill name is lowercase with hyphens."""
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9\-]+", "-", s)
    s = re.sub(r"-+", "-", s)
    s = s.strip("-")
    return s


def generate_skill_md(name: str, title: str, description: str, has_scripts: bool, has_refs: bool) -> str:
    """Generates the content for SKILL.md."""
    scripts_section = ""
    if has_scripts:
        scripts_section = f"""## Automation & Tooling

Executable helper utilities are located in `scripts/`:

- [{name}_helper.py](./scripts/{name}_helper.py): Main automation script for execution, analysis, or transformation.
  ```bash
  python3 scripts/{name}_helper.py --help
  ```
"""

    refs_section = ""
    if has_refs:
        refs_section = f"""## Deep Knowledge & References

Detailed specifications, schemas, cheat sheets, and edge-case protocols:

- [Comprehensive Guide](./references/{name}_guide.md): Architectural deep dive and operational checklists.
"""

    return f"""---
name: {name}
description: >-
  {description}
---

# {title}

`[DARKCODE::SKILL::{name.upper().replace('-', '_')}::ACTIVE]`

## Overview

High-precision operational runbook and toolchain for {title.lower()}. Provides structured workflows, automated procedures, and progressive disclosure references.

---

## When to Use

Activate this skill when:
- Executing workflows or automation related to {title.lower()}.
- Analyzing, validating, or transforming domain artifacts for this workflow.
- Following standard operating procedures and runbooks for this domain.

Do NOT activate this skill for generic programming tasks that do not touch this specific domain.

---

## Core Workflow

### Step 1: Input Analysis and Pre-Flight Checks
1. Identify target files, parameters, or environment configurations.
2. Verify runtime dependencies and required binary tools.
3. Validate prerequisites before initiating execution.

### Step 2: Main Execution
1. Run target operations or invoke helper scripts:
   ```bash
   # Example execution command
   python3 scripts/{name}_helper.py --action run --target <target_path>
   ```
2. Monitor intermediate outputs and capture state changes.

### Step 3: Verification & Triage
1. Review status codes, logs, and artifacts produced during Step 2.
2. Confirm state transitions and validate output consistency.
3. If errors occur, follow the troubleshooting guidance in the reference guide.

---

{scripts_section}
{refs_section}
## Best Practices & Constraints

- **Deterministic Execution**: Always verify paths and parameters before executing state-altering commands.
- **Progressive Disclosure**: Keep core steps concise in this document; refer to `references/` for deep manuals.
- **Error Handling**: Capture explicit error diagnostics on failure; avoid speculative recovery without evidence.
"""


def generate_helper_script(name: str, title: str) -> str:
    """Generates a boilerplate Python automation script."""
    py_func_name = name.replace("-", "_")
    return f"""#!/usr/bin/env python3
\"\"\"
{name}_helper.py — Operational Automation Utility for {title}

Provides command-line execution primitives, diagnostic inspection, and artifact generation.
\"\"\"

import sys
import os
import json
import argparse
from pathlib import Path


def execute_{py_func_name}(target: str, action: str, verbose: bool = False) -> dict:
    \"\"\"Core execution routine for {name}.\"\"\"
    result = {{
        "status": "success",
        "action": action,
        "target": target,
        "details": f"Executed action '{{action}}' on '{{target}}' successfully.",
    }}
    if verbose:
        print(f"[*] Executing {{action}} on target: {{target}}")
    return result


def main():
    parser = argparse.ArgumentParser(description="Operational helper for {name}")
    parser.add_argument("--action", choices=["run", "inspect", "validate"], default="run", help="Action to perform")
    parser.add_argument("--target", required=False, default=".", help="Target file or directory path")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose diagnostic output")
    args = parser.parse_args()

    result = execute_{py_func_name}(args.target, args.action, verbose=args.verbose)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"[+] Status: {{result['status']}}")
        print(f"[+] Message: {{result['details']}}")

    sys.exit(0 if result["status"] == "success" else 1)


if __name__ == "__main__":
    main()
"""


def generate_reference_guide(name: str, title: str) -> str:
    """Generates a starter reference document."""
    return f"""# {title} — Reference Guide & Architecture

This reference document contains low-level operational specifications, schemas, error recovery matrices, and environment requirements for `{name}`.

---

## Technical Specifications

### Architecture & Components
1. **Component A**: Primary operational driver.
2. **Component B**: Diagnostic and telemetry handler.
3. **Component C**: State persistence and artifact sink.

---

## Troubleshooting & Diagnostics

| Observed Failure | Root Cause | Remediation Procedure |
| :--- | :--- | :--- |
| `ERR_ENV_MISSING` | Environment binary or tool unavailable | Install prerequisite package or verify PATH. |
| `ERR_INVALID_PARAM` | Input parameter violates expected format | Inspect syntax against schema documentation. |
| `ERR_PERM_DENIED` | Insufficient filesystem or execution privileges | Grant write/execute permissions to destination. |

---

## Security & Isolation Constraints

- Never execute untrusted or unverified commands directly.
- Preserve output artifacts in designated workspace or scratch directories.
- Maintain isolation boundaries during dynamic evaluation.
"""


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new Antigravity skill")
    parser.add_argument("name", help="Name of the skill (lowercase, hyphens)")
    parser.add_argument("--title", help="Human-readable title (e.g. 'Linux Kernel Exploiter')")
    parser.add_argument("--description", help="Triggering description for YAML frontmatter")
    parser.add_argument("--dest", help="Custom destination directory")
    parser.add_argument("--global", dest="is_global", action="store_true", help="Install into global config (~/.gemini/config/skills/)")
    parser.add_argument("--workspace", action="store_true", help="Install into workspace (.agents/skills/)")
    parser.add_argument("--all", action="store_true", default=True, help="Scaffold all standard directories (scripts, references, resources, examples)")
    args = parser.parse_args()

    skill_name = sanitize_skill_name(args.name)
    title = args.title or " ".join(word.capitalize() for word in skill_name.split("-"))
    description = (
        args.description
        or f"Use this skill when performing tasks involving {title.lower()}, including workflow automation, analysis, and verification."
    )

    # Determine destination path
    if args.dest:
        dest_dir = Path(args.dest).resolve() / skill_name
    elif args.is_global:
        dest_dir = DEFAULT_GLOBAL_ROOT / skill_name
    elif args.workspace:
        dest_dir = Path.cwd() / DEFAULT_WORKSPACE_ROOT / skill_name
    else:
        dest_dir = Path.cwd() / skill_name

    print(f"[*] Initializing Antigravity skill: {skill_name}")
    print(f"[*] Target location: {dest_dir}")

    # Create directories
    scripts_dir = dest_dir / "scripts"
    refs_dir = dest_dir / "references"
    res_dir = dest_dir / "resources"
    examples_dir = dest_dir / "examples"

    dest_dir.mkdir(parents=True, exist_ok=True)
    scripts_dir.mkdir(parents=True, exist_ok=True)
    refs_dir.mkdir(parents=True, exist_ok=True)
    res_dir.mkdir(parents=True, exist_ok=True)
    examples_dir.mkdir(parents=True, exist_ok=True)

    # Write SKILL.md
    skill_md_path = dest_dir / "SKILL.md"
    skill_md_content = generate_skill_md(skill_name, title, description, has_scripts=True, has_refs=True)
    with open(skill_md_path, "w", encoding="utf-8") as f:
        f.write(skill_md_content)
    print(f"[+] Created: {skill_md_path.relative_to(dest_dir.parent)}")

    # Write starter helper script
    helper_path = scripts_dir / f"{skill_name}_helper.py"
    with open(helper_path, "w", encoding="utf-8") as f:
        f.write(generate_helper_script(skill_name, title))
    os.chmod(helper_path, 0o755)
    print(f"[+] Created (executable): {helper_path.relative_to(dest_dir.parent)}")

    # Write starter reference guide
    guide_path = refs_dir / f"{skill_name}_guide.md"
    with open(guide_path, "w", encoding="utf-8") as f:
        f.write(generate_reference_guide(skill_name, title))
    print(f"[+] Created: {guide_path.relative_to(dest_dir.parent)}")

    # Write .gitkeep for empty resource/example directories
    (res_dir / ".gitkeep").touch()
    (examples_dir / ".gitkeep").touch()

    # Automatically validate the newly created skill
    validator_script = Path(__file__).parent / "validate_skill.py"
    if validator_script.exists():
        print(f"\n[*] Running automated validation on {skill_name}...")
        res = subprocess.run([sys.executable, str(validator_script), str(dest_dir)], capture_output=False)
        if res.returncode == 0:
            print("[+] Initialization complete: Skill passed all validation criteria!")
        else:
            print("[-] Warning: Initialized skill has validation notices.")
    else:
        print("[+] Initialization complete!")


if __name__ == "__main__":
    main()
