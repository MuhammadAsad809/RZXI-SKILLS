# Antigravity Skill Validation Checklist & Scorecard

`[DARKCODE::REFERENCE::VALIDATION_CHECKLIST::v1.0]`

Use this 15-point scorecard to audit, review, and certify any skill package before publication or active deployment.

---

## 1. Frontmatter & Routing (Items 1–6)

- [ ] **1. YAML Delimiters**: `SKILL.md` opens with `---` on Line 1 and terminates with `---` before Markdown headings.
- [ ] **2. Canonical Naming**: `name` field contains only lowercase alphanumerics, hyphens, or underscores (`^[a-z0-9][a-z0-9\-_]*[a-z0-9]$`).
- [ ] **3. Folder Consistency**: The `name` matches the parent directory name exactly (e.g., `skill-creator/SKILL.md` has `name: skill-creator`).
- [ ] **4. Description Length & Precision**: The `description` is between 50 and 350 characters, capturing target domains and tools.
- [ ] **5. Third-Person Activation Trigger**: The description explicitly states when to activate ("Use this skill when...") and avoids first-person pronouns ("I will", "My skill").
- [ ] **6. Boundary / Negative Triggers**: The description or `SKILL.md` explicitly defines what tasks should NOT trigger this skill to avoid semantic collisions.

---

## 2. Architecture & Progressive Disclosure (Items 7–10)

- [ ] **7. Token Economy**: `SKILL.md` is concise (under 250 lines / 15KB) and focuses on core workflows.
- [ ] **8. Deep Reference Separation**: Lengthy technical tables, protocol specs, RFCs, and error codes are moved to `references/`.
- [ ] **9. Link Integrity**: Every internal Markdown link (e.g. `[ref](./references/doc.md)`) points to an existing file on disk. No 404 links.
- [ ] **10. Standard Hierarchy**: Standard directories (`scripts/`, `references/`, `resources/`, `examples/`) are used consistently.

---

## 3. Automation Scripts & Executability (Items 11–13)

- [ ] **11. Hashbang & Permissions**: Every script in `scripts/` begins with `#!/usr/bin/env python3` (or `bash`) and has execute bit set (`chmod +x`).
- [ ] **12. Pure Standard Library**: Scripts avoid mandatory external `pip` dependencies unless strictly unavoidable, falling back gracefully if tools are missing.
- [ ] **13. CLI & JSON Support**: Scripts use `argparse`, provide `--help`, and support `--json` output alongside standard exit codes (0 for success, non-zero for failure).

---

## 4. Operational Reliability (Items 14–15)

- [ ] **14. Step-by-Step Runbooks**: Procedures provide exact commands and describe expected outputs.
- [ ] **15. Verification Steps**: Every procedure includes an explicit verification or validation check to prove success.

---

## Automated Scorecard Execution

Run the built-in validator to check items automatically:

```bash
python3 scripts/validate_skill.py <path_to_skill> --strict
```
