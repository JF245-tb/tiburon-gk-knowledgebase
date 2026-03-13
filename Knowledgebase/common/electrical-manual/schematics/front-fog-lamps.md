---
source: SD.pdf
chapter: SD
section: SD-176 to SD-177
pages: 176-177
title: Front Fog Lamps
---

# Front Fog Lamps

**SD-176 -- Front Fog Lamps (1) Schematic**
**SD-177 -- Component Location Index**

<!-- Figure: Front Fog Lamps (1) schematic, source: SD.pdf page 176 -->
<!-- Figure: Component Location Index, source: SD.pdf page 177 -->

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 8 (B+ at all times) | -- | -- | R | 2.0B |
| Fuse 17 (IGN/ON) | -- | -- | R/Y | 2.0B |
| Front fog lamp relay (E47) | coil 85 | -- | G/R | 0.85S |
| Front fog lamp relay (E47) | coil 86 | -- | B | 0.85S |
| Front fog lamp relay (E47) | contact 30 | -- | R | 2.0B |
| Front fog lamp relay (E47) | contact 87 | -- | Y/B | 1.25B |
| Left front fog lamp (E14) | (+) | -- | Y/B | 0.85S |
| Left front fog lamp (E14) | (-) | -- | B | 0.85S |
| Right front fog lamp (E30) | (+) | -- | Y/B | 0.85S |
| Right front fog lamp (E30) | (-) | -- | B | 0.85S |
| Front fog lamp switch (M14) | -- | -- | G/R | 0.85S |
| Multifunction switch (M01-2) | light sw | -- | R/W | 0.85S |
| BCM (Body Control Module) | BCM-CE | -- | -- | -- |
| Joint connector (E66) | -- | -- | -- | -- |
| Joint connector (M58) | -- | -- | -- | -- |

---

## Circuit Paths

### Fog Lamp Power Circuit
```
Battery (+) → Fuse 8 → [R, 2.0B] → Front fog lamp relay E47 (contact 30)
  → Front fog lamp relay E47 (contact 87) → [Y/B, 1.25B]
  → joint connector E66 → [Y/B, 0.85S] → Left front fog lamp E14 (+) → [B, 0.85S] → GND (G12)
  → joint connector E66 → [Y/B, 0.85S] → Right front fog lamp E30 (+) → [B, 0.85S] → GND (G15)
```

### Fog Lamp Relay Coil Circuit
```
IGN switch ON → Fuse 17 → [R/Y, 2.0B] → Multifunction switch M01-2 (light sw in PARK or HEAD)
  → [R/W, 0.85S] → BCM-CE → BCM (tail lamp relay coil energized)
  → Front fog lamp switch M14 (ON) → [G/R, 0.85S]
  → Front fog lamp relay E47 (coil 85)
  → Front fog lamp relay E47 (coil 86) → [B, 0.85S] → GND
```

### Fog Lamp Indicator Circuit
```
Front fog lamp relay E47 (contact 87) → [G/R, 0.5S]
  → Multifunction switch M01-2 → Instrument cluster (fog lamp indicator)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G1 | Engine compartment | Fog lamp relay coil ground | CL-33 |
| G12 | Dash area | Left front fog lamp ground | CL-33 |
| G15 | Engine compartment | Right front fog lamp ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-CE | Body Control Module | CL-14 |
| BCM-DE | Body Control Module | CL-14 |
| BCM-HM | Body Control Module | CL-8 |
| BCM-LM | Body Control Module | CL-8 |
| EM01 | Engine compartment | CL-14 |

---

## Component Location Index (SD-177)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| E14 | Left front fog lamp | CL-10 |
| E30 | Right front fog lamp | CL-11 |
| E47 | Front fog lamp relay | CL-12 |
| E66 | Joint connector | CL-12 |
| M01-2 | Multifunction switch | CL-2 |
| M14 | Front fog lamp switch | CL-2 |
| M58 | Joint connector | CL-4 |

---

## Notes

- Battery voltage is applied at all times to the front fog lamp relay contacts (contact 30) through Fuse 8.
- When the light switch is in PARK or HEAD, the tail lamp relay coil is energized through the BCM (body control module) and battery voltage is applied to the front fog lamp switch.
- When the front fog lamp switch is ON, ground is provided to the coil of the fog lamp relay. Battery voltage from the front fog lamps fuse is then provided to the LEFT/RIGHT front fog lamps through the closed contacts of the front fog lamp relay.
- The front fog lamps will only operate when the light switch is in the PARK or HEAD position.
