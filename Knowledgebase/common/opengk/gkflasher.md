# GKFlasher — ECU Flashing Tool
**Repository:** https://github.com/Dante383/GKFlasher
**Wiki:** https://opengk.org/index.php?title=GKFlasher_Instructions
**Used on:** Blue Tiburon (stock Siemens ECU)

---

## Overview
GKFlasher is an open-source Python CLI/GUI tool for reading, writing, and tuning Siemens **SIMK41 / SIMK43 / SIM2K** ECUs. The project is the result of black-box reverse engineering. Supports calibration data modification, program code updates, checksum correction, immobilizer programming, and BSL (Bootstrap Loader) operations.

## Hardware Required
- **USB-OBD2 interface cable.** FTDI chipset strongly preferred.
- **CH340 is supported as of GKFlasher v1.0.5** — the wiki's blanket "FTDI only" warning
  predates that. CH340 adapters are still *not* supported for BSL operations.
- Recommended: "Galletto 1260 ECU Chip Tuning Tool" (reliable + affordable, genuine FTDI)

## Installation — Precompiled MSI (easiest)
Prebuilt MSI installers are published on the GitHub releases page:
<https://github.com/Dante383/GKFlasher/releases>

Older MSIs (v1.0.0–v1.0.4) are also mirrored at
`opengk.org/files/Users/chase206/` — those are long superseded; take the current one from
GitHub releases. See `file-repository.md`.

The manual install below is for participating in development or running from source.

## Installation (Windows, from source)
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

## Config File (`gkflasher.yml`)
Loaded by default; override with `-c/--config {filename}`. Keep one config per vehicle.

```yaml
protocol: 'canbus'
canbus:
  interface: 'can0'
  tx_id: 0x7e0
  rx_id: 0x7e8
kline:
  interface: '/dev/ttyUSB0'
  baudrate: 10400
  tx_id: 0x11
  rx_id: 0xF1
```

K-Line IDs match `k-line.md`: ECU `0x11`, diagnostic device `0xF1`, 10400 baud.

## GUI
`python3 gui.py` launches the PyQt5 interface, which covers the common read/flash/checksum
operations. The CLI exposes everything, including the BSL/RSW and MTOS functions.

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
Current `requirements.txt` (pins moved a long way from the versions in the wiki guide —
`gkbus` in particular went 0.1.8 → 0.4.88):

```
alive_progress==3.1.5   crcmod==1.7        gkbus==0.4.88
pyqt5==5.15.10          PyYAML==6.0.2      sip==6.10.0
typing_extensions==4.12.2                  plyer==2.1.0
```

`pyftdi`, `pyserial`, `pyusb` and `scapy` are pulled in transitively by `gkbus` rather than
listed directly. Install with `python -m pip install -r requirements.txt` (add
`--break-system-packages` on recent Debian/Ubuntu).

## Supported ECUs & Memory Layout
From `ecu_definitions.py`. GKFlasher identifies an ECU by reading the **identification
offset** and matching the leading bytes against `expected`. That string is the
`description` field in the OpenGK bin filenames (`file-repository.md`), which is why a dump
can name its own reference file.

| ECU | Ident offset | Matches | Size | Calibration zone | Program zone |
|-----|--------------|---------|------|------------------|--------------|
| SIMK43 8mbit | `0x82014` | `6621` | 1024 KiB | `0x90000` +`0x10000` | `0xA0000` +`0x60000` |
| SIMK43 2.0 4mbit | `0x90040` | `ca66` | 512 KiB | `0x90000` +`0x10000` | `0xA0000` +`0x60000` |
| **SIMK43 V6 4mbit (5WY17)** | `0x88040` | `ca65401` | 512 KiB | `0x88000` +`0x5F40` | `0x90000` +`0x70000` |
| **SIMK43 V6 4mbit (5WY18+)** | `0x88040` | `ca654`, `ca655` | 512 KiB | `0x88000` +`0x6EFF` | `0x90000` +`0x70000` |
| **SIMK41 / V6 2mbit** | `0x48040` | `ca660`, `ca652`, `ca650` | 256 KiB | `0x48000` +`0x8000` | `0x50000` +`0x30000` |
| SIMK43 2.0 4mbit (Sonata) | `0x88040` | `ca661` | 512 KiB | `0x88000` +`0x5FF8` | `0x90000` +`0x70000` |
| SIMK2K (Elantra 2.0 Beta) | `0x92040` | *(binary)* | 512 KiB | `0x90000` +`0xEF00` | `0xA0000` +`0x60000` |

Bold rows are the 2.7L V6 families relevant to our cars.

**Match order matters:** `ca65401` (5WY17) is tested before `ca654` (5WY18+), so `ca654012`
resolves to the 5WY17 entry with its smaller `0x5F40` calibration zone.

**Addresses are EEPROM addresses, not file offsets.** Convert with `bin_offset`: `-0x40000`
for the 2mbit, `-0x80000` for the 4mbit V6. So calibration `0x48000` sits at file offset
`0x8000` in a 2mbit dump. The 5WY18+ calibration zone is noted in the source as having "some
readable but non-writable section after this."

If identification fails, GKFlasher offers a manual pick from this list — intended for
reviving a soft-bricked ECU, not for routine use.

