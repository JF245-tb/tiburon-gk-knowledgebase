---
source: BR.pdf
chapter: BR
section: BR-54 to BR-75
pages: 54-75
engine: V6
title: ABS/TCS (Part 2)
---

# ABS / TCS (Part 2)

## DTC Descriptions (Continued)

<!-- EJOC5600 -->

### DTC No. C1605 — CAN Hardware Error

**Probable cause:**

- Interference by means of electronic wave
- Mismatching of the calculation between main and sub processor
- Defects of the valve coil and valve coil operating circuit element

**Action:** Replace the HECU.

---

### DTC No. C1611 — CAN Timeout EMS / C1612 — CAN Timeout TCU / C1613 — CAN Wrong Matched Transmission

**Probable cause:**

- No message from EMS or TCU for 500ms
- Message from A/T or M/T signal mismatching the message from ECM or TCU

**Action:** Inspect the EMS or TCU according to the instructions of Engine or T/M group.

---

### DTC No. C1610 — Bus Off Error

**Probable cause:**

- CAN bus cable open, or short to ground or battery

**Action:** Check CAN bus wiring. Check E37, C03, C133-4 or M42 connectors.

---

### DTC No. C2402 — Motor Pump Failure (Motor Relay, Motor)

**Probable cause:**

- Malfunction of wiring harness
- Malfunction of HECU

When the motor power line is normal but no signal is detected in the motor monitor line.

> **CAUTION**
> Powering the motor with the Hi-Scan (Pro) will discharge the battery. Start and run the engine for a while after testing is complete.

#### Motor Pump Failure Diagnostic Flowchart

1. **Hi-Scan (Pro) actuator test** — Is the sound of the motor operating heard?
   - **YES** → Check the harness and repair if necessary.
   - **NO** → Continue to step 2.

2. **Motor power source inspection** — Terminal 25 of HECU connector E37.
   - **YES** → Continue.
   - **NO** → Continue to step 3.

3. **Disconnect the connector E37** — Check the voltage at the connector E37, terminal 25.
   - **OK (System voltage)** → Replace the HECU.
   - **NG** → Repair the harness or connector.

<!-- Figure: Motor pump failure diagnostic flowchart, source: BR.pdf page 54 -->

---

## Inspection Chart for Trouble Symptoms (Continued)

<!-- EJOC5700 -->

Find out the symptom and check according to the inspection procedure chart.

| Trouble system | Inspection procedure No. |
|---|---|
| Communication with Hi-Scan (Pro) is not possible. Communication with any system is not possible. | 1 |
| Communication with ABS only is not possible. | 2 |
| When the ignition key is turned to "ON" (engine OFF), the ABS warning lamp does not illuminate. | 3 |
| After the engine starts, the lamp remains illuminated. | 4 |
| Faulty ABS operation — Unequal braking power on both sides | 5 |
| Insufficient braking power | - |
| ABS operates under normal braking conditions | - |
| ABS operates before vehicle stops under normal braking conditions | - |
| Large brake pedal vibration (See Caution) | - |

> **CAUTION**
> During ABS operation, the brake pedal may vibrate or may not be able to be depressed. Such phenomena are due to intermittent changes in hydraulic pressure inside the brake line to prevent the wheels from locking and is not an abnormality.

---

## Inspection Procedures for Trouble Symptoms

### Inspection Procedure 1

<!-- EJOC5710 -->

**Symptom:** Communication with Hi-Scan (Pro) is not possible. (Communication with all systems is not possible.)

**Probable cause:**

- Malfunction of connector (ground) for the diagnosis line
- Malfunction of wiring harness

**Action:** Possible defect in the power supply system (including ground) for the diagnosis line.

---

### Inspection Procedure 2

<!-- EJOC5720 -->

**Symptom:** Communication with Hi-Scan (Pro) is not possible. (Communication with ABS only is not possible.)

**Probable cause:**

- Blown fuse
- Malfunction of wiring harness or connector
- Malfunction of HECU

