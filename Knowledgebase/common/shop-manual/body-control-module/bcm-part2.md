---
source: BODY CONTROL MODULE.pdf
chapter: BCM
section: BE-26 to BE-50
pages: 26-50
engine: All
title: Body Control Module - Part 2
vehicle: 2003 Hyundai Tiburon (GK)
---

# Troubleshooting Procedure for BCM - Part 2

## Turn Signal Lamp Troubleshooting (continued)

### 5) One turn signal lamp does not work

| Symptom | Step 1 | Step 2 | Step 3 |
|---|---|---|---|
| Poor operation of front left turn signal lamp | Bulb burnt | BCM-CE (2) - E06 (1) Check | M14 (2) - G10(Ground) Check |
| Poor operation of left cluster | Bulb burnt in cluster | BCM-MP (2) - M10-2 (1) Check | M10-1 (2) - G11(Ground) Check |
| Poor operation of rear left turn signal lamp | Bulb burnt | BCM-FF (3) - M84 (1) Check | M84 (2) - G06(Ground) Check |
| Poor operation of front right turn signal lamp | Bulb burnt | BCM-CE (3) - E01 (1) Check | E12 (2) - G16(Ground) Check |
| Poor operation of right cluster | Bulb burnt in cluster | BCM-MP (2) - M15-1 (3) Check | M15-1 (2) - G11(Ground) Check |
| Poor operation of rear right turn signal lamp | Bulb burnt | BCM-FF (3) - M84 (1) Check | M84 (2) - G06(Ground) Check |

<!-- Figure: Turn signal lamp troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 26 -->

---

## Power Window

### Power Window Circuit Diagram (1)

Power is supplied from the battery through Fuse F19 (in the junction fuse block) to the BCM and power window relay. The BCM controls the power window relay via connector BCM-G7.

<!-- Figure: Power window circuit diagram (1) showing battery feed through fuse, BCM, power window relay, and connections to left power window switch, source: BODY CONTROL MODULE.pdf page 27 -->

**Circuit path:**
- Battery --> Fuse F19 --> Power Window Relay --> BCM-MR / BCM-G7
- Wire gauges: 2.0 sq mm main feeds, 3.0 sq mm to motor circuits
- Grounds: G12, G11

### Power Window Circuit Diagram (2)

<!-- Figure: Power window circuit diagram (2) showing left power window switch, right power window switch, left power switch connector, driver window motor, passenger window motor, and associated wiring, source: BODY CONTROL MODULE.pdf page 28 -->

**Circuit connections:**
- Left Power Window Switch connects to driver and passenger window motors
- Right Power Window Switch controls passenger side independently
- See Illumination connections from BCM
- Left Power Outside Mirror Folding motor connection shown
- Wire gauges: 2.0 sq mm for switch feeds, 2.0Y for motor drives, 3.0 sq mm for power feeds
- Grounds: G01, G11

### Power Window - BCM Diagnostic Procedure

#### 1. Function explanation

1. BCM controls power supply to power window switch when IGN is ON state, and it keeps supplying power to the switch for 30 seconds after IGN is off.
2. If the door is opened within the 30 seconds, it turns off immediately.

#### 2. Input/output signal

- Fuse: F19 (20A)
- Output: Power window output (G2)

#### 3. Related Hi-scan(pro) failure diagnosis

Check BCM input condition against key state: ON or ST, key state = ON.

**1.1 Input/Output Monitoring**

Select "01.POWER" and press [ENTER].

| Parameter | Value |
|---|---|
| MODEL | HD COUPE, 2000MY ALL |
| SYSTEM | BODY CONTROL MODULE |

Menu items:
1. 01. POWER
2. 02. FLASH
3. 03. LAMP
4. 04. DOOR
5. 05. LOCK & FOLDING
6. 06. WIPER
7. 07. ETC

**1.11 Current Data**

| Parameter | Value |
|---|---|
| DOOR WARNING SW | OFF |
| KEY STATE - ACC | OFF |
| KEY STATE - ON/ST | OFF |
| KEY STATE - ON | OFF |
| GENERATOR VOLTAGE | 0.0 V |
| STARTER INHIBIT OUTPUT | OFF |

