---
source: BE.pdf
chapter: BE
title: Power Windows
section_pages: 100-121
printed_pages: BE-99 to BE-120
note: >
  These PDF pages cover the Lighting System (head lamp aiming, front fog lamp
  aiming), Auto Lights Control System, Daytime Running Lights (DRL), Head Lamp
  Levelling Device, and Immobilizer Control System. Filed under "power-windows"
  per extraction-script page mapping.
---

# Lighting System

## Head Lamps

### Head Lamp Aiming Instructions

The head lamps should be aimed with the proper beam-setting equipment, and in accordance with the equipment manufacturer's instructions.

> **NOTE:** If there are any regulations pertinent to the aiming of headlamps in the area where the vehicle is to be used, adjust so as to meet those requirements.

Alternatively turn the adjusting gear to adjust the headlamp aiming. If beam-setting equipment is not available, proceed as follows:

1. Inflate the tires to the specified pressure and remove any loads from the vehicle except the driver, spare tire, and tools.
2. The vehicle should be placed on a flat floor.
3. Draw vertical lines (vertical lines passing through respective headlamp centers) and a horizontal line (horizontal line passing through center of headlamps) on the screen.
4. With the headlamp and battery in normal condition, aim the headlamps so the brightest portion falls on the horizontal and vertical lines. Make vertical and horizontal adjustments to the lower beam using the adjusting wheel.

<!-- Figure: Head lamp assembly with adjusting wheel location, source: BE.pdf page 100 -->
<!-- Figure: Horizontal aiming (high beam) and Horizontal aiming (low beam) diagrams, source: BE.pdf page 100 -->
<!-- Figure: Vertical aiming (high beam) and Vertical aiming (low beam) diagrams, source: BE.pdf page 100 -->

### Front Fog Lamp

The front fog lamps should be aimed as the same manner of the head lamps aiming.

With the front fog lamps and battery normal condition, aim the front fog lamps by turning the adjusting gear.

<!-- Figure: Front fog lamp aiming screw location, source: BE.pdf page 101 -->

### Aiming Diagram Reference Points

- H1: Height between the head lamp bulb center and ground (low beam)
- H2: Height between the head lamp bulb center and ground (high beam)
- H3: Height between the fog lamp bulb center and ground
- W1: Distance between the head lamp bulb center (low beam) -- h1: Height of front side
- W2: Distance between the head lamp bulb center (high beam) -- h2: Height of rear side
- W3: Distance between the fog lamp bulb centers
- L: Distance between the head lamp bulb center and screen

<!-- Figure: Head lamp and fog lamp aiming reference diagram showing side and front views with dimensions H1, H2, H3, W1, W2, W3, L, h1, h2, source: BE.pdf page 101 -->

### Head Lamp and Fog Lamp Aiming Point

Unit: mm

| Vehicle condition | H1 | H2 | H3 | h1 | h2 | W1 | W2 | W3 | L |
|---|---|---|---|---|---|---|---|---|---|
| Without driver | 679 | 672 | 348 | 366 | 349 | 1,202 | 966 | 1,158 | 3,000 |
| With driver | 666 | 659 | 335 | - | - | | | | |

<!-- Figure: Head lamp and fog lamp aiming point measurement table, source: BE.pdf page 101 -->

### Low Beam Aiming

Turn the low beam on without driver aboard. The cut-off line should be projected in the allowable range (shaded region).

Unit: mm

<!-- Figure: Low beam aiming diagram showing vertical lines of left and right head lamp bulb centers, car axis, horizontal line of head lamp bulb center with 15 degree cut-off line, ground line, dimension H1, and W1, source: BE.pdf page 102 -->

### High Beam Aiming

Turn the high beam on without driver aboard. The hot-zone should be projected in the allowable range (shaded region).

Unit: mm

<!-- Figure: High beam aiming diagram showing vertical lines of left and right head lamp bulb centers, car axis, horizontal line of head lamp bulb center, hot-zone areas at 89/90 degree angles, ground line, dimensions H2 and W2, source: BE.pdf page 102 -->

### Front Fog Lamp Aiming

Turn the front fog lamp on without driver aboard. The cut-off line should be projected in the allowable range (shaded region).

Unit: mm

