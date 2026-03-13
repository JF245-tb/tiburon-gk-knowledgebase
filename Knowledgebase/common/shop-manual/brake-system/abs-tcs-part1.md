---
source: BR.pdf
chapter: BR
section: BR-32 to BR-53
pages: 32-53
engine: V6
title: ABS/TCS (Part 1)
---

# ABS / TCS (Part 1)

## ABS Control
<!-- BJCC0005 -->

### 1. Normal Braking

| Solenoid valve | State | Valve | Passage |
|---|---|---|---|
| IN (NC) | OFF | OPEN | Master cylinder ↔ Wheel cylinder |
| OUT (NC) | OFF | CLOSE | Wheel cylinder ↔ Reservoir |

### 2. Dump Mode

| Solenoid valve | State | Valve | Passage |
|---|---|---|---|
| IN (NC) | ON | CLOSE | Master cylinder ↔ Wheel cylinder |
| OUT (NC) | ON | OPEN | Wheel cylinder ↔ Reservoir |

### 3. Hold Mode

| Solenoid valve | State | Valve | Passage |
|---|---|---|---|
| IN (NC) | ON | CLOSE | Master cylinder ↔ Wheel cylinder |
| OUT (NC) | OFF | CLOSE | Wheel cylinder ↔ Reservoir |

### 4. Increase Mode

| Solenoid valve | State | Valve | Passage |
|---|---|---|---|
| IN (NC) | OFF | OPEN | Master cylinder ↔ Wheel cylinder |
| OUT (NC) | OFF | CLOSE | Wheel cylinder ↔ Reservoir |

---

## Traction Control System (TCS)
<!-- BJCC0006 -->

### 1. Normal Mode

| Solenoid valve | State | Valve | Motor pump | TC valve |
|---|---|---|---|---|
| IN (NC) | OFF | OPEN | OFF | OFF |
| OUT (NC) | OFF | CLOSE | OFF | OFF |

- In the normal driving condition, TC valve (normally open) is the passage between the master cylinder and the each wheel cylinder.
- When brake pedal is applied, brake pressure is delivered to the wheel cylinders via NO-TC valve and all solenoid valves inside the hydraulic unit are deactivated.
- In case of TCS malfunction it does not affect brake operation.

### 2. Pressure Increase Mode

| Solenoid valve | State | Valve | Motor pump | TC valve |
|---|---|---|---|---|
| IN (NC) | FRONT: OFF / REAR: ON | FRONT: OPEN / REAR: CLOSE | ON | ON |
| OUT (NC) | OFF | CLOSE | | |

- If a front wheel spin is detected, TCS begins a brake control to decrease a wheel spin.
- Hydraulic shuttle valve (HSV) is opened.
- Brake fluid is supplied from the master cylinder by motor operation to the spin wheel via HSV.
- TC valve is closed (ON).
- Brake pressure generated from motor pump is delivered only to the front wheel.
- Inlet valve remains open to deliver the brake pressure generated from motor pump to the spinning wheels.

### 3. Pressure Dump Mode

| Solenoid valve | State | Valve | Motor pump | TC valve |
|---|---|---|---|---|
| IN (NC) | ON | CLOSE | ON | ON |
| OUT (NC) | FRONT: ON / REAR: OFF | FRONT: OPEN / REAR: CLOSE | ON | ON |

- When the wheel deceleration is under the threshold and the wheel spin is reduced under a slip threshold, applied brake pressure is reduced to get a optimum traction force.
- Outlet valve is open to release the brake pressure and inlet valve is closed to block the pressure increase from the motor pump.
- Until the wheel deceleration is over the standard, TC valve is ON.
- Motor is ON, to dump the brake fluid being released from the lock-up wheel.

### 4. Pressure Hold Mode

| Solenoid valve | State | Valve | Motor pump | TC valve |
|---|---|---|---|---|
| IN (NC) | ON | CLOSE | ON | ON |
| OUT (NC) | OFF | CLOSE | | |

---

## EBD (Electronic Brake-Force Distribution)
<!-- BJCC0007 -->

The EBD system (Electronic Brake-force Distribution) as a sub-part of the ABS system is to control the suitable adhesion utilization by the rear wheels.

It further utilizes the efficiency of highly developed ABS equipment by controlling the slip of the rear wheels in the partial braking range.