<!-- Figure: Hi-scan diagnostic screens for power window, source: BODY CONTROL MODULE.pdf page 29 -->

**Actuator Inspection:**

Select "01.POWER" and press [ENTER]. Select "02.OUTPUT ACTUATION" and press [ENTER]. Then, the following screen will be displayed. Check output condition against power window relay.

**1.1 Input/Output Monitoring (after 02.OUTPUT ACTUATION)**

| Parameter | Value |
|---|---|
| MODEL | HD COUPE, 2000MY ALL |
| SYSTEM | BODY CONTROL MODULE |
| 01. INPUT ACTUATION | |

### Power Window Actuation Test

**1.11 Actuation Test**

| Parameter | Value |
|---|---|
| POWER WINDOW POWER OFF | |
| DURATION | UNTIL STOP KEY |
| METHOD | ACTIVATION |
| CONDITION | IG. KEY ON |

PRESS [STRT], IF YOU ARE READY!

<!-- Figure: Hi-scan actuation test screen for power window, source: BODY CONTROL MODULE.pdf page 30 -->

#### 4. Expected failure symptoms

Power is not supplied to power window switch.

> **NOTE:** As for the power window motor malfunction, refer to power window motor circuit [Refer to workshop manual (BE-75 to BE-77)]

### 5. Actions by failure symptoms

**Power is not supplied to power window switch.**

```
Fuse (F19) short check
  |
  |-- NG --> Fuse replacement
  |
  OK
  |
  v
[Power] Input monitoring
  |
  |-- NG --> Check power supply circuit
  |
  OK
  |
  v
[Power window power]
Is the 12V applied to BCM G2
terminal and both ends of grounding
when output signal is forced driven?
  |
  |-- NG --> 1. Power window relay malfunction --> Relay replacement
  |          2. BCM malfunction --> BCM replacement
  |
  OK
  |
  v
BCM-GF (2) - MD01 (3) - D05 (8) Check
```

<!-- Figure: Power window troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 31 -->

---

## Ignition Key Hole Illumination

### Key Remind Switch Circuit Diagram

<!-- Figure: Key remind switch circuit diagram showing BCM connections through CRASH-IM connector, gas immobilizer control system, key remind switch, ignition switch connector, and associated wiring, source: BODY CONTROL MODULE.pdf page 32 -->

**Circuit connections:**
- Battery feed through Fuse F18
- BCM-JM connector to CRASH-IM connector
- Gas Immobilizer Control System connection
- Key Reminder Switch with connector
- Key Hole Illumination lamp (M05)
- Wire gauges: 2.0 sq mm main feeds, 1.0 sq mm signal wires, 0.85 sq mm for illumination
- Grounds: G11, G01

### Key Hole Illumination - BCM Diagnostic Procedure

#### 1. Function explanation

When driver's side door is opened and closed, ignition key hole illumination turns on for 10 seconds so that the driver can insert the key.

#### 2. Input/output signal

- Fuse: F18 (10A)
- Input: Driver's side door switch (E9), Passenger's side door switch (E4)
- Output: Key hole illumination (J2)

#### 3. Related Hi-scan(pro) failure diagnosis

**Input/output monitoring:**

Select "04.DOOR" and press [ENTER]. Then, the following screen will be displayed. Check BCM output condition against key hole illumination.

**1.1 Input/Output Monitoring**

| Parameter | Value |
|---|---|
| MODEL | HD COUPE, 2000MY ALL |
| SYSTEM | BODY CONTROL MODULE |

**1.11 Current Data**

| Parameter | Value |
|---|---|
| DRIVER DOOR SW | CLOSED |
| PASSENGER DOOR SW | CLOSED |
| DOOR BASE | CLOSED |
| KEY HOLE ILLUMINATION | OFF |
| ROOM LAMP | 0 % |
| HOOD SW | CLOSED |
| TAIL GATE OPEN SW | CLOSED |
| TAIL GATE UNLOCK INPUT | OFF |

**Actuator Inspection:**

Select "02.OUTPUT ACTUATION" and press [ENTER]. Perform forced drive against key hole illumination.

**1.2 Actuation Test**

