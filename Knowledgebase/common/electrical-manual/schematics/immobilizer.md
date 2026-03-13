---
source: SD.pdf
chapter: SD
section: SD-100 to SD-101
pages: 100-101
title: Immobilizer Control System
---

# Immobilizer Control System

**SD-100 -- Immobilizer Control System (1) Schematic**
**SD-101 -- Component Location Index and Circuit Description**

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Transponder (in ignition key) | -- | -- | -- | -- |
| SMARTRA antenna (key cylinder) | -- | -- | -- | 0.3B |
| BCM (Body Control Module) | BCM-HM | -- | -- | 0.85S |
| BCM | BCM-NM | 8 | V | 0.5S |
| BCM | BCM-IM | 19 | V | 0.5S |
| BCM | BCM-LM | -- | -- | 0.5B |
| ECM (2.0L) | C33 | -- | V | 0.5S |
| ECM (2.7L) | C133-1 | 3 | V | 0.5S |
| ECM (1.6L) | C233 | -- | V | 0.5S |
| Data link connector | M07 | 7 | V | 0.5S |
| Multifunction check connector | M06 | -- | V | 0.5S |
| Ignition switch | M04 | -- | -- | -- |
| See Courtesy, Luggage Room Lamp and Key Remind Switch | M65 | -- | -- | -- |

---

## Circuit Paths

### SMARTRA Transponder to BCM

```
Transponder (ignition key)
  → SMARTRA antenna (key cylinder ring)
  → [0.3B] → BCM-HM
  → BCM (internal processing)
```

### K-Line: BCM to ECM (Immobilizer Authorization)

```
BCM-NM (pin 8, IMMOB K-LINE) → [V, 0.5S]
  → BCM-IM (pin 19)
  → [V, 0.5S] → MC01/MC101/MC201
  → [V, 0.5S] → ECM:
      C33 (2.0L)
      C133-1 pin 3 (2.7L)
      C233 (1.6L)
```

### K-Line: BCM to OBD2 DLC

```
BCM-NM (pin 8) → [V, 0.5S]
  → BCM-IM (pin 19)
  → [V, 0.5S] → M07 pin 7 (OBD2 DLC)
  → [V, 0.5S] → M06 (Multifunction check connector)
```

### BCM Power and Ground

```
BCM power: See Courtesy, Luggage Room Lamp and Key Remind Switch → BCM-HM
BCM ground: BCM-LM → [B, 0.5B] → G11 (Main.1)
```

### Ignition Switch Feed to BCM

```
Ignition switch (M04) → [Y/R] → BCM-LM → BCM internal
  → Immobilizer enable/disable logic
  → K-Line output (BCM-NM pin 8) → ECM
```

---

## Signal Flow

```
1. Key inserted → Transponder sends RF code → SMARTRA antenna
2. SMARTRA antenna → BCM-HM → BCM decodes transponder signal
3. BCM compares code with stored key codes
4. If match: BCM sends authorization via K-Line (V, 0.5S)
   → BCM-NM pin 8 → BCM-IM pin 19 → ECM C133-1 pin 3 (2.7L)
5. ECM enables fuel injection → Engine starts
6. If no match: ECM blocks fuel injection → Engine cranks but does not start
```

---

## Ground Points

| Ground ID | Location | Components |
|-----------|----------|------------|
| G11 | Main.1 (instrument panel area) | BCM ground (BCM-LM) |

---

## Component Location Index (SD-101)

### Components

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C33 | ECM (2.0L) | CL-20 |
| C133-1 | ECM (2.7L) | CL-25 |
| C136-3 | TCM (2.7L) | CL-25 |
| C233 | ECM (1.6L) | CL-28 |
| M04 | Ignition switch | CL-2 |
| M06 | Multifunction check connector | CL-2 |
| M07 | Data link connector | CL-2 |

### Connectors

| Connector | Location Page |
|-----------|---------------|
| BCM-HM | CL-8 |
| BCM-IM | CL-8 |
| BCM-LM | CL-8 |
| MC01 | CL-8 |
| MC101 | CL-8 |
| MC201 | CL-8 |

### Grounds

| Ground ID | Location Page |
|-----------|---------------|
| G11 | CL-33 |

---

## Circuit Description (from SD-101)

The immobilizer control system is an anti-theft device which enables the starting to be possible only when the secret codes, stored in the Engine Control Module and the Body Control Module (BCM), are aligned simultaneously.

The transponder (built-in the ignition key) sends unique frequency secret code signals to the BCM through the SMARTRA antenna coil. The BCM compares the received signals with memorized code. When the codes are aligned, the BCM sends signals to the ECM so that the starting is possible through fuel injection control.

---

## Notes

- The K-Line wire is **violet (V), 0.5S** throughout the immobilizer circuit.
- The K-Line routing is: OBD2 DLC M07 pin 7 → BCM-IM pin 19 → BCM-NM pin 8 → ECM C133-1 pin 3 (2.7L).
- This is the same K-Line used for OBD-II diagnostics (ISO 14230 / KWP2000).
- ECM address on K-Line: 0x11, 10400 baud, Fast Init.
- The SMARTRA antenna is the ring around the ignition key cylinder.
- The BCM stores up to 3 transponder key codes.
- Default limp home PIN: 2345; SMARTRA neutralize commands: 0x25 then 0x26 (parameter 0x01).