<!-- Figure: Front fog lamp aiming diagram showing vertical lines of left and right fog lamp bulb centers, car axis, horizontal line of fog lamp bulb center, 60mm offset cut-off line, ground line, dimensions H3 and W3, source: BE.pdf page 103 -->

---

# Auto Lights Control System

## Auto Light Sensor

### Description

The auto light control system operates by using the auto light sensor. The auto light sensor detects the illumination, then turns the head lamp and tail lamp on or off automatically in accordance with the detection illumination.

<!-- Figure: Auto light sensor location on dashboard, source: BE.pdf page 104 -->

### Specifications

| Items | Specifications |
|---|---|
| Rated voltage | DC 5V |
| Operating current | Max. 1mA |
| Detection illumination | |
| Tail lamp - ON | 23.1 +/- 3.4 (Lux), 1.77 +/- 0.08 (V) |
| Tail lamp - OFF | 46.0 +/- 3.4 (Lux), 1.27 +/- 0.10 (V) |
| Head lamp - ON | 6.2 +/- 1.4 (Lux), 0.63 +/- 0.06 (V) |
| Head lamp - OFF | 12.0 +/- 1.4 (Lux), 1.02 +/- 0.06 (V) |

### Circuit Diagram

<!-- Figure: Auto light sensor circuit diagram showing auto light sensor connected to BCM (Vout), with sensor power, signal, and ground lines. Fuse connections through J11 and J10, ground at I1B, source: BE.pdf page 105 -->

**Connector [M07]:**

| Pin No. | Description |
|---|---|
| 1 | Ground |
| 2 | Sensor power (5V) |
| 3 | Signal |
| 4 | - |
| 5 | - |

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|

### Inspection

1. Detach the auto light sensor in the upper crash pad.

<!-- Figure: Auto light sensor removal from crash pad, source: BE.pdf page 105 -->

2. Check the continuity between terminal 2(+) and terminal 1(-).

3. Check the continuity between the terminals while operating the switch.

<!-- Figure: Auto light sensor connector M07 terminal identification, source: BE.pdf page 105 -->

### Auto Light Switch [M01-2]

<!-- Figure: Auto light switch knob showing positions: Auto, parking lights, headlights, off, source: BE.pdf page 106 -->

| Terminal / Position | 14 | 15 | 16 | 17 |
|---|---|---|---|---|
| OFF | | | | |
| I | O-- | | | --O |
| II | O-- | --O | --O | --O |
| AUTO | | | O-- | --O |

<!-- Figure: Auto light switch M01-2 continuity table, source: BE.pdf page 106 -->

---

# Daytime Running Lights

## DRL Control Module

### Circuit Diagram

#### [TYPE 1] - Sweden area

<!-- Figure: Type 1 DRL circuit diagram showing alternator, ignition switch, ETACS connections, head lamp relay, tail lamp relay, DRL unit, rheostat, and dimmer & passing switch. Shows fuse connections (10A, 15A) from BATT 12V, source: BE.pdf page 107 -->

**Connector [EK7]:**

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| 7 | 8 | 9 | 10 | 11 | 12 |

> **NOTE:**
> TYPE 1: SWEDEN area
> TYPE 2: NORWAY area

#### [TYPE 2] - Norway area

<!-- Figure: Type 2 DRL circuit diagram showing alternator, ignition switch, ETACS connections, head lamp relay, tail lamp relay, DRL unit, rheostat, and dimmer & passing switch. Shows fuse connections (10A, 15A) from BATT 12V, source: BE.pdf page 108 -->

**Connector [EK7]:**

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| 7 | 8 | 9 | 10 | 11 | 12 |

### Inspection

#### Operation Check

Check that the lights operate according to the following timing chart.

**[TYPE 1]:**

| Signal | Sequence |
|---|---|
| IGN SWITCH | ON then OFF |
| ALTERNATOR "L" | Active during running |
| D.R.L. | ON during running |
| TAIL LAMP | Follows lighting switch |
| HEADLAMP | ON during running (auto) |

**[TYPE 2]:**

| Signal | Sequence |
|---|---|
| IGN SWITCH | ON then OFF |
| ALTERNATOR "L" | Active during running |
| D.R.L. | ON during running |
| TAIL LAMP | ON during running |
| HEADLAMP | Follows lighting switch |

