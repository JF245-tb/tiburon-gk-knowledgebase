---
source: SD.pdf
chapter: SD
section: SD-66 to SD-77
pages: 66-77
title: MFI Control System (1.6L I4)
---

# MFI Control System (1.6L I4)

> **Note:** The source pages are titled "MFI CONTROL SYSTEM(2.0L)" in the ETM (pages SD-66 through SD-75) and "MFI CONTROL SYSTEM (2.7L)" on pages SD-76 through SD-77. The 2.0L content covers the Beta II engine (G4GC). This file is named per the extraction batch; for the earlier 1.6L (G4GF) content on SD-58 to SD-65, see `mfi-control-i4-2.0l.md`. Pages SD-76 and SD-77 overlap with the V6 MFI system covered more completely in `mfi-control-v6.md`.

**SD-66 -- MFI Control System (2.0L) (1) -- Battery, Ignition Switch, ECM Power, Engine Control Relay, Crash Sensor**
**SD-67 -- MFI Control System (2.0L) (2) -- E/R Fuse Box, Injectors #1-#4, Cooling Fan, CKP Reference**
**SD-68 -- MFI Control System (2.0L) (3) -- Sub Fuse Box, Joint Connectors, ISCV, Canister Purge, CKP Sensor**
**SD-69 -- MFI Control System (2.0L) (4) -- Oxygen Sensors (Front/Rear), Camshaft Position Sensor**
**SD-70 -- MFI Control System (2.0L) (5) -- ECT Sensor, TPS, Knock Sensor, Instrument Cluster**
**SD-71 -- MFI Control System (2.0L) (6) -- Ignition Coils, Fuel Pump Relay, MIL, MAP Sensor**
**SD-72 -- MFI Control System (2.0L) (7) -- ABS, Data Link, Multi-Gauge, Multipurpose Check Connector**
**SD-73 -- Component Location Index (2.0L)**
**SD-74 -- Connector/Ground Index and Circuit Description (2.0L)**
**SD-75 -- Memo (blank)**
**SD-76 -- MFI Control System (2.7L) (1) -- Battery, Ignition Switch, ECM Power, Data Link**
**SD-77 -- MFI Control System (2.7L) (2) -- E/R Fuse Box, Injectors #1-#6, Cooling Fan**

---

## SD-66 -- Sheet 1: Battery, Ignition Switch, ECM Power, Engine Control Relay

<!-- Figure: MFI Control System 2.0L sheet 1 - battery/ignition/ECM power distribution, source: SD.pdf page 66 -->

### Power Source / Fuses

| Source | Condition | Fuse/Relay | Rating | Notes |
|--------|-----------|------------|--------|-------|
| Battery | HOT AT ALL TIMES | Fusible link | -- | Main battery feed |
| Battery | HOT AT ALL TIMES | E/R fuse box | -- | Engine room fuse box |
| Ignition switch | HOT IN ON OR START | -- | -- | IG1 feed |

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Battery | -- | (+) | -- | 2.0R |
| Ignition switch | -- | IG1 | B/W | 1.25 |
| Engine control relay (E42) | -- | coil | -- | 0.85 |
| Engine control relay (E42) | -- | contact | -- | 1.25 |
| ECM | C333 | -- | -- | -- |
| Multipurpose check connector | M06 | -- | -- | 0.5 |
| Condenser | C19 | -- | -- | -- |
| Crash sensor | -- | -- | -- | -- |
| Joint connector | EC01 | -- | -- | -- |
| Joint connector | EC02 | -- | -- | -- |
| C-C18-1 | -- | -- | -- | 1.25 |
| C-C18-2 | -- | -- | -- | 0.85 |

### Circuit Paths

```
Battery (+) -> [2.0R] -> Fusible link -> [R] -> E/R fuse box
  -> Engine control relay (E42) contact side

Ignition switch (IG1) -> [1.25, B/W] -> EC01
  -> [0.85] -> Engine control relay (E42) coil
  -> ECM C333 (relay control)

Engine control relay (E42) contact -> [1.25] -> EC02 -> ECM C333 (main power)

Crash sensor -> [0.85] -> ECM C333

Condenser (C19) -> across ECM power pins (noise suppression)
```

### ECM Pin Connections (SD-66 Bottom Row)

| ECM Connector | ECM Pin | Signal Name | Wire Color | Wire Size |
|---------------|---------|-------------|------------|-----------|
| C333 | -- | Battery power (B+) | R | 1.25 |
| C333 | -- | Ignition power (IG) | B/W | 0.85 |
| C333 | -- | Engine control relay drive | -- | 0.85 |
| C333 | -- | Main relay sense | -- | 0.5 |
| C333 | -- | Crash sensor input | -- | 0.85 |

### Ground Points (Sheet 1)

| Ground ID | Location | Wire Color | Wire Size |
|-----------|----------|------------|-----------|
| G04 | Engine block | B | 1.0 |

---

## SD-67 -- Sheet 2: E/R Fuse Box, Injectors #1-#4, Cooling Fan Reference

<!-- Figure: MFI Control System 2.0L sheet 2 - injectors and E/R fuse box, source: SD.pdf page 67 -->

### Power Source / Fuses

