---
source: SD.pdf
chapter: SD
section: SD-172 to SD-175
pages: 172-175
title: Turn and Hazard Lamps
---

# Turn and Hazard Lamps

**SD-172 -- Turn and Hazard Lamps (1) Schematic**
**SD-173 -- Turn and Hazard Lamps (2) Schematic**
**SD-174 -- Component Location Index**
**SD-175 -- Memo (blank)**

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 7 (B+ at all times) | -- | -- | R | 2.0W |
| Hazard switch (M13) | -- | -- | -- | -- |
| Solid-state hazard relay | -- | -- | -- | -- |
| Multifunction switch (M01-2) | turn L | -- | G/B | 0.85S |
| Multifunction switch (M01-2) | turn R | -- | G/W | 0.85S |
| Instrument cluster (M10-1) | left turn indicator | -- | G/B | 0.5S |
| Instrument cluster (M10-2) | right turn indicator | -- | G/W | 0.5S |
| Left turn signal lamp (E29) | (+) | -- | G/B | 0.85S |
| Left turn signal lamp (E29) | (-) | -- | B | 0.85S |
| Right turn signal lamp (E30) | (+) | -- | G/W | 0.85S |
| Right turn signal lamp (E30) | (-) | -- | B | 0.85S |
| Left side repeater lamp (E04) | (+) | -- | G/B | 0.5S |
| Left side repeater lamp (E04) | (-) | -- | B | 0.5S |
| Right side repeater lamp (E06) | (+) | -- | G/W | 0.5S |
| Right side repeater lamp (E06) | (-) | -- | B | 0.5S |
| Left rear combination lamp (M82) | turn | -- | G/B | 0.85S |
| Left rear combination lamp (M82) | ground | -- | B | 0.85S |
| Right rear combination lamp (M84) | turn | -- | G/W | 0.85S |
| Right rear combination lamp (M84) | ground | -- | B | 0.85S |
| DRL module (daytime running light) | -- | -- | -- | -- |

---

## Circuit Paths

### Turn Signal — Left
```
Fuse 7 → [R, 2.0W] → Hazard relay (solid-state) → Multifunction switch M01-2 (LEFT)
  → [G/B, 0.85S] → Left turn signal lamp E29 (+) → [B, 0.85S] → GND (G10)
  → [G/B, 0.85S] → Left rear combination lamp M82 (turn) → [B, 0.85S] → GND
  → [G/B, 0.5S] → Left side repeater lamp E04 (+) → [B, 0.5S] → GND (G06)
  → [G/B, 0.5S] → Instrument cluster M10-1 (left turn indicator)
```

### Turn Signal — Right
```
Fuse 7 → [R, 2.0W] → Hazard relay (solid-state) → Multifunction switch M01-2 (RIGHT)
  → [G/W, 0.85S] → Right turn signal lamp E30 (+) → [B, 0.85S] → GND (G14)
  → [G/W, 0.85S] → Right rear combination lamp M84 (turn) → [B, 0.85S] → GND
  → [G/W, 0.5S] → Right side repeater lamp E06 (+) → [B, 0.5S] → GND (G14)
  → [G/W, 0.5S] → Instrument cluster M10-2 (right turn indicator)
```

### Hazard Circuit
```
Fuse 7 → [R, 2.0W] → Hazard switch M13 (ON position)
  → Solid-state hazard relay alternately applies and removes battery voltage
  → Both left and right turn signal circuits simultaneously
  → All turn signal lamps + both indicators flash
```

### Turn Signal Page 2 (SD-173) — Rear Lamps via Joint Connector
```
Left turn: [G/B] → via BCM-CE connector → joint connector → Left rear combination lamp M82
Right turn: [G/W] → via BCM-CE connector → joint connector → Right rear combination lamp M84
```

### DRL Integration (SD-173)
```
DRL control module → Multifunction switch M01-2
  → See Illumination circuits for DRL lamp path
Joint connector M58 → [G/B, G/W] → DRL module inputs
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G02 | Engine compartment | Turn signal lamp grounds | CL-32 |
| G05 | Engine compartment | Turn signal grounds | CL-32 |
| G11 | Dash area | Instrument cluster ground | CL-33 |
| G18 | Rear area | Rear combination lamp grounds | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-CE | Body Control Module | CL-14 |
| BCM-FF | Body Control Module | CL-8 |
| BCM-HM | Body Control Module | CL-4 |
| BCM-LM | Body Control Module | CL-8 |

---

## Component Location Index (SD-174)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| E04 | Left side repeater lamp | CL-10 |
| E24 | Left turn signal lamp | CL-10 |
| E29 | Right turn signal lamp | CL-11 |
| E06 | Right side repeater lamp | CL-12 |
| M01-2 | Multifunction switch | CL-2 |
| M10-1 | Instrument cluster | CL-2 |
| M10-2 | Instrument cluster | CL-2 |
| M13 | Hazard switch | CL-4 |
| M82 | Left rear combination lamp | CL-7 |
| M84 | Right rear combination lamp | CL-7 |

---

## Notes

### Turn Signal Lamps
- With the hazard switch in OFF, and ignition switch in ON or START, battery voltage is applied from Fuse 7 to the solid-state hazard relay.
- The solid-state hazard relay senses the turn signal lever position and alternately applies and removes battery voltage to the turn signal lamps.
- Voltage is applied to turn signal lamps and indicators dependent upon the turn signal position.

### Hazard Lamps
- With the hazard switch depressed (ON), battery voltage is applied from Fuse 7 regardless of ignition position.
- The solid-state hazard relay senses that the hazard switch is in the ON position and alternately applies and removes battery voltage to the turn signal lamps and both indicators at the same time.
