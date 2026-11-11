#!/usr/bin/env python3
"""
target_triager.py — Target Format Inspector & Toolchain Recommender

Autonomous triaging utility for binary analysis, firmware carving, and runtime targets.
Uses standard Python libraries to:
1. Parse magic bytes and file signatures (ELF, PE, Mach-O, DEX, Java Class, WASM, SquashFS, PCAP, etc.)
2. Calculate Shannon entropy to detect packed, compressed, or encrypted payloads
3. Map target characteristics to the GitHub Reversing Toolchain Arsenal
4. Emit structured JSON for agent integration
"""

import sys
import os
import math
import json
import struct
import argparse
from pathlib import Path
from typing import Dict, List, Any, Tuple


# Signature mapping table
SIGNATURES = [
    (b"\x7fELF", "ELF Binary", ["readelf", "pyelftools", "ghidra", "rizin", "angr"]),
    (b"MZ", "PE Windows Executable", ["pefile", "capa", "floss", "ida-pro", "ghidra", "kdu"]),
    (b"\xfe\xed\xfa\xce", "Mach-O 32-bit (BE)", ["ghidra", "rizin"]),
    (b"\xfe\xed\xfa\xcf", "Mach-O 64-bit (BE)", ["ghidra", "rizin"]),
    (b"\xce\xfa\xed\xfe", "Mach-O 32-bit (LE)", ["ghidra", "rizin"]),
    (b"\xcf\xfa\xed\xfe", "Mach-O 64-bit (LE)", ["ghidra", "rizin"]),
    (b"\xca\xfe\xba\xbe", "Java Class / Fat Mach-O", ["recaf", "krakatau", "jd-gui"]),
    (b"dex\n", "Android DEX Bytecode", ["jadx", "apktool", "recaf"]),
    (b"PK\x03\x04", "ZIP / JAR / APK / DOCX", ["unzip", "apktool", "jadx", "unblob"]),
    (b"\x00asm", "WebAssembly (WASM)", ["wabt", "wasm2wat", "wasm-decompile"]),
    (b"hsqs", "SquashFS Little-Endian", ["unsquashfs", "sasquatch", "unblob", "binwalk"]),
    (b"sqsh", "SquashFS Big-Endian", ["unsquashfs", "sasquatch", "unblob", "binwalk"]),
    (b"\xd4\xc3\xb2\xa1", "PCAP Capture (LE)", ["tshark", "wireshark", "scapy", "zeek"]),
    (b"\xa1\xb2\xc3\xd4", "PCAP Capture (BE)", ["tshark", "wireshark", "scapy", "zeek"]),
    (b"\x0a\x0d\x0d\x0a", "PCAPNG Capture", ["tshark", "wireshark", "zeek"]),
    (b"\x1f\x8b", "Gzip Compressed Blob", ["gunzip", "binwalk", "unblob"]),
    (b"BZh", "Bzip2 Compressed Blob", ["bunzip2", "binwalk", "unblob"]),
    (b"7z\xbc\xaf\x27\x1c", "7-Zip Archive", ["7z", "unblob"]),
]


def calculate_entropy(data: bytes) -> float:
    """Calculates Shannon entropy of raw byte buffer."""
    if not data:
        return 0.0
    byte_counts = [0] * 256
    for b in data:
        byte_counts[b] += 1
    entropy = 0.0
    length = len(data)
    for count in byte_counts:
        if count > 0:
            p = count / length
            entropy -= p * math.log2(p)
    return round(entropy, 4)


def inspect_elf(header_data: bytes) -> Dict[str, Any]:
    """Inspects standard ELF 32/64 header fields."""
    info = {"format": "ELF"}
    if len(header_data) < 18:
        return info
    ei_class = header_data[4]
    info["bitness"] = "64-bit" if ei_class == 2 else "32-bit" if ei_class == 1 else "Unknown"
    ei_data = header_data[5]
    info["endianness"] = "Little-Endian" if ei_data == 1 else "Big-Endian" if ei_data == 2 else "Unknown"
    
    e_type_raw = header_data[16:18]
    endian = "<" if ei_data == 1 else ">"
    if len(e_type_raw) == 2:
        e_type = struct.unpack(f"{endian}H", e_type_raw)[0]
        types = {1: "ET_REL (Relocatable)", 2: "ET_EXEC (Executable)", 3: "ET_DYN (Shared object / PIE)", 4: "ET_CORE"}
        info["type"] = types.get(e_type, f"Unknown ({hex(e_type)})")
    return info


