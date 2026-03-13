---
source: SD.pdf
chapter: SD
section: SD-30 to SD-43
pages: 30-43
title: Ground Distribution
---

# Ground Distribution

**SD-30 -- Ground Distribution (1) -- G01 (Floor.1)**
**SD-31 -- Ground Distribution (2) -- G04 (Floor.2), G05 (Engine.R)**
**SD-32 -- Ground Distribution (3) -- G06 (Floor.3), G07 (T/Gate)**
**SD-33 -- Ground Distribution (4) -- G06 (T/Gate.1), G08 (RR HTD), G09 (Air Bag)**
**SD-34 -- Ground Distribution (5) -- G11 (Main.1)**
**SD-35 -- Ground Distribution (6) -- G11 (Main.1) continued**
**SD-36 -- Ground Distribution (7) -- G12 (Main.2)**
**SD-37 -- Ground Distribution (8) -- G13 (Main.3), G14 (Engine.2), G17 (A/C)**
**SD-38 -- Ground Distribution (9) -- G16 (Engine.1)**
**SD-39 -- Ground Distribution (10) -- G20/G23 (Control)**
**SD-40 -- Ground Distribution (11) -- G18 (TCM), G19 (ECM) [2.0L]**
**SD-41 -- Ground Distribution (12) -- G20 (TCM), G24 (Engine) [2.7L]**
**SD-42 -- Ground Distribution (13) -- G25 (Control), G26 (ECM) [1.6L]**
**SD-43 -- MEMO (blank page)**

---

## Ground Point Summary

| Ground ID | Location | Page |
|-----------|----------|------|
| G01 | Floor.1 (driver side floor) | SD-30 |
| G04 | Floor.2 (passenger side floor) | SD-31 |
| G05 | Engine.R (right side engine bay) | SD-31 |
| G06 | Floor.3 (rear floor) | SD-32 |
| G07 | T/Gate (tailgate) | SD-32 |
| G06 | T/Gate.1 (tailgate area) | SD-33 |
| G08 | RR HTD (rear heated) | SD-33 |
| G09 | Air Bag | SD-33 |
| G11 | Main.1 (main body ground) | SD-34, SD-35 |
| G12 | Main.2 (main body ground) | SD-36 |
| G13 | Main.3 (engine compartment) | SD-37 |
| G14 | Engine.2 | SD-37 |
| G16 | Engine.1 (engine compartment) | SD-38 |
| G17 | A/C | SD-37 |
| G18 | TCM (2.0L) | SD-40 |
| G19 | ECM (2.0L) | SD-40 |
| G20 | Control (2.0L) / TCM (2.7L) | SD-39, SD-41 |
| G23 | Control (2.7L) | SD-39 |
| G24 | Engine (2.7L) | SD-41 |
| G25 | Control (1.6L) | SD-42 |
| G26 | ECM (1.6L) | SD-42 |

---

## Ground Distribution (1) -- G01 (Floor.1) -- SD-30

### Components Grounded at G01

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| Left door lock actuator | D09 (LHD) / D09-1 (RHD) | 3 | 0.5B |
| Seat belt switch | M48 | 2 | 0.5B |
| Left door switch | M53 | 3 | 0.3B |
| Left front seat warmer | M47 | 2 | 1.25B |
| Left outside mirror & mirror folding motor | D06 | 2 | 0.5B |
| Left power window switch | D05 | 7 | 2.0B |
| Outside mirror switch | D04 | 8 | 0.5B |

### Circuit Path
```
Left door lock actuator (D09, pin 3) → [B, 0.5B] ─┐
Seat belt switch (M48, pin 2) → [B, 0.5B] ────────┤
Left door switch (M53, pin 3) → [B, 0.3B] ────────┤
Left front seat warmer (M47, pin 2) → [B, 1.25B] ─┤
Left outside mirror (D06, pin 2) → [B, 0.5B] ─────┤
Left power window switch (D05, pin 7) → [B, 2.0B] ┤
Outside mirror switch (D04, pin 8) → [B, 0.5B] ───┘
  → [B, 2.0B] → MD02 (pin 11)
  → [B, 2.0B] → MD01 (pin 10)
  → [B, 0.5B] → G01 (Floor.1)
```

---

## Ground Distribution (2) -- G04 (Floor.2), G05 (Engine.R) -- SD-31