| Source | Condition | Fuse/Relay | Rating | Notes |
|--------|-----------|------------|--------|-------|
| E/R fuse box | via Engine control relay | -- | -- | Injector power feed |

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| E/R fuse box | -- | -- | -- | -- |
| Injector #1 | C224-1 | pin 1 (power) | -- | 0.85 |
| Injector #1 | C224-1 | pin 2 (control) | -- | 0.85 |
| Injector #2 | C224-2 | pin 1 (power) | -- | 0.85 |
| Injector #2 | C224-2 | pin 2 (control) | -- | 0.85 |
| Injector #3 | C224-3 | pin 1 (power) | -- | 0.85 |
| Injector #3 | C224-3 | pin 2 (control) | -- | 0.85 |
| Injector #4 | C224-4 | pin 1 (power) | -- | 0.85 |
| Injector #4 | C224-4 | pin 2 (control) | -- | 0.85 |
| Joint connector | C246 | -- | -- | -- |
| Front crankshaft position sensor | -- | -- | -- | -- |
| Knock sensor | -- | -- | -- | -- |
| See Blower & AC Controls (Manual/Auto) | -- | -- | -- | -- |
| See Cooling System | -- | -- | -- | -- |

### Circuit Paths

```
E/R fuse box -> [0.85] -> Joint connector C246
  -> [0.85] -> Injector #1 (C224-1) pin 1
  -> [0.85] -> Injector #2 (C224-2) pin 1
  -> [0.85] -> Injector #3 (C224-3) pin 1
  -> [0.85] -> Injector #4 (C224-4) pin 1

Injector #1 (C224-1) pin 2 -> [0.85] -> ECM C333
Injector #2 (C224-2) pin 2 -> [0.85] -> ECM C333
Injector #3 (C224-3) pin 2 -> [0.85] -> ECM C333
Injector #4 (C224-4) pin 2 -> [0.85] -> ECM C333

Joint connector C140 -> [1.25W] -> ECM C333 (A/C signal)
```

### ECM Pin Connections (SD-67 Bottom Row)

| ECM Connector | ECM Pin | Signal Name | Wire Color | Wire Size |
|---------------|---------|-------------|------------|-----------|
| C333 | -- | Injector #1 control | -- | 0.85 |
| C333 | -- | Injector #2 control | -- | 0.85 |
| C333 | -- | Injector #3 control | -- | 0.85 |
| C333 | -- | Injector #4 control | -- | 0.85 |
| C333 | -- | A/C signal | -- | 0.5 |
| C333 | -- | Cooling fan relay control | -- | 0.5 |

### Cross-References

- "See Blower & AC Controls (Manual/Auto)" -- A/C compressor relay signal
- "See Cooling System" -- Cooling fan relay, coolant temperature

### Ground Points (Sheet 2)

| Ground ID | Location | Wire Color | Wire Size |
|-----------|----------|------------|-----------|
| G19 | Engine block | B | 2.0 |

---

## SD-68 -- Sheet 3: Sub Fuse Box, Joint Connectors, ISCV, Canister Purge, CKP

<!-- Figure: MFI Control System 2.0L sheet 3 - sub fuse box, ISCV, canister purge, CKP sensor, source: SD.pdf page 68 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Sub fuse box | -- | -- | -- | -- |
| Joint connector | C246 | -- | -- | 0.85 |
| Joint connector | C248 | -- | -- | -- |
| Idle speed control valve (ISCV) | -- | -- | -- | 0.85 |
| Canister purge solenoid valve | -- | -- | -- | 0.85 |
| Crankshaft position sensor | C214 | -- | -- | 0.5 |
| EC201 | -- | -- | -- | -- |

### Circuit Paths

```
Sub fuse box -> [0.85] -> Joint connector C246
  -> distributes to sensor power circuits

Sub fuse box -> [0.85] -> ISCV power
ISCV control -> [0.85] -> ECM C333

Canister purge solenoid -> [0.85] -> ECM C333

Crankshaft position sensor (C214):
  CKP signal -> [0.5] -> ECM C333
  CKP ground -> [0.5] -> ECM C333
```

### ECM Pin Connections (SD-68 Bottom Row)

| ECM Connector | ECM Pin | Signal Name | Wire Color | Wire Size |
|---------------|---------|-------------|------------|-----------|
| C333 | -- | ISCV control | -- | 0.85 |
| C333 | -- | Canister purge control | -- | 0.85 |
| C333 | -- | CKP signal (+) | -- | 0.5 |
| C333 | -- | CKP signal (-) / ground | B | 0.5 |
| C333 | -- | Sensor power supply | -- | 0.50 |

---

## SD-69 -- Sheet 4: Oxygen Sensors (Front/Rear), Camshaft Position Sensor

<!-- Figure: MFI Control System 2.0L sheet 4 - oxygen sensors and CMP sensor, source: SD.pdf page 69 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Oxygen sensor (front/upstream) | C216 | pin 1 (heater +) | -- | 0.85 |
| Oxygen sensor (front/upstream) | C216 | pin 2 (signal) | -- | 0.5 |
| Oxygen sensor (front/upstream) | C216 | pin 3 (ground) | -- | 0.5 |
| Oxygen sensor (front/upstream) | C216 | pin 4 (heater -) | -- | 0.5 |
| Oxygen sensor (rear/downstream, EOBD) | C222 | pin 1 (heater +) | -- | 0.85 |
| Oxygen sensor (rear/downstream, EOBD) | C222 | pin 2 (signal) | -- | 0.5 |
| Oxygen sensor (rear/downstream, EOBD) | C222 | pin 3 (ground) | -- | 0.5 |
| Oxygen sensor (rear/downstream, EOBD) | C222 | pin 4 (heater -) | -- | 0.5 |
| Camshaft position sensor | C214 | pin 1 (signal) | -- | 0.5 |
| Camshaft position sensor | C214 | pin 2 (ground) | -- | 0.5 |
| Joint connector | -- | -- | -- | -- |

