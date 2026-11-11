# Omni Systems Reversing & Toolchain Arsenal — Master Architecture & Taxonomy

`[DARKCODE::REFERENCE::OMNI_ARSENAL_TAXONOMY::v1.0]`

This master guide establishes the operational taxonomy, tool ecosystem, and execution workflows across all reversing, low-level engineering, and hardware targets.

---

## 1. Modular Architecture Matrix

Domain Category | Key GitHub Repos & Toolchains | Reference Module
:--- | :--- | :---
**Disassemblers & Decompilers** | Ghidra, IDA Pro, Binary Ninja, Rizin, Radare2 | [Disassemblers & Decompilers](./disassemblers-decompilers.md)
**Deobfuscation & AST Diffing** | Arybo, Obfa, Docovery, Diaphora, BinDiff | [Disassemblers & Decompilers](./disassemblers-decompilers.md)
**Firmware, ROM & Hardware** | Unblob, Binwalk, Sasquatch, ChipWhisperer, OpenOCD | [Firmware & Hardware](./firmware-hardware-rf.md)
**SDR & Wireless RF** | GNURadio, rtl_433, HackRF, Ubertooth, Osmocom-bb | [Firmware & Hardware](./firmware-hardware-rf.md)
**Java, Android & DEX** | Recaf, Krakatau, Fernflower, Jadx, Apktool | [Managed Bytecode](./managed-bytecode-engines.md)
**Game Engines & Memory** | AssetRipper, Il2CppDumper, UE4SS, Cheat Engine | [Managed Bytecode](./managed-bytecode-engines.md)
**Managed Runtimes** | dnSpy, ILSpy, de4dot, pycdc, pyinstxtractor, wabt | [Managed Bytecode](./managed-bytecode-engines.md)
**DBI, Hooking & Tracing** | Frida, Intel PIN, DynamoRIO | [Emulation, DBI & Symbolic](./emulation-symbolic-dbi.md)
**Emulation & Symbolic Exec** | Unicorn, Qiling, Angr, Triton, Miasm | [Emulation, DBI & Symbolic](./emulation-symbolic-dbi.md)
**Binary Lifting** | Remill, McSema/McToll, Anvill, RetDec | [Emulation, DBI & Symbolic](./emulation-symbolic-dbi.md)
**Coverage-Guided Fuzzing** | AFL++, Honggfuzz, Syzkaller, DeepState, Dharma | [Fuzzing & Kernel Systems](./fuzzing-kernel-systems.md)
**Kernel & Hypervisors** | KDU, DefenderCheck, eBPF (BCC, bpftrace), Volatility3 | [Fuzzing & Kernel Systems](./fuzzing-kernel-systems.md)
**Exploit Research & Triage** | Pwntools, ROPgadget, Ropper, Pwndbg, GEF | [Fuzzing & Kernel Systems](./fuzzing-kernel-systems.md)
**Systems Architecture & ABI** | SysV AMD64, MS x64, AAPCS64, Cache Line Coherence | [Low-Level Systems & ABI](./lowlevel-systems-abi.md)
**Vulnerability & Crash Triage** | ASan Decodes, Root Cause Analysis, Mitigation Models | [Vulnerability Research](./vulnerability-triaging.md)

---

## 2. Operational Axioms & Zero-Stub Contract

Every technical deliverable produced under this arsenal adheres to the compilation and fidelity contract:
1. **Zero Stubs**: Never emit `TODO`, `pass`, or placeholder functions. All generated C, C++, Rust, Python, and assembly code must be complete and syntactically valid.
2. **Deterministic Typing**: Explicit integer widths (`uint64_t`, `u64`, `int32_t`), byte alignment attributes (`__attribute__((aligned(64)))`, `alignas(64)`), and compile-time struct assertions (`static_assert(sizeof(...) == ..., "...")`).
3. **Parameter Invariance**: Runtime addresses, ASLR bases, dynamic offsets, and target symbols must be exposed as typed arguments or configuration macros rather than fabricated constants.
4. **Structured Delivery**: Output must follow the designated schemas defined in [Vulnerability Triaging](./vulnerability-triaging.md).
