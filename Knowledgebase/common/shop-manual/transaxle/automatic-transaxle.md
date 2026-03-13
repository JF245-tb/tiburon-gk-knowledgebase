---
source: TR.pdf
chapter: TR
section: TR-10 to TR-87
pages: 10-87
engine: V6
title: Automatic Transaxle System
---

<!-- TR-10 -->
# Automatic Transaxle System

## Troubleshooting (A/T) (F4A42 Model) <!-- EKA90070 -->

**Diagnostic Flowchart:**

1. Gather information from customer
2. Verify complaint
3. Record the DTC and fail-safe code (if communication with scan tool impossible, go to Inspection Procedure No. 1 in Inspection Chart for Trouble Symptom)
4. If abnormal code output: Erase the DTC
5. Basic inspection item adjustment
6. Road test
   - If no abnormality: Recheck DTCs which were read before the road test
     - If abnormal code output: Go to inspection chart for DTC
     - If normal code displayed: Go to Inspection Chart for Trouble Symptom
   - If abnormality exists (No DTC): Go to Inspection Chart for Trouble Symptom
7. Search for cause
   - If found: Repair → if NG → GO TO INTERMITTENT MALFUNCTIONS
   - If not found: GO TO INTERMITTENT MALFUNCTIONS
8. Confirmation test (Road test) → OK → Completed

---

<!-- TR-11 -->
## Basic Inspection Adjustment <!-- EKA90080 -->

### Automatic Transaxle Fluid Check

1. Drive the vehicle until the fluid temperature rises to the normal temperature (70-80°C).
2. Park the vehicle on a level surface.
3. Move the selector lever through all positions to fill the torque converter and the hydraulic circuits with fluid, and then move the selector lever to the N position.
4. After wiping off any dirt around the oil level gauge, reinsert and remove the oil level gauge and check the condition of the fluid.

> **NOTE**
> If the fluid smells as if it is burning, it means that the fluid has been contaminated by fine particles from the bushing and friction materials, a transaxle overhaul may be necessary.

5. Check that the fluid level is at the HOT mark on the oil level gauge. If the fluid level is lower than this, add more fluid until the level reaches the HOT mark.
   Automatic transaxle fluid: GENUINE HYUNDAI ATF SP-III.

> **NOTE**
> If the fluid level is low, the oil pump will draw in air along with the fluid, which will cause bubbles to form inside the hydraulic circuit. This will in turn cause the hydraulic pressure to drop, which will result in late shifting and slipping of the clutches and brakes. If there is too much fluid, the gears can churn it up into foam and cause the same conditions that can occur with low fluid levels. In either case, air bubbles can cause overheating and oxidation of the fluid which can interfere with normal valve, clutch, and brake operation. Foaming can also result in fluid escaping from the transaxle vent, in which case it may be mistaken for a leak.

6. Insert the oil level gauge securely.
7. The fluid and the oil filters should always be replaced when overhauling the transaxle or after the vehicle has been driven under severe conditions. The replacement procedures are given below. Furthermore, the oil filters are special filters which are only to be used for the automatic transaxle.

### Automatic Transaxle Fluid

#### Replacement

If you have a fluid changer, use this changer to replace the fluid. If you do not have a fluid changer, replace the fluid using following procedure.

1. Remove the drain plug from the bottom of the transaxle case to drain the fluid.
2. Install the drain plug and gasket, and tighten to the specified torque.

   **Tightening torque:** 32 Nm (320 kg.cm, 23 lb.ft)

3. Pour the new fluid in through the oil filler tube.

> **CAUTION**
> *Stop pouring if the full volume of fluid cannot be poured in.*

4. Repeat the procedure in step 1 if too much fluid was added.
5. Reconnect the hose that was disconnected in step 1 above, and firmly replace the oil level gauge.
6. Start the engine and run it at idle for 1-2 minutes.
7. Move the select lever through all positions, and then move it to the N position.
8. Drive the vehicle until the fluid temperature rises to the normal temperature (70-80°C), and then check the fluid level again. The fluid level must be at the HOT mark.
9. Firmly insert the oil level gauge into the oil filler tube.

<!-- figure: Automatic transaxle fluid drain/fill procedure -->

---

<!-- TR-12 -->
## Transaxle Range Switch Continuity Check

| Items / Terminal No. | 6 | 5 | 4 | 3 | 2 | 1 | 10 | 9 | 8 | 7 |
|----------------------|---|---|---|---|---|---|----|---|---|---|
| P | | | | | O | | | | | |
| R | | | | O | | | | | | |
| N | | | | | | O | | | | |
| D | | O | | | | | | | | |

<!-- figure: Transaxle range switch connector diagram -->

## Transaxle Range Switch and Control Cable Adjustment

1. Set the selector lever to the "N" position.
2. Loosen the control cable to the manual control lever coupling nut to free the cable and lever.
3. Set the manual control lever to the neutral position.

<!-- figure: Transaxle control cable, adjusting nut, manual control lever -->

4. Loosen the transaxle range switch body mounting bolts and then turn the transaxle range switch body so the hole in the end of the manual control lever and the hole (cross section A-A in the figure) in the flange of the transaxle range switch body flange are aligned.
5. Tighten the transaxle range switch body mounting bolts to the specified torque. Be careful at this time that the position of the switch body does not change.

   **Tightening torque:** 10-12 Nm (100-120 kg.cm, 7-9 ft.lb.)

<!-- figure: Mounting bolts, manual control lever, Section A-A, transaxle range switch body -->

6. Gently pull the transaxle control cable in the direction of the arrow, then tighten the adjusting nut.
7. Check that the selector lever is in the "N" position.
8. Check that each range on the transaxle side operates and functions correctly for each position of the selector lever.

<!-- figure: Adjusting nut, manual control lever -->

---

<!-- TR-13 -->
## A/T Control Component Check

### 1. Throttle Position Sensor Check

The TPS is a variable resistor type that rotates with the throttle body shaft to sense the throttle valve angle. As the throttle shaft rotates, the output voltage of the TPS changes. The ECM detects the throttle valve opening based on voltage change. (Refer to FL-section.)

### 2. Oil Temperature Sensor Check

a. Remove the oil temperature sensor.
b. Measure the resistance between terminals 1 and 2 of the oil temperature sensor connector.

**Standard Value:**

| Oil temperature (°C) | Resistance (kΩ) |
|----------------------|-----------------|
| 0 | 16.7-20.5 |
| 100 | 0.57-0.69 |

### 3. Vehicle Speed Sensor Check

a. Remove the vehicle speed sensor and connect a 3-10 kΩ resistance as shown in the illustration.
b. Turn the shaft of the vehicle speed sensor and check that there is voltage between terminals 2-3 (1 turn=4 pulses).

<!-- figure: Sensor side connector, circuit tester, turn shaft, 3-10 kΩ resistor -->

### 4. A/T Control Relay Check

a. Remove the A/T control relay.
b. Use jumper wires to connect A/T control relay terminal 2 to the battery (+) terminal and terminal 4 to the battery (-) terminal.

<!-- TR-14 -->

c. Check the continuity between terminal 1 and terminal 3 of the A/T control relay when the jumper wires are connected and disconnected from the battery.
d. If there is a problem, replace the A/T control relay.

| Jumper wire | Continuity between terminal No.1 |
|-------------|----------------------------------|
| Connected | Continuity |
| Disconnected | No continuity |

### 5. Solenoid Valve Check

a. Remove the valve body cover.
b. Disconnect the connectors of each solenoid valve.

<!-- figure: Overdrive solenoid valve, underdrive solenoid valve, low & reverse solenoid valve, second solenoid valve, damper clutch solenoid valve -->

c. Measure the resistance between terminals 1 and 2 of each solenoid valve.

**Standard Value:**

| Name | Resistance (at 20°C) |
|------|---------------------|
| Damper clutch solenoid valve | 2.7-3.4Ω |
| Low and reverse solenoid valve | ↑ |
| Second solenoid valve | ↑ |
| Underdrive solenoid valve | ↑ |
| Overdrive solenoid valve | ↑ |

d. If the resistance is outside the standard value, replace the solenoid valve.

> **NOTE**
> Resistance of the solenoid valve connector.

| Terminal No. | Name | Resistance (at 20°C) |
|-------------|------|---------------------|
| 7 & 10 | Damper clutch solenoid valve | 2.7-3.4Ω |
| 10 & 6 | Low and reverse solenoid valve | ↑ |
| 9 & 4 | Second solenoid valve | ↑ |
| 9 & 3 | Underdrive solenoid valve | ↑ |
| 9 & 5 | Overdrive solenoid valve | ↑ |

---

## Torque Converter Stall Test <!-- EKA90175 -->

This test measures the maximum engine speed when the selector lever is in the D or R position. The torque converter stalls to test the operation of the torque converter, starter motor, one-way clutch operation, the holding performance of the clutches, and brakes in the transaxle.

> **CAUTION**
> *Do not let anybody stand in front of or behind the vehicle while this test is being carried out.*

a. Check the automatic transaxle fluid level and temperature, and the engine coolant temperature.
   - Fluid level: At the HOT mark on the oil level gauge
   - Fluid temperature: 80-100°C
   - Engine coolant temperature: 80-100°C

b. Check both rear wheels (left and right).
c. Apply the parking brake lever with the brake pedal fully depressed.
d. Start the engine.
e. Move the selector lever to the D position, fully depress the accelerator pedal and take a reading of the maximum engine speed at this time.

> **CAUTION**
> *The throttle should not be left fully open for more than eight seconds.*
> *If carrying out the stall test two or more times, move the selector lever to the N position and run the engine at 1,000 rpm to let the automatic transaxle fluid cool down before carrying out subsequent tests.*
> **Standard value stall speed: 2,100-2,900 rpm**
> *Move the selector lever to the R position and carry out the same test again.*
> **Standard value stall speed: 2,100-2,900 rpm**

### Torque Converter Stall Test Judgement Results

1. **Stall speed is too high in both D and R ranges**
   - Low line pressure
   - Low & reverse brake slippage
   - Underdrive clutch slippage

2. **Stall speed is too high in D range only**
   - Underdrive clutch slippage

3. **Stall speed is too high in R range only**
   - Reverse clutch slippage

4. **Stall speed too low in both D and R ranges**
   - Malfunction of torque converter
   - Insufficient engine output

---

<!-- TR-15 -->
<!-- figure: Cross-section diagram showing Reverse clutch, Low-reverse brake, Underdrive clutch, Torque converter -->

## Hydraulic Pressure Test

1. Warm up the engine until the automatic transaxle fluid temperature is 80-100°C.
2. Jack up the vehicle so that the wheels are free to turn.
3. Connect the special tool (oil pressure gauge) to each pressure discharge port.
4. Measure the hydraulic pressure at each port under the conditions given in the standard hydraulic pressure table, and check that the measured values are within the standard value ranges.
5. If a value is outside the standard range, correct the problem while referring to the hydraulic pressure test diagnosis table.

<!-- figure: Attach the special tool (oil pressure gauge) 09452-21550 -->

---

<!-- TR-16 -->
### Standard Hydraulic Pressure Test

| Measurement condition | | | Standard hydraulic pressure kPa | | | | | |
|---|---|---|---|---|---|---|---|---|
| **Selector lever position** | **Shift position** | **Engine speed (rpm)** | **Underdrive clutch pressure (UD)** | **Reverse clutch pressure (REV)** | **Overdrive clutch pressure (OD)** | **Low and reverse brake pressure (LR)** | **Second brake pressure (2ND)** | **Damper clutch apply pressure (DA)** | **Damper clutch release pressure (DR)** |
| P | - | 2,500 | - | - | - | 280-340 | - | - | 220-360 |
| R | Reverse | 2,500 | - | 1,270-1,770 | - | 1,270-1,770 | - | - | 500-700 |
| N | Neutral | - | - | - | - | 260-340 | - | - | 220-360 |
| D | 1st gear | 2,500 | 1,010-1,050 | - | - | 1,010-1,050 | - | - | 500-700 |
| D | 2nd gear | 2,500 | 1,010-1,050 | - | - | - | 1,010-1,050 | - | - |
| D | 3rd gear | 2,500 | 780-880 | - | 780-880 | - | - | More than 750 | 450-650 |
| D | 4th gear | 2,500 | - | - | 780-880 | - | - | More than 750 | 450-650 |

