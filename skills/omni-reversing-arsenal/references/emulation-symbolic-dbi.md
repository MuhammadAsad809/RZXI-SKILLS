# Dynamic Instrumentation, Emulation, Symbolic Execution & Lifting

`[DARKCODE::REFERENCE::EMULATION_SYMBOLIC_DBI::v1.0]`

## 1. Dynamic Binary Instrumentation (DBI) & Hooking

### A. Frida (`frida/frida`)
- **Core Orchestration**:
  - `Interceptor.attach(targetAddress, { onEnter(args) { ... }, onLeave(retval) { ... } })`: Function hooking with register and argument modification.
  - `Memory.scan(base, size, pattern, callbacks)`: In-memory signature and pattern searching.
  - `CModule`: Compiling inline C code inside the target process space for sub-microsecond DBI hooks without JS bridge overhead.
  - RPC exports via Python `script.exports_sync` for headless automation.

### B. Intel PIN & DynamoRIO
- **`intel/pin`**: Pintool development in C/C++; instruction-level callbacks (`INS_AddInstrumentFunction`), basic block counters, and cache simulation.
- **`DynamoRIO/dynamorio`**: Open-source DBI runtime with client extensions (`drmgr`, `drwrap`, `drx`) for dynamic code cache management, instruction tracing, and taint tracking.

---

## 2. Emulation, Symbolic Execution & Concolic Engines

### A. Unicorn Engine & Qiling Framework
- **`unicorn-engine/unicorn`**: Lightweight multi-architecture CPU emulator (ARM, ARM64, MIPS, x86, RISC-V) based on QEMU core. Provides instruction hooks (`UC_HOOK_CODE`), memory read/write hooks (`UC_HOOK_MEM_READ | UC_HOOK_MEM_WRITE`), and register state access.
- **`qilingframework/qiling`**: Advanced full-system userland/kernel OS emulator:
  - Cross-platform: Emulates Linux, Windows, macOS, UEFI, FreeRTOS, and MCU environments.
  - Simulates syscalls, dynamic linkers, PEB/TEB structures, IOCTL dispatchers, and hardware peripherals without virtual machines.

### B. Symbolic Execution Engines
- **`angr/angr`**: Python-based multi-architecture binary analysis platform:
  - `CFGFast` & `CFGAccurate`: Static and dynamic control flow graph reconstruction.
  - `SimulationManager`: State exploration using symbolic execution engines, exploring paths to target addresses (`explore(find=..., avoid=...)`).
  - Symbolic memory modeling with claripy constraint solving.
- **`JonathanSalwan/Triton`**: Dynamic Symbolic Execution (DSE) library; instruction lifting, concolic execution, taint analysis, and AST simplification via Z3.
- **`cea-sec/miasm`**: Python reverse engineering framework implementing JIT emulation, expression simplification, and symbolic execution of obfuscated assembly.

---

## 3. Binary Lifting & Intermediate Representations

### A. Lifting Bits Suite
- **`lifting-bits/remill`**: Machine code lifter translating x86, x64, and AArch64 machine instructions into LLVM IR bitcode.
- **`lifting-bits/mctoll`**: Static binary translator raising binary executables directly into LLVM IR.
- **`lifting-bits/anvill`**: Automated binary-to-LLVM decompilation framework.

### B. RetDec (`avast/retdec`)
- Retargetable machine code decompiler translating raw binary code into structured C source code via LLVM IR optimization passes.

---

## 4. Deobfuscation & Anti-Analysis Defeat

### A. Control-Flow Flattening (CFF / OLLVM)
- **Detection**: Identifying state variable switch dispatches inside an outer loop.
- **De-flattening Workflow**:
  1. Recover the state variable dispatcher block and conditional assignments.
  2. Map state values to relevant basic block payloads.
  3. Rewrite conditional branches directly to successor blocks, bypassing the dispatcher.
  4. Fix relocations and control flow edges.

### B. VM-Based Obfuscators & Virtualization
- **Analysis Workflow**:
  1. Identify Virtual Program Counter (`vPC`), Virtual Stack (`vSP`), and Virtual Registers.
  2. Extract opcode dispatch loop and mapping table.
  3. Reverse individual virtual instruction handlers (e.g. `vADD`, `vXOR`, `vLOAD`, `vJMP`).
  4. Disassemble virtual bytecode and lift back to native assembly or C representations.

### C. Anti-Debugging & Anti-VM Neutralization
- **PEB Flags**: Neutralizing `BeingDebugged`, `NtGlobalFlag`, and heap flags.
- **APIs**: Hooking or patching `NtQueryInformationProcess` (`ProcessDebugPort`, `ProcessDebugObjectHandle`).
- **Timing & Hardware Traps**: Patching `RDTSC`/`RDTSCP` timing delta checks; masking hardware breakpoint registers (`DR0`-`DR7`) in SEH/VEH exception context records.
