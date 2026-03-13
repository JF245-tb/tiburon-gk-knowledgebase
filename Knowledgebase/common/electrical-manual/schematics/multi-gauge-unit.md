---
source: SD.pdf
chapter: SD
section: SD-122 to SD-123
pages: 122-123
title: Multi Gauge Unit
---

# Multi Gauge Unit

**SD-122 -- Multi Gauge Unit (1) Schematic**
**SD-123 -- Component Location Index**

<!-- Figure: Multi gauge unit with torque, fuel consumption, and voltage displays, ECM/TCM/VSS signal inputs, source: SD.pdf page 122 -->

---

## Component Table (SD-122)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 18 (HOT AT ALL TIMES) | -- | -- | R | 0.5S |
| Fuse 19 (HOT in ON or START) | -- | -- | G/L | 0.5S |
| Fuse 16 (HOT in ACC or ON) | -- | -- | R/B | 0.85S |
| BCM-KM | -- | -- | -- | -- |
| BCM-MR | -- | -- | -- | -- |
| Multi gauge unit (M62) | B+ (constant) | -- | R | 0.5S |
| Multi gauge unit (M62) | IGN | -- | G/L | 0.5S |
| Multi gauge unit (M62) | illumination | -- | R/B | 0.5S |
| Multi gauge unit (M62) | torque signal | -- | Br/W | 0.3S |
| Multi gauge unit (M62) | fuel cons. signal | -- | Br/W | 0.3S |
| Multi gauge unit (M62) | voltage sense | -- | R | 0.5S |
| Multi gauge unit (M62) | VSS input | -- | P/B | 0.5S |
| Multi gauge unit (M62) | ground | -- | B | 0.5S |
| ECM (2.0L) (C33) | torque output | -- | Br/W | 0.3S |
| ECM (2.7L) (C133-4) | torque output | -- | Br/W | 0.3S |
| TCM (2.0L) (C36-3) | fuel cons. output | -- | Br/W | 0.3S |
| TCM (2.7L) (C36-3) | fuel cons. output | -- | Br/W | 0.3S |
| Vehicle speed sensor (2.0L) (C09) | VSS signal | -- | P/B | 0.5S |
| Vehicle speed sensor (2.7L) (C109) | VSS signal | -- | P/B | 0.5S |
| ABS control module (B37) | VSS input | -- | P/B | 0.5S |
| Instrument cluster (M10-1) | -- | -- | -- | -- |
| Joint connector (C41 / C141) | -- | -- | -- | -- |
| Joint connector (M26) | -- | -- | -- | -- |

---

## Circuit Paths

### Constant Battery Power
```
Battery (+) -> Fuse 18 (HOT AT ALL TIMES)
  -> [R, 0.5S] -> BCM-KM
  -> [R, 0.5S] -> BCM-MR
  -> [R, 0.5S] -> Multi gauge unit M62 (B+ input)
```

### Ignition Power
```
Battery (+) -> Fuse 19 (HOT in ON or START)
  -> [G/L, 0.5S] -> BCM-KM
  -> [G/L, 0.5S] -> BCM-MR
  -> [G/L, 0.5S] -> Multi gauge unit M62 (IGN input)
```

### See Illumination (Dimmer)
```
Fuse 16 (HOT in ACC or ON)
  -> [R/B, 0.85S] -> BCM-KM
  -> [R/B, 0.5S] -> Multi gauge unit M62 (illumination input)
```

### Torque Signal -- ECM to Multi Gauge Unit
```
ECM C33 (2.0L) or ECM C133-4 (2.7L) -- torque output
  -> [Br/W, 0.3S] -> Joint connector C41 (2.0L) / C141 (2.7L)
  -> [Br/W, 0.3S] -> MC101 connector
  -> [Br/W, 0.3S] -> Multi gauge unit M62 (torque signal input)
```

### Fuel Consumption Signal -- TCM to Multi Gauge Unit
```
TCM C36-3 -- instantaneous fuel consumption output
  -> [Br/W, 0.3S] -> MC101 connector
  -> [Br/W, 0.3S] -> Multi gauge unit M62 (fuel consumption signal input)
```

### Voltage Display
```
Multi gauge unit M62 (voltage sense)
  -> Internal measurement of B+ supply voltage
  -> Displays battery/charging system voltage on gauge
```

### Vehicle Speed Signal -- VSS to Multi Gauge Unit
```
Vehicle speed sensor C09 (2.0L) / C109 (2.7L)
  -> [P/B, 0.5S] -> Joint connector M26
  -> [P/B, 0.5S] -> ABS control module B37
  -> [P/B, 0.5S] -> Instrument cluster M10-1
  -> [P/B, 0.5S] -> Multi gauge unit M62 (VSS input)
```

### Ground
```
Multi gauge unit M62 (ground)
  -> [B, 0.5S] -> GND (G01)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G01 | Under dash, driver side | Multi gauge unit ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-JM | BCM junction connector | CL-6 |
| BCM-KM | BCM passenger compartment connector | CL-8 |
| MC01 | Multifunction switch connector | CL-8 |
| MC101 | Connector | CL-8 |
| MC201 | Connector | CL-8 |
| MM02 | Connector | CL-9 |

---

## Component Location Index (SD-123)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C09 | Vehicle speed sensor (2.0L, with A/T) | CL-18 |
| C10 | Vehicle speed sensor (2.0L, with M/T) | CL-18 |
| C33 | TCM (2.0L) | CL-01 |
| C36-3 | TCM (2.7L) | CL-20 |
| C41 | Joint connector (2.0L) | CL-21 |
| C109 | Vehicle speed sensor (2.7L) | CL-22 |
| C133-4 | ECM (2.7L) | CL-25 |
| C133-3 | ECM (2.7L) | CL-25 |
| C141 | Joint connector (2.7L) | CL-21 |
| C231 | Vehicle speed sensor (1.6L) | CL-27 |
| C233 | ECM (1.6L) | CL-08 |
| B37 | ABS control module | CL-12 |
| M10-1 | Instrument cluster | CL-2 |
| M26 | Joint connector | CL-4 |
| M62 | Multi gauge unit | CL-4 |

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-JM | BCM connector | CL-6 |
| BCM-KM | BCM connector | CL-8 |
| MC01 | Connector | CL-8 |
| MC101 | Connector | CL-8 |
| MC201 | Connector | CL-8 |
| MM02 | Connector | CL-9 |

| Ground ID | Location Page |
|-----------|---------------|
| G01 | CL-33 |

---

## Notes

- Battery voltage is supplied at all times to the multi gauge unit via Fuse 18. Fuse 16 also supplies battery voltage when the ignition switch is in ACC or ON position.
- ECM, TCM, VSS, and ignition signals are input to the multi gauge unit, and it displays torque, voltage, and instantaneous fuel consumption.
- The multi gauge unit is an optional accessory gauge pod (center console mounted).
- VSS signal is shared with the instrument cluster and ABS control module.
- Torque signal comes from the ECM; fuel consumption signal comes from the TCM.
