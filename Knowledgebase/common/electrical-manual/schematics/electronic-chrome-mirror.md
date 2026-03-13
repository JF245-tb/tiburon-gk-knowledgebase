---
source: SD.pdf
chapter: SD
section: SD-132 to SD-135
pages: 132-135
title: Electronic Chrome Mirror
---

# Electronic Chrome Mirror

**SD-132 -- Electronic Chrome Mirror (1) Schematic (LHD)**
**SD-133 -- Electronic Chrome Mirror (2) Schematic (RHD)**
**SD-134 -- Component Location Index**
**SD-135 -- Memo (blank)**

<!-- Figure: Electronic chrome mirror with back-up lamp switch input and BCM reverse signal, LHD variant, source: SD.pdf page 132 -->
<!-- Figure: Electronic chrome mirror with back-up lamp switch input and BCM reverse signal, RHD variant, source: SD.pdf page 133 -->

---

## Component Table (LHD -- SD-132)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 7 (HOT AT ALL TIMES) | -- | -- | R | 0.5S |
| Fuse 8 (HOT in ON or START) | -- | -- | -- | -- |
| Fuse illumination | -- | -- | -- | -- |
| BCM-KM | -- | -- | -- | -- |
| Electronic chrome mirror (M60) | B+ (constant) | -- | R | 0.5S |
| Electronic chrome mirror (M60) | reverse signal | -- | V/Y | 0.5S |
| Electronic chrome mirror (M60) | ground | -- | B | 0.5S |
| Back-up lamp switch (2.0L) (C01) | -- | -- | V/Y | 0.85S |
| Back-up lamp switch (2.0L) (C04) | -- | -- | V/Y | 0.85S |
| Back-up lamp switch (2.0L, 6MT) (C06) | -- | -- | V/Y | 0.85S |
| Transaxle range switch (2.7L) (C101) | reverse position | -- | V/Y | 0.85S |
| Back-up lamp switch (1.6L) (C205) | -- | -- | V/Y | 0.85S |
| Joint connector (M20/1, M20/2) | -- | -- | V/Y | 0.5S |

---

## Circuit Paths (LHD)

### Constant Battery Power
```
Battery (+) -> Fuse 7 (HOT AT ALL TIMES)
  -> [R, 0.5S] -> BCM-KM
  -> [R, 0.5S] -> BCM-KM connector
  -> [R, 0.5S] -> BCM-MR connector
  -> [R, 0.5S] -> Electronic chrome mirror M60 (B+ input)
```

### Reverse Signal Path -- Back-Up Lamp Switch to Mirror
```
Back-up lamp switch C01/C04/C06 (2.0L) or Transaxle range switch C101 (2.7L)
  -> [V/Y, 0.85S] -> Joint connector (engine side)
  -> [V/Y, 0.85S] -> BCM-KM
  -> [V/Y, 0.5S] -> Joint connector M20/1
  -> [V/Y, 0.5S] -> Joint connector M20/2
  -> [V/Y, 0.5S] -> Electronic chrome mirror M60 (reverse signal input)
```

### Ground
```
Electronic chrome mirror M60 (ground)
  -> [B, 0.5S] -> GND (G11)
  -> [B, 0.5S] -> GND (G12)
```

### Mirror Operation Logic
```
Ignition ON or START + vehicle NOT in reverse:
  -> Mirror auto-dims based on ambient light sensor (glare reduction)
  -> Automatically controls the glare of headlights from vehicles behind

When reverse is selected (back-up lamp switch closes):
  -> [V/Y] signal goes high
  -> Mirror reverts to normal (non-dimmed) state
  -> Improves visibility while backing up
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G11 | Rear body / interior | Electronic chrome mirror ground | CL-33 |
| G12 | Rear body / interior | Electronic chrome mirror ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-KM | BCM passenger compartment connector | CL-8 |
| BCM-MR | BCM mirror connector | CL-8 |
| MC01 | Connector | CL-8 |
| MC101 | Connector | CL-8 |
| MC201 | Connector | CL-8 |

---

## Component Location Index (SD-134)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C01 | Transaxle range switch (2.0L) | CL-18 |
| C04 | Back-up lamp switch (2.0L) | CL-18 |
| C06 | Back-up lamp switch (2.0L, 6MT) | CL-18 |
| C101 | Transaxle range switch (2.7L) | CL-21 |
| C106 | Back-up lamp switch (2.7L, 6MT) | CL-25 |
| C205 | Back-up lamp switch (1.6L) | CL-26 |
| M60 | Electronic chrome mirror | CL-4 |

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-KM | BCM connector | CL-8 |
| BCM-MR | BCM connector | CL-8 |
| MC01 | Connector | CL-8 |
| MC101 | Connector | CL-8 |
| MC201 | Connector | CL-8 |

| Ground ID | Location Page |
|-----------|---------------|
| G11 | CL-33 |
| G12 | CL-33 |

---

## Notes

- When the ignition switch is in ON or START and the transaxle/back-up lamp switch is in a forward gear position, the electronic chrome mirror automatically controls the glare of headlights from vehicles behind you in low-light situations.
- When reverse is selected, the mirror reverts to normal (clear) mode to improve visibility while backing up.
- The LHD (SD-132) and RHD (SD-133) schematics are functionally identical; differences are in connector routing only.
- Page SD-135 is a blank memo page.
