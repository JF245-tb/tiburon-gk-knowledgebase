---
source: BODY CONTROL MODULE.pdf
chapter: BCM
section: BCM-51 to BCM-75
pages: 51-75
engine: All
title: Body Control Module - Part 3
vehicle: 2003 Hyundai Tiburon (GK)
---

# Body Control Module - Part 3 (BE-51 to BE-75)

Continuation of BCM troubleshooting procedures covering rear window defogger, auto light control, wiper and washer control, keyless entry and burglar alarm, room lamp circuit, and transmitter resynchronization.

---

## Rear Window Defogger (continued from Part 2)

### Function Explanation

When rear window defogger switch on while engine is running, it works.

### Input/Output Signal

- Fuse: F12 (20A)
- Input: Rear defogger switch (H19), Generator L (C13)
- Output: Rear defogger output (Rear window D11), Rear window defogger indicator lamp (I10), Outside mirror defogger (F16)

### Related Hi-scan/pro Failure Diagnosis

#### 1) Input/Output Monitoring

1. Select "01.POWER" and press [ENTER]. The following screen will be displayed. Check BCM input condition against generator voltage.

**1.1 INPUT/OUTPUT MONITORING**

| MODEL | HD COUPE | 2000MY ALL |
|-------|----------|------------|
| SYSTEM | BODY CONTROL MODULE | |

Items displayed:
- 01. POWER
- 02. FLASH
- 03. LAMP
- 04. DOOR
- 05. LOCK & FOLDING
- 06. WIPER
- 07. ETC

**1.11 CURRENT DATA**

| Item | Value |
|------|-------|
| BATTERY VOLTAGE | 0.0 V |
| DOOR WARNING SW | OFF |
| KEY STATE - ACC | OFF |
| KEY STATE - ON OR ST | OFF |
| KEY STATE - ON | OFF |
| GENERATOR VOLTAGE | OFF |
| STARTER INHIBIT OUTPUT | OFF |

<!-- Figure: Hi-scan current data screen for power monitoring, source: BODY CONTROL MODULE.pdf page 51 -->

2. Select "07.ETC" and press [ENTER]. Then the following screen will be displayed. Check BCM input condition against rear window defogger switch and rear window defogger.

**1.1 INPUT/OUTPUT MONITORING**

| MODEL | HD COUPE | 2000MY ALL |
|-------|----------|------------|
| SYSTEM | BODY CONTROL MODULE | |

Items displayed:
- 01. POWER
- 02. FLASH
- 03. LAMP
- 04. DOOR
- 05. LOCK & FOLDING
- 06. WIPER
- 07. ETC

**1.11 CURRENT DATA**

| Item | Value |
|------|-------|
| POWER WINDOW RELAY | OFF |
| SEATBELT SW | UNLOCKED |
| SEATBELT INDICATOR | OFF |
| CHIME BELL | OFF |
| OVERSPEED | OFF |
| REAR DEFOGGER | OFF |
| CHARGE MONITOR VOLTAGE | OFF |

<!-- Figure: Hi-scan current data screen for ETC monitoring, source: BODY CONTROL MODULE.pdf page 51 -->

#### 2) Actuator Inspection

1. Select "01.INPUT ACTUATION" and press [ENTER]. Perform forced drive against rear window defogger switch.

**1.2 ACTUATION TEST**

| MODEL | HD COUPE | 2000MY ALL |
|-------|----------|------------|
| SYSTEM | BODY CONTROL MODULE | |

Items displayed:
- 01. INPUT ACTUATION
- 02. OUTPUT ACTUATION

<!-- Figure: Hi-scan actuation test menu, source: BODY CONTROL MODULE.pdf page 51 -->

### Actuation Test (BE-52)

**1.11 ACTUATION TEST**

| Parameter | Value |
|-----------|-------|
| REAR DEFOGGER SW | |
| DURATION | UNTIL STOP KEY |
| METHOD | ACTUATION |
| CONDITION | IG. KEY ON, ENGINE RUNNING |

PRESS [STRT], IF YOU ARE READY!

2. Select "02.OUTPUT ACTUATION" and press [ENTER]. Perform forced drive against rear window defogger.

**1.2 ACTUATION TEST**

| MODEL | HD COUPE | 2000MY ALL |
|-------|----------|------------|
| SYSTEM | BODY CONTROL MODULE | |

Items displayed:
- 01. INPUT ACTUATION
- 02. OUTPUT ACTUATION

**1.11 ACTUATION TEST**

