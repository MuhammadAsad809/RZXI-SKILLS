# Low-Level Systems, Hardware Architecture, ABI & Concurrency

`[DARKCODE::REFERENCE::LOWLEVEL_SYSTEMS_ABI::v1.0]`

## 1. Hardware Architecture, Caches & Memory Consistency

### A. Cache Hierarchies & Coherence Protocols
- **Topology**: L1i / L1d (32–64 KB, 4–5 cycle latency, per-core), L2 (512 KB–1 MB, 12–14 cycle latency, non-inclusive/inclusive), L3 (shared victim cache, 30–50 cycle latency).
- **Line Alignment & False Sharing**: Standard 64-byte cache lines. Prevent false sharing in concurrent multi-threaded data structures with `alignas(64)` padding on write-hot state.
- **NUMA Topology**: Non-Uniform Memory Access boundaries; penalty of cross-socket QPI/UPI bus traversals for shared state.

### B. Memory Consistency Models
- **x86-64 Total Store Order (TSO)**:
  - Hardware enforces `Load-Load`, `Store-Store`, and `Load-Store` ordering.
  - Only `Store-Load` reordering is permitted (stores can be delayed in store buffers).
  - Explicit synchronization: `mfence` or `lock`-prefixed atomic instructions (`lock cmpxchg`).
- **AArch64 / RISC-V Weak Memory Ordering**:
  - Out-of-order execution allows arbitrary load/store reordering.
  - Sequential consistency requires acquire-release semantics: `ldar` (Load-Acquire) and `stlr` (Store-Release).
  - Memory barriers: `dmb ish` (Data Memory Barrier, Inner Shareable) and `isb` (Instruction Synchronization Barrier).

---

## 2. ABI & Calling Conventions

### A. System V AMD64 ABI (Linux, BSD, macOS)
- **Argument Registers (Integer/Pointer)**:
  1. `RDI`
  2. `RSI`
  3. `RDX`
  4. `RCX`
  5. `R8`
  6. `R9`
- **Return Registers**: `RAX` (64-bit), `RDX:RAX` (128-bit), `XMM0` (floating-point).
- **Callee-Saved Registers**: `RBX`, `RSP`, `RBP`, `R12`, `R13`, `R14`, `R15`.
- **Red Zone**: 128-byte region below `%rsp` that functions can use for temporary scratch storage without adjusting `%rsp`. Signals and interrupts must not clobber this region.

### B. Microsoft x64 Calling Convention (Windows)
- **Argument Registers**:
  1. `RCX`
  2. `RDX`
  3. `R8`
  4. `R9`
- **Return Register**: `RAX`.
- **Shadow Space (Home Space)**: Caller MUST allocate 32 bytes of stack space (`sub rsp, 0x20` / `0x28` with alignment) immediately prior to `call`, reserved for the callee to spill `RCX`, `RDX`, `R8`, `R9`.
- **Callee-Saved Registers**: `RBX`, `RBP`, `RDI`, `RSI`, `RSP`, `R12`, `R13`, `R14`, `R15`, `XMM6`-`XMM15`.

### C. AAPCS64 (ARM 64-bit Architecture Procedure Call Standard)
- **Argument Registers**: `X0` through `X7`.
- **Return Registers**: `X0` (or `X0`-`X1` for 128-bit).
- **Special Registers**:
  - `X29`: Frame Pointer (`FP`).
  - `X30`: Link Register (`LR`), holds return address after `BL`/`BLR`.
  - `SP`: Stack Pointer (must be 16-byte aligned at all public interface boundaries).
- **Callee-Saved Registers**: `X19` through `X28`.

---

## 3. Kernel Subsystems & OS Internals

### A. Linux Kernel Internals
- **SLUB Allocator**: Object caching, freelist pointer obfuscation, slab pages, and kmalloc caches.
- **Virtual Memory Architecture**: Virtual Memory Areas (`vm_area_struct`), page table hierarchy (PGD -> P4D -> PUD -> PMD -> PTE), copy-on-write (`COW`).
- **Synchronization**: RCU (Read-Copy-Update) wait-free reader traversal with deferred reclamation grace periods (`synchronize_rcu`).

### B. Windows Kernel Architecture
- **Object Manager**: Executive object headers (`OBJECT_HEADER`), handle tables, security descriptors.
- **I/O Request Packets (IRP)**: Major/minor function codes, IOCTL completion routines, asynchronous I/O completion.
- **Virtual Address Descriptors (VAD)**: Balanced binary trees describing user-mode process address space allocations.
- **IRQL (Interrupt Request Levels)**: `PASSIVE_LEVEL` (0), `APC_LEVEL` (1), `DISPATCH_LEVEL` (2), `DIRQL` (3-26). Page faults are fatal at `DISPATCH_LEVEL` or higher.

---

## 4. Systems Architecture, Distributed Consensus & Concurrency

### A. High-Performance Concurrency Primitives
- **Lock-Free Ring Buffers**: Single-Producer Multiple-Consumer (SPMC) and MPMC queues using circular buffers and CAS loops.
- **Memory Reclamation**: Hazard pointers and epoch-based reclamation (EBR) to prevent Use-After-Free in lock-free concurrent readers.
- **Zero-Copy Serialization**: Memory-mapped flat buffers, `Cow` (Clone-on-Write) semantics, and typestate validation patterns.

### B. Distributed Systems
- **Consensus Algorithms**: Raft leader election and log replication invariants; Multi-Paxos state machine replication.
- **Conflict-Free Replicated Data Types (CRDTs)**: State-based (CvRDT) and operation-based (CmRDT) convergence models.
