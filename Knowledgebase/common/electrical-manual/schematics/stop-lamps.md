---
source: SD.pdf
chapter: SD
section: SD-186 to SD-187
pages: 186-187
title: Stop Lamps
---

# Stop Lamps

**SD-186 -- Stop Lamps (1) Schematic**
**SD-187 -- Component Location Index**

<!-- Figure: Stop Lamps (1) schematic, source: SD.pdf page 186 -->
<!-- Figure: Component Location Index, source: SD.pdf page 187 -->

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 13 (B+ at all times) | -- | -- | R | 2.0B |
| Stop lamp switch (W/O Cruise, 2.0L) (C31) | -- | -- | G/W | 0.85S |
| Stop lamp switch (With Cruise, 2.0L) (C32) | -- | -- | G/W | 0.85S |
| Stop lamp switch (W/O Cruise, 2.7L) (C131) | -- | -- | G/W | 0.85S |
| Stop lamp switch (With Cruise, 2.7L) (C132) | -- | -- | G/W | 0.85S |
| Cruise control module (2.0L) (C36) | -- | -- | G/W | 0.85S |
| TCM (2.0L) (C36-3) | -- | -- | G/W | 0.85S |
| TCM (2.7L) (C136-3) | -- | -- | G/W | 0.85S |
| Joint connector (C41) | -- | -- | G/W | 0.85S |
| Joint connector (C241) | -- | -- | G/W | 0.85S |
| Left rear combination lamp (M82) | stop | -- | G/W | 0.85S |
| Left rear combination lamp (M82) | ground | -- | B | 0.85S |
| Right rear combination lamp (M84) | stop | -- | G/W | 0.85S |
| Right rear combination lamp (M84) | ground | -- | B | 0.85S |
| High-mounted stop lamp — spoiler (R12) | (+) | -- | G/W | 0.85S |
| High-mounted stop lamp — spoiler (R12) | (-) | -- | B | 0.85S |
| High-mounted stop lamp — P/Tray (R11) | (+) | -- | G/W | 0.85S |
| High-mounted stop lamp — P/Tray (R11) | (-) | -- | B | 0.85S |

---

## Circuit Paths

### Stop Lamp Circuit — Without Cruise Control
```
Battery (+) → Fuse 13 → [R, 2.0B] → Stop lamp switch C31/C131 (brake pedal depressed)
  → [G/W, 0.85S] → joint connector C41 → BCM-KM → BCM-FF
  → [G/W, 0.85S] → Left rear combination lamp M82 (stop) → [B, 0.85S] → GND (G02)
  → [G/W, 0.85S] → Right rear combination lamp M84 (stop) → [B, 0.85S] → GND (G05)
  → [G/W, 0.85S] → High-mounted stop lamp R12/R11 (+) → [B, 0.85S] → GND (G06)
```

### Stop Lamp Circuit — With Cruise Control
```
Battery (+) → Fuse 13 → [R, 2.0B] → Stop lamp switch C32/C132 (brake pedal depressed)
  → [G/W, 0.85S] → Cruise control module C36 (stop lamp signal)
  → [G/W, 0.85S] → joint connector C41 → BCM-KM → BCM-FF
  → [G/W, 0.85S] → Left rear combination lamp M82 (stop) → [B, 0.85S] → GND (G02)
  → [G/W, 0.85S] → Right rear combination lamp M84 (stop) → [B, 0.85S] → GND (G05)
  → [G/W, 0.85S] → High-mounted stop lamp R12/R11 (+) → [B, 0.85S] → GND (G06)
```

### Stop Lamp to TCM Signal
```
Stop lamp switch (brake pedal depressed)
  → [G/W, 0.85S] → TCM C36-3 / C136-3 (stop lamp input)
  TCM uses stop lamp signal for shift control logic
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G02 | Rear area | Left rear combination lamp ground | CL-32 |
| G05 | Rear area | Right rear combination lamp ground | CL-32 |
| G06 | Rear area | High-mounted stop lamp ground | CL-32 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-KM | Body Control Module | CL-6 |
| BCM-FF | Body Control Module | CL-8 |
| MC201 | Multifunction connector | CL-8 |
| MC101 | Multifunction connector | CL-8 |
| MR01 | Rear connector | CL-9 |
| MR02 | Rear connector | CL-9 |
| RR02 | Rear connector | CL-31 |

---

## Component Location Index (SD-187)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C31 | Stop lamp switch (W/O Cruise, 2.0L) | CL-20 |
| C32 | Stop lamp switch (With Cruise, 2.0L) | CL-20 |
| C36 | Cruise control module (2.0L) | CL-21 |
| C36-3 | TCM (2.0L) | CL-21 |
| C41 | Joint connector | CL-21 |
| C131 | Stop lamp switch (W/O Cruise, 2.7L) | CL-25 |
| C132 | Stop lamp switch (With Cruise, 2.7L) | CL-25 |
| C136-3 | TCM (2.7L) | CL-25 |
| C241 | Joint connector (1.6L) | CL-4 |
| M82 | Left rear combination lamp | CL-7 |
| M84 | Right rear combination lamp | CL-7 |
| R12 | High-mounted stop lamp (spoiler) | CL-31 |
| R11 | High-mounted stop lamp (P/Tray) | CL-31 |

---

## Notes

- Battery voltage is applied to the stop lamp switch at all times from Fuse 13.
- With the brake pedal depressed, the stop lamp switch is closed and battery voltage is applied to all the stop lamps (left/right stop lamps and high-mounted stop lamp) and the lamps go on.
- On vehicles with cruise control, the stop lamp switch signal also passes through the cruise control module (C36) to cancel cruise control when braking.
- The stop lamp signal is also fed to the TCM for shift control logic (brake-on detection for torque converter lock-up release, etc.).
- Two high-mounted stop lamp variants exist: R12 (spoiler-mounted) and R11 (package tray-mounted, P/Tray). Only one is installed per vehicle.