When communication with Hi-Scan (Pro) is not possible, the cause may be probably an open circuit in the HECU power circuit or an open circuit in the diagnosis output circuit.

#### Diagnostic Flowchart

1. **Measure the resistance between DLC and HECU connector E37, terminal 7.**
   - Disconnect the connector and measure at the harness side.
   - Continuity between the following terminals: between terminal 7 on HECU and terminal 1 on DLC side.
   - **OK (Continuity)** → Continue to step 2.
   - **NG** → Check the harness between the HECU and diagnosis connector, and repair if necessary.

2. **Check the following connector: MCO1 or ECO2.**
   - **OK** → Check symptoms of trouble.
   - **NG** → Repair.

3. **Measure the resistance HECU connector E37.**
   - Disconnect the connector and measure at the harness side.
   - Ignition switch: ON
   - Voltage between terminal 4 and body ground.
   - **OK (System voltage)** → Continue to step 4.
   - **NG** → Check the harness between the No.28 fuse (10A) inside the ECM unit and HECU, and repair if necessary.

4. **Measure the resistance HECU connector E37.**
   - Disconnect the connector and measure at the harness side.
   - Continuity between terminal 24, 8 and body ground.
   - **OK (Continuity)** → Continue to step 5.
   - **NG** → Repair.

5. **Check the following connector (E37).**
   - **OK** → Check symptoms of trouble.
   - **NG** → Replace the HECU.

<!-- Figure: Inspection procedure 2 flowchart, source: BR.pdf page 56 -->

---

### Inspection Procedure 3

<!-- EJOC5730 -->

**Symptom:** When ignition key is turned "ON" (engine OFF), the ABS warning lamp does not illuminate.

**Probable cause:**

- Blown fuse
- Burnt out ABS warning lamp bulb
- Malfunction of wiring harness or connector

When current flows in the HECU, the ABS relay turns on, to do the initial check. The ABS warning lamp will illuminate when the ABS relay is off even if there is a problem with the circuit between the ABS warning lamp and the HECU. Therefore, if the lamp does not illuminate, the cause may be an open circuit in the lamp power supply circuit, a blown bulb, an open circuit in both the circuits between the ABS warning lamp and the HECU, and in the circuit between the ABS warning lamp and the ABS relay.

#### No. 17 Fuse (10A) Inspection

1. **Fuse OK** → Continue to step 2.

2. **Measure the resistance at connector M10-2.**
   - Disconnect the connector and measure at the pin.
   - Check the ABS warning lamp illuminates when terminal(10) is grounded.
   - **OK (Illuminates)** → Continue to step 3.
   - **NG** → Check whether the ABS warning lamp bulb is burnt out.
     - **Bulb OK** → Check the connectors.
       - **OK** → Check symptoms of trouble.
       - **NG** → Repair.
     - **Bulb NG** → Replace the ABS warning lamp bulb.

3. **Check the harness.** Repair, if necessary.
   - If symptoms of trouble remain → Replace the combination meter.

<!-- Figure: Inspection procedure 3 flowchart, source: BR.pdf page 57 -->

---

### Inspection Procedure 4

<!-- EJOC5740 -->

**Symptom:** Even after the engine is started, the ABS warning lamp remains illuminated.

**Probable cause:**

- Malfunction of combination meter
- Malfunction of HECU
- Malfunction of wiring harness

A possible short-circuit in the ABS warning lamp illumination circuit.

This trouble symptom is limited to cases where communication with the Hi-Scan (Pro) is possible (HECU power supply is normal and DTC is normal).

#### Diagnostic Flowchart

1. **Disconnect connector M10-1 and M10-2 and turn the ignition switch ON.**
   - Does the ABS warning lamp remain illuminated?
   - **YES** → Replace the combination meter.
   - **NO** → Continue to step 2.

2. **Disconnect HECU connector E37.**
   - Ignition switch: ON
   - Does the ABS warning lamp switch off?
   - **YES** → Replace the HECU.
   - **NO** → Check the harness between the combination meter and the HECU. Repair, if necessary.

<!-- Figure: Inspection procedure 4 flowchart, source: BR.pdf page 58 -->