### Hydraulic Pressure Test Diagnosis Table

| Trouble symptom | Possible cause |
|-----------------|---------------|
| All hydraulic pressures are high | Incorrect transaxle control cable adjustment |
| | Malfunction of the regulator valve |
| All hydraulic pressures are low | Incorrect transaxle control cable adjustment |
| | Malfunction of the oil pump |
| | Clogged internal oil filter |
| | Clogged external oil filter |
| | Clogged oil cooler |
| | Malfunction of the regulator valve |
| | Malfunction of the relief valve |
| | Incorrect valve body installation |

---

<!-- TR-17 -->

| Trouble symptom | Possible cause |
|-----------------|---------------|
| Hydraulic pressure is abnormal in "3" or "4" range only | Malfunction of the regulator valve |
| | Clogged orifice |
| | Incorrect valve body installation |
| | Malfunction of the overdrive solenoid valve |
| | Malfunction of the overdrive pressure control valve |
| | Malfunction of the regulator valve |
| | Malfunction of the switch valve |
| | Clogged orifice |
| | Incorrect valve body installation |
| Only underdrive hydraulic pressure is abnormal | Malfunction of the oil seal K |
| | Malfunction of the oil seal L |
| | Malfunction of the oil seal M |
| | Malfunction of the underdrive solenoid valve |
| | Malfunction of the underdrive pressure control valve |
| | Malfunction of check ball |
| | Clogged orifice |
| | Incorrect valve body installation |
| Only reverse clutch hydraulic pressure is abnormal | Malfunction of the oil seal A |
| | Malfunction of the oil seal B |
| | Malfunction of the oil seal C |
| | Clogged orifice |
| | Incorrect valve body installation |
| Only overdrive hydraulic pressure is abnormal | Malfunction of the oil seal D |
| | Malfunction of the oil seal E |
| | Malfunction of the oil seal F |
| | Malfunction of the overdrive solenoid valve |
| | Malfunction of the overdrive pressure control valve |
| | Malfunction check ball |
| | Clogged orifice |
| | Incorrect valve body installation |
| Only low and reverse hydraulic pressure is abnormal | Malfunction of the oil seal I |
| | Malfunction of the oil seal J |
| | Malfunction of the low and reverse solenoid valve |
| | Malfunction of the low and reverse pressure control valve |
| | Malfunction of the switch valve |
| | Malfunction of the fail safe valve A |
| | Malfunction of check ball |
| | Clogged orifice |
| | Incorrect valve body installation |

---

<!-- TR-18 -->

| Trouble symptom | Possible cause |
|-----------------|---------------|
| Only second hydraulic pressure is abnormal | Malfunction of the oil seal G |
| | Malfunction of the oil seal H |
| | Malfunction of the oil seal Q |
| | Malfunction of the second solenoid valve |
| | Malfunction of the second pressure control valve |
| | Malfunction of the fail safe valve B |
| | Clogged orifice |
| | Incorrect valve body installation |
| Only reverse clutch hydraulic pressure is abnormal | Malfunction of the oil cooler |
| | Malfunction of the oil seal N |
| | Malfunction of the damper clutch control solenoid valve |
| | Malfunction of the damper clutch control valve |
| | Malfunction of the torque converter pressure control valve |
| | Clogged orifice |
| Pressure applied to non operating element | Incorrect valve body installation |
| | Incorrect transaxle control cable adjustment |
| | Malfunction of the manual valve |
| | Malfunction of check ball |

---

## Diagnosis Function <!-- EKA93090 -->

1. Connect the Hi Scan Pro to the connector for diagnosis.
2. Read the output diagnostic trouble codes. Then follow the remedy procedures according to the "DIAGNOSTIC TROUBLE CODE DESCRIPTION" on the following pages.

> **NOTE**
> - A maximum of 8 diagnostic trouble codes (in the sequence of occurrence) can be stored in the Random Access Memory (RAM) incorporated within the control module.
> - The same diagnostic trouble code can be stored one time only.
> - If the number of stored diagnostic trouble codes or diagnostic trouble patterns exceeds 8, already stored diagnostic trouble codes will be erased in sequence, beginning with the oldest.
> - Do not disconnect the battery until all diagnostic trouble codes or diagnostic trouble patterns have been read out, because all stored diagnostic trouble codes or diagnostic trouble patterns will be cancelled when the battery is disconnected.

3. If the fail-safe system is activated and the transaxle is locked in third gear, the diagnostic trouble code and the Fail-safe code description will be stored in the RAM. Three of these diagnostic trouble codes can be stored.
4. The cancellation will occur if, with the transaxle locked in third gear, the ignition key is turned to the OFF position, but the diagnostic trouble code is stored in the RAM.
5. Memorization.
   - Up to 8 diagnosis items and 3 fail-safe items can be memorized.
   - If the memory capacity is exceeded, diagnosis and fail-safe items in the memory are overwritten, starting with the oldest.
   - No code can be memorized more than once.
6. Diagnosis Code Deletion.
   1) Automatic Deletion: All diagnosis codes are deleted from memory the 200th time the ATF temperature reaches 50°C after memorization of the most recent diagnosis code.
   2) Forced Deletion.

<!-- TR-19 -->

   Memorized diagnosis codes can be deleted using the scan-tool, provided the following conditions are satisfied:

   - The ignition switch is ON
   - There is no detection pulse from the crank angle sensor
   - There is no detection pulse from the output shaft speed sensor
   - There is no detection pulse from the vehicle speed sensor
   - The fail-safe function is not operational

---

<!-- TR-20 -->
## Road Test <!-- EKA90100 -->

| No | Condition | Operation | Judgement value | Check item |
|----|-----------|-----------|-----------------|------------|
| 1 | Ignition switch: OFF | Ignition switch (1) ON | Battery voltage (mV) | Control relay |
| 2 | - Ignition switch: ON | Selector lever position | (1) P, (2) R, (3) N, | Transaxle range switch |
| | - Engine: Stopped | (1) P, (2) R, | (4) D | |
| | - Select lever position: P | (3) N, (4) D | | |
| | | Accelerator pedal | (1) 400-1,000 mV | Throttle position sensor |
| | | (1) Released | (2) Gradually rises from (1) | |
| | | (2) Half depressed | (3) 4,500-5,000 mV | |
| | | (3) Depressed | | |
| | | Brake pedal | (1) ON | Stop lamp switch |
| | | (1) Depressed | (2) OFF | |
| | | (2) Released | | |
| 3 | - Ignition switch: ST | Starting test with lever | Starting should be possible | Starting possible or |
| | - Engine: Stopped | P or N range | | impossible |
| | Warming up | Drive for 15 minutes or more so that the automatic fluid temperature becomes 70-90°C | Gradually rises to 70-90°C | Oil temperature sensor |
| 4 | | A/C switch | (1) ON | Triple pressure switch |
| | - Engine: Idling | (1) ON | (2) OFF | |
| | Selector lever position: N | (2) OFF | | |
| | | Accelerator pedal | (1) ON | Idle position switch |
| | | (1) Released | (2) OFF | |
| | | (2) Half depressed | | |
| 5 | | | (1) 600-825rpm | Communication with |
| | | | (2) Gradually rises from (1) | engine-ECU |
| | | | (1) Data changes | |
| | | Selector lever position | Should be no abnormal | Malfunction when starting |
| | | (1) N → D | shifting shocks. | |
| | | (2) N → R | Time lag should be within 2 seconds | |

---

<!-- TR-21 -->

| No | Condition | Operation | Judgement value | Check item |
|----|-----------|-----------|-----------------|------------|
| 6 | Selector lever position: N (Carry out on a flat and straight road) | Selector lever position and vehicle speed: | (2) 1st, (4) 3rd, (3) 2nd, (5) 4th | Shift condition |
| | | 1. Idling in 1st gear (Vehicle stopped) | (2) 0%, (4) 100%, (3) 100%, (5) 100% | Low and reverse solenoid valve |
| | | 2. Driving at constant speed of 20 km/h in 1st gear | (2) 0%, (4) 0%, (3) 0%, (5) 100% | Underdrive solenoid valve |
| | | 3. Driving at constant speed of 30 km/h in 2nd gear | (2) 100%, (4) 100%, (3) 0%, (5) 0% | Second solenoid valve |
| | | 4. Driving at 50 km/h in 3rd gear with accelerator fully closed | (2) 100%, (4) 0%, (3) 0%, (5) 0% | Overdrive solenoid valve |
| | | 5. Driving at constant speed of 50 km/h in 4th gear (Each condition should be maintained for 10 seconds or more) | (1) 0km/h | Vehicle speed sensor |
| | | | (4) 50km/h | |
| | | | (4) 1,800-2,100rpm | Input shaft speed sensor |
| | | | (4) 1,800-2,100rpm | Output shaft speed sensor |
| | | | (5) 0% | Damper clutch control solenoid valve |
| | | | (5) Approx. 70-90% | |
| | | | (3) Approx. 100-300rpm | |
| | | | (4) Approx. 0-10rpm | |
| 7 | Selector lever position: D (Carry out on a flat and straight road) | 1. Accelerate to 4th gear at a throttle position sensor output of 1.5V (accelerator opening angle of 30%). | For (1), (2) and (3), the reading should be the same as the specified output shaft torque, and no abnormal shocks should occur. | Malfunction when shifting |
| | | 2. Gently decelerate to a standstill. | For (4), (5) and (6), downshifting should occur immediately after the shifting operation is made. | Displaced shift points |
| | | 3. Accelerate to 4th gear at a throttle position sensor output of 2.5V (accelerator opening angle of 50%). | | Does not shift |
| | | 4. While driving at 60 km/h in 4th gear, shift down to 3rd gear. | | Does not shift from 1 to 2 or 2 to 1 |
| | | 5. While driving at 40 km/h in 3rd gear, shift down to 2nd gear. | | Does not shift from 2 to 3 or 3 to 2 |
| | | 6. While driving at 20 km/h in 2nd gear, shift down to 1st gear. | | Does not shift from 3 to 4 or 4 to 3 |
| 8 | Selector lever position: N (Carry out on a flat and straight road) | Move selector lever to R range; drive at constant speed of 10 km/h. | The ratio between input and output speed sensor data should be the same as the gear ratio when reversing. | Does not shift |

---

<!-- TR-22 -->
## Diagnostic Trouble Code Description <!-- EKA90110 -->

