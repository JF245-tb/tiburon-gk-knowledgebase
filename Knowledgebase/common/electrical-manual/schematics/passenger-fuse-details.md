---
source: SD.pdf
chapter: SD
section: SD-18 to SD-29
pages: 18-29
title: Passenger Compartment Fuse Details
---

# Passenger Compartment Fuse Details

**SD-18 -- Passenger Compartment Fuse Details (1) — Fuse 11, Fuse 12, Fuse 13**
**SD-19 -- Passenger Compartment Fuse Details (2) — Fuse 9, Fuse 20, Fuse 14**
**SD-20 -- Passenger Compartment Fuse Details (3) — Fuse 3, Fuse 15**
**SD-21 -- Passenger Compartment Fuse Details (4) — Fuse 1, Fuse 19, Fuse 8, Fuse 7**
**SD-22 -- Passenger Compartment Fuse Details (5) — Fuse 18**
**SD-23 -- Passenger Compartment Fuse Details (6) — Fuse 10, Fuse 11, Fuse 27**
**SD-24 -- Passenger Compartment Fuse Details (7) — Fuse 4, Fuse 12, Fuse 5, Fuse 16**
**SD-25 -- Passenger Compartment Fuse Details (8) — Fuse 14, Fuse 7**
**SD-26 -- Passenger Compartment Fuse Details (9) — Fuse 18, Fuse 21**
**SD-27 -- Passenger Compartment Fuse Details (10) — Fuse 16, Fuse 14**
**SD-28 -- Passenger Compartment Fuse Details (11) — Fuse 6**
**SD-29 -- Memo (blank)**

---

## Fuse Assignment Summary

All fuses are in the passenger compartment fuse/relay box (BCM box). The BCM box is behind the driver-side lower dash panel.

### Hot At All Times (Battery Direct)

| Fuse | Rating | Color | Circuits Fed |
|------|--------|-------|--------------|
| Fuse 4 | 15A | -- | Horn relay, left/right outside mirror folding motor |
| Fuse 7 | 10A | -- | Turn signal / hazard relay, rear defogger switch |
| Fuse 11 | 10A | -- | Interior lamp, trunk lamp, ignition key illumination |
| Fuse 12 | 10A | -- | BCM (body control module), hazard switch |
| Fuse 13 | 10A | -- | Burglar alarm horn relay |
| Fuse 16 | 15A | -- | Tail lamps, license lamp, parking lamps, side marker lamps |

### Hot in ON or START (IGN)

| Fuse | Rating | Color | Circuits Fed |
|------|--------|-------|--------------|
| Fuse 1 | 10A | -- | Driver power window switch |
| Fuse 3 | 10A | -- | Combination meter (instrument cluster), ignition coil relay |
| Fuse 5 | 15A | -- | Rear window defroster relay |
| Fuse 6 | 10A | -- | BCM (illumination), instrument cluster, tail lamp relay |
| Fuse 8 | 15A | -- | Stop lamp switch, ESC module |
| Fuse 9 | 10A | -- | BCM (front wiper), washer relay |
| Fuse 10 | 10A | -- | Intermittent wiper relay, front wiper |
| Fuse 14 | 10A | -- | Head lamp relay (low/high), DRL module |
| Fuse 15 | 10A | -- | Combination meter, ETC system |
| Fuse 18 | 20A | -- | Power window motor (passenger), sunroof relay |
| Fuse 19 | 15A | -- | Door lock relay, door lock actuators |
| Fuse 20 | 15A | -- | Front wiper motor relay |
| Fuse 21 | 10A | -- | Data link connector, multipurpose connector, door courtesy lamps |
| Fuse 27 | 10A | -- | Cigarette lighter |

---

## SD-18 — Sheet 1: Fuse 11, Fuse 12, Fuse 13

