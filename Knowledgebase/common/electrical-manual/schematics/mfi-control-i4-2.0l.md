---
source: SD.pdf
chapter: SD
section: SD-58 to SD-65
pages: 58-65
title: MFI Control System (1.6L I4)
---

# MFI Control System (1.6L I4)

> **Note:** The source pages are titled "MFI CONTROL SYSTEM(1.6L)" in the ETM. The directory was named `mfi-control-i4-2.0l` but the actual schematic content covers the 1.6L I4 (Beta engine, G4GF). The 1.6L uses ECM connector C333 (single large connector) rather than the V6's four C133-x connectors.

**SD-58 -- MFI Control System (1.6L) (1) -- Battery, Ignition Switch, Engine Control Relay, ECM Power**
**SD-59 -- MFI Control System (1.6L) (2) -- E/R Fuse Box, Injectors #1-#4, Cooling Fan Reference**
**SD-60 -- MFI Control System (1.6L) (3) -- E/R Box continued, TPS, ISC Actuator, Canister Purge, Exhaust Manifold**
**SD-61 -- MFI Control System (1.6L) (4) -- CKP, CMP, Oxygen Sensors (Front/Rear), EOBD**
**SD-62 -- MFI Control System (1.6L) (5) -- Ignition Coils, Fuel Pump Relay, MIL, Instrument Cluster, Multi-Gauge**
**SD-63 -- MFI Control System (1.6L) (6) -- Throttle Position Sensor, Accelerator Position Sensor, ECM-90, Data Link Connector**
**SD-64 -- Component Location Index / Circuit Description**
**SD-65 -- Memo (blank)**

---

## SD-58 -- Sheet 1: Battery, Ignition Switch, Engine Control Relay, ECM Power

<!-- Figure: MFI Control System 1.6L sheet 1 - battery/ignition/ECM power distribution, source: SD.pdf page 58 -->

### Power Source / Fuses

| Source | Condition | Fuse/Relay | Rating | Notes |
|--------|-----------|------------|--------|-------|
| Battery | HOT AT ALL TIMES | Fusible link | -- | Main battery feed |
| Battery | HOT AT ALL TIMES | E/R fuse box | -- | Engine room fuse box |
| Ignition switch | HOT IN ON OR START | -- | -- | IG1 feed to ECM |

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Battery | -- | (+) | -- | 2.0R |
| Ignition switch | -- | IG1 | B/W | 1.25B/W |
| Engine control relay (E42) | -- | coil | -- | 0.85 |
| Engine control relay (E42) | -- | contact | -- | 1.25 |
| ECM | C333 | -- | -- | -- |
| Multipurpose check connector (M06) | -- | -- | -- | 0.5 |
| Crankshaft position sensor | C213 | -- | -- | 0.5 |
| EC201 | -- | -- | -- | -- |
| EC202 | -- | -- | -- | 0.85 |
| Crash sensor | -- | -- | -- | -- |

### Circuit Paths

```
Battery (+) -> [2.0R] -> Fusible link -> [R] -> E/R fuse box
  -> Engine control relay (E42) contact side

Ignition switch (IG1) -> [1.25B/W] -> EC201 -> [0.85] -> Engine control relay (E42) coil
  -> ECM C333 (relay control)

Engine control relay (E42) contact -> [1.25] -> EC202 -> ECM C333 (main power)
```

### ECM Pin Connections (SD-58 Bottom Row)

| ECM Connector | ECM Pin | Signal Name | Wire Color | Wire Size |
|---------------|---------|-------------|------------|-----------|
| C333 | -- | Battery power (B+) | R | 1.25 |
| C333 | -- | Ignition power (IG) | B/W | 0.85 |
| C333 | -- | Engine control relay drive | -- | 0.85 |
| C333 | -- | Main relay sense | -- | 0.5 |

### Ground Points (Sheet 1)

| Ground ID | Location | Wire Color | Wire Size |
|-----------|----------|------------|-----------|
| G04 | Engine block | B | 1.0B |

---

## SD-59 -- Sheet 2: E/R Fuse Box, Injectors #1-#4, Cooling Fan Reference

