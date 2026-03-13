---
source: SD.pdf
chapter: SD
section: SD-106 to SD-109
pages: 106-109
title: Front Wiper and Washer
---

# Front Wiper and Washer

**SD-106 -- Front Wiper & Washer (1) Schematic (LHD)**
**SD-107 -- Front Wiper & Washer (2) Schematic (RHD)**
**SD-108 -- Component Location Index**
**SD-109 -- Memo (blank)**

<!-- Figure: Front wiper motor, washer motor, multifunction switch, front wiper relay, and BCM integration, source: SD.pdf page 106 -->
<!-- Figure: RHD variant of front wiper & washer circuit, source: SD.pdf page 107 -->

---

## Component Table (LHD -- SD-106)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 10 (HOT in ACC or ON) | -- | -- | R/L | 1.25S |
| Fuse 15 (HOT in ACC or ON) | -- | -- | W/R | 0.85S |
| Front wiper relay (E44) | coil 85 | -- | L/R | 0.5S |
| Front wiper relay (E44) | coil 86 | -- | B | 0.5S |
| Front wiper relay (E44) | contact 30 | -- | R/L | 1.25S |
| Front wiper relay (E44) | contact 87 | -- | L/R | 1.25S |
| Front wiper motor (C57) | high | -- | L/W | 1.25B |
| Front wiper motor (C57) | low | -- | L/R | 1.25B |
| Front wiper motor (C57) | +1 (park switch) | -- | L/B | 0.85S |
| Front wiper motor (C57) | +2 (park switch) | -- | L | 0.85S |
| Front wiper motor (C57) | ground | -- | B | 1.25B |
| Washer motor (C58) | (+) | -- | W/R | 0.85S |
| Washer motor (C58) | (-) | -- | B | 0.85S |
| Multifunction switch (M01-1) | INT | -- | L/B | 0.85S |
| Multifunction switch (M01-1) | LOW | -- | L/R | 0.5S |
| Multifunction switch (M01-1) | HIGH | -- | L/W | 0.5S |
| Multifunction switch (M01-1) | WASH | -- | W/R | 0.85S |
| Multifunction switch (M01-1) | +1 | -- | L/B | 0.85S |
| Multifunction switch (M01-1) | +2 | -- | L | 0.85S |
| Joint connector (E56) | -- | -- | -- | -- |
| Joint connector (M34) | -- | -- | -- | -- |
| BCM (Body Control Module) | INT relay control | -- | L/B | 0.85S |

---

## Circuit Paths (LHD)

### Wiper Motor Power -- Low Speed
```
Battery (+) → BCM Box Fuse 10 (HOT in ACC or ON)
  → [R/L, 1.25S] → Front wiper relay E44 (contact 30)
  → Front wiper relay E44 (contact 87) → [L/R, 1.25S]
  → Joint connector E56 → [L/R, 1.25B]
  → Front wiper motor C57 (low speed input)
  → [B, 1.25B] → GND (G16)
```

### Wiper Motor Power -- High Speed
```
Battery (+) → BCM Box Fuse 10 (HOT in ACC or ON)
  → [R/L, 1.25S] → BCM-LR connector
  → [L/W, 1.25B] → Front wiper motor C57 (high speed input)
  → [B, 1.25B] → GND (G16)
```

### Wiper Relay Coil Circuit
```
Multifunction switch M01-1 (LOW position)
  → [L/R, 0.5S] → Front wiper relay E44 (coil 85)
Front wiper relay E44 (coil 86) → [B, 0.5S] → GND
```

### Multifunction Switch -- Speed Selection
```
Multifunction switch M01-1 (LOW) → [L/R, 0.5S] → Wiper relay E44 coil 85 (relay energizes, low speed)
Multifunction switch M01-1 (HIGH) → [L/W, 0.5S] → Wiper motor C57 high speed input (direct, bypasses relay)
```

### Intermittent (INT) Wiper Circuit
```
Multifunction switch M01-1 (INT position)
  → [L/B, 0.85S] → BCM (intermittent relay control)
  → BCM switches wiper relay E44 coil ground on/off per INT timing
  → Front wiper relay E44 (contact 87) → [L/R, 1.25S] → Wiper motor C57 (low)
```

### Wiper Park Switch Circuit
```
Front wiper motor C57 (+1 park) → [L/B, 0.85S] → Multifunction switch M01-1 (+1)
Front wiper motor C57 (+2 park) → [L, 0.85S] → Multifunction switch M01-1 (+2)
  → Park switch feedback ensures motor runs to park position when switch is turned OFF
```

### Washer Motor Circuit
```
Battery (+) → BCM Box Fuse 15 (HOT in ACC or ON)
  → [W/R, 0.85S] → Multifunction switch M01-1 (WASH position, pull toward driver)
  → [W/R, 0.85S] → Washer motor C58 (+)
Washer motor C58 (-) → [B, 0.85S] → GND (G16)
```

### Front Porch Light Link
```
BCM → [B/W, 0.5S] → Front porch light relay input
  (wiper operation triggers front porch light via BCM)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G16 | Engine compartment | Wiper motor ground, washer motor ground | CL-33 |
| G25 | Engine compartment | Wiper relay ground | CL-34 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-CE | BCM engine compartment connector | CL-14 |
| BCM-JM | BCM junction connector | CL-4 |
| BCM-KM | BCM passenger compartment connector | CL-8 |
| EC02 | Engine compartment connector | CL-14 |
| EC102 | Engine compartment connector | CL-14 |
| EC202 | Engine compartment connector | CL-14 |
| EM01 | Engine compartment connector | CL-14 |
| MC01 | Multifunction switch connector | CL-8 |
| MC101 | Multifunction switch connector | CL-8 |
| MC03 | Multifunction switch connector | CL-8 |

---

## Component Location Index (SD-108)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C57 | Front wiper motor (2.0L) | CL-18 |
| C107 | Front wiper motor (2.7L) | CL-25 |
| C207 | Front wiper motor (1.6L) | CL-26 |
| C58 | Washer motor | CL-11 |
| E44 | Front wiper relay | CL-12 |
| E56 | Joint connector | CL-12 |
| M01-1 | Multifunction switch | CL-2 |
| M34 | Joint connector | CL-4 |

---

## Notes

- Battery voltage is supplied to the wiper switch from Fuse 10. When the ignition is turned on and the wiper switch is in LO or High position, the battery voltage is grounded at G202(2.0L) or G302(2.7L) through the wiper motor.
- Intermittent (INT) operation: when the wiper switch is in INT and ignition switch is in ON, the wiper relay coil is energized through BCM. The voltage is grounded at G202(2.0L) or G302(2.7L) through the INT position of the wiper switch and the low position of the wiper motor.
- Washer operation: battery voltage is supplied to the washer switch from Fuse 15. When the ignition switch is on and the washer is activated, the battery voltage is grounded at G16 through the washer motor.
- The LHD (SD-106) and RHD (SD-107) schematics are functionally identical; differences are in connector routing only.
- Page SD-109 is a blank memo page.
