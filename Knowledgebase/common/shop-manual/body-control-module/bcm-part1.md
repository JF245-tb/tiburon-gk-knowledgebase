---
source: BODY CONTROL MODULE.pdf
chapter: BCM
section: BE-1 to BE-25
pages: 1-25
engine: All
title: Body Control Module - Part 1
vehicle: 2003 Hyundai Tiburon (GK)
---

# Troubleshooting Procedure for BCM

## Table of Contents

| Section | Page |
|---------|------|
| BCM Failure Diagnosis Using HI-SCAN(PRO) | BE-2 |
| **Failure Diagnosis by BCM Functions** | |
| Central Door Lock | BE-5 |
| Key Reminder | BE-11 |
| Outside Mirror Folding | BE-15 |
| Flasher | BE-20 |
| Power Window | BE-27 |
| Ignition Key Hole Illumination | BE-32 |
| Fade Out Room Lamp | BE-35 |
| Seat Belt Warning Lamp Timer | BE-39 |
| Tail Lamp Automatic Turn Off | BE-42 |
| Rear Window & Outside Mirror Defogger | BE-48 |
| Auto Light Control | BE-56 |
| Wiper & Washer Control | BE-61 |
| Keyless Entry & Burglar Alarm | BE-67 |

---

## BCM Failure Diagnosis Using HI-SCAN(PRO)

### Overview

1. BCM (Body Control Module) is an integrative type control unit, and it includes following functions:
   1. ETACS (various time & alarm control functions etc.)
   2. Receiver function of remote door lock
   3. Performs communication with Hi-scan(pro).

2. Located in a junction box (power supply and circuit joint format formation), and integrated shape.

3. Firstly, to diagnose BCM functions, select the menu of "01.HI-SCAN" mode and "07. BODY CONTROL MODULE" [ENTER].

### HI-SCAN Vehicle Diagnosis

**Step 1: Select Vehicle**

| # | Model | Year | Engine |
|---|-------|------|--------|
| 1 | ETOSC | 99-MY | ALL |
| 2 | SCOUPE | 95-MY | ALL |
| 3 | ACCENT | 99-MY | ALL |
| 4 | ELANTRA | 2001-05MY | ALL |
| 5 | ELANTRA | 50-03MY | ALL |
| 6 | ELANTRA | 93-95MY | ALL |
| 11 | HD COUPE | 97-2005MY | ALL |

Select: **HD COUPE, 2000MY ALL**

**Step 2: Select System**

| # | System |
|---|--------|
| 01 | ENGINE |
| 02 | AUTOMATIC TRANSAXLE |
| 03 | ANTI-LOCK BRAKE SYSTEM |
| 04 | SRS-AIRBAG |
| 05 | TRACTION CONTROL SYSTEM |
| 06 | SMARTRA |
| 07 | BODY CONTROL MODULE |
| 08 | CODE SAVING |

Select: **07. BODY CONTROL MODULE**

4. Then the following screen will be displayed:

**Step 3: Select Function**

| # | Function |
|---|----------|
| 01 | INPUT/OUTPUT MONITORING |
| 02 | ACTUATION TEST |

### Input/Output Monitoring

**1.11 Current Data Screen:**

| Parameter | Value |
|-----------|-------|
| BATTERY VOLTAGE | 0.0 V |
| KEY STATE - ACC | OFF |
| KEY STATE - ACC or ST | OFF |
| KEY STATE - ON | OFF |
| GENERATOR VOLTAGE | 0.0 V |
| STARTER INHIBIT OUTPUT | OFF |

5. Though self-diagnosis failure (code output) is not provided, we can find out the failure parts more rapidly by monitoring input/output values and forced drive in failure diagnosis.

6. If you want to check the current values of input/output values of BCM, select "01.INPUT/OUTPUT MONITORING" and press [ENTER]. Then the following screen will be displayed.

**1.11 Input/Output Monitoring Items:**

| # | Item |
|---|------|
| 01 | POWER |
| 02 | FLASH |
| 03 | LAMP |
| 04 | DOOR |
| 05 | LOCK & FOLDING |
| 06 | WIPER |
| 07 | ETC |

### BCM Input/Output Condition (Power Supply, Lamp, Door, Lock, Wiper)

It provides BCM input/output condition such as power supply condition, flash function, lamp condition, door condition, locking unit and mirror folding state, wiper circuit and so on.

