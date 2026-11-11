---
name: minimal-workflow-skill
description: >-
  Use this skill when the user asks to run lightweight health checks or status audits
  on local services. Provides direct CLI instructions and triage steps.
---

# Minimal Workflow Skill

`[DARKCODE::EXAMPLE::MINIMAL_WORKFLOW]`

## Overview

Demonstration of a concise, single-file runbook skill designed for rapid execution of diagnostic routines without heavy auxiliary scripts.

---

## When to Use

Activate when:
- Performing baseline health checks on workspace daemons.
- Validating system resource availability (memory, disk, processes).

---

## Operational Runbook

### Step 1: Resource Inspection
```bash
# Check memory and disk space
free -m
df -h .
```

### Step 2: Service Liveness Check
```bash
# Verify active background listener processes
ps aux | grep -v grep | grep -E "node|python|service"
```

### Step 3: Verification
Confirm that available memory exceeds 500MB and no rogue unmanaged processes occupy ports.
