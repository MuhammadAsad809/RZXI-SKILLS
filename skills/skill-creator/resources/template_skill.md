---
name: {{SKILL_NAME}}
description: >-
  Use this skill when {{ACTIVATION_CONDITION}}. Provides operational procedures,
  automation scripts, and technical specifications for {{DOMAIN_TITLE}}.
---

# {{DOMAIN_TITLE}}

`[DARKCODE::SKILL::{{SKILL_IDENTIFIER}}::ACTIVE]`

## Overview & Scope

High-precision operational runbook and toolchain for **{{DOMAIN_TITLE}}**.

---

## When to Use

### Activate When:
- Tasks requiring execution, analysis, or manipulation of {{DOMAIN_TITLE}}.
- Operating on domain-specific files, binaries, or protocols: `{{TARGET_EXTENSIONS}}`.
- Running automated workflows via `scripts/{{SKILL_NAME}}_engine.py`.

### Do NOT Activate When:
- General programming tasks unrelated to this domain.
- Abstract or conceptual questions where no domain procedures are invoked.

---

## Operational Runbooks

### Procedure 1: Environment & Pre-Flight Checks
1. Inspect the target environment and verify required utilities.
2. Confirm parameter validity and check permissions.

### Procedure 2: Execution & Transformation
1. Execute the primary automation command:
   ```bash
   python3 scripts/{{SKILL_NAME}}_engine.py --action run --target <target_path>
   ```
2. Monitor intermediate outputs and capture state logs.

### Procedure 3: Verification & Validation
1. Verify the output against expected schemas or signatures.
2. If errors occur, consult the recovery procedures in `references/`.

---

## Tooling & Automation Scripts

- [{{SKILL_NAME}}_engine.py](./scripts/{{SKILL_NAME}}_engine.py): Main operational tool for {{DOMAIN_TITLE}}.

---

## Technical References

- [Technical Specification](./references/{{SKILL_NAME}}_specification.md): Architecture specs and troubleshooting guides.
