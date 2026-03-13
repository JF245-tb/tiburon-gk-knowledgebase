---
source: FLA.pdf
chapter: FLA
section: FLA-73 to FLA-120
pages: 73-120
engine: V6
title: DTC Troubleshooting
---

# Troubleshooting for DTCs (Siemens EMS)

<!-- EFOC0010 -->

## Diagnostic Item Overview

| DTC | Diagnostic Item |
|-----|----------------|
| P0031 | HO2S Heater Circuit Low (Bank 1, Sensor 1) |
| P0032 | HO2S Heater Circuit High (Bank 1, Sensor 1) |
| P0037 | HO2S Heater Circuit Low (Bank 1, Sensor 2) |
| P0038 | HO2S Heater Circuit High (Bank 1, Sensor 2) |
| P0051 | HO2S Heater Circuit Low (Bank 2, Sensor 1) |
| P0052 | HO2S Heater Circuit High (Bank 2, Sensor 1) |
| P0057 | HO2S Heater Circuit Low (Bank 2, Sensor 2) |
| P0058 | HO2S Heater Circuit High (Bank 2, Sensor 2) |
| P0101 | Mass Air Flow Circuit Range/Performance Problem |
| P0102 | Mass Air Flow Circuit Low Voltage |
| P0103 | Mass Air Flow Circuit High Voltage |
| P0112 | Intake Air Temperature Circuit Low Input |
| P0113 | Intake Air Temperature Circuit High Input |
| P0116 | Engine Coolant Temperature Circuit Range/Performance Problem |
| P0117 | Engine Coolant Temperature Circuit Low Input |
| P0118 | Engine Coolant Temperature Circuit High Input |
| P0121 | Throttle Position Sensor Circuit Range/Performance Problem |
| P0122 | Throttle Position Sensor Circuit Low Input |
| P0123 | Throttle Position Sensor Circuit High Input |
| P0131 | HO2S Circuit Low Input (Bank 1, Sensor 1) |
| P0132 | HO2S Circuit High Input (Bank 1, Sensor 1) |
| P0137 | HO2S Circuit Low Input (Bank 1, Sensor 2) |
| P0138 | HO2S Circuit High Input (Bank 1, Sensor 2) |
| P0151 | HO2S Circuit Low Input (Bank 2, Sensor 1) |
| P0152 | HO2S Circuit High Input (Bank 2, Sensor 1) |
| P0157 | HO2S Circuit Low Input (Bank 2, Sensor 2) |
| P0158 | HO2S Circuit High Input (Bank 2, Sensor 2) |
| P0133 | HO2S Circuit Slow Responsive (Bank 1, Sensor 1) |
| P0153 | HO2S Circuit Slow Responsive (Bank 2, Sensor 1) |
| P0171 | Fuel System Too Lean (Bank 1) |
| P0172 | Fuel System Too Rich (Bank 1) |
| P0174 | Fuel System Too Lean (Bank 2) |
| P0175 | Fuel System Too Rich (Bank 2) |
| P0230 | Fuel Pump Circuit Malfunction |
| P0261 | Cylinder 1 Injector Circuit Low Input |
| P0264 | Cylinder 2 Injector Circuit Low Input |
| P0267 | Cylinder 3 Injector Circuit Low Input |
| P0270 | Cylinder 4 Injector Circuit Low Input |
| P0273 | Cylinder 5 Injector Circuit Low Input |
| P0276 | Cylinder 6 Injector Circuit Low Input |
| P0262 | Cylinder 1 Injector Circuit High Input |
| P0265 | Cylinder 2 Injector Circuit High Input |
| P0268 | Cylinder 3 Injector Circuit High Input |
| P0271 | Cylinder 4 Injector Circuit High Input |
| P0274 | Cylinder 5 Injector Circuit High Input |
| P0277 | Cylinder 6 Injector Circuit High Input |
| P0300 | Random Misfire Detected |
| P0301 | Cylinder 1 Misfire Detected |
| P0302 | Cylinder 2 Misfire Detected |
| P0303 | Cylinder 3 Misfire Detected |
| P0304 | Cylinder 4 Misfire Detected |
| P0305 | Cylinder 5 Misfire Detected |
| P0306 | Cylinder 6 Misfire Detected |
| P0325 | Knock Sensor Circuit Malfunction (Bank 1) |
| P0330 | Knock Sensor Circuit Malfunction (Bank 2) |
| P0335 | Crankshaft Position Sensor Circuit Malfunction |
| P0340 | Camshaft Position Sensor Circuit Malfunction |
| P0350 | Ignition Coil Primary/Secondary Circuit Malfunction |
| P0351 | Ignition Coil "#1" Primary/Secondary Circuit Malfunction |
| P0352 | Ignition Coil "#2" Primary/Secondary Circuit Malfunction |
| P0353 | Ignition Coil "#3" Primary/Secondary Circuit Malfunction |
| P0354 | Ignition Coil "#4" Primary/Secondary Circuit Malfunction |
| P0355 | Ignition Coil "#5" Primary/Secondary Circuit Malfunction |
| P0356 | Ignition Coil "#6" Primary/Secondary Circuit Malfunction |
| P0420 | Main Catalyst Efficiency Deterioration (Bank 1) |
| P0430 | Main Catalyst Efficiency Deterioration (Bank 2) |
| P0444 | EVAP Emission Control System Purge Control Valve Circuit Open |
| P0445 | EVAP Emission Control System Purge Control Valve Circuit Shorted |
| P0501 | Vehicle Speed Sensor Circuit Range/Performance |
| P0506 | Idle Control System RPM Lower Than Expected |
| P0507 | Idle Control System RPM Higher Than Expected |
| P0560 | System Voltage Malfunction |
| P0650 | Malfunction Indication Lamp (MIL) Control Circuit Malfunction |
| P1134 | HO2S Circuit Transition Switch Malfunction/Slip (Bank 1, Sensor 1) |
| P1154 | HO2S Circuit Transition Switch Malfunction/Slip (Bank 2, Sensor 1) |
| P1166 | Lambda Bank Control Limit (Bank 1) |
| P1167 | Lambda Bank Control Limit (Bank 2) |
| P1372 | Segment Time Acquisition Incorrect |
| P1505 | Idle Charge Actuator Signal Low (Coil 1) |
| P1506 | Idle Charge Actuator Signal High (Coil 1) |
| P1507 | Idle Charge Actuator Signal Low (Coil 2) |
| P1508 | Idle Charge Actuator Signal High (Coil 2) |
| P1521 | Power Steering Switch Malfunction |
| P1602 | Serial Communication Problem With TCU (time-out) |
| P1624 | Cooling Fan Relay Circuit Malfunction (Low) |
| P1625 | Cooling Fan Relay Circuit Malfunction (High) |

---

## DTC P0031 / P0032 / P0037 / P0038 / P0051 / P0052 / P0057 / P0058

<!-- EFOC0610 -->

**HO2S Heater Circuit Low/High (All Banks, All Sensors)**

| DTC | Diagnostic Item |
|-----|----------------|
| P0031 | HO2S Heater Circuit Low (Bank 1, Sensor 1) |
| P0032 | HO2S Heater Circuit High (Bank 1, Sensor 1) |
| P0037 | HO2S Heater Circuit Low (Bank 1, Sensor 2) |
| P0038 | HO2S Heater Circuit High (Bank 1, Sensor 2) |
| P0051 | HO2S Heater Circuit Low (Bank 2, Sensor 1) |
| P0052 | HO2S Heater Circuit High (Bank 2, Sensor 1) |
| P0057 | HO2S Heater Circuit Low (Bank 2, Sensor 2) |
| P0058 | HO2S Heater Circuit High (Bank 2, Sensor 2) |

### Test Procedure

<!-- Figure: HO2S Heater Circuit flowchart, source: FLA.pdf pages 73-74 -->

**Step 1:** Turn ignition OFF and disconnect HO2S connector. Start engine and allow engine to idle until ECT reaches operating temperature. Measure voltage between HO2S terminal 4 and ground (B+). Is measured voltage within specification?
- YES → Go to Step 2
- NO → Open or short between main relay and HO2S terminal 4. Repair as necessary.

**Step 2:** With ignition ON and engine OFF, measure voltage between HO2S terminal 3 and ground (B+). Is voltage within specification?
- YES → Go to Step 4
- NO → Go to Step 3

**Step 3:** Measure resistance between HO2S terminal 3 and ground (< 1Ω). Is measured resistance within specification?
- YES → Short to battery between HO2S terminal 3 and ECM. Repair as necessary.
- NO → Go to Step 4a

**Step 4a:** Disconnect ECM connector and measure resistance between HO2S terminal 3 and ECM (< 1Ω). Is measured resistance within specification?
- YES → Go to Step 5
- NO → Repair wire harness between HO2S terminal 3 and ECM, confirm repair and road test vehicle.

**Step 5:** Measure resistance between HO2S heater terminal 3 and terminal 4. Specification: 3.9–5.2Ω at 25°C (68°F). Is measured resistance within specification?
- YES → Temporarily install a known good ECM and check for proper operation. If problem is corrected, replace ECM.
- NO → Temporarily install a known good HO2S and check for proper operation. If problem is corrected, replace HO2S.

