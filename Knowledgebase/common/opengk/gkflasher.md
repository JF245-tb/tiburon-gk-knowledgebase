# GKFlasher — ECU Flashing Tool
**Repository:** https://github.com/Dante383/GKFlasher
**Wiki:** https://opengk.org/index.php?title=GKFlasher_Instructions
**Used on:** Blue Tiburon (stock Siemens ECU)

---

## Overview
GKFlasher is an open-source Python CLI/GUI tool for reading, writing, and tuning Siemens SIMK41/SIMK43 ECUs. Supports calibration data modification, program code updates, checksum correction, immobilizer programming, and BSL (Bootstrap Loader) operations.

## Hardware Required
- **USB-OBD2 interface cable.** FTDI chipset strongly preferred.
- **CH340 is supported as of GKFlasher v1.0.5** — the wiki's blanket "FTDI only" warning
  predates that. CH340 adapters are still *not* supported for BSL operations.
- Recommended: "Galletto 1260 ECU Chip Tuning Tool" (reliable + affordable, genuine FTDI)

## Installation (Windows)
1. Install Git 2.44.0 (64-bit) — select "Git from command line"
2. Install Python 3.11.9 (amd64) — enable "Add python.exe to PATH"
3. Restart, verify: `python -V` → Python 3.11.9, `git.exe -v` → git version 2.44.0
4. Clone: `mkdir "C:\GIT Repos" && cd "C:\GIT Repos" && git clone https://github.com/Dante383/GKFlasher`
5. Install deps: `cd GKFlasher && python -m pip install -r requirements.txt`
6. Launch GUI: `python gui.py`
7. Optional: NPCAP 1.79 for CAN bus support

## Installation (Linux)
```
sudo apt-get install git python3-pip
git clone https://github.com/Dante383/GKFlasher.git
cd GKFlasher
python3 -m pip install -r requirements.txt --break-system-packages
python3 gui.py
```

## Full CLI Parameters

```
python3 gkflasher.py --protocol {canbus/kline} --interface {can0//dev/ttyUSB0}
```

| Flag | Short | Description |
|------|-------|-------------|
| `--config {filename}` | `-c` | Load config file (default: gkflasher.yml). Use for multiple vehicle configs. |
| `--protocol {protocol}` | `-p` | `canbus` or `kline` |
| `--baudrate {baudrate}` | `-b` | Baud rate override |
| `--desired-baudrate {id}` | | Target baudrate identifier (see ecu_definitions.py) |
| `--interface {interface}` | `-i` | Interface name (e.g. `can0`, `/dev/ttyUSB0`, `COM3`) |
| `--read` | `-r` | Read full EEPROM → `output_{start}_{stop}.bin` |
| `--read-calibration` | | Read calibration zone only (auto-detects offset for ECU) |
| `--read-program` | | Read program zone only (auto-detects offset for ECU) |
| `--id` | | Display ECU identification parameters (KWP service 0x1A) |
| `--output {filename}` | `-o` | Override output filename for reads |
| `--address-start {offset}` | `-s` | Start offset for partial read/write |
| `--address-stop {offset}` | `-e` | End offset for partial read/write |
| `--flash {filename}` | `-f` | Flash full bin (auto-detects calibration version, asks confirmation) |
| `--flash-calibration {filename}` | | Flash calibration zone only |
| `--flash-program {filename}` | | Flash program zone only |
| `--correct-checksum {filename}` | | Fix EEPROM checksum in file |
| `--clear-adaptive-values` | | Reset learned/adaptive values on ECU |
| `--bin-to-sie {filename}` | | Convert BIN → SIE for chip-off flashing |
| `--sie-to-bin {filename}` | | Convert SIE → BIN after chip-off flashing |
| `--immo` | | Immobilizer programming functions |
| `--verbose` | `-v` | Enable debug logging |
| `--logger` | `-l` | Start KWP2000 datalogger |
| `--read-dtcs` | | Read stored diagnostic trouble codes |
| `--rsw-boot1 / --rsw-boot2 / --rsw-asw / --rsw-cal / --rsw-full` | | Flash via RSW bootstrap |
| `--rsw-virginize` | | Virginize ECU via RSW bootstrap |
| `--mtos` | | Mini Test Operating System |
| `--mtos-payload {filename}` | | Full-dump BIN to use for MTOS |
| `--mtos-key {key}` | | Key for Siemens access level |

### Connect-Time Identification Banner
Before running any operation, GKFlasher reads and prints the ECU's identity:

```
[*] Trying to find calibration..
[*] Found! Description: ca652051, calibration: G3N7TS0H
```

- `calibration` = 8 bytes at the calibration zone start (`0x48000` on 2mbit, `0x88000` on 4mbit V6)
- `description` = 8 bytes at zone start + `0x40`

These are the first two fields of the factory bin filenames at
<https://opengk.org/files/?dir=EEPROMS/Siemens>, so the banner alone tells you which
reference dump to compare against.

### `--correct-checksum` Is Non-Destructive If You Decline
It prints `Current {region} checksum: X, new checksum: Y` for every region, then prompts
`Save to {filename}? [y/n]`. Answering `n` leaves the file byte-for-byte unchanged
(verified), which makes it usable as a read-only checksum audit on a dump.

Note this operates on a **file**, not the ECU, and uses raw file offsets.

### Important Notes on Partial Reads/Writes
- GKFlasher **always pads output to full EEPROM size** with 0xFF. Reading 16KB calibration on an 8Mbit ECU still produces a 1MB file.
- For `--flash` with `--address-start`/`--address-stop`: input file offsets must match intended EEPROM offsets. This is automatic when using files produced by `--read`.
- Version detection: GKFlasher compares current ECU calibration version vs. file version before flashing and asks confirmation.

## Dependencies
```
alive-progress, crcmod, gkbus, grapheme, pyftdi, PyQt5, PyQt5-Qt5, PyQt5-sip, pyserial, pyusb, PyYAML, setuptools
```

## Checking Whether an ECU Is Stock
See **`ecu-factory-verification.md`** for the full procedure (fingerprint → checksum audit →
diff against a factory bin) and `scripts/verify-ecu-stock.py` for tooling.

Short version: a matching calibration string or a clean checksum does **not** prove an ECU is
untuned. Only a byte-diff against a known-good factory dump does.

## Project Status
46 releases, latest v1.0.92 (Jan 2026), GPL-3.0 license. Supported by OpenGK.org.