| Parameter | Value |
|---|---|
| MODEL | HD COUPE, 2000MY ALL |
| SYSTEM | BODY CONTROL MODULE |
| 01. INPUT ACTUATION | |

**1.11 Actuation Test**

| Parameter | Value |
|---|---|
| KEY HOLE ILLUMINATION | |
| DURATION | 4 UNTIL STOP KEY |
| METHOD | ACTIVATION |
| CONDITION | IG. KEY ON |

PRESS [STRT], IF YOU ARE READY!

<!-- Figure: Hi-scan key hole illumination diagnostic screens, source: BODY CONTROL MODULE.pdf page 33 -->

#### 4. Expected failure symptoms

Key hole illumination does not work.

### 5. Actions by failure symptoms

**Key hole illumination does not work.**

```
Key reminder function check
  |
  |-- NO --> Key reminder function check
  |
  YES
  |
  v
Fuse short check (F18)
  |
  |-- NG --> Fuse replacement
  |
  OK
  |
  v
[Key hole illumination] Output monitoring
  |
  |-- NO --> BCM malfunction
  |
  YES
  |
  v
Output circuit wiring short of key
hole illumination output circuit
  |
  Key hole illumination malfunction
  |
  +--> 1. BCM-JM (3) - M05 (1) Check
  |    2. Check whether 12V is applied to terminal M05 (2)
  |
  +--> Apply 12V to both ends of key hole
       illumination bulbs, and check the operation.
```

**[M05] Connector terminal of key reminder switch:**

| Pin | Function |
|---|---|
| 1 | BCM-JM output |
| 2 | 12V supply |

<!-- Figure: Key hole illumination troubleshooting flowchart and M05 connector, source: BODY CONTROL MODULE.pdf page 34 -->

---

## Fade Out Room Lamp

### Room Lamp Circuit Diagram (1)

<!-- Figure: Room lamp circuit diagram (1) showing battery feed through fuse, BCM-MR connector, BCM-G08 connector, overhead console lamp, room lamp, luggage lamp connections, and associated wiring with grounds G11 and G12, source: BODY CONTROL MODULE.pdf page 35 -->

**Circuit connections:**
- Battery power through Fuse to BCM-MR and BCM-G08
- Overhead Console Lamp connection
- Room Lamp with BCM control
- Luggage Lamp connection
- To Instrument Cluster connection
- BCM-MR1 connector
- BCM-LM connector
- Wire gauges: 2.0 sq mm main power, 0.85 sq mm for lamp circuits
- Grounds: G11, G12

### Room Lamp Circuit Diagram (2)

<!-- Figure: Room lamp circuit diagram (2) showing room lamp switch, tail gate open switch, door switches (driver/passenger), luggage lamp, overhead console lamp, BCM-G7 connector, key reminder switch connector, and associated wiring, source: BODY CONTROL MODULE.pdf page 36 -->

**Circuit connections:**
- Room Lamp Switch (3-position)
- Left Door Switch and connections
- Tail Gate Open Switch
- Door switches feeding BCM
- M03 (Luggage Lamp connector)
- M04 (Overhead Console Lamp)
- M64 connector
- Key Reminder Switch connection
- Wire gauges: 0.85 sq mm for switch circuits, 2.0 sq mm for power, 0.5 sq mm for signals
- Grounds: G01, G11

### Room Lamp - BCM Diagnostic Procedure

#### 1. Function explanation

It turns on when door is opened, and fades out after 5 or 6 seconds when closed.

#### 2. Input/output signal

- Fuse: F18 (10A)
- Input: Door switch (F11)
- Output: Room lamp (M3)

#### 3. Related Hi-scan(pro) failure diagnosis

**Input/output monitoring:**

Select "04.DOOR" and press [ENTER]. Then, the following screen will be displayed. Check BCM input/output condition against all door switches and room lamp.

**1.1 Input/Output Monitoring**

| Parameter | Value |
|---|---|
| MODEL | HD COUPE, 2000MY ALL |
| SYSTEM | BODY CONTROL MODULE |

**1.11 Current Data**