## Immobiliser Functions (`--immo`)
`--immo` opens an interactive menu. Menu entries, in order:

| # | Entry | Notes |
|---|-------|-------|
| 0 | Information | Keys learnt, ECU/key status, SMARTRA status |
| 1 | Limp home mode | Asks for the **4-digit** password (default `2345`) |
| 2 | Immo reset | Asks for the **6-digit** immo PIN |
| 3 | Smartra neutralize | Asks for the 6-digit PIN |
| 4 | Teach keys | Teaches up to 4 keys |
| 5 | Limp home password teaching/changing | |
| 6 | Read VIN | OBD2 service `0x09` |
| 7 | Write VIN | **No validation on input** |
| 8 | Smartra VIN to PIN Calculator | Derives the PIN from the VIN |

**Two different secrets — do not confuse them:** limp-home uses a *4-digit* password
(default `2345`); immo reset / SMARTRA neutralize use the *6-digit* DPN.

### KWP2000 Routine IDs (`ecu_definitions.py`)

| Routine | ID | Purpose |
|---------|----|---------|
| `ERASE_PROGRAM` / `ERASE_CALIBRATION` | `0x00` / `0x01` | Flash erase |
| `VERIFY_BLOCKS` | `0x02` | |
| `CHECK_REPROGRAMMING_STATUS` | `0x03` | |
| `QUERY_IMMO_INFO` | `0x12` | |
| `BEFORE_LIMP_HOME_TEACHING` | `0x13` | |
| `BEFORE_IMMO_KEY_TEACHING` | `0x14` | |
| `BEFORE_IMMO_RESET` | `0x15` | |
| `BEFORE_LIMP_HOME` | `0x16` | |
| `LIMP_HOME_INPUT_NEW_PASSWORD` | `0x17` | |
| `ACTIVATE_LIMP_HOME` | `0x18` | 4-digit password as parameter |
| `LIMP_HOME_CONFIRM_NEW_PASSWORD` | `0x19` | |
| `IMMO_INPUT_PASSWORD` | `0x1A` | 6-digit PIN as parameter |
| `IMMO_TEACH_KEY_1`–`4` | `0x1B`–`0x1E` | |
| `IMMO_RESET_CONFIRM` | `0x20` | |
| `BEFORE_SMARTRA_NEUTRALIZE` | `0x25` | Prerequisite for `0x26` |
| `SMARTRA_NEUTRALIZE` | `0x26` | Parameter `0x01` |
| `EXECUTE_MTOS` | `0xFA` | |

I/O identifiers: `ADAPTIVE_VALUES` `0x50`, automatic-transaxle config `0x40`,
traction-control config `0x41`.

**On the 2.7L V6 these are mostly not what you need** — V6 immobiliser data lives in the BCM,
not the ECU (`immobiliser.md`). The SMARTRA routines apply to the 2.0L, where pairing is
stored in the ECU. GKFlasher warns that a failed limp-home attempt is common on Tiburon FL2
where the limp-home pin was never set, and that wrong data locks the system for about an hour.

## Advanced / Recovery Operations
- **BSL (Bootstrap Loader)** and **RSW** (`--rsw-boot1`, `--rsw-boot2`, `--rsw-asw`,
  `--rsw-cal`, `--rsw-full`, `--rsw-virginize`) — for reviving an ECU that will not respond
  normally. CH340 adapters are *not* supported for BSL.
- **MTOS** (Mini Test Operating System) — `--mtos` with `--mtos-payload` (a full dump) and
  `--mtos-key`.
- **Chip-off** — `--bin-to-sie` / `--sie-to-bin` convert for an external programmer such as
  the Willem GQ-4x4 (`file-repository.md`).
- Bundled assets: `simk4x_bootstrap.bin`, `simk4x_kernel.bin`, `simk43_rsw_fl2.bin`, and
  A29Fx00Bx drivers for I4 and V6.

## Checking Whether an ECU Is Stock
See **`ecu-factory-verification.md`** for the full procedure (fingerprint → checksum audit →
diff against a factory bin) and `scripts/verify-ecu-stock.py` for tooling.

Short version: a matching calibration string or a clean checksum does **not** prove an ECU is
untuned. Only a byte-diff against a known-good factory dump does.

## Project Status
78 release tags, latest **v1.0.99**; most recent commit June 2026 (MTOS). GPL-3.0 license.
Written by dante383 and dmg210, supported by OpenGK.org.

## Upstream Documentation Discrepancies
Checked against the source; the upstream docs are wrong in these places, so do not "correct"
this file back to match them:

| Upstream says | Actually |
|---------------|----------|
| README: `--address_start` / `--address_stop` | argparse defines `--address-start` / `--address-stop`. The underscore spellings fail. |
| README: `--mtos {input filename}` | `--mtos` is a flag; the file goes to `--mtos-payload`. |
| README install: Python 3.10 | Wiki install guide specifies 3.11.9; requirements pin PyQt5 5.15.9. |
| Wiki: genuine FTDI required, never CH340 | CH340 supported since v1.0.5 (still excluded for BSL). |

The wiki's GKFlasher Instructions page is **install-only** — it documents Git/Python setup,
the MSI packages and a desktop shortcut, but contains no read/flash usage. Operational
detail comes from the repository README and source.