<!-- Figure: MFI Control System 1.6L sheet 2 - injectors and E/R fuse box, source: SD.pdf page 59 -->

### Power Source / Fuses

| Source | Condition | Fuse/Relay | Rating | Notes |
|--------|-----------|------------|--------|-------|
| E/R fuse box | -- | -- | -- | Injector power feed |

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
| Joint connector C246 | -- | -- | -- | -- |
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
```

### ECM Pin Connections (SD-59 Bottom Row)

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
| G26 | Engine block | B | 2.0B |

---

## SD-60 -- Sheet 3: E/R Box continued, Joint Connector, Exhaust Manifold, Catalytic Converter

<!-- Figure: MFI Control System 1.6L sheet 3 - E/R box, joint connector, exhaust components, source: SD.pdf page 60 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| E/R fuse box | -- | -- | -- | -- |
| Joint connector | C246 | -- | -- | 0.50 |
| Joint connector | C231 | -- | -- | -- |
| Exhaust manifold | C214 | -- | -- | -- |
| Catalytic converter | -- | -- | -- | -- |
| EC201 | -- | -- | -- | -- |
| Canister purge valve | C221 | -- | -- | 0.5 |

### Circuit Paths

```
E/R fuse box -> [0.50] -> C246 joint connector
  -> distributes to sensor power circuits

E/R fuse box -> [0.85] -> EC201
  -> [0.50, 0.50, 0.16, 0.50, 0.50/16] -> branches to various ECM inputs
```

### ECM Pin Connections (SD-60 Bottom Row)

| ECM Connector | ECM Pin | Signal Name | Wire Color | Wire Size |
|---------------|---------|-------------|------------|-----------|
| C333 | -- | Sensor power supply | -- | 0.50 |
| C333 | -- | Sensor ground | -- | 0.50 |
| C333 | -- | Canister purge control | -- | 0.5L/W |
| C333 | -- | Exhaust manifold signal | -- | 0.50 |

---

## SD-61 -- Sheet 4: CKP, CMP, Oxygen Sensors (Front/Rear), EOBD

<!-- Figure: MFI Control System 1.6L sheet 4 - crank/cam sensors, O2 sensors, source: SD.pdf page 61 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Crankshaft position sensor | C213 | pin 1 (signal) | -- | 0.5Y |
| Crankshaft position sensor | C213 | pin 2 (ground) | -- | 0.5B |
| Camshaft position sensor | C211 | pin 1 (signal) | -- | 0.5 |
| Camshaft position sensor | C211 | pin 2 (ground) | -- | 0.5B |
| Oxygen sensor (front) | C216 | pin 1 (heater +) | -- | 0.8 |
| Oxygen sensor (front) | C216 | pin 2 (signal) | -- | 0.5 |
| Oxygen sensor (front) | C216 | pin 3 (ground) | -- | 0.5 |
| Oxygen sensor (front) | C216 | pin 4 (heater -) | -- | 0.5 |
| Oxygen sensor (rear) | C222 | pin 1 (heater +) | -- | 0.8 |
| Oxygen sensor (rear) | C222 | pin 2 (signal) | -- | 0.5 |
| Oxygen sensor (rear) | C222 | pin 3 (ground) | -- | 0.5 |
| Oxygen sensor (rear) | C222 | pin 4 (heater -) | -- | 0.5 |
| Throttle position sensor | C212 | -- | -- | 0.5 |
| Joint connector | C246 | -- | -- | -- |
| Manifold absolute pressure sensor | -- | -- | -- | 0.5 |

### Sensor Connector Pinouts

#### Crankshaft Position Sensor (C213)

| Pin | Function | Wire Color | Wire Size | ECM Pin |
|-----|----------|------------|-----------|---------|
| 1 | CKP signal | -- | 0.5Y | C333 |
| 2 | Sensor ground | B | 0.5B | C333 |

#### Camshaft Position Sensor (C211)

| Pin | Function | Wire Color | Wire Size | ECM Pin |
|-----|----------|------------|-----------|---------|
| 1 | CMP signal | -- | 0.5 | C333 |
| 2 | Sensor ground | B | 0.5B | C333 |

#### Oxygen Sensor -- Front (C216)

| Pin | Function | Wire Color | Wire Size | ECM Pin |
|-----|----------|------------|-----------|---------|
| 1 | Heater power (+) | -- | 0.8 | via relay |
| 2 | O2 signal | -- | 0.5 | C333 |
| 3 | O2 sensor ground | -- | 0.5 | C333 |
| 4 | Heater control (-) | -- | 0.5 | C333 |

#### Oxygen Sensor -- Rear (C222)

| Pin | Function | Wire Color | Wire Size | ECM Pin |
|-----|----------|------------|-----------|---------|
| 1 | Heater power (+) | -- | 0.8 | via relay |
| 2 | O2 signal | -- | 0.5 | C333 |
| 3 | O2 sensor ground | -- | 0.5 | C333 |
| 4 | Heater control (-) | -- | 0.5 | C333 |

### Circuit Paths

```
CKP (C213 pin 1) -> [0.5Y] -> C246 -> ECM C333 (CKP signal)
CKP (C213 pin 2) -> [0.5B] -> ECM C333 (CKP ground)