| Parameter | Value |
|---|---|
| DRIVER DOOR SW | CLOSED |
| PASSENGER DOOR SW | CLOSED |
| DOOR BASE | CLOSED |
| KEY HOLE ILLUMINATION | OFF |
| ROOM LAMP | 0 % |
| HOOD SW | CLOSED |
| TAIL GATE OPEN SW | CLOSED |
| TAIL GATE UNLOCK INPUT | OFF |

**Actuator Inspection:**

Select "02.OUTPUT ACTUATION" and press [ENTER]. Perform forced drive against room lamp.

**1.2 Actuation Test**

| Parameter | Value |
|---|---|
| MODEL | HD COUPE, 2000MY ALL |
| SYSTEM | BODY CONTROL MODULE |
| 01. INPUT ACTUATION | |
| 02. OUTPUT ACTUATION | |

**1.11 Actuation Test**

| Parameter | Value |
|---|---|
| ROOM LAMP | |
| DURATION | 4 UNTIL STOP KEY |
| METHOD | ACTIVATION |
| CONDITION | ROOM LAMP, DOOR POS. |

PRESS [STRT], IF YOU ARE READY!

<!-- Figure: Hi-scan room lamp diagnostic screens, source: BODY CONTROL MODULE.pdf page 37 -->

#### 4. Expected failure symptoms

Room lamp does not work.

### 5. Actions by failure symptoms

**Room lamp does not work.**

```
Check whether room lamp switch
is placed at door position
  |
  |-- NO --> Place it on the door position
  |
  YES
  |
  v
[Room lamp] Output monitoring
  |
  |-- NG --> BCM malfunction
  |
  OK
  |
  v
Does the room lamp turn on
when room lamp switch is turned on?
  |
  |-- YES --> Output wiring short of room lamp --> BCM-MR (3) - M95 (1) Check
  |
  NO
  |
  v
Room lamp power supply malfunction --> BCM-MR (2) - M95 (3) Check
Room lamp bulb malfunction --> Room lamp bulb replacement
```

<!-- Figure: Room lamp troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 38 -->

---

## Seat Belt Warning Lamp Timer

### Warning Lamp and Gauge Circuit Diagram

<!-- Figure: Warning lamp and gauge circuit diagram showing battery feed through fuses, BCM connections (BCM-JM, BCM-06), instrument cluster warning lamps (oil pressure, coolant temperature, charge), fuel gauge sender, fuel instrument cluster connector, and associated wiring, source: BODY CONTROL MODULE.pdf page 39 -->

**Circuit connections:**
- Battery through Fuse to BCM-JM
- Fuse F17 feed to instrument cluster
- Oil Pressure Switch connection
- Coolant Temperature Gauge sender
- Charge warning indicator
- Fuel Gauge sender with float
- See Airbag connection
- See ECM Circuit connections
- Wire gauges: 0.85 sq mm for warning lamp circuits, 0.5 sq mm for sensor circuits
- Grounds: G01, G11

### Seat Belt Warning Lamp - BCM Diagnostic Procedure

#### 1. Function explanation

Seat belt indicator lamp blinks for 6 seconds when IGN is turned on to recommend driver to buckle up.

#### 2. Input/output signal

- Fuse: F17 (10A)
- Output: Seat belt indicator lamp (J12)

#### 3. Related Hi-scan(pro) failure diagnosis

**Input/output monitoring:**

Select "07.ETC" and press [ENTER]. Then, the following screen will be displayed. Check output condition against seat belt indicator lamp.

**1.1 Input/Output Monitoring**

| Parameter | Value |
|---|---|
| MODEL | HD COUPE, 2000MY ALL |
| SYSTEM | BODY CONTROL MODULE |

Menu items:
1. 01. POWER
2. 02. FLASH
3. 03. LAMP
4. 04. DOOR
5. 05. LOCK & FOLDING
6. 06. WIPER
7. 07. ETC

**1.11 Current Data**

| Parameter | Value |
|---|---|
| POWER WINDOW RELAY | OFF |
| SEATBELT SW | UNLOCKED |
| CHIME BELL | OFF |
| OVERHEATED | OFF |
| REAR DEFOGGER SW | OFF |
| REAR DEFOGGER | OFF |
| CRASH SENSOR VOLTAGE | 0.0 V |

**Actuator Inspection:**