| Parameter | Value |
|-----------|-------|
| REAR DEFOGGER | |
| DURATION | 10 SECONDS |
| METHOD | ACTUATION |
| CONDITION | IG. KEY ON, ENGINE RUNNING |

PRESS [STRT], IF YOU ARE READY!

<!-- Figure: Hi-scan actuation test screens for rear defogger, source: BODY CONTROL MODULE.pdf page 52 -->

### Expected Failure Symptoms

1. Rear window defogger indicator lamp does not work.
2. Rear window defogger does not work.
3. Left side outside mirror defogger does not work.
4. Right outside mirror defogger does not work.

### Troubleshooting by Failure Symptoms (BE-53)

#### 5-1) Rear window defogger indicator lamp does not work

**Diagnostic Flow:**

1. Check Fuse(F12, F5) -- if NO: Fuse replacement
2. Check generator voltage -- if Below 12V:
   - 1. BCM-CE(3) - E20(2) Check
   - 2. Check generator connection
3. If Above 12V: Check rear window defogger switch input monitoring
   - If NO:
     1. Rear window defogger switch wiring short
     2. Rear window defogger switch malfunction
   - If YES: Check rear window defogger after positioning
     - If NO: BCM malfunction
     - If YES: Check if rear window defogger 12V is applied to both ends of BCM G1 and GND after output signal turned short
       - If YES:
         1. Output wiring short of rear window defogger
         2. Rear window defogger indicator lamp malfunction
       - Check rear defogger relay malfunction: Relay replacement

<!-- Figure: Troubleshooting flowchart for rear window defogger indicator lamp, source: BODY CONTROL MODULE.pdf page 53 -->

**Right side symptom flow - Rear window defogger does not work:**

1. BCM-HM(3) - MD5(3) Check (Manual A/C)
2. MO(2) - MK6(3) - MR6(3) - G11 Check (Auto A/C)
3. BCM-HM(3) - M18-1(3) Check (Auto A/C)
4. M18-1(8) - MK6(3) - MR6(3) - G11 Check (Auto A/C)

Install the ohmmeter at the both ends of air conditioning terminals and check the continuity.

5. BCM-E(4) - MD5(2) Check (Manual A/C)
6. MO(2) - MK6(3) - MR6(3) - G11 Check (Auto A/C)
7. BCM-G(1) - M18-1(3) Check (Auto A/C)

Apply 12V to both terminals of air conditioner and check lamp operation:
- MD5(3) - MD(2) (Manual A/C)
- M18-1(2) - M18-1(8) (Auto A/C)

<!-- Figure: Wiring check paths for rear window defogger, source: BODY CONTROL MODULE.pdf page 53 -->

#### 5-2) Rear window defogger does not work (BE-54)

**Diagnostic Flow:**

1. Does rear window defogger indicator lamp work?
   - If NO: See 5-1 [Rear window defogger indicator lamp does not work]
   - If YES:
     1. Output wiring short of rear window defogger
     2. Rear window defogger malfunction

**Wiring checks:**
1. BCM-GF(3) - MR(3) - MR(4) - R1(1) Check
2. R(4)(1) - G08 Check

See workshop manual page BE-76 to BE-79

<!-- Figure: Troubleshooting flowchart for rear window defogger, source: BODY CONTROL MODULE.pdf page 54 -->

#### 5-3) Left outside mirror defogger does not work (BE-54)

**Diagnostic Flow:**

1. Does rear window defogger indicator lamp work?
   - If NO: See 5-1 [Rear window defogger indicator lamp does not work]
   - If YES:
     1. Output wiring short of left outside mirror defogger
     2. Left outside mirror defogger malfunction

**Wiring checks:**
1. BCM-FY(3) - MD01(8) - DK6(2) Check
2. DK6(2) - MD03(1) - M45(18) - G02 Check

It is normal if the measured defogger resistance is 10 ohm.

**[D06]** -- Connector terminal of left outside mirror

<!-- Figure: Left mirror defogger connector pinout and troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 54 -->

#### 5-4) Right outside mirror defogger does not work (BE-55)

**Diagnostic Flow:**

1. Does rear window indicator lamp work?
   - If NO: See 5-1 [Rear window defogger indicator lamp does not work]
   - If YES:
     1. Output wiring short of right outside mirror defogger
     2. Right outside mirror defogger unit malfunction

**Wiring checks:**
1. BCM-FF(19) - MD01(9) - MD04(16) - D06(1) Check
2. D16(2) - MD03(11) - M45(18) - M45(19) - G02 Check