### Fuse 11 (10A, B+ at all times)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-IM | -- | -- | R | 0.85S |
| Interior lamp control module | -- | -- | R | 0.85S |
| BCM-CC | -- | -- | R | 0.85S |
| Trunk lamp | -- | -- | R | 0.85S |
| Ignition key illumination | -- | -- | R | 0.85S |

```
Fuse 11 → [R, 0.85S] → BCM-IM
Fuse 11 → [R, 0.85S] → BCM-CC
```

### Fuse 12 (10A, B+ at all times)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-MR | -- | -- | R | 0.85S |
| Hazard switch (M13) | -- | -- | R | 0.85S |

```
Fuse 12 → [R, 0.85S] → BCM-MR
Fuse 12 → [R, 0.85S] → Hazard switch M13
```

### Fuse 13 (10A, B+ at all times)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Burglar alarm horn relay (M39) | contact 30 | -- | R | 2.0W |

```
Fuse 13 → [R, 2.0W] → Burglar alarm horn relay M39 (contact 30)
  → See Burglar Alarm Horn System (SD-112)
```

### Loads from Fuse 13 via BCM

| Load | Wire Color | Wire Size |
|------|-----------|-----------|
| Rear air control module | -- | 0.85S |
| HVAC control module (with A/C) | -- | 0.85S |
| Indoor mirror (auto) | -- | 0.85S |
| Hazard switch | -- | 0.85S |

---

## SD-19 — Sheet 2: Fuse 9, Fuse 20, Fuse 14

### Fuse 9 (10A, IGN)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-FF | -- | -- | R/Y | 0.85S |
| Washer relay | -- | -- | R/Y | 0.85S |

```
Fuse 9 → [R/Y, 0.85S] → BCM-FF (front wiper control)
Fuse 9 → [R/Y, 0.85S] → Washer relay
```

### Fuse 20 (15A, IGN)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Front wiper motor relay | -- | -- | R/Y | 2.0W |
| Headlamp washer relay | -- | -- | -- | -- |

```
Fuse 20 → [R/Y, 2.0W] → Front wiper motor relay
  → Front wiper motor
```

### Fuse 14 (10A, IGN)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-CE | -- | -- | R/Y | 1.25Y |
| BCM-KM | -- | -- | R/Y | 0.85S |
| DRL control module | -- | -- | R/Y | -- |

```
Fuse 14 → [R/Y] → BCM-CE
Fuse 14 → [R/Y] → BCM-KM
  → Head lamp relay coil circuits
  → DRL control module
```

### Loads from Fuse 20 (via joint connector)

| Load | Wire Color | Wire Size |
|------|-----------|-----------|
| Rear wiper motor (if equipped) | -- | -- |
| Headlamp washer motor (if equipped) | -- | -- |

---

## SD-20 — Sheet 3: Fuse 3, Fuse 15

### Fuse 3 (10A, IGN)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-KM | -- | -- | R/Y | 0.85S |
| BCM-MR | -- | -- | R/Y | 0.85S |
| BCM-CE | -- | -- | R/Y | 0.85S |
| Combination meter (instrument cluster) | -- | -- | R/Y | 0.85S |
| Ignition coil relay | -- | -- | R/Y | -- |

```
Fuse 3 → [R/Y, 0.85S] → BCM-KM
Fuse 3 → [R/Y, 0.85S] → BCM-MR → Ignition coil relay
Fuse 3 → [R/Y, 0.85S] → BCM-CE
```

### Fuse 15 (10A, IGN)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Combination meter (instrument cluster) | -- | -- | R/Y | 0.5S |
| BCM-JM | -- | -- | R/Y | 0.85S |
| ETC (electronic throttle control) system | -- | -- | -- | -- |

```
Fuse 15 → [R/Y] → BCM-JM
  → Combination meter / instrument cluster
  → ETC system relay
```

### Loads from Fuse 3/15