Select "02.OUTPUT ACTUATION" and press [ENTER]. Perform forced drive against seat belt indicator lamp.

**1.2 Actuation Test**

| Parameter | Value |
|---|---|
| MODEL | HD COUPE, 2000MY ALL |
| SYSTEM | BODY CONTROL MODULE |
| 01. INPUT ACTUATION | |

**1.11 Actuation Test**

| Parameter | Value |
|---|---|
| SEATBELT INDICATOR | |
| DURATION | 4 UNTIL STOP KEY |
| METHOD | ACTIVATION |
| CONDITION | IG. KEY ON |
| | SEATBELT SW: SUPPORT |

PRESS [STRT], IF YOU ARE READY!

<!-- Figure: Hi-scan seat belt warning lamp diagnostic screens, source: BODY CONTROL MODULE.pdf page 40 -->

#### 4. Expected failure symptoms

Seat belt indicator lamp does not work.

### 5. Actions by failure symptoms

**Seat belt indicator lamp does not work.**

```
[Seat belt indicator lamp] Output monitoring
  |
  |-- NO --> BCM malfunction
  |
  YES
  |
  v
Does the other indicator inside
cluster lamp turn on when IGN is on?
  |
  |-- NO --> Fuse (F17) Check
  |
  YES
  |
  v
Output circuit wiring short
of seat belt indicator lamp --> BCM-JM (2) - M10-2 (9) Check

Cluster malfunction --> Indicator lamp malfunction inside cluster
```

<!-- Figure: Seat belt indicator lamp troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 41 -->

---

## Tail Lamp Automatic Turn Off

### Tail Lamp and License Lamp Circuit Diagram (1)

<!-- Figure: Tail lamp circuit diagram (1) showing battery feed through fuse, BCM-DD connector, tail lamp relay, tail lamp switch connections, M04-3 connector, license lamp connector (to Fuse 8 and Fuse 14), and associated wiring with grounds G14 and G11, source: BODY CONTROL MODULE.pdf page 42 -->

**Circuit connections:**
- Battery through junction fuse block
- Tail Lamp Relay controlled by BCM
- BCM-DD connector
- BCM-HI connector
- License lamp connector via M04-3
- To Fuse 8 and Fuse 14
- Wire gauges: 2.0 sq mm for relay control, 0.85 sq mm for lamp feeds
- Grounds: G14, G11

### Tail Lamp and License Lamp Circuit Diagram (2)

<!-- Figure: Tail lamp circuit diagram (2) showing front tail lamp relay, BCM-FF connector, left/right front turn signal lamps, left/right rear combination lamps (with tail lamp, turn signal, backup lamp sections), side markers, license plate lamp, and associated wiring, source: BODY CONTROL MODULE.pdf page 43 -->

**Circuit connections:**
- Front Tail Lamp Relay feed
- Fuse 14 feed
- BCM-FF connector
- Left and Right front turn signal/position lamps
- Left and Right rear combination lamps
- Side marker connections (left/right)
- License Plate Lamp
- Wire gauges: 0.85 sq mm typical for lamp circuits, 2.0 sq mm for main feeds
- Grounds: G14, G05, G06, G16

### Tail Lamp - BCM Diagnostic Procedure

#### 1. Function explanation

Remove key at the tail lamp on state. Tail lamp turns off automatically when the driver's door is opened. So, battery discharging is prevented by turning the tail lamp off.

#### 2. Input/output signal

- Fuse: F13 (10A), F14 (10A)
- Input: Driver's side door switch (E9), Tail lamp switch (H5), Door warning switch (M4)
- Output: Tail lamp (C10, C11, F5, F16, J5, I15)

#### 3. Related Hi-scan(pro) failure diagnosis

**Step 1 - Power monitoring:**

Select "01.POWER" and press [ENTER].

**1.1 Input/Output Monitoring**

| Parameter | Value |
|---|---|
| MODEL | HD COUPE, 2000MY ALL |
| SYSTEM | BODY CONTROL MODULE |

Menu items:
1. 01. POWER
2. 02. FLASH
3. 03. LAMP
4. 04. DOOR
5. 05. LOCK & FOLDING
6. 06. WIPER
7. 07. ETC

