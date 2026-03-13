---
source: SD.pdf
chapter: SD
section: SD-86 to SD-89
pages: 86-89
title: Auto Transaxle Control (2.0L)
---

# Auto Transaxle Control (2.0L)

> **Note:** The source pages are titled "AUTOMATIC TRANSAXLE CONTROL SYSTEM (2.0L)" in the ETM. This covers the transaxle control module (TCM), solenoid valves, speed sensors, and instrument cluster connections for the 2.0L automatic transaxle variant.

**SD-86 -- Automatic Transaxle Control System (2.0L) (1) -- TCM Power, Transaxle Range Switch, Solenoids**
**SD-87 -- Automatic Transaxle Control System (2.0L) (2) -- Pulse Generators, Instrument Cluster, ABS, Multi-Gauge, Data Link**
**SD-88 -- Automatic Transaxle Control System (2.0L) (3) -- Fuse Box, A/T Relay, Solenoid Valves, Oil Temp Sensor**
**SD-89 -- Component Location Index / Circuit Description**

---

## SD-86 -- Sheet 1: TCM Power, Transaxle Range Switch, Solenoids

<!-- Figure: Auto Transaxle Control 2.0L sheet 1 - TCM power and transaxle range switch, source: SD.pdf page 86 -->

### Power Source / Fuses

| Source | Condition | Fuse/Relay | Rating | Notes |
|--------|-----------|------------|--------|-------|
| HOT IN ON OR START | Sub fuse box | -- | TCM power feed | Via ignition switch |

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Sub fuse box | -- | -- | -- | 0.85 |
| Transaxle range switch | -- | -- | -- | 0.5 |
| TCM | C36-2 | -- | -- | -- |
| Joint connector | -- | -- | -- | -- |
| See Starting System | -- | -- | -- | -- |
| See Illumination | -- | -- | -- | -- |
| MC01 | -- | -- | -- | -- |

### Transaxle Range Switch Connections

| Switch Position | Wire Color | Wire Size | TCM Input |
|-----------------|------------|-----------|-----------|
| P (Park) | -- | 0.5 | C36-2 |
| R (Reverse) | -- | 0.5 | C36-2 |
| N (Neutral) | -- | 0.5 | C36-2 |
| D (Drive) | -- | 0.5 | C36-2 |
| 2 (Second) | -- | 0.5 | C36-2 |
| L (Low) | -- | 0.5 | C36-2 |

### Circuit Paths

```
Sub fuse box (HOT IN ON OR START) -> [0.85] -> MC01
  -> [0.5] -> TCM C36-2 (power feed)

Transaxle range switch:
  Position signals -> [0.5 each] -> Joint connector
  -> [0.5] -> TCM C36-2 (range inputs P, R, N, D, 2, L)

Reverse signal -> [0.5] -> See Illumination (backup lamps)
Neutral/Park -> [0.5] -> See Starting System (starter inhibit)
```

### TCM Pin Connections (SD-86 Bottom Row)

| TCM Connector | Pin | Signal Name | Wire Color | Wire Size |
|---------------|-----|-------------|------------|-----------|
| C36-2 | -- | TCM power (IG) | -- | 0.85 |
| C36-2 | -- | Range switch P | -- | 0.5 |
| C36-2 | -- | Range switch R | -- | 0.5 |
| C36-2 | -- | Range switch N | -- | 0.5 |
| C36-2 | -- | Range switch D | -- | 0.5 |
| C36-2 | -- | Range switch 2 | -- | 0.5 |
| C36-2 | -- | Range switch L | -- | 0.5 |
| C36-2 | -- | Sport mode switch (C39) | -- | 0.5 |

### Cross-References

- "See Starting System" -- Neutral safety / starter inhibit circuit
- "See Illumination" -- Backup lamp feed from range switch R position

---

## SD-87 -- Sheet 2: Pulse Generators, Instrument Cluster, ABS, Multi-Gauge, Data Link

<!-- Figure: Auto Transaxle Control 2.0L sheet 2 - speed sensors, cluster, ABS module, source: SD.pdf page 87 -->

### Power Source / Fuses