### Components Grounded at G04 (Floor.2)

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| License plate lamp | M60 | 1 | 0.85B |
| Right front fog lamp | M64 | 6 | 1.0B |
| Right power window switch | -- | -- | 0.85B |
| Right door lock actuator | -- | -- | 0.85B |
| Right side repeater lamp | D16 (LHD) | -- | 0.85B |
| Right front speaker | S716 | -- | 1.0B |
| Display panel & cluster | -- | -- | 0.85B |

### Components Grounded at G05 (Engine.R)

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| Right headlamp assembly | -- | -- | 0.85B |

### Circuit Path
```
Multiple components → Joint connector (M34, M36) →
  → [B] → G04 (Floor.2)
  → [B] → G05 (Engine.R)
```

---

## Ground Distribution (3) -- G06 (Floor.3), G07 (T/Gate) -- SD-32

### Components Grounded at G06 (Floor.3)

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| Left rear combination lamp | M82 | 6 | 0.85B |
| Rear intermittent wiper motor | M76 | 6 | 0.85B |

### Components Grounded at G07 (T/Gate)

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| AMP #1 (HIGH) | M63-1 | 7 | 0.85B |
| Rear window motor | MR01 | 2 | 3.0B |
| Rear right assembly | RR01 | 2 | 3.0B |

### Circuit Path
```
Left rear combination lamp (M82, pin 6) → [B, 0.85B] ─┐
Rear intermittent wiper motor (M76, pin 6) → [B, 0.85B] ┤
  → [B] → G06 (Floor.3)

AMP #1 (M63-1, pin 7) → [B, 0.85B] ─┐
  → [B, 3.0B] → MR01 (pin 2) ───────┤
  → [B, 3.0B] → RR01 (pin 2) ───────┘
  → G07 (T/Gate)
```

---

## Ground Distribution (4) -- G06 (T/Gate.1), G08 (RR HTD), G09 (Air Bag) -- SD-33

### Components Grounded at G06 (T/Gate.1)

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| Rear wiper motor | R13 | 4 | 0.85B |
| High mounted stop lamp | R12 | 1 | 0.5B |
| High mounted stop lamp | R14 | 2 | 0.85B |
| Trunk lid solenoid | R01 | 3 | 0.5B |
| Luggage lamp switch | R17 | 2 | 0.5B |
| Tail gate unlock switch | R03 | 2 | 0.5B |

### Components Grounded at G08 (RR HTD)

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| Rear window defogger | R06 | 1 | 3.0B |

### Components Grounded at G09 (Air Bag)

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| SRS control module | I14 | 20 | 0.5B |

### Circuit Path
```
Rear wiper motor (R13, pin 4) → [B, 0.85B] ──────┐
High mounted stop lamp (R12, pin 1) → [B, 0.5B] ─┤
High mounted stop lamp (R14, pin 2) → [B, 0.85B] ┤  (Spoiler / P/TRAY variants)
Trunk lid solenoid (R01, pin 3) → [B, 0.5B] ─────┤
Luggage lamp switch (R17, pin 2) → [B, 0.5B] ────┤
Tail gate unlock switch (R03, pin 2) → [B, 0.5B] ┘
  → G06 (T/Gate.1)

Rear window defogger (R06, pin 1) → [B, 3.0B] → G08 (RR HTD)

SRS control module (I14, pin 20) → [B, 0.5B] → G09 (Air Bag)
```

---

## Ground Distribution (5) -- G11 (Main.1) -- SD-34

### Components Grounded at G11 (Main.1)

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| Cigarette lighter | M31 | 1 | 0.5B |
| Instrument cluster | M10-1 | 8 | 0.5B |
| Instrument cluster | M10-1 | 1 | 0.5B |
| Rheostat | M29 | 5 | 0.5B |
| BCM box | BCM-LM | 5 | 2.0B |

### Circuit Path
```
Cigarette lighter (M31, pin 1) → [B, 0.5B] ───────┐
Instrument cluster (M10-1, pin 8) → [B, 0.5B] ───┤
Instrument cluster (M10-1, pin 1) → [B, 0.5B] ───┤
Rheostat (M29, pin 5) → [B, 0.5B] ────────────────┤
BCM box (BCM-LM, pin 5) → [B, 2.0B] ─────────────┘
  → [B, 1.25B] → G11 (Main.1)
```

---

## Ground Distribution (6) -- G11 (Main.1) continued -- SD-35

### Components Grounded at G11 (Main.1) -- Upper Bus

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| Front fog lamp switch | M14 | 2 | 0.85S |
| Key reminder switch | -- | -- | 0.85S |
| Multi-purpose check connector | -- | -- | 0.85S |
| Data link connector | -- | -- | 0.85S |
| Multipurpose connector | -- | -- | 0.85S |
| Digital clock | -- | -- | 0.85S |
| Hazard switch | -- | -- | 0.85S |
| Multifunction switch | M08-S(F/C) | -- | 0.85S |