CMP (C211 pin 1) -> [0.5] -> C246 -> ECM C333 (CMP signal)
CMP (C211 pin 2) -> [0.5B] -> ECM C333 (CMP ground)

O2 front (C216) signal -> [0.5] -> ECM C333 (O2 front signal)
O2 front (C216) heater -> [0.5] -> ECM C333 (O2 heater control)
O2 front (C216) heater+ -> [0.8] -> Engine control relay output

O2 rear (C222) signal -> [0.5] -> ECM C333 (O2 rear signal)
O2 rear (C222) heater -> [0.5] -> ECM C333 (O2 rear heater control)
O2 rear (C222) heater+ -> [0.8] -> Engine control relay output
```

### ECM Pin Connections (SD-61 Bottom Row)

| ECM Connector | ECM Pin | Signal Name | Wire Color | Wire Size |
|---------------|---------|-------------|------------|-----------|
| C333 | -- | CKP signal (+) | -- | 0.5Y/W |
| C333 | -- | CKP signal (-) | -- | 0.5B |
| C333 | -- | CMP signal | -- | 0.5 |
| C333 | -- | CMP ground | -- | 0.5 |
| C333 | -- | O2 sensor (front) signal | -- | 0.5 |
| C333 | -- | O2 sensor (front) ground | -- | 0.5 |
| C333 | -- | O2 heater (front) control | -- | 0.5 |
| C333 | -- | O2 sensor (rear) signal | -- | 0.5 |
| C333 | -- | O2 sensor (rear) ground | -- | 0.5 |
| C333 | -- | O2 heater (rear) control | -- | 0.5 |

---

## SD-62 -- Sheet 5: Ignition Coils, Fuel Pump Relay, MIL, Instrument Cluster

<!-- Figure: MFI Control System 1.6L sheet 5 - ignition, fuel pump, MIL lamp, cluster, source: SD.pdf page 62 -->

### Power Source / Fuses

| Source | Condition | Fuse/Relay | Rating | Notes |
|--------|-----------|------------|--------|-------|
| HOT IN ON OR START | Fuse 17 | -- | Via passenger compartment fuse | Ignition coil power |
| HOT IN ON OR START | Fuse 18 | 10A | Fuel pump relay coil | See passenger fuse details |
| -- | Fuse (50A) | 50A | Main ignition coil power | E/R fuse box |

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Ignition coil #1-2 | C218-1 | -- | -- | 0.5L/B |
| Ignition coil #3-4 | C218-2 | -- | -- | 0.5L/B |
| Fuel pump relay | E49 | coil | -- | 0.5 |
| Fuel pump relay | E49 | contact | R | 1.25R |
| MIL (check engine lamp) | -- | -- | -- | 0.5L/B |
| Instrument cluster | M10-2 | pin 3 | -- | 0.5L/B |
| BCM-IM | pin 4 | -- | -- | 0.5R/O |
| BCM-KM | pin 13 | -- | R | 1.25R |
| MC168 | -- | -- | -- | -- |
| MC201 | -- | -- | -- | 0.5L/B |
| MC263 | -- | -- | -- | 0.5L/B |
| MC265 | -- | -- | -- | -- |
| Joint connector C241 | -- | -- | -- | -- |
| Cont. (next page) | -- | -- | -- | -- |
| Multi-gauge (M42) | -- | -- | -- | -- |

### Ignition Coil Configuration

The 1.6L uses a wasted-spark coil pack (2 coils for 4 cylinders):

| Coil Pack | Connector | Fires Cylinders | Wire Color | Wire Size |
|-----------|-----------|-----------------|------------|-----------|
| Coil #1-2 | C218-1 | 1 & 2 | -- | 0.5L/B |
| Coil #3-4 | C218-2 | 3 & 4 | -- | 0.5L/B |

### Circuit Paths

```
Fuse (50A) -> [R, 1.25] -> Joint connector C241 -> [R]
  -> Ignition coil #1-2 (C218-1) power
  -> Ignition coil #3-4 (C218-2) power