It is normal if the measured defogger resistance is 10 ohm.

**[D16]** -- Connector terminal of right outside mirror

<!-- Figure: Right mirror defogger connector pinout and troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 55 -->

---

## Auto Light Control (BE-56 to BE-60)

### Auto Light Circuit Diagram (1) (BE-56)

<!-- Figure: Auto light circuit diagram (1) showing BCM connections to fuse/relay panel, multifunction switch, headlamp relay, tail lamp relay, and auto light sensor, source: BODY CONTROL MODULE.pdf page 56 -->

Circuit includes:
- Hot at all times fuse connections
- BCM-GN(12) connection
- BCM-CE connections
- BCM-LR connection to headlamp relay
- To multifunction switch (tail position)
- Instrument cluster connections
- Front fog lamp relay connector
- Multifunction switch connector

### Auto Light Circuit Diagram (2) (BE-57)

<!-- Figure: Auto light circuit diagram (2) showing light sensor, headlamp relay, multifunction switch positions (OFF/PARK/AUTO/HEAD/FLASH), and ground connections, source: BODY CONTROL MODULE.pdf page 57 -->

Circuit includes:
- Light sensor connection
- BCM-RR connection
- BCM-LR and BCM-MR connections
- Front headlamp relay/fuse box
- Multifunction switch positions: OFF / PARK / AUTO / HEAD / FLASH
- MH1-2 connector
- Ground connections G12, G11

### Function Explanation (BE-58)

When multi-function lighting switch is put at AUTO position in ignition key is on state, tail lamp and headlamp turn on automatically depending on the auto light sensor values.

### Input/Output Signal

- Fuse: Fuse 15A, F21(10A)
- Input: Auto light switch (H14), Auto light sensor voltage (J13)
- Output: Tail lamp, headlamp

### Related Hi-scan/pro Failure Diagnosis

#### 1) Input/Output Monitoring

Select "03.LAMP" and press [ENTER]. Then the following screen will be displayed. Check BCM input/output condition against auto light switch, auto light sensor voltage, auto light, tail lamp and headlamp.

**1.1 INPUT/OUTPUT MONITORING**

| MODEL | HD COUPE | 2000MY ALL |
|-------|----------|------------|
| SYSTEM | BODY CONTROL MODULE | |

Items displayed:
- 01. POWER
- 02. FLASH
- 03. LAMP
- 04. DOOR
- 05. LOCK & FOLDING
- 06. WIPER
- 07. ETC

**1.11 CURRENT DATA**

| Item | Value |
|------|-------|
| TAIL LAMP SW | OFF |
| TAIL LAMP | OFF |
| HEAD LAMP HI | OFF |
| HEAD LAMP LO | OFF |
| FLASHER | OFF |
| AUTO LIGHT SENSOR | 0.5 V |
| FRONT FOG SW | OFF |

<!-- Figure: Hi-scan current data for lamp monitoring, source: BODY CONTROL MODULE.pdf page 58 -->

#### 2) Actuator Inspection

Select "01.INPUT ACTUATION" and press [ENTER]. Perform forced drive against auto light switch.

**1.2 ACTUATION TEST**

| MODEL | HD COUPE | 2000MY ALL |
|-------|----------|------------|
| SYSTEM | BODY CONTROL MODULE | |

Items displayed:
- 01. INPUT ACTUATION
- 02. OUTPUT ACTUATION

**1.11 ACTUATION TEST**

| Parameter | Value |
|-----------|-------|
| AUTO LIGHT | |
| DURATION | UNTIL STOP KEY |
| METHOD | ACTUATION |
| CONDITION | IG. KEY ON |

PRESS [STRT], IF YOU ARE READY!

<!-- Figure: Hi-scan actuation test for auto light switch, source: BODY CONTROL MODULE.pdf page 58 -->

### Expected Failure Symptoms

1. Auto light does not work. (Tail lamp and headlamp works by the switch.)
2. When auto light is turned on, tail lamp and headlamp turn on simultaneously.

> **NOTE:** When the ambient luminous intensity is dark, tail lamp and headlamp may turn on simultaneously in auto light condition. In this case it's not the failure.

### Troubleshooting by Failure Symptoms (BE-59)

#### 5-1) Auto light does not work (Tail lamp and headlamp works by the switches)

**Diagnostic Flow:**