### Components Grounded at G11 (Main.1) -- Lower Bus (via M08 Joint Connector)

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| Seat warmer switch (LH) | -- | -- | 0.85S |
| Seat warmer switch (RH) | -- | -- | 0.85S |
| Auto light module | -- | -- | 0.85S |
| Headlamp leveling module | -- | -- | 0.85S |

### Circuit Path
```
Upper bus (0.85S each) → Joint connector M08 →
  → [B, 1.25B] → G11 (Main.1)

Lower bus (0.85S each) → Joint connector →
  → [B, 0.85S] → G11 (Main.1)
```

---

## Ground Distribution (7) -- G12 (Main.2) -- SD-36

### Components Grounded at G12 (Main.2)

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| BCM BCS | BCM-LR | 1 | 3.0B |
| Door warning relay | E04 | -- | 3.0B |
| Power transistor | E64 | 1 | 3.0B |
| Audio relay | M12 (AUDIO) | 5 | 3.0B |
| Blower motor | M01 | 5 | 3.0B |
| Blower fan/tastic switch | B01 | -- | 1.25B |
| Thermostatic lamp switch | M07 | 1 | 0.85S |
| Glove box lamp switch | -- | 1 | 0.85S |

### Circuit Path
```
BCM BCS (BCM-LR, pin 1) → [B, 3.0B] ──────────┐
Door warning relay (E04) → [B, 3.0B] ──────────┤
Power transistor (E64, pin 1) → [B, 3.0B] ─────┤
Audio relay (M12, pin 5) → [B, 3.0B] ──────────┤
Blower motor (M01, pin 5) → [B, 3.0B] ─────────┤
  → 10 → MM04 →
  → [B, 2.0B] → G12 (Main.2)

Blower fan switch (B01) → [B, 1.25B] ──────────┐
Thermostatic lamp switch (M07) → [B, 0.85S] ───┤
Glove box lamp switch → [B, 0.85S] ────────────┘
  → [B] → G12 (Main.2)
```

---

## Ground Distribution (8) -- G13 (Main.3), G14 (Engine.2), G17 (A/C) -- SD-37

### Components Grounded at G13 (Main.3)

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| ECM | C133-A | 17 | 0.85S |
| Fuel sender & pump | M55 | -- | 0.85S |
| Instrument cluster | M10-1 | 1 | 0.85S |
| Left cooler sensor | -- | -- | 1.25B |
| Right cooler sensor | -- | -- | 1.25B |

### Components Grounded at G14 (Engine.2) -- (2.7L labeled ZONE.2)

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| Right front combination lamp | -- | -- | 0.85S |
| Condenser fan motor | -- | -- | 0.85S |

### Components Grounded at G17 (A/C)

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| A/C control module | C210 | -- | 0.85S |

### Circuit Path
```
ECM (C133-A, pin 17) → [B, 0.85S] ────────────┐
  → 12 → MC7/40 ──────────────────────────────┤
Fuel sender (M55) → [B, 0.85S] ───────────────┤
Instrument cluster (M10-1) → [B, 0.85S] ──────┤
  → [B, 1.0B] → MM05 ────────────────────────┤
  → 7 → MM05 → [B, 0.85S] ──────────────────┤
  → 6 → EE04 ─────────────────────────────────┘
  → [B, 0.85B] → G13 (Main.3)
  → [B, 2.0B] → G14 (Engine.2 / ZONE.2)
  → [B, 1.25B] → G17 (A/C)
```

---

## Ground Distribution (9) -- G16 (Engine.1) -- SD-38

### Components Grounded at G16 (Engine.1)

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| Left front fog lamp | E14 | 2 | 1.0B |
| Front right fog lamp | E14 | -- | 1.0B |
| Left side repeater | E46 | -- | 0.85S |
| Left turn lamp | -- | -- | 0.5B |
| Horn | E47 | 1 | 0.85S |
| Front right head lamp | E17 | 1 | 0.85S |
| Left front head lamp | -- | -- | 0.85S |
| Start relay | E41 | -- | 0.85S |
| Condenser relay | -- | -- | 0.85S |
| Burglar alarm relay | -- | -- | 0.85S |