The brake force is moved even closer to the optimum and controlled electronically, thus dispensing with the need for the proportioning valve.

The proportioning valve, because of a mechanical device, has limitations to achieve an ideal brake force distribution to the rear wheels as well as to carry out the flexible brake force distribution proportioning to the vehicle load or weight increasing. And in the event of malfunctioning, driver cannot notice whether it fails or not.

EBD controlled by the ABS Control Module, calculates the slip ratio of each wheel at all times and controls the brake pressure of the rear wheel not to exceed that of the front wheel.

If the EBD fails, the EBD warning lamp (Parking brake warning lamp) lights up.

### Advantages

- Function improvement of the base-brake system.
- Compensation for the different friction coefficients.
- Elimination of the proportioning valve.
- Failure recognition by the warning lamp.

### Comparison Between Proportioning Valve and EBD

<!-- Figure: Comparison graphs - (With P-Valve) shows rear pressure vs front pressure with fixed distribution, ideal distribution, and cut-in point; (With EBD) shows rear pressure vs front pressure with EBD starting point and controlled distribution, source: BR.pdf page 34 -->

### Fail Safe

| Fail Cause | System | Warning Lamp | | |
|---|---|---|---|---|
| | **ABS** | **EBD** | **ABS** | **EBD** |
| None | ON | ON | OFF | OFF |
| 1-Wheel speed sensor failure | OFF | ON | ON | OFF |
| Pump malfunction | OFF | ON | ON | OFF |
| Low voltage | OFF | ON | ON | OFF |
| 2 or more wheel speed sensor failure | OFF | OFF | ON | ON |
| Solenoid valve failure | OFF | OFF | ON | ON |
| HECU malfunction | OFF | OFF | ON | ON |
| Other failure | OFF | OFF | ON | ON |

---

## Warning Lamp Control
<!-- BJCC0008 -->

<!-- Figure: Instrument cluster showing TCS function lamp, TCS warning lamp (left), Parking/EBD warning lamp (center), ABS warning lamp (right), source: BR.pdf page 35 -->

### 1. ABS Warning Lamp Module

The active ABS warning lamp module indicates the operating condition of the ABS.

The ABS warning lamp is turned on under the following conditions:

- During the initialization phase after ignition switch ON (3 seconds).
- In the event of inhibition of ABS functions by failure.
- When the system ECU is shut down even though ignition power is applied.
- During diagnostic mode.

### 2. EBD Warning Lamp Module

The active EBD warning lamp module indicates the operating condition of the EBD. However, in case the parking brake switch is turned on, the EBD warning lamp is always turned on regardless of EBD functions.

The EBD warning lamp is turned on under the following conditions:

- During the initialization phase after ignition switch ON (3 seconds).
- When the system ECU is shut down even though ignition power is applied.
- When the parking brake switch is ON or brake fluid is low level.

### 3. TCS Lamp Module

The passive TCS warning lamp module indicates the operating condition of the TCS.

The TCS warning lamp is turned on under the following conditions:

- During the initialization phase after ignition switch ON (3 seconds).
- In the event of inhibition of TCS functions by failure.
- When the TCS OFF switch is turned on.

TCS function lamp is turned on when the TCS functions are operating (Blinking 2Hz).

---

## Standard Flow of Diagnostic Troubleshooting
<!-- BJCC0009 -->

<!-- Figure: Diagnostic troubleshooting flowchart - Gathering information from customer, branching to Check diagnostic code (reoccurs vs does not reoccur), and No trouble code path (check basic brake system, refer to BR-Troubleshooting), source: BR.pdf page 36 -->

*Using the customer problem analysis check sheet for reference, ask the customer as much detail as possible about the problem.*

### Notes with Regard to Diagnosis

The phenomena listed in the following table are not abnormalities:

| Phenomenon | Explanation |
|---|---|
| System check sound | When starting the engine, a thudding sound can sometimes be heard coming from inside the engine compartment. This is because the system operation check is being performed. |
| ABS operation sound | 1. Sound of the motor inside the ABS hydraulic unit operation (whirrs). 2. Sound is generated along with vibration of the brake pedal (pulsing). 3. When ABS operates, sound is generated from the vehicle chassis due to repeated brake application and release (thump, suspension, squeal, tire). |
| ABS operation (Long braking distance) | For road surfaces such as snow-covered and gravel roads, the braking distance for vehicles with ABS can sometimes be longer than that for other vehicles. Accordingly advise the customer to drive safely on such roads by lowering the vehicle speed. |
| Pedal kick back | Pedal kick back is normal operation. |

