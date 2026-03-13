---
source: SD.pdf
chapter: SD
section: SD-180 to SD-183
pages: 180-183
title: Tail Parking and License Lamps
---

# Tail, Parking and License Lamps

**SD-180 -- Tail, Parking and License Lamps (1) Schematic**
**SD-181 -- Tail, Parking and License Lamps (2) Schematic**
**SD-182 -- Component Location Index**
**SD-183 -- Memo (blank)**

<!-- Figure: Tail, Parking and License Lamps (1) schematic, source: SD.pdf page 180 -->
<!-- Figure: Tail, Parking and License Lamps (2) schematic, source: SD.pdf page 181 -->
<!-- Figure: Component Location Index, source: SD.pdf page 182 -->

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 8 (B+ at all times) | -- | -- | R | 2.0B |
| Fuse 14 (B+ at all times) | -- | -- | R | 2.0B |
| Fuse 9 (B+ at all times) | -- | -- | R | 2.0B |
| Tail lamp relay (E46) | coil 85 | -- | R/W | 0.85S |
| Tail lamp relay (E46) | coil 86 | -- | B | 0.85S |
| Tail lamp relay (E46) | contact 30 | -- | R | 2.0B |
| Tail lamp relay (E46) | contact 87 | -- | G | 0.85S |
| BCM (Body Control Module) | BCM-LR | -- | -- | -- |
| Multifunction switch (M01-2) | light sw | -- | R/W | 0.85S |
| Left head lamp (E07) | side marker | -- | G | 0.85S |
| Right head lamp (E27) | side marker | -- | G | 0.85S |
| Left rear combination lamp (M82) | tail | -- | G | 0.85S |
| Right rear combination lamp (M84) | tail | -- | G | 0.85S |
| License lamp & rear fog lamp (M85) | license | -- | G | 0.85S |
| Joint connector (M36) | -- | -- | -- | -- |
| Joint connector (M45) | -- | -- | -- | -- |
| Joint connector (E66) | -- | -- | -- | -- |

---

## Circuit Paths

### Tail Lamp Relay Coil Circuit (SD-180)
```
Multifunction switch M01-2 (light sw in PARK or HEAD)
  → [R/W, 0.85S] → BCM-LR → Tail lamp relay E46 (coil 85)
  → Tail lamp relay E46 (coil 86) → [B, 0.85S] → GND
```

### Front Side Marker Lamps (SD-180)
```
Battery (+) → Fuse 8 → [R, 2.0B] → Tail lamp relay E46 (contact 30)
  → Tail lamp relay E46 (contact 87) → [G, 0.85S]
  → via BCM-CE → joint connector E66
  → [G, 0.85S] → Left head lamp E07 (side marker) → [B, 0.85S] → GND (G20)
  → [G, 0.85S] → Right head lamp E27 (side marker) → [B, 0.85S] → GND (G25)
```

### Rear Tail Lamps (SD-181)
```
Battery (+) → Fuse 14 → [R, 2.0B] → joint connector
  → via BCM-FF → BCM-JM → BCM-CE
  → [G, 0.85S] → Left rear combination lamp M82 (tail) → [B, 0.85S] → GND (G02)
  → [G, 0.85S] → Right rear combination lamp M84 (tail) → [B, 0.85S] → GND (G05)
```

### License Plate Lamps (SD-181)
```
Battery (+) → Fuse 14 → [R, 2.0B] → joint connector
  → via BCM-FF → BCM-JM
  → [G, 0.85S] → License lamp & rear fog lamp M85 (license) → [B, 0.85S] → GND (G02)
```

### Left/Right Park Lamp and License Lamp (SD-181)
```
Fuse 9 → [R, 2.0B] → joint connector → BCM-EE
  → [G, 0.85S] → Left rear combination lamp M82 (park) → [B, 0.85S] → GND (G02)
  → [G, 0.85S] → Right rear combination lamp M84 (park) → [B, 0.85S] → GND (G05)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G02 | Rear area | Left rear combination lamp, license lamp | CL-32 |
| G05 | Rear area | Right rear combination lamp | CL-32 |
| G12 | Dash area | Front side marker ground (left) | CL-33 |
| G15 | Engine compartment | Front side marker ground (right) | CL-33 |
| G20 | Engine compartment | Left head lamp side marker ground | CL-32 |
| G25 | Engine compartment | Right head lamp side marker ground | CL-32 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-CE | Body Control Module | CL-14 |
| BCM-DE | Body Control Module | CL-14 |
| BCM-FF | Body Control Module | CL-8 |
| BCM-HM | Body Control Module | CL-8 |
| BCM-LM | Body Control Module | CL-8 |

---

## Component Location Index (SD-182)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| E07 | Left head lamp | CL-10 |
| E27 | Right head lamp | CL-11 |
| E66 | Joint connector | CL-12 |
| M01-2 | Multifunction switch | CL-2 |
| M36 | Joint connector | CL-4 |
| M45 | Joint connector | CL-4 |
| M82 | Left rear combination lamp | CL-7 |
| M84 | Right rear combination lamp | CL-7 |
| M85 | License lamp & rear fog lamp | CL-7 |

---

## Notes

- Battery voltage is applied at all times to the coil and contacts of the tail lamp relay from the B+/T fusible link.
- With the light switch in the multifunction switch in PARK or HEAD, the coil of the tail lamp relay is grounded through the light switch. Battery voltage from Fuse 8 and Fuse 14 is then provided to the lamps (Right/Left side marker lamps, Left/Right tail lamps, Left/Right park lamp and license lamps) through the tail lamp relay contact and all the lamps go on.
- The tail lamp relay is shared with the front fog lamp circuit (see front-fog-lamps.md) and the rear fog lamp circuit (see rear-fog-lamps.md); the tail lamp relay must be energized before either fog lamp circuit can operate.