### Sensor Connector Pinouts

#### Oxygen Sensor -- Front/Upstream (C216)

| Pin | Function | Wire Color | Wire Size | ECM Pin |
|-----|----------|------------|-----------|---------|
| 1 | Heater power (+) | -- | 0.85 | via relay |
| 2 | O2 signal | -- | 0.5 | C333 |
| 3 | O2 sensor ground | -- | 0.5 | C333 |
| 4 | Heater control (-) | -- | 0.5 | C333 |

#### Oxygen Sensor -- Rear/Downstream EOBD (C222)

| Pin | Function | Wire Color | Wire Size | ECM Pin |
|-----|----------|------------|-----------|---------|
| 1 | Heater power (+) | -- | 0.85 | via relay |
| 2 | O2 signal | -- | 0.5 | C333 |
| 3 | O2 sensor ground | -- | 0.5 | C333 |
| 4 | Heater control (-) | -- | 0.5 | C333 |

#### Camshaft Position Sensor (C214)

| Pin | Function | Wire Color | Wire Size | ECM Pin |
|-----|----------|------------|-----------|---------|
| 1 | CMP signal | -- | 0.5 | C333 |
| 2 | Sensor ground | B | 0.5 | C333 |

### Circuit Paths

```
O2 front (C216) heater+ -> [0.85] -> Engine control relay output
O2 front (C216) signal -> [0.5] -> ECM C333 (O2 front signal)
O2 front (C216) heater- -> [0.5] -> ECM C333 (O2 heater control)

O2 rear (C222) heater+ -> [0.85] -> Engine control relay output
O2 rear (C222) signal -> [0.5] -> ECM C333 (O2 rear signal)
O2 rear (C222) heater- -> [0.5] -> ECM C333 (O2 rear heater control)

CMP (C214 pin 1) -> [0.5] -> ECM C333 (CMP signal)
CMP (C214 pin 2) -> [0.5B] -> ECM C333 (CMP ground)
```

### ECM Pin Connections (SD-69 Bottom Row)

| ECM Connector | ECM Pin | Signal Name | Wire Color | Wire Size |
|---------------|---------|-------------|------------|-----------|
| C333 | -- | O2 sensor (front) signal | -- | 0.5 |
| C333 | -- | O2 sensor (front) ground | -- | 0.5 |
| C333 | -- | O2 heater (front) control | -- | 0.5 |
| C333 | -- | O2 sensor (rear) signal | -- | 0.5 |
| C333 | -- | O2 sensor (rear) ground | -- | 0.5 |
| C333 | -- | O2 heater (rear) control | -- | 0.5 |
| C333 | -- | CMP signal | -- | 0.5 |
| C333 | -- | CMP ground | -- | 0.5 |

---

## SD-70 -- Sheet 5: ECT Sensor, TPS, Knock Sensor, Instrument Cluster

<!-- Figure: MFI Control System 2.0L sheet 5 - ECT, TPS, knock sensor, cluster connections, source: SD.pdf page 70 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Engine coolant temp sensor & sender | C211 | pin 1 (signal) | -- | 0.5 |
| Engine coolant temp sensor & sender | C211 | pin 2 (ground) | -- | 0.5 |
| Throttle position sensor | C212 | pin 1 (ground) | B | 0.5 |
| Throttle position sensor | C212 | pin 2 (signal) | -- | 0.5 |
| Throttle position sensor | C212 | pin 3 (+5V supply) | -- | 0.5 |
| Knock sensor | C223 | -- | -- | 0.5 |
| Instrument cluster | M10-1 | -- | -- | 0.5 |
| Joint connector | C246 | -- | -- | -- |
| EC201 | -- | -- | -- | -- |
| MC168 | -- | -- | -- | -- |

### Sensor Connector Pinouts

#### Engine Coolant Temperature Sensor & Sender (C211)

| Pin | Function | Wire Color | Wire Size | ECM Pin |
|-----|----------|------------|-----------|---------|
| 1 | ECT signal | -- | 0.5 | C333 |
| 2 | Sensor ground | -- | 0.5 | C333 |

#### Throttle Position Sensor (C212)

| Pin | Function | Wire Color | Wire Size | ECM Pin |
|-----|----------|------------|-----------|---------|
| 1 | Sensor ground | B | 0.5 | C333 |
| 2 | TPS signal | -- | 0.5 | C333 |
| 3 | 5V supply | -- | 0.5 | C333 |

#### Knock Sensor (C223)

| Pin | Function | Wire Color | Wire Size | ECM Pin |
|-----|----------|------------|-----------|---------|
| 1 | Knock signal | -- | 0.5 | C333 |

### Circuit Paths