### E/R Box Components Also at G16

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| Start relay | E41 | -- | 0.85S |
| Condenser relay (E/R) | -- | -- | 0.85S |
| Burglar alarm relay (E/R) | -- | -- | 0.85S |

### Circuit Path
```
Left front fog lamp (E14, pin 2) → [B, 1.0B] ──────┐
Front right fog lamp (E14) → [B, 1.0B] ────────────┤
Left side repeater (E46) → [B, 0.85S] ─────────────┤
Left turn lamp → [B, 0.5B] ────────────────────────┤
Horn (E47, pin 1) → [B, 0.85S] ────────────────────┤
  → 4 → EE08 ──────────────────────────────────────┤
Front right head lamp (E17) → [B, 0.85S] ──────────┤
E/R box relays → [B, 0.85S / 0.85B] ──────────────┘
  → [B, 1.0B] → G16 (Engine.1)
```

---

## Ground Distribution (10) -- G20/G23 (Control) -- SD-39

### Components Grounded at G20 (2.0L) / G23 (2.7L)

| Component | Connector | Pin | Wire Size | Engine |
|-----------|-----------|-----|-----------|--------|
| Front wiper motor | C07 (2.0L) / C107 (2.7L) | 1 | 2.0B | All |
| Brake fluid level sensor | C20 (2.0L) / C120 (2.7L) | 1 | 0.5B | All |
| Cruise clutch pedal position switch | C35 (2.0L) / C135 (2.7L) | 1 | 0.5B | All |
| Vehicle speed sensor | C09 (2.0L) / C109 (2.7L) | 2 | 0.5B | All |
| Vehicle speed sensor | C10 | 1 | 0.5B | All |
| Cruise control module | C38 (2.0L) / C138 (2.7L) | 8 | 0.85B | All |

### Notes on Transmission Variants

- A/T and M/T variants share the same ground point
- Connector numbers differ by engine: 2.0L uses Cxx, 2.7L uses C1xx

### Circuit Path
```
Front wiper motor (C07/C107, pin 1) → [B, 2.0B] ──┐
Brake fluid level sensor (C20/C120, pin 1) → [B, 0.5B] ┤
Cruise clutch pedal switch (C35/C135, pin 1) → [B, 0.5B] ┤
Vehicle speed sensor (C09/C109, pin 2) → [B, 0.5B] ┤
Vehicle speed sensor (C10, pin 1) → [B, 0.5B] ────┤
Cruise control module (C38/C138, pin 8) → [B, 0.85B] ┘
  → G20 (2.0L, CONTROL) / G23 (2.7L, CONTROL)
```

---

## Ground Distribution (11) -- G18 (TCM), G19 (ECM) [2.0L] -- SD-40

### Components Grounded at G18 (TCM) -- 2.0L Only

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| TCM | C36-3 | 22 | 0.85B |
| TCM | C36-3 | 26 | 1.25B |
| TCM | C36-3 | 12 | 1.25B |
| TCM | C36-3 | 13 | 1.25B |
| TCM | C36-1 | 25 | 1.25B |

### Components Grounded at G19 (ECM) -- 2.0L Only

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| A/T control relay | C37 | 2 | 0.5B |
| ECM | C33 | 1 | 2.0B |
| ECM | C33 | 2 | 2.0B |

### Circuit Path
```
TCM (C36-3, pins 22/26/12/13) → [B, 0.85B-1.25B] ──┐
TCM (C36-1, pin 25) → [B, 1.25B] ───────────────────┘
  → G18 (TCM)

A/T control relay (C37, pin 2) → [B, 0.5B] ──┐
ECM (C33, pin 1) → [B, 2.0B] ────────────────┤
ECM (C33, pin 2) → [B, 2.0B] ────────────────┘
  → G19 (ECM)
```

---

## Ground Distribution (12) -- G20 (TCM), G24 (Engine) [2.7L] -- SD-41

### Components Grounded at G20 (TCM) -- 2.7L

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| TCM | C136-3 | 25 | 0.85B |
| TCM | C136-3 | -- | 1.25B |
| A/T control relay | -- | -- | 1.25B |

### Components Grounded at G24 (Engine) -- 2.7L

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| DCM | C136-1 | -- | 2.0B |
| ECM | C133-1 | -- | 2.0B |

### Ignition Coil Grounds

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| Ignition coil #1-#6 | C106-6 | -- | 1.25B |

### Circuit Path
```
TCM (C136-3) → [B, 0.85B-1.25B] ──────────┐
A/T control relay → [B, 1.25B] ───────────┘
  → G20 (TCM)

DCM (C136-1) → [B, 2.0B] ────────┐
ECM (C133-1) → [B, 2.0B] ────────┤
Ignition coil grounds → [B, 1.25B] ┘
  → G24 (Engine)
```