<!-- Figure: DRL timing charts for Type 1 (Sweden) and Type 2 (Norway), source: BE.pdf page 109 -->

#### Inspect Circuits for Daytime Running Light System

1. Disconnect the wire connector to DRL module from engine compartment.

<!-- Figure: DRL module location in engine compartment, source: BE.pdf page 109 -->

2. Inspect the connector on wire harness side as shown.

**Connector (Harness side):**

| 6 | 5 | 4 | 3 | 2 | 1 |
|---|---|---|---|---|---|
| 12 | 11 | 10 | 9 | 8 | 7 |

<!-- Figure: DRL harness side connector, source: BE.pdf page 109 -->

#### DRL Module Connector Test Table

| Check For | Test Connect | Condition | Test Specification |
|---|---|---|---|
| Continuity | 5-Ground | Head lamp switch OFF | No continuity |
| | | Head lamp switch ON | Continuity |
| | 6-Ground | Constant | Continuity |
| | 9-Ground | Dimmer/passing switch - Head light ON | Continuity |
| | | Dimmer/passing switch - Head light OFF | No continuity |
| Voltage | 9-Ground | Ignition switch ON | Battery voltage |
| | | Ignition switch ACC or LOCK | No voltage |
| | 5-Ground | Ignition switch ON | Battery voltage |
| | | Ignition switch ACC or LOCK | No voltage |
| | 7-Ground | Constant | Battery voltage |
| | 3-Ground | Engine Stop | No voltage |
| | | Engine Running | Battery voltage |

3. If circuit is not as specified, refer to schematic diagram and inspect for short circuits.

---

# Head Lamp Levelling Device

## Head Lamp Levelling Switch

### Circuit Diagram

<!-- Figure: Head lamp levelling switch circuit diagram showing head lamp relay and tail lamp relay connections, resistors R1-R5 for positions 0-3, rheostat, and LH/RH head lamp levelling actuators, source: BE.pdf page 111 -->

### Pin Connection

**Connector [M12]:**

| Pin No. | Description |
|---|---|
| 1 | Illumination (+) |
| 2 | Rheostat |
| 3 | Ground |
| 4 | IGN |
| 5 | Actuator (+) |

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|

### Inspection

1. Disconnect the switch connector from the crash pad lower panel.

**Connector [M12]:**

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|

2. Connect the battery voltage between terminals 3 and 4 (Reference voltage = V_R).

3. Measure the voltage between terminals 3 and 5(V).

4. Check the percent ratio (V/V_R x 100%) between voltages V_R and V at each position.

| Position No. | Rotation | Ratio (%) | Voltage (V) |
|---|---|---|---|
| 0 | 0 deg | 85% | 11.05 +/- 0.5V |
| 1 | 30 deg | 70% | 9.1 +/- 0.5V |
| 2 | 60 deg | 56% | 7.28 +/- 0.5V |
| 3 | 90 deg | 45% | 5.85 +/- 0.5V |

5. If the voltage is not as specified, replace the head lamp levelling switch.

<!-- Figure: Head lamp levelling switch rotation positions and voltage test, source: BE.pdf page 112 -->

---

# Immobilizer Control System

## General

There are two types of immobilizer functions available on the Body Control Module (BCM). The first is a "SMARTRA (SMARTRA Transceiver Antenna)" type and the second is a "Stand alone" type that will emulate the system known as the "SCC immobilizer." The hardware to support the selection of immobilizer type on the BCM is identical. The selection of immobilizer type when the BCM is activated by setting the appropriate EEPROM bits. All communications between the BCM and the ECM (Engine Control Module) for the purpose of immobilization will be over the W line.

### System Block Diagram

The source of diagnostics commands for immobilizer equipped ECM is different depending upon the type of immobilizer used. The diagnostics communication for the SMARTRA system will be performed by communicating with the ECM on its K line.

In the case of a BCM that has an immobilizer, the detection of a tester being present will cause the K-line relay to close and the Diag pull up to be switched off. This mode of the diagnostics interface is called "Diagnostic Mode." This will then remain the case until the setter is disconnected. When the K-line enable relay is off and the Diag pull up is enabled, the ECM cannot communicate with the HI-SCAN tool directly.