---

### Inspection Procedure 5

<!-- EJOC5750 -->

**Symptom:** Brake operation is abnormal.

**Probable cause:**

- Malfunction of wheel speed sensor
- Malfunction of rotor
- Malfunction of wheel bearing
- Malfunction of HECU

Brake operation varies depending on driving conditions and road surface conditions, so diagnosis can be difficult. However, if a normal DTC is displayed, carry out the following inspection.

#### Diagnostic Flowchart

1. **Inspect wheel speed sensor installation.**
   - **NG** → Repair.
   - **OK** → Continue to step 2.

2. **Inspect wheel speed sensor output voltage.**
   - **NG** → Inspect wheel speed sensor.
     - **NG** → Replace the wheel speed sensor.
     - **OK** → Inspect rotor.
       - **NG** → Replace the rotor (or excitor).
       - **OK** → Continue to hydraulic unit inspection.

3. **Hydraulic unit inspection.**
   - Inspect wheel bearing.
   - **NG** → Repair.
   - **OK** → Check the following connectors: E01, E39, M64, MM09, M65, MM07, EM01.
     - **NG** → Repair.
     - **OK** → Check symptoms of trouble.

4. **Measure the resistance at HECU connector E37.**
   - Disconnect the connector and measure at the harness side.
   - Resistance value between terminals: 1, 19-2, 20 and 5, 22-6, 23.
   - **OK (1,385 +/- 110 ohm)** — While these measurements are carried out, the connector should be moved around to detect intermittent connections.
   - **NG** → Repair.

5. **Check the following connector (E37).**
   - **OK** → Check symptoms of trouble.
   - **NG** → Replace the HECU.

<!-- Figure: Inspection procedure 5 flowchart, source: BR.pdf page 59 -->

---

## Anti-Lock Braking System Control Module

### Components

<!-- EJOC5800 -->

<!-- Figure: HECU exploded view showing ABS control module (HECU), bracket, and mounting bolts, source: BR.pdf page 60 -->

| Component | Torque |
|---|---|
| Bracket mounting bolt | 8-10 Nm (80-100 kg-cm, 5.9-7.3 lb-ft) |

**TORQUE: Nm (kg-cm, lb-ft)**

---

### HECU

<!-- EJOC5900 -->

#### ABS ECU Valve Layout

<!-- Figure: ABS ECU connector face showing valve positions, source: BR.pdf page 61 -->

| Position | Function |
|---|---|
| A | Inlet valve (FR) |
| B | Inlet valve (FL) |
| C | Inlet valve (RR) |
| D | Inlet valve (FL) |
| E | Outlet valve (FR) |
| F | Outlet valve (FL) |
| G | Outlet valve (RR) |
| H | Outlet valve (FL) |
| M | Motor (+) |
| N | Motor (-) |

#### TCS ECU Valve Layout

<!-- Figure: TCS ECU connector face showing valve positions, source: BR.pdf page 61 -->

| Position | Function |
|---|---|
| A | Inlet valve (FR) |
| B | Inlet valve (FL) |
| C | Inlet valve (RR) |
| D | Inlet valve (FL) |
| E | Outlet valve (FR) |
| F | Outlet valve (FL) |
| G | Outlet valve (RR) |
| H | Outlet valve (FL) |
| I | Traction valve (RH) |
| J | Traction valve (LH) |
| M | Motor (+) |
| N | Motor (-) |

---

### HECU Block Diagram

<!-- EJOC5904 -->

#### 1. Input/Output Diagram

<!-- Figure: HECU input/output block diagram, source: BR.pdf page 62 -->

**Inputs:**

| Pin | Signal |
|---|---|
| 4 | IGN (+) |
| 25 | Motor |
| 25 | Valve |
| 18 | Stop lamp switch |

**Wheel speed sensor inputs:**

| Pin | Signal |
|---|---|
| 1 | FL 1 |
| 2 | FL 0 |
| 19 | FR 1 |
| 20 | FR 0 |
| 5 | RL 1 |
| 6 | RL 0 |
| 22 | RL 1 |
| 23 | RR 0 |