| DTC No | Diagnosis item | Possible cause |
|--------|---------------|----------------|
| P1704 | Throttle position sensor | Short circuit: TPS output > 4.8 V with engine idling |
| P1703 | | Open circuit: TPS output < 0.2 V with engine not idling |
| P1702 | | Sensor misadjustment: TPS output < 0.2 V or > 1.2 V with engine idling |
| P0713 | Fluid temperature sensor | Open circuit: Oil temperature sensor output > 4.57 V for 1 second or longer (oil temperature does not increase) |
| P0712 | | Short circuit: Output < 0.49V for 1 second |
| P0725 | CKP sensor | Open circuit: No crank angle sensor output pulse detected for 5 seconds at vehicle speed of 25 km/h |
| P0715 | Input speed sensor | Short circuit/open circuit: No input speed sensor output pulse detected for > 1 second at vehicle speed of > 30 km/h |
| P0720 | Output speed sensor | Short circuit/open circuit: At vehicle speed of > 30 km/h, output speed sensor output < 50% of vehicle speed sensor output for > 1 second |
| P0703 | Stop lamp switch | Short circuit/open circuit: At vehicle speed of 6 km/h, stop lamp switch is ON continuously for 5 minutes |
| P0750 | LR solenoid valve | Short circuit/open circuit: With relay voltage>10V, open or short circuit is continuously for 0.3 second |
| P0755 | UD solenoid valve | Short circuit/open circuit | |
| P0760 | 2nd solenoid valve | Short circuit/open circuit | |
| P0765 | OD solenoid valve | Short circuit/open circuit | |
| P0743 | TCC solenoid valve | Short circuit/open circuit | |
| P0731 | Gear shift incomplete | 1st | After gear shift, output shaft speed sensor output x gear ratio of new gear ≠ input shaft speed sensor output |
| P0732 | | 2nd | |
| P0733 | | 3rd | |
| P0734 | | 4th | |
| P0736 | | Reverse | |
| P1749 | Serial communication | Short circuit/open circuit: With ignition ON, battery voltage > 10V, and engine speed > 450 r/min, communication is continuously irregular for 1 second or communication error signal is received for > 4 seconds continuously |
| P0740 | TCC | System defect/stuck on: DCC solenoid valve drive duty ratio is 100% for 4 seconds continuously |
| P1723 | A/T control relay | Earth short circuit/open circuit: After ignition ON, A/T control relay voltage < 7V |
| P0707 | Transaxle range switch | Open circuit: No signal is continuous for > 30 seconds |
| P0708 | | Short circuit: Above 2 kinds signals are continuous for 30 seconds |

---

<!-- TR-23 -->

| DTC No | Diagnosis item | Possible cause |
|--------|---------------|----------------|
| P1630 | CAN-BUS OFF | TCM Fail/open/short: Receive BUS-OFF information from CAN CONTROLLER |
| P1631 | CAN-TIME OUT ECM | ECM Fail/open/short: No output signal for 1.5 second |
| P1764 | CAN MI-COM CIRCUIT | TCM internal circuit malfunction: Communication error output is continuously for > 1 second |

---

## Inspection Chart for Diagnosis Codes <!-- EKA00100 -->

### Code No. P1704, P1703, P1702 — Throttle position sensor system

If the TPS output voltage is 4.8 V or higher when the engine is idling, the output is judged to be too high and diagnosis code No.P1704 is output. If the TPS output voltage is 0.2 V or lower at times other than when the engine is idling, the output is judged to be too low and diagnosis code No.P1703 is output. If the TPS output voltage is 0.2 V or lower or it is 1.2 V or higher when the engine is idling, the TPS adjustment is judged to be incorrect and diagnosis code P1702 set.

| Code | Diagnosis item | Probable cause |
|------|---------------|----------------|
| P1704 | Short circuit | Malfunction of the throttle position sensor |
| P1703 | Open circuit | Malfunction of connector |
| P1702 | Sensor misadjusted | Malfunction of the TCM |

**Flowchart:**
1. Throttle position check → NG → Replace
2. OK → Check the TPS connector → NG → Repair
3. OK → Harness check: Throttle position sensor - TCM → NG → Repair
4. OK → Check the trouble symptoms → NG → Replace the TCM

---

<!-- TR-24 -->
### Code No. P0720 — Output speed sensor system

If the output from the output shaft speed sensor is continuously 50% lower than the vehicle speed for 1 second or more while driving in 3rd or 4th gear at a speed of 30 km/h or more, it is judged to be an open circuit or short-circuit in the output shaft speed sensor and diagnosis code P0720 is set. If diagnosis code P0720 is set four times, the transmission is locked into 3rd gear (D range) or 2nd gear as a fail-safe measure.

| Code | Diagnosis item | Probable cause |
|------|---------------|----------------|
| P0720 | Short circuit/open circuit | Malfunction of the output shaft speed sensor |
| | | Malfunction of connector |
| | | Malfunction of the TCM |
| | | Malfunction of the transfer drive gear or driven gear |

### Code No. P0703 — Stop lamp switch system

If the stop lamp switch is on for 5 minutes or more while driving, it is judged that there is a short circuit in the stop lamp switch and diagnostic trouble code P0703 is output.

| Code | Diagnosis item | Probable cause |
|------|---------------|----------------|
| P0703 | Short circuit/open circuit | Malfunction of the stop lamp switch |
| | | Malfunction of connector |
| | | Malfunction of the TCM |

### Code No. P0750 — Low and reverse solenoid valve system
### Code No. P0755 — Underdrive solenoid valve system
### Code No. P0760 — Second solenoid valve system
### Code No. P0765 — Overdrive solenoid valve system

If the resistance value for a solenoid valve is too large or too small, it is judged that there is a short or an open circuit in the solenoid valve and the respective diagnosis code is set. The transmission is locked into 3rd gear as a fail-safe measure.

| Code | Diagnosis item | Probable cause |
|------|---------------|----------------|
| P0750 | Short circuit/Open circuit | Malfunction of solenoid valve |
| P0755 | | Malfunction of connector |
| P0760 | | Malfunction of the TCM |
| P0765 | | |

### Code No. P0743 — Torque converter clutch solenoid valve system

If the resistance value for the torque converter clutch solenoid is too large or too small, it is judged that there is a short circuit or an open circuit in the solenoid valve and the respective diagnosis code is set. The transmission is locked into 3rd gear as a fail-safe measure.

| Code | Diagnosis item | Probable cause |
|------|---------------|----------------|
| P0743 | Short circuit/Open circuit | Malfunction of the torque converter clutch solenoid |
| | | Malfunction of connector |
| P0740 | Defective system | Malfunction of the TCM |

---

<!-- TR-25 -->
### Code No. P0731 — 1st gear ratio does not meet the specification

If the output from the output shaft speed sensor multiplied by the 1st gear ratio is not the same as the output from the input shaft speed sensor after the shift to 1st gear has been completed, diagnosis code P0731 is set. If diagnosis code P0731 is set four times, the transmission is locked into 3rd gear as a fail-safe measure.

| Code | Diagnosis item | Probable cause |
|------|---------------|----------------|
| P0731 | | Malfunction of the input shaft speed sensor |
| | | Malfunction of the output shaft speed sensor |
| | | Malfunction of the underdrive clutch retainer |
| | | Malfunction of the transfer drive gear or driven gear |
| | | Malfunction of the low and reverse brake system |
| | | Malfunction of the underdrive clutch system |
| | | Noise generated |

### Code No. P0732 — 2nd gear ratio does not meet the specification

If the output from the output shaft speed sensor multiplied by the 2nd gear ratio is not the same as the output from the input shaft speed sensor after the shift to 3rd gear has been completed, diagnosis code P0732 is set. If diagnosis code P0732 is set four times, the transmission is locked into 3rd gear as a fail-safe measure.

| Code | Diagnosis item | Probable cause |
|------|---------------|----------------|
| P0732 | | Malfunction of the input shaft speed sensor |
| | | Malfunction of the output shaft speed sensor |
| | | Malfunction of the underdrive clutch retainer |
| | | Malfunction of the transfer drive gear or driven gear |
| | | Malfunction of the underdrive clutch system |
| | | Malfunction of the second brake system |
| | | Noise generated |

### Code No. P0733 — 3rd gear ratio does not meet the specification

If the output from the output shaft speed sensor multiplied by the 3rd gear ratio is not the same as the output from the input shaft speed sensor after the shift to 3rd gear has been completed, diagnosis code P0733 is set. If diagnosis code P0733 is set four times, the transaxle is locked into 3rd gear as a fail-safe measure.

| Code | Diagnosis item | Probable cause |
|------|---------------|----------------|
| P0733 | | Malfunction of the input shaft speed sensor |
| | | Malfunction of the output shaft speed sensor |
| | | Malfunction of the underdrive clutch retainer |
| | | Malfunction of the transfer drive gear or driven gear |
| | | Malfunction of the underdrive clutch system |
| | | Malfunction of the overdrive clutch system |
| | | Noise generated |

### Code No. P0734 — 4th gear ratio does not meet the specification

If the output from the output shaft speed sensor multiplied by the 4th gear ratio is not the same as the output from the input shaft speed sensor after the shift to 4th gear has been completed, diagnosis code P0734 is the output. If diagnostic trouble code P0734 is the output four times, the transaxle is locked into 3rd gear as a fail-safe measure.

| Code | Diagnosis item | Probable cause |
|------|---------------|----------------|
| P0734 | | Malfunction of the input shaft speed sensor |
| | | Malfunction of the output shaft speed sensor |
| | | Malfunction of the underdrive clutch retainer |
| | | Malfunction of the transfer drive gear or driven gear |
| | | Malfunction of the second brake system |
| | | Malfunction of the overdrive clutch system |
| | | Noise generated |

### Code No. P0736 — Reverse gear ratio does not meet the specification

If the output from the output shaft speed sensor multiplied by the reverse gear ratio is not the same as the output from the input shaft speed sensor after the shift to reverse gear has been completed, diagnosis code P0736 is set. If diagnosis code P0736 is set four times, the transaxle is locked into 3rd gear as a fail-safe measure.

| Code | Diagnosis item | Probable cause |
|------|---------------|----------------|
| P0736 | | Malfunction of the input shaft speed sensor |
| | | Malfunction of the output shaft speed sensor |
| | | Malfunction of the underdrive clutch retainer |
| | | Malfunction of the transfer drive gear or driven gear |
| | | Malfunction of the low and reverse brake system |
| | | Malfunction of the reverse clutch system |
| | | Noise generated |

---

<!-- TR-26 -->
### Code No. P1749 — Serial communication

If normal communication is not possible for a continuous period of 1 second or more when the ignition switch is at the ON position, the battery voltage is 10 V or more and the engine speed is 450 r/min or more, diagnosis code No.P1749 is set. Diagnosis code No.P1749 is also set if the data being received is abnormal for a continuous period of 4 seconds under the same conditions.

| Code | Diagnosis item | Probable cause |
|------|---------------|----------------|
| P1749 | | Malfunction of connector |
| | | Malfunction of the ECM |
| | | Malfunction of the TCM |

### Code No. P1723 — A/T control relay system

If the A/T control relay voltage is less than 7 V after the ignition switch has been turned ON, it is judged that there is an open circuit or a short-circuit in the A/T control relay earth and diagnostic trouble code P1723 is output. The transmission is locked into 3rd gear as a fail-safe measure.

| Code | Diagnosis item | Probable cause |
|------|---------------|----------------|
| P1723 | Short circuit to ground/Open circuit | Malfunction of the A/T control relay |
| | | Malfunction of connector |
| | | Malfunction of the TCM |

### Code No. P0707 — Transaxle range switch

No signal is continuous for > 30 seconds.

### Code No. P0708

Above 2 signals are continuous for > 30 seconds.

| Code | Diagnosis item | Probable cause |
|------|---------------|----------------|
| P0707 | | Malfunction of transaxle range switch |
| P0708 | | |

### Code No. P1630 — CAN-BUS OFF

- No 3 speed hold fail
- No PGA, B fail
- Battery voltage > 10V continuously for 0.5 second
- No engine stop
- Receive BUS OFF information from CAN CONTROLLER

| Probable cause |
|----------------|
| TCM Fail |
| TCM side open & short |

### Code No. P1631 — CAN-TIME OUT ECM

- No 3 speed hold fail
- No PGA, B fail
- Battery voltage > 10V continuously for 0.5 second
- No engine stop
- No output signal for 1.5 second

| Probable cause |
|----------------|
| ECM fail |
| ECM side open & short |

### Code No. P1764 — TCM CAN MI-COM

- No 3 speed hold fail
- No PGA, B fail
- Battery voltage > 10V continuously for 0.5 second
- No engine stop
- Communication error output is continuously for > 1 second

| Probable cause |
|----------------|
| CAN MI-COM CIRCUIT |

---

<!-- TR-27 -->
## Inspection Chart for Trouble Symptoms <!-- EKA90130 -->