**Final:** Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P0101 / P0102 / P0103

<!-- EFOC0020 -->

**Mass Air Flow Circuit Range/Performance / Low Voltage / High Voltage**

| DTC | Diagnostic Item |
|-----|----------------|
| P0101 | Mass Air Flow Circuit Range/Performance Problem |
| P0102 | Mass Air Flow Circuit Low Voltage |
| P0103 | Mass Air Flow Circuit High Voltage |

### Test Procedure

<!-- Figure: MAFS circuit flowchart, source: FLA.pdf pages 75-76 -->

**Step 1:** Start engine and allow engine to idle until engine reaches operating temperature. Measure voltage between MAFS terminal 2 and ground. Is voltage within specification (0.2–0.8V)?
- YES → Go to Step 6
- NO → Go to Step 2

**Step 2:** Turn ignition switch to OFF and disconnect MAFS connector. Turn ignition switch to ON and measure voltage between MAFS harness terminal 1 and ground. Is voltage within specification (B+)?
- YES → Go to Step 3
- NO → Open or short to ground between MAFS and main relay. Repair wire as necessary.

**Step 3:** Measure voltage between MAFS harness terminal 1 and terminal 3. Is voltage within specification (B+)?
- YES → Go to Step 4
- NO → Open between MAFS and ECM terminal M17. Repair wire or connector as necessary.

**Step 4:** Turn ignition switch to OFF and connect MAFS connector. Measure voltage between MAFS terminal 1 and ground. Is voltage within specification (B+)?
- YES → Go to Step 5
- NO → Open or short to ground between MAFS and main relay. Repair wire or connector as necessary.

**Step 5:** Turn ignition switch OFF and connect MAFS connector. Turn ignition switch ON and measure voltage between ECM terminal M1 and ground. Is voltage within specification (B+)?
- YES → Go to Step 6
- NO → Open or short to ground between MAFS and ECM terminal M1. Repair wire or connector as necessary.

**Step 6:** Check for wire connection at MAFS. Is a poor connection found?
- YES → Repair connection as necessary.
- NO → Temporarily install a known good MAFS and check for proper operation. If problem is corrected, replace MAFS.

**Final:** Return vehicle to original condition. Clear all Diagnostic Trouble Codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P0112 / P0113

<!-- EFOC0001 -->

**Intake Air Temperature Circuit Low/High Input**

| DTC | Diagnostic Item |
|-----|----------------|
| P0112 | Intake Air Temperature Circuit Low Input |
| P0113 | Intake Air Temperature Circuit High Input |

### Test Procedure

<!-- Figure: IATS circuit flowchart, source: FLA.pdf page 77 -->

**Step 1:** Turn ignition OFF and disconnect IATS connector. Turn ignition ON, measure voltage between IATS signal terminal 2 (to ECM) and ground (5V). Is voltage within specification?
- YES → Go to Step 2
- NO → Open or short between IATS signal terminal 2 and ECM. Repair as necessary.

**Step 2:** Turn ignition OFF and measure resistance between IATS ground terminal 1 and ECM (< 1Ω). Is resistance within specification?
- YES → Go to Step 3
- NO → Open or short between IATS ground terminal 1 and ECM. Repair as necessary.

**Step 3:** Measure resistance between IATS ground terminal 1 and signal terminal 2.
- 2.22–2.82 KΩ at 20°C (68°F)
- 0.29–0.36 KΩ at 80°C (176°F)

Is resistance within specification?
- YES → Poor terminal contact due to oxidation, bent or misplaced terminal. Repair as necessary.
- NO → Temporarily install a known good IATS and check for proper operation. If problem is corrected, replace IATS.

**Final:** Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P0116

<!-- EFOC0040 -->

**Engine Coolant Temperature Circuit Range/Performance Problem**

| DTC | Diagnostic Item |
|-----|----------------|
| P0116 | Engine Coolant Temperature Circuit Range/Performance Problem |

### Test Procedure

<!-- Figure: ECTS circuit flowchart, source: FLA.pdf page 78 -->

**Step 1:** Turn ignition OFF and disconnect ECTS connector. Turn ignition ON, measure voltage between ECTS signal terminal 3 (to ECM) and ground (5V). Is voltage within specification?
- YES → Go to Step 2
- NO → Open or short between ECTS signal terminal 3 and ECM. Repair as necessary.

**Step 2:** Turn ignition OFF and measure resistance between ECTS ground terminal 1 (to ECM) and ECM (< 1Ω). Is resistance within specification?
- YES → Go to Step 3
- NO → Open between ECTS ground terminal 1 and ECM. Repair as necessary.

**Step 3:** Measure resistance between ECTS ground terminal 1 and signal terminal 2.
- 2.31–2.59 KΩ at 20°C (68°F)
- 0.31–0.33 KΩ at 80°C (176°F)

Is resistance within specification?
- YES → Go to Step 4
- NO → Temporarily install a known good ECTS and check for proper operation. If problem is corrected, replace ECTS.

**Step 4:** Check ECTS for contamination, deterioration or damage. Is ECTS contaminated, deteriorated or damaged?
- YES → Clean ECTS with cleaner before installing. If damaged or deteriorated, replace ECTS.
- NO → Go to Step 5

**Step 5:** Thoroughly check for loose, bent or corroded connectors at ECM and ECTS connectors. With ignition OFF, disconnect ECM and ECTS connectors. Measure resistance between ECTS and ECM on both circuits. Is resistance all below 1 ohm?
- YES → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Repair as necessary.

---

## DTC P0117 / P0118

<!-- EFOC0030 -->

**Engine Coolant Temperature Circuit Low/High Input**

| DTC | Diagnostic Item |
|-----|----------------|
| P0117 | Engine Coolant Temperature Circuit Low Input |
| P0118 | Engine Coolant Temperature Circuit High Input |

### Test Procedure

<!-- Figure: ECTS Low/High circuit flowchart, source: FLA.pdf page 79 -->

**Step 1:** Turn ignition OFF and disconnect ECTS connector. Turn ignition ON, measure voltage between ECTS signal terminal 3 (to ECM) and ground (5V). Is voltage within specification?
- YES → Go to Step 2
- NO → Open or short between ECTS signal terminal 3 and ECM. Repair as necessary.

**Step 2:** Turn ignition OFF and measure resistance between ECTS ground terminal 1 and ECM (< 1Ω). Is resistance within specification?
- YES → Go to Step 3
- NO → Open or short between ECTS ground terminal 1 and ECM. Repair as necessary.

**Step 3:** Measure resistance between ECTS ground terminal 1 and signal terminal 3.
- 2.31–2.59 KΩ at 20°C (68°F)
- 0.31–0.33 KΩ at 80°C (176°F)

Is resistance within specification?
- YES → Poor terminal contact due to oxidation, bent or misplaced terminal. Repair as necessary.
- NO → Temporarily install a known good ECTS and check for proper operation. If problem is corrected, replace ECTS.

**Final:** Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P0121 / P0122 / P0123

<!-- EFOC0050 -->

**Throttle Position Sensor Circuit Range/Performance / Low Input / High Input**

| DTC | Diagnostic Item |
|-----|----------------|
| P0121 | Throttle Position Sensor Circuit Range/Performance Problem |
| P0122 | Throttle Position Sensor Circuit Low Input |
| P0123 | Throttle Position Sensor Circuit High Input |

### Test Procedure

<!-- Figure: TPS circuit flowchart, source: FLA.pdf pages 80-81 -->

**Step 1:** Turn ignition OFF and disconnect TPS connector. Turn ignition ON and measure voltage between TPS reference terminal 3 and ground (5V). Is voltage within specifications?
- YES → Go to Step 2
- NO → Open or short between TPS terminal 3 and ECM. Repair as necessary.

**Step 2:** Turn ignition OFF and measure resistance between TPS terminal 2 and ground (< 1Ω). Is resistance within specification?
- YES → Go to Step 3
- NO → Open between TPS terminal 2 and ECM. Repair as necessary.

**Step 3:** Reconnect TPS connector and turn ignition ON. Measure voltage between TPS signal terminal 1 and ground with throttle closed (0.2–0.8V). Is voltage within specification?
- YES → Go to Step 4
- NO → Open or short between TPS signal terminal 1 and ECM. Repair as necessary.

**Step 4:** Press accelerator pedal fully and measure voltage between TPS signal terminal 1 and ground (4.0–4.8V). Is voltage within specification?
- YES → Temporarily install a known good TPS and check for proper operation. If problem is corrected, replace TPS.
- NO → Go to Step 5

**Step 5:** Poor terminal contact due to oxidation, bent or misplaced terminal. Repair as necessary. Then go to Step 6.

**Step 6:** Check TPS for contamination, deterioration or damage. Is TPS contaminated, deteriorated or damaged?
- YES → Clean TPS with cleaner before installing. If damaged or deteriorated, replace.
- NO → Go to Step 7