**Outputs:**

| Pin | Signal |
|---|---|
| 7 | Diagnosis |
| 16 | ABS & EBD Warning lamp |
| 17 | TCS lamp |

**HECU internal blocks:** System, Motor, Valve

---

#### 2. ABS ECU Block Diagram

<!-- Figure: ABS ECU internal block diagram, source: BR.pdf page 63 -->

**Power supply:**
- IGNITION
- BATT 1
- BATT 2

**Internal components:**
- Voltage Regulator
- Processor 1 (16bit)
- Processor 2 (8bit)
- 8 x Valve Driver → Solenoid Valves
- Interface Circuit
- A/D Monitor Circuit
- Motor relay & TDR Driver Circuit
- Wheel signal conditioning Circuit
- Lamp Driver Circuit → EBD Warning lamp, ABS Warning lamp
- Communication Circuit → K-Line
- Switch Control/Lamp Circuit

**External connections:**
- FR wheel sensors
- Wheel speed output
- Stop lamp switch

---

#### 3. TCS ECU Block Diagram

<!-- Figure: TCS ECU internal block diagram, source: BR.pdf page 63 -->

**Power supply:**
- IGNITION
- BATT 1
- BATT 2

**Internal components:**
- Voltage Regulator
- Processor 1 (16bit)
- Processor 2 (8bit)
- 8 x Valve Driver + 2 x Valve Driver → Solenoid Valves
- Interface Circuit
- A/D Monitor Circuit
- Motor relay & TDR Driver Circuit
- Wheel signal conditioning Circuit
- Lamp Driver Circuit → TCS Warning lamp, EBD Warning lamp, ABS Warning lamp
- Communication Circuit → K-Line
- Switch Control/Lamp Circuit
- CAN

**External connections:**
- CAN (High), CAN (Low)
- Wheel Sensors
- FR wheel speed output
- Stop lamp switch
- TCS Switch

---

### External Wiring Diagram (ABS)

<!-- EJNC504 -->

<!-- Figure: ABS external wiring diagram showing HECU pin connections to ignition switch, battery, brake switch, fuses, pump motor, wheel speed sensors (FL, FR, RL, RR), Hi-Scan, DND, wheel speed output, and main connector, source: BR.pdf page 64 -->

**Key connections:**
- Ignition switch → HECU
- Battery → Main connector → HECU
- Brake switch → HECU pin 18
- Pump motor → HECU
- Hi-Scan → HECU
- Wheel Speed Out (FR) → HECU
- Wheel Sensor (FL) → HECU pins 1, 2
- Wheel Sensor (FR) → HECU pins 19, 20
- Wheel Sensor (RL) → HECU pins 5, 6
- Wheel Sensor (RR) → HECU pins 22, 23
- GND connections to main connector

---

### External Wiring Diagram (TCS)

<!-- EJNC506 -->

<!-- Figure: TCS external wiring diagram showing HECU pin connections — same as ABS plus TCS lamp, TCS switch, CAN High, CAN Low lines, source: BR.pdf page 65 -->

**Additional TCS connections (beyond ABS):**
- TCS Lamp → HECU
- TCS Switch → HECU
- Hi-Scan → HECU
- CAN H → HECU
- CAN L → HECU
- Wheel Speed Out (FR) → HECU
- GND 1, GND 2 → Main connector

---

## Inspection at HECU Terminals

<!-- EJOC6000 -->

**(HECU Wiring Harness Side Connector)**

<!-- Figure: HECU E37 connector pin layout diagram, source: BR.pdf page 66 -->