### 1. SMARTRA type immobilizer

The "SMARTRA" type immobilizer system is applied to the 1.6 engine and 2.0 engines.

The immobilizer system consists of a passive challenge-response (mutual authentication) transponder inside the key head, a stand alone antenna, the BCM unit and the ECM. The BCM unit shall emulate the original SMARTRA immobilizer as closely as possible. The interface from the antenna shall be known as SMARTRA. SMARTRA shall just be known as SMARTRA.

In the SMARTRA system, the immobilizer is contained within the ECM. The BCM shall provide the low-level routines and functions necessary to communicate with the transponder.

### 2. Stand alone type immobilizer

The "Stand alone" type immobilizer system is applied to the 2.7 engine.

The immobilizer system consists of a passive challenge-response (mutual authentication) transponder inside the key head, a stand alone antenna, the BCM unit and the ECM. The BCM unit shall emulate the original SCC type immobilizer to ECM protocol as closely as possible.

In the stand alone immobilizer system, the immobilizer is contained within the BCM. The ECM shall request the BCM for permission to start the vehicle. The BCM shall perform the immobilisation functions and reply "start" or "no start" permission to the ECM.

<!-- Figure: Immobilizer system block diagrams for SMARTRA type (1.6a/2.0b engine) and Stand Alone type (2.7d engine), showing ECM, BCM, Transponder, K-Line, W-Line, DCT, and HI-SCAN connections, source: BE.pdf page 114 -->

## System Components

### Transponder (Built-in keys)

When ignition is ON, the coil supplies energy to the transponder, which in turn accumulates energy in the condenser. Once the energy supplied from the coil has stopped, the transponder begins reading out the ID data from the EEPROM and transmitting the secret data. The transponder has an advanced encryption algorithm. During the key teaching procedure, the transponder will be programmed with vehicle specific data. The vehicle specific data are written into the transponder memory. The write procedure is once only; therefore, the contents of the transponder can never be modified or changed.

### Coil Antenna

Supplies energy to the transponder. Receives signal from the transponder. Sends transponder signal to the BCM.

<!-- Figure: Coil antenna unit, source: BE.pdf page 115 -->

### Body Control Module (BCM)

The BCM carries out communication with the built-in transponder in the ignition key. The wireless communication runs on RF (Radio Frequency). The RF signal (responses) from the transponder is converted into messages for serial communication by the BCM. Also, the received messages from the ECM are converted into an RF signal, which is transmitted to the transponder by the antenna.

In case of "SMARTRA" type immobilizer system, the BCM does not carry out the validity check of the transponder data. This device is only an advanced interface, which provides bi-directional line of communication to enable serial communication and vice versa.

### Engine Control Module (ECM)

In case of "SMARTRA" type immobilizer system, the ECM carries out a check of the ignition key using a special encryption algorithm, which is programmed into the ECM as well as the ECM simultaneously. Only if the results are equal can the engine be started. The data of all transponders, which are valid for the vehicle, are stored in ECM.

<!-- Figure: ECM unit, source: BE.pdf page 115 -->

### Data Link Connector (DLC)

By connecting the voltmeter or Hi-scan, the control module diagnostic code can be read.

<!-- Figure: DLC connector pinout, source: BE.pdf page 116 -->

### Diagnostic Tester

Has the function BCM, ECM, and key diagnosis and change.

<!-- Figure: Diagnostic tester (HI-SCAN), source: BE.pdf page 116 -->

## Immobilizer States

The ECM has three defined states. These are described below.

### 1. Engine Control Module (ECM) States

| State | Description |
|---|---|
| Virgin State | The ECM is delivered to HMC in virgin state. There is no Vehicle Identification Number (VIN) stored in the ECM. It can only be in virgin state once. The ECM will allow starting on the second cycle of ignition. Virgin state is exited when a VIN has successfully been taught by the BCM. |
| Learnt State | Engine start is possible only when the received VIN from the BCM matches that stored in the ECM. |
| Neutral State | Same as virgin state except engine starting not possible on the second cycle of ignition. Neutral state is entered at the BCM changes to neutral state. |

### 2. Body Control Module (BCM) States

The Body Control Module (BCM) has three defined states. These are described below.

