# Disassemblers, Decompilers, Deobfuscation & Binary Diffing

`[DARKCODE::REFERENCE::DISASSEMBLERS_DECOMPILERS::v1.0]`

## 1. The Big Four Disassemblers & Decompilers

### A. NSA Ghidra (`NationalSecurityAgency/ghidra`)
- **Headless Execution**: Automation via `analyzeHeadless <project_dir> <project_name> -import <target> -postScript <script.py>`.
- **Python / Jython & Ghidra Bridge**: Scripting via FlatProgramAPI and Ghidra Bridge (connecting modern Python 3 to Ghidra Jython environment).
- **P-Code AST Manipulation**: Low-level instruction semantics manipulation via `HighFunction`, `Varnode`, and `PcodeOp`.
- **Custom SLEIGH Specs**: Developing processor definitions (`.slaspec`, `.sinc`) for non-standard or proprietary architectures.
- **Type Injection**: Programmatic struct definition and data type manager injection via C header parsing or Java/Python APIs.

### B. IDA Pro & Hex-Rays (`HexRaysSA`)
- **IDAPython Architecture**: Supporting v7.x, v8.x, and v9.x API modularization:
  - `ida_bytes`: Direct byte, flag, and item manipulation.
  - `ida_funcs`: Function boundary queries, chunk management, and frame pointers.
  - `ida_hexrays`: Decompiler AST manipulation (`cfunc_t`, `citem_t`, `cinsn_t`, `cexpr_t`).
  - `ida_xref`: Cross-reference collection (code and data xrefs).
- **Hex-Rays Microcode SDK**: Intermediate Representation optimization plugins via `cblist_t`, `mop_t`, and `minsn_t` to strip obfuscation layers prior to AST generation.
- **AST/C-Tree Mutation**: Decompiler tree transformation to rename variables, inline obfuscated trampolines, and normalize control flow.

### C. Binary Ninja (`Vector35/binaryninja-api`)
- **Tiered Intermediate Languages**:
  - **LLIL (Low Level IL)**: Architecture-independent expression of instruction semantics.
  - **MLIL (Medium Level IL)**: Variable and parameter identification, stack variable resolution.
  - **HLIL (High Level IL)**: High-level control flow structures (if/while/switch) approaching C AST.
  - **SSA Forms**: Single Static Assignment variants for LLIL, MLIL, and HLIL for data-flow tracking and def-use chains.
- **Custom Architectures & Lifters**: Extending `Architecture` base class to support exotic microcontrollers.

### D. Rizin & Radare2 (`rizinorg/rizin`, `radareorg/radare2`)
- **Headless Automation**: Scripting via `rzpipe` (or `r2pipe`) in Python, interacting with headless core via JSON commands (`ij`, `pdfj`, `aflj`).
- **Signature Generation**: Zignatures (`zg`, `zp`) for pattern recognition across stripped binaries.
- **Control Flow Graphs**: Command-line CFG rendering (`agf`, `agfd`) and graph exports (DOT, JSON).
- **Binary Patching**: In-place instruction modification with `wa` and opcode writing with `wx`.

---

## 2. Exotic Deobfuscation, MBA Reduction & Binary Diffing

### A. Symbolic SMT Deobfuscators
- **`quarkslab/arybo`**: Expression manipulation and simplification engine using Z3 bit-vector arithmetic to unroll Mixed Boolean-Arithmetic (MBA) expressions into canonical algebraic formulas.
- **`mrphrazer/obfa`**: Automated heuristic and concolic detection and normalization of opaque predicates and flattened control-flow loops.
- **`RobinDavid/Docovery`**: Symbolic execution-based detection of dead code paths, dead registers, and opaque conditional jumps.
- **`sogeti-esec-lab/Luz-PreProcess`**: Microcode deobfuscation framework combining LLVM passes and MBA simplification.

### B. Binary Diffing & Semantic AST Matching
- **`joxeankoret/diaphora`**: The most advanced open-source binary diffing tool:
  - Compares functions using heuristics, AST subtrees, call graphs, and pseudo-code hashes.
  - Matches across different architectures, compilers, and optimization flags.
  - Exports diff databases and automates symbol and comment porting.
- **`google/bindiff`**: Standard graph-theoretic comparison engine analyzing basic block topology and edge counts.
- **`0xec/IdaClang`**: Clang-based C++ struct and header parser to inject typed debug symbols into IDA Pro databases from source.