```
ECT sensor (C211 pin 1) -> [0.5] -> ECM C333 (ECT signal)
ECT sensor (C211 pin 2) -> [0.5] -> ECM C333 (sensor ground)

ECM C333 -> [0.5] -> TPS (C212) pin 3 (5V supply)
TPS (C212) pin 2 -> [0.5] -> ECM C333 (TPS signal)
TPS (C212) pin 1 -> [0.5B] -> ECM C333 (sensor ground)

Knock sensor (C223) -> [0.5] -> ECM C333 (knock signal)

ECM C333 -> [0.5] -> MC168 -> Instrument cluster M10-1 (tachometer/ECT gauge)
```

### ECM Pin Connections (SD-70 Bottom Row)

| ECM Connector | ECM Pin | Signal Name | Wire Color | Wire Size |
|---------------|---------|-------------|------------|-----------|
| C333 | -- | ECT signal | -- | 0.5 |
| C333 | -- | ECT sensor ground | -- | 0.5 |
| C333 | -- | TPS signal | -- | 0.5 |
| C333 | -- | TPS 5V supply | -- | 0.5 |
| C333 | -- | TPS / sensor ground | B | 0.5 |
| C333 | -- | Knock sensor signal | -- | 0.5 |
| C333 | -- | Instrument cluster output | -- | 0.5 |

---

## SD-71 -- Sheet 6: Ignition Coils, Fuel Pump Relay, MIL, MAP Sensor

<!-- Figure: MFI Control System 2.0L sheet 6 - ignition coils, fuel pump, MIL, MAP sensor, source: SD.pdf page 71 -->

### Power Source / Fuses

| Source | Condition | Fuse/Relay | Rating | Notes |
|--------|-----------|------------|--------|-------|
| HOT IN ON OR START | Fuse 16 | -- | Ignition coil power feed | E/R fuse box |
| HOT IN ON OR START | Fuse 17 | -- | MIL lamp power | Passenger compartment |
| -- | -- | Fuel pump relay | -- | -- |

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Ignition power transistor | -- | -- | -- | 0.85 |
| Ignition coil | C218 | -- | -- | 0.85 |
| Fuel pump relay | E49 | coil | -- | 0.5 |
| Fuel pump relay | E49 | contact | R | 1.25 |
| MIL (check engine lamp) | -- | -- | -- | 0.5 |
| BCM-IM | pin 4 | -- | -- | 0.5 |
| Joint connector | C241 | -- | -- | -- |
| MC201 | -- | -- | -- | 0.5 |
| MC109 | -- | -- | -- | -- |
| Manifold absolute pressure sensor | C225 | -- | -- | 0.5 |

### Ignition Coil Configuration

The 2.0L uses wasted-spark ignition via an ignition power transistor assembly:

| Coil Pack | Connector | Fires Cylinders | Wire Color | Wire Size |
|-----------|-----------|-----------------|------------|-----------|
| Coil #1-4 | C218 | 1 & 4 | -- | 0.85 |
| Coil #2-3 | C218 | 2 & 3 | -- | 0.85 |

### Manifold Absolute Pressure Sensor (C225)

| Pin | Function | Wire Color | Wire Size | ECM Pin |
|-----|----------|------------|-----------|---------|
| 1 | MAP signal | -- | 0.5 | C333 |
| 2 | Sensor ground | -- | 0.5 | C333 |
| 3 | 5V supply | -- | 0.5 | C333 |

### Circuit Paths

```
Fuse 16 -> [0.85] -> Ignition power transistor -> [0.85]
  -> Ignition coil (C218) primary winding
  -> ECM C333 controls firing timing

Fuse 17 -> BCM-IM pin 4 -> [0.5]
  -> Instrument cluster (MIL CHECK lamp)
  -> [0.5] -> MC201 -> ECM C333 (MIL control)

Fuel pump relay (E49):
  Coil: ECM C333 controls relay ground via [0.5]
  Contact: Battery -> [1.25R] -> E49 contact -> [1.25R] -> M55 (fuel sender & pump)

MAP sensor (C225):
  ECM C333 -> [0.5] -> C225 pin 3 (5V supply)
  C225 pin 1 -> [0.5] -> ECM C333 (MAP signal)
  C225 pin 2 -> [0.5] -> ECM C333 (sensor ground)
```

### ECM Pin Connections (SD-71 Bottom Row)

| ECM Connector | ECM Pin | Signal Name | Wire Color | Wire Size |
|---------------|---------|-------------|------------|-----------|
| C333 | -- | Ignition coil #1-4 trigger | -- | 0.85 |
| C333 | -- | Ignition coil #2-3 trigger | -- | 0.85 |
| C333 | -- | MIL (check engine) control | -- | 0.5 |
| C333 | -- | Fuel pump relay control | -- | 0.5 |
| C333 | -- | MAP signal | -- | 0.5 |
| C333 | -- | MAP supply | -- | 0.5 |
| C333 | -- | MAP ground | -- | 0.5 |

### MIL (Check Engine Light) Circuit

```
Fuse 17 -> BCM-IM pin 4 -> [0.5]
  -> Instrument cluster M10-2 pin 3 (MIL CHECK lamp)
  -> [0.5] -> MC201 -> [0.5]
  -> C241 joint connector -> ECM C333
```

### Fuel Pump Circuit