| Source | Condition | Fuse/Relay | Rating | Notes |
|--------|-----------|------------|--------|-------|
| HOT AT ALL TIMES | E/R fuse box | -- | Pulse generator power |
| HOT IN ON OR START | Fuse 17 | -- | Instrument cluster |

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| A/T pulse generator #1 | C02-1 | -- | -- | 0.5 |
| A/T pulse generator #2 | C02-2 | -- | -- | 0.5 |
| Instrument cluster | M10-1 | -- | -- | 0.3 |
| Instrument cluster | M10-2 | -- | -- | 0.5 |
| Multi-gauge unit | M42 | -- | -- | 0.5 |
| ABS control module | E37 | -- | -- | 0.5 |
| Vehicle speed sensor | C09 | -- | -- | 0.5 |
| MC109 | -- | -- | -- | 0.3 |
| MC168 | -- | -- | -- | -- |
| MC201 | -- | -- | -- | 0.5 |
| MC265 | -- | -- | -- | -- |
| Joint connector | C241 | -- | -- | -- |
| See Cruise Control | -- | -- | -- | -- |
| Data link connector | M07 | -- | -- | 0.5 |
| Multipurpose check connector | M06 | -- | -- | 0.5 |

### Pulse Generator Connections

#### A/T Pulse Generator #1 (C02-1)

| Pin | Function | Wire Color | Wire Size | TCM Pin |
|-----|----------|------------|-----------|---------|
| 1 | Speed signal (+) | -- | 0.5 | C36-2 |
| 2 | Speed signal (-) | -- | 0.5 | C36-2 |

#### A/T Pulse Generator #2 (C02-2)

| Pin | Function | Wire Color | Wire Size | TCM Pin |
|-----|----------|------------|-----------|---------|
| 1 | Speed signal (+) | -- | 0.5 | C36-2 |
| 2 | Speed signal (-) | -- | 0.5 | C36-2 |

#### Vehicle Speed Sensor (C09)

| Pin | Function | Wire Color | Wire Size | Destination |
|-----|----------|------------|-----------|-------------|
| 1 | VSS signal | -- | 0.5 | TCM / ABS / Instrument cluster |

### Circuit Paths

```
A/T pulse generator #1 (C02-1) -> [0.5] -> TCM C36-2 (input speed)
A/T pulse generator #2 (C02-2) -> [0.5] -> TCM C36-2 (output speed)

Vehicle speed sensor (C09) -> [0.5] -> MC109
  -> [0.3] -> Instrument cluster M10-1 (speedometer)
  -> [0.5] -> ABS control module (E37)
  -> [0.5] -> See Cruise Control

TCM C36-2 -> [0.5] -> MC201 -> [0.5]
  -> Instrument cluster M10-2 (A/T indicator)

TCM C36-2 -> [0.5] -> Data link connector (M07) (K-line)
TCM C36-2 -> [0.5] -> Multipurpose check connector (M06)

TCM C36-2 -> [0.5] -> Multi-gauge unit (M42)
  -> [0.5] -> MC265 -> ABS control module (E37)
```

### TCM Pin Connections (SD-87 Bottom Row)

| TCM Connector | Pin | Signal Name | Wire Color | Wire Size |
|---------------|-----|-------------|------------|-----------|
| C36-2 | -- | Pulse gen #1 signal (+) | -- | 0.5 |
| C36-2 | -- | Pulse gen #1 signal (-) | -- | 0.5 |
| C36-2 | -- | Pulse gen #2 signal (+) | -- | 0.5 |
| C36-2 | -- | Pulse gen #2 signal (-) | -- | 0.5 |
| C36-2 | -- | Vehicle speed signal | -- | 0.5 |
| C36-2 | -- | A/T indicator output | -- | 0.5 |
| C36-2 | -- | K-line (diagnostic) | -- | 0.5 |
| C36-2 | -- | Multi-gauge data | -- | 0.5 |

### Cross-References

- "See Cruise Control" -- Vehicle speed signal feed
- Instrument cluster M10-1 receives tachometer/speed signals
- ABS control module (E37) shares vehicle speed data

---

## SD-88 -- Sheet 3: Fuse Box, A/T Relay, Solenoid Valves, Oil Temp Sensor