| Trouble symptom | Probable cause |
|-----------------|---------------|
| **Communication with HI-SCAN is not possible.** If communication with the HI-SCAN is not possible, the cause is probably a defective diagnosis line or the TCM is not functioning. | Malfunction diagnosis line · Malfunction of connector · Malfunction of the TCM |
| **Starting impossible.** Starting is not possible when the selector lever is in P or N range. In such cases, the cause is probably a defective engine system, torque converter or oil pump. | Malfunction of the engine system · Malfunction of the torque converter · Malfunction of the oil pump |
| **Does not move forward.** If the vehicle does not move forward when the selector lever is shifted from N to D, 3, 2 or L range while the engine is idling, the cause is probably abnormal line pressure or a malfunction of the underdrive clutch or valve body. | Abnormal line pressure · Malfunction of the underdrive solenoid valve · Malfunction of the underdrive clutch · Malfunction of the valve body |
| **Does not reverse.** If the vehicle does not reverse when the selector lever is shifted from N to R range while the engine is idling, the cause is probably abnormal pressure in the reverse clutch or low and reverse brake or a malfunction of the reverse clutch, low and reverse brake or valve body. | Abnormal reverse clutch pressure · Abnormal low and reverse brake pressure · Malfunction of the low and reverse solenoid valve · Malfunction of the reverse clutch · Malfunction of the low and reverse brake · Malfunction of the valve body |
| **Does not move (forward or reverse).** If the vehicle does not move forward or reverse when the selector lever is shifted to any position while the engine is idling, the cause is probably abnormal line pressure or a malfunction of the power train, oil pump or valve body. | Abnormal line pressure · Malfunction of power train · Malfunction of the oil pump · Malfunction of the valve body |
| **Engine stalling when shifting.** If the engine stalls when the selector lever is shifted from N to D or R range while the engine is idling, the cause is probably a malfunction of the engine system, damper clutch solenoid valve, valve body or torque converter (damper clutch malfunction). | Malfunction of the engine system · Malfunction of the damper clutch control solenoid valve · Malfunction of the valve body · Malfunction of the torque converter (Malfunction of the damper clutch) |
| **Shocks when changing from N to D and large time lag.** If abnormal shocks or a time lag of 2 seconds or more occur when the selector lever is shifted from N to D range while the engine is idling, the cause is probably abnormal underdrive clutch pressure or a malfunction of the underdrive clutch, valve body or idle position switch. | Abnormal underdrive clutch pressure · Malfunction of the underdrive solenoid valve · Malfunction of the valve body · Malfunction of the idle position switch |

---

<!-- TR-28 -->

| Trouble symptom | Probable cause |
|-----------------|---------------|
| **Shocks when changing from N to R and large time lag.** If abnormal shocks or a time lag of 2 seconds or more occur when the selector lever is shifted from N to R range while the engine is idling, the cause is probably abnormal reverse clutch pressure or low and reverse brake pressure, or a malfunction of the reverse clutch, low and reverse brake, valve body or idle position switch. | Abnormal reverse clutch pressure · Abnormal low and reverse brake pressure · Malfunction of the low and reverse solenoid valve · Malfunction of the reverse clutch · Malfunction of the low and reverse brake · Malfunction of the valve body · Malfunction of the idle position switch |
| **Shocks when changing from N to D, N to R and large time lag.** If abnormal shocks or a time lag of 2 seconds or more occur when the selector lever is shifted from N to D range and from N to R range while the engine is idling, the cause is probably abnormal line pressure or a malfunction of the oil pump or valve body. | Abnormal line pressure · Malfunction of the oil pump · Malfunction of the valve body |
| **Shocks and running up.** If shocks occur when driving due to up shifting or down shifting and the transmission speed becomes higher than the engine speed, the cause is probably abnormal line pressure or a malfunction of a solenoid valve, oil pump, valve body or of a brake or clutch. | Abnormal line pressure · Malfunction of each solenoid valve · Malfunction of the oil pump · Malfunction of the valve body · Malfunction of each brake or each clutch |
| **Displaced shifting points.** If all shift points are displaced while driving, the cause is probably a malfunction of the output shaft speed sensor, TPS or a solenoid valve. **All points.** | Malfunction of the output shaft speed sensor · Malfunction of the throttle position sensor · Malfunction of each solenoid valve · Abnormal line pressure · Malfunction of the valve body · Malfunction of the TCM |
| **Some points.** If some of the shift points are displaced while driving, the cause is probably a malfunction of the valve body, or it is related to control and is not an abnormality. | Malfunction of the valve body |
| **Does not shift.** If shifting does not occur while driving and no diagnosis codes are output, the cause is probably a malfunction of the transaxle range switch, or TCM. **No diagnosis codes.** | Malfunction of the transaxle range switch · Malfunction of the TCM |
| **Malfunction while driving.** If acceleration is poor even if downshifting occurs while driving, the cause is probably a malfunction of the engine system or of a brake or clutch. **Poor acceleration.** | Malfunction of the engine system · Malfunction of the brake or clutch |
| **Malfunction while driving.** If vibration occurs when driving at constant speed or when accelerating and deceleration in top range, the cause is probably abnormal damper clutch pressure or a malfunction of the engine system, damper clutch control solenoid valve, valve body or torque converter. **Vibration.** | Abnormal damper clutch pressure · Malfunction of the engine system · Malfunction of the damper clutch control solenoid valve · Malfunction of the torque converter · Malfunction of the valve body |
| **Transaxle range switch system.** The cause is probably a malfunction of the inhibitor switch circuit, ignition switch circuit or a defective TCM. | Malfunction of the transaxle range switch · Malfunction of the ignition switch · Malfunction of connector · Malfunction of the TCM |

---

<!-- TR-29 -->

| Trouble symptom | Probable cause |
|-----------------|---------------|
| **Idle position switch system.** The cause is probably a defective idle position switch circuit, or a defective TCM. | Malfunction of the triple pressure switch · Malfunction of connector · Malfunction of the TCM |
| **Triple pressure switch system.** The cause is probably a defective dual pressure switch circuit or a defective TCM. | Malfunction of the triple pressure switch · Malfunction of connector · Malfunction of A/C system · Malfunction of the TCM |
| **Vehicle speed sensor system.** The cause is probably a defective vehicle speed sensor circuit or a defective TCM. | Malfunction of the vehicle speed sensor · Malfunction of connector · Malfunction of the TCM |

---

## Elements in Use in Each Gear <!-- EKA90140 -->

| Operating element / Selector lever position | Underdrive clutch (UD) | Reverse clutch (REV) | Overdrive clutch (OD) | Low-and-reverse brake (LR) | Second brake (2nd) | One way clutch (OWC) |
|---|---|---|---|---|---|---|
| P (Parking) | - | - | - | O | - | - |
| R (Reverse) | - | O | - | O | - | - |
| N (Neutral) | - | - | - | O | - | - |
| D - 1st | O | - | - | - | - | O |
| D - 2nd | O | - | - | - | O | - |
| D - 3rd | O | - | O | - | - | - |
| D - 4th | - | - | O | - | - | - |
| 3 - 1st | O | - | - | - | - | O |
| 3 - 2nd | O | - | - | - | O | - |
| 3 - 3rd | O | - | O | - | - | - |
| 2 - 1st | O | - | - | - | - | O |
| 2 - 2nd | O | - | - | - | O | - |
| L - 1st | O | - | - | O | - | - |

O = Engaged

## Operating Elements and Their Function

| Operating element | Code | Function |
|-------------------|------|----------|
| Underdrive clutch | UD | Connects input shaft and underdrive sun gear |
| Reverse clutch | REV | Connects input shaft and reverse sun gear |
| Overdrive clutch | OD | Connects input shaft and overdrive planetary carrier |
| Low-and-reverse brake | LR | Locks low-and-reverse annulus gear and overdrive planetary carrier |
| Second brake | 2ND | Locks reverse sun gear |

---

<!-- TR-30 -->
## Inspection Process for Diagnostic Trouble Codes <!-- EKCR0075 -->

### Code No. P1704, P1703, P1702 — Throttle position sensor system

If the TPS output voltage is 4.8 V or higher when the engine is idling, the output is judged to be too high and diagnostic trouble code No.P1704 is output. If the TPS output voltage is 0.2 V or lower at times other than when the engine is idling, the output is judged to be too low and diagnostic trouble code No.P1703 is output. If the TPS output voltage is 0.2 V or lower or it is 1.2 V or higher when the engine is idling, the TPS adjustment is judged to be incorrect and diagnostic trouble code P1702 set.

| Possible cause |
|----------------|
| Malfunction of the throttle position sensor · Malfunction of connector · Malfunction of the TCM |

**Flowchart:**
1. Throttle position check → NG → Replace
2. OK → Check the TPS connector → NG → Repair
3. OK → Harness check: Throttle position sensor - TCM → NG → Repair
4. OK → Check the trouble symptoms → NG → Replace the TCM

---

<!-- TR-31 -->
### Code No. P0710, Oil temperature sensor system

If the oil temperature sensor output voltage is 2.6 V or more even after driving for 10 minutes or more (if the oil temperature does not increase), it is judged that there is an open circuit in the oil temperature sensor and diagnostic trouble code No.P0713 is output. If the oil temperature sensor output detects the voltage which corresponds to 200°C (392°F) or more for more than one second, it is judged that there is an open circuit in oil temperature sensor and diagnostic trouble code No. P0710 is output.

| Possible cause |
|----------------|
| Malfunction of the oil temperature sensor · Malfunction of connector · Malfunction of the TCM |

**Flowchart:**
1. Oil temperature check → NG → Replace
2. OK → Check the following connector: 2.0L: C04, 2.7L: C104 → NG → Repair
3. OK → Harness check: Oil temperature sensor - TCM → NG → Repair
4. OK → Check the trouble symptoms → NG → Replace the TCM

---

<!-- TR-32 -->
<!-- figure: Solenoid valve control wiring diagram — 2.0L variant showing TCM connections via C36-2, C36-1, C36-2 to LR, DCC, OD, 2ND, UD, OT solenoid valves and oil temp sensor via C04 with ATM idle solenoid valve -->

<!-- figure: Solenoid valve control wiring diagram — 2.7L variant showing TCM connections via C136-0, C136-1, C136-2 to LR, DCC, OD, 2ND, UD, OT solenoid valves and oil temp sensor via C104 with ATM idle solenoid valve -->

---

<!-- TR-33 -->
### Code No. P0725 — Crankshaft position sensor system

If no output pulse is detected from the crankshaft position sensor for 5 seconds or more while driving at 25 km/h (16 mph) or more, it is judged that there is an open circuit in the crankshaft position sensor and diagnostic trouble code No.P0725 is set.

| Possible cause |
|----------------|
| Malfunction of the crankshaft position sensor · Malfunction of connector · Malfunction of the TCM |

**Flowchart:**
1. Check the connector → NG → Replace
2. OK → Harness check: Crankshaft position sensor - TCM → NG → Repair
3. OK → Crankshaft position sensor check
4. OK → Check the trouble symptoms → NG → Replace the TCM

---

<!-- TR-34 -->
### Code No. P0715 — Input shaft speed sensor system (Pulse generator 'A')

If no output pulse is detected from the input shaft speed sensor for 1 second or more while driving in 3rd or 4th gear at a speed of 30 km/h (19 mph) or more, it is judged to be an open or short circuit in the input shaft speed sensor and diagnostic trouble code No.P0715 is output. If diagnostic trouble code P0715 is output four times, the transaxle is locked into 3rd gear or 2nd gear as a fail-safe measure.

| Possible cause |
|----------------|
| Malfunction of the input shaft speed sensor (PG-A) · Malfunction of underdrive clutch retainer · Malfunction of connector · Malfunction of the TCM |

**Flowchart:**

1. Measure at the input shaft sensor connector (2.0L: C02-1, 2.7L: C102-1)
   - Disconnect the connector and check at the harness side.
   - Voltage between terminal 3 and ground (Ignition switch: ON) → OK: Battery voltage
   - Voltage between terminal 2 and ground (Ignition switch: ON) → OK: Approx. 5V
   - Continuity between terminal 1 and ground → OK: Continuity
   - NG → Check the connector → NG → Repair
   - OK → Check the following harness:
     - Between input shaft speed (PG-A) sensor and ignition switch
     - Between input shaft speed (PG-A) sensor and TCM
     - NG → Repair
