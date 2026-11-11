# Firmware Extraction, Hardware Dissection & RF Analysis

`[DARKCODE::REFERENCE::FIRMWARE_HARDWARE_RF::v1.0]`

## 1. Firmware Unpacking & ROM Carving

### A. Extraction Frameworks
- **`onekey-sec/unblob`**: Modern recursive binary extractor and carved image analyzer. Recursively extracts nested archives, compressed filesystems, and proprietary firmware headers without execution sandboxes.
- **`ReFirmLabs/binwalk`**: Signature-based firmware scanner.
  - Carving filesystems: `binwalk -eM <firmware.bin>` (recursive extraction).
  - Entropy graphing: `binwalk -E <firmware.bin>` to locate encrypted or compressed regions.
- **`devttys0/sasquatch`**: Patched SquashFS utilities supporting non-standard vendor compression (LZMA, LZO variants) frequently found in embedded IoT routers.
- **`sviehb/jefferson`**: Pure Python filesystem extractor for JFFS2 (Journaling Flash File System v2), handling endianness inversion and marker byte irregularities.

### B. Bootloader & Platform Firmware Tools
- **`corna/me_cleaner`**: Tool for neutralizing and minimizing Intel Management Engine (ME) firmware modules on x86 platforms.
- **`plaidyc/vboot-tools`**: Parsing and validating ChromeOS and embedded verified boot partition tables and cryptographic descriptors.
- **`msr-quandary/msr-tools`**: Low-level reading and writing of x86 Model-Specific Registers (`rdmsr`, `wrmsr`) to inspect CPU security registers (MTRR, IA32_FEATURE_CONTROL).

---

## 2. Hardware Debugging & Fault Injection

### A. JTAG / SWD & Flash SPI Extraction
- **`openocd-org/openocd`**: On-Chip Debugger supporting ARM Cortex-M, Cortex-A, RISC-V, MIPS, and Xtensa cores via FTDI, J-Link, or CMSIS-DAP probes.
  - Command: `openocd -f interface/ftdi/... -f target/... -c "init; halt; dump_image flash.bin 0x08000000 0x100000"`
- **`flashrom/flashrom`**: Universal flash ROM programmer utility for SPI, LPC, FWH, and parallel flash chips via dedicated hardware programmers or bus pirates.

### B. Side-Channel Analysis & Fault Glitching
- **`newaetech/chipwhisperer`**: Hardware and Python automation suite for:
  - Differential Power Analysis (DPA) and Correlation Power Analysis (CPA) on hardware AES/DES implementations.
  - Clock and voltage glitching to induce instruction skips and fault transitions in secure boot loops.
- **`OP-TEE/optee_os`**: Open-source Trusted Execution Environment (TEE) reference implementation for ARM TrustZone architectures; analyzing Secure Monitor Call (SMC) handlers and trusted application isolation.

---

## 3. Software-Defined Radio (SDR) & RF Analysis

### A. Signal Processing & Demodulation
- **`gnuradio/gnuradio`**: High-performance digital signal processing (DSP) runtime and graphical flowgraph development environment (`gnuradio-companion`). Supports custom OOK, FSK, PSK, and QAM demodulation blocks.
- **`merbanan/rtl_433`**: Generic data receiver and multi-protocol decoder for ISM band devices (433.92 MHz, 868 MHz, 315 MHz, 915 MHz) using RTL-SDR dongles.

### B. Hardware Pipelines & Baseband Stacks
- **`mossmann/hackrf` & `greatscottgadgets/ubertooth`**:
  - `hackrf_transfer`: Raw I/Q sample capture and transmission across 1 MHz to 6 GHz.
  - `ubertooth-btle`: Sniffing and demodulating raw Bluetooth Low Energy (BLE) advertisements and connection state packets.
- **`osmocom/osmocom-bb`**: Free Software GSM baseband stack implementation running on Calypso-based baseband processors for Layer 1/2/3 GSM analysis.
- **`srsran/srsRAN`**: Open-source 4G/5G software radio suite implementing complete UE (User Equipment) and eNodeB/gNodeB baseband stacks over SDR hardware.