1. Check auto light switch input monitoring
   - If NO:
     - Input wiring short of auto light switch
     - Front terminal of auto light switch
     - Auto light switch malfunction

     **Wiring checks:**
     1. BCM-HM(2) - M01-2(5) Check
     2. M01-2(5) - MK6(2) - MK6(2) - G11 (Ground) Check

     Install ohmmeter at both ends of auto light switch terminals and check the continuity.

     **[MH1-2]** -- Connector terminal of multi-function switch (auto light portion)

   - If YES:
     1. BCM-JM(3) - M07(1) Check
     2. BCM-JM(5) - M07(2) Check
     3. BCM-JM(3) - M07(1) Check

     Auto light sensor re-installation or replacement.

2. Check transmitting/estimating (auto light sensor voltage) input monitoring:
   - If Remain (same voltage): Input wiring short of auto light sensor -- Auto light sensor malfunction -- Auto light sensor replacement
   - If Change: After covering (if light is not transmitted to auto light switch) -- forced drive
     - If Does not work: BCM malfunction

<!-- Figure: Auto light troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 59 -->

#### 5-2) When auto light is turned on, tail lamp and headlamp turn on simultaneously (BE-60)

**Diagnostic Flow:**

1. Check auto light option input monitoring:
   - If ON: Auto light option wrong wiring connection -- Cut BCM-H(12)
   - If OFF: BCM malfunction

<!-- Figure: Auto light simultaneous activation troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 60 -->

---

## Wiper and Washer Control (BE-61 to BE-66)

### Front Wiper and Washer Circuit Diagram (BE-61)

<!-- Figure: Front wiper and washer circuit diagram showing BCM connections, wiper motor, washer motor, intermittent wiper switch, multifunction switch, front wiper relay, and ground connections. Includes BCM-CE, BCM-KN, BCM-LN, BCM-JN, BCM-AN connectors and relay/fuse box connections, source: BODY CONTROL MODULE.pdf page 61 -->

Circuit includes:
- See Rear Wiper & Washer connections
- FRONT & METER fuse box
- BCM-CE, BCM-KN connections
- BCM-LN, BCM-JN connections
- BCM-AN connections
- Wiper motor connections (LO, HI)
- Front washer switch
- Front wiper relay
- CAM-1 connection
- EMPS connector
- Ground connections G01, G14

### Function Explanation (BE-62)

1. When washer switch is turned on, wiper operates two or three rotation.
2. Intermittent time varies by the vehicle speed and intermittent wiper volume control.

### Input/Output Signal

- Fuse: F7, F8, F15(20A)
- Input: Washer switch (H5), Wiper INT switch (J8), Wiper INT(1,2)(H3), Wiper parking (E14)
- Output: Wiper relay (C24)

### Related Hi-scan/pro Failure Diagnosis

#### 1) Input/Output Monitoring

Select "06.WIPER" and press [ENTER]. Then the following screen will be displayed. Check BCM input/output condition against front washer switch, intermittent wiper switch, intermittent wiper relay, intermittent wiper variable voltage, wiper parking, snow safety relay.

**1.1 INPUT/OUTPUT MONITORING**

| MODEL | HD COUPE | 2000MY ALL |
|-------|----------|------------|
| SYSTEM | BODY CONTROL MODULE | |

Items displayed:
- 01. POWER
- 02. FLASH
- 03. LAMP
- 04. DOOR
- 05. LOCK & FOLDING
- 06. WIPER
- 07. ETC

**1.11 CURRENT DATA**

| Item | Value |
|------|-------|
| FRONT WASHER SW | OFF |
| FRONT INT WIPER RELAY | OFF |
| WIPER INT TIME | 0.1 V |
| WIPER PARKING | OFF |
| SNOW SAFETY RELAY | OFF |

<!-- Figure: Hi-scan current data for wiper monitoring, source: BODY CONTROL MODULE.pdf page 62 -->

#### 2) Actuator Inspection

1. Select "01.INPUT ACTUATION" and press [ENTER]. Perform forced drive against front washer switch, intermittent wiper switch.

**1.2 ACTUATION TEST**

| MODEL | HD COUPE | 2000MY ALL |
|-------|----------|------------|
| SYSTEM | BODY CONTROL MODULE | |

Items displayed:
- 01. INPUT ACTUATION
- 02. OUTPUT ACTUATION

**1.11 ACTUATION TEST**

| Parameter | Value |
|-----------|-------|
| INTERMITTENT WIPER SW | |
| DURATION | UNTIL STOP KEY |
| METHOD | ACTUATION |
| CONDITION | IG. KEY ON |

PRESS [STRT], IF YOU ARE READY!

