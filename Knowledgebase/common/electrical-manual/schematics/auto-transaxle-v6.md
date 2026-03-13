---
source: SD.pdf
chapter: SD
section: SD-90 to SD-99
pages: 90-99
title: Auto Transaxle Control (2.7L V6)
---

# Auto Transaxle Control (2.7L V6)

**SD-90 -- Auto Transaxle Control System (2.7L) (1) -- Power, Transaxle Range Switch, Inhibitor Switch**
**SD-91 -- Auto Transaxle Control System (2.7L) (2) -- Stop Lamps, Cruise, A/T Pulse Gen, ABS, TCM Data**
**SD-92 -- Auto Transaxle Control System (2.7L) (3) -- Solenoid Valves, Oil Temp Sensor**
**SD-93 -- Component Location Index / Circuit Description**
**SD-94 -- Anti-Lock Brake System / Traction Control System (1) -- Power, ABS Module, TCS Switch**
**SD-95 -- Anti-Lock Brake System / Traction Control System (2) -- Sensors, Data Link, Wheel Speed**
**SD-96 -- Anti-Lock Brake System / Traction Control System (3) -- ABS Solenoid Valves, Motor**
**SD-97 -- Component Location Index (ABS/TCS)**
**SD-98 -- Circuit Description (ABS/TCS)**
**SD-99 -- Memo (blank)**

---

## SD-90 -- Sheet 1: Power Distribution, Transaxle Range Switch, Inhibitor Switch

<!-- Figure: Auto Transaxle Control System (2.7L) sheet 1 -- power feeds, transaxle range switch, mode switch, inhibitor switch to TCM, source: SD.pdf page 90 -->

### Power Supply

| Source | Fuse/Link | Rating | Wire Color | Wire Size |
|--------|-----------|--------|------------|-----------|
| HOT IN ON OR START | Fuse 5 | -- | -- | -- |
| HOT IN ON OR START | Fuse 6 | -- | -- | -- |
| HOT AT ALL TIMES | Fusible link | -- | R | -- |

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Transaxle range switch | C101 | -- | -- | -- |
| A/T solenoid valve | C104 | -- | -- | -- |
| Sport mode switch | C139 | -- | -- | -- |
| Instrument cluster | M10-3 | -- | -- | -- |
| BCM-IM | -- | -- | -- | 0.5P |
| MC168 | -- | -- | -- | -- |
| MC169 | -- | -- | -- | -- |
| Joint connector | C141 | -- | -- | -- |

### Transaxle Range Switch (C101) Connections

| Pin | Signal | Wire Color | Wire Size | Destination |
|-----|--------|------------|-----------|-------------|
| -- | Park/Neutral | -- | 0.5R | See Starting System |
| -- | Reverse | -- | 0.5B | See Illumination |
| -- | Drive position signals | -- | 0.5P/B | TCM (C136-2) |

### TCM Connector Assignments (Bottom of SD-90)

The shaded band represents the TCM (C136-1, C136-2, C136-3) internal connections. Wires enter from the top (components) and bottom (ECM side).

| TCM Connector | Signal | Wire Color | Wire Size |
|---------------|--------|------------|-----------|
| C136-2 | Range switch signal | -- | 0.5R |
| C136-2 | Range switch signal | -- | 0.5B |
| C136-2 | Range switch signal | -- | 0.3P/B |
| C136-2 | Range switch signal | -- | 0.3P/B |
| C136-2 | Range switch signal | -- | 0.5R |
| C136-2 | Range switch signal | -- | 0.5R |
| C136-2 | Range switch signal | -- | 0.5R |

### Circuit Paths

#### Ignition Power to TCM
```
Fuse 5 (HOT IN ON OR START) -> [0.5P] -> BCM-IM -> [0.5P] -> MC168
  -> [0.5P] -> TCM power (C136-2)
```

#### Transaxle Range Switch to TCM
```
Transaxle range switch (C101) -> [0.5R] -> C141 joint connector
  -> [0.5R] -> TCM (C136-2) range position inputs
```

#### Reverse Lamp Feed
```
Transaxle range switch (C101) reverse -> [0.5B] -> See Illumination section
```

#### Inhibitor Switch / Park-Neutral to Starter
```
Transaxle range switch (C101) P/N -> [0.5R] -> See Starting System
```

#### Sport Mode Switch
```
Sport mode switch (C139) -> [0.5R] -> MC168 -> TCM (C136-2)
```

#### TCM to Indicators & Gauges
```
TCM (C136-2) -> [0.5R] -> MC168 -> [0.5R] -> See Indicators & Gauges
```

