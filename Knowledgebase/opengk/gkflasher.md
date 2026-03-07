# GKFlasher — ECU Flashing Tool
**Repository:** https://github.com/Dante383/GKFlasher
**Wiki:** https://opengk.org/index.php?title=GKFlasher_Instructions
**Used on:** Blue Tiburon (stock Siemens ECU)

---

## Overview
GKFlasher is an open-source Python CLI/GUI tool for reading, writing, and tuning Siemens SIMK41/SIMK43 ECUs. Supports calibration data modification, program code updates, checksum correction, immobilizer programming, and BSL (Bootstrap Loader) operations.

## Hardware Required
- **FTDI USB-OBD2 interface cable** — MUST use genuine FTDI chipset (NOT CH340C)
- Recommended: "Galletto 1260 ECU Chip Tuning Tool" (reliable + affordable)

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
| `--address_start {offset}` | `-s` | Start offset for partial read/write |
| `--address_stop {offset}` | `-e` | End offset for partial read/write |
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

### Important Notes on Partial Reads/Writes
- GKFlasher **always pads output to full EEPROM size** with 0xFF. Reading 16KB calibration on an 8Mbit ECU still produces a 1MB file.
- For `--flash` with `--address_start`/`--address_stop`: input file offsets must match intended EEPROM offsets. This is automatic when using files produced by `--read`.
- Version detection: GKFlasher compares current ECU calibration version vs. file version before flashing and asks confirmation.

## Dependencies
```
alive-progress, crcmod, gkbus, grapheme, pyftdi, PyQt5, PyQt5-Qt5, PyQt5-sip, pyserial, pyusb, PyYAML, setuptools
```

## Project Status
46 releases, latest v1.0.92 (Jan 2026), GPL-3.0 license. Supported by OpenGK.org.
