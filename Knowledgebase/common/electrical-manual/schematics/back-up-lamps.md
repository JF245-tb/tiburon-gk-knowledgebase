---
source: SD.pdf
chapter: SD
section: SD-184 to SD-185
pages: 184-185
title: Back-Up Lamps
---

# Back-Up Lamps

**SD-184 -- Back-Up Lamps (1) Schematic**
**SD-185 -- Component Location Index**

<!-- Figure: Back-Up Lamps (1) schematic, source: SD.pdf page 184 -->
<!-- Figure: Component Location Index, source: SD.pdf page 185 -->

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 3 (IGN/ON or START) | -- | -- | R | 2.0B |
| Back-up lamp switch — manual transaxle (C06) | -- | -- | V | 0.85S |
| Back-up lamp switch — auto transaxle (C06) | -- | -- | V | 0.85S |
| Transaxle range switch — 2.0L (C01) | -- | -- | V | 0.85S |
| Transaxle range switch — 2.7L (C101) | -- | -- | V | 0.85S |
| TCM — 2.0L (C36-3) | -- | -- | V | 0.85S |
| TCM — 2.7L (C136-3) | -- | -- | V | 0.85S |
| Left rear combination lamp (M82) | back-up | -- | V | 0.85S |
| Left rear combination lamp (M82) | ground | -- | B | 0.85S |
| Right rear combination lamp (M84) | back-up | -- | V | 0.85S |
| Right rear combination lamp (M84) | ground | -- | B | 0.85S |
| Joint connector (C41) | -- | -- | V | 0.85S |
| Instrument cluster (M10-1) | gear indicator R | -- | V | 0.5S |

---

## Circuit Paths

### Back-Up Lamp — Manual Transaxle
```
IGN switch ON or START → Fuse 3 → [R, 2.0B]
  → Back-up lamp switch C06 (transaxle in Reverse)
  → [V, 0.85S] → joint connector C41 → BCM-KM → BCM-FF
  → [V, 0.85S] → Left rear combination lamp M82 (back-up) → [B, 0.85S] → GND (G02)
  → [V, 0.85S] → Right rear combination lamp M84 (back-up) → [B, 0.85S] → GND (G05)
```

### Back-Up Lamp — Auto Transaxle (2.0L)
```
IGN switch ON or START → Fuse 3 → [R, 2.0B]
  → Transaxle range switch C01 (in Reverse)
  → [V, 0.85S] → TCM C36-3
  → [V, 0.85S] → joint connector C41 → BCM-KM → BCM-FF
  → [V, 0.85S] → Left rear combination lamp M82 (back-up) → [B, 0.85S] → GND (G02)
  → [V, 0.85S] → Right rear combination lamp M84 (back-up) → [B, 0.85S] → GND (G05)
```

### Back-Up Lamp — Auto Transaxle (2.7L V6)
```
IGN switch ON or START → Fuse 3 → [R, 2.0B]
  → Transaxle range switch C101 (in Reverse)
  → [V, 0.85S] → TCM C136-3
  → [V, 0.85S] → joint connector C41 → BCM-KM → BCM-FF
  → [V, 0.85S] → Left rear combination lamp M82 (back-up) → [B, 0.85S] → GND (G02)
  → [V, 0.85S] → Right rear combination lamp M84 (back-up) → [B, 0.85S] → GND (G05)
```

### Gear Indicator (Reverse) Circuit
```
Back-up lamp switch / transaxle range switch (Reverse)
  → [V, 0.5S] → Instrument cluster M10-1 (gear indicator R)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G02 | Rear area | Left rear combination lamp ground | CL-32 |
| G05 | Rear area | Right rear combination lamp ground | CL-32 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-FF | Body Control Module | CL-8 |
| BCM-KM | Body Control Module | CL-6 |
| MC201 | Multifunction connector | CL-8 |
| MC101 | Multifunction connector | CL-8 |
| MC001 | Multifunction connector | CL-8 |

---

## Component Location Index (SD-185)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C01 | Transaxle range switch (2.0L) | CL-18 |
| C06 | Back-up lamp switch (2.0L) | CL-18 |
| C06 | Back-up lamp switch (2.0L, BMT) | CL-18 |
| C101 | Transaxle range switch (2.7L) | CL-21 |
| C106 | Back-up lamp switch (2.7L, BMT) | CL-21 |
| C136-3 | TCM (2.7L) | CL-25 |
| C36-3 | TCM (2.0L) | CL-21 |
| C241 | Joint connector (1.6L) | CL-4 |
| M82 | Left rear combination lamp | CL-3 |
| M84 | Right rear combination lamp | CL-3 |

---

## Notes

- With the ignition switch in ON or START, battery voltage is applied from Fuse 3 to the back-up lamp switch (manual transaxle) or the transaxle range switch (automatic transaxle).
- With the transaxle in Reverse, battery voltage is applied to the back-up lamps and the back-up lamps go on.
- For automatic transaxle vehicles, the signal passes through the TCM before reaching the back-up lamp circuit.
- The back-up lamp circuit also feeds the reverse gear indicator in the instrument cluster.
