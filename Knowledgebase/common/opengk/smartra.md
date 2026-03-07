# SMARTRA — OpenGK Wiki
**Source:** https://opengk.org/index.php?title=SMARTRA
**Vehicle:** 2003 Hyundai Tiburon GK (uses SMARTRA2)

---

## Overview

**SMARTRA** (SMARt TRansponder Antenna) is a passive challenge-response immobilizer system developed for HMC (Hyundai Motor Company) by Bosch. The GK platform uses **SMARTRA2**. SMARTRA3 is backwards compatible and its protocol spec is available via FCC (ID: LXP-VIMA01).

---

## System Architecture

Three components, all required:

| Component | Role |
|-----------|------|
| **Keyfob transponder** | Stores 32-bit unique ID + 3-byte encryption key |
| **BCM (SMARTRA CU)** | RF interface only — does NOT store transponder data or validate data |
| **ECU** | Stores registered key IDs (up to 4) and 6-digit DPN; performs all validation |

**Key insight: BCMs are NOT paired. Keyfob transponders are paired to ECUs.**
- Replacing/swapping a BCM does NOT affect immobilizer pairing
- ECU stores all transponder IDs and the DPN (Diagnostic PIN Number)

---

## How It Works (Ignition Cycle)

1. ECU requests transponder identification number
2. If key is registered, ECU generates 4 random bytes (challenge)
3. ECU sends challenge to transponder (via BCM/W-Line) along with inverted first 4 bytes of keystream
4. Transponder responds with encrypted challenge (Hitag2 algorithm)
5. ECU performs same encryption and compares results
6. Match → engine allowed to start

---

## Hardware

### Keyfob Transponder
- Based on **Hitag2** protocol (NXP)
- Chip: **PCF7936** (NXP, 32-bit unique identifier)
- 32-bit ID = "Pre Secret Encryption Key" (stored in ECU EEPROM)
- 3-byte encryption key stored in transponder memory
- **No timeout mechanism** → brute-force possible
  - Using Proxmark 3 + pre-generated list (0–999999, increments of 16): **under 4 hours**

### BCM RF Hardware
- Antenna: Around ignition switch (125 kHz, ASK modulation)
- IC: **PCF7991AT** (NXP immobilizer base station)
- BCM transmits RF data in/out via **SMARTRA Protocol over W-Line**
- BCM is semi-transparent — does not verify data

---

## Encryption Key (DPN / Immo Pin)

- **6-digit number** used to program new keys or neutralize immobilizer
- Also called "immo pin" or "DPN (Diagnostic PIN Number)"
- **Can be derived from last 6 characters of VIN**
  - Algorithm reverse-engineered: Python implementation at https://github.com/Dante383/smartra-vin-to-pin
- Full Hitag2 key structure: `0xFFFFxxxxxxFF` (xxx = DPN digits)
- Every PIN computed from VIN is divisible by 16 → only **65,535 available combinations**
  - Exception: Russian market vehicles may differ
  - FL2 ECU memory position may also differ (needs verification)

---

## Limp Home Pin

- **4-digit user-customizable password** (NOT the same as the 6-digit DPN)
- Default: **2345** (set at dealership, rarely changed)
- Allows one engine start if immobilizer system fails
- Changeable over K-Line (GKFlasher or Cascade) if previous PIN is known
- **⚠️ Removed in FL2 ECUs (2007+)** — limited testing suggests this feature may be gone

### Entering Limp Home Mode
Option 1: Via GKFlasher/Cascade (diagnostics session must stay active until start)
Option 2: **Ignition switch method:**
- 1 rapid switch ACC→IGN = digit "1"
- 4 rapid switches = digit "4"
- Continue for each digit of the 4-digit PIN

---

## Standalone SMARTRA2 Unit

A standalone (external) SMARTRA2 box exists — seen around steering columns in Elantra/Accent. NOT installed in Tiburons, but the hardware/firmware inside BCM is virtually identical.

**Workaround:** Snap the W-line on your BCM and connect to the standalone box to externalize the SMARTRA function.

- FCC ID for standalone unit: **LXP-SMARTRA32** — https://fcc.report/FCC-ID/LXP-SMARTRA32

---

## Race Car Notes

**Blue Tiburon:**
- Has BCM-based immobilizer (V6 uses BCM, not standalone SMARTRA)
- BCM-HM pins 1 and 11 = immobilizer antenna connections
- To bypass: neutralize SMARTRA via K-Line (GKFlasher routine 0x26 — see k-line.md)
- Default limp home PIN: 2345 (unless dealership changed it)
- DPN derivable from VIN using smartra-vin-to-pin tool

**Key GKFlasher immobilizer routines (from k-line.md):**
| Routine | Description |
|---------|-------------|
| 0x12 | Query immobilizer info (keys learned, status) |
| 0x1A | Input 6-digit immo password (DPN) |
| 0x1B–0x1E | Teach keys 1–4 |
| 0x20 | Reset ECU immo |
| 0x25 | Pre-requisite before neutralizing SMARTRA |
| 0x26 | Confirm neutralizing SMARTRA (parameter: 0x01) |