**1.11 Current Data (01.POWER)**

| Parameter | Value |
|---|---|
| BATTERY VOLTAGE | 0.0 V |
| DOOR WARNING SW | OFF |
| KEY STATE - ACC | OFF |
| KEY STATE - ON/ST | OFF |
| KEY STATE - ON | OFF |
| GENERATOR VOLTAGE | 0.0 V |
| STARTER INHIBIT OUTPUT | OFF |

<!-- Figure: Hi-scan power monitoring screen for tail lamp diagnosis, source: BODY CONTROL MODULE.pdf page 44 -->

**Step 2 - Lamp monitoring:**

Select "03.LAMP" and press [ENTER]. Then, the following screen will be displayed. Check BCM input condition against tail lamp.

**1.11 Current Data (03.LAMP)**

| Parameter | Value |
|---|---|
| TAIL LAMP | OFF |
| HEAD LAMP SW | OFF |
| HEAD LAMP | OFF |
| AUTO LIGHT OPTION | OFF |
| AUTO LIGHT SW | OFF |
| AUTO LIGHT SENSOR | 0 V |
| PANIC FOG SW | OFF |

**Step 3 - Door monitoring:**

Select "04.DOOR" and press [ENTER]. Then, the following screen will be displayed. Check BCM input condition against driver's side door switch.

**1.11 Current Data (04.DOOR)**

| Parameter | Value |
|---|---|
| DRIVER DOOR SW | CLOSED |
| PASSENGER DOOR SW | CLOSED |
| DOOR BASE | CLOSED |
| KEY HOLE ILLUMINATION | OFF |
| ROOM LAMP | 0 % |
| HOOD SW | CLOSED |
| TAIL GATE OPEN SW | CLOSED |
| TAIL GATE UNLOCK INPUT | OFF |

<!-- Figure: Hi-scan door monitoring screen for tail lamp diagnosis, source: BODY CONTROL MODULE.pdf page 45 -->

**Actuator Inspection:**

1. Select "01.INPUT ACTUATION" and press [ENTER]. Perform forced drive against tail lamp switch.
2. Select "02.OUTPUT ACTUATION" and press [ENTER]. Perform forced drive against tail lamp.

**1.11 Actuation Test (Input - Tail Lamp Switch)**

| Parameter | Value |
|---|---|
| TAIL LAMP SW | |
| DURATION | 4 UNTIL STOP KEY |
| METHOD | ACTIVATION |
| CONDITION | AS KEY ON |

PRESS [STRT], IF YOU ARE READY!

**1.11 Actuation Test (Output - Tail Lamp)**

| Parameter | Value |
|---|---|
| TAIL LAMP | |
| DURATION | 4 UNTIL STOP KEY |
| METHOD | ACTIVATION |
| CONDITION | AS KEY ON |

PRESS [STRT], IF YOU ARE READY!

#### 4. Expected failure symptoms

1. Tail lamp does not work.
2. Left tail lamp only does not work.
3. Right tail lamp only does not work.
4. External tail lamp works, but internal tail lamp does not.
5. Only one tail lamp does not work.
6. Tail lamp automatic turn off function does not work.

### 5. Actions by failure symptoms

#### 1) Tail lamp does not work

```
Does the tail lamp work
when IG is on (start)?
  |
  |-- NO --> Fuse (F18) short
  |
  YES
  |
  v
[Tail lamp switch] Input monitoring
  |
  |-- NO --> Input wiring of tail lamp switch
  |          Tail lamp switch malfunction
  |
  YES
  |
  v
[Tail lamp] Output monitoring
  |
  |-- NO --> BCM malfunction
  |
  YES
  |
  v
R4(Fuse F9) & I4(Fuse F14)
checks at both simultaneously?
  |
  |-- NG --> Fuse replacement
  |
  OK
  |
  v
Tail lamp switch 12V applied
to F13 and both terminals of
grounding after grounding?
  |
  |-- NO --> Since PCB internal relay is fail,
  |          replace BCM.
  |
  YES --> BCM 'C' & 'P' Connector installation check
```

**Wire check for tail lamp switch:**

1. BCM-HI (5) - M4-1 (2) Check
2. M01-2 (5) - M6 (2) - M69 (8) - G11 (Ground) Check