#### TCM to Instrument Cluster
```
TCM -> [0.5P/B] -> instrument cluster (M10-3)
  -> indicator lamp (shift position display)
```

### Ground Points (SD-90)

| Ground ID | Location | Components |
|-----------|----------|------------|
| F06 | -- | TCM ground path |

---

## SD-91 -- Sheet 2: Stop Lamps, Cruise Control, A/T Pulse Generator, ABS, Data Link

<!-- Figure: Auto Transaxle Control System (2.7L) sheet 2 -- brake switch, cruise control, pulse generators, ABS module inputs, data link, source: SD.pdf page 91 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| A/T pulse generator #1 | C130-1 | -- | -- | 0.5R |
| A/T pulse generator #2 | C130-2 | -- | -- | 0.5R |
| Stop lamp switch | C241 | -- | G/W | 0.85 |
| Cruise control (see Cruise) | -- | -- | -- | 0.5BCC |
| Multi-gauge unit | M42 | -- | -- | 0.5 |
| ABS control module | E37 | -- | -- | -- |
| Data link connector | M07 | -- | -- | -- |
| Multipurpose check connector | M06 | -- | -- | -- |
| MC101 | -- | -- | -- | -- |
| MC102 | -- | -- | -- | -- |
| MC168 | -- | -- | -- | -- |
| Joint connector | C141 | -- | -- | -- |

### TCM Connections (SD-91 Top and Bottom)

| TCM Connector | Signal | Wire Color | Wire Size |
|---------------|--------|------------|-----------|
| C136-1 | A/T pulse generator #1 signal | -- | 0.5R |
| C136-1 | A/T pulse generator #1 ground | -- | 0.5R |
| C136-1 | A/T pulse generator #2 signal | -- | 0.5R |
| C136-1 | A/T pulse generator #2 ground | -- | 0.5R |
| C136-1 | Stop lamp switch input | G/W | 0.85 |
| C136-1 | Cruise control input | -- | 0.5BCC |
| C136-3 | Vehicle speed (to ABS) | -- | 0.5 |

### Circuit Paths

#### A/T Pulse Generator #1
```
A/T pulse generator #1 (C130-1) -> [0.5R] -> C136-1 -> TCM
A/T pulse generator #1 (C130-1) ground -> [0.5R] -> C136-1 -> TCM
```

#### A/T Pulse Generator #2
```
A/T pulse generator #2 (C130-2) -> [0.5R] -> C136-1 -> TCM
A/T pulse generator #2 (C130-2) ground -> [0.5R] -> C136-1 -> TCM
```

#### Stop Lamp Switch to TCM
```
Stop lamp switch (C241) -> [G/W, 0.85] -> C136-1 -> TCM (brake input)
```

#### Cruise Control Input
```
See Cruise Control section -> [0.5BCC] -> C136-1 -> TCM
```

#### TCM to ABS Control Module
```
TCM (C136-3) -> [0.5] -> MC101 -> [0.5] -> ABS control module (E37)
```

#### TCM to Multi-Gauge Unit
```
TCM (C136-3) -> [0.3L/G] -> MC102 -> [0.3L/G] -> Multi-gauge unit (M42)
```

#### TCM to Data Link / Diagnostics
```
TCM (C136-3) -> [0.5L/G] -> MC168 -> M07 (data link connector)
TCM (C136-3) -> [0.5] -> M06 (multipurpose check connector)
```

### Ground Points (SD-91)

| Ground ID | Location | Components |
|-----------|----------|------------|
| G21 | -- | TCM ground |

---

## SD-92 -- Sheet 3: Solenoid Valves, A/T Control Relay, Oil Temp Sensor

<!-- Figure: Auto Transaxle Control System (2.7L) sheet 3 -- fusible links, A/T control relay, solenoid valves, oil temperature sensor, source: SD.pdf page 92 -->

### Power Supply

| Source | Fuse/Link | Rating | Wire Color | Wire Size |
|--------|-----------|--------|------------|-----------|
| HOT AT ALL TIMES | Fusible link | -- | R | 2.0R |
| HOT AT ALL TIMES | Fusible link | -- | R | 2.0R |

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| A/T control relay (C137) | contact 30 | power in | R | 2.0R |
| A/T control relay (C137) | contact 87 | power out | -- | -- |
| A/T control relay (C137) | coil | control | -- | 0.85 |
| Joint connector | E56 | -- | R | -- |
| Joint connector | C141 | -- | -- | -- |
| Joint connector | C142 | -- | -- | -- |
| A/T solenoid #1 | C104 | -- | -- | -- |
| A/T solenoid #2 | C104 | -- | -- | -- |
| Underdrive brake solenoid valve | -- | -- | -- | -- |
| 2nd valve | -- | -- | -- | -- |
| Low solenoid valve | -- | -- | -- | -- |
| Oil temperature sensor | C108 | -- | -- | -- |
| EC101 | -- | -- | -- | -- |
| EC102 | -- | -- | -- | -- |