2. OK → Measure output waveform from the input shaft speed sensor.
   - Engine: 2,000 rpm (approx. 50 km/h (31 mph))
   - Selector lever position: D
   - NG → Replace the TCM → NG → Replace the input shaft speed sensor (PG-A)
   - OK → Check trouble symptoms
3. OK → Check trouble symptoms
   - NG → Replace the TCM
4. NG → A/T overhaul: Replace the transfer drive gear and driven gear
   - Check trouble symptoms → NG → Eliminate the cause of the noise

---

<!-- TR-35 -->
<!-- figure: A/T Pulse Generator #1 wiring diagram — 2.0L variant showing C02-1 connector to Pulse generator #1 (input speed) and TCM via C36-3 -->
<!-- figure: A/T Pulse Generator #1 wiring diagram — 2.7L variant showing C102-1 connector to Pulse generator #1 (input speed) and TCM via C136-3 -->

---

<!-- TR-36 -->
### Code No. P0720 — Output shaft sensor system (Pulse generator 'B')

If the output from the output shaft speed sensor is continuously 50% lower than the vehicle speed for 1 second or more, it is judged to be an open or short circuit in the output shaft speed sensor (PG-B) and diagnostic trouble code No.P0720 is output.

| Possible cause |
|----------------|
| Malfunction of the output shaft sensor (PG-B) · Malfunction of connector · Malfunction of the TCM |

**Flowchart:**

1. Measure at the output shaft sensor (PG-B) connector (2.0L: C02-2, 2.7L: C102-2)
   - Disconnect the connector and check at the harness side.
   - Voltage between terminal 3 and ground (Ignition switch: ON) → OK: Battery voltage
   - Voltage between terminal 2 and ground (Ignition switch: ON) → OK: Approx. 5V
   - Continuity between terminal 1 and ground → OK: Continuity
   - NG → Check the connector → NG → Repair
   - OK → Harness check:
     - Between output shaft speed sensor and ignition switch
     - Between output shaft speed sensor and TCM
     - NG → Repair
2. OK → Check trouble symptoms → OK → Replace the TCM
3. NG → Replace the output shaft speed sensor
   - OK → Check trouble symptoms
   - NG → A/T overhaul: Replace the transfer drive gear and driven gear
     - Check trouble symptoms → NG → Eliminate the cause of the noise

---

<!-- TR-37 -->
<!-- figure: A/T Pulse Generator #2 wiring diagram — 2.0L variant showing C02-2 connector to Pulse generator #2 (output speed) and TCM via C36-2 -->
<!-- figure: A/T Pulse Generator #2 wiring diagram — 2.7L variant showing C102-2 connector to Pulse generator #2 (output speed) and TCM via C136-2 -->

---

<!-- TR-38 -->
### Code No. P0703 — Stop light switch system

If the stop light switch is on for 5 minutes or more while driving, it is judged that there is a short circuit in the stop light switch and diagnostic trouble code P0703 is output.

| Possible cause |
|----------------|
| Malfunction of the stop light switch · Malfunction of connector · Malfunction of the TCM |

**Flowchart:**
1. Stop light switch check → NG → Replace
2. OK → Check the connector → NG → Repair
3. OK → Harness check (2.0L: C36-3 (No.9), 2.7L: C136-3 (No.9)): Between stop light switch and TCM → NG → Repair
4. OK → Check the trouble symptoms → NG → Replace the TCM

---

<!-- TR-39 -->
### Code No. P0750 — Low and reverse solenoid valve system
### Code No. P0755 — Underdrive solenoid valve system
### Code No. P0760 — Second solenoid valve system
### Code No. P0765 — Overdrive solenoid valve system

If the resistance value for a solenoid valve is too large or too small, it is judged that there is a short or an open circuit in the solenoid valve and the respective diagnostic code is output. The transaxle is locked into 3rd gear as a fail-safe measure.

| Possible cause |
|----------------|
| Malfunction of the solenoid valve · Malfunction of connector · Malfunction of the TCM |

**Flowchart:**
1. Solenoid valve check → NG → Replace
2. OK → Check the connector (2.0L: C04, 2.7L: C104) → NG → Repair
3. OK → Harness check: Between solenoid valve and TCM → NG → Repair
4. OK → Replace the solenoid valve
5. OK → Check the trouble symptoms → NG → Replace the TCM

---

<!-- TR-40 -->
<!-- figure: Solenoid valve control wiring diagram — 2.0L variant showing TCM connections via C36-2, C36-1, C36-2 to LR, DCC, OD, 2ND, UD, OT solenoid valves and oil temp sensor via C04 with ATM idle solenoid valve -->

<!-- figure: Solenoid valve control wiring diagram — 2.7L variant showing TCM connections via C136-0, C136-1, C136-2 to LR, DCC, OD, 2ND, UD, OT solenoid valves and oil temp sensor via C104 with ATM idle solenoid valve -->

---

<!-- TR-41 -->
### Code No. P0743 / P0740 — Torque converter clutch solenoid system

If the resistance value for the torque converter clutch solenoid is too large or too small, it is judged that there is a short or an open circuit in the torque converter clutch solenoid and diagnostic trouble code No.P0743 is output. If the drive duty rate for the torque converter clutch solenoid is 100% for a continuous period of 4 seconds or more, it is judged that there is an abnormality in the torque converter clutch system and diagnostic trouble code No.P0740 is output. When diagnostic trouble code No.P0743 is the output, the transaxle is locked into 3rd gear as a fail-safe measure. If the lock-up clutch remains engaged for a continuous period of 10 seconds when the TCM is attempting to disengage the lock-up clutch, it is judged that the torque converter clutch is stuck on and diagnostic trouble code P0740 is output.

| Possible cause |
|----------------|
| Malfunction of the torque converter clutch solenoid · Malfunction of connector · Malfunction of the TCM |

**Flowchart:**
1. Torque converter clutch solenoid check → NG → Replace
2. OK → Check the connector (2.0L: C04, 2.7L: C104) → NG → Repair
3. OK → Harness check: Between torque converter clutch solenoid → NG → Repair
4. OK → Replace the torque converter clutch solenoid
5. OK → Check the trouble symptoms → NG → Replace the TCM

*Only when code No.P0740 is the output, check INSPECTION PROCEDURE 6: Engine stalling when shifting*

---

<!-- TR-42 -->
### Code No. P0731 — 1st gear incorrect ratio

If the output from the output shaft speed sensor multiplied by the 2nd gear ratio is not the same as the output from the input shaft speed sensor after shifting to 2nd gear has been completed, diagnostic trouble code P0732 is output four times, the transaxle is locked into 3rd gear as a fail-safe measure.

| Possible cause |
|----------------|
| Malfunction of the input shaft speed sensor · Malfunction of the output shaft speed sensor · Malfunction of the underdrive clutch retainer · Malfunction of the transfer drive gear or driven gear · Malfunction of the low and reverse brake system · Malfunction of the underdrive clutch system · Noise generated |

**Flowchart:**
1. SCAN TOOL DTC: Is the diagnostic trouble code No.P0715 the output? → YES → Code No.P0715 input shaft speed sensor system check
2. SCAN TOOL DTC: Is the diagnostic trouble code No.P0720 the output? → YES → Code No.P0720 output shaft speed sensor system check
3. NO → Measure output waveform from the input shaft speed sensor (Using an oscilloscope)
   - Engine: 2,000 rpm (approx. 50km/h (31 mph))
   - Selector lever position: D
   - NG → Replace the input shaft speed sensor → Check the trouble symptoms → NG → A/T overhaul: Replace the underdrive clutch retainer → Check the trouble symptoms → NG → Eliminate the cause of the noise
4. OK → Measure output waveform from the output shaft speed sensor (Using an oscilloscope)
   - Engine: 2,000 rpm (approx. 50 km/h (30 mph))
   - Selector lever position: D
   - NG → Replace the output shaft speed sensor → Check trouble symptoms → NG → A/T overhaul: Replace the transfer drive gear and driven gear → Check trouble symptoms → Eliminate the cause of the noise
5. NO → A/T overhaul: Replace the underdrive clutch. Replace the low and reverse clutch.

---

<!-- TR-43 -->
### Code No. P0732 — 2nd gear incorrect ratio

If the output from the output shaft speed sensor multiplied by the 2nd gear ratio is not the same as the output from the input shaft speed sensor after shifting to 2nd gear has been completed, diagnostic trouble code P0732 is output. If diagnostic trouble code P0732 is output four times, the transaxle is locked into 3rd gear as a fail-safe measure.

| Possible cause |
|----------------|
| Malfunction of the input shaft speed sensor · Malfunction of the output shaft speed sensor · Malfunction of the underdrive clutch retainer · Malfunction of the transfer drive gear or driven gear · Malfunction of the second brake system · Malfunction of the underdrive clutch system · Noise generated |

**Flowchart:**
1. SCAN TOOL DTC: Is the diagnostic trouble code No.P0715 the output? → YES → Code No.P0715 input shaft speed sensor system check
2. SCAN TOOL DTC: Is the diagnostic trouble code No.P0720 the output? → YES → Code No.P0720 output shaft speed sensor system check
3. NO → Measure output waveform from the input shaft speed sensor (Using an oscilloscope)
   - Engine: 2,000 rpm (approx. 50km/h (31 mph))
   - Selector lever position: D
   - NG → Replace the input shaft speed sensor → Check the trouble symptoms → NG → A/T overhaul: Replace the underdrive clutch retainer → Check the trouble symptoms → NG → Eliminate the cause of the noise
4. OK → Measure output waveform from the output shaft speed sensor (Using an oscilloscope)
   - Engine: 2,000 rpm (approx. 50 km/h (31 mph))
   - Selector lever position: D
   - OK: A waveform (Inspection Procedure Using an Oscilloscope) is output (flashing between 0 ← → 5V) and there is no noise appearing in the waveform.
   - NG → Replace the output shaft speed sensor → Check the trouble symptoms → NG → A/T overhaul: Replace the transfer drive gear and driven gear → Check trouble symptoms → Eliminate the cause of the noise
5. NO → A/T overhaul: Replace the underdrive clutch. Replace the second clutch.

---

<!-- TR-44 -->
### Code No. P0733 — 3rd gear incorrect ratio

If the output from the output shaft speed sensor multiplied by the 3rd gear ratio is not the same as the output from the input shaft speed sensor after shifting to 3rd gear has been completed, diagnostic trouble code P0733 is output. If diagnostic trouble code P0733 is output four times, the transaxle is locked into 3rd gear as a fail-safe measure.

| Possible cause |
|----------------|
| Malfunction of the input shaft speed sensor · Malfunction of the output shaft speed sensor · Malfunction of the underdrive clutch retainer · Malfunction of the transfer drive gear or driven gear · Malfunction of the overdrive clutch system · Malfunction of the underdrive clutch system · Noise generated |

**Flowchart:**
1. SCAN TOOL DTC: Is the diagnostic trouble code No.P0715 the output? → YES → Code No.P0715 input shaft speed sensor system check
2. SCAN TOOL DTC: Is the diagnostic trouble code No.P0720 the output? → YES → Code No.P0720 output shaft speed sensor system check
3. NO → Measure output waveform from the input shaft speed sensor (Using an oscilloscope)
   - Engine: 2,000 rpm (approx. 50km/h (31 mph))
   - Selector lever position: D
   - OK: A waveform (Inspection Procedure Using an Oscilloscope) is output (flashing between 0 ← → 5V) and there is no noise appearing in the waveform.
   - NG → Replace the input shaft speed sensor → Check the trouble symptoms → NG → A/T overhaul: Replace the underdrive clutch retainer → Check the trouble symptoms → NG → Eliminate the cause of the noise