2. Select "02.OUTPUT ACTUATION" and press [ENTER]. Perform forced drive against intermittent wiper relay and snow safety relay.

**1.2 ACTUATION TEST**

| MODEL | HD COUPE | 2000MY ALL |
|-------|----------|------------|
| SYSTEM | BODY CONTROL MODULE | |

Items displayed:
- 01. INPUT ACTUATION
- 02. OUTPUT ACTUATION

**1.11 ACTUATION TEST (BE-63)**

| Parameter | Value |
|-----------|-------|
| FRONT INT WIPER RELAY | |
| DURATION | 1 SECONDS |
| METHOD | ACTIVATION |
| CONDITION | IG. KEY ON |

PRESS [STRT], IF YOU ARE READY!

<!-- Figure: Hi-scan actuation test screens for wiper system, source: BODY CONTROL MODULE.pdf pages 62-63 -->

### Expected Failure Symptoms (BE-63)

1. Wiper low and Wiper high does not work.
2. Wiper does not work when wiper INT is turned on.
3. When washer switch is turned on, wiper does not interlock.
4. When wiper INT volume is controlled, wiper intermittent time does not change.
5. Wiper intermittent time does not change by the vehicle speed.
6. When wiper INT operating, wiper stops in-between.

### Troubleshooting by Failure Symptoms (BE-64 to BE-66)

#### 5-1) Wiper low and Wiper high does not work (BE-64)

Since wire drives directly wiper low and high operation, check the following 3 items by referring to front wiper & washer:

1. Check multi-function switch connector removal
2. Check wiper motor
3. Check wiring

#### 5-2) When wiper INT is ON, wiper does not work (BE-64)

**Diagnostic Flow:**

1. Check Fuse(F7/10) short
   - If NO: Fuse replacement
   - If OK:
2. Check intermittent wiper switch input monitoring
   - If NO:
     - Input wiring short of intermittent wiper switch
     - Intermittent wiper switch malfunction

     **Wiring checks:**
     1. BCM-JM(2) - M01-1(2) Check
     2. M01-1(2) - BCM-LM(2) Check

     Install ohmmeter at both ends of intermittent wiper switch terminals and check the continuity.

     **[MH1-1]** -- Connector terminal of multi-function wiper switch

   - If YES: Check intermittent wiper relay output monitoring (does it turn on and off?)
     - If NO: BCM malfunction
     - If YES:
       - Wiper relay malfunction of engine room relay & fuse box: Relay replacement
       - Output wiring malfunction of intermittent wiper relay:
         1. BCM-CE(2) - E46(1) Check
         2. E46(2) - EM01(2) - M01-1(5) Check

<!-- Figure: Wiper INT troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 64 -->

#### 5-3) When washer switch is on, wiper does not interlock (BE-65)

**Diagnostic Flow:**

1. Check Fuse(F7/10) short
   - If NO: Fuse replacement
   - If OK:
2. Check front washer switch input monitoring
   - If NO:
     - Input wiring short of front washer switch
     - Front washer switch malfunction

     **Wiring checks:**
     1. BCM-MK(3) - M01-1(1) Check
     2. M01-1(2) - BCM-LM(2) Check

     Install ohmmeter at the both ends of front washer switch terminals and check the continuity.

     **[MH1-1]** -- Connector terminal of wiper switch

   - If YES: Does the wiper work when wiper INT is on?
     - See 5-2 [Wiper does not work when wiper INT is on]

3. If wiper INT works: BCM malfunction

<!-- Figure: Washer interlock troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 65 -->

#### 5-4) When wiper INT volume is controlled, wiper intermittent time does not vary (BE-65)

**Diagnostic Flow:**

1. Check intermittent wiper variable voltage (Does it change within the range of 0.7V and 3.5V in case of input monitoring?)
   - If Changes: BCM malfunction
   - If Remain unchanged:
     - Wiring short in relation to intermittent wiper variable voltage switch malfunction

     **Wiring checks:**
     1. BCM-LM(2) - M11-1(2) Check
     2. M11-1(2) - BCM-JM(2) Check

     Install the ohmmeter at the both ends of intermittent wiper variable switch, and check the resistance (resistance changes within the ranges of 0 ohm and 560 ohm by changing INT volume).

     **[MH1-1]** -- Connector terminal of multi-function wiper switch

<!-- Figure: Wiper INT volume troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 65 -->

#### 5-5) Wiper intermittent time does not change with the vehicle speed (BE-66)

**Wiring checks:**
1. BCM-JM(2) - M34(2) Check
2. M34(2) - M10-1(2) Check