Diagnosis detection conditions can vary depending on the diagnosis code. When checking the trouble symptom after the diagnosis code has been erased, ensure that the requirements listed in "Comment" are met.

---

## ABS Check Sheet
<!-- BJCC0010 -->

<!-- Figure: ABS Check Sheet form with fields for: Customer's Name, Registration No., Registration Year, VIN, Date Vehicle Brought In, Odometer (Km/Miles), Date the Problem First Occurred, Frequency of Occurrence (Continuous / Intermittent with times a day), Symptoms (ABS does not operate / ABS does not operate efficiently / ABS Warning Light Abnormal with sub-options Remains ON and Intermittent and Does not light up), Diagnostic Trouble Code Check (1st Time and 2nd Time with Normal Code / Malfunction Code fields), source: BR.pdf page 37 -->

---

## Hi-Scan (Pro) Check
<!-- BJCC0011 -->

1. Turn the ignition OFF.
2. Connect the Hi-Scan (Pro) to the Data Link Connector located underneath the lower crash pad panel.
3. Turn the ignition ON.
4. Use the Hi-Scan (Pro) to check for diagnostic trouble codes.
5. After completion of the repair or correction of the problem, erase the stored fault codes using the clear key on the Hi-Scan (Pro).
6. Disconnect the Hi-Scan (Pro).

<!-- Figure: Data Link Connector diagram showing 16-pin OBD2 connector pinout with Ground and Power pins labeled, located underneath the lower crash pad panel, source: BR.pdf page 38 -->

---

## Connector Check
<!-- BJCC0012 -->

1. Remove the negative battery (-) terminal.
2. Disconnect the connectors and check terminals following the troubleshooting procedure.

> **NOTE:** When you check the terminals, be sure to use a small enough pin so as to not damage the connector terminals.

---

## Inspection Chart for Diagnostic Trouble Codes
<!-- BJCC0013 -->

Inspect according to the inspection chart that is appropriate for the malfunction code.

| DTC | Trouble Location | Remarks |
|---|---|---|
| C1101 | Battery voltage over volt: 18V or more | |
| C1102 | Battery voltage low volt: 9.5V or less | |
| C1200 | FL wheel sensor: open or short to ground | |
| C1201 | Range/Performance: speed jump or damaged exciter | |
| C1202 | No signal: air-gap error or wrong excite | |
| C1203 | FR wheel sensor: open or short to ground | |
| C1204 | Range/Performance: speed jump or damaged exciter | |
| C1205 | No signal excite: air-gap error or wrong excite | |
| C1206 | RL wheel sensor: open or short to ground | |
| C1207 | Range/Performance: speed jump or damaged exciter | |
| C1208 | No signal: air-gap error or wrong excite | |
| C1209 | RR wheel sensor: open or short to ground | |
| C1210 | Range/Performance: speed jump or damaged exciter | |
| C1211 | No signal: air-gap error or wrong excite | |
| C1604 | ECU hardware: ECU internal or valve failure | |
| C1212 | Valve relay: valve relay or fuse failure | |
| C2402 | Motor/Electrical: open or short to battery, motor relay, fuse or motor lock fail | |
| C2027 | Brake disc overheat | Only TCS |
| C1503 | TCS switch failure | With TCS switch |
| C1610 | CAN bus off failure | Only TCS |
| C1611 | EMS time-out failure | Only TCS |
| C1612 | TCU time-out failure | Only TCS |
| C1613 | TCU un-matching failure | Only TCS |
| C1605 | CAN hardware failure | Only TCS |

---

## Actuator Driving
<!-- BJCC0014 -->

