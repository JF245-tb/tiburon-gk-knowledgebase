---
source: SD.pdf
chapter: SD
section: SD-160 to SD-161
pages: 160-161
title: Head Lamps
---

# Head Lamps

**SD-160 -- Head Lamps (1) Schematic**
**SD-161 -- Component Location Index**

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 17 (IGN/ON) | -- | -- | R/Y | 2.0B |
| Fuse 11 | -- | -- | R | 2.0B |
| Head lamp relay (LOW) (E48) | coil 85 | -- | R/W | 0.85S |
| Head lamp relay (LOW) (E48) | coil 86 | -- | B | 0.85S |
| Head lamp relay (LOW) (E48) | contact 30 | -- | R | 2.0B |
| Head lamp relay (LOW) (E48) | contact 87 | -- | W | 1.25B |
| Head lamp relay (HIGH) (E51) | coil 85 | -- | R/B | 0.85S |
| Head lamp relay (HIGH) (E51) | coil 86 | -- | B | 0.85S |
| Head lamp relay (HIGH) (E51) | contact 30 | -- | R | 2.0B |
| Head lamp relay (HIGH) (E51) | contact 87 | -- | R/W | 1.25B |
| Left head lamp (E07) | low beam | -- | W | 1.25B |
| Left head lamp (E07) | high beam | -- | R/W | 1.25B |
| Left head lamp (E07) | ground | -- | B | 0.85S |
| Right head lamp (E27) | low beam | -- | W | 1.25B |
| Right head lamp (E27) | high beam | -- | R/W | 1.25B |
| Right head lamp (E27) | ground | -- | B | 0.85S |
| Multifunction switch (M01-1) | light sw | -- | R/W | 0.85S |
| Multifunction switch (M01-1) | dimmer | -- | R/B | 0.85S |
| Multifunction switch (M01-1) | flash | -- | R/B | 0.85S |
| Daytime running light control module | -- | -- | -- | -- |
| Joint connector (E58) | -- | -- | -- | -- |
| Instrument cluster (M10) | high beam indicator | -- | R/B | 0.5S |

---

## Circuit Paths

### Low Beam Circuit
```
Battery (+) → Fuse 11 → [R, 2.0B] → Head lamp relay LOW E48 (contact 30)
  → Head lamp relay LOW E48 (contact 87) → [W, 1.25B]
  → Left head lamp E07 (low beam) → [B, 0.85S] → GND (G11)
  → Right head lamp E27 (low beam) → [B, 0.85S] → GND (G15)
```

### Low Beam Relay Coil Circuit
```
IGN switch ON → Fuse 17 → [R/Y, 2.0B] → Multifunction switch M01-1 (light sw)
  → [R/W, 0.85S] → Head lamp relay LOW E48 (coil 85)
  → Head lamp relay LOW E48 (coil 86) → [B, 0.85S] → GND
```

### High Beam Circuit
```
Battery (+) → Fuse 11 → [R, 2.0B] → Head lamp relay HIGH E51 (contact 30)
  → Head lamp relay HIGH E51 (contact 87) → [R/W, 1.25B]
  → Left head lamp E07 (high beam) → [B, 0.85S] → GND (G11)
  → Right head lamp E27 (high beam) → [B, 0.85S] → GND (G15)
```

### High Beam Relay Coil Circuit
```
IGN switch ON → Fuse 17 → Multifunction switch M01-1 (dimmer in HIGH)
  → [R/B, 0.85S] → Head lamp relay HIGH E51 (coil 85)
  → Head lamp relay HIGH E51 (coil 86) → [B, 0.85S] → GND
```

### Flash-to-Pass Circuit
```
Multifunction switch M01-1 (flash) → [R/B, 0.85S]
  → Head lamp relay HIGH E51 (coil 85) — bypasses light switch position
  Operates with light switch in OFF, PARK, or HEAD positions
  (switch held in FLASH position applies ground to high beam relay coil)
```

### High Beam Indicator Circuit
```
Head lamp relay HIGH E51 (contact 87) → [R/B, 0.5S]
  → Instrument cluster M10 (high beam indicator)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G11 | Dash area | Left head lamp ground | CL-33 |
| G15 | Engine compartment | Right head lamp ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| EC01 | Engine compartment | CL-14 |
| BCM-HM | Body Control Module | CL-8 |
| D01 | Dash connector | CL-4 |

---

## Component Location Index (SD-161)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| E07 | Left head lamp | CL-10 |
| E27 | Right head lamp | CL-11 |
| E48 | Head lamp relay (LOW) | CL-12 |
| E51 | Head lamp relay (HIGH) | CL-12 |
| E58 | Joint connector | CL-12 |
| M01-1 | Multifunction switch | CL-2 |
| M10 | Instrument cluster | CL-3 |
| M58 | Joint connector | CL-4 |

---

## Notes

### Low Beam Operation
- With the ignition switch in ON, battery voltage is applied to the coil of the head lamp relays (low and high) through Fuse 17.
- With the light switch in HEAD and the dimmer switch in low, ground is provided to the coil of the low beam relay through the head lamp fuse.
- The low beam relay contacts close and battery voltage from the head lamp fuse is provided to the low beam headlamps through the closed contacts of the head lamp relay (low).

### High Beam Operation
- With the ignition switch in ON, battery voltage is applied to the coil of the head lamp relay through Fuse 17.
- With the light switch in HEAD and the dimmer switch in HIGH, ground is provided to the coil of the high beam relay.
- Battery voltage from the head lamp fuse is then provided to the high beam headlamps and the beam indicator in the instrument cluster.

### Flash Operation
- The flash feature works with the light switch in all positions (OFF, PARK, or HEAD).
- With the light switch in OFF or PARK and the head lamp dimmer switch held in FLASH, ground is provided to the high beam headlamps and the beam indicator light.
- As long as the switch is held in the FLASH position, the high beam indicator light is on.