ECM C333 -> [0.5L/B] -> Ignition coil #1-2 (C218-1) trigger
ECM C333 -> [0.5L/B] -> Ignition coil #3-4 (C218-2) trigger

Fuse 17 -> BCM-IM pin 4 -> [0.5R/O] -> MC168 -> [0.25R]
  -> Instrument cluster M10-2 pin 3 (MIL CHECK lamp)
  -> [0.5L/B] -> MC201 -> MC263 -> [0.5L/B]
  -> ECM C333 (MIL control)

Fuse 18 (10A) -> [R] -> BCM-KM pin 13 -> [1.25R]
  -> MC168 -> Fuel pump relay (E49) coil
  -> ECM C333 controls relay ground

Fuel pump relay (E49) contact -> [1.25R] -> Fuel sender & fuel pump motor (M55)
```

### ECM Pin Connections (SD-62 Bottom Row)

| ECM Connector | ECM Pin | Signal Name | Wire Color | Wire Size |
|---------------|---------|-------------|------------|-----------|
| C333 | -- | Ignition coil #1-2 trigger | -- | 0.5L/B |
| C333 | -- | Ignition coil #3-4 trigger | -- | 0.5L/B |
| C333 | -- | MIL (check engine) control | -- | 0.5L/B |
| C333 | -- | Fuel pump relay control | -- | 0.5 |
| C333 | -- | Tachometer signal output | -- | 0.3L/B |

### MIL (Check Engine Light) Circuit

```
Fuse 17 -> BCM-IM pin 4 -> [0.5R/O] -> MC168 -> [0.25R]
  -> Instrument cluster M10-2 pin 3 (MIL CHECK lamp)
  -> [0.5L/B] -> MC201 -> MC263 -> [0.5L/B]
  -> C241 joint connector -> ECM C333
```

### Fuel Pump Circuit

```
Fuse 18 (10A) -> [R] -> BCM-KM pin 13 -> [1.25R]
  -> MC168 -> Fuel pump relay (E49) coil
  -> ECM controls relay ground via C333

Fuel pump relay (E49) contact:
  Battery feed -> [R] -> E49 contact -> [1.25R] -> M55 (fuel sender & fuel pump motor)
```

### Ignition Coil Power Feed

```
Fuse (50A) -> [1.25R] -> C241 joint connector -> [R]
  -> Ignition coil #1-2 (C218-1) B+ terminal
  -> Ignition coil #3-4 (C218-2) B+ terminal
  -> Spark plugs (via HT leads, wasted spark)
