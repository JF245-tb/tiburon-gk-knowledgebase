---
source: SD.pdf
chapter: SD
section: SD-158 to SD-159
pages: 158-159
title: Horns
---

# Horns

**SD-158 -- Horns (1) Schematic**
**SD-159 -- Component Location Index**

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 4 (B+ at all times) | -- | -- | R | 3.0W |
| Horn relay (E45) | coil 85 | -- | B/R | 0.5S |
| Horn relay (E45) | coil 86 | -- | B | 0.85S |
| Horn relay (E45) | contact 30 | -- | R | 3.0W |
| Horn relay (E45) | contact 87 | -- | L/O | 1.25B |
| Multifunction switch (M01-1) | horn | -- | B/R | 0.5S |
| Multifunction switch (Remocon sw) (M01-3) | -- | -- | B/R | 0.5S |
| Left horn (E70) | (+) | -- | L/O | 1.25B |
| Left horn (E70) | (-) | -- | B | 1.25B |
| Center horn (E71) | (+) | -- | L/O | 1.25B |
| Center horn (E71) | (-) | -- | B | 1.25B |
| Clock spring | -- | -- | B/R | 0.5S |
| BCM (Body Control Module) | -- | -- | B/R | 0.5S |

---

## Circuit Paths

### Horn Power Circuit
```
Battery (+) → Fuse 4 → [R, 3.0W] → Horn relay E45 (contact 30)
  → Horn relay E45 (contact 87) → [L/O, 1.25B] → Left horn E70 (+)
  → Horn relay E45 (contact 87) → [L/O, 1.25B] → Center horn E71 (+)
```

### Horn Relay Coil Circuit (Steering Wheel Switch)
```
Fuse 4 → [R, 3.0W] → Horn relay E45 (coil 85, B+ side)
Horn relay E45 (coil 86) → [B/R, 0.5S] → Multifunction switch M01-1 (horn contact)
  → Clock spring → [B/R, 0.5S] → Horn switch (steering wheel)
  → [B, 0.85S] → GND (G16)
```

### Horn Relay Coil Circuit (Remote Control)
```
Horn relay E45 (coil 86) → [B/R, 0.5S] → Multifunction switch (Remocon sw) M01-3
  → BCM → GND
```

### Horn Ground Circuit
```
Left horn E70 (-) → [B, 1.25B] → GND (G16)
Center horn E71 (-) → [B, 1.25B] → GND (G16)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G16 | Engine compartment | Horn grounds, horn relay coil ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| EC02 | Engine compartment | CL-14 |
| EC102 | Engine compartment | CL-14 |
| EE02 | Engine compartment | CL-14 |
| MC03 | Multifunction switch | CL-8 |
| MC103 | Multifunction switch | CL-8 |
| MC203 | Multifunction switch | CL-8 |

---

## Component Location Index (SD-159)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| E45 | Horn relay | CL-12 |
| E70 | Left horn | CL-13 |
| E71 | Center horn | CL-13 |
| M01-1 | Multifunction switch | CL-2 |
| M01-3 | Multifunction switch (Remocon sw) | CL-2 |

---

## Notes

- Battery voltage is applied at all times to both the coil and the contacts of the horn relay.
- With the horn switch depressed, ground is provided to the coil of the horn relay through the horn switch.
- The relay contacts close and apply battery voltage to the horns, sounding the horns.
- The remote control (Remocon) switch path through M01-3 allows the BCM to trigger the horn for keyless entry confirmation.