| State | Description |
|---|---|
| Virgin State | The BCM is set to virgin state during manufacture. The BCM must be set to learnt state before leaving an initial BCM command. The diagnostics password is set to the default. No VIN is stored. Virgin state is exited after the VIN been learned. |
| Learnt State | The BCM contains a VIN. |
| Neutral State | The BCM is set to neutral state by issuing a "Teaching ECM" command. The purpose of the neutral state is to allow the ECM to be set to neutral state. The BCM neutral state expires 15 seconds after an ignition ON-OFF cycle. |

## Teaching Procedures

### 1. Key Teaching Procedure

Key teaching must be done after replacing a defective ECM or when providing additional keys to the vehicle owner.

The procedure starts with an ECM request for vehicle specific data from the tester. The "virgin" ECM stores the vehicle specific data and the key teaching can be started. The "learnt" ECM compares the vehicle specific data from the tester with the stored data. If the data are correct, the teaching can proceed.

If incorrect vehicle specific data have been sent to the ECM three times, the ECM will reject the request of key teaching for one hour. This time cannot be reduced by disconnecting the battery or other manipulation. After reconnecting the battery, the timer starts again for one hour.

The key teaching is done by ignition on with the key and additional tester commands. The ECM stores the relevant data in the EEPROM and in the transponder. Then the ECM runs the authentication required for confirmation of the teaching process. The successful programming is then confirmed by a message to the tester.

If the key is already known to the ECM from a previous teaching, the authentication will be accepted and the EEPROM data are updated. There is no changed transponder content (this is impossible for a learnt transponder).

The attempt to repeatedly teach a key, which has been taught already during the same teaching cycle, is recognized by the ECM. This rejects the key and a message is sent to the tester.

The ECM rejects invalid keys, which are presented for teaching. A message is sent to the tester. The key can be invalid due to faults in the transponder or other reasons, which result from unsuccessful programming of data. If the ECM detects different authentications of a transponder and an ECM, the key is considered to be invalid.

The maximum number of taught keys is 4.

If an error occurs during the Immobilizer Service Menu, the ECM status remains unchanged and a specific fault code is stored.

If the ECM and the key status do not match for teaching of keys, the tester procedure will be stopped and a specific fault code will be stored at ECM.

### 2. User Password Teaching Procedure

The user password for limp home is taught at the service station. The owner of the vehicle can select a number with four digits.

The teaching is started by ignition on, with a valid key and sending the user password by tester. After successful teaching, the status of the user password changes from "virgin" to "learnt."

User password teaching is only accepted by a "learnt" ECM. Before first teaching of user password to an ECM, the status of the password is "virgin." No limp home function is possible.

The learnt user password can also be changed. This can be done if the user password status is "learnt" and the tester sends authorization of access, either the old user password or the vehicle specific data. After correct authorization, the ECM requests the new user password. The status remains "learnt" and the new user password will be valid for the next limp home mode.

If incorrect user passwords or wrong vehicle specific data have been sent to the ECM three times, the ECM will reject the request to change the password for one hour. This time cannot be reduced by disconnecting the battery or any other actions. After reconnecting the battery, the timer starts again for one hour.

#### The User Password Can Be In the Status

**00. Not yet checked**

The status is stored in the EEPROM. In case of incorrect or no plausible data from this circuit, the ECM cannot check the status and the ECM sends 00.

**01. Learnt**

The password has been taught successfully to the ECM.

**02. Virgin**

This is the status at the end of the ECM production line before delivery to the final customer.

**04. Locked by timer**

After a certain number of incorrect inputs, the ECM is locked for one hour and no inputs are accepted during this time.

**05. Teaching not accepted**

This status is set if, for example, the ECM is in neutral state.

## Limp Home Function

Limp home mode allows the driver to start a car when the immobilizer system has failed but the BCM is still able to communicate with the ECM. When the limp home is activated, the ECM still communicates with the BCM via the K-line / W-line. The limp home function within the ECM is regardless of the values of the VIN, MIN, Transponder or Random number stored within the BCM.

Limp home mode is activated by "entering" the limp home password of the system via activation of the ignition key. The timing of entering the password are shown below in timing chart.