```

---

## SD-63 -- Sheet 6: Throttle Position Sensor, Accelerator Position Sensor, Data Link, ECM-90

<!-- Figure: MFI Control System 1.6L sheet 6 - TPS, accelerator sensor, DLC, ECM-90, source: SD.pdf page 63 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Throttle position sensor | C212 | pin 1 (ground) | B | 0.5L/W |
| Throttle position sensor | C212 | pin 2 (signal) | -- | 0.5 |
| Throttle position sensor | C212 | pin 3 (supply +5V) | -- | 0.5L/W |
| Accelerator position sensor | C265 | pin 1 | -- | 0.5 |
| Accelerator position sensor | C265 | pin 2 | -- | 0.5/18 |
| Accelerator position sensor | C265 | pin 3 | -- | 0.5 |
| ECM-90 | -- | -- | -- | -- |
| Data link connector (M07) | -- | -- | -- | 0.5L |
| Multipurpose check connector | M06 | -- | -- | 0.5 |
| MC201 | -- | -- | -- | -- |
| Joint connector C244 | -- | -- | -- | -- |

### Sensor Connector Pinouts

#### Throttle Position Sensor (C212)

| Pin | Function | Wire Color | Wire Size | ECM Pin |
|-----|----------|------------|-----------|---------|
| 1 | Sensor ground | B | 0.5L/W | C333 |
| 2 | TPS signal | -- | 0.5 | C333 |
| 3 | 5V supply | -- | 0.5L/W | C333 |

#### Accelerator Position Sensor (C265)

| Pin | Function | Wire Color | Wire Size | ECM Pin |
|-----|----------|------------|-----------|---------|
| 1 | Signal / supply | -- | 0.5 | C333 |
| 2 | Signal | -- | 0.5 | C333 |
| 3 | Ground | -- | 0.5 | C333 |

### Circuit Paths

```
ECM C333 -> [0.5L/W] -> TPS (C212) pin 3 (5V supply)
TPS (C212) pin 2 -> [0.5] -> ECM C333 (TPS signal)
TPS (C212) pin 1 -> [0.5L/W] -> ECM C333 (sensor ground)

ECM C333 -> [0.5] -> Accelerator position sensor (C265)
  -> Signal and ground back to ECM C333

ECM C333 -> [0.5L] -> Data link connector (M07)
  -> K-line (diagnostic communication)

