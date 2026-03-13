---
source: SD.pdf
chapter: SD
section: SD-48 to SD-49
pages: 48-49
title: Vehicle Speed Sensor
---

# Vehicle Speed Sensor

**SD-48 -- Vehicle Speed Sensor (1) Schematic**
**SD-49 -- Component Location Index and Circuit Description**

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Vehicle speed sensor (2.0L, with A/T) | C09 | -- | -- | 0.5S |
| Vehicle speed sensor (2.0L, with M/T) | C10 | -- | -- | 0.5S |
| Vehicle speed sensor (2.7L) | C109 | -- | -- | 0.5S |
| Vehicle speed sensor (1.6L) | C210 | -- | -- | 0.5S |
| ECM (2.0L) | C33 | -- | G/B | 0.5S |
| ECM (2.7L) | C133-4 | -- | G/B | 0.5S |
| ECM (1.6L) | C233 | -- | -- | 0.5S |
| Instrument cluster | M10-1 | 17 | G/B | 0.85S |
| Data link connector | M07 | -- | -- | 0.85S |
| Multi gauge unit | M42 | -- | -- | 0.85S |
| Joint connector (2.0L) | C41 | -- | -- | -- |
| Joint connector (2.7L) | C141 | -- | -- | -- |
| Joint connector (1.6L) | C241 | -- | -- | -- |
| BCM-JM | -- | -- | -- | 0.5S |

---

## Circuit Paths

### VSS Signal Path (2.7L V6)

```
Vehicle speed sensor (C109) → [G/B, 0.5S]
  → Joint connector (C141)
  → BCM-JM (pin 4)
  → [G/B, 0.85S] → Instrument cluster (M10-1, pin 17)
  → [G/B, 0.5S] → ECM (C133-4)
```

### VSS Signal Path (2.0L)

```
Vehicle speed sensor (C09/C10) → [G/B, 0.5S]
  → Joint connector (C41)
  → BCM-JM
  → [G/B, 0.85S] → Instrument cluster (M10-1, pin 17)
  → [G/B, 0.5S] → ECM (C33)
```

### VSS Signal Path (1.6L)

```
Vehicle speed sensor (C210) → [G/B, 0.5S]
  → Joint connector (C241)
  → BCM-JM
  → Instrument cluster (M10-1)
  → ECM (C233)
```

### VSS Power Feed

```
BCM Fuse 16 (10A) → [Y/R, 0.5S]
  → Joint connector (MC01/MC101/MC201)
  → Vehicle speed sensor power pin
```

### VSS Ground

```
Vehicle speed sensor ground → [B, 0.5B]
  → G20 (2.0L, CONTROL)
  → G23 (2.7L, CONTROL)
  → G25 (1.6L, CONTROL)
```

---

## Connector Bus Detail (SD-48)

### Upper ECM Bus

| Source | Connector | Signal | Wire | Destination |
|--------|-----------|--------|------|-------------|
| ECM (2.0L) | C33 | VSS | G/B, 0.5S | C41 joint |
| ECM (2.7L) | C133-4 | VSS | G/B, 0.5S | C141 joint |
| ECM (2.7L) | C133-1 | -- | -- | -- |

### BCM Bus Connections

| From | Connector | To | Connector | Wire | Size |
|------|-----------|-----|-----------|------|------|
| BCM-JM | -- | MC01 | -- | G/B | 0.5S |
| BCM-JM | -- | MC101 | -- | G/B | 0.5S |
| BCM-JM | -- | MC201 | -- | G/B | 0.5S |
| BCM-JM | -- | MC401 | -- | G/B | 0.5S |

### Lower Instrument Bus

| Component | Connector | Pin | Wire | Size |
|-----------|-----------|-----|------|------|
| Data link connector | M07 | 1 | -- | 0.85S |
| Instrument cluster | M10-1 | 17 | G/B | 0.85S |
| Multi gauge unit | M42 | -- | -- | 0.85S |
| Joint connector | M34 | -- | -- | 0.85S |
| Joint connector | M24 | -- | -- | 0.85S |
| Cruise control module | C38/C138 | -- | G/B | 0.85S |

---

## Ground Points

| Ground ID | Location | Components |
|-----------|----------|------------|
| G20 | Control (2.0L) | VSS ground, front wiper, brake fluid, cruise |
| G23 | Control (2.7L) | VSS ground, front wiper, brake fluid, cruise |
| G25 | Control (1.6L) | VSS ground, wiper, CMP sensor |

---

## Component Location Index (SD-49)

### Components

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C09 | Vehicle speed sensor (2.0L, with A/T) | CL-18 |
| C10 | Vehicle speed sensor (2.0L, with M/T) | CL-18 |
| C33 | ECM (2.0L) | CL-20 |
| C41 | Joint connector (2.0L) | CL-21 |
| C109 | Vehicle speed sensor (2.7L) | CL-22 |
| C133-4 | ECM (2.7L) | CL-25 |
| C141 | Joint connector (2.7L) | CL-25 |
| C210 | Vehicle speed sensor (1.6L) | CL-27 |
| C241 | Joint connector (1.6L) | CL-28 |
| M10-1 | Instrument cluster | CL-2 |
| M24 | Joint connector | CL-4 |
| M42 | Multi gauge unit | CL-4 |

### Connectors

| Connector | Location Page |
|-----------|---------------|
| BCM-JM | CL-8 |
| MC01 | CL-8 |
| MC101 | CL-8 |
| MC203 | CL-8 |
| MM02 | CL-9 |

### Grounds

| Ground ID | Location Page |
|-----------|---------------|
| G20 | CL-32 |
| G23 | CL-34 |
| G25 | CL-34 |

---

## Circuit Description (from SD-49)

The vehicle speed sensor, located on the speedometer driven gear in the transaxle, generates pulse signals that indicate the vehicle's speed and provides signals to the control modules to calculate the vehicle speed.

The vehicle speed sensor (VSS) intermittently grounds the circuits. The number of pulses per minute increases/decreases with the speed of the car.

---

## Notes

- The VSS is a Hall-effect sensor producing 4 pulses per revolution of the speedometer drive gear.
- Signal wire is G/B (green with black stripe), 0.5S gauge.
- The VSS signal feeds: ECM, instrument cluster, cruise control module, multi gauge unit, and BCM-JM.
- For the 2.7L V6: the VSS is at connector C109 on the transaxle, signal routes through joint connector C141 to ECM C133-4 and instrument cluster M10-1 pin 17.
- VSS ground is at the engine-area control ground point (G20 for 2.0L, G23 for 2.7L, G25 for 1.6L).
