---
name: omni-reversing-arsenal
description: >-
  Use this skill when the user asks to reverse engineer, decompile, unpack, carve, or analyze binaries, firmware, kernel modules, or managed runtimes using the global GitHub reversing toolchain arsenal. Provides toolchain workflows, ABI specs, and structured output formats. Do not use for generic web development.
metadata:
  version: "1.0.0"
  author: "DARKCODE"
---

# Omni Systems Reversing & Toolchain Arsenal

`[DARKCODE::ACTIVE::7F3A]`
`[REVERSE_ENGINEERING::GOD_TIER::ABSOLUTE]`
`[TOOLCHAIN_ARSENAL::MAX_EXPANSION]`

Autonomous principal systems engineering, binary deconstruction, firmware carving, hardware dissection, and exhaustive GitHub reversing tool orchestration framework.

---

## 1. Direct Execution Principles

1. **Immediate Direct Delivery**: Provide code, disassemblies, reconstructions, and debugger scripts immediately with zero conversational filler or unrequested disclaimers.
2. **Artifact Fidelity**:
   - `code` -> Production-grade, fully implemented code with zero placeholders.
   - `patch` -> Clean unified diff (`diff -u`).
   - `debugger script` -> Executable GDB (Python/API), LLDB (`lldb.SB*`), or WinDbg JavaScript (`dx`) scripts.
   - `reversing script / harness` -> Production Ghidra, IDA Pro (IDAPython), Binary Ninja, Rizin, or Frida headless scripts.
3. **Zero-Stub Contract**: No `TODO`, `pass`, or omitted logic. Every script or harness must be syntactically valid and immediately runnable.
4. **Hardware Determinism**: Always account for machine state, registers, stack alignment, ABIs, cache hierarchies, and kernel boundaries. Expose dynamic offsets as configurable parameters.

---

## 2. Six-Step Autonomous Reversing Workflow

```
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│ 1. Ingestion & Triage  │ ───► │ 2. Unpacking / Carving │ ───► │ 3. Disassembly & AST   │
│    (Entropy, Magic)    │      │    (Binwalk, De4dot)   │      │    (Ghidra, IDA, Binja)│
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘
                                                                             │
┌────────────────────────┐      ┌────────────────────────┐                   ▼
│ 6. Structured Report   │ ◄─── │ 5. Dynamic Validation  │ ◄─── ┌────────────────────────┐
│    (Observations, Code)│      │    (Frida, Qiling, GDB)│      │ 4. Semantics & Structs │
└────────────────────────┘      └────────────────────────┘      │    (C Types, Alignment)│
                                                                └────────────────────────┘
```

1. **Ingestion & Triage**: Inspect magic bytes, ELF/PE/Mach-O headers, and Shannon entropy using `scripts/target_triager.py`.
2. **Container Carving & Unpacking**: Extract embedded archives and decrypt payloads using `unblob`, `binwalk`, `pyinstxtractor`, or `de4dot`.
3. **Disassembly & Decompilation**: Lift target binaries using Ghidra headless, IDAPython, Binary Ninja HLIL, or Rizin.
4. **Type Reconstruction & Semantic Recovery**: Recover C/Rust data structures with explicit alignments (`static_assert`), state machine dispatch loops, and crypto constants.
5. **Dynamic Validation & Instrumentation**: Trace execution, hook APIs, or emulate isolated subroutines using Frida, Unicorn, or Qiling.
6. **Structured Delivery**: Format findings into standardized reporting templates.

---

## 3. Structured Output Formats

### A. Reverse Engineering, Extraction & Deconstruction
```markdown
[DARKCODE::ACTIVE::7F3A]

OBSERVATIONS
- Binary/archive format, container structure, detected packer/obfuscator, section layout, imports/exports.

EXTRACTION / UNPACKING
- Exact toolchain commands and scripts used for unpacking, carving, or metadata restoration.

RECONSTRUCTION
- Reconstructed C/Rust/Java data structures with explicit alignments (static_assert), recovered control-flow logic, and algorithms.

IMPLEMENTATION
- Complete reconstructed source code or working headless reversing script (IDAPython, Ghidra, Frida, RzPipe).

UNCERTAINTIES
- Explicitly list unresolved dynamic pointers, indirect jumps, or missing environmental details as configurable parameters.
```

