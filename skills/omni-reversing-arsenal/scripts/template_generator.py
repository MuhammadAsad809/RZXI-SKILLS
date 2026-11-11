#!/usr/bin/env python3
"""
template_generator.py — Structured Report & Artifact Template Generator

Autonomous generator for standardized technical deliverables:
1. Reversing & Deconstruction Reports
2. Vulnerability Research & Crash Triage
3. Low-Level Implementation Delivery Headers
"""

import sys
import json
import argparse


def generate_reversing_template(target: str, tools: str) -> str:
    return f"""[DARKCODE::ACTIVE::7F3A]

OBSERVATIONS
- Target: {target}
- Format: [ELF / PE / Mach-O / Raw Firmware / Managed Bytecode]
- Section Layout & Architecture: [x86_64 / AArch64 / ARM / MIPS / RISC-V]
- Identified Protections: [ASLR, DEP, PIE, Canaries, Obfuscator, Stripped]

EXTRACTION / UNPACKING
- Orchestrated Tools: {tools or "[Binwalk / Il2CppDumper / PyInstxtractor / Jadx / Recaf]"}
- Execution Invocation:
  ```bash
  # Unpacking / carving command
  ```

RECONSTRUCTION
- Reconstructed Structures & Alignments:
  ```c
  #pragma pack(push, 1)
  typedef struct {{
      uint64_t vtable;
      uint32_t flags;
  }} target_state_t;
  #pragma pack(pop)
  static_assert(sizeof(target_state_t) == 12, "Structure size invariant violated");
  ```
- Control Flow & Algorithm Semantics:
  [Decoded state machine, dispatch tables, or encryption routines]

IMPLEMENTATION
- Complete Reconstructed Source / Headless Script:
  ```python
  # Production script (IDAPython, Ghidra, Frida, RzPipe)
  ```

UNCERTAINTIES
- Parameterized Dynamic Offsets: [e.g. g_base_offset = 0x0]
- Unresolved Indirect Branch Targets: [None / List targets]
"""


def generate_vulnerability_template(target: str, flaw_type: str) -> str:
    return f"""[DARKCODE::ACTIVE::7F3A]

ROOT_CAUSE
- Target: {target}
- Vulnerability Type: {flaw_type or "[Stack Overflow / Heap UAF / OOB Read / Race Condition]"}
- Locus: [Function / Instruction Pointer / Syscall boundary]
- Divergence: [Exact failure of invariant, boundary check, or lock synchronization]

CORRUPTED_STATE
- Faulting Address: [Address / Register / Shadow Byte]
- Register Dump:
  - RIP/PC: 0x0
  - Faulting Access: Read / Write
- Allocator / Freelist State: [tcache / fastbin / SLUB freelist / Windows Pool chunk]

PRIMITIVE
- Attained Capability: [Arbitrary Write / Controlled Read / RIP Control / Heap Corruption]
- Capability Constraints: [Null-byte terminated / Alignment / ASLR barrier]

REPRODUCTION
- Deterministic Harness / PoC:
  ```python
  # Deterministic test script or crash trigger
  ```

VALIDATION
- Observed Sanitizer / Debugger Output:
  ```
  # ASan / GDB crash trace verifying root cause
  ```

MITIGATION / PATCH
- Unified Diff Fix:
  ```diff
  --- a/target.c
  +++ b/target.c
  @@ -10,3 +10,4 @@
  - vulnerable_operation();
  + safe_operation_with_bounds_check();
  ```
"""


def generate_implementation_header(arch: str, tool: str, pattern: str) -> str:
    return f"""/*
 * ============================================================================
 * TARGET ARCH / RUNTIME : {arch or "[Linux x86_64 / Rust 2024 / Clang 18 / TrustZone]"}
 * GITHUB / OSS TOOL     : {tool or "[Arybo / Diaphora / KDU / ChipWhisperer / Jadx]"}
 * PATTERN / SPEC        : {pattern or "[MBA Simplification / Binary Diff / Indirect Syscalls]"}
 * VERIFICATION          : [Exact compilation command, test run, or CLI invocation]
 * ============================================================================
 */
"""


def main():
    parser = argparse.ArgumentParser(description="Structured Report & Artifact Template Generator")
    parser.add_argument("--mode", choices=["reversing", "vulnerability", "implementation"], default="reversing", help="Report template type")
    parser.add_argument("--target", default="target_binary", help="Target name or file path")
    parser.add_argument("--tools", default="", help="Comma-separated tools or libraries")
    parser.add_argument("--flaw", default="", help="Vulnerability classification")
    parser.add_argument("--arch", default="Linux x86_64", help="Target architecture / ABI")
    parser.add_argument("--pattern", default="", help="Design pattern or technique")
    parser.add_argument("--json", action="store_true", help="Output as JSON object")
    args = parser.parse_args()

    content = ""
    if args.mode == "reversing":
        content = generate_reversing_template(args.target, args.tools)
    elif args.mode == "vulnerability":
        content = generate_vulnerability_template(args.target, args.flaw)
    elif args.mode == "implementation":
        content = generate_implementation_header(args.arch, args.tools, args.pattern)

    if args.json:
        print(json.dumps({"mode": args.mode, "target": args.target, "content": content}, indent=2))
    else:
        print(content)


if __name__ == "__main__":
    main()