<!-- Figure: Vehicle speed wiper troubleshooting, source: BODY CONTROL MODULE.pdf page 66 -->

#### 5-6) When wiper INT is operating, wiper stops in-between (BE-66)

1. If parking signal is troubled when wiper INT or OFF is operating, wiper stops judging wiper motor overload.
2. When wiper Low / High is operating, this function is not available.

**Diagnostic Flow:**

1. Does the wiper turn on and off in case of input monitoring while operating wiper low (wiper parking)?
   - If NO:
     - Wiper motor inner plate malfunction -- Wiper replacement
     - Wiring short in relation to wiper parking:
       - BCM-KN(8) - MC105(3) - C10T(1) Check (2.7 ENG)
       - BCM-KN(8) - MK06(1) - G07(2) Check (2.0 ENG)
   - If YES: Check wiring short -- BCM-CE(3) - E46(1) Check

<!-- Figure: Wiper stops in-between troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 66 -->

---

## Keyless Entry and Burglar Alarm (BE-67 to BE-75)

### Anti-Theft Alarm Circuit Diagram (BE-67)

<!-- Figure: Anti-theft alarm circuit diagram showing BCM connections to rear power distribution, fuse 13, central door lock actuators, burglar alarm horn, trunk/gate switch, hood switch, and ground connections. Includes BCM-HE, BCM-ED, BCM-EF connectors and connections to door lock/unlock circuits, source: BODY CONTROL MODULE.pdf page 67 -->

Circuit includes:
- Hot at all times fuse connections
- Rear Power Distribution fuse box
- FUSE 13
- BCM connections: BCM-HE, BCM-ED, BCM-EF
- SMARTRA (1), SMARTRA (2)
- Central door lock actuator connections
- Burglar alarm horn
- Trunk/tail gate switch
- Hood switch
- Ground connections G16, G11

### Room Lamp Circuit Diagram (BE-68)

<!-- Figure: Room lamp circuit diagram showing door switches (driver, passenger, rear), room lamp, luggage compartment lamp, BCM connections, and illumination switch. Includes BCM-GR/FF connections to door switches, BCM connections to room lamp timer, and tail gate illumination switch, source: BODY CONTROL MODULE.pdf page 68 -->

Circuit includes:
- DOOR FUSE connection
- TK1 DOOR SW1 (driver)
- Full door open/closed switches
- BCM-GR/FF connections
- Room lamp with door/on/off switch positions
- I/P LAMP CONNECTOR
- LUGGAGE COMPARTMENT lamp
- Tail gate illumination switch
- Ground connections G01, G02

### Function Explanation (BE-69)

Door is opened and closed by using the transmitter. When the vehicle is broken in, alarm works and vehicle can not be started.

### Input/Output Signal

- Input: Hood switch, tailgate switch, door switch, tailgate unlock switch
- Output: Starter inhibit, burglar alarm relay, burglar alarm horn

### Related Hi-scan/pro Failure Diagnosis

#### 1) Input/Output Monitoring

1. Select "01.POWER" and press [ENTER]. Then the following screen will be displayed. Check BCM auto output condition against starter inhibit output.

**1.1 INPUT/OUTPUT MONITORING**

| MODEL | HD COUPE | 2000MY ALL |
|-------|----------|------------|
| SYSTEM | BODY CONTROL MODULE | |

Items displayed:
- 01. POWER
- 02. FLASH
- 03. LAMP
- 04. DOOR
- 05. LOCK & FOLDING
- 06. WIPER
- 07. ETC

**1.11 CURRENT DATA**

| Item | Value |
|------|-------|
| BATTERY VOLTAGE | 0.0 V |
| DOOR WARNING SW | OFF |
| KEY STATE - ACC | OFF |
| KEY STATE - ON OR ST | OFF |
| KEY STATE - ON | OFF |
| GENERATOR VOLTAGE | OFF |
| STARTER INHIBIT OUTPUT | OFF |

<!-- Figure: Hi-scan current data for power/starter inhibit monitoring, source: BODY CONTROL MODULE.pdf page 69 -->

2. Select "04.DOOR" and press [ENTER]. Then the following screen will be displayed. Check BCM input condition against door switch, tailgate switch, tailgate key unlock.

**1.1 INPUT/OUTPUT MONITORING**

| MODEL | HD COUPE | 2000MY ALL |
|-------|----------|------------|
| SYSTEM | BODY CONTROL MODULE | |