| No. | Description | Condition | Recognition | Time |
|---|---|---|---|---|
| 01 | Motor | | Motor pump relay operation (Click sounds) | 2 seconds |
| 02 | Front left valve (In) | | Front left solenoid valve operation (Click sounds) | |
| 03 | Front right valve (In) | | Front left solenoid valve operation (Click sounds) | |
| 04 | Rear left valve (In) | | Rear left solenoid valve operation (Click sounds) | |
| 05 | Rear right valve (In) | KEY ON, ENG. OFF | Rear right solenoid valve operation (Click sounds) | |
| 06 | Front left valve (Out) | | Front left solenoid valve operation (Click sounds) | |
| 07 | Front right valve (Out) | | Front right solenoid valve operation (Click sounds) | |
| 08 | Rear left valve (Out) | | Rear left solenoid valve operation (Click sounds) | |
| 09 | Rear right valve (Out) | | Rear right solenoid valve operation (Click sounds) | |

---

## Current Data
<!-- BJCC0015 -->

| No. | Description | Recognition | Unit |
|---|---|---|---|
| 1 | Battery | Battery | Voltage |
| 2 | FL wheel speed SNSR | Front left wheel speed sensor | km/h |
| 3 | FR wheel speed SNSR | Front right wheel speed sensor | |
| 4 | RL wheel speed SNSR | Rear left wheel speed sensor | |
| 5 | RR wheel speed SNSR | Rear right wheel speed sensor | ON/OFF |
| 6 | ABS SPI status | Warning lamp | |
| 7 | Brake SW | Brake switch | ON/OFF |
| 8 | Motor pump relay | Motor relay | |
| 9 | Valve relay | Valve relay | |
| 10 | Motor pump status | Motor | |
| 11 | FL valve (In) | Front left valve (In) | |
| 12 | FR valve (In) | Front right valve (In) | |
| 13 | RL valve (In) | Rear left valve (In) | |
| 14 | RR valve (In) | Rear right valve (In) | |
| 15 | FL valve (Out) | Front left valve (Out) | |
| 16 | FR valve (Out) | Front right valve (Out) | |
| 17 | RL valve (Out) | Rear left valve (Out) | |
| 18 | RR valve (Out) | Rear right valve (Out) | |

---

## Fail-Safe Specification
<!-- BJCC0016 -->

### Detect Mode

- A: Initial check
- B: Outside the ABS control cycle
- C: Inside the ABS control cycle
- D: Diagnostic mode
- E: Failure mode

### The Ability of Detecting a Failure

- Detect the failure
- Not detect the failure

### The Management of Failure Detection

1. **System down.** Both the ABS (TCS) and the EBD function are inhibited and the ABS (TCS) and the EBD warning lamps are activated. If this happens, the valve relay and all solenoids are prevented from being switched on.

2. **Only the ABS (TCS) function is inhibited.** The ABS (TCS) warning lamp is activated and the EBD warning lamp is not activated.

3. **Sensor failure outside the ABS control cycle.**
   1. Only one sensor fail: take the same action as management 1.
   2. More than two sensors fail: take the same action as management 1.

4. **Sensor failure inside the ABS control cycle.**
   1. One front sensor fails: inhibit the ABS control of the failed wheel and maintain ABS control of the other wheels. After the controller completes the ABS control, take the same action as in management 1.
   2. One rear sensor fails: inhibit ABS control of both front wheels and the pressure of both rear wheels is decreased. After the controller completes the ABS control, take the same action as in management 2.
   3. More than two sensor fail: take the same action as in management 1.

5. **Low operating voltage.**

6. Outside the ABS control cycle: inhibit the ABS (TCS) warning lamp is turned on and the ABS control of front wheels and allow the ABS control of rear wheels. The ABS (TCS) warning lamp is directly switched on.

   When the voltage recovers to the normal operating range, enable the ABS function and the ABS (TCS) warning lamp is switched off and erase the error code of low voltage.

7. Inside the ABS control cycle: inhibit the ABS control of the front wheels and allow the ABS control of rear wheels, deactivating the motor. The ABS (TCS) warning lamp is directly switched on and remains on. The error code is always stored.

8. Motor error during the ABS control cycle. Inhibit the ABS control of front wheels, allow ABS control of the rear wheels and ABS (TCS) warning lamp is switched ON at the end of the ABS cycle.

9. **TCS failure.**
   Inhibit the TCS control and allow the ABS/EBD control. Meanwhile, stop checking the TCS switch failure under the TCS control.

---