| Load | Connector | Wire Color | Wire Size |
|------|-----------|-----------|-----------|
| Transaxle range switch indicator | C088 | R/Y | 0.85S |
| Shift-lock control actuator | -- | R/Y | 0.85S |
| Passenger air bag indicator | -- | R/Y | 0.85S |
| Instrument cluster | MR10-1 | R/Y | 0.5S |
| ETC system | EP1-2 | R/Y | 0.5S |
| ECM | ES2-2 | R/Y | -- |

---

## SD-21 — Sheet 4: Fuse 1, Fuse 19, Fuse 8, Fuse 7

### Fuse 1 (10A, IGN)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-A1 | -- | 1 | R/Y | 0.85S |
| BCM-CE-1 | -- | -- | R/Y | -- |
| Driver power window switch | -- | -- | R/Y | 1.25Y |

```
Fuse 1 → [R/Y, 0.85S] → BCM-A1 pin 1
  → [R/Y, 1.25Y] → Driver power window switch
```

### Fuse 19 (15A, IGN)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-MR | -- | -- | R/Y | -- |
| Door lock relay | -- | -- | R/Y | 1.25Y |

```
Fuse 19 → [R/Y] → BCM-MR
  → Door lock relay → Door lock actuators
```

### Fuse 8 (15A, IGN)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-KM | -- | -- | R/Y | 1.25Y |
| Stop lamp switch | -- | -- | G/R | 1.25Y |
| ESC control module | -- | -- | -- | -- |
| MC103 | -- | -- | -- | -- |

```
Fuse 8 → [R/Y, 1.25Y] → BCM-KM → MC103
  → Stop lamp switch → [G/R, 1.25Y] → Stop lamps
```

### Fuse 7 (10A, B+ at all times)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-MR1 | -- | -- | R | 1.25Y |
| Turn signal / hazard relay | -- | -- | R | -- |

```
Fuse 7 → [R, 1.25Y] → BCM-MR1
  → Hazard / turn signal relay (solid-state)
  → See Turn and Hazard Lamps (SD-172)
```

### Loads from Fuse 8

| Load | Wire Color | Wire Size |
|------|-----------|-----------|
| Driver air bag | R/Y | 1.25Y |
| Passenger air bag | R/Y | 1.25Y |
| Ignition switch (coil position) | R/Y | -- |
| Instrument cluster (IG1) | R/Y | 0.5S |
| Electronic control module | R/Y | 0.85S |

---

## SD-22 — Sheet 5: Fuse 18

### Fuse 18 (20A, IGN)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-MR | -- | -- | R/Y | 0.85S |
| Passenger power window motor | -- | -- | -- | 0.85S |
| Sunroof relay | -- | -- | -- | 0.85S |

```
Fuse 18 → [R/Y, 0.85S] → BCM-MR
  → Passenger power window motor (up/down via relay)
  → Sunroof motor relay
```

### Loads from Fuse 18

| Load | Connector | Wire Color | Wire Size |
|------|-----------|-----------|-----------|
| Power window motor (passenger) | -- | -- | 0.85S |
| Sunroof relay / motor | -- | -- | 0.85S |
| Door courtesy switches | -- | -- | -- |
| Illumination control (via BCM) | -- | -- | 0.85S |

---

## SD-23 — Sheet 6: Fuse 10, Fuse 11 (detail), Fuse 27

### Fuse 10 (10A, IGN)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-MR | -- | -- | R/Y | 0.85S |
| BCM-KM | -- | -- | -- | -- |
| Intermittent wiper relay | -- | -- | -- | -- |

```
Fuse 10 → BCM-MR → Intermittent wiper relay → Front wiper motor (INT mode)
```

### Fuse 27 (10A, IGN)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-FF | -- | -- | R/Y | 0.85S |
| Cigarette lighter | -- | -- | R/Y | -- |

```
Fuse 27 → [R/Y] → BCM-FF → Cigarette lighter socket
```

### Loads from Fuse 10/27

| Load | Wire Color | Wire Size |
|------|-----------|-----------|
| Wiper delay relay | -- | 1.25Y |
| Intermittent wiper control | -- | 0.85S |
| Cigarette lighter | -- | -- |
| Sequential clock | -- | 0.85S |
| Rheostat (illumination dimmer) | -- | 0.85S |
| Cartridge heater | -- | -- |

