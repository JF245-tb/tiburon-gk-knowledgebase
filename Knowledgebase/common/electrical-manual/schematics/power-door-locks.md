---
source: SD.pdf
chapter: SD
section: SD-124 to SD-127
pages: 124-127
title: Power Door Locks
---

# Power Door Locks

**SD-124 -- Power Door Locks (1) Schematic (LHD)**
**SD-125 -- Power Door Locks (2) Schematic (RHD)**
**SD-126 -- Component Location Index**
**SD-127 -- Memo (blank)**

<!-- Figure: Power door lock actuators, key switch, BCM lock/unlock relay control, LHD variant, source: SD.pdf page 124 -->
<!-- Figure: Power door lock actuators, key switch, BCM lock/unlock relay control, RHD variant, source: SD.pdf page 125 -->

---

## Component Table (LHD -- SD-124)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 14 (HOT AT ALL TIMES) | -- | -- | R | 0.5S |
| Fuse 16 (HOT in ACC or ON) | -- | -- | -- | -- |
| BCM lock relay (internal) | coil | -- | -- | -- |
| BCM unlock relay (internal) | coil | -- | -- | -- |
| BCM lock relay (internal) | contact | -- | G/R | 0.5S |
| BCM unlock relay (internal) | contact | -- | G/B | 0.5S |
| Key switch -- driver door (D09) | lock signal | -- | G/R | 0.5S |
| Key switch -- driver door (D09) | unlock signal | -- | G/B | 0.5S |
| Key switch -- driver door (D09) | ground | -- | B | -- |
| Door lock actuator -- driver (D09) | lock (+) | -- | G/R | 0.85S |
| Door lock actuator -- driver (D09) | unlock (+) | -- | G/B | 0.85S |
| Door lock actuator -- driver (D09) | ground | -- | B | 0.85S |
| Door lock actuator -- left (D09) | lock | -- | G/R | 0.85S |
| Door lock actuator -- left (D09) | unlock | -- | G/B | 0.85S |
| Door lock actuator -- right (D10) | lock | -- | G/R | 0.85S |
| Door lock actuator -- right (D10) | unlock | -- | G/B | 0.85S |
| Door lock actuator -- right (D10) | ground | -- | B | 0.85S |
| BCM-EF | -- | -- | -- | -- |
| BCM-FF | -- | -- | -- | -- |
| BCM-EP | -- | -- | -- | -- |
| BCM-LR | -- | -- | -- | -- |
| Joint connector (M45) | -- | -- | -- | -- |

---

## Circuit Paths (LHD)

### Lock Relay Power Supply
```
Battery (+) -> Fuse 14 (HOT AT ALL TIMES)
  -> [R, 0.5S] -> BCM-FF
  -> BCM internal lock relay (contact 30)
  -> [G/R, 0.5S] -> BCM-EF
  -> [G/R, 0.85S] -> MD01 connector
  -> [G/R, 0.85S] -> Driver door lock actuator D09 (lock)
  -> [G/R, 0.85S] -> MD02 connector
  -> [G/R, 0.85S] -> Left door lock actuator (lock)
  -> [G/R, 0.85S] -> MD03 connector
  -> [G/R, 0.85S] -> Right door lock actuator D10 (lock)
```

### Unlock Relay Power Supply
```
Battery (+) -> Fuse 14 (HOT AT ALL TIMES)
  -> [R, 0.5S] -> BCM-FF
  -> BCM internal unlock relay (contact 30)
  -> [G/B, 0.5S] -> BCM-EF
  -> [G/B, 0.85S] -> MD01 connector
  -> [G/B, 0.85S] -> Driver door lock actuator D09 (unlock)
  -> [G/B, 0.85S] -> MD02 connector
  -> [G/B, 0.85S] -> Left door lock actuator (unlock)
  -> [G/B, 0.85S] -> MD03 connector
  -> [G/B, 0.85S] -> Right door lock actuator D10 (unlock)
```

### Key Switch -- Lock Signal to BCM
```
Key switch D09 (turned to LOCK)
  -> [G/R, 0.5S] -> MD01 connector
  -> [G/R, 0.5S] -> BCM-EF
  -> BCM detects lock request -> energizes lock relay
  -> All actuators receive lock pulse
```

### Key Switch -- Unlock Signal to BCM
```
Key switch D09 (turned to UNLOCK)
  -> [G/B, 0.5S] -> MD01 connector
  -> [G/B, 0.5S] -> BCM-EF
  -> BCM detects unlock request -> energizes unlock relay
  -> All actuators receive unlock pulse
```

### Door Lock Actuator Grounds
```
Driver door lock actuator D09 -> [B, 0.85S] -> MD01 -> GND (G01)
Left door lock actuator -> [B, 0.85S] -> MD02 -> GND (G02)
Right door lock actuator D10 -> [B, 0.85S] -> MD03 -> Joint connector M45 -> GND (G11)
```

### Hatch Door Lock
```
BCM-LR -> [G/R, 0.85S] -> MD04 connector
  -> [G/R, 0.85S] -> Hatch door lock actuator (lock)
BCM-LR -> [G/B, 0.85S] -> MD04 connector
  -> [G/B, 0.85S] -> Hatch door lock actuator (unlock)
Hatch door lock actuator -> [B, 0.85S] -> GND (G12)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G01 | Under dash, driver side | Driver door lock actuator ground | CL-32 |
| G02 | Under dash, passenger side | Left door lock actuator ground | CL-32 |
| G10 | Body ground | Door lock ground | CL-32 |
| G11 | Rear body | Right door / hatch lock ground | CL-33 |
| G12 | Rear body | Hatch lock actuator ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-EF | BCM door lock connector | CL-4 |
| BCM-FF | BCM fuse/relay connector | CL-8 |
| BCM-LR | BCM rear connector | CL-8 |
| MD01 | Driver door connector | CL-8 |
| MD02 | Left door connector | CL-8 |
| MD03 | Right door connector | CL-8 |
| MD04 | Hatch door connector | CL-8 |

---

## Component Location Index (SD-126)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| D09 | Left door lock actuator | CL-30 |
| D10 | Right door lock actuator | CL-30 |
| M45 | Joint connector | CL-4 |

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-FF | BCM connector | CL-4 |
| BCM-EF | BCM connector | CL-8 |
| MD01 | Door connector | CL-8 |
| MD02 | Door connector | CL-8 |
| MD03 | Door connector | CL-8 |
| MD04 | Door connector | CL-8 |

| Ground ID | Location Page |
|-----------|---------------|
| G01 | CL-32 |
| G02 | CL-32 |
| G10 | CL-32 |
| G11 | CL-33 |
| G12 | CL-33 |

---

## Notes

- Battery voltage is supplied at all times to the door lock relays and unlock relay. When locking the vehicle by using the door unlock switch in the left power window switch, the door unlock switch will provide a ground to the lock relay and the doors lock. When the door lock knob is pulled, the door lock switch will provide a ground to the unlock relay and the doors unlock.
- The polarity of the voltage applied to the lock actuators is reversed to lock vs. unlock the doors.
- The body control module also has an input from the ignition key switch. This input prevents the doors from accidentally being locked when exiting the vehicle with the ignition off and the key left in the ignition switch.
- The LHD (SD-124) and RHD (SD-125) schematics are functionally identical; differences are in driver/passenger side connector routing only.
- Page SD-127 is a blank memo page.