Items displayed:
- 01. POWER
- 02. FLASH
- 03. LAMP
- 04. DOOR
- 05. LOCK & FOLDING
- 06. WIPER
- 07. ETC

**1.11 CURRENT DATA**

| Item | Value |
|------|-------|
| DRIVER DOOR SW | CLOSED |
| PASSENGER DOOR SW | CLOSED |
| DOOR SW | CLOSED |
| ROOM LAMP ILLUMINATION | OFF |
| ROOM LAMP | OFF |
| TAIL GATE OPEN SW | CLOSED |
| TAIL GATE UNLOCK INPUT | OFF |

<!-- Figure: Hi-scan current data for door monitoring, source: BODY CONTROL MODULE.pdf page 69 -->

3. Select "07.ETC" and press [ENTER]. Then the following screen will be displayed. Check BCM output condition against burglar alarm horn.

**1.1 INPUT/OUTPUT MONITORING**

| MODEL | HD COUPE | 2000MY ALL |
|-------|----------|------------|
| SYSTEM | BODY CONTROL MODULE | |

Items displayed:
- 01. POWER
- 02. FLASH
- 03. LAMP
- 04. DOOR
- 05. LOCK & FOLDING
- 06. WIPER
- 07. ETC

**1.11 CURRENT DATA (BE-70)**

| Item | Value |
|------|-------|
| OVERSPEED | OFF |
| REAR DEFOGGER SW | OFF |
| REAR DEFOGGER | OFF |
| POWER WINDOW RELAY | OFF |
| SEATBELT SW | UNLOCKED |
| SEATBELT INDICATOR | OFF |

<!-- Figure: Hi-scan current data for ETC monitoring (burglar alarm), source: BODY CONTROL MODULE.pdf page 70 -->

#### 2) Actuator Inspection (BE-70)

Select "02.OUTPUT ACTUATION" and press [ENTER]. Perform forced drive against starter inhibit output and burglar alarm horn.

**1.2 ACTUATION TEST**

| MODEL | HD COUPE | 2000MY ALL |
|-------|----------|------------|
| SYSTEM | BODY CONTROL MODULE | |

Items displayed:
- 01. INPUT ACTUATION
- 02. OUTPUT ACTUATION

**1.11 ACTUATION TEST**

| Parameter | Value |
|-----------|-------|
| STARTER INHIBIT OUTPUT | |
| DURATION | 60 SECONDS |
| METHOD | ACTIVATION |
| CONDITION | IG. KEY ON |

PRESS [STRT], IF YOU ARE READY!

<!-- Figure: Hi-scan actuation test for starter inhibit, source: BODY CONTROL MODULE.pdf page 70 -->

### Expected Failure Symptoms (BE-70)

1. Alarm does not work. (Hazard lamp works.)
2. When hood is opened inside the car like alarm test, horn does not work.
3. When door is opened inside the car like alarm test, horn does not work.
4. When tailgate is opened inside the car like alarm test, horn does not work.
5. When the vehicle is locked by the remote transmitter, central door lock function works but hazard lamp does not work once.
6. When system is arm condition, if the tailgate is tried open by the key, then the horn will work.
7. When the alarm is released condition, engine does not start.
8. Central door lock function works, but keyless entry system does not work.

> **NOTE:** When the door (driver's or passenger's) is opened by the key, horn will work -- it's not malfunction (normal operation).

### Troubleshooting by Failure Symptoms (BE-71 to BE-75)

#### 5-1) Alarm does not work (Hazard lamp works) (BE-71)

**Diagnostic Flow:**

1. Check Fuse(F(1)) short
   - If NO: Fuse replacement
   - If OK:
2. Check burglar alarm horn (Does horn when forced drive?)
   - Output wiring malfunction of burglar alarm horn:
     1. BCM-KN(5) - MC10(2) - MO9(1) - M59(5) Check (2.7 Engine)
     2. BCM-KN(6) - MC10(1) - M58(5) - MJ4(1) Check
     3. BCM-JM(2) - M59(3) Check
     4. M59(2) - M94(3) - E17(2) Check
     5. E17(2) - G10(Ground) Check
   - Burglar alarm relay malfunction: Relay replacement
   - Burglar alarm horn malfunction: Burglar alarm horn replacement

<!-- Figure: Alarm does not work troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 71 -->

#### 5-2) When hood is opened inside the car like alarm test, horn does not work (BE-71)

**Diagnostic Flow:**

