---
source: SD.pdf
chapter: SD
section: SD-192 to SD-197
pages: 192-197
title: Illuminations
---

# Illuminations

**SD-192 -- Illuminations (1) Schematic**
**SD-193 -- Illuminations (2) Schematic**
**SD-194 -- Illuminations (3) Schematic**
**SD-195 -- Component Location Index**

> Pages SD-196 to SD-197 are the Air Bag System (SRS) section (separate system, included in page range for continuity).

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 9 (HOT AT ALL TIMES) | -- | -- | R | 2.0B |
| Fuse 14 (HOT AT ALL TIMES) | -- | -- | R | 2.0B |
| Tail lamp relay (E47) | coil 85 | -- | R/W | 0.85S |
| Tail lamp relay (E47) | coil 86 | -- | B | 0.85S |
| Tail lamp relay (E47) | contact 30 | -- | R | 2.0B |
| Tail lamp relay (E47) | contact 87 | -- | G | 1.25B |
| BCM-CE | -- | -- | -- | -- |
| BCM-HM | -- | -- | R/W | 0.85S |
| Multifunction switch (M01-1) | light sw | -- | R/W | 0.85S |
| Rheostat (M11) | -- | -- | G | 0.85S |
| Instrument cluster (M10) | illumination | -- | G | 0.5S |
| Audio (M15-2) | illumination | -- | G | 0.5S |
| A/C control module (Manual) (M20) | illumination | -- | G | 0.5S |
| A/C control module (Auto) (M19-1) | illumination | -- | G | 0.5S |
| Heater control illumination | -- | -- | G | 0.5S |
| Digital clock (M11) | illumination | -- | G | 0.5S |
| Power window switch (D51) | illumination | -- | G | 0.5S |
| Cigarette lighter lamp | -- | -- | G | 0.5S |
| Front fog lamp switch (M14) | illumination | -- | G | 0.5S |
| Left front side marker lamp (E08) | -- | -- | G | 0.85S |
| Right front side marker lamp (E28) | -- | -- | G | 0.85S |
| Left rear combination lamp (E09) | tail lamp | -- | G | 1.25B |
| Right rear combination lamp (E29) | tail lamp | -- | G | 1.25B |
| License lamp #1 (O2) | -- | -- | G | 0.85S |
| License lamp #2 (O2) | -- | -- | G | 0.85S |
| Glove box lamp switch #1 (O2) | -- | -- | G/W | 0.5S |
| Glove box lamp switch #2 (O2) | -- | -- | G/W | 0.5S |
| Sport mode switch (2.0L) (C39) | illumination | -- | G | 0.5S |
| Sport mode switch (2.7L) (C139) | illumination | -- | G | 0.5S |
| Left front seat warmer switch (M43) | illumination | -- | G | 0.5S |
| Right front seat warmer switch (M44) | illumination | -- | G | 0.5S |
| Head lamp leveling switch (M12) | illumination | -- | G | 0.5S |
| Ignition switch ring | illumination | -- | G/W | 0.5S |
| Ash tray lamp | -- | -- | G | 0.5S |

---

## Circuit Paths

### Tail Lamp / Illumination Power (Main)
<!-- Figure: Illumination power distribution through tail lamp relay, source: SD.pdf page 192 -->
```
Battery (+) → Fuse 9 (HOT AT ALL TIMES) → [R, 2.0B] → Tail lamp relay E47 (contact 30)
  → Tail lamp relay E47 (contact 87) → [G, 1.25B]
    → Left rear combination lamp E09 (tail) → [B, 0.85S] → GND (G10)
    → Right rear combination lamp E29 (tail) → [B, 0.85S] → GND (G10)
    → Left front side marker lamp E08 → [B, 0.85S] → GND (G11)
    → Right front side marker lamp E28 → [B, 0.85S] → GND (G15)
    → License lamps O2 → [B, 0.85S] → GND (G10)
```

### Tail Lamp Relay Coil Circuit
```
Battery (+) → Fuse 14 (HOT AT ALL TIMES) → [R, 2.0B]
  → Multifunction switch M01-1 (light sw in PARK or HEAD)
  → [R/W, 0.85S] → BCM-HM
  → Tail lamp relay E47 (coil 85) → [R/W, 0.85S]
  → Tail lamp relay E47 (coil 86) → [B, 0.85S] → GND
```

### Illumination Bus (Dimmer-Controlled)
<!-- Figure: Rheostat-controlled illumination bus, source: SD.pdf page 192 -->
```
Tail lamp relay E47 (contact 87) → [G, 1.25B]
  → Rheostat M11 (brightness control) → [G, 0.85S]
    → Instrument cluster M10 (illumination)
    → Audio M15-2 (illumination)
    → A/C control module M20 or M19-1 (illumination)
    → Digital clock M11 (illumination)
    → Cigarette lighter lamp
    → Ash tray lamp
    → Front fog lamp switch M14 (illumination)
    → Head lamp leveling switch M12 (illumination)
    → Sport mode switch C39/C139 (illumination)
    → Power window switch D51 (illumination)
    → Left front seat warmer switch M43 (illumination)
    → Right front seat warmer switch M44 (illumination)
  All → [B, 0.5S] → GND (G11)
```

### Glove Box Lamp Circuit
<!-- Figure: Glove box lamp independent of rheostat, source: SD.pdf page 193 -->
```
Tail lamp relay E47 (contact 87) → [G/W, 0.5S]
  → Glove box lamp switch #1 O2 → GND
  → Glove box lamp switch #2 O2 → GND
```