The password is stored in EEPROM. The password is also stored in RAM. If both the EEPROM and RAM copy match then the vehicle is allowed to start once upon the next cycle of ignition. After the vehicle has been allowed to start once, the RAM copy is cleared thus preventing further starting.

At limp mode, the owner is asked to choose a password which is 4 digit (2 bytes) in length. All digits chosen by the user must be between zero and nine. This password is placed within the BCM EEPROM using the Hi scan command.

If limp home mode is required, the owner enters the password via the ignition key. The password is decoded by the BCM then placed in RAM for comparison with the EEPROM copy. The password may also be placed directly in RAM using the Hi Scan. However, the tester must be still connected at the time of starting.

If the user forgets the password, the dealer shall use the forgotten password menu on the HiScan. The HiScan will prompt the dealer to enter the pin code as obtained from the HMC database for the vehicle in question.

> **NOTE**
> The password and the pin code are not the same. Pin code is scanned from a bar code at the End Of Line (EOL). The password is a number chosen by the owner for the purposes of limp starting.

In case of "SMARTRA" type immobilizer system, only if the ECM is in status "learnt" and the user password status is "learnt," the ECM will be unlocked for a period of time (90 sec.). The engine can be started during this time. After the time has elapsed, engine start is not possible. After a new password has been input, the timer (90 sec.) will start again.

But the ECM unlock time (90 sec.) is not necessary in the "Stand alone" type immobilizer system.

But in case of "Stand alone" type immobilizer system, the ECM is locked instantly after ignition off.

### Limp Home Activation Methods

#### 1. By tester

If the ECM detects the fault of the BCM or transponder, the ECM will allow limp home function of the immobilizer. Limp home is only possible if the user password (4 digits) has been given to the ECM before. This password can be selected by the vehicle owner and is programmed at the service.

The user password can be sent to the ECM via the Hi-scan.

In case of "SMARTRA" type immobilizer system, only if the ECM is in status "learnt" and the user password status is "learnt," will the ECM be unlocked for a period of time (90 sec.). The engine can only be started during this time. After the time has elapsed, engine start is not possible. After reconnecting the battery to the ECM, the timer starts again.

But the ECM unlock timer (90 sec.) is not necessary in the "Stand alone" type immobilizer system.

#### 2. By ignition key

The limp home can be activated also by the ignition key. The user password can be input to the ECM by a special sequence of ignition on/off.

Limp home code entry is enabled after the key has been in the ignition position for greater than 5 seconds. If the ignition is on for longer than 10 seconds during the sequence, the sequence is then restarted and all timers are cleared. If the ignition is turned off for more than 3 seconds during the entry, the code number for that digit of the limp home password is determined. If the ignition is turned off for longer than 10 seconds at any time before during or after code entry, all timers are cleared and limp home mode is deactivated. The number "D" is represented by 10 cycles of the ignition key.

Only if the ECM is in status "learnt" and the user password status is "learnt," will the ECM be unlocked for a period of time (90 sec.). The engine can be started during this time. After the time has elapsed, engine start is not possible. After a new password has been input, the timer (90 sec.) will start again.

But in case of "Stand alone" type immobilizer system, the engine start is possible after the timer (90 sec.) has elapsed.

### Limp Home Timing Diagrams

#### [SMARTRA TYPE]

**Normal Condition:**
- IGN On -> Start (within T5) -> Start (within T6)

**Start Possible:**
- User Password (1234H) entered via ignition cycling
- T1 > 5 sec
- 3 sec < T2 < 10 sec
- 0.2 sec < T3 < 5 sec
- 0.2 sec < T4 < 3 sec
- After password entry, engine stall recovery within T7

**Start Impossible:**
- Password entered incorrectly -> Start attempts fail

#### [STAND ALONE TYPE]

**Start Possible:**
- User Password (1234H) entered via ignition cycling
- Limp home activated indication shown
- Same timing constraints as SMARTRA type

**Timing Values:**
- T1 > 5 sec
- 3 sec < T2 < 10 sec
- 0.2 sec < T3 < 5 sec
- 0.2 sec < T4 < 3 sec
- T5 < 5 sec
- T6 < 30 sec
- T7 < 8 sec

<!-- Figure: Limp home timing diagrams for SMARTRA type (normal condition, start possible, start impossible) and Stand Alone type (start possible), showing IGN on/off sequences and user password entry via ignition cycling, source: BE.pdf page 119 -->