4. OK → Measure output waveform from the output shaft speed sensor (Using an oscilloscope)
   - Engine: 2,000 rpm (approx. 50 km/h (31 mph))
   - Selector lever position: D
   - NG → Replace the output shaft speed sensor → Check the trouble symptoms → NG → A/T overhaul: Replace the transfer drive gear and driven gear → Check trouble symptoms → Eliminate the cause of the noise
5. NO → A/T overhaul: Replace the underdrive clutch. Replace the overdrive clutch.

---

<!-- TR-45 -->
### Code No. P0734 — 4th gear incorrect ratio

If the output from the output shaft speed sensor multiplied by the 4th gear ratio is not the same as the output from the input shaft speed sensor after shifting to 4th gear has been completed, diagnostic trouble code P0734 is the output. If diagnostic trouble code P0734 is the output four times, the transaxle is locked into 3rd gear as a fail-safe measure.

| Possible cause |
|----------------|
| Malfunction of the input shaft speed sensor · Malfunction of the output shaft speed sensor · Malfunction of the underdrive clutch retainer · Malfunction of the transfer drive gear or driven gear · Malfunction of the second brake system · Malfunction of the overdrive clutch system · Noise generated |

**Flowchart:**
1. SCAN TOOL DTC: Is the diagnostic trouble code No.P0715 the output? → YES → Code No.P0715 input shaft speed sensor system check
2. SCAN TOOL DTC: Is the diagnostic trouble code No.P0720 the output? → YES → Code No.P0720 output shaft speed sensor system check
3. NO → Measure output waveform from the input shaft speed sensor (Using an oscilloscope)
   - Engine: 2,000 rpm (approx. 50km/h (31 mph))
   - Selector lever position: D
   - OK: A waveform (Inspection Procedure Using an Oscilloscope) is output (flashing between 0 ← → 3.5V) and there is no noise appearing in the waveform.
   - NG → Replace the input shaft speed sensor → Check the trouble symptoms → NG → A/T overhaul: Replace the underdrive clutch retainer → Check the trouble symptoms → NG → Eliminate the cause of the noise
4. OK → Measure output waveform from the output shaft speed sensor (Using an oscilloscope)
   - Engine: 2,000 rpm (approx. 50 km/h (31 mph))
   - Selector lever position: D
   - NG → Replace the output shaft speed sensor → Check the trouble symptoms → NG → A/T overhaul: Replace the transfer drive gear and driven gear → Check trouble symptoms → Eliminate the cause of the noise
5. NO → A/T overhaul: Replace the overdrive clutch. Replace the second clutch.

---

<!-- TR-46 -->
### Code No. P0736 — Reverse gear incorrect ratio

If the output from the output shaft speed sensor multiplied by the reverse gear ratio is not the same as the output from the input shaft speed sensor after shifting to reverse gear has been completed, diagnostic trouble code P0736 is output. If diagnostic trouble code P0736 is output four times, the transaxle is locked into 3rd gear as a fail-safe measure.

| Possible cause |
|----------------|
| Malfunction of the input shaft speed sensor · Malfunction of the output shaft speed sensor · Malfunction of the underdrive clutch retainer · Malfunction of the transfer drive gear or driven gear · Malfunction of the low and reverse brake system · Malfunction of the reverse clutch system · Noise generated |

**Flowchart:**
1. SCAN TOOL DTC: Is the diagnostic trouble code No.P0715 the output? → YES → Code No.P0715 input shaft speed sensor system check
2. SCAN TOOL DTC: Is the diagnostic trouble code No.P0720 the output? → YES → Code No.P0720 output shaft speed sensor system check
3. NO → Measure output waveform from the input shaft speed sensor (Using an oscilloscope)
   - Engine: 2,000 rpm (approx. 50km/h (31 mph))
   - Selector lever position: D
   - OK: A waveform (Inspection Procedure Using an Oscilloscope) is output (flashing between 0 ← → 5V) and there is no noise appearing in the waveform.
   - NG → Replace the input shaft speed sensor → Check the trouble symptoms → NG → A/T overhaul: Replace the underdrive clutch retainer → Check the trouble symptoms → NG → Eliminate the cause of the noise
4. OK → Measure output waveform from the output shaft speed sensor (Using an oscilloscope)
   - Engine: 2,000 rpm (approx. 50 km/h (31 mph))
   - Selector lever position: D
   - OK: A waveform (Inspection Procedure Using an Oscilloscope) is output (flashing between 0 ← → 5V) and there is no noise appearing in the waveform.
   - NG → Replace the output shaft speed sensor → Check the trouble symptoms → NG → A/T overhaul: Replace the transfer drive gear and driven gear → Check trouble symptoms → Eliminate the cause of the noise
5. NO → A/T overhaul: Replace the low and reverse brake. Replace the reverse clutch.

---

<!-- TR-47 -->
### Code No. P1723 — A/T Control relay system

If the relay voltage is less than 7 V after the ignition switch has been turned to ON, it is judged that there is an open or short circuit in the A/T control relay earth and diagnostic trouble code P1723 is output. The transaxle is locked into 3rd gear as a fail-safe measure.

| Possible cause |
|----------------|
| Malfunction of the A/T control relay · Malfunction of connector · Malfunction of the TCM |

**Flowchart:**
1. Check the A/T control relay → NG → Replace
2. OK → Check the connector (2.0L: C37, 2.7L: C137) → NG → Replace
3. OK → Harness check:
   - Between control relay and body ground
   - Between control relay and battery
   - Between control relay and TCM
   → NG → Replace
4. OK → Check the trouble symptoms → Replace the TCM

---

<!-- TR-48 -->
## Inspection Process for Trouble Symptoms <!-- EKA4260 -->

### Inspection Procedure 1

| Communication with the scan tool | Possible cause |
|----------------------------------|---------------|
| If communication with the scan tool is not possible, the cause may be a defective diagnostic trouble line or the TCM is not functioning. | Malfunction of diagnostic trouble line · Malfunction of connector · Malfunction of the TCM |

**Flowchart:**
1. Is communication with other systems possible using the scan tool?
   - NO → Check the diagnostic trouble line with the scan tool and repair if necessary
     - NG → Check the connectors: M07 → NG → Repair
     - OK → Harness check: Between power supply and TCM, Between ground and TCM → NG → Repair
     - OK → Check the trouble symptoms → OK → Replace the TCM
   - YES → Check the continuity and voltage of the TCM connector
     - NG → Check the connectors → NG → Repair
     - OK → Harness check: Between data link trouble connector and TCM → NG → Repair
     - OK → Check the trouble symptoms → NG → Replace the TCM

---

<!-- TR-49 -->
### Inspection Procedure 2

| Starting impossible | Possible cause |
|--------------------|---------------|
| Starting is not possible when the selector lever is in P or N range. In such cases, the cause may be a defective engine system, torque converter or oil pump. | Malfunction of the engine system · Malfunction of the torque converter · Malfunction of the oil pump |

**Flowchart:**
1. Is communication with other systems possible using the scan tool? → NG → Repair, Replace
2. OK → Torque converter check: Check for incorrect installation (inserted at an angle, etc.) and for damaged splines.
   - NG → Repair if possible. If the splines are damaged and repairs are not possible, replace the torque converter assembly.
3. OK → Replace the oil pump assembly. (The oil pump cannot be disassembled.)

---

<!-- TR-50 -->
### Inspection Procedure 3

| Does not move | Possible cause |
|---------------|---------------|
| If the vehicle does not move forward when the selector lever is shifted from N to D, 3, 2 or L range while the engine is idling, the cause may be abnormal line pressure or a malfunction of the underdrive clutch or valve body. | Abnormal line pressure · Malfunction of the underdrive solenoid valve · Malfunction of the underdrive clutch · Malfunction of the valve body |

**Flowchart:**
1. Scan Tool Actuator Test: Underdrive solenoid valve → OK: Sound of operation can be heard. → NG → Replace the solenoid valve
2. OK → Hydraulic pressure test: Measure the hydraulic pressure for each element when in range.
   - NG → Valve body disassembly, cleaning and reassembly. Pay particular attention to loosening of bolts, and valve bodies. If the damage cannot be repaired, replace the valve body assembly.
3. OK → Underdrive clutch system check: Remove the transaxle assembly, valve body cover and valve body. Piston should operate and pressure should be maintained when air is blown through the underdrive clutch oil hole in the transaxle case.
   - NG → Underdrive clutch check: Check for burning of the facing, defective piston seal rings, and interference at the retainer.

---

<!-- TR-51 -->
### Inspection Procedure 4

| Does not reverse | Possible cause |
|-----------------|---------------|
| If the vehicle does not reverse when the selector lever is shifted from N to R range while the engine is idling, the cause may be abnormal pressure in the reverse clutch or low and reverse brake or a malfunction of the reverse clutch, low and reverse brake or valve body. | Abnormal reverse clutch pressure · Abnormal low and reverse brake pressure · Malfunction of the low and reverse solenoid valve · Malfunction of the reverse clutch · Malfunction of the low and reverse brake · Malfunction of the valve body |

**Flowchart:**
1. Is communication with other systems possible using the scan tool? → NG → Repair, Replace
2. OK → Torque converter check: Check for incorrect installation (inserted at an angle, etc.) and for damaged splines.
   - NG → Repair if possible. If the splines are damaged and repairs are not possible, replace the torque converter assembly.
3. OK → Replace the oil pump assembly. (The oil pump cannot be disassembled.)

---

<!-- TR-52 -->
### Inspection Procedure 5

| Does not move (forward or reverse) | Possible cause |
|------------------------------------|---------------|
| If the vehicle does not move forward or reverse when the selector lever is shifted to any position while the engine is idling, the cause may be abnormal line pressure, or a malfunction of the power train, oil pump or valve body. | Abnormal line pressure · Malfunction of the underdrive solenoid valve · Malfunction of the underdrive clutch · Malfunction of the valve body |

**Flowchart:**
1. Hydraulic pressure check: Measure the hydraulic pressure for each element when moving forward and back.
   - NG → Replace the transaxle
   - OK → Check power train. If OK, replace transaxle.

---

<!-- TR-53 -->
### Inspection Procedure 6

| Engine stalling when shifting | Possible cause |
|------------------------------|---------------|
| If the engine stalls when the selector lever is shifted from N to D or R range while the engine is idling, the cause may be a malfunction of the engine system, torque converter clutch solenoid, valve body or torque converter (torque converter clutch malfunction). | Malfunction of the engine system · Malfunction of the torque converter clutch solenoid · Malfunction of the valve body · Malfunction of the torque converter (Malfunction of the torque converter clutch) |

**Flowchart:**
1. Engine system check: Check the control system, ignition, fuel system and main system. → NG → Repair, Replace
2. OK → Replace the torque converter clutch solenoid
3. NG → Replace the torque converter.

---

<!-- TR-54 -->
### Inspection Procedure 7

| Shocks when changing from N to D and range time lag | Possible cause |
|----------------------------------------------------|---------------|
| If abnormal shocks or a time lag of 2 seconds or more occurs when the selector lever is shifted from N to D range while the engine is idling, the cause may be abnormal underdrive clutch pressure or a malfunction of the underdrive clutch, valve body or closed throttle position switch. | Abnormal line pressure · Malfunction of the underdrive solenoid valve · Malfunction of the underdrive clutch · Malfunction of the valve body · Malfunction of the closed throttle position switch |

**Flowchart:**
1. Scan Tool Actuator Test: Underdrive solenoid valve → OK: Sound of operation can be heard.
   - NG → Replace the underdrive solenoid valve
2. OK → When does the shock occur?
   - When starting → Replace the underdrive solenoid valve
   - When shifting → Hydraulic pressure test: Measure the underdrive clutch pressure when shifting from N to D.
     - NG → Scan Tool Data list → OK: Turns from On to Off when the accelerator pedal is slightly depressed from the closed position → OK → Replace the transaxle.

---

<!-- TR-55 -->
### Inspection Procedure 8