Connect ohmmeter to both terminals of tail lamp switch, and check the continuity.

**[M01-2] Connector terminal of tail lamp switch:**

| Pin | Function |
|---|---|
| 1 | Input |
| 2 | Output |

<!-- Figure: Tail lamp troubleshooting flowchart (symptom 1), source: BODY CONTROL MODULE.pdf page 46 -->

#### 2) Left tail lamp only does not work

Fuse F1(4) short check.

#### 3) Right tail lamp only does not work

Fuse F(9) short check.

#### 4) External tail lamp works but internal tail lamp does not

```
Does tail lamp of the power
window switch work?
  |
  |-- NO --> Check the joint connector
  |
  YES
  |
  v
Check shut connector installation
  |
  |-- NO --> Install it
  |
  YES
  |
  v
Rheostat malfunction
```

<!-- Figure: Internal tail lamp troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 47 -->

#### 5) One tail lamp only does not work

Check related wire bulb burnt.

#### 6) Tail lamp automatic turn off function does not work

```
[Power warning switch] Input monitoring
  |
  |-- NO --> See key reminder function
  |
  YES
  |
  v
[Driver's side door switch] Input monitoring
  |
  |-- NO --> See key reminder function
  |
  YES
  |
  v
BCM malfunction
```

<!-- Figure: Tail lamp auto turn off troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 47 -->

---

## Rear Window and Outside Mirror Defogger

### Rear Window and Outside Mirror Defogger Circuit Diagram (1)

<!-- Figure: Rear window and outside mirror defogger circuit diagram (1) showing battery feed through fuse, BCM connections (BCM-HI, BCM-06), defogger relay, rear window defogger grid, outside mirror defogger elements, TJ A/C control module connection, and associated wiring, source: BODY CONTROL MODULE.pdf page 48 -->

**Circuit connections:**
- Battery through Fuse 19 to defogger relay
- BCM-HI connector controls defogger relay
- BCM-06 connector
- Rear Window Defogger heating grid
- Outside Mirror Defogger elements (left and right)
- TJ A/C Control Module connection (Climate control illumination lamps)
- MD01 connector
- MD04 connector (Left outside mirror defogger)
- Wire gauges: 3.0 sq mm for defogger power feeds, 2.0 sq mm for relay control, 0.85 sq mm for signal wiring
- Grounds: G01, G11, G14

### Rear Window and Outside Mirror Defogger Circuit Diagram (2)

<!-- Figure: Rear window and outside mirror defogger circuit diagram (2) showing BCM-MR connector, CRASH sensor, defogger switch connections, outside mirror defogger elements (left and right mirror A/C), joint connectors, and associated wiring, source: BODY CONTROL MODULE.pdf page 49 -->

**Circuit connections:**
- BCM-MR connector
- CRASH Sensor connection
- Front Fuse 8 feed
- Left Mirror A/C (MIRROR-L/R) defogger connection
- Right Mirror A/C (MIRROR-L/R) defogger connection
- 3KFRD-BD1 and 3KFRD-BD2 connectors
- M36 connector
- Wire gauges: 0.5 sq mm for mirror circuits, 0.85 sq mm for signal, 2.0 sq mm for power
- Grounds: G11

---

## Charging Circuit Diagram (2.0L)

<!-- Figure: Charging circuit diagram for 2.0L engine showing battery, generator (alternator), BCM-LM connector, starter motor relay, ignition switch, charge warning lamp in cluster, ATD connection, and associated wiring paths, source: BODY CONTROL MODULE.pdf page 50 -->

**Circuit connections:**
- Battery to Generator (Alternator)
- BCM-LM connector
- BCM-B connector
- Starter motor connection
- Charge indicator lamp in instrument cluster
- ATD (Automatic Transaxle Diagnosis) connection
- Start/Stop relay connections
- M06-1 connector
- Wire gauges: 5.0 sq mm for charging main cable, 3.0 sq mm for battery/starter feeds, 2.0 sq mm for relay circuits, 0.85 sq mm for signal wiring
- Grounds: G01, G11
- Note: Diagram labeled specifically for 2.0L engine variant