1. Check hood switch input monitoring
   - If NO:
     - Check input wiring short of hood switch

     **Wiring checks:**
     1. BCM-HM(3) - MO02(2) - EC01(5) - E38(1) Check
     2. BCM-HM(2) - MC102(2) - EC11(9) - E3M(1) (2.7 Engine)

   - Hood switch malfunction: Hood switch replacement

<!-- Figure: Hood switch troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 71 -->

#### 5-3) When door is opened inside the car like alarm test, horn does not work (If tailgate and hood is opened, alarm works) (BE-72)

**Diagnostic Flow:**

1. Check all door switch input monitoring
   - If NO:
     - Check input wiring short of all doors

     **Wiring checks:**
     1. BCM - FF(1) - M53(2) Check
     2. M53(3) - G01 Check
     3. BCM - FF(1) - M54(2) Check
     4. M54(3) - M45(8) - M45(9) - G02 Check

   - All door switch malfunction

<!-- Figure: Door switch troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 72 -->

#### 5-4) When tailgate is opened inside the car like alarm test, horn does not work (BE-72)

**Diagnostic Flow:**

1. Check tailgate input monitoring
   - If NO:
     - Check input wiring short of tailgate

     **Wiring checks:**
     1. BCM-EF(9) - MR02(4) - RR02(4) - R17(1) Check
     2. R17(6) - G06 Check

   - Tailgate switch malfunction

<!-- Figure: Tailgate switch troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 72 -->

#### 5-5) When the vehicle is locked by the transmitter, central door lock function works but hazard lamp works only once (BE-73)

**Diagnostic Flow:**

1. Check all door switch input monitoring
   - If NO: See 5-3
   - If YES:
2. Check tailgate switch input monitoring
   - If NO: See 5-4
   - If YES:
3. When checking hood switch under closed condition:
   - Display open condition: Rubber at the above hood is not pressing enough the hood switch

<!-- Figure: Hazard lamp only works once troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 73 -->

#### 5-6) When tailgate is opened by the key under system arm condition, horn works (BE-73)

> **NOTE:** When the door (driver's or passenger's) is opened by the key, horn will work -- it's not malfunction (normal operation). (Arm system is released by the transmitter unlock only.)

**Diagnostic Flow:**

1. Check tailgate key unlock switch input monitoring
   - If NO:
     - Check wiring short of tailgate key unlock switch

     **Wiring checks:**
     1. BCM-EF(2) - MR02(2) - RR02(2) - R05(2) Check
     2. R05(3) - G06(Ground) Check

     Check the continuity while key in.

     **[R05]** -- Connector terminal of tailgate key unlock switch

   - Tailgate key unlock switch malfunction

<!-- Figure: Tailgate key unlock troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 73 -->

#### 5-7) Engine does not start, when the alarm released condition (BE-74)

**Diagnostic Flow:**

1. Does the start motor move?
   - If YES: Check the starting circuit
   - If NO:
2. Check starter inhibit output -- Turn the key into start position as monitoring
   - If Change in on state: BCM is currently alarm condition mode
   - If Remain off: Check the starting circuit

<!-- Figure: Engine no-start with alarm released troubleshooting flowchart, source: BODY CONTROL MODULE.pdf page 74 -->

#### 5-8) Central door lock function works, but keyless entry system does not work (BE-75)

**Diagnostic Flow:**

1. Does the transmitter lamp work when its button is depressed?
   - If NO: Transmitter battery replacement
   - If YES:
2. Does the hazard lamp turn on once when transmitter is resynchronized under ACC position?
   - If NO: After replacing transmitter, register the transmitter code using Hi-scan (See workshop manual page BE-04)
   - If YES:
3. Does the keyless entry operation work after removing the key?
   - If NO: Since BCM is defective, replace transmitter and register transmitter code
   - If YES: Normal

### Transmitter Resynchronization (BE-75)

> **NOTE:** Transmitter resynchronization: When transmitter are not resynchronized, which has been registered already by the receiver, it can be used without registration of code registration procedures. However if they were not resynchronized by the resynchronization procedures, follow the transmitter code registration procedures.

**1. Perform transmitter resynchronization in the following cases:**
- After battery (vehicle) replacement
- After replacing transmitter battery
- When synchronization between transmitter and BCM is not made

**2. Transmitter resynchronization methods:**

Turn off the ignition key after releasing the ignition key from OFF state to ACC position, and then press lock or unlock of the transmitter within 10 seconds, then hazard lamps blinks once.

**3. Transmitter resynchronization is not available in the following cases:**
- When resynchronized by the other people's transmitter
- When resynchronized with new transmitter