## DTC Inspection Chart: Wheel Speed Sensor Open/Short
<!-- BJCC0017 -->

### DTC No. C1200, C1203, C1206, C1209 -- Wheel Speed Sensor Open or Short to GND Circuit

The HECU determines that an open or short circuit has occurred in more than one wire of a wheel speed sensor.

**Probable cause:**

- Malfunction of wheel speed sensor
- Malfunction of wiring harness or connector
- Malfunction of HECU

#### Inspection Procedure

1. Inspect wheel speed sensor installation. --> NG --> Repair
2. OK --> Measure at the HECU connectors E01, E39. Disconnect connector and measure from the harness side. Resistance values between 1 and 2, 19 and 20, 5 and 6, 22 and 23. OK: 1,360 +/- 110 ohm
3. OK --> Inspect wheel speed sensor output voltage.
4. OK --> Check the following connectors E37. --> NG --> Inspect rotor. --> NG --> Replace the rotor
5. OK --> Check symptoms of trouble
6. NG at step 2 --> Check the following connectors E01, E39, M64, M65. --> NG --> Check the harness wire between each wheel speed sensor and HECU, and repair if necessary
7. OK at connector check --> Check symptoms of trouble
8. NG at step 3 --> Inspect wheel speed sensor inspection. --> NG --> Replace the wheel speed sensor
9. If all checks pass with no resolution --> Replace the HECU

<!-- Figure: Diagnostic flowchart for C1200/C1203/C1206/C1209, source: BR.pdf page 49 -->

---

## DTC Inspection Chart: Wheel Speed Sensor Range/Performance/No Signal
<!-- BJCC0018 -->

### DTC No. C1201, C1204, C1207, C1210 -- Speed Jump or Wrong Exciter

Abnormal output signal from a wheel speed sensor other than an open or short circuit.

**Probable cause:**

- Improper installation of wheel speed sensor
- Malfunction of wheel speed sensor
- Malfunction of rotor
- Malfunction of wheel bearing
- Malfunction of wiring harness or connector
- Malfunction of HECU

#### Inspection Procedure

1. Inspect wheel speed sensor installation. --> NG --> Repair
2. OK --> Inspect wheel speed sensor output voltage. --> NG --> Inspect wheel speed sensor. --> NG --> Replace the wheel speed sensor
3. OK at output voltage --> Check the connector. --> NG --> Inspect rotor. --> NG --> Replace the rotor
4. OK at rotor --> Check symptoms of trouble. --> NG --> Check the harness wire between each wheel speed sensor and HECU, and repair if necessary
5. OK at connector --> Check symptoms of trouble
6. NG at symptoms of trouble --> Replace the HECU

<!-- Figure: Diagnostic flowchart for C1201/C1204/C1207/C1210, source: BR.pdf page 50 -->

---

### DTC No. C1202, C1205, C1208, C1211 -- Large Air Gap

No wheel speed sensor output signal.

**Probable cause:**

- Malfunction of wheel speed sensor
- Improper installation of wheel speed sensor
- Malfunction of rotor (excitor)
- Malfunction of wiring harness or connector
- Malfunction of HECU

#### Inspection Procedure

1. Inspect wheel speed sensor installation. --> NG --> Repair
2. OK --> Inspect air gap between wheel speed sensor and tone wheel. Air gap: 0.2-0.9 mm --> NG --> Repair
3. OK --> Check the following connectors E01, E39, M64, M65. --> NG --> Repair
4. OK --> Replace the HECU

<!-- Figure: Diagnostic flowchart for C1202/C1205/C1208/C1211, source: BR.pdf page 51 -->

---

## DTC Inspection Chart: Battery Voltage
<!-- BJCC0019 -->

### DTC No. C1101, C1102 -- Voltage Out of Range (Low and Over Voltage)

The voltage of the HECU power supply drops lower than or rises higher than the specified value. If the voltage returns to the specified value, this code is no longer output.

> **CAUTION:** If battery voltage drops or rises during inspection, this code will be output as well. If the voltage returns to the standard value, the code is no longer output. Before carrying out the following inspection, check the battery level, and refill if necessary.

#### Inspection Procedure