<!-- Figure: Auto Transaxle Control 2.0L sheet 3 - A/T relay, solenoid valves, oil temp sensor, source: SD.pdf page 88 -->

### Power Source / Fuses

| Source | Condition | Fuse/Relay | Rating | Notes |
|--------|-----------|------------|--------|-------|
| E/R fuse box | HOT AT ALL TIMES | Fuse | -- | A/T relay power feed |
| -- | -- | A/T control relay (C37) | -- | Solenoid valve power |
| -- | -- | Front fuse 16 | -- | -- |
| -- | -- | Front fuse 18 | -- | -- |

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| E/R fuse box | -- | -- | -- | -- |
| Sub fuse box | EC01 | -- | -- | -- |
| A/T control relay | C37 | coil | -- | 0.5 |
| A/T control relay | C37 | contact | -- | 1.25 |
| A/T solenoid valve A | -- | -- | -- | 0.85 |
| A/T solenoid valve B | -- | -- | -- | 0.85 |
| A/T pulse solenoid valve #1 | -- | -- | -- | 0.85 |
| A/T pulse solenoid valve #2 | -- | -- | -- | 0.85 |
| Oil temp sensor | -- | -- | -- | 0.5 |
| Joint connector | C246 | -- | -- | -- |
| Damper clutch solenoid | -- | -- | -- | 0.85 |
| See Blower & AC Controls | -- | -- | -- | -- |
| G19 | -- | -- | B | -- |

### Solenoid Valve Connections

| Solenoid | Function | Wire Size | Power Feed | Control |
|----------|----------|-----------|------------|---------|
| Solenoid valve A | Shift solenoid | 0.85 | A/T relay (C37) | TCM ground control |
| Solenoid valve B | Shift solenoid | 0.85 | A/T relay (C37) | TCM ground control |
| Pulse solenoid #1 | Line pressure control | 0.85 | A/T relay (C37) | TCM PWM control |
| Pulse solenoid #2 | Converter clutch | 0.85 | A/T relay (C37) | TCM PWM control |
| Damper clutch solenoid | Torque converter lockup | 0.85 | A/T relay (C37) | TCM ground control |

### Oil Temperature Sensor

| Pin | Function | Wire Color | Wire Size | TCM Pin |
|-----|----------|------------|-----------|---------|
| 1 | Oil temp signal | -- | 0.5 | C36-2 |
| 2 | Sensor ground | -- | 0.5 | C36-2 |

### Circuit Paths

```
E/R fuse box -> [1.25] -> A/T control relay (C37) contact side
  -> Fuse feed through sub fuse box EC01

A/T control relay (C37) contact output -> [1.25] -> C246 joint connector
  -> [0.85] -> Solenoid valve A (power)
  -> [0.85] -> Solenoid valve B (power)
  -> [0.85] -> Pulse solenoid #1 (power)
  -> [0.85] -> Pulse solenoid #2 (power)
  -> [0.85] -> Damper clutch solenoid (power)

Solenoid valve A (control) -> [0.85] -> TCM C36-2
Solenoid valve B (control) -> [0.85] -> TCM C36-2
Pulse solenoid #1 (control) -> [0.85] -> TCM C36-2
Pulse solenoid #2 (control) -> [0.85] -> TCM C36-2
Damper clutch solenoid (control) -> [0.85] -> TCM C36-2

Oil temp sensor signal -> [0.5] -> TCM C36-2
Oil temp sensor ground -> [0.5] -> TCM C36-2

A/T control relay (C37) coil:
  TCM C36-2 -> [0.5] -> C37 coil ground (relay activation)

Front fuse 16 -> [0.5] -> TCM C36-2 (A/C signal path)
Front fuse 18 -> [0.5] -> See Blower & AC Controls
```

### TCM Pin Connections (SD-88 Bottom Row)

