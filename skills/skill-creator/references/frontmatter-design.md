# Frontmatter Design & Trigger Engineering

`[DARKCODE::REFERENCE::FRONTMATTER_DESIGN::v1.0]`

## 1. The Critical Role of Frontmatter

In the Antigravity Customization Architecture, the YAML frontmatter block in `SKILL.md` is the **only part of the skill** loaded into the agent's base system context.

If the frontmatter description is weak, vague, or missing key trigger criteria:
- The agent will fail to activate the skill when needed (**False Negative**).
- Or the agent will activate the skill for unrelated prompts, wasting context (**False Positive / Collision**).

---

## 2. Frontmatter Schema & Specifications

```yaml
---
name: target-skill-name
description: >-
  Use this skill when the user asks to perform specific domain workflows,
  analyze target formats, or utilize specific tools. Provides step-by-step
  operational runbooks and automation scripts.
metadata:
  version: "1.0.0"
  author: "DARKCODE"
---
```

### Field Specifications:
1. **`name`** (Required):
   - Constraint: Lowercase alphanumeric with hyphens or underscores (`^[a-z0-9][a-z0-9\-_]*[a-z0-9]$`).
   - Must match the parent directory name to ensure cross-system consistency.
   - Example: `linux-kernel-fuzzer`, `apk-decompiler`, `skill-creator`.

2. **`description`** (Required):
   - String, recommended length 50–350 characters.
   - Must be written in **third-person** imperative/declarative style.
   - Must explicitly specify **WHAT** the skill does and **WHEN** it must be activated.

3. **`metadata`** (Optional):
   - Arbitrary key-value pairs (e.g. `version`, `author`, `tool_count`).

---

## 3. High-Precision Description Formulation

### The 4-Part Formula for Bulletproof Descriptions:

Every high-performing skill description follows this 4-part structure:

1. **Activation Imperative**: `Use this skill when the user asks to...`
2. **Domain Scope**: Specific targets, file types, protocols, or technologies.
3. **Core Actions**: Verbs indicating operational procedures (e.g., *scaffold, audit, extract, decompile, patch, fuzz*).
4. **Negative Boundary (Anti-Trigger)**: Explicit guidance on when NOT to activate.

### Good vs Bad Examples:

#### ❌ Bad (Vague / First-Person / Weak Routing):
```yaml
description: I will help you with reverse engineering and code stuff.
```
*Why it fails*: First-person phrasing, completely generic, offers no distinguishing domain keywords or boundaries.

#### ❌ Bad (Tutorial Style / Passive):
```yaml
description: An introduction to ELF binaries and how memory works in Linux.
```
*Why it fails*: Sounds like educational material rather than an operational agent capability.

#### ✅ Elite (High Precision & Clear Routing):
```yaml
description: >-
  Use this skill when the user asks to reverse engineer, inspect, decompile, or patch
  native ELF/PE binaries, firmware images, or stripped executables using GDB, Rizin,
  or objdump. Provides low-level disassembly analysis, symbol recovery, and binary
  patching runbooks. Skip for ordinary source-level debugging.
```

---

## 4. Preventing Trigger Collisions

When multiple skills share overlapping keywords (e.g., `c-memory-debugger` vs `gdb-reverse-engineer`), resolve collisions through **Negative Framing**:

- "Use this skill for dynamic runtime debugging with GDB. For static source code linting or memory leak analysis without binary execution, use `c-memory-auditor`."
- "Skip this skill for standard web application development."

---

## 5. YAML Multiline Scalars

Always use `>-` (folded, stripped) for multiline descriptions:
- `>-` folds newlines into spaces and strips trailing blank lines, preventing syntax parsing errors across different agent runtimes.
- Avoid raw unquoted strings containing colons (`:`) or braces (`{}`), which break standard YAML parsers.
