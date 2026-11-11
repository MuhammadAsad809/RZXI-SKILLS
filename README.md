# RZXI-SKILLS

Autonomous agent skills, reverse engineering arsenals, systems programming frameworks, and Antigravity workflow extensions.

---

## Repository Structure

```
RZXI-SKILLS/
├── skills/                          # Custom High-End Engineering & Research Skills
│   ├── omni-reversing-arsenal/      # Complete reversing toolchain, disassemblers, firmware, ABI specs
│   ├── reverse-engineer-anything/   # REA framework for native, managed, web, & mobile targets
│   ├── skill-creator/               # Autonomous skill scaffolding, synthesis, and validation tools
│   └── skillject-security-context/  # Security auditing, payload generators, SNS engine, trace mutators
├── builtin/                         # Antigravity Platform Core Skills
│   ├── agy-customizations/          # Guides for hooks, MCP servers, plugins, rules, and skills
│   ├── antigravity_guide/           # Complete CLI, IDE, and SDK reference documentation
│   ├── automation/                  # Autonomous task execution workflows
│   ├── generative_ui/               # Dynamic inline/standalone visual UI widgets
│   ├── migrate-workflows/           # Migration tooling for workflows
│   ├── permissioned-github/         # Secure GitHub token and repository operations
│   ├── plugin/                      # Extensible plugin framework
│   └── ui-plugin-navigation/        # UI navigation hooks and interfaces
├── .gitignore
└── README.md
```

---

## Skills Breakdown

### Custom Engineering & Research Skills (`skills/`)

| Skill | Version | Description | Key Modules |
| :--- | :---: | :--- | :--- |
| **`omni-reversing-arsenal`** | 1.0.0 | Global reverse engineering toolchain orchestrator covering ELF, PE, Mach-O, firmware carving, DBI, kernel, and fuzzing systems. | `target_triager.py`, `template_generator.py`, reference guides |
| **`reverse-engineer-anything`** | 49 | Reverse engineer native, managed (.NET/Java), Electron, browser, and Android artifacts using REA runtime evidence. | Android, Native, Web, Environment references |
| **`skill-creator`** | 1.0.0 | Complete framework to architect, scaffold, validate, and package production-grade Antigravity skills. | `validate_skill.py`, `init_skill.py`, `ai_skill_synthesizer.py`, `package_skill.py` |
| **`skillject-security-context`** | 1.0.0 | Advanced security auditing context, Structural Naturalness Score (SNS) analyzers, trace mutation, and memory extraction primitives. | `payload_generator.py`, `trace_mutator.py`, `sns_engine.py` |

### Platform Builtin Skills (`builtin/`)

| Skill | Purpose |
| :--- | :--- |
| **`agy-customizations`** | Technical documentation for extending Antigravity via hooks, rules, plugins, and MCP. |
| **`antigravity_guide`** | Developer handbook for CLI commands, IDE hotkeys, SDK integration, and architecture. |
| **`generative_ui`** | Protocols for generating interactive KaTeX, Mermaid, Charts, and responsive widgets. |
| **`permissioned-github`** | Automated GitHub repository management and authenticated API interactions. |
| **`automation` / `plugin`** | Platform automation and extensible plugin runtime interfaces. |

---

## Installation & Deployment

### Adding Skills to Antigravity

To deploy these skills into your local Antigravity environment:

```bash
# Clone the repository
git clone https://github.com/MuhammadAsad809/RZXI-SKILLS.git

# Copy custom skills into Antigravity user config
mkdir -p ~/.gemini/config/skills/
cp -r RZXI-SKILLS/skills/* ~/.gemini/config/skills/
```

### Validating a Skill

To lint and validate any skill structure using the `skill-creator` validation engine:

```bash
python3 skills/skill-creator/scripts/validate_skill.py skills/omni-reversing-arsenal
```

---

## License

Proprietary / Research — Maintained by MuhammadAsad809.