**Step 7:** Thoroughly check for loose, bent or corroded connectors at ECM and TPS connectors. With ignition OFF, disconnect TPS connector. Measure resistance between TPS terminals 2 (ground) and 3 (signal):
- 0.71–1.38 KΩ at wide open throttle
- 2.2–3.4 KΩ at wide open throttle

Measure resistance between TPS terminals (power supply) and 2 (ground):
- 1.6–2.4 KΩ at all throttle positions

Is resistance all below 1 ohm?
- YES → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Repair as necessary.

---

## DTC P0131 / P0132 / P0137 / P0138 / P0151 / P0152 / P0157 / P0158

<!-- EFOC0070 -->

**HO2S Circuit Low/High Input (All Banks, All Sensors)**

| DTC | Diagnostic Item |
|-----|----------------|
| P0131 | HO2S Circuit Low Input (Bank 1, Sensor 1) |
| P0132 | HO2S Circuit High Input (Bank 1, Sensor 1) |
| P0137 | HO2S Circuit Low Input (Bank 1, Sensor 2) |
| P0138 | HO2S Circuit High Input (Bank 1, Sensor 2) |
| P0151 | HO2S Circuit Low Input (Bank 2, Sensor 1) |
| P0152 | HO2S Circuit High Input (Bank 2, Sensor 1) |
| P0157 | HO2S Circuit Low Input (Bank 2, Sensor 2) |
| P0158 | HO2S Circuit High Input (Bank 2, Sensor 2) |

### Test Procedure

<!-- Figure: HO2S Signal Circuit flowchart, source: FLA.pdf pages 82-83 -->

**Step 1:** Turn ignition OFF and disconnect HO2S connector. Measure resistance between HO2S terminal 1 and terminal 2. Is measured resistance infinite?
- YES → Go to Step 2
- NO → Short between ECM and HO2S terminal 1 or and terminal 2. Repair as necessary.

**Step 2:** Measure resistance between HO2S heater terminal 3 and terminal 4. Specification: 3.9–5.2 W at 20°C (68°F). Is measured resistance within specification?
- YES → Go to Step 3
- NO → Temporarily install a known good HO2S and check for proper operation. If problem is corrected, replace HO2S.

**Step 3:** Reconnect HO2S connector, start engine and allow engine to idle until ECT reaches operating temperature. Measure voltage between HO2S terminal 4 and ground (B+). Is voltage within specification?
- YES → Go to Step 4
- NO → Open or short between HO2S terminal 4 and main relay. Repair as necessary.

**Step 4:** Measure resistance between HO2S terminal 3 and ECM (< 1Ω). Is resistance within specification?
- YES → Go to Step 5
- NO → Open between HO2S terminal 3 and ECM. Repair as necessary.

**Step 5:** Warm up engine to normal operating temperature for more than 10 minutes. Using SCAN TOOL monitor HO2S signal. Does the HO2S signal switch lean to rich or rich to lean over 3 times for 10 seconds?
- YES → Go to Step 6
- NO → Temporarily install a known good HO2S and check for proper operation. If problem is corrected, replace HO2S.

**Step 6:** Check HO2S for contamination, deterioration or damage. Is HO2S contaminated, deteriorated or damaged?
- YES → Clean HO2S with cleaner before installing. If damaged or deteriorated, replace.
- NO → Go to Step 7

**Step 7:** Thoroughly check for loose, bent or corroded connectors at ECM and HO2S connectors. Are connectors normal?
- YES → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Repair as necessary.

---

## DTC P0133 / P0153

<!-- EFOC0080 -->

**HO2S Circuit Slow Responsive (Bank 1/Bank 2, Sensor 1)**

| DTC | Diagnostic Item |
|-----|----------------|
| P0133 | HO2S Circuit Slow Responsive (Bank 1, Sensor 1) |
| P0153 | HO2S Circuit Slow Responsive (Bank 2, Sensor 1) |

### Test Procedure

<!-- Figure: HO2S Slow Response flowchart, source: FLA.pdf pages 84-85 -->

**Step 1:** First check for DTC relating to misfire, purge system, and front HO2S heater. Do DTCs exist?
- YES → Repair all other malfunctions on DTCs.
- NO → Go to Step 2

**Step 2:** Visually check for leak from exhaust system (especially between TWC converter and front exhaust pipe). Are any leaks present?
- YES → Repair exhaust system leaks as necessary.
- NO → Go to Step 3

**Step 3:** Visually check for leak from intake system. Are any vacuum leaks present?
- YES → Repair intake system leaks as necessary.
- NO → Go to Step 4

**Step 4:** Start engine after installing fuel pressure gauge at service valve in fuel rail. With engine running at operating temperature, is fuel pressure within specification? Fuel pressure at idle: 46–49 psi (320–340kPa, 3.26–3.47kg/cm²)
- YES → Go to Step 5 (Path B)
- NO → Go to Step 5a (Path A)

**Step 5a (Path A — pressure out of spec, too high):** If measured pressure is too high: Disconnect return line hose from fuel filter. Blow through line towards tank. Is return line restricted?
- YES → Check for blockage in return line, clean or replace as necessary.
- NO → Repair pressure regulator.

**Step 5b (Path A — pressure out of spec, too low):** If measured pressure is too low: Clamp a return line from fuel filter and check if pressure rises. Does fuel pressure rise?
- YES → Replace fuel delivery module.
- NO → Check fuel filter at fuel pump. If it is OK, measure fuel pump maximum pressure and repair as necessary.

**Step 5 (Path B — pressure OK):** Temporarily install a known good HO2S and check for proper operation. If problem is corrected, replace HO2S.

**Final:** Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P0171 / P0172 / P0174 / P0175

<!-- EFOC0110 -->

**Fuel System Too Lean/Rich (Bank 1/Bank 2)**

| DTC | Diagnostic Item |
|-----|----------------|
| P0171 | Fuel System Too Lean (Bank 1) |
| P0172 | Fuel System Too Rich (Bank 1) |
| P0174 | Fuel System Too Lean (Bank 2) |
| P0175 | Fuel System Too Rich (Bank 2) |

### Test Procedure

<!-- Figure: Fuel System Lean/Rich flowchart, source: FLA.pdf pages 86-88 -->

**Step 1:** Using SCAN TOOL, check for stored DTCs. Are any DTCs stored in ECM memory?
- YES → First repair all other malfunctions related to others.
- NO → Go to Step 2

**Step 2:** Check for air leaks and for loose hose and/or duct between air cleaner and throttle body.
- YES → Go to Step 3
- NO → Rectify as necessary.

**Step 3:** Check for correct vacuum hose connections to engine dynamic chamber (especially PSV, ISC hose, and brake booster). Are connections OK?
- YES → Go to Step 4
- NO → Rectify as necessary.

**Step 4:** With engine idling, disconnect hose between EVAP valve and canister. Check for vacuum at purge valve when EVAP valve is not operating. Is vacuum available at purge valve when EVAP valve is not operating?
- YES → EVAP canister purge valve or circuit failure. Repair according to DTC P0444/445 repair procedures.
- NO → Go to Step 5

**Step 5:** After installing fuel pressure gauge to service port on fuel rail, connect DLC F/P and B (B+) with a jumper wire. Is fuel line pressure correct with ignition switch ON? Fuel pressure at idle: 46–49 psi (320–340kPa, 3.26–3.47kg/cm²)
- YES → Go to Step 6
- NO → See pressure diagnosis below

**Step 6:** Back probe front HO2S output wire. Start engine and allow engine to warm up to operating temperature. In short spurts, spray aerosol carburetor cleaner in the following areas while looking for a long rise in voltage at front HO2S output terminal (a rise in voltage that is approximately as long as the spray of carburetor indicates some of the carburetor cleaner was drawn into the intake chamber richening the fuel mixture verifying a leak). Allow enough time between areas checked for carburetor spray to dissipate.

> **WARNING**
> **Do not spray carburetor cleaner on or near coils or plug wires. An arcing wire or coil could start a fire!**

Check the following areas for air leaks:
- Throttle body gasket
- Gasket between intake manifold and surge tank
- Seals between intake manifold and fuel injectors
- Deals between surge tank and PCV valves

Are air leaks indicated?
- YES → Repair as necessary.
- NO → Go to Step 7

**Step 6 (NO path — Low/High pressure):**

Low pressure:
- Clamp return line and check if pressure rises.
  - If pressure rises: replace pressure regulator.
  - If pressure does not rise: check the strainer at the fuel pump.

High pressure:
- Disconnect return line from fuel filter side and blow through line towards tank.
  - If line is clear: replace fuel delivery module.
  - If line is blocked, check for blockage in return line and clear or replace as necessary.
  - If it is OK, check fuel.

**Step 7:** Check for leaks from exhaust system (especially exhaust manifold catalyst around rear HO2S, etc.). Are leaks present in exhaust system?
- YES → Repair as necessary.
- NO → Go to Step 8

**Step 8:** Start engine and check for engine RPM decrease when disconnecting each injector connector in sequence. Measure the decreasing engine RPM of all 6 cylinders. Is there any cylinder with no change in RPM or only a small RPM change?
- YES → Repair as necessary.
- NO → Go to Step 9

