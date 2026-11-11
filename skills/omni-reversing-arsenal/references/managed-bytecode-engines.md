# Managed Bytecode, Runtimes, Game Engines & Asset Extractors

`[DARKCODE::REFERENCE::MANAGED_BYTECODE_ENGINES::v1.0]`

## 1. Java, JVM, Android & DEX Ecosystem

### A. JVM Bytecode Inspection & Decompilation
- **`Col-E/Recaf`**: Modern Java bytecode editor with live constant pool editing, ASM integration, and control flow graph (CFG) visualization.
- **`Storyyeller/Krakatau`**: Bytecode assembler, disassembler, and decompiler designed to parse invalid, malformed, or hostile class files that crash standard decompilers.
- **`fesh0r/fernflower`**: Analytical decompiler powering IntelliJ IDEA's built-in Java decompiler engine.
- **`java-decompiler/jd-gui`**: Standalone graphical utility for browsing decompiled Java source code.

### B. Android & Dalvik/ART Extraction
- **`skylot/jadx`**: State-of-the-art Dex-to-Java decompiler supporting multi-DEX APKs, AARs, and DEX files with automatic renaming of obfuscated identifiers.
  - Headless CLI: `jadx -d out/ target.apk --deobf`
- **`iBotPeaches/Apktool`**: Reverse engineering Android applications; decodes binary XML, resources (`resources.arsc`), smali disassembly, and rebuilds APK packages.

### C. Defeating Java & Android Obfuscators
- **Obfuscation Engines**: ProGuard, R8, Allatori, Zelix KlassMaster (ZKM), DexGuard.
- **Counter-Measures**:
  - Identifying dynamic reflection lookup loops and decrypting constant string tables.
  - Normalizing mangled control flow loops (opaque branch unflattening).
  - Restoring class, method, and field signatures via heuristics, API cross-references, and intent action string patterns.

---

## 2. Game Engines, Assets & Live Memory Inspection

### A. Unity Engine Decompilation & Extraction
- **`AssetRipper/AssetRipper`**: Reconstructs complete Unity Editor projects from compiled `.assets`, AssetBundles, and Player executable data.
- **`Perfare/Il2CppDumper`**: Restores `assembly-csharp.dll` from native AOT compiled Unity binaries (`libil2cpp.so` or `GameAssembly.dll`) using `global-metadata.dat`.
  - Produces: `dump.cs` (structs, methods, offsets) and `script.json` (for IDA/Ghidra symbol recovery).

### B. Unreal Engine Modding & Struct Dumping
- **`flz/UE4SS`**: Unreal Engine 4/5 C++ Modding Framework. Injects live into game processes, dumps `UObject`, `UEnum`, `UStruct` reflection tables, and executes live Lua mod scripts.
- **`gildor2/UEViewer` (umodel)**: Extracts meshes, textures, animations, and sound packages from Unreal Engine packages (`.pak`, `.utoc`, `.ucas`).

### C. Live Memory Struct Mapping & Cheat Tools
- **`cheat-engine/cheat-engine`**: Memory scanning, pointer maps, auto-assembler scripts (`alloc`, `hook`), and Lua automation.
- **`ReClassNET/ReClass.NET`**: Interactive memory struct reverse engineering tool; maps raw memory structures, pointers, RTTI tables, and virtual function tables in live processes.

---

## 3. Managed Runtimes (.NET, Python, WASM, Electron)

### A. .NET & Common Language Runtime (CLR)
- **`icsharpcode/ILSpy` & `dnSpyEx/dnSpy`**: Core .NET decompilers and in-memory debuggers; edit C# or IL in place and recompile assemblies directly.
- **`0xd4d/de4dot`**: Automated .NET deobfuscator supporting ConfuserEx, Dotfuscator, SmartAssembly, Crypto Obfuscator, and agile.net.

### B. Python Bytecode & Frozen Executables
- **`bannsec/pyinstxtractor`**: PyInstaller Extractor; unpacks Windows/Linux PyInstaller executables into native `.pyc` bytecode files, restoring magic headers.
- **`zrax/pycdc` (Decompyle++)**: C++ based disassembler and decompiler for Python 3.x `.pyc` bytecode.
- **`rocky/python-uncompyle6`**: Python multi-version AST-based decompiler for legacy Python 2.x and early 3.x bytecodes.

### C. WebAssembly (WASM) & Electron
- **`WebAssembly/wabt`**: WebAssembly Binary Toolkit.
  - `wasm2wat`: Disassembles binary WASM into WebAssembly text format.
  - `wasm-decompile`: Decompiles WASM bytecode into C-like pseudocode.
- **`electron/asar`**: Archive packing and extraction tool for Electron applications (`app.asar`), recovering bundled JavaScript/TypeScript sources.
