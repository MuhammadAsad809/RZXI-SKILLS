#!/usr/bin/env python3
"""
package_skill.py — Skill Packaging, Installation, and Distribution Utility for Antigravity

Features:
- Validates skill compliance prior to deployment
- Bundles skills into compressed archives (.tar.gz)
- Installs skills into global (~/.gemini/config/skills/) or workspace (.agents/skills/)
- Lists and manages installed skills across configuration layers
"""

import sys
import os
import shutil
import tarfile
import argparse
import subprocess
from pathlib import Path


GLOBAL_SKILLS_DIR = Path("/data/user/0/com.agy/files/.gemini/config/skills")
WORKSPACE_SKILLS_DIR = Path(".agents/skills")


def run_validation(skill_dir: Path) -> bool:
    """Invokes validate_skill.py against target directory."""
    validator_path = Path(__file__).parent / "validate_skill.py"
    if not validator_path.exists():
        return True

    res = subprocess.run([sys.executable, str(validator_path), str(skill_dir)], capture_output=False)
    return res.returncode == 0


def bundle_skill(skill_dir: Path, output_archive: Path) -> None:
    """Creates a compressed tar.gz bundle of the skill directory."""
    print(f"[*] Packaging '{skill_dir.name}' into archive: {output_archive}")
    with tarfile.open(output_archive, "w:gz") as tar:
        tar.add(skill_dir, arcname=skill_dir.name)
    print(f"[+] Bundle created successfully: {output_archive} ({output_archive.stat().st_size} bytes)")


def install_skill(skill_dir: Path, dest_root: Path, force: bool = False) -> None:
    """Copies the skill directory to the target root."""
    target_dir = dest_root / skill_dir.name
    print(f"[*] Installing '{skill_dir.name}' to: {target_dir}")

    if target_dir.exists():
        if not force:
            print(f"[-] Error: Destination already exists: {target_dir}. Use --force to overwrite.", file=sys.stderr)
            sys.exit(1)
        shutil.rmtree(target_dir)

    shutil.copytree(skill_dir, target_dir)
    print(f"[+] Installed '{skill_dir.name}' successfully to {target_dir}!")


def list_installed_skills() -> None:
    """Lists skills discovered in global and workspace locations."""
    print("\n========================================================")
    print(" Installed Antigravity Skills")
    print("========================================================")

    # Global
    print(f"\n[+] Global Skills ({GLOBAL_SKILLS_DIR}):")
    if GLOBAL_SKILLS_DIR.exists():
        count = 0
        for item in sorted(GLOBAL_SKILLS_DIR.iterdir()):
            if item.is_dir() and (item / "SKILL.md").exists():
                print(f"  - {item.name}")
                count += 1
        if count == 0:
            print("  (none)")
    else:
        print("  (directory does not exist)")

    # Workspace
    print(f"\n[+] Workspace Skills ({WORKSPACE_SKILLS_DIR.resolve()}):")
    if WORKSPACE_SKILLS_DIR.exists():
        count = 0
        for item in sorted(WORKSPACE_SKILLS_DIR.iterdir()):
            if item.is_dir() and (item / "SKILL.md").exists():
                print(f"  - {item.name}")
                count += 1
        if count == 0:
            print("  (none)")
    else:
        print("  (directory does not exist)")

    print(f"========================================================\n")


def main():
    parser = argparse.ArgumentParser(description="Antigravity Skill Packager and Manager")
    parser.add_argument("skill_dir", nargs="?", help="Path to the skill directory")
    parser.add_argument("--bundle", help="Create a compressed .tar.gz archive at specified path")
    parser.add_argument("--install-global", action="store_true", help="Install into global config (~/.gemini/config/skills/)")
    parser.add_argument("--install-workspace", action="store_true", help="Install into workspace (.agents/skills/)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing destination during install")
    parser.add_argument("--no-validate", action="store_true", help="Skip pre-install validation")
    parser.add_argument("--list", action="store_true", help="List all installed skills")
    args = parser.parse_args()

    if args.list:
        list_installed_skills()
        return

    if not args.skill_dir:
        parser.error("skill_dir is required unless --list is specified.")

    skill_path = Path(args.skill_dir).resolve()
    if not skill_path.is_dir() or not (skill_path / "SKILL.md").exists():
        print(f"[-] Error: '{skill_path}' is not a valid Antigravity skill directory (missing SKILL.md).", file=sys.stderr)
        sys.exit(1)

    if not args.no_validate:
        print(f"[*] Running pre-flight validation on '{skill_path.name}'...")
        if not run_validation(skill_path):
            print(f"[-] Validation failed. Fix errors before packaging/installing or use --no-validate.", file=sys.stderr)
            sys.exit(1)

    if args.bundle:
        bundle_skill(skill_path, Path(args.bundle).resolve())

    if args.install_global:
        GLOBAL_SKILLS_DIR.mkdir(parents=True, exist_ok=True)
        install_skill(skill_path, GLOBAL_SKILLS_DIR, force=args.force)

    if args.install_workspace:
        WORKSPACE_SKILLS_DIR.mkdir(parents=True, exist_ok=True)
        install_skill(skill_path, WORKSPACE_SKILLS_DIR, force=args.force)


if __name__ == "__main__":
    main()