**Step 9:** Inspect MAFS output signal between MAFS output terminal 2 and ground terminal 3 (0.2–0.8V at idling). Is output voltage within specifications?
- YES → Go to Step 10
- NO → Inspect according to MAFS diagnosis and repair.

**Step 10:** Remove spark plugs and inspect spark plug tips. Check for abnormal color of spark plug tips compared to other cylinders. Any spark plug with abnormal color compared to other cylinders?
- YES → Check for engine mechanical failure. If it is OK, replace spark plug.
- NO → Go to Step 11

**Step 11:** Check for ECM input signal from MAFS, HO2S, TPS and other input signals. Are input signals within specification?
- YES → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Replace all failed parts.

---

## DTC P0230

<!-- EFOC0130 -->

**Fuel Pump Circuit Malfunction**

| DTC | Diagnostic Item |
|-----|----------------|
| P0230 | Fuel Pump Circuit Malfunction |

### Test Procedure

<!-- Figure: Fuel Pump Circuit flowchart, source: FLA.pdf page 90 -->

**Step 1:** Check fuel pump relay. Is fuel pump relay normal?
- YES → Go to Step 2
- NO → Replace fuel pump relay.

**Step 2:** Turn ignition ON and measure voltage between ECM terminal F10 and ground (B+). Is measured voltage within specification?
- YES → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Open or short between fuel pump relay and ECM. Repair as necessary.

---

## DTC P0261–P0277

<!-- EFOC0124 -->

**Cylinder 1–6 Injector Circuit Low/High Input**

| DTC | Diagnostic Item |
|-----|----------------|
| P0261 | Cylinder 1 Injector Circuit Low Input |
| P0264 | Cylinder 2 Injector Circuit Low Input |
| P0267 | Cylinder 3 Injector Circuit Low Input |
| P0270 | Cylinder 4 Injector Circuit Low Input |
| P0273 | Cylinder 5 Injector Circuit Low Input |
| P0276 | Cylinder 6 Injector Circuit Low Input |
| P0262 | Cylinder 1 Injector Circuit High Input |
| P0265 | Cylinder 2 Injector Circuit High Input |
| P0268 | Cylinder 3 Injector Circuit High Input |
| P0271 | Cylinder 4 Injector Circuit High Input |
| P0274 | Cylinder 5 Injector Circuit High Input |
| P0277 | Cylinder 6 Injector Circuit High Input |

### Test Procedure

<!-- Figure: Injector Circuit flowchart, source: FLA.pdf page 89 -->

**Step 1:** Turn ignition switch to OFF and disconnect injector connector. With ignition ON and measure voltage between injector terminal 2 and ground (B+). Is measured voltage within specification?
- YES → Go to Step 2
- NO → Open or short between main relay and injector terminal 2. Repair as necessary.

**Step 2:** Reconnect injector connector and measure voltage between injector terminal 1 and ground (B+). Is voltage within specification?
- YES → Go to Step 3
- NO → Open or short between injector terminal 1 and ECM. Repair as necessary.

**Step 3:** Turn ignition switch OFF and disconnect injector connector. With ignition ON and measure voltage between injector terminal 1 and ground. Is measured voltage less than 0.5V?
- YES → Go to Step 4
- NO → Short to battery between injector terminal 1 and ECM. Repair as necessary.

**Step 4:** Measure resistance between injector terminal 1 and terminal 2. Specification: 13.8–15.2 KΩ at 20°C (68°F). Is measured resistance within specification?
- YES → Poor terminal contact due to oxidation, bent or misplaced terminal. Repair as necessary.
- NO → Temporarily install a known good injector and check for proper operation. If problem is corrected, replace HO2S.

**Final:** Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P0300 / P0301 / P0302 / P0303 / P0304 / P0305 / P0306

<!-- EFOC0140 -->

**Random Misfire / Cylinder 1–6 Misfire Detected**

| DTC | Diagnostic Item |
|-----|----------------|
| P0300 | Random Misfire Detected |
| P0301 | Cylinder 1 Misfire Detected |
| P0302 | Cylinder 2 Misfire Detected |
| P0303 | Cylinder 3 Misfire Detected |
| P0304 | Cylinder 4 Misfire Detected |
| P0305 | Cylinder 5 Misfire Detected |
| P0306 | Cylinder 6 Misfire Detected |

### Test Procedure

<!-- Figure: Misfire flowchart, source: FLA.pdf pages 91-93 -->

**Step 1:** Check for any split, disconnected or perforated vacuum hoses. Also, check PCV valve for proper operation. Are vacuum hoses and PCV okay?
- YES → Go to Step 2
- NO → Replace faulty vacuum hoses or PCV.

**Step 2:** Turn ignition OFF and disconnect ignition coil connector. Turn ignition ON and measure voltage at ignition coil terminal 4 (B+). Is battery voltage within specifications?
- YES → Go to Step 3
- NO → Check for open between ignition switch and ignition coil terminal 4. If wiring is OK, check for loose, bent, misplaced or corroded terminals at ignition coil connector. Repair as necessary.