6. If you want forced drive of BCM input factors, select "01. INPUT ACTUATION" after selecting "02. ACTUATION TEST".

### Actuation Test

**1.2 Actuation Test Screen:**

Select: **01. INPUT ACTUATION** or **02. OUTPUT ACTUATION**

7. Press [ENTER] and then the following screen will be displayed.

**1.11 Actuation Test Example (Left Turn Signal):**

| Parameter | Value |
|-----------|-------|
| LEFT TURN SIGNAL SW | - |
| DURATION | UNTIL STOP KEY |
| METHOD | ACTUATION |
| CONDITION | IG. KEY ON |

### Input Factor Forced Drive

**1.11 Actuation Test (Input):**

| Parameter | Value |
|-----------|-------|
| LEFT TURN SIGNAL SW | - |
| DURATION | UNTIL STOP KEY |
| METHOD | ACTUATION |
| CONDITION | IG. KEY ON |

### Output Factor Forced Drive

**1.11 Actuation Test (Output):**

| Parameter | Value |
|-----------|-------|
| LEFT TURN SIGNAL LAMP | - |
| DURATION | UNTIL STOP KEY |
| METHOD | ACTUATION |
| CONDITION | IG. KEY ON |

### Input/Output Monitoring - Current Data

**1.11 Current Data (Various Parameters):**

| Parameter | Value |
|-----------|-------|
| LEFT TURN SIGNAL SW | OFF |
| LEFT TURN SIGNAL LAMP | OFF |
| RIGHT TURN SIGNAL LAMP | OFF |
| HAZARD SW | OFF |

### Diagnostic Logic

1. When switch input is not normal: Possibility of malfunction in multi-function contact or input circuit.
2. Though switch input is normal, when turn signal lamp output is not normal: Possibility of BCM malfunction.
3. If both are normal: Possibility of malfunction in output wiring or lamp.

### BCM Self-Diagnosis Application Example

**Example:** Symptom: lamp is not operating when left turn signal switch is turned on.

**Failure diagnosis** -- Following are the expected failure origins:

1. Poor switch contact of multi-function switch
2. Input wiring malfunction
3. BCM malfunction
4. Output wiring malfunction
5. Left turn signal lamp malfunction

### Diagnostic Procedure

When multi-function switch or BCM output circuit are probably in problem (in the above 3-1), check the lamp operation by inputting input factors (BCM input) and outputting drive output factors compulsively:

- Multi-function switch: Wiring -> Diagnose circuit failure before BCM input terminal.
- Define output signals (lamp drive signal) to lamp compulsively to test BCM output terminal.
- Turn signal lamp (output factor) will blink, if it is normal when driven compulsively.
- BCM output terminal: Wiring -> Check any malfunction in BCM control and output circuit by directly diagnosing circuit to load (lamp).

---

## Failure Diagnosis by BCM Functions

---

## Central Door Lock

### Power Door Lock Circuit Diagram

<!-- Figure: Power door lock circuit diagram showing BCM connections to door lock actuators, door lock switches, and related wiring, source: BODY CONTROL MODULE.pdf page 5 -->

**Circuit elements:**