```
Fuel pump relay (E49) coil:
  ECM C333 -> [0.5] -> E49 coil -> Fuse power feed

Fuel pump relay (E49) contact:
  Battery feed -> [R] -> E49 contact -> [1.25R] -> M55 (fuel sender & fuel pump motor)
```

---

## SD-72 -- Sheet 7: ABS, Data Link, Multi-Gauge, Multipurpose Check Connector

<!-- Figure: MFI Control System 2.0L sheet 7 - ABS module, data link, multi-gauge, source: SD.pdf page 72 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| ABS control module | E37 | -- | -- | 0.5 |
| Data link connector | M07 | -- | -- | 0.5 |
| Multipurpose check connector | M06 | -- | -- | 0.5 |
| Multi-gauge unit | M42 | -- | -- | 0.5 |
| Instrument cluster | M10-1 | -- | -- | 0.3 |
| MC109 | -- | -- | -- | -- |
| MC201 | -- | -- | -- | -- |
| MC265 | -- | -- | -- | -- |
| EC201-AB | -- | -- | -- | -- |
| EC201-BB | -- | -- | -- | -- |

### Circuit Paths

```
ECM C333 -> [0.5] -> Data link connector (M07) (K-line diagnostic)

ECM C333 -> [0.5] -> Multipurpose check connector (M06)

ABS control module (E37) -> [0.5] -> MC109 -> ECM C333 (vehicle speed signal)

ECM C333 -> [0.3] -> MC109 -> Instrument cluster M10-1 (tachometer signal)

ECM C333 -> [0.5] -> MC265 -> Multi-gauge unit M42

ECM C333 -> [0.5] -> EC201-AB/BB (diagnostic data bus)
```

### ECM Pin Connections (SD-72 Bottom Row)

| ECM Connector | ECM Pin | Signal Name | Wire Color | Wire Size |
|---------------|---------|-------------|------------|-----------|
| C333 | -- | K-line (diagnostic) | -- | 0.5 |
| C333 | -- | Multipurpose check | -- | 0.5 |
| C333 | -- | Vehicle speed (from ABS) | -- | 0.5 |
| C333 | -- | Tachometer signal output | -- | 0.3 |
| C333 | -- | Multi-gauge data | -- | 0.5 |

---

## Component Location Index (SD-73)

<!-- Figure: Component location index for MFI Control System 2.0L, source: SD.pdf page 73 -->

### Components

| Component ID | Description | Location Page |
|--------------|-------------|---------------|
| C11 | Engine coolant temperature sensor & sender | CL-18 |
| C12 | Throttle position sensor | CL-18 |
| C13 | Crankshaft position sensor | CL-19 |
| C14 | Camshaft position sensor | CL-19 |
| C15 | Oxygen sensor(1) | CL-19 |
| C15-6 | Ignition coil #1 | CL-19 |
| C19 | Condenser | CL-19 |
| C21 | Canister purge valve | CL-19 |
| C22 | Oxygen sensor(Down) (EOBD) | CL-19 |
| C23 | Knock sensor | CL-19 |
| C24-1 | Injector #1 | CL-20 |
| C24-2 | Injector #2 | CL-20 |
| C24-3 | Injector #3 | CL-20 |
| C24-4 | Injector #4 | CL-20 |
| C25 | Manifold absolute pressure sensor | CL-20 |
| C28 | A/C compressor | CL-20 |
| C33 | ECM | CL-20 |
| C36-3 | TCM | CL-20 |
| C37 | A/T control relay | CL-20 |
| C41 | Joint connector | CL-21 |
| C42 | Joint connector | CL-21 |
| E39 | Right front wheel sensor | CL-21 |
| E41 | Fuel pump relay | CL-12 |
| E42 | Engine control relay | CL-12 |
| E44 | A/C relay | CL-12 |
| E56 | Joint connector | CL-12 |
| M06 | Multipurpose check connector | CL-2 |
| M07 | Data link connector | CL-2 |
| M10-1 | Instrument cluster | CL-2 |
| M10-2 | Instrument cluster | CL-2 |
| M24 | Joint connector | CL-4 |
| M42 | Multi gauge unit | CL-4 |
| M55 | Fuel sender & fuel pump motor | CL-5 |

---

## Connector and Ground Index (SD-74)

<!-- Figure: Connector/ground index and circuit description for MFI Control System 2.0L, source: SD.pdf page 74 -->

### Connectors

| Connector ID | Location Page |
|--------------|---------------|
| BCM-IM | CL-8 |
| EC01 | CL-14 |
| EC02 | CL-14 |
| EM01 | CL-14 |
| MC01 | CL-8 |
| MC02 | CL-8 |
| MC03 | CL-8 |
| MM01 | CL-9 |
| MM02 | CL-9 |

### Grounds

| Ground ID | Location Page |
|-----------|---------------|
| G04 | CL-32 |
| G19 | CL-34 |

---

## SD-76 -- Sheet 1 (V6): Battery, Ignition Switch, ECM Power, Data Link

<!-- Figure: MFI Control System 2.7L sheet 1 - battery/ignition/ECM power/data link, source: SD.pdf page 76 -->

> **Note:** Pages SD-76 and SD-77 begin the 2.7L V6 MFI system. For complete V6 coverage (SD-78 through SD-85), see `mfi-control-v6.md`.

### Power Source / Fuses

