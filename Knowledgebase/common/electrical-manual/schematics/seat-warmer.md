---
source: SD.pdf
chapter: SD
section: SD-136 to SD-137
pages: 136-137
title: Seat Warmer
---

# Seat Warmer

**SD-136 -- Seat Warmer (1) Schematic**
**SD-137 -- Component Location Index**

<!-- Figure: Left and right front seat warmer circuits with thermostat switches and BCM power supply, source: SD.pdf page 136 -->

---

## Component Table (SD-136)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 25 (HOT in ON) | -- | -- | R/W | 3.0S |
| BCM-KM | -- | -- | R/W | 3.0S |
| Left front seat warmer switch (M43) | input | -- | R/W | 1.25S |
| Left front seat warmer switch (M43) | output | -- | R/W | 1.25S |
| Left front seat warmer switch (M43) | illumination | -- | R/B | 0.5S |
| Left front seat warmer switch (M43) | ground | -- | B | 0.5S |
| Right front seat warmer switch (M44) | input | -- | R/W | 1.25S |
| Right front seat warmer switch (M44) | output | -- | R/W | 1.25S |
| Right front seat warmer switch (M44) | illumination | -- | R/B | 0.5S |
| Right front seat warmer switch (M44) | ground | -- | B | 0.5S |
| Left front seat warmer (M47) | heater (+) | -- | R/W | 1.25S |
| Left front seat warmer (M47) | thermostat | -- | -- | -- |
| Left front seat warmer (M47) | heater (-) | -- | B | 1.25S |
| Right front seat warmer (M51) | heater (+) | -- | R/W | 1.25S |
| Right front seat warmer (M51) | thermostat | -- | -- | -- |
| Right front seat warmer (M51) | heater (-) | -- | B | 1.25S |
| Joint connector (M36) | -- | -- | R/W | 1.25S |
| Joint connector (M45) | -- | -- | -- | -- |

---

## Circuit Paths

### Left Front Seat Warmer Power
```
Battery (+) -> Fuse 25 (HOT in ON)
  -> [R/W, 3.0S] -> BCM-KM
  -> [R/W, 1.25S] -> Joint connector M36
  -> [R/W, 1.25S] -> Left front seat warmer switch M43 (input)
  -> M43 switch closed (pushed ON)
  -> [R/W, 1.25S] -> Left front seat warmer M47 (heater element)
  -> Thermostat (opens at ~75 +/- 5 deg C, closes at ~55 +/- 5 deg C)
  -> [B, 1.25S] -> GND (G01)
```

### Right Front Seat Warmer Power
```
Battery (+) -> Fuse 25 (HOT in ON)
  -> [R/W, 3.0S] -> BCM-KM
  -> [R/W, 1.25S] -> Joint connector M45
  -> [R/W, 1.25S] -> Right front seat warmer switch M44 (input)
  -> M44 switch closed (pushed ON)
  -> [R/W, 1.25S] -> Right front seat warmer M51 (heater element)
  -> Thermostat (opens at ~75 +/- 5 deg C, closes at ~55 +/- 5 deg C)
  -> [B, 1.25S] -> GND (G02)
```

### Switch Illumination -- Left
```
See illumination feed
  -> [R/B, 0.5S] -> Left front seat warmer switch M43 (illumination)
M43 illumination ground -> [B, 0.5S] -> GND (G01)
```

### Switch Illumination -- Right
```
See illumination feed
  -> [R/B, 0.5S] -> Right front seat warmer switch M44 (illumination)
M44 illumination ground -> [B, 0.5S] -> GND (G02)
```

### Seat Warmer Ground Paths
```
Left front seat warmer M47 -> [B, 1.25S] -> M36 connector -> GND (G01)
Right front seat warmer M51 -> [B, 1.25S] -> M45 connector -> GND (G02)
Switch grounds -> [B, 0.5S] -> GND (G11)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G01 | Under dash, driver side | Left seat warmer ground, left switch ground | CL-32 |
| G02 | Under dash, passenger side | Right seat warmer ground, right switch ground | CL-32 |
| G11 | Rear body / interior | Switch illumination ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-KM | BCM passenger compartment connector | CL-8 |

---

## Component Location Index (SD-137)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| M36 | Joint connector | CL-4 |
| M43 | Left front seat warmer switch | CL-4 |
| M44 | Right front seat warmer switch | CL-4 |
| M45 | Joint connector | CL-4 |
| M47 | Left front seat warmer | CL-5 |
| M51 | Right front seat warmer | CL-5 |

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-KM | BCM connector | CL-8 |

| Ground ID | Location Page |
|-----------|---------------|
| G01 | CL-32 |
| G02 | CL-32 |
| G11 | CL-33 |

---

## Notes

- Fuse 25 supplies battery voltage to the left/right front seat warmer when the ignition switch is ON and the left/right front seat warmer switches are pushed.
- When each seat warmer switch is pushed, battery voltage is supplied to the seat warmer and grounded through G01/G02.
- Each seat warmer has an internal thermostat that opens at approximately 75 deg C (+/- 5 deg C) to prevent overheating, and closes again at approximately 55 deg C (+/- 5 deg C) to resume heating.
- The heater elements are resistive pads embedded in the seat cushion and backrest.