def inspect_pe(file_path: Path) -> Dict[str, Any]:
    """Inspects basic PE header fields."""
    info = {"format": "PE"}
    try:
        with open(file_path, "rb") as f:
            dos_header = f.read(64)
            if len(dos_header) < 64:
                return info
            e_lfanew = struct.unpack("<I", dos_header[60:64])[0]
            f.seek(e_lfanew)
            pe_sig = f.read(4)
            if pe_sig != b"PE\x00\x00":
                return info
            coff_header = f.read(20)
            if len(coff_header) == 20:
                machine, sections, time_date, _, _, opt_size, chars = struct.unpack("<HHIIIHH", coff_header)
                machines = {0x14c: "i386 (32-bit)", 0x8664: "AMD64 (64-bit)", 0xaa64: "ARM64", 0x1c0: "ARM"}
                info["machine"] = machines.get(machine, f"Unknown ({hex(machine)})")
                info["section_count"] = sections
    except Exception as e:
        info["error"] = str(e)
    return info


def triage_file(file_path: Path) -> Dict[str, Any]:
    """Triages target file and yields analysis summary and recommended toolchains."""
    if not file_path.exists():
        return {"status": "error", "message": f"Target not found: {file_path}"}
    if file_path.is_dir():
        return {
            "status": "success",
            "type": "directory",
            "path": str(file_path),
            "file_count": sum(1 for _ in file_path.rglob("*") if _.is_file()),
            "recommended_tools": ["ripgrep", "binwalk", "tree"]
        }

    file_size = file_path.stat().st_size
    with open(file_path, "rb") as f:
        head_sample = f.read(min(file_size, 65536))
    
    entropy = calculate_entropy(head_sample)
    is_high_entropy = entropy > 7.2

    detected_type = "Raw / Unknown Binary"
    recommended_tools = ["ghidra", "rizin", "binwalk", "strings"]
    details: Dict[str, Any] = {}

    for magic, name, tools in SIGNATURES:
        if head_sample.startswith(magic):
            detected_type = name
            recommended_tools = tools
            break

    if detected_type == "ELF Binary":
        details = inspect_elf(head_sample)
    elif detected_type == "PE Windows Executable":
        details = inspect_pe(file_path)

    classification = "Normal / Uncompressed"
    if is_high_entropy:
        classification = "High Entropy (Likely Packed, Encrypted, or Compressed)"

    return {
        "status": "success",
        "file_name": file_path.name,
        "file_size": file_size,
        "detected_type": detected_type,
        "shannon_entropy": entropy,
        "classification": classification,
        "metadata": details,
        "recommended_tools": recommended_tools,
        "recommended_references": [
            "references/disassemblers-decompilers.md" if "ghidra" in recommended_tools else "",
            "references/firmware-hardware-rf.md" if "binwalk" in recommended_tools else "",
            "references/managed-bytecode-engines.md" if any(t in ["jadx", "apktool", "recaf"] for t in recommended_tools) else "",
            "references/fuzzing-kernel-systems.md" if "pefile" in recommended_tools or "pyelftools" in recommended_tools else ""
        ]
    }


def main():
    parser = argparse.ArgumentParser(description="Autonomous Target Triager & Toolchain Recommender")
    parser.add_argument("target", help="Path to binary file or archive to triage")
    parser.add_argument("--json", action="store_true", help="Emit output as machine-readable JSON")
    args = parser.parse_args()

    result = triage_file(Path(args.target))

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if result.get("status") != "success":
            print(f"[!] Error: {result.get('message')}")
            sys.exit(1)
        print(f"=== Target Triage: {result.get('file_name', result.get('path'))} ===")
        print(f"  Detected Type:  {result.get('detected_type')}")
        print(f"  Entropy:        {result.get('shannon_entropy', 0.0)} ({result.get('classification', '')})")
        print(f"  Tools:          {', '.join(result.get('recommended_tools', []))}")
        if result.get("metadata"):
            for k, v in result["metadata"].items():
                print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
