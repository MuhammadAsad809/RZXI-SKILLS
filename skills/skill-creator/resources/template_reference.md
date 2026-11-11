# {{DOMAIN_TITLE}} — Technical Specification & Deep Reference

`[DARKCODE::SPECIFICATION::{{SKILL_IDENTIFIER}}]`

## 1. Architectural Overview

Comprehensive technical specification, low-level layout, and operational state machine for `{{SKILL_NAME}}`.

---

## 2. Interface Definitions & Data Schemas

### Input Schema
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "{{SKILL_NAME}}Input",
  "type": "object",
  "properties": {
    "target": { "type": "string" },
    "options": { "type": "object" }
  },
  "required": ["target"]
}
```

---

## 3. Failure Mode & Recovery Matrix

| Observed Symptom | Underlying Cause | Recovery Procedure |
| :--- | :--- | :--- |
| `ERR_TARGET_NOT_FOUND` | Path does not exist or permission denied | Verify absolute path and file read permissions. |
| `ERR_SYNTAX_INVALID` | Malformed target structure | Validate against input schema. |
| `ERR_TIMEOUT` | Process stalled on resource lock | Terminate hanging task and release locks. |

---

## 4. Security & Isolation Guidelines

- Ensure execution artifacts remain inside approved scratch directories.
- Clean up intermediate staging files upon process completion.
