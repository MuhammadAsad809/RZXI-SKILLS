# Antigravity Skill Architecture & Design Principles

`[DARKCODE::REFERENCE::SKILL_ARCHITECTURE::v1.0]`

## 1. Overview & Mechanics

An Antigravity **Skill** is a self-contained, modular package of operational runbooks, deterministic tool wrappers, and domain knowledge that extends an AI agent's capabilities. 

Unlike passive system prompts or static rule files, skills operate on a **Progressive Disclosure** model designed to optimize token economy and maximize precision.

---

## 2. Progressive Disclosure & Token Economy

In modern agentic architectures, context window space and attention allocation are critical resources. If all documentation, manuals, and tool instructions were permanently loaded into the agent's context, two failures occur:
1. **Context Window Exhaustion**: Long runbooks bloat the system prompt and reduce space for actual code and conversation history.
2. **Attention Dilution / Hallucination**: Massive static prompts cause the model's attention weights to drift, leading to instruction non-compliance.

### How Antigravity Resolves This:
1. **Discovery & Registration Phase**:
   - The agent reads ONLY the YAML frontmatter (`name` and `description`) of discovered skills.
   - This metadata takes minimal token space (~30-60 tokens per skill).
2. **Conditional Activation Phase**:
   - When a user query matches the `description` criteria, the agent activates the skill.
   - The agent loads the main `SKILL.md` into active context.
3. **On-Demand Reference Phase**:
   - If `SKILL.md` delegates complex technical tables, schemas, or diagnostic trees to files in `references/`, the agent only reads those specific reference files when needed using file viewing tools.

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Registration: Name + Description (~50 tokens)             │
└──────────────────────────────┬──────────────────────────────┘
                               │ User prompt matches triggers
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. Activation: SKILL.md Core Workflow (~500 - 1500 tokens)   │
└──────────────────────────────┬──────────────────────────────┘
                               │ Specific deep detail needed
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. Deep Reference: references/*.md (Loaded on demand)        │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Directory Specification

Every skill package must adhere to the standardized directory structure:

```text
skills/<skill-name>/
├── SKILL.md             # Required: Entrypoint, frontmatter, core runbooks
├── scripts/             # Optional/Recommended: Executable CLI automation tools
│   ├── <name>_engine.py
│   └── run.sh
├── references/          # Optional: Deep architectural manuals, schemas, matrices
│   ├── protocol_spec.md
│   └── troubleshooting.md
├── resources/           # Optional: Static assets, configuration templates
│   └── config.template.json
└── examples/            # Optional: Sample workflows, reference inputs/outputs
    └── sample_run.json
```

### Component Roles:
- **`SKILL.md`**: Contains YAML frontmatter and the primary, step-by-step procedures. Must remain under ~250 lines.
- **`scripts/`**: Contains deterministic, executable scripts (Python/Bash) that perform actions directly rather than having the agent guess bash one-liners.
- **`references/`**: Contains in-depth manuals, hardware/firmware registers, RFC specifications, and recovery protocols.
- **`resources/`**: Houses static templates, payloads, or sample configuration files.
- **`examples/`**: Houses concrete demonstrations and sample command sessions.

---

## 4. Discovery Hierarchy & Precedence

Antigravity traverses multiple directories to discover installed skills. If multiple skills share the same `name`, the higher priority location overrides:

| Priority | Scope | Default Path | Best For |
| :--- | :--- | :--- | :--- |
| **1 (Highest)** | Workspace | `<project_root>/.agents/skills/<name>/` | Project-specific team runbooks, local build tools |
| **2** | Workspace Config | Explicitly declared in `skills.json` | Custom paths or vendor packages |
| **3** | Machine Global | `~/.gemini/config/skills/<name>/` | Universal developer skills, offensive security tools |
| **4** | Built-in | Application internal bundled skills | Core default system capabilities |

---

## 5. Architectural Quality Standards

1. **Deterministic Execution**:
   - Skills should prefer calling a tested helper script in `scripts/` over constructing unverified long shell chains.
2. **Explicit Verification Steps**:
   - Every procedure in `SKILL.md` must conclude with a verification step instructing the agent how to check if the action succeeded.
3. **No General Knowledge Duplication**:
   - Avoid explaining generic Python or Linux commands that any frontier model already knows. Focus strictly on domain-specific workflows.