| Source | Condition | Fuse/Relay | Rating | Notes |
|--------|-----------|------------|--------|-------|
| Battery | HOT AT ALL TIMES | Fusible link | -- | Main battery feed |
| Battery | HOT AT ALL TIMES | E/R fuse box | -- | Engine room fuse box |
| Ignition switch | HOT IN ON OR START | -- | -- | IG1 feed |

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Battery | -- | (+) | -- | 2.0R |
| Ignition switch | -- | IG1 | -- | 1.25 |
| Engine control relay (E42) | -- | coil | -- | 0.85 |
| Engine control relay (E42) | -- | contact | -- | 1.25 |
| ECM | C133-1 | -- | -- | -- |
| ECM | C133-2 | -- | -- | -- |
| Multipurpose check connector | M06 | -- | -- | 0.5 |
| Data link connector | M07 | -- | -- | 0.5 |
| Multipurpose check connector | -- | -- | -- | 0.5 |
| Condenser | -- | -- | -- | -- |
| EC101 | -- | -- | -- | -- |
| EC161 | -- | -- | -- | -- |
| Crash sensor | -- | -- | -- | -- |
| Joint connector | EC101-21 | -- | -- | -- |

### Circuit Paths

```
Battery (+) -> [2.0R] -> Fusible link -> [R] -> E/R fuse box
  -> Engine control relay (E42) contact side

Ignition switch (IG1) -> [1.25] -> EC101
  -> [0.85] -> Engine control relay (E42) coil
  -> ECM C133-1 (relay control)

Engine control relay (E42) contact -> [1.25] -> EC161 -> ECM C133-1 (main power)

ECM -> [0.5] -> Data link connector (M07)
ECM -> [0.5] -> Multipurpose check connector (M06)
```

### ECM Pin Connections (SD-76 Bottom Row)

| ECM Connector | ECM Pin | Signal Name | Wire Color | Wire Size |
|---------------|---------|-------------|------------|-----------|
| C133-1 | -- | Battery power (B+) | R | 1.25 |
| C133-1 | -- | Ignition power (IG) | -- | 0.85 |
| C133-1 | -- | Engine control relay drive | -- | 0.85 |
| C133-1 | -- | Crash sensor input | -- | 0.85 |
| C133-1 | -- | K-line (diagnostic) | -- | 0.5 |
| C133-1 | -- | Multipurpose check | -- | 0.5 |

### Ground Points

| Ground ID | Location | Wire Color | Wire Size |
|-----------|----------|------------|-----------|
| G22 | Engine block | B | 2.0 |

---

## SD-77 -- Sheet 2 (V6): E/R Fuse Box, Injectors #1-#6, Cooling Fan

<!-- Figure: MFI Control System 2.7L sheet 2 - injectors and E/R fuse box, source: SD.pdf page 77 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| E/R fuse box | -- | -- | -- | -- |
| Injector #1 | C124-1 | pin 1 (power) | -- | 0.85 |
| Injector #1 | C124-1 | pin 2 (control) | -- | 0.85 |
| Injector #2 | C124-2 | pin 1 (power) | -- | 0.85 |
| Injector #2 | C124-2 | pin 2 (control) | -- | 0.85 |
| Injector #3 | C124-3 | pin 1 (power) | -- | 0.85 |
| Injector #3 | C124-3 | pin 2 (control) | -- | 0.85 |
| Injector #4 | C124-4 | pin 1 (power) | -- | 1.25W |
| Injector #4 | C124-4 | pin 2 (control) | -- | 0.85 |
| Injector #5 | C124-5 | pin 1 (power) | -- | 0.85 |
| Injector #5 | C124-5 | pin 2 (control) | -- | 0.85 |
| Injector #6 | C124-6 | pin 1 (power) | -- | 0.85 |
| Injector #6 | C124-6 | pin 2 (control) | -- | 0.85 |
| Joint connector | C140 | -- | -- | -- |
| EC241 | -- | -- | -- | -- |
| See Cooling System | -- | -- | -- | -- |
| See Blower & AC Controls | -- | -- | -- | -- |

### Circuit Paths

```
E/R fuse box -> [1.25W] -> EC241 -> Joint connector C140
  -> [0.85] -> Injector #1 (C124-1) pin 1
  -> [0.85] -> Injector #2 (C124-2) pin 1
  -> [0.85] -> Injector #3 (C124-3) pin 1
  -> [0.85] -> Injector #4 (C124-4) pin 1
  -> [0.85] -> Injector #5 (C124-5) pin 1
  -> [0.85] -> Injector #6 (C124-6) pin 1

Injector #1 (C124-1) pin 2 -> [0.85] -> ECM C133-1
Injector #2 (C124-2) pin 2 -> [0.85] -> ECM C133-1
Injector #3 (C124-3) pin 2 -> [0.85] -> ECM C133-1
Injector #4 (C124-4) pin 2 -> [0.85] -> ECM C133-1
Injector #5 (C124-5) pin 2 -> [0.85] -> ECM C133-1
Injector #6 (C124-6) pin 2 -> [0.85] -> ECM C133-1

A/C signal -> [0.5] -> ECM (see Blower & AC Controls)
Cooling fan -> [0.5] -> ECM (see Cooling System)
```

### ECM Pin Connections (SD-77 Bottom Row)