**Step 3:** Turn ignition OFF and check ignition coils and plug wires for cracks or carbon tracing. Check resistance of primary coils (0.66–0.82 Ω at 20°C) and secondary coils (11.3–15.3 KΩ at 20°C) per service manual. Check for resistance of plug wires (16 KΩ per 1m/1'). Are ignition coils and plug wires OK?
- YES → Go to Step 4
- NO → Repair as necessary.

**Step 4:** Remove CKPS and calculate air gap between sensor and flywheel/torque converter (0.5–1.7mm ±0.012–0.067in.) [measure distance from housing to teeth on flywheel/torque converter (measurement "A") and from mounting surface on sensor to sensor tip (measurement "B") subtract "B" from "A" = air gap]. Are air gap and resistance measurements within specifications?
- YES → Go to Step 5
- NO → Repair as necessary.

**Step 5:** Thoroughly check for loose, bent or corroded terminals between CKPS and ECM. Repair as necessary. Then proceed to Step 6.

**Step 6:** Back probe front HO2S output wire. Start engine and allow engine to warm up to operating temperature. In short spurts, spray aerosol carburetor cleaner in the following areas while looking for a long rise in voltage at front HO2S output terminal (a rise in voltage that is approximately as long as the spray of carburetor indicates some of the carburetor cleaner was drawn into the intake chamber richening the fuel mixture verifying a leak). Allow enough time between areas checked for carburetor spray to dissipate.

> **WARNING**
> **Do not spray carburetor cleaner on or near coils or plug wires. An arcing wire or coil could start a fire!**

Check the following areas:
- Throttle body gasket
- Gasket between intake manifold and surge tank
- Seals between intake manifold and fuel injectors
- Seals between surge tank and PCV valves

Are air leaks indicated?
- YES → Rectify as necessary.
- NO → Go to Step 7

**Step 7:** Release fuel pressure and attach fuel pressure gauge to service port on fuel rail. Start engine and warm up to operating temperature. Check for fuel pressure at idle. Fuel pressure at idle: 46–51 psi (320–350kPa, 3.2–3.5kg/cm²). Is fuel pressure within specification?
- YES → Go to Step 8
- NO → Check fuel delivery system.

**Step 8:** Check for any injector related DTCs. Are DTCs related any injectors present?
- YES → Refer to DTC.
- NO → Go to Step 9

**Step 9:** Remove spark plugs and check gap (1.0–1.1mm [0.027–0.031in.?]) and plug condition. Are spark plugs gapped properly and in good condition?
- YES → Go to Step 10
- NO → Repair as necessary.

**Step 10:** Perform compression test [approximately 184 psi, 1275kPa, 13.0kg/cm²] at 300rpm (no more than 10% between highest and lowest cylinder). Is compression OK?
- YES → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Perform leak down test to determine source of low compression and repair as necessary.

---

## DTC P0325 / P0330

<!-- EFOC0150 -->

**Knock Sensor Circuit Malfunction (Bank 1/Bank 2)**

| DTC | Diagnostic Item |
|-----|----------------|
| P0325 | Knock Sensor Circuit Malfunction (Bank 1) |
| P0330 | Knock Sensor Circuit Malfunction (Bank 2) |

### Test Procedure

<!-- Figure: Knock Sensor circuit flowchart, source: FLA.pdf page 94 -->

**Step 1:** Turn ignition OFF and disconnect knock sensor connector and ECM connector. Measure resistance between knock sensor terminal 2 (to ECM) and ECM (< 1Ω). Is resistance within specification?
- YES → Go to Step 2
- NO → Open between knock sensor terminal 2 and ECM. Repair as necessary.

**Step 2:** Measure resistance between knock sensor terminal 3 (to ECM) and ECM (< 1Ω). Is resistance within specification?
- YES → Go to Step 3
- NO → Open between knock sensor terminal 3 and ECM. Repair as necessary.

**Step 3:** Measure resistance between knock sensor terminal 1 and ECM (< 1Ω). Is resistance within specification?
- YES → Go to Step 4
- NO → Open between knock sensor terminal 1 and ECM. Repair as necessary.

**Step 4:** Reconnect knock sensor connector and ECM connector. Measure resistance between knock sensor terminal 3 (to ECM) and ground (< 1Ω). Is resistance infinite?
- YES → Go to Step 5
- NO → Short to ground between knock sensor terminal 3 and ECM. Repair as necessary.

**Step 5:** Measure resistance between knock sensor terminal 3 and terminal 2 (4.87MΩ ± 10% at 20°C [68°F]). Is resistance within specification?
- YES → Poor terminal contacts due to oxidation, bent or misplaced terminals. Repair as necessary.
- NO → Temporarily install a known good knock sensor and check for proper operation. If problem is corrected, replace knock sensor.

**Final:** Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P0335

<!-- EFOC0160 -->

**Crankshaft Position Sensor Circuit Malfunction**

| DTC | Diagnostic Item |
|-----|----------------|
| P0335 | Crankshaft Position Sensor Circuit Malfunction |

### Test Procedure

<!-- Figure: CKPS circuit flowchart, source: FLA.pdf page 95 -->

**Step 1:** Turn ignition OFF and disconnect CKPS connector. Turn ignition ON and measure voltage between CKPS terminal 3 (to main relay) and ground (B+). Is voltage within specification?
- YES → Go to Step 2
- NO → Open or short between CKPS terminal 3 and main relay. Repair as necessary.

**Step 2:** Turn ignition OFF and disconnect ECM connector. Measure resistance between CKPS terminal 1 (to ECM) and ECM (< 1Ω). Is resistance within specification?
- YES → Go to Step 3
- NO → Open between CKPS terminal 1 and ECM. Repair as necessary.

**Step 3:** Measure resistance between CKPS terminal 2 and ECM (< 1Ω). Is resistance within specification?
- YES → Go to Step 4
- NO → Open between CKPS terminal 2 and ECM. Repair as necessary.

**Step 4:** Measure resistance between CKPS terminal 2 (to ECM) and terminal 1 (infinite resistance). Is resistance infinite?
- YES → Go to Step 5
- NO → Short between CKPS terminal 2 and terminal 1. Repair as necessary.

**Step 5:** Turn ignition ON and measure voltage between CKPS terminal 1 (to ECM) and ground (< 0.5V). Is voltage within specification?
- YES → Go to Step 6
- NO → Short to battery between CKPS terminal 1 and ECM. Repair as necessary.

**Step 6:** Remove CKPS and calculate air gap between sensor and flywheel/torque converter (0.5–1.7mm ±0.012–0.067in.) [measure distance from housing to teeth on flywheel/torque converter (measurement "A") and from mounting surface on sensor to sensor tip (measurement "B") subtract "B" from "A" = air gap]. Are air gap and resistance measurements within specifications?
- YES → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Temporarily install a known good CKPS and check for proper operation. If problem is corrected, replace CKPS.

---

## DTC P0340

<!-- EFOC0170 -->

**Camshaft Position Sensor Circuit Malfunction**

| DTC | Diagnostic Item |
|-----|----------------|
| P0340 | Camshaft Position Sensor Circuit Malfunction |

### Test Procedure

<!-- Figure: CMPS circuit flowchart, source: FLA.pdf pages 96-97 -->

**Step 1:** Turn ignition OFF and disconnect CMPS connector. Turn ignition ON and measure voltage between CMPS terminal 3 (to main relay) and ground (B+). Is voltage within specification?
- YES → Go to Step 2
- NO → Open or short between CMPS terminal 3 and main relay. Repair as necessary.

**Step 2:** Turn ignition OFF and disconnect ECM connector. Measure resistance between CMPS terminal 1 (to ECM) and ECM (< 1Ω). Is resistance within specification?
- YES → Go to Step 3
- NO → Open between CMPS terminal 1 and ECM. Repair as necessary.

**Step 3:** Measure resistance between CMPS terminal 2 and ECM (< 1Ω). Is resistance within specification?
- YES → Go to Step 4
- NO → Open between CMPS terminal 2 and ECM. Repair as necessary.

**Step 4:** Measure resistance between CMPS terminal 2 (to ECM) and terminal 1 (infinite resistance). Is resistance infinite?
- YES → Go to Step 5
- NO → Open between CMPS terminal 2 and ECM. Repair as necessary.

**Step 5:** Turn ignition ON and measure voltage between CMPS terminal 1 (to ECM) and ground (< 0.5V). Is voltage within specification?
- YES → Go to Step 6
- NO → Short to battery between CMPS terminal 1 and ECM. Repair as necessary.

**Step 6:** Turn ignition OFF and disconnect CMPS connector. Check for CMPS installation. Is CMPS installed properly?
- YES → Temporarily install a known good CMPS and check for proper operation. If problem is corrected, replace CMPS.
- NO → Remove camshaft and install CMPS correctly.

**Final:** Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P0350–P0356

<!-- EFOC0180 -->

**Ignition Coil Primary/Secondary Circuit Malfunction**

| DTC | Diagnostic Item |
|-----|----------------|
| P0350 | Ignition Coil Primary/Secondary Circuit Malfunction |
| P0351 | Ignition Coil "#1" Primary/Secondary Circuit Malfunction |
| P0352 | Ignition Coil "#2" Primary/Secondary Circuit Malfunction |
| P0353 | Ignition Coil "#3" Primary/Secondary Circuit Malfunction |
| P0354 | Ignition Coil "#4" Primary/Secondary Circuit Malfunction |
| P0355 | Ignition Coil "#5" Primary/Secondary Circuit Malfunction |
| P0356 | Ignition Coil "#6" Primary/Secondary Circuit Malfunction |

### Test Procedure

<!-- Figure: Ignition Coil circuit flowchart, source: FLA.pdf page 98 -->

**Step 1:** Turn ignition OFF and disconnect ignition coil connector. Turn ignition ON and measure voltage between ignition coil terminal 4 and ground (B+). Is voltage within specification?
- YES → Go to Step 2
- NO → Open between ignition coil terminal 4 and ignition switch. Repair as necessary.

**Step 2:** Turn ignition OFF and measure resistance of primary coil (0.66–0.82Ω at 20°C [<68°F>]). Measure resistance of secondary coil (11.3–15.3KΩ at 20°C [<68°F>]). Is resistance within specification?
- YES → Poor terminal contacts due to oxidation, bent or misplaced terminals. Repair as necessary. Go to Step 3.
- NO → Temporarily install a known good ignition coil and check for proper operation. If problem is corrected, replace ignition coil.

**Step 3:** Turn ignition ON and measure voltage between ECM terminal Z1 (cylinder 1 & 4) and ground (B+). Is voltage within specification?
- YES → Go to Step 4
- NO → Open or short between ignition coil terminal 3 and ECM terminal Z1. Repair as necessary.

**Step 4:** Measure voltage between ECM terminal Z2 (cylinder 2 & 5) and ground (B+). Is voltage within specification?
- YES → Go to Step 5
- NO → Open or short between ignition coil terminal 2 and ECM terminal Z2. Repair as necessary.

**Step 5:** Measure voltage between ECM terminal Z3 (cylinder 1 & 6) and ground (B+). Is voltage within specification?
- YES → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Open or short between ignition coil terminal 1 and ECM terminal Z3. Repair as necessary.

---

## DTC P0420 / P0430

<!-- EFOC0190 -->

**Main Catalyst Efficiency Deterioration (Bank 1/Bank 2)**

| DTC | Diagnostic Item |
|-----|----------------|
| P0420 | Main Catalyst Efficiency Deterioration (Bank 1) |
| P0430 | Main Catalyst Efficiency Deterioration (Bank 2) |

### Test Procedure

<!-- Figure: Catalyst Efficiency flowchart, source: FLA.pdf pages 99-100 -->

**Step 1:** Check for DTCs relating to HO2S, ECTS, injector, MAFS, misfire, EVAP, and DTC P0170–P0173. Do DTCs exist?
- YES → First repair all other malfunctions based on DTCs.
- NO → Go to Step 2

**Step 2:** Release fuel pressure and attach fuel pressure gauge to service port on fuel rail. Start engine and warm up to operating temperature. Check for fuel pressure at idle. Fuel pressure at idle: 46–49psi (320–340kPa, 3.26–3.47kg/cm²). Is fuel pressure within specification?
- YES → Go to Step 3
- NO → Check fuel delivery system.

**Step 3:** Check for any split, disconnected or perforated vacuum hoses. Also, check PCV valve for proper operation. Are vacuum hoses and PCV okay?
- YES → Go to Step 4
- NO → Replace faulty vacuum hoses or PCV.

**Step 4:** Check fuel injector operation (refer to service manual). Are fuel injectors working normal and dispensing proper volume?
- YES → Go to Step 5
- NO → Repair as necessary.

**Step 5:** Back probe front HO2S output wire. Start engine and allow engine to warm up to operating temperature. In short spurts, spray aerosol carburetor cleaner in the following areas while looking for a long rise in voltage at front HO2S output terminal (a rise in voltage that is approximately as long as the spray of carburetor indicates some of the carburetor cleaner was drawn into the intake chamber richening the fuel mixture verifying a leak). Allow enough time between areas checked for carburetor spray to dissipate.

> **WARNING**
> **Do not spray carburetor cleaner on or near coils or plug wires. An arcing wire or coil could start a fire!**

Check the following areas:
- Throttle body gasket
- Gasket between intake manifold and surge tank
- Seals between intake manifold and fuel injectors
- Deals between surge tank and PCV valves

Are air leaks indicated?
- YES → Repair as necessary.
- NO → Go to Step 6

**Step 6:** Check for leaks from exhaust system (especially exhaust manifold catalyst around rear HO2S, etc.). Are any leaks present in exhaust system?
- YES → Repair as necessary.
- NO → Replace catalytic converter as necessary.

**Final:** Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P0444 / P0445

<!-- EFOC0200 -->

**EVAP Emission Control System Purge Control Valve Circuit Open/Shorted**

| DTC | Diagnostic Item |
|-----|----------------|
| P0444 | EVAP Emission Control System Purge Control Valve Circuit Open |
| P0445 | EVAP Emission Control System Purge Control Valve Circuit Shorted |

### Test Procedure

<!-- Figure: PCSV circuit flowchart, source: FLA.pdf page 101 -->

**Step 1:** Turn ignition OFF and disconnect PCSV connector. Turn ignition ON and measure voltage between PCSV terminal 2 and ground (B+). Is voltage within specification?
- YES → Go to Step 2
- NO → Open or short to ground between PCSV terminal 2 and main relay. Repair as necessary.

**Step 2:** Turn ignition OFF and measure voltage between PCSV terminal 1 and terminal 2 (24.5–27.5Ω at 20°C [<68°F>]). Is resistance within specification?
- YES → Check for poor terminal contacts due to oxidation, bent deformed, or misplaced terminals. Repair as necessary. Go to Step 3.
- NO → Temporarily install a known good PCSV and check for proper operation. If problem is corrected, replace PCSV.

**Step 3:** Disconnect ECM connector. Measure resistance between PCSV terminal 1 and ECM (< 1Ω). Is resistance within specification?
- YES → Go to Step 4
- NO → Open between PCSV terminal 1 and ECM. Repair as necessary.

**Step 4:** Measure resistance between PCSV terminal 1 and ground (infinite resistance). Is resistance infinite?
- YES → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Short to ground between PCSV terminal 1 and ECM. Repair as necessary.

---

## DTC P0501

<!-- EFOC0250 -->

**Vehicle Speed Sensor Circuit Range/Performance**

| DTC | Diagnostic Item |
|-----|----------------|
| P0501 | Vehicle Speed Sensor Circuit Range/Performance |

### Test Procedure

<!-- Figure: VSS circuit flowchart, source: FLA.pdf page 102 -->

**Step 1:** Measure voltage between ECM terminal F17 and ground.
- B+ with ignition ON
- 0–B+ while driving

Is voltage within specification?
- YES → Check for poor terminal contacts due to oxidation, bent deformed, or misplaced terminals. Repair as necessary.
- NO → Go to Step 2

**Step 2:** Measure voltage between wheel speed sensor signal terminal and ground.
- B+ with ignition ON
- 0–B+ while driving

Is voltage within specification?
- YES → Check for poor terminal contacts due to oxidation, bent deformed, or misplaced terminals. If OK, open or short between wheel speed sensor and ECM. Repair as necessary.
- NO → Faulty WSS or other problem. Repair as necessary.

**Final:** Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P0506

<!-- EFOC0260 -->

**Idle Control System RPM Lower Than Expected**

| DTC | Diagnostic Item |
|-----|----------------|
| P0506 | Idle Control System RPM Lower Than Expected |

### Test Procedure

<!-- Figure: Idle Control Low RPM flowchart, source: FLA.pdf pages 103-104 -->

**Step 1:** Turn ignition OFF and disconnect IAC connector. Turn ignition ON and measure voltage at IAC power terminal 2 (harness side) (B+). Is measured voltage within specification?
- YES → Go to Step 2
- NO → Locate source of open between main relay and IAC. Repair as necessary.

**Step 2:** Turn ignition OFF and reconnect IAC connector. Measure resistance between IAC power terminal 2 and terminal 3 (opening coil)/terminal 1 (closing coil).
- Opening coil: 15–16Ω at 20°C (68°F)
- Closing coil: 17–18.2Ω at 20°C (68°F)

Is measured resistance within specification?
- YES → Thoroughly check for loose, bent or corroded terminals at all connectors in circuit. Go to Step 3.
- NO → Temporarily install a known good CCV and check for proper operation. If problem is corrected, replace CCV.

**Step 3:** Turn ignition OFF and disconnect ECM connector. Measure resistance between ECM terminal M46 and IAC terminal 3 (opening coil side) (< 1Ω). Is measured resistance within specification?
- YES → Go to Step 4
- NO → Locate source of open or high resistance between ECM and IAC. Repair as necessary.

**Step 4:** Turn ignition to OFF and disconnect ECM connector. Measure resistance between ECM terminal M47 and IAC terminal 1 (closing coil side) (< 1Ω). Is measured resistance within specification?
- YES → Go to Step 5
- NO → Locate source of open or high resistance between ECM and IAC. Repair as necessary.

**Step 5:** Remove IAC valve from throttle body and check for excessive carbon deposits and sticking per following check. Connect IAC valve terminal 2 to 12V power source. One at a time, momentarily ground terminals 1 and 3 while visually verifying valve closes when terminal 1 is grounded and valve opens when terminal 3 is grounded. Repeat numerous times to ensure valve reliability. Is IAC valve moving freely and is not carbon fouled?

> **NOTE**
> While IAV valve is removed, inspect throttle body for obstructions in idle circuit ports. Repair or replace as necessary.

- YES → Thoroughly check for loose, bent or corroded terminals at all connectors in circuit. Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Temporarily install a known good CCV and check for proper operation. If problem is corrected, replace CCV.

---

## DTC P0507

<!-- EFOC0070 -->

**Idle Control System RPM Higher Than Expected**

| DTC | Diagnostic Item |
|-----|----------------|
| P0507 | Idle Control System RPM Higher Than Expected |

### Test Procedure

<!-- Figure: Idle Control High RPM flowchart, source: FLA.pdf pages 105-107 -->

**Step 1:** Check accelerator cable free play [0.040–0.120 in (1.0–3.0mm)]. Is accelerator cable free play within specification?
- YES → Go to Step 2
- NO → Adjust cable.

**Step 2:** Check for any split, disconnected or perforated vacuum hoses. Also, check PCV valve for proper operation and purge solenoid valve for proper installation and operation. Are vacuum hoses, PCV and PSV okay?
- YES → Go to Step 3
- NO → Replace faulty vacuum hoses, PCV or PSV.

**Step 3:** Remove intake hose and inspect throttle plate for excessive carbon deposits. Is throttle plate being held open with excessive carbon deposits?
- YES → Clean throttle body.
- NO → Go to Step 4

**Step 4:** Turn ignition ON and measure voltage between TPS signal terminal 1 and ground with throttle closed (0.2–0.8V). Is voltage within specification?
- YES → Go to Step 5
- NO → Open or short between TPS signal terminal 1 and ECM. Repair as necessary.

**Step 5:** Measure resistance between IAC power terminal 2 and terminal 3 (opening coil)/terminal 1 (closing coil).
- Opening coil: 15–16Ω at 20°C (68°F)
- Closing coil: 17–18.2Ω at 20°C (68°F)

Is measured resistance within specification?
- YES → Thoroughly check for loose, bent or corroded terminals at all connectors in circuit. Go to Step 6.
- NO → Temporarily install a known good CCV and check for proper operation. If problem is corrected, replace CCV.

**Step 6:** Remove IAC valve from throttle body and check for excessive carbon deposits and sticking per following check. Connect IAC valve terminal 2 to 12V power source. One at a time, momentarily ground terminals 1 and 3 while visually verifying valve closes when terminal 1 is grounded and valve opens when terminal 3 is grounded. Repeat numerous times to ensure valve reliability. Is IAC valve moving freely and is not carbon fouled?

> **NOTE**
> While IAV valve is removed, inspect throttle body for obstructions in idle circuit ports. Repair or replace as necessary.

- YES → Go to Step 7
- NO → Temporarily install a known good CCV and check for proper operation. If problem is corrected, replace CCV.

**Step 7:** Check for loose, bent or corroded terminals at all connectors in circuit. Then go to Step 8.

**Step 8:** Turn ignition OFF and disconnect ECM connector. Measure resistance between ECM terminal M46 and IAC terminal 3 (opening coil side) (< 1Ω). Is measured resistance within specification?
- YES → Go to Step 9
- NO → Locate source of open or high resistance between ECM and IAC. Repair as necessary.

**Step 9:** Turn ignition OFF and disconnect ECM connector. Measure resistance between ECM terminal M47 and IAC terminal 1 (closing coil side) (< 1Ω). Is measured resistance within specification?
- YES → Go to Step 10
- NO → Locate source of open or high resistance between ECM and IAC. Repair as necessary.

**Step 10:** Back probe front HO2S output wire. Start engine and allow engine to warm up to operating temperature. In short spurts, spray aerosol carburetor cleaner in the following areas while looking for a long rise in voltage at front HO2S output terminal (a rise in voltage that is approximately as long as the spray of carburetor indicates some of the carburetor cleaner was drawn into the intake chamber richening the fuel mixture verifying a leak). Allow enough time between areas checked for carburetor spray to dissipate.

> **WARNING**
> **Do not spray carburetor cleaner on or near coils or plug wires. An arcing wire or coil could start a fire!**

Check the following areas:
- Throttle body gasket
- Gasket between intake manifold and cylinder head
- Gasket between intake manifold and surge tank
- Seals between intake manifold and fuel injectors
- Seals between surge tank and PCV valves

Are air leaks indicated?
- YES → Repair as necessary.
- NO → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P0560

<!-- EFOC0090 -->

**System Voltage Malfunction**

| DTC | Diagnostic Item |
|-----|----------------|
| P0560 | System Voltage Malfunction |

### Test Procedure

<!-- Figure: System Voltage flowchart, source: FLA.pdf page 108 -->

**Step 1:** Measure voltage between ECM terminal P23 and ground (B+). Is voltage within specification?
- YES → Go to Step 2
- NO → Open or short between main relay and ECM terminal P23. Repair as necessary.

**Step 2:** Check for poor terminal contact due to oxidation, bent or misplaced terminal at ECM and main relay. Is connection normal?
- YES → Go to Step 3
- NO → Repair as necessary.

**Step 3:** Check main relay for contamination, deterioration or damage. Is main relay contaminated, deteriorated or damaged?
- YES → Replace main relay.
- NO → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P0650

<!-- EFOC0090 -->

**Malfunction Indication Lamp (MIL) Control Circuit Malfunction**

| DTC | Diagnostic Item |
|-----|----------------|
| P0650 | Malfunction Indication Lamp (MIL) Control Circuit Malfunction |

### Test Procedure

<!-- Figure: MIL circuit flowchart, source: FLA.pdf page 109 -->

**Step 1:** Turn ignition ON and measure voltage between ECM terminal F20 and ground (< 1V). Is voltage within specification?
- YES → Go to Step 2
- NO → Short to battery voltage between instrument cluster and ECM terminal 37. Repair as necessary.

**Step 2:** Turn ignition OFF and disconnect instrument cluster connector. Measure resistance between instrument cluster C01-B3 and ground (infinite resistance). Is resistance within specification?
- YES → Go to Step 3
- NO → Short to ground between harness connector C01-B3 and ECM terminal F20. Repair as necessary.

**Step 3:** Measure resistance between harness connector C01-B3 and ECM terminal F20 (< 1Ω). Is resistance within specification?
- YES → Go to Step 4
- NO → Open between harness C01-B3 and ECM terminal F20. Repair as necessary.

**Step 4:** Check for MIL in instrument cluster. Does MIL operate correctly?
- YES → Poor terminal contact due to oxidation, bent or misplaced terminal at ECM and MIL. Repair as necessary.
- NO → Replace MIL.

**Final:** Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P1134 / P1154

<!-- EFOC0280 -->

**HO2S Circuit Transition Switch Malfunction/Slip (Bank 1/Bank 2, Sensor 1)**

| DTC | Diagnostic Item |
|-----|----------------|
| P1134 | HO2S Circuit Transition Switch Malfunction/Slip (Bank 1, Sensor 1) |
| P1154 | HO2S Circuit Transition Switch Malfunction/Slip (Bank 2, Sensor 1) |

### Test Procedure

<!-- Figure: HO2S Transition Switch flowchart, source: FLA.pdf pages 110-111 -->

**Step 1:** First check for DTC relating to front HO2S. Do DTCs exist?
- YES → First repair all other malfunctions on DTCs.
- NO → Go to Step 2

**Step 2:** Warm up engine to normal operating temperature for more than 10 minutes. Using SCAN TOOL monitor HO2S signal. Does the HO2S signal switch lean to rich or rich to lean over 3 times in 10 seconds?
- YES → Go to Step 3
- NO → Temporarily install a known good front HO2S and check for proper operation. If problem is corrected, replace front HO2S.

**Step 3:** Check HO2S for contamination, deterioration or damage. Is HO2S contaminated, deteriorated or damaged?
- YES → Clean HO2S with cleaner before installing. If damaged or deteriorated, replace.
- NO → Go to Step 4

**Step 4:** Thoroughly check for loose, bent or corroded connectors at ECM and HO2S connectors. Are connectors normal?
- YES → Go to Step 5
- NO → Repair as necessary.

**Step 5:** Turn ignition switch OFF and disconnect HO2S connector. Measure resistance between HO2S signal terminal 2 and ECM (< 1Ω). Is measured resistance within specification?
- YES → Go to Step 6
- NO → Open between ECM and HO2S terminal 2. Repair as necessary.

**Step 6:** Measure resistance between HO2S terminal 1 and ECM (< 1Ω). Is measured resistance within specification?
- YES → Go to Step 7
- NO → Open between ECM and HO2S terminal 1. Repair as necessary.

**Step 7:** Reconnect HO2S connector, start engine and allow engine to idle until ECT reaches operating temperature. Measure voltage between HO2S terminal 4 and ground (B+). Is voltage within specification?
- YES → Go to Step 8
- NO → Open or short between HO2S terminal 4 and main relay. Repair as necessary.

**Step 8:** Measure resistance between HO2S terminal 3 and ECM (< 1Ω). Is resistance within specification?
- YES → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Open between HO2S terminal 3 and ECM. Repair as necessary.

---

## DTC P1166 / P1167

<!-- EFOC0290 -->

**Lambda Bank Control Limit (Bank 1/Bank 2)**

| DTC | Diagnostic Item |
|-----|----------------|
| P1166 | Lambda Bank Control Limit (Bank 1) |
| P1167 | Lambda Bank Control Limit (Bank 2) |

### Test Procedure

<!-- Figure: Lambda Bank Control flowchart, source: FLA.pdf pages 112-114 -->

**Step 1:** Check for DTCs relating to front/rear HO2S, fuel system, EVAP, and ignition system. Do DTCs exist?
- YES → First repair all other malfunctions on DTCs.
- NO → Go to Step 2

**Step 2:** Check for correct vacuum hose connections to engine dynamic chamber (especially PSV, ISC hose, and brake booster). Are connections OK?
- YES → Go to Step 3
- NO → Rectify as necessary.

**Step 3:** With engine idling, disconnect hose between EVAP valve and canister. Check for vacuum at EVAP valve. Is vacuum available at purge valve when EVAP valve is not operating?
- YES → EVAP canister purge valve or circuit failure. Repair according to DTC P0443 repair procedures.
- NO → Go to Step 4

**Step 4:** After installing fuel pressure gauge to service port on fuel rail, connect DLC F/P and B (B+) with a jumper wire. Is fuel line pressure correct with ignition switch ON? Fuel pressure at idle: 46–49psi (320–340kPa, 3.26–3.47kg/cm²)
- YES → Go to Step 5
- NO → See pressure diagnosis below

**Step 4 (NO path — Low/High pressure):**

Low pressure:
- Clamp return line and check if pressure rises.
  - If pressure rises: replace pressure regulator.
  - If pressure does not rise: check the strainer at the fuel pump.

High pressure:
- Disconnect return line from fuel filter side and blow through line towards tank.
  - If line is clear: replace fuel delivery module.
  - If line is blocked, check for blockage in return line and clear or replace as necessary.
  - If it is OK, check fuel.

**Step 5:** Warm up engine to normal operating temperature for more than 10 minutes. Using SCAN TOOL monitor HO2S signal. Does the front HO2S signal switch lean to rich or rich to lean over 3 times in 10 seconds?
- YES → Go to Step 6
- NO → Temporarily install a known good front HO2S and check for proper operation. If problem is corrected, replace front HO2S.

**Step 6:** Check front/rear HO2S for contamination, deterioration or damage. Is front/rear HO2S contaminated, deteriorated or damaged?
- YES → Clean HO2S with cleaner before installing. If damaged or deteriorated, replace front/rear HO2S.
- NO → Go to Step 7

**Step 7:** Thoroughly check for loose, bent or corroded connectors at ECM and front/rear HO2S connectors. Are connectors normal?
- YES → Go to Step 8
- NO → Repair as necessary.

**Step 8:** Visually check for exhaust system leak. Are any leaks present?
- YES → Repair as necessary.
- NO → Go to Step 9

**Step 9:** Start engine and check for engine RPM decrease when disconnecting each injector connector in sequence. Measure the decreasing engine RPM of all 6 cylinders. Is there any cylinder with no change in RPM or only a small RPM change?
- YES → Rectify as necessary.
- NO → Go to Step 10

**Step 10:** Inspect MAFS output signal between MAFS output terminal 2 and ground terminal 3 (0.2–0.8V at idling). Is output voltage within specifications?
- YES → Go to Step 11
- NO → Inspect according to MAFS diagnosis and repair.

**Step 11:** Remove spark plugs and inspect spark plug tips. Check for abnormal color of spark plug tips compared to other cylinders. Any spark plug with abnormal color compared to other cylinders?
- YES → Check for engine mechanical failure. If it is OK, replace spark plug.
- NO → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P1372

<!-- EFOC0310 -->

**Segment Time Acquisition Incorrect**

| DTC | Diagnostic Item |
|-----|----------------|
| P1372 | Segment Time Acquisition Incorrect |

### Test Procedure

<!-- Figure: Segment Time flowchart, source: FLA.pdf page 115 -->

**Step 1:** Turn ignition OFF and disconnect wheel speed sensor connector. Measure resistance between wheel speed sensor terminal 1 and terminal 2 (1275–1495Ω at 20°C [<68°F>]). Is measured resistance within specification?
- YES → Go to Step 2
- NO → Temporarily install a known good wheel speed sensor and check for proper operation. If problem is corrected, replace wheel speed sensor.

**Step 2:** Check for following items:
- Gap between wheel speed sensor and rotor: 0.0118–0.0433 in. (0.3–1.1 mm)
- Damage of rotor teeth
- Connection, rust and deformation of wheel speed sensor connector

All items OK?
- YES → Go to Step 3
- NO → Repair or replace as necessary.

**Step 3:** Measure resistance between wheel speed sensor terminal 1 and ECM (< 1Ω). Is resistance within specification?
- YES → Go to Step 4
- NO → Open between wheel speed sensor terminal 1 and ECM. Repair as necessary.

**Step 4:** Measure resistance between wheel speed sensor terminal 2 and ECM (< 1Ω). Is resistance within specification?
- YES → Go to Step 5
- NO → Open between wheel speed sensor terminal 2 and ECM. Repair as necessary.

**Step 5:** Measure resistance between wheel speed sensor terminal 2 (to ECM) and terminal 1 (infinite resistance). Is resistance infinite?
- YES → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Short between wheel speed sensor terminal 2 and terminal 1. Repair as necessary.

---

## DTC P1505 / P1506 / P1507 / P1508

<!-- EFOC0320 -->

**Idle Charge Actuator Signal Low/High (Coil 1/Coil 2)**

| DTC | Diagnostic Item |
|-----|----------------|
| P1505 | Idle Charge Actuator Signal Low (Coil 1) |
| P1506 | Idle Charge Actuator Signal High (Coil 1) |
| P1507 | Idle Charge Actuator Signal Low (Coil 2) |
| P1508 | Idle Charge Actuator Signal High (Coil 2) |

### Test Procedure

<!-- Figure: Idle Charge Actuator flowchart, source: FLA.pdf page 116 -->

**Step 1:** Turn ignition OFF and disconnect IAC connector. Turn ignition ON and measure voltage at IAC power terminal 2 (harness side) (B+). Is measured voltage within specification?
- YES → Go to Step 2
- NO → Locate source of open between main relay and IAC. Repair as necessary.

**Step 2:** Turn ignition OFF and disconnect ECM connector. Measure resistance between ECM terminal M46 and IAC terminal 3 (opening coil side) (< 1Ω). Is measured resistance within specification?
- YES → Go to Step 3
- NO → Locate source of open or high resistance between ECM and IAC. Repair as necessary.

**Step 3:** Turn ignition OFF and disconnect ECM connector. Measure resistance between ECM terminal M47 and IAC terminal 1 (closing coil side) (< 1Ω). Is measured resistance within specification?
- YES → Go to Step 4
- NO → Locate source of open or high resistance between ECM and IAC. Repair as necessary.

**Step 4:** Measure resistance between ECM terminal M47 and terminal M46 (infinite resistance). Is resistance within specification?
- YES → Go to Step 5
- NO → Short between ECM terminal M46 and terminal M47. Repair as necessary.

**Step 5:** Turn ignition OFF and reconnect IAC connector. Measure resistance between IAC power terminal 2 and terminal 3 (opening coil)/terminal 1 (closing coil).
- Opening coil: 15–16Ω at 20°C (68°F)
- Closing coil: 17–18.2Ω at 20°C (68°F)

Is measured voltage within specification?
- YES → Thoroughly check for loose, bent or corroded terminals at all connectors in circuit.
- NO → Temporarily install a known good CCV and check for proper operation. If problem is corrected, replace CCV.

**Final:** Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P1521

<!-- EFOC0330 -->

**Power Steering Switch Malfunction**

| DTC | Diagnostic Item |
|-----|----------------|
| P1521 | Power Steering Switch Malfunction |

### Test Procedure

<!-- Figure: Power Steering Switch flowchart, source: FLA.pdf page 117 -->

**Step 1:** Check for poor contacts between power steering switch and ground. Is contact okay?
- YES → Go to Step 2
- NO → Repair as necessary.

**Step 2:** Turn ignition OFF and disconnect power steering switch connector. Measure resistance between power steering switch terminal and ground (infinite resistance). Is resistance within specification?
- YES → Go to Step 3
- NO → Replace power steering switch.

**Step 3:** Reconnect power steering switch connector. Measure resistance between power steering switch terminal and ground (infinite resistance). Is resistance within specification?
- YES → Go to Step 4
- NO → Short to ground between power steering switch and ECM terminal M26. Repair as necessary.

**Step 4:** Turn ignition ON and measure voltage between power steering switch terminal and ground (approximately 10V). Is voltage within specification?
- YES → Poor terminal contact due to oxidation, bent or misplaced terminal at ECM and power steering switch. Repair as necessary.
- NO → Open between power steering switch and ECM terminal M26. Repair as necessary.

**Final:** Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.

---

## DTC P1602

<!-- EFOC0340 -->

**Serial Communication Problem With TCU (time-out)**

| DTC | Diagnostic Item |
|-----|----------------|
| P1602 | Serial Communication Problem With TCU (time-out) |

### Test Procedure

<!-- Figure: TCU Communication flowchart, source: FLA.pdf page 118 -->

**Step 1:** Turn ignition OFF and disconnect ECM connector. Measure resistance between ECM terminal F36 and ground (infinite resistance). Is measured resistance within specification?
- YES → Go to Step 2
- NO → Short to ground between ECM terminal F36 and TCM terminal C3. Repair as necessary.

**Step 2:** Measure resistance between ECM terminal F37 and ground (infinite resistance). Is measured resistance within specification?
- YES → Go to Step 3
- NO → Short to ground between ECM terminal F37 and TCM terminal C4. Repair as necessary.

**Step 3:** Measure resistance between ECM terminal F36 and terminal F37 (infinite resistance). Is measured resistance within specification?
- YES → Go to Step 4
- NO → Short between ECM terminal F36 and terminal F37. Repair as necessary.

**Step 4:** Thoroughly check for loose, bent or corroded connectors at ECM and TCM connectors. With ignition OFF, disconnect ECM and TCM connectors. Measure resistance between TCM and ECM on both circuits. Is resistance all below 1 ohm?
- YES → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Check TCM related fault code by scan tool and measure appropriately. Repair as necessary.

---

## DTC P1624

<!-- EFOC0370 -->

**Cooling Fan Relay Circuit Malfunction (Low)**

| DTC | Diagnostic Item |
|-----|----------------|
| P1624 | Cooling Fan Relay Circuit Malfunction (Low) |

### Test Procedure

<!-- Figure: Cooling Fan Low Relay flowchart, source: FLA.pdf page 119 -->

**Step 1:** Check for poor terminal contacts due to oxidation, bent or misplaced terminals at cooling fan low relay. Is connection normal?
- YES → Go to Step 2
- NO → Repair as necessary.

**Step 2:** Turn ignition ON and measure voltage between ECM terminal F18 and ground (B+). Is voltage within specification?
- YES → Go to Step 3
- NO → Open or short between ECM terminal F18 and cooling fan low relay. Repair as necessary.

**Step 3:** Check for poor terminal contacts due to oxidation, bent or misplaced terminals at ECM terminal F18. Is connection normal?
- YES → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Repair as necessary.

---

## DTC P1625

<!-- EFOC0380 -->

**Cooling Fan Relay Circuit Malfunction (High)**

| DTC | Diagnostic Item |
|-----|----------------|
| P1625 | Cooling Fan Relay Circuit Malfunction (High) |

### Test Procedure

<!-- Figure: Cooling Fan High Relay flowchart, source: FLA.pdf page 120 -->

**Step 1:** Check for poor terminal contacts due to oxidation, bent or misplaced terminals at cooling fan high relay No.1. Is connection normal?
- YES → Go to Step 2
- NO → Repair as necessary.

**Step 2:** Turn ignition ON and measure voltage between ECM terminal F40 and ground (B+). Is voltage within specification?
- YES → Go to Step 3
- NO → Open or short between ECM terminal F40 and cooling fan high relay No.1 and/or No.2. Repair as necessary.

**Step 3:** Check for poor terminal contacts due to oxidation, bent or misplaced terminals at ECM terminal F40. Is connection normal?
- YES → Return vehicle to original condition. Clear all diagnostic trouble codes. Verify by driving vehicle with SCAN TOOL connected and monitor for pending codes.
- NO → Repair as necessary.
