#!/usr/bin/env python3
"""
validate_skill.py — Autonomous Skill Linter and Validation Engine for Antigravity

Validates Antigravity skill directories against specification standards:
- YAML Frontmatter presence, syntax, and schema (name, description)
- Skill naming conventions (lowercase, alphanumeric, hyphens)
- Trigger phrasing and semantic routing description quality
- Progressive disclosure rules and size limits
- Internal link integrity (references, scripts, resources)
- Python / Bash script syntax and executability
- JSON output support for machine consumption by AI agents
"""

import sys
import os
import re
import ast
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional


class SkillValidator:
    def __init__(self, skill_dir: Path, strict: bool = False):
        self.skill_dir = skill_dir.resolve()
        self.skill_md = self.skill_dir / "SKILL.md"
        self.strict = strict
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
        self.frontmatter: Dict[str, Any] = {}

    def parse_frontmatter(self, content: str) -> Optional[Dict[str, Any]]:
        """Parses YAML frontmatter using pure standard library parser."""
        lines = content.splitlines()
        if not lines or lines[0].strip() != "---":
            self.errors.append("SKILL.md must start with '---' on line 1.")
            return None

        end_idx = -1
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                end_idx = i
                break

        if end_idx == -1:
            self.errors.append("SKILL.md has an unclosed frontmatter block (missing terminating '---').")
            return None

        fm_lines = lines[1:end_idx]
        data: Dict[str, Any] = {}
        curr_key: Optional[str] = None
        curr_multiline: List[str] = []
        in_multiline = False

        for line in fm_lines:
            raw_line = line
            stripped = line.strip()

            if not stripped or stripped.startswith("#"):
                continue

            # Check if this line is part of a multiline scalar
            if in_multiline:
                if line.startswith("  ") or line.startswith("\t"):
                    curr_multiline.append(stripped)
                    continue
                else:
                    # Multiline ended
                    if curr_key:
                        data[curr_key] = " ".join(curr_multiline).strip()
                    curr_key = None
                    curr_multiline = []
                    in_multiline = False

            # Check for key: value
            match = re.match(r"^([a-zA-Z0-9_\-]+)\s*:\s*(.*)$", line)
            if match:
                key = match.group(1).strip()
                val = match.group(2).strip()

                if val in (">-", ">", "|", "|-"):
                    curr_key = key
                    in_multiline = True
                    curr_multiline = []
                elif (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                    data[key] = val[1:-1]
                else:
                    data[key] = val
            elif in_multiline:
                curr_multiline.append(stripped)

        if in_multiline and curr_key:
            data[curr_key] = " ".join(curr_multiline).strip()

        return data

    def validate_frontmatter(self) -> None:
        """Validates frontmatter keys, naming, and description quality."""
        if not self.frontmatter:
            return

        # Check 'name'
        if "name" not in self.frontmatter or not self.frontmatter["name"]:
            self.errors.append("Frontmatter is missing required 'name' field.")
        else:
            name = str(self.frontmatter["name"]).strip()
            if not re.match(r"^[a-z0-9][a-z0-9\-_]*[a-z0-9]$", name) and not re.match(r"^[a-z0-9]+$", name):
                self.errors.append(f"Skill name '{name}' must be lowercase alphanumeric with hyphens or underscores.")
            
            # Check consistency with folder name
            folder_name = self.skill_dir.name
            if name != folder_name:
                self.warnings.append(f"Skill name '{name}' does not match directory name '{folder_name}'.")

        # Check 'description'
        if "description" not in self.frontmatter or not self.frontmatter["description"]:
            self.errors.append("Frontmatter is missing required 'description' field.")
        else:
            desc = str(self.frontmatter["description"]).strip()
            length = len(desc)
            if length < 25:
                self.warnings.append(f"Description is very short ({length} chars). Recommend 50-300 chars for accurate semantic routing.")
            elif length > 1024:
                self.warnings.append(f"Description is unusually long ({length} chars). Consider concise routing triggers.")

            # Trigger phrasing check
            trigger_patterns = [
                r"\buse this skill\b",
                r"\bwhen to use\b",
                r"\bwhen the user\b",
                r"\bactivates when\b",
                r"\bfor tasks involving\b",
                r"\btrigger\b",
                r"\bexpert in\b",
            ]
            has_trigger = any(re.search(pat, desc, re.IGNORECASE) for pat in trigger_patterns)
            if not has_trigger:
                self.warnings.append(
                    "Description lacks clear activation criteria. Recommend including 'Use this skill when...' to guide agent selection."
                )

            # Avoid first-person phrasing
            if re.search(r"\b(I will|my goal|I can|as an AI)\b", desc, re.IGNORECASE):
                self.warnings.append("Description contains first-person phrasing ('I', 'my'). Use objective third-person instructions.")

    def validate_progressive_disclosure(self, content: str) -> None:
        """Verifies progressive disclosure rules (preventing massive single-file context bloat)."""
        lines = content.splitlines()
        line_count = len(lines)
        byte_count = len(content.encode("utf-8"))

        self.info.append(f"SKILL.md size: {line_count} lines, {byte_count} bytes.")

        ref_dir = self.skill_dir / "references"
        scripts_dir = self.skill_dir / "scripts"

        if line_count > 300 or byte_count > 20480:
            if not ref_dir.is_dir() or not any(ref_dir.iterdir()):
                self.warnings.append(
                    f"SKILL.md is long ({line_count} lines, {byte_count} bytes) but 'references/' directory is empty or missing. "
                    "Apply progressive disclosure by splitting detailed documentation into references/."
                )

    def validate_relative_links(self, file_path: Path, content: str) -> None:
        """Validates that all relative markdown links point to existing files."""
        # Strip fenced code blocks and inline code spans so examples are not parsed as active links
        clean_content = re.sub(r"```[\s\S]*?```", "", content)
        clean_content = re.sub(r"`[^`\n]+`", "", clean_content)

        # Regex to find markdown links: [text](path)
        pattern = r"\[([^\]]+)\]\(([^)]+)\)"
        for match in re.finditer(pattern, clean_content):
            link_target = match.group(2).strip()

            # Ignore absolute URLs, mailto, anchor-only links
            if re.match(r"^(https?:\/\/|mailto:|#)", link_target):
                continue

            # Strip in-page anchors: path/to/file#heading
            path_part = link_target.split("#")[0]
            if not path_part:
                continue

            # Resolve path relative to the file containing the link
            resolved = (file_path.parent / path_part).resolve()
            if not resolved.exists():
                self.errors.append(f"Broken relative link in '{file_path.name}': '{link_target}' -> target '{resolved}' does not exist.")

    def validate_scripts(self) -> None:
        """Validates syntax and permissions for scripts in scripts/ directory."""
        scripts_dir = self.skill_dir / "scripts"
        if not scripts_dir.is_dir():
            return

        for script_file in scripts_dir.rglob("*"):
            if not script_file.is_file():
                continue

            rel_path = script_file.relative_to(self.skill_dir)

            # Python files
            if script_file.suffix == ".py":
                try:
                    with open(script_file, "r", encoding="utf-8") as f:
                        code = f.read()
                    ast.parse(code, filename=str(script_file))
                    self.info.append(f"Python script syntax valid: {rel_path}")
                except SyntaxError as e:
                    self.errors.append(f"Syntax error in '{rel_path}' at line {e.lineno}: {e.msg}")
                except Exception as e:
                    self.errors.append(f"Failed to read/parse '{rel_path}': {e}")

            # Bash / Shell files
            elif script_file.suffix in (".sh", ".bash"):
                # Check executable bit
                if not os.access(script_file, os.X_OK):
                    self.warnings.append(f"Shell script '{rel_path}' is not marked executable (+x).")

    def run(self) -> Tuple[bool, Dict[str, Any]]:
        """Executes full validation suite."""
        if not self.skill_dir.is_dir():
            self.errors.append(f"Skill directory does not exist: {self.skill_dir}")
            return False, self.get_report()

        if not self.skill_md.is_file():
            self.errors.append(f"Missing required 'SKILL.md' in {self.skill_dir}")
            return False, self.get_report()

        try:
            with open(self.skill_md, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            self.errors.append(f"Could not read SKILL.md: {e}")
            return False, self.get_report()

        # Step 1: Frontmatter check
        self.frontmatter = self.parse_frontmatter(content) or {}
        self.validate_frontmatter()

        # Step 2: Progressive disclosure
        self.validate_progressive_disclosure(content)

        # Step 3: Link checking in SKILL.md
        self.validate_relative_links(self.skill_md, content)

        # Step 4: Link checking in references/*.md if present
        ref_dir = self.skill_dir / "references"
        if ref_dir.is_dir():
            for ref_file in ref_dir.rglob("*.md"):
                try:
                    with open(ref_file, "r", encoding="utf-8") as f:
                        ref_content = f.read()
                    self.validate_relative_links(ref_file, ref_content)
                except Exception as e:
                    self.warnings.append(f"Could not read reference file {ref_file.name}: {e}")

        # Step 5: Scripts check
        self.validate_scripts()

        success = len(self.errors) == 0
        if self.strict and len(self.warnings) > 0:
            success = False

        return success, self.get_report()

    def get_report(self) -> Dict[str, Any]:
        return {
            "skill": str(self.skill_dir),
            "valid": len(self.errors) == 0 and (not self.strict or len(self.warnings) == 0),
            "frontmatter": self.frontmatter,
            "errors": self.errors,
            "warnings": self.warnings,
            "info": self.info,
        }


def main():
    parser = argparse.ArgumentParser(description="Antigravity Skill Validator and Linter")
    parser.add_argument("path", help="Path to skill directory or SKILL.md")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    target_path = Path(args.path)
    if target_path.is_file() and target_path.name == "SKILL.md":
        target_dir = target_path.parent
    else:
        target_dir = target_path

    validator = SkillValidator(target_dir, strict=args.strict)
    success, report = validator.run()

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"\n========================================================")
        print(f" Antigravity Skill Validation: {target_dir.name}")
        print(f" Path: {target_dir}")
        print(f"========================================================")

        if report["errors"]:
            print(f"\n[!] ERRORS ({len(report['errors'])}):")
            for err in report["errors"]:
                print(f"  [-] {err}")

        if report["warnings"]:
            print(f"\n[*] WARNINGS ({len(report['warnings'])}):")
            for warn in report["warnings"]:
                print(f"  [?] {warn}")

        if report["info"]:
            print(f"\n[+] INFO:")
            for inf in report["info"]:
                print(f"  [i] {inf}")

        print(f"\n--------------------------------------------------------")
        if success:
            print("[+] STATUS: PASS — Skill conforms to Antigravity standards.")
        else:
            print("[-] STATUS: FAIL — Please address reported errors.")
        print(f"========================================================\n")

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