| ECM Connector | ECM Pin | Signal Name | Wire Color | Wire Size |
|---------------|---------|-------------|------------|-----------|
| C133-1 | -- | Injector #1 control | -- | 0.85 |
| C133-1 | -- | Injector #2 control | -- | 0.85 |
| C133-1 | -- | Injector #3 control | -- | 0.85 |
| C133-1 | -- | Injector #4 control | -- | 0.85 |
| C133-1 | -- | Injector #5 control | -- | 0.85 |
| C133-1 | -- | Injector #6 control | -- | 0.85 |
| C133-1 | -- | A/C signal | -- | 0.5 |
| C133-1 | -- | Cooling fan relay | -- | 0.5 |

### Cross-References

- "See Cooling System" -- Cooling fan relay, coolant temperature
- "See Blower & AC Controls" -- A/C compressor relay signal

---

## Ground Points (All Sheets)

| Ground ID | Location | Components Served | Reference |
|-----------|----------|-------------------|-----------|
| G04 | Engine block | ECM ground, sensor grounds (2.0L) | SD-66 |
| G19 | Engine block | Injector grounds, heavy ground (2.0L) | SD-67 |
| G22 | Engine block | ECM ground (2.7L) | SD-76 |

---

## Master ECM Pinout Summary (2.0L I4 -- Connector C333)

> **Note:** The 2.0L I4 uses a single large ECM connector (C333) like the 1.6L. Exact pin numbers are difficult to resolve at 150 DPI scan resolution; pin assignments are listed by signal function.

### Power and Ground

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| Battery power (B+) | R | 1.25 | Battery via fusible link |
| Ignition power (IG1) | B/W | 0.85 | Ignition switch |
| Engine control relay drive | -- | 0.85 | E42 relay coil |
| Main relay sense | -- | 0.5 | E42 relay output |
| ECM ground | B | 1.0 | G04 (engine block) |
| Crash sensor input | -- | 0.85 | Crash sensor |

### Fuel Injection

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| Injector #1 control | -- | 0.85 | C224-1 pin 2 |
| Injector #2 control | -- | 0.85 | C224-2 pin 2 |
| Injector #3 control | -- | 0.85 | C224-3 pin 2 |
| Injector #4 control | -- | 0.85 | C224-4 pin 2 |
| Fuel pump relay control | -- | 0.5 | E49 relay coil |

### Ignition

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| Ignition coil #1-4 trigger | -- | 0.85 | C218 via power transistor |
| Ignition coil #2-3 trigger | -- | 0.85 | C218 via power transistor |

### Position Sensors

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| CKP signal (+) | -- | 0.5 | Crankshaft position sensor C214 |
| CKP signal (-) / ground | B | 0.5 | Crankshaft position sensor C214 |
| CMP signal | -- | 0.5 | Camshaft position sensor C214 |
| CMP ground | B | 0.5 | Camshaft position sensor C214 |
| TPS signal | -- | 0.5 | Throttle position sensor C212 pin 2 |
| TPS 5V supply | -- | 0.5 | Throttle position sensor C212 pin 3 |
| TPS / sensor ground | B | 0.5 | Throttle position sensor C212 pin 1 |

### Temperature and Pressure Sensors

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| ECT signal | -- | 0.5 | Engine coolant temp sensor C211 pin 1 |
| ECT sensor ground | -- | 0.5 | Engine coolant temp sensor C211 pin 2 |
| MAP signal | -- | 0.5 | Manifold absolute pressure sensor C225 pin 1 |
| MAP sensor ground | -- | 0.5 | MAP sensor C225 pin 2 |
| MAP 5V supply | -- | 0.5 | MAP sensor C225 pin 3 |
| Knock sensor signal | -- | 0.5 | Knock sensor C223 |

### Oxygen Sensors

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| O2 front signal | -- | 0.5 | C216 pin 2 |
| O2 front ground | -- | 0.5 | C216 pin 3 |
| O2 front heater control | -- | 0.5 | C216 pin 4 |
| O2 rear signal | -- | 0.5 | C222 pin 2 |
| O2 rear ground | -- | 0.5 | C222 pin 3 |
| O2 rear heater control | -- | 0.5 | C222 pin 4 |

### Idle and Emissions

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| ISCV control | -- | 0.85 | Idle speed control valve |
| Canister purge control | -- | 0.85 | Canister purge solenoid |

### Diagnostics and Output

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| MIL (check engine) control | -- | 0.5 | Instrument cluster M10-2 pin 3 |
| K-line (diagnostic) | -- | 0.5 | Data link connector M07 |
| Multipurpose check | -- | 0.5 | Check connector M06 |
| Tachometer signal | -- | 0.3 | Instrument cluster M10-1 |
| Vehicle speed (from ABS) | -- | 0.5 | ABS control module E37 |
| A/C compressor signal | -- | 0.5 | A/C relay (see Blower & AC) |
| Cooling fan relay control | -- | 0.5 | See Cooling System |

---

## Relay and Fuse Summary