---

## Ground Distribution (13) -- G25 (Control), G26 (ECM) [1.6L] -- SD-42

### Components Grounded at G25 (Control) -- 1.6L Only

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| Front wiper motor | C207 (LHD) / C206 (RHD) | 1/5 | 2.0B |
| Camshaft position sensor | C214 | 3 | 0.5B |
| Vehicle speed sensor | C210 | 1 | 0.5B |
| Brake fluid level sensor | C220 | 1 | 0.5B |

### Components Grounded at G26 (ECM) -- 1.6L Only

| Component | Connector | Pin | Wire Size |
|-----------|-----------|-----|-----------|
| ECM | C233 | 3 | 0.5B |
| ECM | C233 | 51 | 0.5B |
| ECM | C233 | 3,3 | 0.5B |
| ECM | C233 | 61 | 0.5B |
| ECM | C233 | 80 | 0.5B |

### Circuit Path
```
Front wiper motor (C207/C206) → [B, 2.0B] ──┐
Camshaft position sensor (C214) → [B, 0.5B] ┤
Vehicle speed sensor (C210) → [B, 0.5B] ────┤
Brake fluid level sensor (C220) → [B, 0.5B] ┘
  → G25 (Control)

ECM (C233, multiple pins) → [B, 0.5B each] → G26 (ECM)
```

---

## Master Ground Location Table

| Ground ID | Location | Wire Sizes | Primary Components |
|-----------|----------|------------|--------------------|
| G01 | Floor.1 (driver side) | 0.3B-2.0B | Door locks, seat warmer, power windows, mirrors |
| G04 | Floor.2 (passenger side) | 0.85B-1.0B | License lamp, fog lamp, speakers, door locks |
| G05 | Engine.R (right engine bay) | 0.85B | Right headlamp |
| G06 | Floor.3 (rear floor) | 0.85B | Rear combination lamp, rear wiper |
| G07 | T/Gate (tailgate) | 0.85B-3.0B | AMP, rear window motor |
| G06 | T/Gate.1 | 0.5B-0.85B | Rear wiper, stop lamp, trunk solenoid |
| G08 | RR HTD | 3.0B | Rear window defogger |
| G09 | Air Bag | 0.5B | SRS control module |
| G11 | Main.1 (instrument area) | 0.5B-2.0B | Cigarette lighter, cluster, rheostat, BCM, fog switch, hazard, clock |
| G12 | Main.2 | 0.85S-3.0B | BCM, door warning, blower, audio, power transistor |
| G13 | Main.3 (engine compartment) | 0.85S-1.25B | ECM, fuel sender, cluster, cooler sensors |
| G14 | Engine.2 (ZONE.2) | 0.85S | Front combination lamp, condenser fan |
| G16 | Engine.1 | 0.5B-1.0B | Fog lamps, horn, headlamps, E/R relays |
| G17 | A/C | 0.85S-1.25B | A/C control module |
| G18 | TCM (2.0L) | 0.85B-1.25B | TCM (C36-3, C36-1) |
| G19 | ECM (2.0L) | 0.5B-2.0B | ECM (C33), A/T control relay |
| G20 | Control (2.0L) / TCM (2.7L) | 0.5B-2.0B | Wiper, VSS, brake fluid, cruise |
| G23 | Control (2.7L) | 0.5B-2.0B | Same as G20 for 2.7L |
| G24 | Engine (2.7L) | 1.25B-2.0B | ECM (C133-1), ignition coils |
| G25 | Control (1.6L) | 0.5B-2.0B | Wiper, CMP, VSS, brake fluid |
| G26 | ECM (1.6L) | 0.5B | ECM (C233) |

---

## Notes

- All ground wires use **B** (black) color.
- Wire sizes range from 0.3B (small signal grounds) to 20B (battery ground cable).
- Ground distribution is split by vehicle area: driver floor (G01), passenger floor (G04), rear floor/tailgate (G06/G07), instrument panel (G11/G12), engine compartment (G13/G14/G16), and dedicated ECM/TCM grounds per engine variant.
- The 2.7L V6 uses G23 (Control) and G24 (Engine) for ECM/ignition grounds.
- The 2.0L uses G18 (TCM), G19 (ECM), and G20 (Control).
- The 1.6L uses G25 (Control) and G26 (ECM).
- SD-43 is a blank MEMO page with no content.