- FUSE 10 (via power distribution)
- FUSE 16 (via power distribution)
- BCM connectors: BCM-01, BCM-07, BCM-F7, BCM-JR
- Door lock switch (driver's side)
- Door lock switch (passenger's side)
- Door lock actuator (driver's side)
- Door lock actuator (passenger's side)
- Door lock actuator (rear/hatch)

**Ground points:** G01, G11

### Function Explanation

1. **Function explanation:** When lock/unlock knob of driver's side is controlled, passenger side also interlock. If the passenger side knob is controlled, driver side interlocks also.

2. **Input/Output signal:**
   - Fuse: F10 (10A)
   - Input: Driver's side door lock switch (E0), passenger side door lock switch (C3)
   - Output: Door lock (F6), Door unlock (F8)

### HI-SCAN(PRO) Failure Diagnosis

**1. Input/Output Monitoring:**

Select "05. LOCK & FOLDING" and press [ENTER]. Then the following screen will be displayed. Check BCM input/output state against driver's side door lock switch, passenger side door lock switch, door lock, door unlock.

**1.11 Current Data:**

| Parameter | Value |
|-----------|-------|
| DRIVER DOOR LOCK SW | LOCK |
| PASSENGER DOOR LOCK SW | LOCK |
| DOOR LOCK | OFF |
| DOOR UNLOCK | OFF |
| FOLDING MIRROR SW | OFF |
| OUTSIDE MIRROR FOLDING | OFF |
| OUTSIDE MIRROR UNFOLD | OFF |

### Actuation Inspection

**1. Input Actuation Test:**

Select "01. INPUT ACTUATION" and then press [ENTER]. Complete driver's side door lock/unlock switch, passenger side door switch.

| Parameter | Value |
|-----------|-------|
| DRIVER DOOR LOCK/UNLOCK SW | - |
| DURATION | UNTIL STOP KEY |
| METHOD | ACTUATION |
| CONDITION | IG. KEY ON (CLOSED DOOR) |

**2. Output Actuation Test:**

Select "02. OUTPUT ACTUATION" and then press [ENTER]. Perform forced drive against door lock and door unlock.

| Parameter | Value |
|-----------|-------|
| DOOR LOCK | - |
| DURATION | 1 SECONDS |
| METHOD | ACTUATION |
| CONDITION | IG. KEY ON |

### Expected Failure Symptoms

1. Lock function works but unlock function does not.
2. Unlock function works but lock function does not.
3. When lock/unlock knob of passenger side is controlled, driver side interlocks. But when the driver side knob is controlled, passenger side does not interlock.
4. When passenger side knob is controlled, driver side does not interlock.
5. Both sides do not interlock.

### Troubleshooting by Failure Symptoms

#### Symptom 1: Lock function works but unlock function does not respond

**If lock function works but unlock does not:**

Since PCB integrated relay is fail, replace the BCM.

#### Symptom 2: Unlock function works but lock function does not interlock

Since PCB integrated relay is fail, replace the BCM.

#### Symptom 3: Passenger side controlled, driver side interlocks; driver side controlled, passenger side does not interlock

**Flowchart:**

1. Check passenger's side door lock switch input monitoring -> NG -> Connection not defective of passenger's side door lock actuator
2. Check driver's side door lock switch input monitoring -> NG:
   - Input wiring short of driver's side door lock switch
   - Internal switch contact failure of driver's side door lock actuator

**Wiring checks:**
- Measure resistance of actuator by handling it by the hand after connecting an ohmmeter to the both ends of actuator unit.
  - Locked condition / Unlocked condition: Normal if it is below 1 ohm.

**BCM connector pin checks (driver's side interlock):**

| Check | Pins |
|-------|------|
| 1 | BCM-FF (2) - MD02 (2) - D06 (2) Check |
| 2 | D.M2 (2) - MD02 (1) - M45 (2) - M45 (3) - G01(Ground) Check |

<!-- Figure: Connector terminal diagram D06 (driver's side door lock actuator), source: BODY CONTROL MODULE.pdf page 8 -->

**If OK -> Output wiring short of passenger's side door lock switch OR Passenger's side door lock actuator failure:**

| Check | Pins |
|-------|------|
| 1 | BCM-FF (2) - MD01 (2) - D06 (2) Check |
| 2 | BCM-FF (3) - MD01 (1) - MD04 (3) - D19 (2) Check |

*Normal condition in the parenthesis (Driver: Passenger's side interlocks)*

Apply 12V to the both ends under uninstalled condition, and it is normal if it operates.

<!-- Figure: Connector terminal diagram D06 (passenger's side door lock actuator), source: BODY CONTROL MODULE.pdf page 8 -->

#### Symptom 4: Driver side controlled, passenger side interlocks; passenger side controlled, driver side does not interlock

**Flowchart:**

1. Check driver's side actuator operation -> NG -> Connection not defective of driver's side door lock actuator
2. Check passenger's side door lock switch input monitoring -> NG:
   - Input wiring short of passenger's side door lock switch
   - Internal switch contact failure of passenger's side door lock actuator

**BCM connector pin checks:**

| Check | Pins |
|-------|------|
| 1 | BCM-FF (2) - MD04 (2) - D16 (2) Check |
| 2 | D.112 (2) - MD04 (3) - M45 (2) - M45 (3) - G01(Ground) Check |

<!-- Figure: Connector terminal diagram D16 (passenger's side door lock actuator), source: BODY CONTROL MODULE.pdf page 9 -->

**If OK:**

| Check | Pins |
|-------|------|
| 1 | BCM-FF (6) - MD01 (2) - D06 (2) Check |
| 2 | BCM-FF (3) - MD01 (1) - MD04 (3) - D06 (2) Check |

*Normal condition in the parenthesis (Driver: Passenger's side interlocks)*

Apply 12V to the both ends under uninstalled condition, and it is normal if it operates.

<!-- Figure: Connector terminal diagram D06 (driver's side door lock actuator), source: BODY CONTROL MODULE.pdf page 9 -->

#### Symptom 5: Both sides do not interlock

**Flowchart:**

1. Does it operate in IGN ON state? -> NO -> BCM main FUSE (F18) short -> BCM malfunction
2. FUSE (F24) short check -> NO -> FUSE replacement
3. Driver's side door lock switch input monitoring -> check
4. Passenger's side door lock switch input monitoring -> check

**If passenger's side door lock switch input is NG:**
- BCM "E" connector is removed
- Driver's side door lock actuator connector is removed

**If passenger's side door lock switch input monitoring is OK:**
- (Door lock) Is a forced drive, is the 12V applied to F5 & F19 terminal of BCM connector? -> If fail, since the PCB integrated relay is fail, replace BCM.

**Final wiring check:**

Does the connector operate when 12V is applied to wiring connector BCM-FF (2) and BCM-FF (1)?

| Check | Pins |
|-------|------|
| 1 | BCM-FF (5) - MD01 (2) Check |
| 2 | BCM-FF (3) - MD01 (1) Check |

**Notes:**
1. Five terminal contact of BCM "F" connector
2. Both actuator fail at the same time

---

## Key Reminder

### Key Reminder Switch Circuit Diagram

<!-- Figure: Key reminder switch circuit diagram showing BCM connections to ignition key cylinder switch and key reminder buzzer, source: BODY CONTROL MODULE.pdf page 11 -->

**Circuit elements:**

- C-07 A1 FUSE (via power distribution)
- FUSE 10 (via power distribution)
- FUSE 16 (gas passenger's side junction connector)
- BCM connectors: BCM-IM, BCM-JR, BCM-LIB
- Key reminder buzzer
- Joint connector (M65)
- Ground points: G11

### Room Lamp Circuit Diagram

<!-- Figure: Room lamp circuit diagram showing trunk lamp, left/right door switches, floor courtesy lamps, and luggage room lamp, source: BODY CONTROL MODULE.pdf page 12 -->

**Circuit elements:**

- FUSE 10 (via power distribution)
- BCM connectors: BCM-E7, BCM-07, BCM-JR, BCM-UB
- Multi-function switch (with dimmer)
- Left front door switch (M04)
- Right front door switch (M04)
- Trunk lid switch
- Left front door courtesy lamp
- Right front door courtesy lamp
- Luggage room lamp
- Remote switch
- Joint connector
- Ground points: G01, G11

### Function Explanation

1. **Function explanation:** When ignition key is in the key cylinder and driver's side door or the passenger's side door is open, if the knob is locked, then it outputs automatically to prevent the door lock.

2. **Input/Output signal:**
   - Fuse: F10 (10A)
   - Input: Door warning switch (M6), Driver's side door switch (E0), Passenger's side door switch (E4)
   - Output: Key hole illumination (F20), Door unlock (F12)

### HI-SCAN(PRO) Failure Diagnosis

**1. Input/Output Monitoring:**

Select "01.POWER" and press [ENTER]. Then the following screen will be displayed. Check BCM input condition against door warning switch.

**1.11 Current Data:**

| Parameter | Value |
|-----------|-------|
| BATTERY VOLTAGE | 0.0 V |
| KEY STATE - ACC | OFF |
| KEY STATE - ACC or ST | OFF |
| KEY STATE - ON | OFF |
| GENERATOR VOLTAGE | 0.0 V |
| STARTER INHIBIT OUTPUT | OFF |

Select "04.DOOR" and press [ENTER].

**1.11 Current Data (Door):**

| Parameter | Value |
|-----------|-------|
| DRIVER DOOR SW | CLOSED |
| PASSENGER DOOR SW | CLOSED |
| DOOR WARN | OFF |
| KEY HOLE ILLUMINATION | OFF |
| ROOM LAMP | 0 % |
| HOOD SW | CLOSED |
| TAIL GATE OPEN SW | CLOSED |
| TAIL GATE UNLOCK INPUT | OFF |

### Expected Failure Symptoms

Key reminder function does not work.

### Troubleshooting Flowchart

**Key reminder function does not work:**

1. Does the central door lock function work? -> NO -> Check central door lock function
2. Door warning switch input monitoring -> NG:
   1. Removal of door warning switch
   2. Input wiring short of door warning switch
   3. Internal switch malfunction of door warning switch

**BCM connector check:**

| Check | Pins |
|-------|------|
| 1 | BCM-IM(4) - M05 (2) Check |
| 2 | M05 (2) - M18 (2) - M96 (2) - G11 Check |

Connect ohmeter to both ends of door warning switch, and check the continuity when key is inserted or withdrawn.

<!-- Figure: Connector terminal diagram M05 (door warning switch), source: BODY CONTROL MODULE.pdf page 14 -->

3. Driver's side door switch input monitoring -> NG -> Driver's side door switch is removed or broken.

**BCM connector check:**

| Check | Pins |
|-------|------|
| 1 | BCM-EF (3) - M04 (2) Check |
| 2 | M04 (2) - G01(Ground) Check |

4. Passenger's side door switch input monitoring -> NG -> Passenger's side door switch is removed or broken.

**BCM connector check:**

| Check | Pins |
|-------|------|
| 1 | BCM-EF (3) - M4 (2) Check |
| 2 | M4 (2) - M45 (2) - M18 (2) - G22 - (Ground) Check |

5. Since BCM is defective, replace BCM.

---

## Outside Mirror Folding

### Circuit Diagram of Power Outside Mirror

<!-- Figure: Power outside mirror folding circuit diagram showing BCM connections to left and right folding mirror motors, folding mirror switch, source: BODY CONTROL MODULE.pdf page 15 -->

**Circuit elements:**

- C-07 A1 FUSE (via power distribution)
- FUSE 10 (via power distribution)
- FUSE 16 (gas passenger's side junction connector)
- BCM connectors: BCM-01, BCM-F7, BCM-JR, BCM-LIB
- Folding mirror switch
- Left folding mirror motor (Left mirror actuator)
- Right folding mirror motor (Right mirror actuator)
- Ground points: G11, G12

### Function Explanation

1. **Function explanation:** When folding mirror switch is turned on, Mirror folds or unfolds.

2. **Input/Output signal:**
   - Fuse: F10 (10A)
   - Input: Folding mirror switch (E3)
   - Output: Mirror folding (F20), Drive unlock (F12)

### HI-SCAN(PRO) Failure Diagnosis

**1. Input/Output Monitoring:**

Select "05. LOCK & FOLDING" and press [ENTER]. Then the following screen will be displayed. Check BCM input/output state against folding mirror switch, outside mirror folding, outside mirror unfolding.

**1.11 Current Data:**

| Parameter | Value |
|-----------|-------|
| DRIVER DOOR LOCK SW | LOCK |
| PASSENGER DOOR LOCK SW | LOCK |
| DOOR LOCK | OFF |
| DOOR UNLOCK | OFF |
| FOLDING MIRROR SW | OFF |
| OUTSIDE MIRROR FOLDING | OFF |
| OUTSIDE MIRROR UNFOLD | OFF |

### Actuation Inspection

**1. Input Actuation Test:**

Select "01. INPUT ACTUATION" and then press [ENTER].

| Parameter | Value |
|-----------|-------|
| FOLDING MIRROR SW | - |
| DURATION | UNTIL STOP KEY |
| METHOD | ACTUATION |
| CONDITION | IG. KEY ON |

**2. Output Actuation Test:**

Select "02. OUTPUT ACTUATION" and then press [ENTER]. Perform forced drive against outside mirror folding, outside mirror unfolding.

**Actuation Test (Output):**

| Parameter | Value |
|-----------|-------|
| OUTSIDE MIRROR FOLDING | - |
| DURATION | 10 SECONDS |
| METHOD | ACTUATION |
| CONDITION | IG. KEY ON |

### Expected Failure Symptoms

1. Folding function works but unfolding function does not.
2. Unfolding function works, but folding function does not.
3. Driver side mirror works, but passenger side mirror does not.
4. Passenger side mirror works, but driver side does not.
5. Both sides do not work.

### Troubleshooting by Failure Symptoms

#### Symptom 1: Folding function works, but unfolding function does not

Since unfolding relay is fail, replace the relay.

#### Symptom 2: Unfolding function works, but folding function does not

Since folding relay is fail, replace the relay.

#### Symptom 3: Driver side mirror works, but passenger side does not

**Flowchart:**

1. Passenger's side folding mirror output wiring short.
2. Passenger's side folding mirror failure.

**BCM connector check:**

| Check | Pins |
|-------|------|
| 1 | BCM-FF (8) - MD03 (2) - D16 (2) Check |
| 2 | BCM-FF (3) - MD03 (1) - D16 (2) Check |

*Normal condition inside the parenthesis (Since driver's side works)*

Normal if the unit operates when 12V is applied to ends of terminal.

<!-- Figure: Connector terminal diagram D16 (passenger's side folding mirror), source: BODY CONTROL MODULE.pdf page 18 -->

#### Symptom 4: Passenger side mirror works, but driver side does not

**Flowchart:**

1. Driver's side folding mirror output wiring short.
2. Driver's side folding mirror failure.

**BCM connector check:**

| Check | Pins |
|-------|------|
| 1 | BCM-FF (8) - MD00 (2) - MD03 (1) - D06 (2) Check |
| 2 | BCM-FF (3) - MD00 (3) - MD03 (1) - D06 (2) Check |

*Normal condition in the parenthesis (Since passenger's side works)*

If the unit operates when 12V is applied under uninstalled condition, it is normal.

<!-- Figure: Connector terminal diagram D06 (driver's side folding mirror), source: BODY CONTROL MODULE.pdf page 18 -->

#### Symptom 5: Both sides do not work

**Flowchart:**

1. Fuse (F13) short check -> NO -> Fuse replacement
2. Folding mirror switch input monitoring -> NG:
   1. Input wiring short of folding mirror switch
   2. Internal switch contact malfunction of folding mirror switch

**BCM connector check:**

| Check | Pins |
|-------|------|
| 1 | BCM-EF (2) - MD03 (3) - D05 (2) Check |
| 2 | D05 (2) - MD09 (1) - G01(Ground) Check |

Connect ohmeter to both ends of power outside mirror switch, and check the continuity (main switch, and the fold/unfold selection).

<!-- Figure: Connector terminal diagram D05 (power window switch), source: BODY CONTROL MODULE.pdf page 19 -->

3. Mirror folding: Is the 12V applied to F20 and F12 terminals of BCM connector in forced drive? -> NO:
   - Folding relay malfunction & unfolding relay malfunction -> Replace two relays at once
   - BCM malfunction -> BCM replacement

4. Does the mirror work when 12V is applied to BCM-FF (8) and BCM-FF (3) terminals of wiring BCM-FF?

**BCM connector check:**

| Check | Pins |
|-------|------|
| 1 | BCM-FF (8) - MD03 (1) Check |
| 2 | BCM-FF (3) - MD03 (1) Check |

-> NO -> Poor contact of BCM "F" connection terminal

---

## Flasher

### Turn Signal Lamp and Hazard Lamp Circuit Diagram (1)

<!-- Figure: Turn signal lamp and hazard lamp circuit diagram (1) showing BCM connections to front/rear turn signal lamps, multi-function switch, hazard switch, and related wiring through BCM connectors, source: BODY CONTROL MODULE.pdf page 20 -->

**Circuit elements:**

- C-07 A1 FUSE (via power distribution)
- FUSE 7 (power distribution)
- BCM connectors: BCM-02, BCM-F7, BCM-01, BCM-FF, BCM-JR
- Multi-function switch (turn signal)
- Hazard lamp switch
- Front left/right turn signal & caution lamps
- Side marker & turn signal (Tail Tot & Direction)
- Ground points: G01, G11

### Turn Signal Lamp and Hazard Lamp Circuit Diagram (2)

<!-- Figure: Turn signal lamp and hazard lamp circuit diagram (2) showing rear lamp connections, CHMSL module, and joint connectors, source: BODY CONTROL MODULE.pdf page 21 -->

**Circuit elements:**

- BCM connectors: BCM-LR, BCM-LIB
- C/D04 module, C/D08 module
- Rear left/right caution/direction lamps
- Joint connector
- Ground points: G01, G11

### Function Explanation

1. **Function explanation:** It works at battery(B+) state when hazard switch turns on, and works at IGN state when turn signal lamp turns on. When the bulb burnt, hazard lamp blinks with the same interval, but turn signal lamp (left/right) blinks quickly.

2. **Input/Output signal:**
   - Fuse: F10 (10A)
   - Input: Hazard switch (M18), left turn signal switch (H12), right turn signal switch (H2)
   - Output: Left turn signal lamp (C9,F7,F13), Right turn signal lamp (C5,B7,F1)

### HI-SCAN(PRO) Failure Diagnosis

**1. Input/Output Monitoring:**

Select "02.FLASH" and press [ENTER]. Then following screen will be displayed. Check BCM input/output state against left turn signal lamp switch, right turn signal lamp, right turn signal lamp and hazard lamp switch.

**1.11 Current Data:**

| Parameter | Value |
|-----------|-------|
| LEFT TURN SIGNAL SW | OFF |
| LEFT TURN SIGNAL LAMP | OFF |
| RIGHT TURN SIGNAL LAMP | OFF |
| HAZARD SW | OFF |

### Actuation Inspection

**1. Input Actuation Test:**

Select "01. INPUT ACTUATION" and then press [ENTER].

| Parameter | Value |
|-----------|-------|
| LEFT TURN SIGNAL SW | - |
| DURATION | UNTIL STOP KEY |
| METHOD | ACTUATION |
| CONDITION | IG. KEY ON |

**2. Output Actuation Test:**

Select "02. OUTPUT ACTUATION" and then press [ENTER]. Perform forced drive against left turn signal lamp, right turn signal lamp.

**Actuation Test (Left Turn Signal Lamp):**

| Parameter | Value |
|-----------|-------|
| LEFT TURN SIGNAL LAMP | - |
| DURATION | UNTIL STOP KEY |
| METHOD | ACTUATION |
| CONDITION | IG. KEY ON |

### Expected Failure Symptoms

1. Hazard lamps do not work.
2. Right turn signal lamp does not work.
3. Left turn signal lamp does not work.
4. It blinks quickly. (When the bulb is not burnt)
5. One turn signal lamp does not work.

### Troubleshooting by Failure Symptoms

#### Symptom 1: Hazard lamp does not work

**Flowchart:**

1. Does the turn signal lamp work, when turn signal lamp switch is turned on in IGN state? -> NO:
   - Fuse (F7) short -> BCM malfunction
2. Hazard lamp switch input monitoring -> YES -> Fuse (F18) short
3. Input wiring short of hazard lamp switch -> Hazard lamp switch malfunction

**BCM connector check:**

| Check | Pins |
|-------|------|
| 1 | BCM-IM (6) - M13 (2) Check |
| 2 | M13 (2) - M18 (2) - M96 (3) - G11(Ground) Check |

Connect ohmeter to both ends of hazard lamp switch, and check the continuity.

<!-- Figure: Connector terminal diagram M13 (hazard lamp switch), source: BODY CONTROL MODULE.pdf page 24 -->

#### Symptom 2: Right turn signal lamp does not work

**BCM connector check:**

| Check | Pins |
|-------|------|
| 1 | BCM-IM (3) - M h1-2 (2) Check |
| 2 | M h1-2 (2) - M h4 (2) - M96 (3) - G11(Ground) Check |

Connect ohmeter to both ends of right turn signal lamp switch, and check the continuity.

<!-- Figure: Connector terminal diagram Mh1-2 (multi-function switch), source: BODY CONTROL MODULE.pdf page 24 -->

#### Symptom 3: Left turn signal lamp does not work

**BCM connector check:**

| Check | Pins |
|-------|------|
| 1 | BCM-IM(4) (3) - Mh1-2 (2) Check |
| 2 | Mh1-2 (2) - M04 (2) - M96 (3) - G11(Ground) Check |

Connect ohmeter to both ends of left turn signal lamp switch, and check the continuity.

<!-- Figure: Connector terminal diagram Mh1-2 (multi-function switch), source: BODY CONTROL MODULE.pdf page 25 -->

#### Symptom 4: It blinks quickly (When the bulb is not burnt)

**Flowchart:**

1. When the hazard lamp switch blinks too frequently when it is turned on -> YES -> BCM malfunction
2. When the right turn signal lamp switch blinks too frequently when it is turned on -> YES:
   - Wrong bulb specification of the right turn signal lamp
   - BCM malfunction
3. When the left turn signal lamp switch blinks too frequently when it is turned on:
   - Wrong bulb specification of the left turn signal lamp
   - BCM malfunction

**Correct bulb specifications:**

| Area | Front Turn Signal | Rear Turn Signal |
|------|-------------------|------------------|
| EC & General area | 21W | 21W |
| U.S.A area | 28W | 27W |
