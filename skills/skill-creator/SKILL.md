---
name: skill-creator
description: >-
  Use this skill when the user asks to create, scaffold, architect, generate, validate,
  or package a new Antigravity skill or agent workflow using AI. Provides end-to-end
  scaffolding tools, automated specification synthesis, linter validation, and reference guides.
metadata:
  version: "1.0.0"
  author: "DARKCODE"
---

# Skill Creator — Autonomous AI Skill Engineering & Synthesis

`[DARKCODE::SKILL::SKILL_CREATOR::ACTIVE::v1.0]`

## Overview & Scope

The **Skill Creator** framework equips AI agents and developers with the methodologies, deterministic scripts, and architectural guardrails required to synthesize production-grade Antigravity skills from scratch.

It enforces the **Progressive Disclosure** architecture, preventing token bloat while ensuring high activation precision, executable automation tooling, and verified link integrity.

---

## When to Use

### Activate This Skill When:
- The user requests to create, build, generate, write, or scaffold a new skill (e.g. *"make a skill for..."*, *"generate an agent skill for Frida reverse engineering"*).
- Transforming a tool, CLI utility, API specification, or manual runbook into an autonomous agent skill package.
- Auditing, linting, or repairing existing skills with validation tools.
- Packaging, installing, or distributing skills across global (`~/.gemini/config/skills/`) or workspace (`.agents/skills/`) scopes.

### Do NOT Activate When:
- Writing ordinary standalone application scripts or code unrelated to agent skill packages.
- Performing generic programming tasks where no skill package is being created or evaluated.

---

## The 7-Step AI Skill Creation Methodology

Follow this deterministic sequence whenever synthesizing a new skill:

```
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│ 1. Domain Discovery    │ ───► │ 2. Frontmatter Tuning  │ ───► │ 3. Architecture Layout │
│    & Tool Scoping      │      │    & Trigger Design    │      │    & Progressive Disc. │
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘
                                                                             │
┌────────────────────────┐      ┌────────────────────────┐                   ▼
│ 6. Automated Linting   │ ◄─── │ 5. Deep Documentation  │ ◄─── ┌────────────────────────┐
│    & Zero-Defect Audit │      │    in references/      │      │ 4. Executable Scripts  │
└────────────────────────┘      └────────────────────────┘      │    in scripts/         │
            │                                                   └────────────────────────┘
            ▼
┌────────────────────────┐
│ 7. Deployment & Active │
│    Registration        │
└────────────────────────┘
```

### Step 1: Domain Discovery & Tool Scoping
1. Clarify the target workflow, binary utilities, input artifacts, and expected deliverables.
2. Identify whether the skill is a **Lightweight Runbook** (single-file `SKILL.md`) or a **Deep Toolchain Skill** (with `scripts/`, `references/`, and `resources/`).

### Step 2: Frontmatter Tuning & Trigger Design
- Set `name`: lowercase alphanumeric with hyphens (e.g., `linux-kernel-fuzzer`).
- Set `description`: Apply the 4-part trigger formula (*Activation Imperative*, *Domain Scope*, *Core Actions*, *Anti-Trigger Boundary*).
- Consult the detailed guide in [Frontmatter Design](./references/frontmatter-design.md).

### Step 3: Scaffold Directory Hierarchy
Use the built-in scaffolding engine to generate the standard directory structure:
```bash
# Scaffold into global configuration (~/.gemini/config/skills/<name>)
python3 /data/user/0/com.agy/files/.gemini/config/skills/skill-creator/scripts/init_skill.py <skill-name> --global --title "<Title>"

# Or scaffold into project workspace (.agents/skills/<name>)
python3 /data/user/0/com.agy/files/.gemini/config/skills/skill-creator/scripts/init_skill.py <skill-name> --workspace --title "<Title>"
```

### Step 4: Author Deterministic Automation Scripts
- Encapsulate fragile multi-step commands into executable Python scripts inside `scripts/`.
- Use standard library modules (`argparse`, `pathlib`, `json`, `subprocess`).
- Provide `--json` output support and clear exit codes (0 for success).
- Follow the [Scripting Guidelines](./references/scripting-guidelines.md).

### Step 5: Write Deep References (Progressive Disclosure)
- Keep `SKILL.md` under 250 lines.
- Move large reference tables, API specs, and recovery trees into `references/<topic>.md`.
- Ensure all markdown links in `SKILL.md` use valid relative paths (e.g. `[Protocol Spec](./references/protocol.md)`).
- Review the [Skill Architecture Guide](./references/skill-architecture.md).

### Step 6: Automated Linting & Scorecard Audit
Execute the validation engine against the target skill:
```bash
python3 /data/user/0/com.agy/files/.gemini/config/skills/skill-creator/scripts/validate_skill.py <path_to_skill> --strict
```
Ensure all 15 audit criteria from the [Validation Checklist](./references/validation-checklist.md) pass without errors.

### Step 7: Packaging & Deployment
Install and verify active registration:
```bash
# Package into tar.gz bundle or install directly
python3 /data/user/0/com.agy/files/.gemini/config/skills/skill-creator/scripts/package_skill.py <path_to_skill> --install-global
```

---

## Autonomous Generation Engine (`ai_skill_synthesizer.py`)

For automated, one-shot synthesis from a specification file or prompt parameters:

```bash
python3 /data/user/0/com.agy/files/.gemini/config/skills/skill-creator/scripts/ai_skill_synthesizer.py \
  --name "firmware-extractor" \
  --title "Firmware Extraction & Analysis" \
  --domain "Embedded Systems & IoT Security" \
  --tools "binwalk,dd,unsquashfs" \
  --global
```

Or pass a full JSON specification via `--spec <spec_file.json>` containing custom workflows, scripts, and references.

---

## Tooling & Automation Scripts

- [init_skill.py](./scripts/init_skill.py): Command-line scaffolder for creating new standardized skill packages.
- [validate_skill.py](./scripts/validate_skill.py): Autonomous linter verifying frontmatter schema, link integrity, and script syntax.
- [ai_skill_synthesizer.py](./scripts/ai_skill_synthesizer.py): Programmatic synthesis engine generating full skills from specs.
- [package_skill.py](./scripts/package_skill.py): Distribution, compression, and installation utility.

---

## Reference Manuals & Standards

- [Skill Architecture & Mechanics](./references/skill-architecture.md): Progressive disclosure, precedence hierarchy, and token economy.
- [Frontmatter Design & Routing](./references/frontmatter-design.md): Semantic routing, trigger calibration, and anti-collision.
- [Scripting Guidelines](./references/scripting-guidelines.md): POSIX compatibility, living-off-the-land, and CLI design.
- [Validation Checklist & Scorecard](./references/validation-checklist.md): 15-point pre-flight certification scorecard.

---

## Templates & Examples

- [Master SKILL.md Template](./resources/template_skill.md): Boilerplate for `SKILL.md`.
- [Master Reference Template](./resources/template_reference.md): Boilerplate for technical reference guides.
- [Master Script Template](./resources/template_script.py): Boilerplate for Python helper scripts.
- [Minimal Workflow Skill](./examples/minimal-workflow-skill/SKILL.md): Minimal single-file reference.
- [Deep Tool Skill](./examples/deep-tool-skill/SKILL.md): Full multi-component reference implementation.