| TCM Connector | Pin | Signal Name | Wire Color | Wire Size |
|---------------|-----|-------------|------------|-----------|
| C36-2 | -- | A/T relay coil control | -- | 0.5 |
| C36-2 | -- | Solenoid valve A control | -- | 0.85 |
| C36-2 | -- | Solenoid valve B control | -- | 0.85 |
| C36-2 | -- | Pulse solenoid #1 control | -- | 0.85 |
| C36-2 | -- | Pulse solenoid #2 control | -- | 0.85 |
| C36-2 | -- | Damper clutch solenoid control | -- | 0.85 |
| C36-2 | -- | Oil temp sensor signal | -- | 0.5 |
| C36-2 | -- | Oil temp sensor ground | -- | 0.5 |

### Ground Points (Sheet 3)

| Ground ID | Location | Wire Color | Wire Size |
|-----------|----------|------------|-----------|
| G19 | Engine block / transaxle | B | 1.0 |

### Cross-References

- "See Blower & AC Controls" -- A/C signal to TCM for torque management

---

## Component Location Index (SD-89)

<!-- Figure: Component location index and circuit description for Auto Transaxle Control 2.0L, source: SD.pdf page 89 -->

### Components

| Component ID | Description | Location Page |
|--------------|-------------|---------------|
| C01 | Transaxle range switch | CL-18 |
| C02-1 | A/T pulse generator #1 | CL-18 |
| C02-2 | A/T pulse generator #2 | CL-18 |
| C04 | ATM solenoid valve | CL-18 |
| C09 | Vehicle speed sensor (A/T) | CL-18 |
| C33 | ECM | CL-20 |
| C36-2 | TCM | CL-20 |
| C37 | A/T control relay | CL-20 |
| C39 | Sport mode switch | CL-21 |
| C41 | Joint connector | CL-21 |
| C42 | Joint connector/A | CL-21 |
| E56 | Joint connector | CL-12 |
| M06 | Multipurpose check connector | CL-2 |
| M07 | Data link connector | CL-2 |
| M10-1 | Instrument cluster | CL-2 |
| M10-2 | Instrument cluster | CL-2 |
| M42 | Multi gauge unit | CL-4 |

### Connectors

| Connector ID | Location Page |
|--------------|---------------|
| BCM-IM | CL-8 |
| BCM-KM | CL-8 |
| EC01 | CL-6 |
| MC01 | CL-8 |
| MC02 | CL-8 |
| MC03 | CL-8 |
| MM01 | CL-9 |

### Grounds

| Ground ID | Location Page |
|-----------|---------------|
| G19 | CL-33 |

---

## Master TCM Pinout Summary (2.0L A/T -- Connector C36-2)

> **Note:** The 2.0L automatic transaxle uses TCM connector C36-2. Exact pin numbers are difficult to resolve at 150 DPI scan resolution; pin assignments are listed by signal function.

### Power and Ground

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| TCM power (IG) | -- | 0.85 | Sub fuse box (HOT IN ON OR START) |
| TCM ground | B | 1.0 | G19 (engine block / transaxle) |

### Range Switch Inputs

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| Range switch P | -- | 0.5 | Transaxle range switch (C01) |
| Range switch R | -- | 0.5 | Transaxle range switch (C01) |
| Range switch N | -- | 0.5 | Transaxle range switch (C01) |
| Range switch D | -- | 0.5 | Transaxle range switch (C01) |
| Range switch 2 | -- | 0.5 | Transaxle range switch (C01) |
| Range switch L | -- | 0.5 | Transaxle range switch (C01) |
| Sport mode switch | -- | 0.5 | Sport mode switch (C39) |

### Speed Sensor Inputs

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| Pulse gen #1 signal (+) | -- | 0.5 | A/T pulse generator #1 (C02-1) |
| Pulse gen #1 signal (-) | -- | 0.5 | A/T pulse generator #1 (C02-1) |
| Pulse gen #2 signal (+) | -- | 0.5 | A/T pulse generator #2 (C02-2) |
| Pulse gen #2 signal (-) | -- | 0.5 | A/T pulse generator #2 (C02-2) |
| Vehicle speed signal | -- | 0.5 | Vehicle speed sensor (C09) |

### Solenoid Outputs

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| Solenoid valve A control | -- | 0.85 | Shift solenoid A |
| Solenoid valve B control | -- | 0.85 | Shift solenoid B |
| Pulse solenoid #1 control | -- | 0.85 | Line pressure solenoid |
| Pulse solenoid #2 control | -- | 0.85 | Converter clutch solenoid |
| Damper clutch solenoid control | -- | 0.85 | Torque converter lockup |
| A/T relay coil control | -- | 0.5 | A/T control relay (C37) |