| Shock when changing from N to R and large time lag | Possible cause |
|---------------------------------------------------|---------------|
| If abnormal shocks or a time lag of 2 seconds or more occurs when the selector lever is shifted from N to R range while the engine is idling, the cause may be abnormal reverse clutch pressure or low and reverse brake pressure, or a malfunction of the reverse clutch, low and reverse brake, valve body. | Abnormal reverse clutch pressure · Abnormal low and reverse brake pressure · Malfunction of the low and reverse solenoid valve · Malfunction of the reverse clutch · Malfunction of the low and reverse brake · Malfunction of the valve body |

**Flowchart:**
1. Scan Tool Data list: Low and reverse solenoid valve → OK: Sound of operation can be heard.
   - NG → Replace the low and reverse solenoid valve
2. OK → When does the shock occur?
   - When starting → Shock sometimes occur
   - When shifting → Hydraulic pressure test: Measure the reverse clutch pressure in R range.
     - NG → Scan Tool Data list → OK: Turns from on to off when the accelerator pedal is slightly depressed from the fully closed position. → OK → Replace the transaxle.
   - OK → Reverse clutch system and low and reverse brake system check: Remove the transaxle assembly, valve body cover and valve body. Piston should operate and pressure should be maintained when air is blown through the reverse clutch oil hole and reverse brake in the transaxle case.
     - NG → Valve body disassembly, cleaning and reassembly. Pay particular attention to the loosening of bolts, and to damage and slippage of O-rings, valves and valve bodies. If the damage cannot be repaired, replace the valve body assembly.
   - NG → Reverse clutch and low reverse brake check: Check the burning of the facing, defective piston seal rings and interference at the retainer.

---

<!-- TR-56 -->
### Inspection Procedure 9

| Shocks when changing from N to D, N to R and large time lag | Possible cause |
|------------------------------------------------------------|---------------|
| If abnormal shocks or a time lag of 2 seconds or more occurs when the selector lever is shifted from N to D, N to R range while the engine is idling, the cause may be abnormal line pressure or a malfunction of the oil pump or valve body. | Abnormal line pressure · Malfunction of the oil pump · Malfunction of the valve body |

**Flowchart:**
1. Hydraulic pressure test: Measure the hydraulic pressure for each element when in range D and range R.
   - NG → Replace the transaxle
2. OK → When does the shock occur?
   - When starting → Replace the transaxle
   - When shifting → Replace the oil pump assembly (The oil pump cannot be disassembled.)

---

<!-- TR-57 -->
### Inspection Procedure 10

| Shocks and running up | Possible cause |
|----------------------|---------------|
| If shocks occur when driving due to upshifting or downshifting and the transaxle speed becomes higher than the engine speed, the cause may be abnormal line pressure or a malfunction of a solenoid valve, oil pump, valve body or of a brake or clutch. | Abnormal line pressure · Malfunction of each solenoid valve · Malfunction of the oil pump · Malfunction of the valve body · Malfunction of each brake or each clutch |

**Flowchart:**
1. Scan Tool Actuator Test: Low and reverse solenoid valve, Underdrive solenoid valve, Second solenoid valve, Overdrive solenoid valve → OK: Sound of operation can be heard.
   - NG → Replace the solenoid valve
2. OK → Adjust the line pressure.
   - NG → Replace the oil pump assembly (The oil pump cannot be disassembled.)
   - NG → Valve body disassembly, cleaning, and reassembly. Pay particular attention to the loosening of bolts, and to damage and slippage of O-rings, valves, and valve bodies. If the damage cannot be repaired, replace the valve body assembly.
3. OK → Clutch and brake check: Check burning of the facing, defective seal rings, and interference on the retainer.

---

<!-- TR-58 -->
### Inspection Procedure 11

| All points (Displaced shifting points) | Possible cause |
|---------------------------------------|---------------|
| If all shift points are displaced while driving, the cause may be a malfunction of the output shaft speed sensor, TPS or a solenoid valve. | Malfunction of the output shaft speed sensor · Malfunction of the throttle position sensor · Malfunction of each solenoid valve · Abnormal line pressure · Malfunction of the valve body · Malfunction of the TCM |

**Flowchart:**
1. Scan Tool Data list: Output shaft speed sensor → OK: Increases in proportion to vehicle speed
2. OK → Scan Tool Data list: TPS → OK: Increases in proportion to accelerator pedal opening angle
3. OK → Scan Tool Data list: Low and reverse solenoid valve duty %, Underdrive solenoid valve duty %, Second solenoid valve duty %, Overdrive solenoid valve duty % → OK: Refer to the table below
   - OK → Replace the solenoid valve
   - OK → Replace the TCM
4. OK → Adjust the line pressure
   - OK → Valve body disassembly, cleaning and reassembly. Pay particular attention to the loosening of bolts, and to damage and slippage of O-rings, valves, and valve bodies. If the damage cannot be repaired, replace the valve body assembly.

---

<!-- TR-59 -->
### Inspection Procedure 12

| Some points (Displaced shifting points) | Possible cause |
|----------------------------------------|---------------|
| If some of the shift points are displaced while driving, the cause may be a malfunction of the valve body, or it is related to control and is not an abnormality. | Malfunction of the valve body |

**Flowchart:**
1. Do standard shifting occur normally?
   - Yes → It is related to adaptive logic control and is not an abnormality.
   - No → Does the problem occur only when the automatic transaxle fluid temperature is -29°C or lower or 125°C or higher?
     - Yes → It is related to adaptive logic control and is not an abnormality.
     - No → Replace the transaxle

---

<!-- TR-60 -->
### Inspection Procedure 13

| No diagnostic trouble codes (Does not shift) | Possible cause |
|----------------------------------------------|---------------|
| If shifting does not occur while driving and no diagnostic trouble codes are given, the cause may be a malfunction of the Park/Neutral position switch, or TCM. | Malfunction of the Park/Neutral position switch · Malfunction of the TCM |

**Flowchart:**
1. Does the transaxle remain in 3rd gear with selector lever in position D?
   - NO → (end)
   - YES → Is backup power being supplied to the TCM?
     - NO → Is power being supplied to the TCM?
       - YES → TCM input signal and selector lever position should match.
       - NO → Power supply circuit check: Pay particular attention to an open circuit in the harness or poor connector. If there is a blown fuse, investigate why a short circuit has occurred and then replace the fuse.

---

<!-- TR-61 -->
### Inspection Procedure 14

| Poor acceleration | Possible cause |
|-------------------|---------------|
| If acceleration is poor even if downshifting occurs while driving, the cause may be a malfunction of the engine system or of a brake or clutch. | Malfunction of the engine system · Malfunction of the brake or clutch |

**Flowchart:**
1. Check for DTCs
   - PRESENT → Correct condition
   - NONE → Engine system check: Check the control system, ignition system, fuel system, and main system. → NG → Replace, repair
2. OK → Brake or clutch check: Check for burning of the facing, defective piston seal rings, and interference at the retainer.

---

<!-- TR-62 -->
### Inspection Procedure 15

| Vibration | Possible cause |
|-----------|---------------|
| If vibration occurs when driving at constant speed or when accelerating in top range, the cause may be abnormal torque converter clutch pressure or a malfunction of the engine system, torque converter, torque converter clutch solenoid, torque converter or valve body. | Abnormal torque converter clutch pressure · Malfunction of the engine system · Malfunction of the torque converter clutch solenoid · Malfunction of the torque converter · Malfunction of the valve body |

**Flowchart:**
1. Scan Tool Actuator Test: Torque converter clutch solenoid → OK: Sound of operation can be heard.
   - NG → Replace the torque converter clutch solenoid valve
2. OK → Does the problem occur even when the oil temperature sensor connector is disconnected?
   - Yes → Engine system check: Check the control system, ignition, fuel system, and main system
3. No → Hydraulic pressure test: Measure the torque converter clutch pressure
   - NG → Valve body disassembly, cleaning, and reassembly. Pay particular attention to the loosening of bolts, and to damage and slippage of O-rings, valves, and valve body. If the damage cannot be repaired, replace the valve body assembly.
4. OK → Replace the torque converter assembly

---

<!-- TR-63 -->
## Service Adjustment Procedures <!-- EKA90052 -->

### Brake Reaction Plate End Play Adjustment

Replace the pressure plate of the low-reverse brake with the special tool, and then install the brake disc, brake plate, and snap ring as shown in the figure. Install the reaction plate and the used snap ring. Move the special tool to measure the end play, and then replace the snap ring to adjust the end play to standard value.

**Standard value:** 0 - 0.16 mm

(Refer to the "Snap ring and spacer for adjustment")

<!-- figure: Reaction plate, snap ring, special tool 09456-39100 -->

### Second Brake End Play Adjustment

Replace the pressure plate of the second brake with the special tool, and then install the brake disc and brake plate as shown in the figure. Install the return spring, second brake piston, and snap ring.

**Standard value:** 0.79-1.25 mm

Select a pressure plate whose thickness is within the following value. {A (moving amount) + thickness of the special tool - 1.25} to {A (moving amount) + thickness of the special tool - 0.79}. (Refer to the "Snap ring and spacer for adjustment".)

<!-- figure: Second brake piston, snap ring, return spring, special tool 09456-39100 -->

### Low-Reverse Brake End Play Adjustment

Reverse the transmission and install a dial gauge. Move the special tool up and down to measure the end play.

**Standard value:** 1.35 - 1.81 mm

Select a pressure plate whose thickness is within the following value. {A (moving amount) + thickness of the special tool - 1.81} to {A (moving amount) + thickness of the special tool - 1.35}. (Refer to the "Snap ring and spacer for adjustment".)

<!-- figure: Special tool 09456-39100, dial gauge -->

---

<!-- TR-64 -->
### Identification of Thrust Bearing, Thrust Races, and Thrust Washers

<!-- figure: Cross-section of automatic transaxle showing thrust bearing/race locations #1 through #8 -->

| O.D. | I.D. | Thickness | Symbol | O.D. | I.D. | Thickness | Symbol |
|------|------|-----------|--------|------|------|-----------|--------|
| 59 | 47 | 1.8 | #1 | 48.9 | 37 | 1.6 | #8 |
| 59 | 47 | 2.0 | #1 | 48.9 | 37 | 1.7 | #8 |
| 59 | 47 | 2.2 | #1 | 48.9 | 37 | 1.8 | #8 |
| 59 | 47 | 2.4 | #1 | 48.9 | 37 | 1.9 | #8 |
| 59 | 47 | 2.6 | #1 | 48.9 | 37 | 2.0 | #8 |
| 59 | 47 | 2.8 | #1 | 48.9 | 37 | 2.1 | #8 |
| 49 | 36 | 3.6 | #2 | 48.9 | 37 | 2.2 | #8 |
| 49 | 36 | 3.6 | #3 | 48.9 | 37 | 2.3 | #8 |
| 42.3 | 31 | 3.3 | #4 | 48.9 | 37 | 2.4 | #8 |
| 49 | 36 | 3.6 | #5 | 48.9 | 37 | 2.5 | #8 |
| 49 | 36 | 3.6 | #6 | 48.9 | 37 | 2.6 | #8 |
| 59 | 37 | 2.8 | #7 | - | - | - | - |

---

<!-- TR-65 -->
### Underdrive Sun Gear End Play Adjustment

Install the used thrust race #8, and then the rear cover. Measure the underdrive sun gear end play. Replace thrust race #8 to adjust the play to the standard value.

**Standard value:** 0.25 - 0.45 mm

> **NOTE**
> *Installing the underdrive clutch hub makes it easy to measure the underdrive sun gear end play.*

<!-- figure: Underdrive sun gear, underdrive clutch hub -->

### Differential Case Preload Adjustment

Place a piece of solder (approx. 10 mm in length, 3 mm in diameter) on the torque converter housing as shown in the figure. Install the torque converter housing to the transmission case without applying sealant. Tighten its mounting bolts to the specified torque. Loosen the bolts, and remove the solder. Use a micrometer to measure the thickness (T) of the pressed solder. Select a spacer with a thickness that is within the following value.

**Standard value:** (T+0.045 mm) to (T+0.105 mm)