| No. | Mark | Terminal name | Specification | Note |
|---|---|---|---|---|
| 4 | IGN+ | Power source via ignition switch terminal | Over voltage range: 16.5 < 0.5V < V < 20V | |
| | | | Operating voltage range: 9.5 < 0.5V < V < 16.5 < 0.5V | |
| | | | Under voltage range: V < 7.5 < 0.5V | |
| | | | System down range: V < 7.5 < 0.5V | |
| | | | Max. current: 300mA | |
| 8, 24 | GND1, GND2 | Ground terminal | Max. current (Total of 2 terminals): I < 60A | In ABS control |
| 18 | BRAKE | Brake lamp switch input terminal | Input voltage (Low): -1.00 < V_in < 2.00V | |
| | | | Input voltage (High): 7.00 < V_in < 16.00V | |
| 1, 19 | FL+, FR+ | Wheel sensor input terminal | Min. sensor voltage: V_p = 130mV_pp | |
| 5, 22 | RL+, RR+ | | Resistance: 1,385 +/- 110 ohm | |
| 2, 20 | FL-, FR- | | Input range: 15 - 2000Hz | |
| 6, 23 | RL-, RR- | | Inductance: 0.1H +/- 30% | |
| | | | Permissible offset voltage range: -3.15V < V_offset < 3.5V | |
| 16 | W.LP | ABS and EBD warning lamp output terminal | Max. current: I < 200mA | |
| | | | Saturation voltage, at I = 200mA: V_out < 1.5V | |
| 7 | Diag. | Diagnosis interface | Input voltage: V_in < 0.3V_cc, V_out < 2.7V_cc | V_p: Ignition voltage |
| | | | Output voltage: V_out < 0.2V_cc, V_high > 0.8V_cc | |
| 3 | FR-out | Wheel speed output | External pull up resistance: above 10 kohm | |
| | | | (Open collector type) | |
| 25 | Batt 1 | Battery power (Valve power source) | Max. current (Inside control): I < 30A | |
| | | | Max. current (Outside circuit): I < 20mA | |
| | | | At IGN off: | |
| 25 | Batt 2 | Battery power source 2 terminal (Motor power source) | Max. rush current: I < 100A (t < 150 msec) | I: The running time |
| | | | Max. current: I < 30A | |
| | | | At IGN off: | |
| | | | Dark current: I < 0.5mA | |
| 14 | TCS | TCS ON/OFF Switch | Input voltage: -1.0 < V < 16.0V | |
| 17 | TCS Lamp | TCS Warning/Function lamp output | Max. current: I < 200mA | |

### Continued HECU Terminal Specifications

| No. | Mark | Terminal name | Specification | Note |
|---|---|---|---|---|
| 10 | CAN_L | CAN Bus line (Low) | Max. current: I < 10mA | |
| 11 | CAN_H | CAN Bus line (High) | Max. current: I < 10mA | |

---

## Component Specification

<!-- EJOC6001 -->

### Wheel Speed Sensor

| Item | Content |
|---|---|
| Type | Electromagnetic induction type |
| Resistance | 1,385 +/- 110 ohm |
| Output range | 15 - 2000Hz |
| Inductance | 0.1H +/- 30% |

### ABS/EBD Warning Lamp Circuit

- Type: Active ABS and EBD warning module
- Max. current: I < 200mA

<!-- Figure: ABS/EBD warning lamp circuit schematic showing ECU connection through transistor driver, source: BR.pdf page 67 -->

### Timing Diagram for Driving the ABS and EBD Warning Lamp Module

<!-- Figure: Timing diagram showing three sequences (sequence 1: ABS on/EBD init off; sequence 2: transition; sequence 3: both active), V_ECU and V_EBD voltage of ECU side, source: BR.pdf page 67 -->

### Diagnosis Tester

- Pulled up in ignition voltage by 220 kohm

<!-- Figure: Diagnosis tester circuit — ECU pin 7 to K line through 220 kohm pull-up to IGN, source: BR.pdf page 68 -->

### Wheel Speed Output

- Max. current: I < 10mA
- Output voltage: V < IGN
- External resistor: Must use resistance above 10 kohm

<!-- Figure: Wheel speed output circuit — ABS ECU pin 3 through 1 kohm to other ECU, external R > 10 kohm pull-up to V < IGN, source: BR.pdf page 68 -->

### Brake Lamp Switch

- Type: Contact type (Normal open)
- Pulled up in ignition voltage by 15 kohm

