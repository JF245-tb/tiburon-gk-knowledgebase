# K-Line Protocol — OpenGK Wiki
**Source:** https://opengk.org/index.php?title=K-Line
**Applies to:** SIMK43/SIMK41 ECUs (Hyundai/Kia Siemens)

---

## Overview

K-Line on SIMK43 runs at **10400 baud** and uses the **KWP2000 protocol** for diagnostic communication.

---

## Connection Points

### OBD2
K-line uses the standard **pin 7** on the OBD2 connector.

### ECU Connection (Varies by Engine/Immobilizer Config)

**2.7L V6 (G6BA) — both with and without immobilizer:**
- K-Line pins (OBD2/MCC) → connected to **BCM-IM pin 19** ("Diagnosis")
- ECU K/Immo-Line pin (**C133-1, pin 3**) → connected to **BCM-IM pin 20** ("Immo W-line")
- **2.7 ECUs don't have a separate K and W line** — it's all integrated in one pin
- No special handling needed for 2.7L compared to 2.0L

**2.0L without immobilizer:**
- K-Line (OBD2/MCC) connected directly to K-line pin on ECU (2.0 - pin 77)

**2.0L with immobilizer:**
- K-Line (OBD2/MCC) → BCM-IM pin 19 ("Diagnosis")
- ECU 2.0 pin 77 = NOTHING CONNECTED
- All K-line routed through BCM; ECU uses W-Line (2.0 - pin 47)

---

## KWP2000 Protocol

**Recommended reference:** OBDII Specifications - KWP2000 DaimlerChrysler 2002.pdf

### Initialization
Use **Fast Init**:
1. Bring K-line LOW for exactly 25ms
2. Bring K-line HIGH for 25ms
3. Send `StartCommunication` request

Python example: see GKBus code (part of GKFlasher project).

**Device IDs:**
- ECU address: `0x11`
- Diagnostic device address: `0xF1`

**Example exchange (security access):**
```
Diagnostic → ECU:  82 11 F1 27 01 AC
ECU → Diagnostic:  83 F1 11 67 02 34 22
```

### Baudrate

Default: **10400 baud**

Optional `StartDiagnosticSession` baudrate parameter (not supported on all ECUs; pre-2005 may not support):

| Identifier | Baudrate (bps) |
|-----------|---------------|
| 0x01 | 10400 (default) |
| 0x02 | 20000 |
| 0x03 | 40000 |
| 0x04 | 60000 |
| 0x05 | 120000 |

### Security Access (Challenge-Response)

SIMK43/41 uses 2-byte seed + 2-byte key.

Python implementation (from GKFlasher `ecu.py` line 42):
```python
def calculate_key(seed):
    key = 0x9360
    for index in range(0x24):
        key = key * 2 ^ seed
    return key & 0xFFFF
```

---

## Input/Output Local Identifiers (Actuator Tests)

These can be activated via KWP2000 for diagnostic/test purposes:

| Identifier (hex) | Description | Notes |
|-----------------|-------------|-------|
| 0x10 | Check engine light | |
| 0x11 | EVAP canister close valve (on) | |
| 0x12 | Fuel pump relay | |
| 0x13 | A/C compressor relay | |
| 0x14 | Fuel pump control | |
| 0x1A | Cooling fan relay high | |
| 0x1B | Cooling fan relay low | |
| 0x1C | Main relay | |
| 0x20 | Canister purge valve | |
| 0x23 | Idle speed actuator | |
| 0x24 | CVVT valve | |
| **0x31** | **Ignition coil #1, 4** | |
| **0x32** | **Ignition coil #2, 3** | Coil #5 V6 only |
| **0x33** | **Ignition coil #3, 6** | Coil #6 V6 only |
| 0x300701 | Injector cylinder 1 | V6 only |
| 0x300702 | Injector cylinder 2 | V6 only |
| 0x300704 | Injector cylinder 3 | V6 only |
| 0x300708 | Injector cylinder 4 | V6 only |
| 0x300710 | Injector cylinder 5 | V6 only |
| 0x300720 | Injector cylinder 6 | V6 only |
| 0x39 | Injector cylinder 1 | I4 only |
| 0x3A | Injector cylinder 2 | I4 only |
| 0x3B | Injector cylinder 3 | I4 only |
| 0x3C | Injector cylinder 4 | I4 only |
| 0x40 | Version Config — Automatic Transaxle (0x08) | ECU reset for M/T or Non-TCS |
| 0x41 | Version Config — Traction Control System (0x08) | ECU reset for M/T or Non-TCS |
| 0x50 | Adaptive values (0x04 = clear) | |
| 0x95 | EVAP leakage test (0x06 = start) | |

---

## Routines by Local Identifier (Reprogramming/Immobilizer)

| Identifier (hex) | Description | Notes |
|-----------------|-------------|-------|
| 0x00 | Erase program section | |
| 0x01 | Erase calibration section | |
| 0x02 | Verify and mark blocks as ready to execute | **Must call after flashing** |
| 0x03 | Check reprogramming status | Available after complete flash until ECU reset. 0xBBA0 = success |
| 0x12 | Query immobilizer info | Returns: # keys learned, immo status, key status, SMARTRA status |
| 0x13 | Pre-requisite before immo password teach/change | |
| 0x14 | Pre-requisite before immo teaching | |
| 0x15 | Pre-requisite before ECU immo reset | |
| 0x16 | Pre-requisite before limp home mode | |
| 0x17 | Input new limp home password | |
| 0x18 | Activate limp home mode | Takes user-provided password (default: 2345) |
| 0x19 | Confirm limp home password change | Takes 0x01 as parameter |
| 0x1A | Input 6-digit immobilizer password | Required before teach/reset/modify. Takes password + 6× 0xFF |
| 0x1B–0x1E | Teach keys 1–4 | Takes 0x01 as parameter |
| 0x20 | Reset ECU immo | Takes 0x01 as parameter |
| 0x25 | Pre-requisite before neutralizing SMARTRA | |
| 0x26 | Confirm neutralizing SMARTRA | Takes 0x01 as parameter |
| 0xFA | Launch MTOS | Requires Siemens level access (0xFD) |

---

## Race Car Notes

**Blue Tiburon (GKFlasher tuning):**
- K-Line connection: OBD2 pin 7 → BCM-IM pin 19 → ECU C133-1 pin 3 (all V6)
- Use FTDI-based adapter (NOT CH340 — use genuine FTDI chipset)
- GKFlasher handles all KWP2000 initialization/security automatically

**White Tiburon (Haltech):**
- K-Line is irrelevant for Haltech ECU (standalone, not OEM protocol)
- K-Line wiring can be removed from harness during white car build