| Relay/Fuse | Rating | Function | Controlled By |
|------------|--------|----------|--------------|
| E42 (Engine control relay) | -- | Main ECM power relay | ECM C333 (coil drive) |
| E49 (Fuel pump relay) | -- | Fuel pump power | ECM C333 (ground control) |
| E44 (A/C relay) | -- | A/C compressor | ECM signal |
| Fuse 16 | -- | Ignition coil power | E/R fuse box |
| Fuse 17 | -- | MIL lamp power (HOT IN ON OR START) | Passenger compartment fuse box |
| Fusible link | -- | Main battery feed | Battery |

---

## Connector Cross-Reference

| Connector | Component | Sheets |
|-----------|-----------|--------|
| C211 | Engine coolant temperature sensor & sender | SD-70 |
| C212 | Throttle position sensor | SD-70 |
| C214 | Crankshaft position sensor / Camshaft position sensor | SD-68, SD-69 |
| C216 | Oxygen sensor (front/upstream) | SD-69 |
| C218 | Ignition coil assembly | SD-71 |
| C221 | Canister purge solenoid | SD-68 |
| C222 | Oxygen sensor (rear/downstream, EOBD) | SD-69 |
| C223 | Knock sensor | SD-70 |
| C224-1 | Injector #1 | SD-67 |
| C224-2 | Injector #2 | SD-67 |
| C224-3 | Injector #3 | SD-67 |
| C224-4 | Injector #4 | SD-67 |
| C225 | Manifold absolute pressure sensor | SD-71 |
| C241 | Joint connector (ignition coil power) | SD-71 |
| C246 | Joint connector (injector power, sensor feeds) | SD-67, SD-68 |
| C248 | Joint connector | SD-68 |
| C333 | ECM (single large connector) | SD-66 through SD-72 |
| E37 | ABS control module | SD-72 |
| E42 | Engine control relay | SD-66 |
| E44 | A/C relay | SD-73 (index) |
| E49 | Fuel pump relay | SD-71 |
| E56 | Joint connector (E/R box) | SD-73 (index) |
| M06 | Multipurpose check connector | SD-72 |
| M07 | Data link connector | SD-72 |
| M10-1 | Instrument cluster | SD-70, SD-72 |
| M10-2 | Instrument cluster | SD-71 |
| M42 | Multi-gauge unit | SD-72 |
| M55 | Fuel sender & fuel pump motor | SD-71 |

---

## Key Differences: 2.0L I4 vs 1.6L I4 vs 2.7L V6 MFI Systems

| Feature | 1.6L I4 (SD-58 to SD-65) | 2.0L I4 (SD-66 to SD-74) | 2.7L V6 (SD-76 to SD-85) |
|---------|--------------------------|--------------------------|--------------------------|
| ECM connector | C333 (single) | C333 (single) | C133-1 to C133-4 (four) |
| Injectors | 4 (C224-1 to C224-4) | 4 (C224-1 to C224-4) | 6 (C124-1 to C124-6) |
| Ignition | 2 coil packs, wasted spark | Power transistor + coil, wasted spark | Individual coils (C118), DIS/COP |
| O2 sensors | 2 (front C216, rear C222) | 2 (front C216, rear C222 EOBD) | 6 (3 per bank) |
| Knock sensors | Not shown | 1 (C223) | 2 (C123-1, C123-2) |
| MAP sensor | C225 (in SD-62 index) | C225 (SD-71) | Uses MAF (C125) instead |
| CKP connector | C213 | C214 | C113 |
| CMP connector | C211 | C214 | C114 |
| TPS connector | C212 | C212 | C112 |
| ECT connector | C211 | C211 | C111 |
| Ground points | G04, G26 | G04, G19 | G22, G24 |
| ISCV | Not shown in these pages | ISCV on SD-68 | ISC actuator C126 |
| Condenser | Not shown | C19 (SD-66) | Present |

---

## Circuit Description (from SD-74)

The Multiport Fuel Injection (MFI) control system is an electronic fuel metering system with fuel injectors near the inlet port of each cylinder. The amount of fuel injection is determined by the ECM according to engine speed and intake air-flow quantity measured. The emission control system includes the oxygen sensors and catalytic converters. The MFI's three major functions are air-fuel mixture, idle speed, and ignition timing control. Refer to the shop manual, section FL for details.

---

## Notes

- **Scan quality:** 150 DPI scans -- some wire color codes and pin numbers may be approximate where the source image was not fully legible. Cross-reference with the ETM physical copy for critical wiring work.
- **ECM connector:** The 2.0L I4 uses connector ID **C333** (a single multi-pin connector), same as the 1.6L, and distinct from the V6 four-connector arrangement (C133-1 through C133-4).
- **Wasted spark ignition:** The 2.0L uses an ignition power transistor module feeding a coil pack assembly (C218). This differs from the 1.6L's direct two-coil-pack arrangement and the V6's individual COP coils.
- **Connector ID scheme:** 2.0L I4 components use C2xx series (e.g., C211, C214, C224) while the V6 uses C1xx series (e.g., C111, C113, C124). This is the Hyundai ETM convention for differentiating engine variants.
- **MAP vs MAF:** The 2.0L I4 uses a MAP sensor (C225) for load sensing, while the 2.7L V6 uses a MAF sensor (C125).
- **Page SD-75** is a blank MEMO page with no circuit content.
- **Pages SD-76 and SD-77** begin the 2.7L V6 MFI section (sheets 1-2) covering power distribution and injectors. The remaining V6 sheets (SD-78 through SD-85) are in `mfi-control-v6.md`.