---

## SD-24 — Sheet 7: Fuse 4, Fuse 12 (detail), Fuse 5, Fuse 16

### Fuse 4 (15A, B+ at all times)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-CC | -- | -- | R | 2.0W |
| BCM-FF | -- | -- | R | -- |
| Horn relay (E45) | coil/contact | -- | R | 3.0W |

```
Fuse 4 → [R, 3.0W] → Horn relay E45 → See Horns (SD-158)
Fuse 4 → [R, 2.0W] → BCM-CC
```

### Fuse 12 (detail) — Loads

| Load | Connector | Wire Color | Wire Size |
|------|-----------|-----------|-----------|
| Left front turn signal lamp | -- | G/B | 0.85S |
| Left rear side marker lamp | -- | G/B | 0.85S |
| Right front turn signal lamp | -- | G/W | 0.85S |
| Right rear side marker lamp | -- | G/W | 0.85S |

### Fuse 5 (15A, IGN)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Rear window defroster relay | -- | -- | R/Y | 2.0W |
| Left outside mirror (folding motor) | M01 | -- | -- | 1.25Y |
| Right outside mirror (folding motor) | -- | -- | -- | 1.25Y |

```
Fuse 5 → [R/Y, 2.0W] → Rear window defroster relay
  → Rear defogger grid → GND
```

### Fuse 16 (15A, B+ at all times)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-MR1 | -- | -- | R | 1.25Y |
| BCM-FF | -- | -- | R | -- |
| Tail lamp relay | -- | -- | -- | -- |

```
Fuse 16 → [R, 1.25Y] → BCM-MR1
  → Tail lamp relay → Tail lamps, license lamp, side markers
```

---

## SD-25 — Sheet 8: Fuse 14 (detail), Fuse 7 (detail)

### Fuse 14 (detail) — Additional Loads

| Load | Connector | Wire Color | Wire Size |
|------|-----------|-----------|-----------|
| Left head lamp (low beam) | -- | W | 1.25B |
| Left head lamp (high beam) | -- | R/W | 1.25B |
| Right head lamp (low beam) | -- | W | 1.25B |
| Right head lamp (high beam) | -- | R/W | 1.25B |

```
Fuse 14 → Head lamp relay LOW → [W, 1.25B] → Left/Right head lamp low beam
Fuse 14 → Head lamp relay HIGH → [R/W, 1.25B] → Left/Right head lamp high beam
  → See Head Lamps (SD-160)
```

### Fuse 7 (detail) — Additional Loads via Power Connector

| Load | Wire Color | Wire Size |
|------|-----------|-----------|
| Front turn signal lamps | G/B, G/W | 0.85S |
| Rear combination lamp (turn) | G/B, G/W | 0.85S |
| Side repeater lamps | G/B, G/W | 0.5S |
| Instrument cluster turn indicators | G/B, G/W | 0.5S |

---

## SD-26 — Sheet 9: Fuse 18 (detail), Fuse 21

### Fuse 18 (detail) — Additional Loads

| Load | Connector | Wire Color | Wire Size |
|------|-----------|-----------|-----------|
| DATA LINK connector (OBD2) | -- | R/Y | 0.5S |
| Audio system | -- | -- | -- |
| Multipurpose connector | -- | -- | -- |

### Fuse 21 (10A, IGN)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-M | -- | -- | R/Y | 0.5S |
| BCM-KM | -- | -- | -- | -- |
| BCM-MR | -- | -- | -- | -- |
| BCM-FF | -- | -- | R/Y | -- |
| Multipurpose connector | -- | -- | R/Y | 0.5S |
| Door courtesy lamps | -- | -- | -- | -- |
| Luggage lamp | -- | -- | -- | -- |
| Dome lamp | -- | -- | -- | -- |
| Vanity mirror lamp | -- | -- | -- | -- |
| Map lamp | -- | -- | -- | -- |