### Ignition Key Illumination Circuit
```
Tail lamp relay E47 (contact 87) → [G/W, 0.5S]
  → Ignition switch ring (illumination) → GND
```

### Instrument Cluster Illumination Detail (SD-193 / SD-194)
<!-- Figure: Cluster and switch illumination detail showing parallel feeds, source: SD.pdf page 193 -->
```
Rheostat M11 output → [G, 0.5S] parallel bus to:
  M10 (cluster) — multiple internal lamps
  M15-2 (audio) illumination
  M14 (fog lamp switch) illumination
  M12 (headlamp leveling) illumination
  M20 (heater control) illumination
  M43/M44 (seat warmer switches) illumination
  C39/C139 (sport mode switch) illumination
```

### Rear Combination Lamp / Marker Lamp Detail (SD-194)
<!-- Figure: Rear and front marker lamp connections to illumination bus, source: SD.pdf page 194 -->
```
Illumination bus [G, 1.25B] → Joint connector
  → MF6 (left rear combination lamp connector) → E09 tail lamp → [B] → GND (G10)
  → MF7-B (right rear connector) → E29 tail lamp → [B] → GND (G10)
  → Left front side marker E08 → [B] → GND (G11)
  → Right front side marker E28 → [B] → GND (G15)
  → License lamps (×2) → [B] → GND (G10)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G10 | Rear body area | Rear combination lamps, license lamps | CL-33 |
| G11 | Dash area | Left front side marker lamp, cluster illumination | CL-33 |
| G12 | Dash area | Illumination ground bus | CL-33 |
| G15 | Engine compartment | Right front side marker lamp | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-CE | Body Control Module | CL-8 |
| BCM-HM | Body Control Module | CL-8 |
| BCM-JM | Body Control Module | CL-8 |
| MC02 | Multifunction switch connector | CL-8 |
| MC03 | Multifunction switch connector | CL-8 |
| MD01 | Dash connector | CL-4 |
| MD02 | Dash connector | CL-4 |
| MR01 | Rear connector | CL-9 |

---

## Component Location Index (SD-195)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C39 | Sport mode switch (2.0L) | CL-21 |
| C139 | Sport mode switch (2.7L) | CL-23 |
| C39-1 | TCM (2.0L) | CL-21 |
| D15 | Right power window switch | CL-30 |
| M01-1 | Multifunction switch | CL-2 |
| M10 | Instrument cluster | CL-3 |
| M10-1 | Instrument cluster | CL-3 |
| M11 | Digital clock | CL-3 |
| M12 | Head lamp leveling switch | CL-3 |
| M14 | Front fog lamp switch | CL-3 |
| M15-2 | Audio | CL-4 |
| M19-1 | A/C control module (Auto A/C) | CL-3 |
| M20 | A/C control module (Manual A/C) | CL-3 |
| M30 | Rheostat | CL-3 |
| M33 | Joint connector | CL-4 |
| M38 | Joint connector | CL-4 |
| M43 | Left front seat warmer switch | CL-4 |
| M44 | Right front seat warmer switch | CL-4 |
| M45 | Joint connector | CL-4 |
| M46 | Joint connector | CL-4 |
| M47 | Joint connector | CL-4 |
| O2 | Glove box lamp switch #1 | CL-15 |
| -- | Glove box lamp switch #2 | CL-15 |

### Connectors

| Connector | Location Page |
|-----------|---------------|
| BCM-CE | CL-14 |
| BCM-HF | CL-8 |
| BCM-HM | CL-8 |
| BCM-M | CL-8 |
| MC02 | CL-8 |
| MC03 | CL-8 |
| MD01 | CL-4 |
| MD02 | CL-4 |
| MR01 | CL-9 |

### Grounds

| Ground ID | Location Page |
|-----------|---------------|
| G10 | CL-33 |
| G11 | CL-33 |
| G12 | CL-33 |

---

## Notes

### Illumination Control
- Battery voltage is applied at all times to the coil and the contacts of the tail lamp relay from the BATT fusible link.
- With the light switch (multifunction switch) in the PARK or HEAD position, ground is provided to the tail lamp relay coil through the light switch.
- Battery voltage from Fuse 9 and Fuse 14 is then provided to the illumination lamps through the closed contacts of the tail lamp relay.
- Ground is provided to the illumination lamps through the rheostat. The rheostat controls brightness of the illumination lamps.

### Rheostat Operation
- The rheostat (M30) is in series with the ground path of all illumination lamps.
- Rotating the rheostat varies resistance in the ground circuit, controlling lamp brightness.
- Maximum brightness occurs when the rheostat is at minimum resistance (fully clockwise).

### Tail Lamp / Marker Lamp Operation
- The tail lamps (rear combination lamps), front side marker lamps, and license lamps are powered through the tail lamp relay contacts.
- These lamps are NOT dimmer-controlled -- they receive full voltage when the tail lamp relay is energized.
- Only the interior illumination lamps (cluster, switches, etc.) are controlled by the rheostat.

### Air Bag System (SRS) -- Pages SD-196 to SD-197
- Pages 196-197 in this range cover the Air Bag System (SRS), which is a separate system.
- The SRS section includes the SRS control module, driver/passenger air bags, clock spring, seat belt pre-tensioners, and data link connector.
- These pages are not part of the illumination circuit.