### A/T Control Relay (C137)

| Pin | Function | Wire Color | Wire Size |
|-----|----------|------------|-----------|
| 30 (power in) | Battery feed from fusible link | R | 2.0R |
| 87 (power out) | Feed to solenoid valves | -- | 1.25 |
| 85 (coil +) | Ignition power | -- | 0.85 |
| 86 (coil -) | TCM controlled ground | -- | 0.85 |

### Solenoid Valve Connections

| Solenoid | Connector | Power Wire | Control Wire | Wire Size |
|----------|-----------|-----------|--------------|-----------|
| A/T solenoid valve #1 | C104 | from C137 relay | to TCM (C136-1) | 0.85 |
| A/T solenoid valve #2 | C104 | from C137 relay | to TCM (C136-1) | 0.85 |
| Underdrive brake solenoid | -- | from Fuse/Fusible | to TCM | 0.85 |
| 2nd valve solenoid | -- | from Fuse/Fusible | to TCM | 0.85 |
| Low solenoid valve | -- | from Fuse/Fusible | to TCM | 0.85 |

### Oil Temperature Sensor (C108)

| Pin | Function | Wire Color | Wire Size | Destination |
|-----|----------|------------|-----------|-------------|
| 1 | OT signal | -- | 0.5 | TCM (C136-2) |
| 2 | OT ground | -- | 0.5 | TCM (C136-2) |

### TCM Connections (SD-92 Bottom)

| TCM Connector | Signal | Wire Color | Wire Size |
|---------------|--------|------------|-----------|
| C136-1 | Solenoid #1 control | -- | 0.85 |
| C136-1 | Solenoid #2 control | -- | 0.85 |
| C136-1 | Underdrive solenoid control | -- | 0.85 |
| C136-1 | 2nd valve control | -- | 0.85 |
| C136-1 | Low solenoid control | -- | 0.85 |
| C136-2 | Oil temp sensor signal | -- | 0.5 |
| C136-2 | Oil temp sensor ground | -- | 0.5 |
| C136-2 | A/T control relay coil | -- | 0.85 |

### Circuit Paths

#### A/T Control Relay Power
```
Fusible link (HOT AT ALL TIMES) -> [R, 2.0R] -> E56 joint connector
  -> [R, 2.0R] -> A/T control relay C137 (contact 30)
A/T control relay C137 (contact 87) -> [1.25] -> solenoid valve power bus
```

#### A/T Control Relay Coil
```
Fuse/Fusible -> [0.85] -> A/T control relay C137 coil (+)
A/T control relay C137 coil (-) -> [0.85] -> TCM (C136-2) relay control
```

#### Solenoid #1 Circuit
```
A/T control relay output -> [0.85] -> A/T solenoid #1 (C104) power
A/T solenoid #1 (C104) control -> [0.85] -> EC101 -> C136-1 -> TCM
```

#### Solenoid #2 Circuit
```
A/T control relay output -> [0.85] -> A/T solenoid #2 (C104) power
A/T solenoid #2 (C104) control -> [0.85] -> EC102 -> C136-1 -> TCM
```

#### Oil Temperature Sensor
```
Oil temp sensor (C108 pin 1) -> [0.5] -> C136-2 -> TCM (OT signal)
Oil temp sensor (C108 pin 2) -> [0.5] -> C136-2 -> TCM (OT ground)
```

---

## SD-93 -- Component Location Index / Circuit Description (Auto Transaxle)

<!-- Figure: Component location index and circuit description for Auto Transaxle Control System (2.7L), source: SD.pdf page 93 -->

### Components

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C101 | Transaxle range switch | CL-21 |
| C130-1 | A/T pulse generator #1 | CL-21 |
| C130-2 | A/T pulse generator #2 | CL-21 |
| C104 | ATM solenoid valve | CL-21 |
| C133-1 | ECM | CL-25 |
| C133-4 | ECM | CL-25 |
| C136-1 | TCM | CL-25 |
| C136-2 | TCM | CL-25 |
| C136-3 | TCM | CL-25 |
| C137 | A/T control relay | CL-25 |
| C139 | Sport mode switch | CL-25 |
| C141 | Joint connector | CL-25 |
| C142 | Joint connector | CL-25 |
| E37 | ABS control module | CL-12 |
| E56 | Joint connector | CL-12 |
| M06 | Multipurpose check connector | CL-2 |
| M07 | Data link connector | CL-2 |
| M10-3 | Instrument cluster | CL-2 |
| M42 | Multi gauge unit | CL-4 |