<!-- Figure: Brake lamp switch circuit — ECU pin 18 through 15 kohm pull-up to IGN, brake signal input, source: BR.pdf page 68 -->

### TCS Warning/Function Lamp Circuit (Only TCS System)

- Max. current: I < 200mA

<!-- Figure: TCS warning/function lamp circuit — ECU pin 17 to TCS Warning/Function lamp with IGN pull-up, source: BR.pdf page 69 -->

### TCS ON/OFF Switch

- Type: Contact type (Normal open)

<!-- Figure: TCS ON/OFF switch circuit — ECU pin 14 to TCS Switch with IGN pull-up, source: BR.pdf page 69 -->

---

## HECU Removal and Installation

### Removal

<!-- EJOC6100 -->

1. Disconnect the double lock connector from the HECU.

<!-- Figure: Disconnecting HECU connector, source: BR.pdf page 70 -->

2. Disconnect the brake tubes from the HECU.

<!-- Figure: Disconnecting brake tubes from HECU, source: BR.pdf page 70 -->

3. Remove the HECU bracket mounting bolts and remove the HECU.

> **CAUTION**
> 1. Never attempt to disassemble the HECU.
> 2. The HECU must be transported and stored in an upright position and the ports sealed. The HECU must not be drained.

<!-- Figure: Removing HECU from bracket, source: BR.pdf page 70 -->

**Tightening torque:**

HECU bracket mounting bolts:
: 17-26 Nm (170-260 kg-cm, 12.5-19.1 lb-ft)

### Installation

<!-- EJNC508 -->

1. Installation is the reverse of removal.

2. Tighten the modulator mounting bolts and brake tube nuts to the specified torque.

**Tightening torque:**

| Fastener | Torque |
|---|---|
| HECU mounting bolt | 8-10 Nm (80-100 kg-cm, 5.9-7.3 lb-ft) |
| Brake tube nut | 13-17 Nm (130-170 kg-cm, 9-12.5 lb-ft) |

---

## ABS Operation Check

<!-- EJNC510 -->

### Wheel Speed Sensor Output Voltage Check

1. Raise the vehicle and release the parking brake.

2. Disconnect the HECU harness connector's and measure from the harness side connector.

> **CAUTION**
> Be sure to remove the connector's double lock and insert the probe into the harness side (back-probe). Inserting it into the terminal side may result in a bad connection.

3. Rotate the wheel to be measured approximately 1/2 to 1 rotation per second, and check the output voltage using a circuit tester or an oscilloscope.

#### Wheel Speed Sensor Terminal Assignments

| Wheel speed sensor | Front left | Front right | Rear left | Rear right |
|---|---|---|---|---|
| Terminal 1 | 1 | 19 | 5 | 22 |
| Terminal 2 | 2 | 20 | 6 | 23 |

**Output voltage:**
When measuring with an oscilloscope: **130mV peak-to-peak or more**

<!-- Figure: Oscilloscope connected to HECU harness connector measuring wheel speed sensor output, source: BR.pdf page 71 -->

---

## Anti-Lock Braking System Wheel Speed Sensor

### Components

<!-- EJOC6800 -->

<!-- Figure: Wheel speed sensor mounting locations showing front and rear, source: BR.pdf page 72 -->

| Component | Torque |
|---|---|
| Front wheel speed sensor mounting bolt | 8.2-9.7 Nm (80-97 kg-cm, 5.7-6.8 lb-ft) |
| Rear wheel speed sensor mounting bolt | 8.2-9.7 Nm (80-97 kg-cm, 5.7-6.8 lb-ft) |

**TORQUE: Nm (kg-cm, lb-ft)**

### Removal

<!-- EJOC6900 -->

#### Front Wheel Speed Sensor

1. Remove the front wheel speed sensor mounting bolt.

<!-- Figure: Removing front wheel speed sensor mounting bolt, source: BR.pdf page 72 -->

2. Remove the front wheel speed sensor after disconnecting the wheel speed sensor connector.