### Temperature Sensor

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| Oil temp sensor signal | -- | 0.5 | Oil temp sensor |
| Oil temp sensor ground | -- | 0.5 | Oil temp sensor |

### Diagnostics and Output

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| A/T indicator output | -- | 0.5 | Instrument cluster M10-2 |
| K-line (diagnostic) | -- | 0.5 | Data link connector M07 |
| Multipurpose check | -- | 0.5 | Check connector M06 |
| Multi-gauge data | -- | 0.5 | Multi-gauge unit M42 |

---

## Relay and Fuse Summary

| Relay/Fuse | Rating | Function | Controlled By |
|------------|--------|----------|--------------|
| C37 (A/T control relay) | -- | Solenoid valve power relay | TCM C36-2 (coil ground control) |
| Front fuse 16 | -- | A/C signal path | Passenger compartment fuse box |
| Front fuse 18 | -- | A/C related | Passenger compartment fuse box |
| Sub fuse box | -- | TCM IG power | Ignition switch |

---

## Connector Cross-Reference

| Connector | Component | Sheets |
|-----------|-----------|--------|
| C01 | Transaxle range switch | SD-86 |
| C02-1 | A/T pulse generator #1 | SD-87 |
| C02-2 | A/T pulse generator #2 | SD-87 |
| C04 | ATM solenoid valve | SD-89 (index) |
| C09 | Vehicle speed sensor (A/T) | SD-87 |
| C36-2 | TCM | SD-86 through SD-88 |
| C37 | A/T control relay | SD-88 |
| C39 | Sport mode switch | SD-86 |
| C41 | Joint connector | SD-89 (index) |
| C42 | Joint connector | SD-89 (index) |
| C246 | Joint connector (solenoid power distribution) | SD-88 |
| E37 | ABS control module | SD-87 |
| E56 | Joint connector | SD-89 (index) |
| M06 | Multipurpose check connector | SD-87 |
| M07 | Data link connector | SD-87 |
| M10-1 | Instrument cluster (speedometer/tach) | SD-87 |
| M10-2 | Instrument cluster (A/T indicator) | SD-87 |
| M42 | Multi-gauge unit | SD-87 |

---

## Ground Points (All Sheets)

| Ground ID | Location | Components Served | Reference |
|-----------|----------|-------------------|-----------|
| G19 | Engine block / transaxle case | TCM ground, solenoid grounds | SD-88 |

---

## Circuit Description (from SD-89)

The transaxle control module provides precise gear shift timing and torque converter lock-up by controlling the operation of the automatic transaxle solenoid valves (i.e., shift control solenoid valve A, shift control solenoid valve B, 2nd valve, and under-drive solenoid valve). The transaxle control module operates these solenoid valves based on input signals from the various sensors (for instance, pulse generator #1, #2). The transaxle control module has a built-in self diagnostic feature. Refer to the Shop Manual, section ATM for details.

---

## Notes

- **Scan quality:** 150 DPI scans -- some wire color codes and pin numbers may be approximate where the source image was not fully legible. Cross-reference with the ETM physical copy for critical wiring work.
- **TCM connector:** The 2.0L A/T uses connector ID **C36-2** for the transaxle control module.
- **A/T control relay (C37):** Provides switched power to all five solenoid valves in the transaxle. The relay is energized by the TCM via ground-side switching.
- **Pulse generators:** Two pulse generators (C02-1 and C02-2) provide input and output shaft speed signals to the TCM for shift timing and torque converter slip calculations.
- **Sport mode switch (C39):** Provides an alternate shift map input to the TCM for more aggressive shift points.
- **Shared signals:** The vehicle speed sensor (C09) feeds both the TCM and the ABS control module (E37), as well as the instrument cluster speedometer.
- **This section applies only to 2.0L automatic transaxle vehicles.** The 2.7L V6 has a separate auto transaxle section (see SD pages beyond this range). Manual transaxle (M6CF1) vehicles do not have a TCM or these solenoid circuits.
