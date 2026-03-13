---
source: SD.pdf
chapter: SD
section: SD-44 to SD-47
pages: 44-47
title: Data Link Details
---

# Data Link Details

**SD-44 -- Data Link Details (1) -- OBD2 DLC, BCM, ECM, ABS, SRS connections**
**SD-45 -- Data Link Details (2) -- Multipurpose Check Connector, TCM, Fuel Pump**
**SD-46 -- Component Location Index**
**SD-47 -- MEMO (blank page)**

---

## Data Link Connector (DLC) -- M07

### OBD2 DLC Pin Assignment (SD-44)

The 16-pin OBD2 DLC (M07) is located in the driver-side instrument panel area.

| DLC Pin | Function | Wire Color | Wire Size | Destination |
|---------|----------|------------|-----------|-------------|
| 1 | -- | -- | -- | -- |
| 2 | -- | -- | -- | -- |
| 3 | -- | -- | -- | -- |
| 4 | Chassis ground | B | 0.85S | G11 |
| 5 | Signal ground | B | 0.85S | G11 |
| 6 | -- | -- | -- | -- |
| 7 | K-Line | V | 0.5S | BCM-IM (pin 19) → ECM |
| 8 | -- | -- | -- | -- |
| 9 | -- | -- | -- | -- |
| 10 | -- | -- | -- | -- |
| 11 | -- | -- | -- | -- |
| 12 | -- | -- | -- | -- |
| 13 | -- | -- | -- | -- |
| 14 | -- | -- | -- | -- |
| 15 | -- | -- | -- | -- |
| 16 | Battery (+) | R | 0.85S | Fuse 18 (10A) |

---

## Circuit Paths (SD-44)

### K-Line (OBD2 Pin 7)

```
DLC M07 pin 7 → [V, 0.5S] → BCM-IM (pin 19)
  → [V, 0.5S] → BCM-NM (pin 8, IMMOB K-LINE)
  → [V, 0.5S] → ECM C133-1 pin 3 (2.7L)
                  ECM C33 pin x (2.0L)
```

### Battery Feed (OBD2 Pin 16)

```
BCM Fuse 18 (10A) → [R, 0.85S] → M07 pin 16
  Also feeds: Room lamp, Clock, Audio, Data link connector, Multi gauge unit
```

### BCM to ECM Connections (SD-44)

| Source | Connector | Pin | Wire | Size | Destination | Connector | Pin |
|--------|-----------|-----|------|------|-------------|-----------|-----|
| BCM | BCM-AI | -- | L | 0.5S | ECM (2.7L) | MC101 (L) | -- |
| BCM | BCM-JM | -- | L | 0.5S | ECM (2.7L) | MC101 (L) | -- |
| BCM | BCM-NM | 8 | V | 0.5S | ECM (K-Line) | C133-1 | 3 |
| BCM | BCM-NM | 10 | -- | 0.5S | Vehicle speed | -- | -- |

### ECM Diagnostic Connections

```
ECM (2.7L, C133-1) →
  → MC101 (L) → BCM-AI → DLC M07

ECM (2.0L, C33) →
  → MC01 (L) → BCM → DLC M07
```

### ABS Module Connection

```
ABS control module (E37) →
  → [L, 0.5S] → BCM-JM → M07
```

### SRS Module Connection

```
SRS control module (I14) →
  → BCM-AI → M07
```

---

## Data Link Details (2) -- SD-45

### Multipurpose Check Connector (M06)

| Pin | Function | Wire Color | Wire Size | Destination |
|-----|----------|------------|-----------|-------------|
| 1 | TCM | -- | 0.85S | TCM (C136-3) |
| 2 | Diagnostic | -- | 0.85S | -- |
| 3 | K-Line | V | 0.5S | ECM |
| 4 | Data error | -- | 0.85S | -- |
| 5 | -- | -- | -- | -- |
| 6 | -- | -- | -- | -- |
| 7 | -- | -- | -- | -- |
| 8 | Fuel pump | -- | 0.85S | Fuel pump relay (E49) |
| 9 | -- | -- | -- | -- |
| 10 | -- | -- | -- | -- |

### Multipurpose Check Connector Bus

```
BCM-GR → [B, 0.85S] → BCM-HR (bus connector)
  → [B, 0.85S] → Joint connector → M06

From Multipurpose Check Connector (M06):
  → [V, 0.5S] → To ECM (K-Line feed)
  → [--] → To TCM diagnostic
  → [--] → To fuel pump relay (E49)
```

### Lower Bus Connections (SD-45)

| Source | Connector | Wire | Size | Destination |
|--------|-----------|------|------|-------------|
| Joint connector | -- | -- | 0.85S | TCM (C136-3 / 2.7L) |
| Joint connector | -- | -- | 0.85S | TCM (C36-3 / 2.0L) |
| Fuel pump relay | E49 | -- | 1.25B | Fuel pump (M55) |
| ECM | C133-1 | -- | 0.85S | Multipurpose connector |
| ECM | CM01 | -- | 2.0B | -- |

### Circuit Path: TCM Diagnostic

```
M06 pin 1 → [0.85S] → Joint connector
  → TCM C136-3 (2.7L) or C36-3 (2.0L)
  → Tr.Diag(SE11)
```

### Circuit Path: Fuel Pump Check

```
M06 pin 8 → [0.85S] → Joint connector
  → Fuel pump relay (E49)
  → Fuel sender & fuel pump motor (M55)
```

---

## Component Location Index (SD-46)

### Components

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C33 | ECM (2.0L) | CL-20 |
| C36-3 | TCM (2.0L) | CL-20 |
| C133-1 | ECM (2.7L) | CL-25 |
| C136-3 | TCM (2.7L) | CL-25 |
| C233 | ECM (1.6L) | CL-28 |
| E37 | ABS control module | CL-12 |
| E49 | Fuel pump relay | CL-12 |
| I14 | SRS control module | CL-16 |
| M06 | Multipurpose check connector | CL-2 |
| M07 | Data link connector | CL-2 |
| M34 | Joint connector | CL-4 |
| M36 | Joint connector | CL-4 |
| M55 | Fuel sender & Fuel pump motor | CL-5 |

### Connectors

| Connector | Location Page |
|-----------|---------------|
| BCM-AI | CL-17 |
| BCM-IM | CL-8 |
| BCM-JM | CL-8 |
| EC02 | CL-14 |
| EC102 | CL-14 |
| EC202 | CL-14 |
| MC01 | CL-8 |
| MC101 | CL-8 |
| MC201 | CL-8 |

### Grounds

| Ground ID | Location Page |
|-----------|---------------|
| G11 | CL-33 |

---

## Notes

- The K-Line (OBD2 pin 7, violet wire) routes: DLC M07 → BCM-IM pin 19 → ECM C133-1 pin 3 (2.7L). This is the primary diagnostic communication line for OBD-II scan tools.
- The DLC receives constant battery power from BCM Fuse 18 (10A) on pin 16.
- DLC pins 4 and 5 provide chassis ground and signal ground respectively, both via G11.
- The Multipurpose Check Connector (M06) provides additional diagnostic access to the TCM, fuel pump relay, and ECM for factory/dealer diagnostic tools.
- SD-47 is a blank MEMO page with no content.
