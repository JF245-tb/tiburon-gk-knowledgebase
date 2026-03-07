# W-Line — OpenGK Wiki
**Source:** https://opengk.org/index.php?title=W-Line

---

## Overview

W-Line is the protocol used for immobilizer communication between the **BCM** and the **ECU** in SMARTRA-equipped vehicles.

**Key fact: W-Line = K-Line (physically)**

The physical layer is identical to K-Line. See `k-line.md` for physical layer specs. The data layer is documented in `smartra-protocol.md`.

LIN bus also uses the same physical layer.

---

## Hardware Tip (from OpenGK)

A "UART to LIN module" (e.g., CH341A running in TTL↔USB mode) can be used for W-Line work — same physical layer as LIN. Useful for EEPROM programming / SMARTRA reverse engineering.

---

## Connection (2.7L V6 GK)

From `k-line.md`:
- ECU W-Line: **C133-1 pin 3** → **BCM-IM pin 20** ("Immo W-line")
- OBD2 K-Line: **OBD2 pin 7** → **BCM-IM pin 19** ("Diagnosis")
- On the 2.7L, K and W lines are integrated into one pin on the ECU (C133-1 pin 3)

## Connection (2.0L with Immobilizer)

- ECU 2.0 pin 77 = NOT connected (K-line is NOT at pin 77 on immo-equipped 2.0L)
- All K-line routed through BCM; ECU uses **W-Line** (2.0L pin 47) for ECU↔BCM comms