### Connectors

| Connector | Location Page |
|-----------|---------------|
| BCM-IM | CL-8 |
| BCM-KM | CL-8 |
| EC101 | CL-14 |
| MC101 | CL-8 |
| MC102 | CL-8 |
| MC103 | CL-8 |

### Grounds

| Ground ID | Location Page |
|-----------|---------------|
| G21 | CL-34 |

### Circuit Description

The transaxle control module provides precise gear shift timing and torque converter lock-up by controlling the operation of the automatic transaxle solenoid valves (Low solenoid valve, underdrive brake solenoid valve, 2nd valve and under-drive solenoid valve). The transaxle control module operates these solenoid valves based on input signals from the various sensors (for instance, pulse generator #1, #2). The transaxle control module has a built-in self diagnostic feature. Refer to the Shop Manual, section ATM, for details.

---

## SD-94 -- Sheet 1: Anti-Lock Brake System / Traction Control System (1)

<!-- Figure: ABS/TCS system sheet 1 -- power distribution, ABS module, TCS switch, brake fluid level, solenoid valves, source: SD.pdf page 94 -->

### Power Supply

| Source | Fuse/Link | Rating | Wire Color | Wire Size |
|--------|-----------|--------|------------|-----------|
| HOT AT ALL TIMES | Fusible link | -- | R | 2.0 |
| CONT TO IGN OF START | Fuse distributor | -- | -- | -- |
| HOT AT ALL TIMES | Fuse 17 | -- | -- | 0.5P/B |
| -- | Fuse 17 | -- | -- | -- |

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| ABS control module | E37 | -- | -- | -- |
| TCS switch | M15 | -- | -- | 0.5 |
| Brake fluid level switch | -- | -- | -- | 0.85 |
| Instrument cluster | M10-1 | -- | -- | -- |
| MC101 | -- | -- | -- | -- |
| MC102 | -- | -- | -- | -- |
| MC103 | -- | -- | -- | -- |
| BCM-CE | -- | -- | -- | -- |
| MC168 | -- | -- | -- | -- |
| Coupled with Smart Junction Systems | -- | -- | -- | -- |

### ABS Control Module (E37) Connections -- Upper Section

| E37 Pin Area | Signal | Wire Color | Wire Size | Direction |
|--------------|--------|------------|-----------|-----------|
| Power in | Battery feed (fusible link) | R | 2.0 | from fusible link |
| Power in | Ignition feed | -- | 0.5P/B | from fuse 17 |
| Ground | Chassis ground | B | 0.85 | to ground |
| M15-1 | TCS switch | -- | 0.5 | from TCS switch |
| M15-2 | TCS indicator | -- | 0.5 | to instrument cluster |
| -- | Brake fluid level | -- | 0.85 | from level switch |
| MR11-1 | ABS motor relay | -- | 0.85 | internal |
| MR11-2 | ABS warning lamp | -- | 0.3L/R | to instrument cluster |

### ABS Module to Instrument Cluster

| Signal | Wire Color | Wire Size | Cluster Pin |
|--------|------------|-----------|-------------|
| ABS warning lamp | L/R | 0.3L/R | M10-1 |
| TCS indicator | -- | 0.5 | M10-1 |

### ABS Module to ECM/TCM

| Signal | Wire Color | Wire Size | Destination |
|--------|------------|-----------|-------------|
| MC101(L,1) / MC101(L,2) | -- | 0.5 | ECM (C133-4) |
| MC102(L,1) / MC102(L,2) | -- | 0.5 | TCM (C136-3) |
| MC103 | -- | 0.85 | BCM-CE |

### Circuit Paths

#### ABS Module Power Feed
```
Fusible link (HOT AT ALL TIMES) -> [R, 2.0] -> ABS control module (E37) power
Fuse 17 -> [0.5P/B] -> ABS control module (E37) ignition power
```

#### TCS Switch Circuit
```
TCS switch (M15) -> [0.5] -> ABS control module (E37)
  -> [0.5] -> TCS indicator in instrument cluster (M10-1)
```

#### ABS Warning Lamp
```
ABS control module (E37) -> [0.3L/R] -> MC168
  -> [0.3L/R] -> Instrument cluster (M10-1) ABS warning lamp
```

#### Brake Fluid Level Switch
```
Brake fluid level switch -> [0.85] -> ABS control module (E37)
  -> Coupled with Smart Junction Systems
```

#### ABS to ECM Communication
```
ABS control module (E37) -> [0.5] -> MC101(L,1) -> ECM (C133-4)
ABS control module (E37) -> [0.5] -> MC101(L,2) -> ECM (C133-4)
```

#### ABS to TCM Communication
```
ABS control module (E37) -> [0.5] -> MC102(L,1) -> TCM (C136-3)
ABS control module (E37) -> [0.5] -> MC102(L,2) -> TCM (C136-3)
```

### Ground Points (SD-94)

| Ground ID | Location | Components |
|-----------|----------|------------|
| E37 | ABS module internal | ABS motor, solenoid grounds |

---

## SD-95 -- Sheet 2: ABS/TCS Sensors, Data Link, Wheel Speed Sensors

<!-- Figure: ABS/TCS system sheet 2 -- wheel speed sensors, data link, diagnostics, source: SD.pdf page 95 -->

### Power Supply

| Source | Fuse/Link | Rating | Wire Color | Wire Size |
|--------|-----------|--------|------------|-----------|
| -- | Fuse 16 | -- | -- | 0.5P/B |

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Left front wheel sensor | E01 | -- | -- | 0.5 |
| Right front wheel sensor | E39 | -- | -- | 0.5 |
| Left rear wheel sensor | M64 | -- | -- | 0.5 |
| Right rear wheel sensor | M65 | -- | -- | 0.5 |
| Data link connector | M07 | -- | -- | 0.5 |
| ABS control module | E37 | -- | -- | -- |
| BCM-KM | -- | -- | -- | -- |
| BCM-CE | -- | -- | -- | -- |
| MC101 | -- | -- | -- | -- |
| MC103 | -- | -- | -- | -- |
| EM01 | -- | -- | -- | -- |

### Wheel Speed Sensor Connections

| Sensor | Connector | Signal+ Wire | Signal+ Size | Signal- Wire | Signal- Size | ABS Module Pin |
|--------|-----------|-------------|--------------|-------------|--------------|----------------|
| Left front | E01 | MC101(L,1) | 0.5 | MC101(L,2) | 0.5 | E37 |
| Right front | E39 | MC103(L,1) | 0.5 | MC103(L,2) | 0.5 | E37 |
| Left rear | M64 | -- | 0.5 | -- | 0.5 | E37 |
| Right rear | M65 | -- | 0.5 | -- | 0.5 | E37 |

### ABS Module (E37) -- Sensor Input Section

| E37 Signal | Wire Color | Wire Size |
|------------|------------|-----------|
| LF wheel sensor + | -- | 0.5 |
| LF wheel sensor - | -- | 0.5 |
| RF wheel sensor + | -- | 0.5 |
| RF wheel sensor - | -- | 0.5 |
| LR wheel sensor + | -- | 0.5 |
| LR wheel sensor - | -- | 0.5 |
| RR wheel sensor + | -- | 0.5 |
| RR wheel sensor - | -- | 0.5 |
| TCS (band 12V) | -- | 0.5P/B |
| Diagnostic | -- | 0.5 |
| CAN START (batt) | -- | -- |

### ABS to Data Link
```
ABS control module (E37) -> [0.5] -> BCM-KM -> [0.5] -> M07 (data link connector)
```

### Circuit Paths

#### Left Front Wheel Speed Sensor
```
Left front wheel sensor (E01) pin 1 -> [0.5] -> EC01 -> MC101 -> ABS module (E37)
Left front wheel sensor (E01) pin 2 -> [0.5] -> EC01 -> MC101 -> ABS module (E37)
```

#### Right Front Wheel Speed Sensor
```
Right front wheel sensor (E39) pin 1 -> [0.5] -> EC02 -> MC103 -> ABS module (E37)
Right front wheel sensor (E39) pin 2 -> [0.5] -> EC02 -> MC103 -> ABS module (E37)
```

#### Left Rear Wheel Speed Sensor
```
Left rear wheel sensor (M64) pin 1 -> [0.5] -> EM01 -> ABS module (E37)
Left rear wheel sensor (M64) pin 2 -> [0.5] -> EM01 -> ABS module (E37)
```

#### Right Rear Wheel Speed Sensor
```
Right rear wheel sensor (M65) pin 1 -> [0.5] -> EM01 -> ABS module (E37)
Right rear wheel sensor (M65) pin 2 -> [0.5] -> EM01 -> ABS module (E37)
```

#### Diagnostic / Data Link
```
ABS control module (E37) -> [0.5] -> BCM-KM -> [0.5]
  -> Data link connector (M07) for OBD-II communication
```

### Wheel Speed Sensor Physical Locations

| Sensor | Location |
|--------|----------|
| E01 (Left front) | Left front knuckle |
| E39 (Right front) | Right front knuckle |
| M64 (Left rear) | Left rear hub area |
| M65 (Right rear) | Right rear hub area |

### Ground Points (SD-95)

| Ground ID | Location | Components |
|-----------|----------|------------|
| E37 | ABS module internal | Sensor return grounds |

---

## SD-96 -- Sheet 3: ABS Solenoid Valves, Motor Relay, Hydraulic Unit

<!-- Figure: ABS/TCS system sheet 3 -- ABS internal solenoid valves, pump motor, motor relay, hydraulic modulator detail, source: SD.pdf page 96 -->

### Power Supply

| Source | Fuse/Link | Rating | Wire Color | Wire Size |
|--------|-----------|--------|------------|-----------|
| CONT TO IGN OF START | Fusible link | -- | R | -- |

### ABS Hydraulic Unit Internal Components

The ABS control module (E37) contains multiple solenoid valves and a pump motor internally. The following are the internal solenoid connections shown on SD-96.

| Component | Function | Wire Size |
|-----------|----------|-----------|
| Solenoid valve (LF inlet) | Left front brake inlet | 0.5 |
| Solenoid valve (LF outlet) | Left front brake outlet | 0.5 |
| Solenoid valve (RF inlet) | Right front brake inlet | 0.5 |
| Solenoid valve (RF outlet) | Right front brake outlet | 0.5 |
| Solenoid valve (LR inlet) | Left rear brake inlet | 0.5 |
| Solenoid valve (LR outlet) | Left rear brake outlet | 0.5 |
| Solenoid valve (RR inlet) | Right rear brake inlet | 0.5 |
| Solenoid valve (RR outlet) | Right rear brake outlet | 0.5 |
| ABS pump motor | Hydraulic pump | 1.0 |
| Motor relay | Pump motor power control | 0.85 |

### ABS Module (E37) -- Solenoid/Motor Section

| E37 Internal | Signal | Wire Size |
|--------------|--------|-----------|
| Solenoid valve bank (8 valves) | Controlled by E37 logic | 0.5 |
| Pump motor + | Battery via motor relay | 1.0 |
| Pump motor - | Ground | 1.0 |
| Motor relay coil | E37 logic controlled | 0.85 |
| Load ground module | Common solenoid ground | 0.5 |

### External Connections from ABS Module

| E37 Pin | Signal | Wire Color | Wire Size | Destination |
|---------|--------|------------|-----------|-------------|
| -- | Solenoid ground bus | B | 0.5 | Load ground module |
| -- | Motor power | R | 1.0 | from fusible link |
| -- | Motor ground | B | 1.0 | chassis ground |

### Circuit Paths

#### ABS Motor Relay Circuit
```
Fusible link (CONT TO IGN OF START) -> [R] -> E37 motor relay (contact 30)
E37 motor relay (contact 87) -> [1.0] -> ABS pump motor (+)
ABS pump motor (-) -> [B, 1.0] -> chassis ground
E37 logic -> motor relay coil -> [0.85] -> internal ground
```

#### ABS Solenoid Valve Power/Ground
```
E37 internal logic -> individual solenoid valve drivers (8 channels)
All solenoid valve grounds -> [0.5] -> load ground module -> chassis ground
```

### Inline Connectors

| Connector | Wire Color | Wire Size |
|-----------|------------|-----------|
| EC101(L,1) | -- | 0.5 |
| EC101(L,2) | -- | 0.5 |
| EC102(L,1) | -- | 0.5 |
| EC102(L,2) | -- | 0.5 |
| EC201 | -- | 0.5 |
| EC202 | -- | 0.5 |
| MM01 | -- | 0.5 |
| MM03 | -- | 0.5 |

### Ground Points (SD-96)

| Ground ID | Location | Components |
|-----------|----------|------------|
| G17 | Chassis | ABS pump motor ground, solenoid valve ground bus |

---

## SD-97 -- Component Location Index (ABS / Traction Control System)

<!-- Figure: Component location index for ABS/TCS system, source: SD.pdf page 97 -->

### Components

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C33 | ECM (2.0L) | CL-20 |
| C36-3 | TCM (2.0L) | CL-20 |
| C133-4 | ECM (2.7L) | CL-25 |
| C136-3 | TCM (2.7L) | CL-25 |
| C231 | Stop lamp switch (1.6L) | CL-28 |
| E01 | Left front wheel sensor | CL-10 |
| E37 | ABS control module | CL-12 |
| E39 | Right front wheel sensor | CL-12 |
| M07 | Data link connector | CL-2 |
| M15 | TCS Switch | CL-2 |
| M64 | Left rear wheel sensor | CL-6 |
| M65 | Right rear wheel sensor | CL-6 |

### Connectors

| Connector | Location Page |
|-----------|---------------|
| BCM-CE | CL-8 |
| BEC-IM | CL-8 |
| BCM-KM | CL-8 |
| EC01 | CL-14 |
| EC02 | CL-14 |
| EC101 | CL-14 |
| EC102 | CL-14 |
| EC201 | CL-14 |
| EC202 | CL-14 |
| EM01 | CL-14 |
| MC01 | CL-14 |
| MC02 | CL-14 |
| MC03 | CL-14 |
| MC101 | CL-8 |
| MC102 | CL-8 |
| MC103 | CL-8 |
| MM01 | CL-9 |
| MM03 | CL-9 |

### Grounds

| Ground ID | Location Page |
|-----------|---------------|
| G17 | CL-33 |

---

## SD-98 -- Circuit Description (ABS / Traction Control System)

<!-- Figure: Circuit description text for ABS and TCS systems, source: SD.pdf page 98 -->

### ABS

The Anti-Lock Brake System (ABS) controls the hydraulic brake pressure of all four wheels during braking to prevent the wheels from locking on slippery surfaces, preventing the wheels from locking. The ABS provides the following benefits:

1. Enables steering around obstacles with a greater degree of certainty during panic braking
2. Enables stopping during panic braking while allowing stability and control even on curves
3. In the event of a malfunction in the ABS control system, the system will operate as a normal brake system (safe mode). A diagnostic function and fail-safe system have been included for serviceability.

### TCS

The traction control is a variable system designed to enhance traction during acceleration and cornering. It does so by determining a driving situation, then suppressing spin for any given driving condition. The ABS control module gets signals about the vehicle speed, direction, and road conditions from sensors at the wheels and the steering column. Based on these signals, the control module will determine the optimum amount of wheel spin. Because the vehicle is in a given driving situation, the control module will determine the amount of wheel spin best suited to the driver's needs. If traction control is no longer required, it can be manually cancelled with the TCS switch. The TCS provides the following benefits:

1. When the drive wheel speed exceeds the vehicle speed by a given amount, the ABS control module judges that the drive wheels are slipping, and it outputs the traction control signal to reduce engine power.
2. Based on signals about road load based on frequency changes, the control module detects a rough condition. The control module signals the TCS control valve actuator and ECM to relax engine power, thus improving acceleration efficiency.
3. Based on signals about wheel speed, the control module determines the efficiency of the grip of the tires on the road and signals the TCS control valve actuator and the ECM to relax engine power if necessary, thus improving grip.

---

## SD-99 -- Memo (Blank)

<!-- Figure: Blank memo page, source: SD.pdf page 99 -->

No content.

---

## Master TCM Pinout Table (2.7L V6, from SD-90 through SD-92)

### Connector C136-1

| Pin | Signal Name | Wire Color | Wire Size | Connected To |
|-----|-------------|------------|-----------|-------------|
| -- | A/T pulse generator #1 signal | -- | 0.5R | C130-1 |
| -- | A/T pulse generator #1 ground | -- | 0.5R | C130-1 |
| -- | A/T pulse generator #2 signal | -- | 0.5R | C130-2 |
| -- | A/T pulse generator #2 ground | -- | 0.5R | C130-2 |
| -- | Stop lamp switch input | G/W | 0.85 | C241 stop lamp switch |
| -- | Solenoid #1 control | -- | 0.85 | C104 A/T solenoid |
| -- | Solenoid #2 control | -- | 0.85 | C104 A/T solenoid |
| -- | Underdrive solenoid control | -- | 0.85 | Underdrive solenoid |
| -- | 2nd valve solenoid control | -- | 0.85 | 2nd valve solenoid |
| -- | Low solenoid valve control | -- | 0.85 | Low solenoid valve |

### Connector C136-2

| Pin | Signal Name | Wire Color | Wire Size | Connected To |
|-----|-------------|------------|-----------|-------------|
| -- | Range switch position signals | -- | 0.5R | C101 transaxle range switch |
| -- | Range switch position signals | -- | 0.3P/B | C101 transaxle range switch |
| -- | Oil temperature sensor signal | -- | 0.5 | C108 oil temp sensor |
| -- | Oil temperature sensor ground | -- | 0.5 | C108 oil temp sensor |
| -- | A/T control relay coil control | -- | 0.85 | C137 A/T control relay |
| -- | Sport mode switch | -- | 0.5R | C139 sport mode switch |

### Connector C136-3

| Pin | Signal Name | Wire Color | Wire Size | Connected To |
|-----|-------------|------------|-----------|-------------|
| -- | Vehicle speed (to/from ABS) | -- | 0.5 | ABS module E37 via MC101 |
| -- | Multi-gauge signal | L/G | 0.3L/G | Multi-gauge M42 via MC102 |
| -- | Data link (diagnostic) | L/G | 0.5L/G | M07 data link connector |
| -- | Multipurpose check | -- | 0.5 | M06 check connector |
| -- | ABS communication | -- | 0.5 | ABS module E37 |

---

## Cross-References

### Fuse / Relay Summary

| Fuse/Relay | Rating | Circuit | Sheet |
|------------|--------|---------|-------|
| Fuse 5 (HOT IN ON OR START) | -- | TCM ignition power | SD-90 |
| Fuse 6 (HOT IN ON OR START) | -- | TCM/range switch | SD-90 |
| Fuse 16 | -- | ABS TCS power | SD-95 |
| Fuse 17 | -- | ABS ignition power | SD-94 |
| Fusible link (HOT AT ALL TIMES) | -- | A/T control relay, ABS motor | SD-92, SD-94, SD-96 |
| A/T control relay (C137) | -- | Solenoid valve power | SD-92 |

### All Ground Points

| Ground ID | Location Page | Systems |
|-----------|---------------|---------|
| F06 | -- | TCM ground (SD-90) |
| G17 | CL-33 | ABS motor ground, solenoid ground bus (SD-96) |
| G21 | CL-34 | TCM ground (SD-91) |

### All Connector IDs Referenced

| Connector | Description | Pages Referenced |
|-----------|-------------|-----------------|
| C101 | Transaxle range switch | SD-90 |
| C104 | A/T solenoid valve | SD-90, SD-92 |
| C108 | Oil temperature sensor | SD-92 |
| C130-1 | A/T pulse generator #1 | SD-91 |
| C130-2 | A/T pulse generator #2 | SD-91 |
| C133-1 | ECM | SD-93 |
| C133-4 | ECM | SD-93, SD-94 |
| C136-1 | TCM | SD-90, SD-91, SD-92 |
| C136-2 | TCM | SD-90, SD-92 |
| C136-3 | TCM | SD-91, SD-93, SD-94 |
| C137 | A/T control relay | SD-92 |
| C139 | Sport mode switch | SD-90 |
| C141 | Joint connector | SD-90, SD-91, SD-92 |
| C142 | Joint connector | SD-92 |
| C241 | Stop lamp switch | SD-91 |
| E01 | Left front wheel sensor | SD-95 |
| E37 | ABS control module | SD-91, SD-94, SD-95, SD-96 |
| E39 | Right front wheel sensor | SD-95 |
| E56 | Joint connector | SD-92 |
| M06 | Multipurpose check connector | SD-91 |
| M07 | Data link connector | SD-91, SD-95 |
| M10-1 | Instrument cluster | SD-94 |
| M10-3 | Instrument cluster | SD-90 |
| M15 | TCS switch | SD-94 |
| M42 | Multi-gauge unit | SD-91 |
| M64 | Left rear wheel sensor | SD-95 |
| M65 | Right rear wheel sensor | SD-95 |

---

## Notes

- The 2.7L V6 automatic transaxle uses a 4-speed electronically controlled transmission with the TCM (Transaxle Control Module) managing shift patterns via five solenoid valves.
- The TCM uses THREE connectors: C136-1 (pulse generators, solenoid controls, brake input), C136-2 (range switch positions, oil temp sensor, relay control, sport mode), C136-3 (ABS communication, diagnostics, multi-gauge).
- The ABS/TCS system shares the ABS control module (E37) which communicates with both the ECM (C133-4) and TCM (C136-3) for traction control coordination.
- Four wheel speed sensors (E01, E39, M64, M65) feed the ABS module for anti-lock and traction control functions.
- The A/T control relay (C137) provides switched power to all five solenoid valves; the relay coil is controlled by the TCM.
- **V6 build note:** For the 2.7L, the ECM connector is C133-4 and TCM connectors are C136-1/2/3. The 2.0L uses C33 (ECM) and C36-3 (TCM) per the component location index on SD-97.