1. Measure at the HECU connector E37. Disconnect the connector and measure from the harness side. Start the engine. Voltage between terminal 4 and body ground. OK: System voltage.
2. NG --> Check symptoms of trouble. --> NG --> Check the harness wire between each wheel speed sensor and HECU, and repair if necessary
3. OK at connector --> Check the battery.
4. OK at battery --> Check symptoms of trouble. --> NG --> Replace the HECU

<!-- Figure: Diagnostic flowchart for C1101/C1102, source: BR.pdf page 52 -->

---

## DTC Inspection Chart: ECU Hardware and Valve Relay
<!-- BJCC0020 -->

### DTC No. C1604 -- ECU Hardware (EEPROM and ECU failure)

The HECU always monitors the solenoid valve drive circuit. It determines that there is an open or short-circuit in the solenoid coil or in a harness even if no current flows in the solenoid or through the HECU.

**Probable cause:**

- Malfunction of wiring harness
- Malfunction of HECU

### DTC No. C2212 -- Valve Relay (Including Fuse Failure)

When the ignition switch is turned OK, the HECU switches the valve relay on and off during its initial check. During this time, voltage sent to the valve relay is compared to the voltage in the valve power monitor line. If no current is detected in the valve power monitor line, the HECU determines that there is an open circuit and DTC C2112 is recorded.

**Probable cause:**

- Malfunction of wiring harness or connector
- Malfunction of HECU

#### Inspection Procedure

1. ABS fusible link (30A) inspection. --> NG --> Replace the fusible link
2. OK --> Check HECU connector (E37) terminal No.8.
3. OK --> Replace the HECU

<!-- Figure: Diagnostic flowchart for C1604 and C2212, source: BR.pdf page 53 -->

---

## Fail-Safe DTC Cross-Reference Tables

### Table 1 (BR-42): Sensor and Voltage DTCs

| DTC | Location | Failure Description | Condition for Detection | Management/Check Mode |
|---|---|---|---|---|
| C1200 FL, C1203 FR, C1206 RL, C1209 RR | Wheel speed sensor | Open or short to ground | The sensor output is continuously in a low or high position during the running of the vehicle | A: -/3, B: -/3, C: -/3, D: -/3, E: -/3 |
| C1201 FL, C1204 FR, C1207 RL, C1210 RR | Wheel speed sensor | Speed jump or damaged exciter | The sensor signal is proportionate to the speed (above 15 km/h). Then causes the noise exceeding the tolerance range of the controller | A: -, B: -/2b, C: -/2b, D: -, E: -/2b |
| C1202 FL, C1205 FR, C1208 RL, C1211 RR | Wheel speed sensor | No signal, air-gap error or wrong excite | The motor acceleration is higher than 1,000g (about 250 m/s). Then causes the motor not to rotate more than 15 km/h. The condition duration is 13 seconds | A: -/3, B: -/3, C: -/3, D: -, E: -/3 |
| C1101 | H-Scan (Pin 4) | Battery voltage over volt: 18V or more | | A: -/2b, B: -/2b, C: -/2b, D: -/2b, E: -/2b |
| C1102 | H-Scan (Pin 4) | Battery voltage low volt: 9.5V or less | | A: -/5, B: -/5, C: -/6, D: -, E: -/5 |

### Table 2 (BR-43): Hardware and Communication DTCs

| DTC | Location | Failure Description | Condition for Detection | Management/Check Mode |
|---|---|---|---|---|
| C1604 | ECU hardware | EEPROM and ECU failure | | A: -/1, B: -/1, C: -/1, D: -/1, E: - |
| C2402 | Motor/Electrical | Open or short to battery, motor relay, fuse or motor lock fail | When the motor is not running in normal mode, the diagnostic monitors the condition of the valve power supply | A: -/1, B: -/1, C: -/1, D: -, E: - |
| C2212 | Valve relay | Valve relay or fuse failure | | A: -/1, B: -/1, C: -/1, D: -/1, E: -/1 |
| C1212 | Valve relay | Valve relay or fuse failure | When the ignition is turned on, the HECU compares the output of the valve to the valve power monitor line. If no current is detected, the code is stored | A: -/1, B: -/1, C: -/1, D: -/1, E: - |

### Table 3 (BR-44): ECU and Sensor DTCs