### Immobilizer Activation by Tester

If the wrong user password is sent, the ECM will reject the request of limp home for one hour. Disconnecting the battery or any other action cannot reduce that time. After reconnecting the battery to the ECM, the timer starts again.

But in case of "Stand alone" type immobilizer system, the ECM is locked instantly after ignition off.

### Immobilizer Activation by Ignition Key

The limp home can be activated also by the ignition key. The user password can be input to the ECM by a special sequence of ignition on/off.

Limp home code entry is enabled after the key has been in the ignition position for greater than 5 seconds. If the ignition is on for longer than 10 seconds during the sequence, the sequence is then restarted and all timers are cleared. If the ignition is turned off for more than 3 seconds during the entry, the code number for that digit of the limp home password is determined. If the ignition is turned off for longer than 10 seconds at any time before, during, or after code entry, all timers are cleared and limp home mode is deactivated. The number "D" is represented by 10 cycles of the ignition key.

Only if the ECM is in status "learnt" and the user password status is "learnt" will the ECM be unlocked for a period of time (90 sec.). The engine can be started during this time. After the time has elapsed, engine start is not possible. After a new password has been input, the timer (90 sec.) will start again.

But in case of "Stand alone" type immobilizer system, the engine start is possible after the timer (90 sec.) has elapsed.

## Replacement of ECM and BCM

### ECM Replacement

In case of a defective ECM, the unit has to be replaced with a "virgin" or "neutral" ECM. All keys have to be programmed into the new ECM as well. Keys, which are not programmed into the ECM, are invalid for the new ECM (Refer to key teaching procedure). The vehicle specific data have to be left unchanged due to the unique programming of transponders.

In case of a defective BCM, there is no special procedure required. A new BCM simply replaces the old one. There are no transponder-related data stored in this device.

### Neutralising ECM

The ECM can be set to the "neutral" status by a tester.

## Diagnosis of Immobilizer Related Faults

The diagnosis monitors:
- Communication between the ECM and the BCM
- Function of the BCM and the transponder, and
- Data (stored in the ECM) related to the immobilizer function.

There are four different faults that are assigned to the immobilizer system. Every fault is broken down into four different types (circuit malfunction, circuit range / performance problem, low input, high input). The following table shows the assignment of immobilizer related faults to each type:

### SMARTRA (1.6a / 2.0b Engine)

| Type | Diagnostic Code | Immobilizer Related Faults | Fault types |
|---|---|---|---|
| | P1610 | | No answer from the BCM. Invalid message from BCM to ECM |
| | P1800 | BCM fault | Antenna error |
| | P1803 | | Invalid request from ECM or corrupted data |
| | P1801 | Transponder fault | Invalid transponder signal. Passive mode invalid. Programming error |
| | P1805 | EEPROM | Inconsistent data of EEPROM. Invalid write operation to EEPROM. No valid data from BCM after 3 attempts by ECM. Invalid tester message or unexpected requests by tester |
| | | ECM fault | Transponder error due to a wrong code, untagged, bad touch on bad read. |

### STAND ALONE (2.7 Engine)

| Type | Diagnostic Code | Immobilizer Related Faults | Fault types |
|---|---|---|---|
| 01 | | ECM communication error | ECM error due to bad SID, bad MID or protocol error |
| 02 | | ECM communication error | Keyless entry problem (no keys taught to ECM) |
| 04 | | Immobilizer antenna error | Open immobilizer antenna |
| 05 | | BCM internal fault | BCM internal fault (smart driver failure) |
| 06 | | BCM EEPROM error | EEPROM error detected in ECM |
| 07 | | ECM signal not detected | ECM signal not detected |

### Replacement of ECM and BCM (Additional Notes)

A valid ignition key is inserted and after ignition on it should be waiting for the communication between ECM and the tester. The communication messages are described by the "teach mode." After successfully receiving the data, the ECM is neutralized.

The ECM remains locked. Neither the limp home mode nor the "New ignition on" function, is accepted by the ECM.

The teaching of keys follows the procedure described for the virgin ECM. The vehicle specific data have to be unchanged due to the unique programming of the transponder. If data should be changed, new keys with a virgin transponder are requested.