<!-- figure: Solder placement on torque converter housing -->

---

<!-- TR-66 -->
## Automatic Transaxle Hydraulic Circuit <!-- EKA90115 -->

### Park & Neutral

<!-- figure: Hydraulic circuit diagram for Park & Neutral position showing line pressure, pump suction pressure, and torque converter and lubrication pressure paths -->

**Legend:**
- Solid black = LINE PRESSURE
- Cross-hatched = PUMP SUCTION PRESSURE
- Diagonal lines = TORQUE CONVERTER AND LUBRICATION PRESSURE

---

<!-- TR-67 -->
### First

<!-- figure: Hydraulic circuit diagram for First gear showing line pressure, pump suction pressure, and torque converter and lubrication pressure paths -->

---

<!-- TR-68 -->
### Second

<!-- figure: Hydraulic circuit diagram for Second gear showing line pressure, pump suction pressure, and torque converter and lubrication pressure paths -->

---

<!-- TR-69 -->
### Third

<!-- figure: Hydraulic circuit diagram for Third gear showing line pressure, pump suction pressure, and torque converter and lubrication pressure paths -->

---

<!-- TR-70 -->
### Fourth

<!-- figure: Hydraulic circuit diagram for Fourth gear showing line pressure, pump suction pressure, and torque converter and lubrication pressure paths -->

---

<!-- TR-71 -->
### Reverse

<!-- figure: Hydraulic circuit diagram for Reverse gear showing line pressure, pump suction pressure, and torque converter and lubrication pressure paths -->

---

<!-- TR-72 -->
## TCM Circuit Diagram (2.0L) <!-- EKC60400 -->

<!-- figure: TCM wiring diagram for 2.0L engine showing:
- BCM-IM fuse 8 (10A) power supply via MC91 (0.5R)
- Transaxle range switch (C01) with contact point connections: R input, P input, N input, Select, Up shift, Down shift
- Sport mode switch (C39) connections
- See Starting System reference
- See Indicators & Gauges reference
- See Illuminations reference
- TCM connector C36-3 -->

---

<!-- TR-73 -->
<!-- figure: TCM wiring diagram continuation for 2.0L showing:
- ECU fuse 14 (10A) and ECU fuse 13A via E08, E26 and joint connector
- Instrument cluster (M10-0) connections
- Cruise Control System reference
- Stop Lamps reference
- A/T Pulse Generators via C06-1, C06-2
- TCM connections to C36-0, C36-1, C36-2, C36-3
- Communication error network, data link, K-Line connections
- Multi gauge unit, ABS control module connections
- Data link connector (M67), multipurpose check connector (G16) -->

---

<!-- TR-74 -->
<!-- figure: TCM wiring diagram continuation for 2.0L showing:
- ECU fusible link (80A), ECU fuse 13A via E08
- A/T control relay (C37) connections
- Joint connector (C45, C46) connections
- Stop Lamps reference
- A/T Pulse Generator #1 (C06-1), A/T Pulse Generator #2 (C06-2)
- Solenoid valve control connections: LR, DCC, OD, 2ND, UD, OT
- Oil temp sensor (C04) and ATM idle solenoid valve
- Battery voltage, relay switch, generator #1 (input speed), ground, generator #2 (output speed) connections to TCM -->

---

<!-- TR-75 -->
## TCM Circuit Diagram (2.7L) <!-- ENCC0600 -->

<!-- figure: TCM wiring diagram for 2.7L engine showing:
- BCM-IM fuse 8 (10A) power supply via MC101 (0.5R), MC103
- Transaxle range switch (C101) with contact point connections: R input, P input, N input, Select, Up shift, Down shift
- Sport mode switch (C136) connections
- See Starting System reference
- See Illuminations reference
- TCM connector C136-3 -->

---

<!-- TR-76 -->
<!-- figure: TCM wiring diagram continuation for 2.7L showing:
- Joint connector (C141) connections
- Instrument cluster (M10-3) connections
- Stop Lamps reference
- Cruise Control System reference
- A/T Pulse Generator via C136-1, C136-3
- Communication error network, constant input, K-Line connections
- TCM connections: Low voltage / High voltage, power for switch input, ground
- Multi gauge unit, ABS control module connections via EC102
- BCM-IM connections
- Data link connector (M99), multipurpose check connector (G21) -->

---

<!-- TR-77 -->
<!-- figure: TCM wiring diagram continuation for 2.7L showing:
- ECU fusible link (100A), ECU fuse 13A via E08
- A/T control relay (C137) connections
- Joint connector (C142, G21) connections
- Stop Lamps reference
- A/T Pulse Generator #1 (C102-1), A/T Pulse Generator #2 (C102-2)
- Solenoid valve control connections: LR, DCC, OD, 2ND, UD, OT via C136-3, C136-1, C136-2
- Oil temp sensor (C104) and ATM idle solenoid valve
- Battery voltage, relay switch, generator #1 (input speed), ground, generator #2 (output speed) connections to TCM -->

---

<!-- TR-78 -->
## Automatic Transaxle

### Removal <!-- EKC0030 -->

1. Remove the engine cover.
2. Remove the battery terminal.
3. Remove the air duct.
4. Remove the battery tray.
5. Remove the air cleaner.
   a. Upper
   b. Lower
6. After removing the CKP sensor, O2 sensor and oil pressure switch wiring bracket, separate the connectors.
7. Remove the speedometer sensor connector.

<!-- figure: Steps 1-7 removal illustrations -->

---

<!-- TR-79 -->

8. Remove the transaxle range switch.
9. Remove the oil cooler hose.
10. Remove the clip (transaxle side) of the shift cable.
11. Separate the steering column shaft joint.
12. Separate the power steering oil pump hose.

> **NOTE**
> *Be careful not to leak after separating.*

13. Separate the hose after removing the clip of the power steering return hose.
14. Remove the upper connecting transaxle bolt.

<!-- figure: Steps 8-14 removal illustrations -->

---

<!-- TR-80 -->

15. Separate the start motor.
16. Install the engine support fixture. (Special tool: 09200-38001)
17. After removing the tire, remove the caliper.
18. Remove the transaxle side cover.
19. Remove the transaxle under cover.
20. Separate the tie rod end.
21. Remove the wheel speed sensor and the knuckle mounting bolt.
22. Drain the oil.
23. Remove the transaxle mounting bracket.
    a. Insulator bolt

<!-- figure: Steps 15-23 removal illustrations -->

---

<!-- TR-81 -->

    b. Body mounting bolt (Upper)
    c. Body mounting bolt (Side)
    d. Transaxle side mounting bolt.
    b. Stopper bolt (Upper)
    c. Stopper bolt (Lower)

24. Remove the front roll stopper.
    a. Insulator bolt

25. Remove the rear roll stopper.
    a. Insulator bolt
    b. Stopper bolt

<!-- figure: Steps 23b-25 removal illustrations -->

---

<!-- TR-82 -->

26. Remove the drive shaft.
27. Remove the front muffler.
28. Remove the sub frame mounting bolt.
29. Install the jack under the transaxle assembly.
30. Remove the transaxle lower mounting bolt to the engine.
31. Remove the transaxle assembly.

### Installation <!-- EKCC3080 -->

1. Attach the torque converter on the transaxle side and mount the transaxle assembly onto the engine.

> **CAUTION**
> *If the torque converter is mounted first on the engine, the oil seal on the transaxle may be damaged. Therefore, first be sure to assemble the torque converter to the transaxle.*

2. Install the transaxle control cable and adjust as follows:
   a. Move the shift lever and the transaxle range switch to the "N" position and install the control cable.
   b. When connecting the control cable to the transaxle mounting bracket, install the clip until it contacts to the control cable.
   c. Remove any free-play in the control cable by adjusting the nut and then check to see that the selector lever moves smoothly.
   d. Check to see that the control cable has been adjusted correctly.

<!-- figure: Steps 26-31 removal illustrations and installation illustration -->

---

<!-- TR-83 -->
## Components <!-- EKA90040 -->

### F4A42

<!-- figure: Cross-section diagram of F4A42 automatic transaxle showing:
- Rear cover
- Overdrive clutch (OD)
- Second brake (2ND)
- Reverse clutch (REV)
- Low-reverse brake (LR)
- One way clutch (OWC)
- Underdrive clutch (UD)
- Damper clutch
- Torque converter
- Oil pump
- Output shaft
- Transfer drive gear
- Differential -->

---

<!-- TR-84 -->
## Automatic Transaxle Shift Control

### Components <!-- EKC60050 -->

<!-- figure: Exploded view of shift control components showing:
- Shift lock cable
- Control cable
- Key lock cable
- Shift lever
- Control cable to transaxle

Torque values:
- 9-11 Nm (90-110, 7-8) — shift lock cable bracket
- 9-14 Nm (90-140, 7-10) — key lock cable bracket
- 10-14 Nm (100-140, 7-10) — transaxle side (for 2.7 DOHC)
- 9-14 Nm (90-140, 7-10) — control cable at transaxle (for 2.0 DOHC)
- 4-9 Nm (40-90, 3-7) — shift lock cable at shift lever

TORQUE: Nm (kg.cm, lb.ft) -->

---

<!-- TR-85 -->
### Removal <!-- EKC60190 -->

1. Remove the push button, the spring and the cap.
2. Remove the knob mounting nut.
3. Remove the shift knob.
4. Remove the console upper cover.
5. Remove the console assembly.
6. Remove the indicator panel.
7. Remove the indicator lower cover.
8. Remove the indicator plate.
9. Remove the key lock cable nut.

<!-- figure: Steps 1-9 removal illustrations -->

---

<!-- TR-86 -->

10. Remove the shift lock cable nut.
11. Remove the control cable snap pin.
12. Remove the control cable clip and the control cable.
13. Remove the shift lever bracket bolt.
14. Remove the shift lever.

### Installation <!-- ENCC0800 -->

#### Procedure to Install the Lock Cam

1. Move A/T lever to "P" position to set the key lock cam and the shift lock cam as shown in the figure.
   a. Check that the key lock cam is located at "B" by the detent pin.
   b. Check that the shift lock cam is located at "A".

<!-- figure: Steps 10-14 removal illustrations and lock cam installation diagram -->

---

<!-- TR-87 -->

<!-- figure: Key lock cam, shift lock cam, detent pin installation detail -->

2. Check that the key cylinder is at "LOCK".

### Procedure for Adjusting Shift Lock and Key Lock Cable

1. Check that each lock cam is as shown in the figure.
2. Install the shift lock and key lock cable in position. In this case, the shift lock cable must be fixed to the brake pedal and the key lock cable must be fixed to the key cylinder.
3. Temporarily install each cable to the A/T lever assembly as shown in the figure. Securely insert the cable end into the fixing pin of each cam.

<!-- figure: Key lock cam, spring, washer, shift lock cable assembly -->

4. Slightly pull the shift lock cable in the direction "E".
5. After checking that the portion of the cable end touches the cable fixing pin, fix with the self-tapping bolt.
6. Slightly push the key lock cam to direction "Q".
7. Slightly pull the key lock cable in the direction "G" to stretch the cable. Then fix the cable with the self-tapping bolt.
8. Check that the key lock and the shift lock cable are secure.

### Procedure for Checking the Shift Lock

1. When the brake pedal is not depressed, the push button of the shift lever at "P" position must not be operable. (Shift lever cannot be shifted at the other positions from "P".)
2. When the brake pedal stroke is 15-20mm (with shift lever at "P" position), the push button should be operable without catching and the shift lever should shift smoothly to other positions.
3. When the brake pedal is not depressed, the shift lever should shift smoothly to "P" position from all heading other positions.
4. The brake pedal must operate smoothly without catching.
5. When the ignition key is at the "LOCK" position, although brake pedal is depressed, the push button should be operable.
6. The ignition key must not be able to be turned to the "LOCK" position except in the "P" position.
7. If the shift lever is shifted to the "P" position, the ignition key must turn to the "LOCK" position smoothly.
