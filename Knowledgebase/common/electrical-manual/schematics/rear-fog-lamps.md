---
source: SD.pdf
chapter: SD
section: SD-178 to SD-179
pages: 178-179
title: Rear Fog Lamps
---

# Rear Fog Lamps

**SD-178 -- Rear Fog Lamps (1) Schematic**
**SD-179 -- Component Location Index**

<!-- Figure: Rear Fog Lamps (1) schematic, source: SD.pdf page 178 -->
<!-- Figure: Component Location Index, source: SD.pdf page 179 -->

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 22 (B+ at all times) | -- | -- | R | 2.0B |
| Rear fog lamp relay | coil 85 | -- | O/R | 0.5S |
| Rear fog lamp relay | coil 86 | -- | B | 0.85S |
| Rear fog lamp relay | contact 30 | -- | R | 2.0B |
| Rear fog lamp relay | contact 87 | -- | O/R | 0.85S |
| Rear fog lamp switch (M30) | -- | -- | O/R | 0.5S |
| Left rear fog lamp (M85) | (+) | -- | O/R | 0.85S |
| Left rear fog lamp (M85) | (-) | -- | B | 0.85S |
| Right rear fog lamp (M85) | (+) | -- | O/R | 0.85S |
| Right rear fog lamp (M85) | (-) | -- | B | 0.85S |
| License lamp & rear fog lamp (M85) | -- | -- | O/R | 0.85S |
| Joint connector (M36) | -- | -- | -- | -- |
| Joint connector (M45) | -- | -- | -- | -- |

---

## Circuit Paths

### Rear Fog Lamp Power Circuit
```
Battery (+) → Fuse 22 → [R, 2.0B] → Rear fog lamp relay (contact 30)
  → Rear fog lamp relay (contact 87) → [O/R, 0.85S]
  → via BCM-HM → joint connector M36 → joint connector M45
  → [O/R, 0.85S] → Left rear fog lamp M85 (+) → [B, 0.85S] → GND (G02)
  → [O/R, 0.85S] → Right rear fog lamp M85 (+) → [B, 0.85S] → GND (G02)
```

### Rear Fog Lamp Relay Coil Circuit
```
Tail lamp relay energized (light switch in PARK or HEAD)
  → BCM-FF → [O/R, 0.5S] → Rear fog lamp switch M30 (depressed)
  → [O/R, 0.5S] → Rear fog lamp relay (coil 85)
  → Rear fog lamp relay (coil 86) → [B, 0.85S] → GND (G11)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G02 | Rear area | Rear fog lamp grounds | CL-32 |
| G11 | Dash area | Rear fog lamp relay coil ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-FF | Body Control Module | CL-8 |
| BCM-HM | Body Control Module | CL-8 |

---

## Component Location Index (SD-179)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| M30 | Rear fog lamp switch | CL-3 |
| M36 | Joint connector | CL-4 |
| M45 | Joint connector | CL-4 |
| M85 | License lamp & rear fog lamp | CL-7 |

---

## Notes

- When the rear fog lamp switch is depressed with the light switch in PARK or HEAD, the rear fog lamp coil is energized.
- Battery voltage is supplied to the left/right rear fog lamp lights from Fuse 22 through the rear fog lamp relay contact.
- The rear fog lamps are integrated into the license lamp and rear fog lamp assembly (M85).
- The rear fog lamp relay requires the tail lamp circuit to be active (light switch in PARK or HEAD) before it will energize.
