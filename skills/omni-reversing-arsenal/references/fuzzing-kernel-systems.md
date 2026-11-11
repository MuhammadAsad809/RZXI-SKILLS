# Fuzzing, Kernel Diagnostics, Forensics & Exploit Research

`[DARKCODE::REFERENCE::FUZZING_KERNEL_SYSTEMS::v1.0]`

## 1. Advanced Fuzzing, Sanitizers & Protocol Testing

### A. Coverage-Guided Fuzzing Frameworks
- **`AFLplusplus/AFLplusplus`**:
  - LLVM instrumentation mode (`afl-clang-fast`, `afl-clang-lto`).
  - Persistent in-memory fuzzing harnesses using `__AFL_LOOP(10000)` to eliminate `fork()` overhead.
  - Sanitizer integration: AddressSanitizer (`AFL_USE_ASAN=1`), MemorySanitizer (`AFL_USE_MSAN=1`), UndefinedBehaviorSanitizer (`AFL_USE_UBSAN=1`).
  - Custom mutators via C/Python mutator API (`afl_custom_fuzz`).
- **`google/honggfuzz`**:
  - Hardware-assisted feedback using Intel Processor Trace (Intel PT) and CPU performance branch counters.
  - Multithreaded execution with automated crash deduplication and signal interception.
- **`google/syzkaller`**:
  - State-of-the-art unsupervised, grammar-driven kernel fuzzer.
  - Defining syscall descriptions and constraints in declarative format (`sys/linux/*.txt`, `sys/windows/*.txt`).
  - Automated VM orchestration (QEMU/KVM) and crash reproducer generation (`.c` syz-repro).

### B. Grammar & Protocol Fuzzers
- **`MozillaSecurity/dharma`**: Generation-based grammar fuzzer for complex structured inputs, file formats, and JIT compilers.
- **`fuzzowski/fuzzowski`**: Network protocol fuzzer based on Boofuzz with state machine transition monitoring and live socket carving.
- **`trailofbits/deepstate`**: Unit-testing interface combining symbolic execution and fuzzing backends (libFuzzer, AFL, Angr, Manticore).

---

## 2. Kernel Diagnostics, Tracing & Driver Analysis

### A. Windows Kernel Internals & Driver Utilities
- **`hfiref0x/KDU` (Kernel Driver Utility)**: Driver Signature Enforcement (DSE) bypass research exploiting vulnerabilities in signed third-party drivers to execute ring0 code.
- **`matterpreter/DefenderCheck`**: Binary bisection tool identifying exact byte ranges triggering static antivirus/EDR signatures.
- **`Snovvcrash/DInjector`**: In-memory PE loading, unhooking mechanisms, and APC injection routines.
- **`tandasat/Kernel-Mode-Exploitation`**: Windows kernel exploitation primitives, Pool chunk manipulation, and Token stealing patterns.

### B. Linux Kernel Diagnostics & eBPF
- **`The-Z-Labs/linux-exploit-suggester`**: Kernel vulnerability auditing based on compile flags, kernel release strings, and enabled security mitigations.
- **`iovisor/bcc` & `libbpf/libbpf`**: BPF Compiler Collection and modern CO-RE (Compile Once – Run Everywhere) eBPF programs for non-invasive tracing.
- **`iovisor/bpftrace`**: High-level tracing language for Linux kernels, attaching probes to kprobes, kretprobes, uprobes, and tracepoints.

### C. Forensics, Hypervisors & Debugging
- **`volatilityfoundation/volatility3`**: Memory forensics framework for analyzing physical RAM dumps, recovering process trees, network sockets, and kernel modules.
- **`intel/IntelPT` & `tandasat/HyperPlatform`**: Hardware execution tracing and lightweight Intel VT-x hypervisors for stealthy kernel breakpointing and instruction tracking.
- **`kdlib/kdlib`**: Python scripting engine for WinDbg / DbgEng kernel and userland debugging.

---

## 3. Exploit Research, Triage & Network Analysis

### A. Exploit Automation & ROP Gadgetry
- **`Gallopsled/pwntools`**: Standard Python exploitation framework (`remote`, `process`, `ELF`, `ROP`, `p32`, `p64`).
- **ROP Gadget Finders**:
  - `JonathanSalwan/ROPgadget`: CLI gadget scanner with automated ROP chain generator.
  - `sashs/Ropper`: Multi-architecture gadget and JOP/dispatcher finder.
  - `0vercl0k/rp`: Ultra-fast C++ gadget finder for x86/x64 binaries.
- **Debugger Enhancements**:
  - `pwndbg/pwndbg` & `hugsy/gef`: GDB plugins providing contextual registers, stack, disassembly views, and glibc heap analyzers (`vis_heap_chunks`, `bins`).

### B. Binary Formats, Carving & Capability Triage
- **`erocarrera/pefile` & `eliben/pyelftools`**: Python modules for parsing PE and ELF headers, relocations, sections, and symbols.
- **`mandiant/capa`**: Automated capability identifier detecting binary behaviors (cryptography, persistence, injection) via rule matching.
- **`VirusTotal/yara` & `mandiant/FLOSS`**: Pattern-matching engine and automated obfuscated string deobfuscator.

### C. Network Protocol & Traffic Analysis
- **`secdev/scapy`**: Interactive packet manipulation and protocol forging in Python.
- **`zeek/zeek` & `wireshark/tshark`**: Network security monitoring, metadata extraction, and packet stream dissection.
- **`mitmproxy/mitmproxy`**: Interactive SSL/TLS-intercepting HTTP proxy with Python scripting hooks.