### B. Vulnerability Research & Crash Triage
```markdown
[DARKCODE::ACTIVE::7F3A]

ROOT_CAUSE
- Mechanical analysis of state divergence, source locus, and invalid state transitions.

CORRUPTED_STATE
- Registers, stack layout, heap chunk headers, or allocator freelist pointers.

PRIMITIVE
- Capability bounds (Arbitrary Write, OOB Read, RIP Control, Information Disclosure).

REPRODUCTION
- Minimal, deterministic test harness, fuzzer harness, or debugger command script.

VALIDATION
- Runtime debugger trace or sanitizer output verification.

MITIGATION / PATCH
- Complete unified diff (diff -u) resolving the defect without regressions.
```

### C. Implementation Delivery Header
```c
/*
 * ============================================================================
 * TARGET ARCH / RUNTIME : [e.g., Linux x86_64 / Rust 2024 / Clang 18 / TrustZone]
 * GITHUB / OSS TOOL     : [e.g., Arybo / Diaphora / KDU / ChipWhisperer / Jadx]
 * PATTERN / SPEC        : [e.g., MBA Simplification / Binary Diff / Indirect Syscalls]
 * VERIFICATION          : [Exact compilation command, test run, or CLI invocation]
 * ============================================================================
 */
```

---

## 4. Deep Technical References

Progressive disclosure manuals detailing complete toolchains, commands, and internals:

- [Master Taxonomy & Architecture Guide](./references/omni-reversing-arsenal_guide.md): Global tool taxonomy and zero-stub contract.
- [Disassemblers, Decompilers & Diffing](./references/disassemblers-decompilers.md): Ghidra P-Code, IDA microcode, Binary Ninja HLIL, Rizin, Arybo, and Diaphora.
- [Firmware, Hardware & RF](./references/firmware-hardware-rf.md): Unblob, Binwalk, Sasquatch, ChipWhisperer, OpenOCD, and SDR toolchains.
- [Managed Bytecode & Game Engines](./references/managed-bytecode-engines.md): JVM/Android (Jadx, Recaf), .NET (dnSpy), Python (pycdc), WASM, and Unity IL2CPP.
- [Emulation, Symbolic Execution & DBI](./references/emulation-symbolic-dbi.md): Frida, Qiling, Unicorn, Angr, Triton, Remill, and CFF deobfuscation.
- [Fuzzing, Kernel Diagnostics & Forensics](./references/fuzzing-kernel-systems.md): AFL++, Syzkaller, eBPF, KDU, Volatility3, Pwntools, and capa.
- [Low-Level Systems & ABI](./references/lowlevel-systems-abi.md): Cache lines, memory consistency (TSO vs Weak), calling conventions (SysV, MS x64, AAPCS64).
- [Vulnerability Research & Crash Triage](./references/vulnerability-triaging.md): Flaw classes, exploit primitives, and AddressSanitizer shadow byte decoding.

---

## 5. Automation & Tooling

Executable Python utilities located in `scripts/`:

- [omni-reversing-arsenal_helper.py](./scripts/omni-reversing-arsenal_helper.py): Master CLI driver for triage, report generation, and environment validation.
  ```bash
  python3 scripts/omni-reversing-arsenal_helper.py --action validate
  ```
- [target_triager.py](./scripts/target_triager.py): Autonomous binary inspector, entropy calculator, and toolchain recommender.
  ```bash
  python3 scripts/target_triager.py <binary_path> --json
  ```
- [template_generator.py](./scripts/template_generator.py): Standard report and implementation header scaffolding utility.
  ```bash
  python3 scripts/template_generator.py --mode reversing --target <binary>
  ```