```
Fuse 21 → [R/Y, 0.5S] → BCM-M
  → Data link connector (OBD2 pin 7 power)
  → Multipurpose connector
  → Door courtesy lamps
  → Audio control module
  → Luggage lamp
  → Dome lamp relay
```

---

## SD-27 — Sheet 10: Fuse 16 (detail), Fuse 14 (tail)

### Fuse 16 — Tail / Parking / License Lamp Details

| Load | Connector | Wire Color | Wire Size |
|------|-----------|-----------|-----------|
| Left tail lamp | E07 | G/R | 0.5S |
| Left rear side marker | -- | G/R | 0.85S |
| Right tail lamp | -- | G/R | 0.5S |
| Right rear side marker | -- | G/R | 0.85S |
| License lamp (left) | -- | G/O | 0.5S |
| License lamp (right) | -- | G/O | 0.5S |
| Left rear parking lamp | -- | G/R | 0.85S |
| Right rear parking lamp | -- | G/R | 0.85S |
| DRL (daytime running lights) | -- | -- | -- |
| Parking brake warning switch | -- | -- | -- |

```
Fuse 16 → Tail lamp relay → [G/R, 0.85S] → Left tail lamp
  → [G/R, 0.85S] → Right tail lamp
  → [G/O, 0.5S] → License lamps (left + right)
  → [G/R, 0.5S] → Left rear side marker
  → [G/R, 0.5S] → Right rear side marker
```

### Joint Connector — Rear Lamp Distribution

| Output | Wire Color | Destination |
|--------|-----------|-------------|
| G/R | 0.85S | Left rear parking lamp |
| G/R | 0.85S | Right rear parking lamp |
| G/O | 0.5S | Left license lamp |
| G/O | 0.5S | Right license lamp |

---

## SD-28 — Sheet 11: Fuse 6

### Fuse 6 (10A, IGN)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| BCM-N | -- | -- | R/Y | 0.85S |
| BCM-FF | -- | -- | R/Y | -- |
| BCM-CE | -- | -- | R/Y | -- |
| BCM-JM | -- | -- | R/Y | -- |
| Instrument cluster | -- | -- | R/Y | 0.5S |
| Tail lamp relay (coil) | -- | -- | R/Y | 0.85S |

```
Fuse 6 → [R/Y, 0.85S] → BCM-N
Fuse 6 → [R/Y, 0.85S] → BCM-FF
Fuse 6 → [R/Y] → BCM-CE → BCM-JM
  → Instrument cluster (illumination feed)
  → Tail lamp relay coil
```

### Loads from Fuse 6

| Load | Connector | Wire Color | Wire Size |
|------|-----------|-----------|-----------|
| Rheostat (illumination dimmer) | -- | -- | 0.5S |
| BCM illumination output | -- | -- | 0.85S |
| Tail lamp relay coil | -- | R/Y | 0.85S |
| Instrument cluster (IG2) | -- | R/Y | 0.5S |
| Cigarette lighter illumination | E37 | -- | 0.5S |
| Audio illumination | E01 | -- | 0.5S |

---

## Notes

- All fuses are located in the passenger compartment fuse/relay box (integrated with BCM).
- "B+ at all times" fuses are powered directly from battery through the fusible links, regardless of ignition switch position.
- "IGN" fuses are powered only when the ignition switch is in ON or START position.
- Many circuits pass through BCM connectors (BCM-CC, BCM-CE, BCM-FF, BCM-KM, BCM-LM, BCM-MR, BCM-JM) even though the BCM does not actively control all of them -- the BCM box serves as a wiring junction for the passenger fuse panel.
- For the 2.7L V6 build, all fuse assignments and ratings are the same as the 2.0L.
- Cross-references to other schematic sections are noted inline (e.g., Horns SD-158, Head Lamps SD-160, Turn/Hazard SD-172, Burglar Alarm SD-112).