<!-- Figure: Removing front wheel speed sensor from knuckle, source: BR.pdf page 72 -->

#### Rear Wheel Speed Sensor

1. Remove the rear wheel speed sensor mounting bolt.

<!-- Figure: Removing rear wheel speed sensor mounting bolt, source: BR.pdf page 73 -->

2. Remove the luggage trim and disconnect the wire connector from the rear wheel speed sensor.

<!-- Figure: Disconnecting rear wheel speed sensor connector, source: BR.pdf page 73 -->

### Inspection

<!-- EJOC6906 -->

> **NOTE**
> Set the voltmeter to measure AC voltage. Service standard: AC voltage detected.

1. Connect an ohmmeter between the wheel speed sensor terminals and measure the resistance.

**Service standard:**

Front, Rear: **1,385 +/- 110 ohm**

<!-- Figure: Measuring wheel speed sensor resistance with ohmmeter, source: BR.pdf page 73 -->

2. Connect a voltmeter between the wheel speed sensor terminals and measure the voltage by turning the wheel.

---

## Bleeding of Brake System

<!-- EJOC6908 -->

This procedure should be followed to ensure adequate bleeding of air and filling of the ABS unit, brake lines and master cylinder with brake fluid.

1. Remove the reservoir cap and fill the brake reservoir with brake fluid.

> **CAUTION**
> If there is any brake fluid on any painted surface, wash it off immediately.

> **NOTE**
> When pressure bleeding, do not depress the brake pedal.
> Recommended fluid: DOT3 or DOT4

2. Connect a clear plastic tube to the wheel cylinder bleeder plug and insert the other end of the tube into a half filled clear plastic bottle.

<!-- Figure: Bleeder tube connected to wheel cylinder, source: BR.pdf page 74 -->

3. Connect the Hi-Scan (Pro) to the Data Link Connector located underneath the dash panel.

<!-- Figure: Hi-Scan connected to DLC, source: BR.pdf page 74 -->

4. Select and operate according to the instructions of the Hi-Scan (Pro) screens.

> **CAUTION**
> You must obey the maximum operating time of the ABS motor with the Hi-Scan (Pro) to prevent the motor pump from burning.

#### Hi-Scan (Pro) Procedure

1. Select Hyundai vehicle diagnosis.

**Initial Screen:**

```
01. VEHICLE DIAGNOSIS
02. TOOL IN
03. SCANNER II DIAGNOSIS
04. FLIGHT RECORD REVIEW
05. SYSTEM SETUP
```

2. Select vehicle name.
3. Select Anti-Lock Brake system.
4. Select air bleeding mode.

5. Press "YES" to operate motor pump and solenoid valve.

**1.5 Air Bleeding Mode — Initial Screen:**

```
ABS AIR BLEEDING STATUS

01. SOLENOID VALVE STATUS    CLOSE
02. MOTOR PUMP STATUS        OFF
DO YOU WANT TO START ?
(PRESS [YES] KEY)
```

6. Wait 60 sec. before operating the air bleeding. (If not, you may damage the motor).

**1.6 Air Bleeding Mode — Active Screen:**

```
ABS AIR BLEEDING STATUS

01. SOLENOID VALVE STATUS    OPEN
02. MOTOR PUMP STATUS        ON
TIME: AUTOMATIC COUNT (1-60 SEC.)
```

5. Pump the brake pedal several times, and then loosen the bleeder screw until fluid starts to run out without bubbles. Then close the bleeder screw.

6. Repeat step 5 until there are no more bubbles in the fluid for each wheel.

#### Bleeding Order

<!-- Figure: Bleeding order diagram showing numbered sequence: 1 = rear right, 2 = front left, 3 = rear left, 4 = front right, source: BR.pdf page 75 -->

| Position | Order |
|---|---|
| 1 | Front right |
| 2 | Front left |
| 3 | Rear right |
| 4 | Rear left |

7. Tighten the bleeder screw.

**Bleeder screw tightening torque:**
: **7-13 Nm (70-130 kg-cm, 5-9.5 lb-ft)**