| DTC | Location | Failure Description | Condition for Detection | Management/Check Mode |
|---|---|---|---|---|
| C2402 | Motor/Electrical | Open or short to battery, motor relay, fuse or motor lock fail | When the HECU detects loss of the motor current after 500ms of the start command, 3 or 5 supply voltage variations compare to the monitoring output of V+M | A: -/1, B: -/1, C: -/1, D: -, E: - |
| C1100 | Steering sensor | | If the steering sensor does not send a data value via CAN within 500ms, the controller suspends the recording | A: -/1, B: -/1, C: -/1, D: -/1, E: -/1 |
| C1101 | H-Scan (Pin 4) | Over voltage: 18V or more | | A: -/5, B: -/5, C: -/6, D: -, E: -/5 |
| C1102 | H-Scan (Pin 4) | Low voltage: 9.5V or less | The motor deceleration is higher than 500g. Then causes the motor to not rotate more than 7.5V. The condition duration is 0.5 seconds | A: -/5, B: -/5, C: -/6, D: -, E: -/5 |

### Table 4 (BR-45): TCS-Specific DTCs

| DTC | Location | Failure Description | Condition for Detection | Management/Check Mode |
|---|---|---|---|---|
| C1610, C1611, C1612, C1613, C1605 | CAN bus / EMS / TCU | CAN failure, time-out, un-matching | | A: -/9, B: -/9, C: -/9, D: -/9, E: -/9 |
| C1503 | TCS switch | TCS switch failure | | A: -/9, B: -/9, C: -/9, D: -/9, E: -/9 |
| C2027 | Brake disc | Brake disc overheat | | A: -/9, B: -/9, C: -/9, D: -, E: - |
| C0403 | Brake disc | Brake disc overheat | Determine that the level of TCS braking at high computed engine torque is higher than the limit | A: -/9, B: -/9, C: -/9, D: -, E: - |

---

## ABS Schematic Diagrams

### Schematic Diagram (1)
<!-- Figure: ABS system wiring schematic (1) showing: ETACS fuse connections, ABS warning lamp, EBD/parking warning lamp, ABS HECU module connections including motor relay, valve relay, brake switch input, instrument cluster connections, and wheel speed sensor harness connections (E01/E39 connectors to M64/M65 at ESP module), source: BR.pdf page 46 -->

Key circuit elements:
- Fuse 13, Fuse 20 power feeds
- ABS warning lamp and Parking/EBD warning lamp to instrument cluster
- HECU motor relay and pump motor
- Brake switch input
- Wheel speed sensor connections: FL, FR, RL, RR through connectors E01, E39 to M64, M65

### Schematic Diagram (2)
<!-- Figure: ABS system wiring schematic (2) showing: Fuse 21 power feed, TCS function lamp, Data Link Connector, TCS switch/TOV, Diagnostic connection, IG1 START input, and four wheel speed sensors (left front, right front, left rear, right rear) with their wiring to the HECU, source: BR.pdf page 47 -->

Key circuit elements:
- TCS switch connection
- Data Link Connector (OBD2) for diagnostics
- IG1 START signal
- All four wheel speed sensor wiring with individual ground connections
- Wire gauges: 0.5 sq, 0.3 sq typical

### Schematic Diagram (3)
<!-- Figure: ABS system wiring schematic (3) showing: Fuse 8 and Fuse 9 power feeds to HECU solenoid valves, CAN communication area network connections, valve relay circuit, and motor pump circuit with relay control. Shows HECU internal solenoid connections for all 8 valves (4 inlet, 4 outlet) for FL/FR/RL/RR channels, source: BR.pdf page 48 -->

Key circuit elements:
- 8 solenoid valves (4 inlet NC, 4 outlet NC)
- CAN communication bus connection
- Valve relay and motor pump relay
- Fusible link connections
- Wire connections to body ground points

---

## Key Specifications Summary

| Parameter | Value |
|---|---|
| Wheel speed sensor resistance | 1,360 +/- 110 ohm |
| Wheel speed sensor air gap | 0.2 - 0.9 mm |
| Battery over-voltage DTC threshold | 18V or more |
| Battery under-voltage DTC threshold | 9.5V or less |
| ABS fusible link | 30A |
| ABS warning lamp init duration | 3 seconds |
| EBD warning lamp init duration | 3 seconds |
| TCS function lamp blink rate | 2 Hz |