ECM C333 -> [0.5] -> Multipurpose check connector (M06)
```

### ECM Pin Connections (SD-63 Bottom Row)

| ECM Connector | ECM Pin | Signal Name | Wire Color | Wire Size |
|---------------|---------|-------------|------------|-----------|
| C333 | -- | TPS signal | -- | 0.5 |
| C333 | -- | TPS 5V supply | -- | 0.5L/W |
| C333 | -- | TPS/sensor ground | -- | 0.5L/W |
| C333 | -- | Accelerator position signal 1 | -- | 0.5 |
| C333 | -- | Accelerator position signal 2 | -- | 0.5 |
| C333 | -- | Accelerator position ground | -- | 0.5 |
| C333 | -- | K-line (diagnostic) | L | 0.5L |
| C333 | -- | Multipurpose check | -- | 0.5 |

---

## Component Location Index (SD-64)

<!-- Figure: Component location index and circuit description, source: SD.pdf page 64 -->

### Components

| Component ID | Description | Location Page |
|--------------|-------------|---------------|
| C211 | Engine coolant temperature sensor & sender | CL-27 |
| C213 | Crankshaft position sensor | CL-27 |
| C214 | Camshaft position sensor | CL-27 |
| C215 | Oxygen sensor(1) | CL-27 |
| C216-1 | Ignition coil #1 | CL-27 |
| C221 | Canister purge valve | CL-27 |
| C222 | Oxygen sensor(Down) | CL-27 |
| C224-1 | Injector #1 | CL-28 |
| C224-2 | Injector #2 | CL-28 |
| C224-3 | Injector #3 | CL-28 |
| C224-4 | Injector #4 | CL-28 |
| C225 | Manifold absolute pressure sensor | CL-28 |
| C333 | ECM | CL-28 |
| C232 | Joint connector | CL-28 |
| E42 | Engine control relay | CL-12 |
| E49 | Fuel pump relay | CL-12 |
| E56 | Joint connector | CL-12 |
| M06 | Multipurpose check connector | CL-2 |
| M10-1 | Instrument cluster | CL-2 |
| M10-2 | Instrument cluster | CL-2 |
| M34 | Joint connector | CL-2 |
| M42 | Multi gauge unit | CL-4 |
| M55 | Fuel sender & fuel pump motor | CL-5 |

### Connectors

| Connector ID | Location Page |
|--------------|---------------|
| BCM-IM | CL-8 |
| BCM-KM | CL-8 |
| EC201 | CL-14 |
| EM01 | CL-14 |
| MC101 | CL-8 |
| MC102 | CL-8 |
| MC103 | CL-8 |
| MC201 | -- |
| MM02 | CL-9 |

### Grounds

| Ground ID | Location Page |
|-----------|---------------|
| G04 | CL-32 |
| G26 | CL-34 |

---

## Ground Points (All MFI 1.6L Sheets)

| Ground ID | Location | Components Served | Reference |
|-----------|----------|-------------------|-----------|
| G04 | Engine block | ECM ground, sensor grounds | SD-58 |
| G26 | Engine block | Injector grounds, heavy ground | SD-59 |

---

## Master ECM Pinout Summary (1.6L I4 -- Connector C333)

> **Note:** The 1.6L I4 uses a single large ECM connector (C333) rather than the four separate connectors (C133-1 through C133-4) used by the 2.7L V6. Exact pin numbers are difficult to resolve at 150 DPI scan resolution; pin assignments are listed by signal function.

### Power and Ground

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| Battery power (B+) | R | 1.25 | Battery via fusible link |
| Ignition power (IG1) | B/W | 0.85 | Ignition switch |
| Engine control relay drive | -- | 0.85 | E42 relay coil |
| Main relay sense | -- | 0.5 | E42 relay output |
| ECM ground | B | 1.0B | G04 (engine block) |

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
| Ignition coil #1-2 trigger | -- | 0.5L/B | C218-1 |
| Ignition coil #3-4 trigger | -- | 0.5L/B | C218-2 |

### Position Sensors

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| CKP signal (+) | -- | 0.5Y | Crankshaft position sensor C213 pin 1 |
| CKP signal (-) / ground | B | 0.5B | Crankshaft position sensor C213 pin 2 |
| CMP signal | -- | 0.5 | Camshaft position sensor C211 pin 1 |
| CMP ground | B | 0.5B | Camshaft position sensor C211 pin 2 |
| TPS signal | -- | 0.5 | Throttle position sensor C212 pin 2 |
| TPS 5V supply | -- | 0.5L/W | Throttle position sensor C212 pin 3 |
| TPS / sensor ground | -- | 0.5L/W | Throttle position sensor C212 pin 1 |

### Accelerator Position Sensor

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| Accel position signal 1 | -- | 0.5 | C265 pin 1 |
| Accel position signal 2 | -- | 0.5 | C265 pin 2 |
| Accel position ground | -- | 0.5 | C265 pin 3 |

### Oxygen Sensors

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| O2 front signal | -- | 0.5 | C216 pin 2 |
| O2 front ground | -- | 0.5 | C216 pin 3 |
| O2 front heater control | -- | 0.5 | C216 pin 4 |
| O2 rear signal | -- | 0.5 | C222 pin 2 |
| O2 rear ground | -- | 0.5 | C222 pin 3 |
| O2 rear heater control | -- | 0.5 | C222 pin 4 |

### Emissions

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| Canister purge control | -- | 0.5L/W | Canister purge valve C221 |

### Diagnostics and Output

| Signal Name | Wire Color | Wire Size | Source/Destination |
|-------------|------------|-----------|-------------------|
| MIL (check engine) control | -- | 0.5L/B | Instrument cluster M10-2 pin 3 |
| K-line (diagnostic) | L | 0.5L | Data link connector M07 |
| Multipurpose check | -- | 0.5 | Check connector M06 |
| Tachometer signal | -- | 0.3L/B | Instrument cluster |
| A/C compressor signal | -- | 0.5 | A/C relay (see Blower & AC) |
| Cooling fan relay control | -- | 0.5 | See Cooling System |

---

## Relay and Fuse Summary

| Relay/Fuse | Rating | Function | Controlled By |
|------------|--------|----------|--------------|
| E42 (Engine control relay) | -- | Main ECM power relay | ECM C333 (coil drive) |
| E49 (Fuel pump relay) | -- | Fuel pump power | ECM C333 (ground control) |
| Fuse 17 | -- | MIL lamp power (HOT IN ON OR START) | Passenger compartment fuse box |
| Fuse 18 | 10A | Fuel pump relay coil power | Passenger compartment fuse box |
| Fuse (50A) | 50A | Ignition coil power | E/R fuse box |
| Fusible link | -- | Main battery feed | Battery |

---

## Connector Cross-Reference

| Connector | Component | Sheets |
|-----------|-----------|--------|
| C211 | Camshaft position sensor | SD-61 |
| C212 | Throttle position sensor | SD-63 |
| C213 | Crankshaft position sensor | SD-58, SD-61 |
| C214 | Exhaust manifold / CMP reference | SD-60 |
| C216 | Oxygen sensor (front/upstream) | SD-61 |
| C218-1 | Ignition coil #1-2 | SD-62 |
| C218-2 | Ignition coil #3-4 | SD-62 |
| C221 | Canister purge valve | SD-60 |
| C222 | Oxygen sensor (rear/downstream) | SD-61 |
| C224-1 | Injector #1 | SD-59 |
| C224-2 | Injector #2 | SD-59 |
| C224-3 | Injector #3 | SD-59 |
| C224-4 | Injector #4 | SD-59 |
| C225 | Manifold absolute pressure sensor | SD-64 (index) |
| C232 | Joint connector | SD-64 (index) |
| C241 | Joint connector (ignition coil power) | SD-62 |
| C246 | Joint connector (injector power, sensor feeds) | SD-59, SD-60 |
| C265 | Accelerator position sensor | SD-63 |
| C333 | ECM (single large connector) | SD-58 through SD-63 |
| E42 | Engine control relay | SD-58 |
| E49 | Fuel pump relay | SD-62 |
| E56 | Joint connector (E/R box) | SD-64 (index) |
| M06 | Multipurpose check connector | SD-63 |
| M07 | Data link connector | SD-63 |
| M10-1 | Instrument cluster | SD-62 |
| M10-2 | Instrument cluster | SD-62 |
| M34 | Joint connector | SD-64 (index) |
| M42 | Multi-gauge unit | SD-62 |
| M55 | Fuel sender & fuel pump motor | SD-62 |

---

## Key Differences: 1.6L I4 vs 2.7L V6 MFI Systems

| Feature | 1.6L I4 | 2.7L V6 |
|---------|---------|---------|
| ECM connector | C333 (single) | C133-1, C133-2, C133-3, C133-4 (four) |
| Injectors | 4 (C224-1 to C224-4) | 6 (C124-1 to C124-6) |
| Ignition coils | 2 coil packs, wasted spark (C218-1, C218-2) | Individual coils (C118), DIS/COP |
| O2 sensors | 2 (front C216, rear C222) | 6 (3 per bank) |
| Knock sensors | Not shown in these pages | 2 (C123-1, C123-2) |
| CKP connector | C213 | C113 |
| CMP connector | C211 | C114 |
| TPS connector | C212 | C112 |
| Ground points | G04, G26 | G22, G24 |

---

## Circuit Description (from SD-64)

The Multiport Fuel Injection (MFI) control system is an electronic fuel metering system with fuel injection near the inlet port of each cylinder. The amount of fuel injection is determined by the ECM according to engine speed and intake air-flow quantity measured. The emission control system includes the oxygen sensors and catalytic converters. The MFI's three major functions are air-fuel mixture, idle speed, and ignition timing control. Refer to the shop manual, section FL for details.

---

## Notes

- **Scan quality:** 150 DPI scans -- some wire color codes and pin numbers may be approximate where the source image was not fully legible. Cross-reference with the ETM physical copy for critical wiring work.
- **ECM connector:** The 1.6L I4 uses connector ID **C333** (a single multi-pin connector), distinct from the V6 four-connector arrangement (C133-1 through C133-4). All C2xx-series connectors are engine-room components.
- **Wasted spark ignition:** The 1.6L uses two coil packs (C218-1 and C218-2), each firing two cylinders simultaneously (wasted spark). This contrasts with the V6 which has individual coils.
- **Connector ID scheme:** 1.6L I4 components use C2xx series (e.g., C211, C213, C224) while the V6 uses C1xx series (e.g., C111, C113, C124). This is the Hyundai ETM convention for differentiating engine variants.
- **Page SD-65** is a blank MEMO page with no circuit content.
