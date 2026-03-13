---
source: FLA.pdf
chapter: FLA
section: FLA-20 to FLA-45
pages: 20-45
engine: V6
title: MFI Control System (Part 1)
---

# MFI Control System

## Troubleshooting
<!-- EFOC0301 -->

### Diagnostic Troubleshooting Flow

<!-- Figure: Diagnostic troubleshooting flowchart, source: FLA.pdf page 20 -->

1. Gather information from customer.
2. Verify complaint.
3. Determine frequency:
   - **Several reoccurrences** → Check for diagnostic trouble codes.
   - **One time only** → Check for diagnostic trouble codes.
4. Results:
   - **Diagnostic trouble code found** → Record the diagnostic trouble code, then erase the codes.
   - **No code** (one time only) → No further action.
   - **No code or communication with scan tool not possible** → Refer to the MFI TROUBLESHOOTING PROCEDURES.
5. Try to reproduce the symptom.
   - **Reproduced** → Read the diagnostic trouble codes.
     - **Diagnostic trouble code displayed** → Refer to the INSPECTION CHART FOR DIAGNOSTIC TROUBLE CODES (FL-21).
     - **Diagnostic trouble code not displayed** → INTERMITTENT MALFUNCTIONS (Refer to FL-17 How to Cope with Intermittent Malfunctions).
   - **No symptom** → OK.

---

## Inspection Chart for Diagnostic Trouble Codes
<!-- EFOC0040 -->

| DTC No. | Content | EOBD | Non-EOBD |
|:--------|:--------|:----:|:--------:|
| P0031 | HO2S Heater Circuit Low (Bank 1, Sensor 1) | O | △ |
| P0032 | HO2S Heater Circuit High (Bank 1, Sensor 1) | O | △ |
| P0037 | HO2S Heater Circuit Low (Bank 1, Sensor 2) | O | △ |
| P0038 | HO2S Heater Circuit High (Bank 1, Sensor 2) | O | △ |
| P0051 | HO2S Heater Circuit Low (Bank 2, Sensor 1) | O | △ |
| P0052 | HO2S Heater Circuit High (Bank 2, Sensor 1) | O | △ |
| P0057 | HO2S Heater Circuit Low (Bank 2, Sensor 2) | O | △ |
| P0058 | HO2S Heater Circuit High (Bank 2, Sensor 2) | O | △ |
| P0101 | Mass or Volume Air Flow Circuit Range/Performance Problem | O | △ |
| P0102 | Mass or Volume Air Flow Circuit Low Input | - | △ |
| P0103 | Mass or Volume Air Flow Circuit High Input | - | △ |
| P0112 | Intake Air Temperature Circuit Low Input | O | △ |
| P0113 | Intake Air Temperature Circuit High Input | O | △ |
| P0116 | Engine Coolant Temperature Sensor Circuit Range/Performance Problem | - | △ |
| P0117 | Engine Coolant Temperature Circuit Low Input | O | △ |
| P0118 | Engine Coolant Temperature Circuit High Input | O | △ |
| P0121 | Throttle Position Sensor Circuit Range/Performance Problem | - | △ |
| P0122 | Throttle Position Sensor Circuit Low Input | O | △ |
| P0123 | Throttle Position Sensor Circuit High Input | O | △ |
| P0131 | HO2S Circuit Low Input (Bank 1, Sensor 1) | - | △ |
| P0132 | HO2S Circuit High Input (Bank 1, Sensor 1) | - | △ |
| P0133 | HO2S Circuit Slow Responsive (Bank 1, Sensor 1) | - | △ |
| P0137 | HO2S Circuit Low Input (Bank 1, Sensor 2) | - | △ |
| P0138 | HO2S Circuit Low Input (Bank 1, Sensor 2) | - | △ |
| P0151 | HO2S Circuit Low Input (Bank 2, Sensor 1) | - | △ |
| P0152 | HO2S Circuit High Input (Bank 2, Sensor 1) | - | △ |
| P0153 | HO2S Circuit Slow Responsive (Bank 2, Sensor 1) | - | △ |
| P0157 | HO2S Circuit Low Input (Bank 2, Sensor 2) | - | △ |
| P0158 | HO2S Circuit High Input (Bank 2, Sensor 2) | - | △ |
| P0171 | Fuel System Too Lean (Bank 1) | - | △ |
| P0172 | Fuel System Too Rich (Bank 1) | - | △ |
| P0174 | Fuel System Too Lean (Bank 2) | - | △ |
| P0175 | Fuel System Too Rich (Bank 2) | - | △ |
| P0230 | Fuel Pump Circuit Malfunction | - | △ |
| P0261 | Injector Circuit Low Input (Cylinder -1) | O | △ |
| P0264 | Injector Circuit Low Input (Cylinder -2) | O | △ |
| P0267 | Injector Circuit Low Input (Cylinder -3) | O | △ |
| P0270 | Injector Circuit Low Input (Cylinder -4) | O | △ |
| P0273 | Injector Circuit Low Input (Cylinder -5) | O | △ |
| P0276 | Injector Circuit Low Input (Cylinder -6) | O | △ |
| P0262 | Injector Circuit High Input (Cylinder -1) | O | △ |
| P0265 | Injector Circuit High Input (Cylinder -2) | O | △ |
| P0268 | Injector Circuit High Input (Cylinder -3) | O | △ |
| P0271 | Injector Circuit High Input (Cylinder -4) | O | △ |
| P0274 | Injector Circuit High Input (Cylinder -5) | O | △ |
| P0277 | Injector Circuit High Input (Cylinder -6) | O | △ |
| P0300 | Random Misfire Detected | O | - |
| P0301 | Misfire Detected (Cylinder -1) | O | - |
| P0302 | Misfire Detected (Cylinder -2) | O | - |
| P0303 | Misfire Detected (Cylinder -3) | O | - |
| P0304 | Misfire Detected (Cylinder -4) | O | - |
| P0305 | Misfire Detected (Cylinder -5) | O | - |
| P0306 | Misfire Detected (Cylinder -6) | O | - |
| P0325 | Knock Sensor Circuit Malfunction (Bank 1) | △ | △ |
| P0330 | Knock Sensor Circuit Malfunction (Bank 2) | △ | △ |
| P0335 | Crankshaft Position Sensor Circuit Malfunction | O | △ |
| P0340 | Camshaft Position Sensor Circuit Malfunction | O | △ |
| P0350 | Ignition Coil Primary/Secondary Circuit Malfunction | △ | - |
| P0351 | Ignition Coil 'A' Primary/Secondary Circuit Malfunction | - | △ |
| P0352 | Ignition Coil 'B' Primary/Secondary Circuit Malfunction | - | △ |
| P0353 | Ignition Coil 'C' Primary/Secondary Circuit Malfunction | - | △ |
| P0354 | Ignition Coil 'D' Primary/Secondary Circuit Malfunction | - | △ |
| P0355 | Ignition Coil 'E' Primary/Secondary Circuit Malfunction | - | △ |
| P0356 | Ignition Coil 'F' Primary/Secondary Circuit Malfunction | - | △ |
| P0420 | Main Catalyst Efficiency Deterioration (Bank 1) | O | △ |
| P0430 | Main Catalyst Efficiency Deterioration (Bank 2) | O | △ |
| P0444 | EVAP Emission Control System Purge Control Valve Circuit Open | - | △ |
| P0445 | EVAP Emission Control System Purge Control Valve Circuit Shorted | - | △ |
| P0501 | Vehicle Speed Sensor Range/Performance | O | △ |
| P0506 | Idle Control System Rpm Lower than Expected | - | △ |
| P0507 | Idle Control System Rpm Higher than Expected | - | △ |
| P0560 | System Voltage Malfunction | - | △ |
| P0605 | Internal CONTROL Module ROM Error | - | △ |
| P0650 | Malfunction Indication Lamp (MIL) Control Circuit Malfunction | - | △ |
| P1134 | HO2S Circuit - Transition Switch Malfunction/Slip (Bank 1, Sensor 1) | O | △ |
| P1154 | HO2S Circuit - Transition Switch Malfunction/Slip (Bank 2, Sensor 1) | O | △ |
| P1166 | Lambda Bank Control Limit (Bank 1) | O | △ |
| P1167 | Lambda Bank Control Limit (Bank 2) | O | - |
| P1372 | Segment Time Acquisition Incorrect | - | △ |
| P1505 | Idle Charge Actuator Signal Low of Coil #1 | O | △ |
| P1506 | Idle Charge Actuator Signal High of Coil #1 | O | △ |
| P1507 | Idle Charge Actuator Signal Low of Coil #2 | O | △ |
| P1508 | Idle Charge Actuator Signal High of Coil #2 | O | △ |
| P1521 | Power Steering Switch Malfunction | - | △ |
| P1529 | TCU Request for MIL ON/Freeze Frame to ECU via CAN | - | △ |
| P1602 | Serial Communication Problem with TCU (Timeout) | - | △ |
| P1624 | Cooling Fan Relay Circuit Malfunction (LOW) | - | △ |
| P1625 | Cooling Fan Relay Circuit Malfunction (HIGH) | - | △ |

- "O" : means DTC and MIL-ON.
- "△" : means only DTC-ON.

---

## Trouble Area Related to DTC
<!-- EFOC0065 -->

> **Note:** Check items for each diagnostic item do not list all probable causes.

| DTC No. | Diagnostic Items | Trouble Area |
|:--------|:-----------------|:-------------|
| P0031 | HO2S Heater Circuit Low (Bank 1, Sensor 1) | - Blown or missing HO2S fuse - Open or short to GND between HO2S and ECM - Faulty HO2S |
| P0032 | HO2S Heater Circuit High (Bank 1, Sensor 1) | - Short to battery between HO2S and ECM - Faulty HO2S |
| P0037 | HO2S Heater Circuit Low (Bank 1, Sensor 2) | - Blown or missing HO2S fuse - Open or short to GND between HO2S and ECM - Faulty HO2S |
| P0038 | HO2S Heater Circuit High (Bank 1, Sensor 2) | - Short to battery between HO2S and ECM - Faulty HO2S |
| P0051 | HO2S Heater Circuit Low (Bank 2, Sensor 1) | - Blown or missing HO2S fuse - Open or short to GND between HO2S and ECM - Faulty HO2S |
| P0052 | HO2S Heater Circuit High (Bank 2, Sensor 1) | - Short to battery between HO2S and ECM - Faulty HO2S |
| P0057 | HO2S Heater Circuit Low (Bank 2, Sensor 2) | - Blown or missing HO2S fuse - Open or Short to GND between HO2S and ECM - Faulty HO2S |
| P0058 | HO2S Heater Circuit High (Bank 2, Sensor 2) | - Short to battery between HO2S and ECM - Faulty HO2S |
| P0101 | Mass or Volume Air Flow Circuit Range/Performance Problem | - Dirty air cleaner - Oil cap or dipstick missing or not installed correctly - Air leak in intake system - Contaminated, deteriorated or damaged mass air flow sensor - Faulty mass air flow sensor or throttle position sensor - Poor connections between ECM and MAFS or TPS |

> **NOTE**
> *If any codes relating to MAFS are present, do all repairs associated with them before proceeding with this troubleshooting area.*

| DTC No. | Diagnostic Items | Trouble Area |
|:--------|:-----------------|:-------------|
| P0102 | Mass or Volume Air Flow Circuit Low Input | - Short to ground between MAFS and ECM - Signal line open between MAFS and ECM - Faulty MAFS |
| P0103 | Mass or Volume Air Flow Circuit High Input | - Short to Battery between MAFS and ECM - Ground open between MAFS and EGI main relay - Ground open or Poor connections between open or short to battery between MAFS and ECM - Faulty MAFS |
| P0112 | Intake Air Temperature Circuit Low Input | - Short to ground between IAT sensor and ECM - Short between IAT sensor wires |
| P0113 | Intake Air Temperature Circuit High Input | - Open or short to battery between IAT sensor and ECM - Faulty IAT sensor |
| P0116 | Engine Coolant Temperature Sensor Circuit Range/Performance Problem | - After engine start-up, the measured coolant temperature shows no variation after detecting the calculated coolant temperature variation (engine coolant temperature sensor input is stuck.) - Poor connections between ECT sensor and ECM - Misplaced, loose or corroded terminals - Foreign materials fouled ECTS - Faulty ECTS |

> **NOTE**
> *If any codes relating to ECTS are present, do all repairs associated with them before proceeding with this troubleshooting area.*

| DTC No. | Diagnostic Items | Trouble Area |
|:--------|:-----------------|:-------------|
| P0117 | Engine Coolant Temperature Circuit Low Input | - Short to ground between ECTS and ECM - Short between ECTS wires - Faulty ECTS |
| P0118 | Engine Coolant Temperature Circuit High Input | - Open or short to battery between ECTS and ECM - Faulty ECTS |
| P0121 | Throttle Position Sensor Circuit Range/Performance Problem | - Poor connections between TPS and ECM - Misplaced, loose or corroded terminals - Contaminated, deteriorated TPS - Open or short between TPS 5V reference and ECM - Open or short between TPS signal and ECM - Short between TPS wires - Faulty TPS |
| P0122 | Throttle Position Sensor Circuit Low Input | - Short to GND between TPS and ECM - Open short to GND between TPS and ECM - Short to RND between ECM and fuel tank pressure sensor (FTPS) - Faulty TPS or FTPS |
| P0123 | Throttle Position Sensor Circuit High Input | - Open or battery short between TPS and ECM - Open between and ECM - Faulty TPS |
| P0131 | HO2S Circuit Low Input (Bank 1, Sensor 1) | - Short to GND between HO2S and ECM - Faulty front HO2S |
| P0132 | HO2S Circuit High Input (Bank 1, Sensor 1) | - Short to battery between HO2S and ECM - Faulty front HO2S |
| P0133 | HO2S Circuit Slow Responsive (Bank 1, Sensor 1) | - Front and rear HO2S connections reversed - Faulty fuel delivery system - Leak in intake system - Leak in exhaust system - Faulty MAFS ground circuit - Faulty HO2S |

> **NOTE**
> *If any misfire, purge solenoid valve, MAFS or HO2S heater codes are present, do all repairs associated with those codes before proceeding with this trouble area.*

| DTC No. | Diagnostic Items | Trouble Area |
|:--------|:-----------------|:-------------|
| P0137 | HO2S Circuit Low Input (Bank 1, Sensor 2) | - Short to GND between HO2S and ECM - Faulty front HO2S |
| P0138 | HO2S Circuit Low Input (Bank 1, Sensor 2) | - Open or short to battery between HO2S and ECM - Faulty front HO2S |
| P0151 | HO2S Circuit Low Input (Bank 2, Sensor 1) | - Short to GND between HO2S and ECM - Faulty front HO2S |
| P0152 | HO2S Circuit High Input (Bank 2, Sensor 1) | - Short to battery between HO2S and ECM - Faulty front HO2S |
| P0153 | HO2S Circuit Slow Responsive (Bank 2, Sensor 1) | - Front and rear HO2S connections reversed - Faulty fuel delivery system - Leak in intake system - Leak in exhaust system - Faulty MAFS ground circuit - Faulty HO2S |

> **NOTE**
> *If any misfire, purge solenoid valve, MAFS or HO2S heater codes are present, do all repairs associated with those codes before proceeding with this trouble area.*

| DTC No. | Diagnostic Items | Trouble Area |
|:--------|:-----------------|:-------------|
| P0157 | HO2S Circuit Low Input (Bank 2, Sensor 2) | - Short to GND between HO2S and ECM - Faulty rear HO2S |
| P0158 | HO2S Circuit High Input (Bank 2, Sensor 2) | - Open or short to battery between HO2S and ECM - Faulty rear HO2S |
| P0171 | Fuel System Too Lean (Bank 1) | - Faulty ignition system (Ignition coil/spark plug/ignition cable) - Faulty fuel delivery system (Fuel tank/Pressure regulator/Canister purge valve) - Clogged fuel injectors - Faulty fuel injectors - Leak in intake system - Leak in exhaust system - Faulty MAFS |

> **NOTE**
> *If any codes relating to injectors, HO2S, ECTS or MAFS are stored, do all repairs associated with those codes before proceeding with this trouble area.*

| DTC No. | Diagnostic Items | Trouble Area |
|:--------|:-----------------|:-------------|
| P0172 | Fuel System Too Rich (Bank 1) | - Faulty fuel delivery system (Fuel tank/Pressure regulator/Canister purge valve) - Faulty fuel injectors - Faulty MAFS |

> **NOTE**
> *If any codes relating to injectors, HO2S, ECTS or MAFS are stored, do all repairs associated with those codes before proceeding with this trouble area.*

| DTC No. | Diagnostic Items | Trouble Area |
|:--------|:-----------------|:-------------|
| P0174 | Fuel System Too Lean (Bank 2) | - Faulty ignition system (Ignition coil/spark plug/ignition cable) - Faulty fuel delivery system (Fuel tank/Pressure regulator/Canister purge valve) - Clogged fuel injectors - Faulty fuel injectors - Leak in intake system - Leak in exhaust system - Faulty MAFS |

> **NOTE**
> *If any codes relating to injectors, HO2S, ECTS or MAFS are stored, do all repairs associated with those codes before proceeding with this trouble area.*

| DTC No. | Diagnostic Items | Trouble Area |
|:--------|:-----------------|:-------------|
| P0175 | Fuel System Too Rich (Bank 2) | - Faulty fuel delivery system (Fuel tank/Pressure regulator/Canister purge valve) - Faulty fuel injectors - Faulty MAFS |

> **NOTE**
> *If any codes relating to injectors, HO2S, ECTS or MAFS are stored, do all repairs associated with those codes before proceeding with this trouble area.*

| DTC No. | Diagnostic Items | Trouble Area |
|:--------|:-----------------|:-------------|
| P0230 | Fuel Pump Circuit Malfunction | - Blown or missing fuse/relay - Short to battery between fuel pump relay and ECM - Open between fuel pump relay and ECM - Faulty fuel pump relay |
| P0261 | Injector Circuit Low Input (Cylinder -1) | - Short to GND between injector and ECM - Faulty fuel injector |
| P0264 | Injector Circuit Low Input (Cylinder -2) | |
| P0267 | Injector Circuit Low Input (Cylinder -3) | |
| P0270 | Injector Circuit Low Input (Cylinder -4) | |
| P0273 | Injector Circuit Low Input (Cylinder -5) | |
| P0276 | Injector Circuit Low Input (Cylinder -6) | |
| P0262 | Injector Circuit High Input (Cylinder -1) | - Open between injector fuse and injector - Open or short to battery between injector and ECM - Faulty fuel injector |
| P0265 | Injector Circuit High Input (Cylinder -2) | |
| P0268 | Injector Circuit High Input (Cylinder -3) | |
| P0271 | Injector Circuit High Input (Cylinder -4) | |
| P0274 | Injector Circuit High Input (Cylinder -5) | |
| P0277 | Injector Circuit High Input (Cylinder -6) | |
| P0300 | Random Misfire Detected | - Vacuum leak in air intake system - CKP sensor circuit malfunction - Faulty CKP sensor |
| P0301 | Misfire Detected (Cylinder -1) | - Ignition circuit malfunction - Faulty ignition coil or plug wire - Spark plug malfunction |
| P0302 | Misfire Detected (Cylinder -2) | - Low compression due to blown head gasket, leaking valve or piston ring |
| P0303 | Misfire Detected (Cylinder -3) | - Low/high fuel pressure due to faulty pressure regulator, restricted fuel lines, plugged fuel filter or faulty fuel pump |
| P0304 | Misfire Detected (Cylinder -4) | - Fuel injector circuit malfunction - Faulty fuel injector |
| P0305 | Misfire Detected (Cylinder -5) | |
| P0306 | Misfire Detected (Cylinder -6) | |

> **NOTE**
> *If any fuel injector codes (or pending codes) are present, do all repairs associated with those codes before proceeding with this trouble area.*

| DTC No. | Diagnostic Items | Trouble Area |
|:--------|:-----------------|:-------------|
| P0325 | Knock Sensor Circuit Malfunction (Bank 1) | - Open or short to GND between knock sensor and ECM - Source of high resistance between knock sensor and ECM - Faulty knock sensor |
| P0330 | Knock Sensor Circuit Malfunction (Bank 2) | - Faulty knock sensor |
| P0335 | Crankshaft Position Sensor Circuit Malfunction | - Short to GND between CKP sensor and ECM - Open or short to battery between CKP sensor and ECM - Short between CKP sensor wires - Poor connection between CKP connector & harness connector - Out of allowable air gap - Faulty target wheel tolerance - Faulty CKP sensor |
| P0340 | Camshaft Position Sensor Circuit Malfunction | - Short to GND between CMP sensor and ECM - Open or short to battery between CMP and ECM - Short between CMP sensor wires - Poor connection between CMP connector & harness connector - Faulty CMP sensor |
| P0350 | Ignition Coil Primary/Secondary Circuit Malfunction | - Faulty ignition system - Poor connection - Faulty wires between ignition coil and ECM - Faulty ignition coil |
| P0420 | Main Catalyst Efficiency Deterioration (Bank 1) | - Catalytic converter deteriorated |

> **NOTE**
> *If any codes relating to HO2S sensor, MAFS, injectors, a P0170 or a P0173 are present, do all repairs associated with them before proceeding with this trouble area.*

| DTC No. | Diagnostic Items | Trouble Area |
|:--------|:-----------------|:-------------|
| P0430 | Main Catalyst Efficiency Deterioration (Bank 2) | - Catalytic converter deteriorated |

> **NOTE**
> *If any codes relating to HO2S sensor, MAFS, injectors, a P0170 or a P0173 are present, do all repairs associated with them before proceeding with this trouble area.*

| DTC No. | Diagnostic Items | Trouble Area |
|:--------|:-----------------|:-------------|
| P0444 | EVAP Emission Control System Purge Control Valve Circuit Open | - Faulty PSV - Open between PSV and ECM |
| P0445 | EVAP Emission Control System Purge Control Valve Circuit Shorted | - Faulty PSV - Short to GND or battery between PSV and ECM - Open between WSS and GND |
| P0501 | Vehicle Speed Sensor Range/Performance | - Open between fuse and wheel speed sensor (WSS) - Open between WSS and GND - Open between WSS and ECM - Short to battery or GND between WSS and ECM - Faulty WSS |
| P0506 | Idle Control System Rpm Lower than Expected | - High resistance between injector fuse and IAC valve - High resistance between IAC and ECM - Faulty IAC valve - Carbon fouled throttle plate |

> **NOTE**
> *If any TPS, MAFS, fuel injector or IAC valve circuit codes (or pending codes) are present, do all repairs associated with them before proceeding with this troubleshooting area.*

| DTC No. | Diagnostic Items | Trouble Area |
|:--------|:-----------------|:-------------|
| P0507 | Idle Control System Rpm Higher than Expected | - Improperly adjusted accelerator cable - Air leak in intake system between head and throttle plate - Faulty PCV valve or PSV - Poor connections in TPS circuit or faulty TPS - High resistance between IAC valve and ECM - Faulty IAC valve |

> **NOTE**
> *If any codes relating to TPS, MAFS, fuel injector or IAC valve are present, do all repairs associated with them before proceeding with this troubleshooting area.*

| DTC No. | Diagnostic Items | Trouble Area |
|:--------|:-----------------|:-------------|
| P0560 | System Voltage Malfunction | - Short between main relay and ECM - Open between main relay and ECM - Poor connection - Faulty main relay |
| P0650 | Malfunction Indication Lamp (MIL) Control Circuit Malfunction | - Open or short between lamp and ECM - Faulty lamp |
| P1505 | Idle Charge Actuator Signal Low of Coil #1 | - Open or short to GND between ISC and ECM - Faulty ISC |
| P1506 | Idle Charge Actuator Signal High of Coil #1 | - Short to battery between ISC and ECM - Faulty ISC |
| P1507 | Idle Charge Actuator Signal Low of Coil #2 | - Open or short to GND between ISC and ECM - Faulty ISC |
| P1508 | Idle Charge Actuator Signal High of Coil #2 | - Short to battery between ISC and ECM - Faulty ISC |
| P1521 | Power Steering Switch Malfunction | - Open or short to battery between switch and ECM - Short to GND between switch and ECM - Open between switch and ECM - Faulty power steering switch |
| P1529 | TCU Request for MIL ON/Freeze Frame to ECU via CAN | - This is only a request from TCM to turn the MIL ON. The fault code is stored in the TCM. The freeze frame data is stored in the ECM under the P1529 request code. Be sure to retrieve freeze frame data before clearing code P1529 from ECM. |
| P1602 | Serial Communication Problem with TCU (Timeout) | - Open or short to serial communication line - CAN message timeout - Faulty TCU |
| P1624 | Cooling Fan Relay Circuit Malfunction (LOW) | - Open or short between relay and ECM - Short to GND between relay and ECM - Open between relay and ECM - Faulty relay |
| P1625 | Cooling Fan Relay Circuit Malfunction (HIGH) | - Open or short between relay and ECM - Faulty relay |

---

## Major Sensor Reference Wave-Forms
<!-- EFOC0345 -->

The following are the major sensor reference wave-forms. Below is the data for CMP, Mass Air Flow Sensor, Throttle Position Sensor, Rear O2 Sensor, Front O2 Sensor and Injection Pulse when moving quickly up to 4000 rpm at no load after warming up engine sufficiently. Each value is for reference, the exact values may vary.

### CMP and CKP

Should increase gradually while depressing the accelerator pedal and should decrease gradually after releasing the pedal without any intermittent drop or rise.

<!-- Figure: CMP and CKP waveform (2.7 V6 scope capture), source: FLA.pdf page 29 -->

### MAF Sensor and TPS

MAF should increase when depressing the accelerator pedal and should decrease at the moment "THRTL POS SEN" is closed (accelerator pedal is released).

TPS should increase while depressing the accelerator pedal and should decrease while releasing it.

<!-- Figure: MAF and TPS overlay waveform (2.7 V6 scope capture), source: FLA.pdf page 30 -->

### FR O2 Sensor and RR O2 Sensor

FR O2 and RR O2 sensor may increase immediately after depressing the accelerator pedal and may decrease after releasing the pedal.

<!-- Figure: Front and Rear O2 sensor waveforms (2.7 V6 scope capture), source: FLA.pdf page 30 -->

### INJ Pulse

Should increase when depressing the accelerator pedal and should decrease when the pedal is released.

<!-- Figure: Injector pulse waveform (2.7 V6 scope capture), source: FLA.pdf page 30 -->

---

## Location of MFI Components
<!-- EFOC3260 -->

### Engine Bay (Top View)

<!-- Figure: Engine bay component locations showing IAT, TPS, MAF, CKP, Ignition coil, Knock sensor, WTS, CMP, Injector positions, source: FLA.pdf page 31 -->

**Engine bay components:**
- IAT (Intake Air Temperature sensor)
- TPS (Throttle Position Sensor)
- MAF (Mass Air Flow sensor)
- CKP (Crankshaft Position sensor)
- Ignition coil
- WTS (Water Temperature Sensor / ECT)
- CMP (Camshaft Position sensor)
- Injector
- Knock sensor

### Interior / Dashboard Area

<!-- Figure: Interior component locations showing Vehicle speed sensor, ECM, Ignition switch, DLC positions, source: FLA.pdf page 31 -->

**Interior components:**
- Vehicle speed sensor
- ECM
- Ignition switch
- DLC (Data Link Connector)

### Component Legend (Numbered from engine diagram)

<!-- EFOC325B -->

| No. | Component |
|:----|:----------|
| 1 | Engine coolant temperature (ECT) sensor |
| 2 | Mass air flow sensor |
| 3 | Intake air temp. (IAT) sensor |
| 4 | Throttle position sensor (TPS) |
| 5 | Idle speed actuator (ISA) |
| 6 | Heated oxygen sensor (HO2S) |
| 7 | Camshaft position sensor (CMP) |
| 8 | Crankshaft position sensor (CKP) |
| 9 | Injector |
| 10 | Evap. canister purge control solenoid valve (PCSV) |
| 11 | Knock sensor |
| 12 | Power steering oil pressure switch |
| 13 | Canister close valve |
| 14 | Fuel tank pressure sensor |

### Additional Component Location Photos

<!-- Figure: ECT Sensor location on engine, source: FLA.pdf page 33 -->
<!-- Figure: Power Steering Oil Pressure Switch location, source: FLA.pdf page 33 -->
<!-- Figure: Vehicle Speed Sensor location, source: FLA.pdf page 33 -->
<!-- Figure: Ignition Timing Adjustment Terminal location, source: FLA.pdf page 33 -->
<!-- Figure: EVAP Solenoid Valve location, source: FLA.pdf page 33 -->
<!-- Figure: MAP, TPS, ISA, TR location on throttle body area (labeled TH, MAP, TPS, ISA), source: FLA.pdf page 33 -->
<!-- Figure: CMP Sensor location, source: FLA.pdf page 33 -->
<!-- Figure: CKP Sensor location on lower front of engine, source: FLA.pdf page 33 -->
<!-- Figure: Data Link Connector (DLC) location under dashboard, source: FLA.pdf page 34 -->
<!-- Figure: Heated Oxygen Sensor (HO2S) location, source: FLA.pdf page 34 -->
<!-- Figure: Transaxle Range (TR) Switch location near battery, source: FLA.pdf page 34 -->
<!-- Figure: Injectors on intake manifold, source: FLA.pdf page 34 -->
<!-- Figure: Knock Sensor location on engine block, source: FLA.pdf page 34 -->

---

## Engine Coolant Temperature (ECT) Sensor
<!-- EFOC0400 -->

The engine coolant temperature sensor installed in the engine coolant passage of the cylinder head detects the engine coolant temperature and emits signals to the ECM. This part employs a thermistor which is sensitive to changes in temperature. The electric resistance of the thermistor decreases in response to a temperature rise. The ECM determines engine coolant temperature by the sensor output voltage and provides optimum fuel enrichment when the engine is cold.

### Circuit Diagram

**[2.7 V6]**

<!-- Figure: ECT sensor circuit diagram showing harness side connector (A), ECT sensor side connector, and wiring to ECM pins 24 (Engine coolant temp. sensor output) and 25 (Sensor ground). Includes resistance vs. coolant temperature graph showing inverse relationship, source: FLA.pdf page 35 -->

**ECM connections:**
- Pin 24 → Engine coolant temp. sensor output
- Pin 25 → Sensor ground

### Sensor Checking

#### Using HI-SCAN

| Check Item | Data Display | Check Conditions | Intake Air Temperature | Test Specification |
|:-----------|:-------------|:-----------------|:----------------------:|:------------------:|
| Engine coolant temperature sensor | Sensor temperature | Ignition switch: ON or engine running | When -20°C (-4°F) | -20°C |
| | | | When 0°C (32°F) | 0°C |
| | | | When 20°C (68°F) | 20°C |
| | | | When 40°C (104°F) | 40°C |
| | | | When 80°C (176°F) | 80°C |

#### Using Multi-Meter

1. Remove engine coolant temperature sensor from the intake manifold.
2. With temperature sensing portion of engine coolant temperature sensor immersed in hot engine coolant, check resistance.

| Temperature [°C (°F)] | Resistance (kΩ) |
|:----------------------|:---------------:|
| 0 (32) | 5.9 |
| 20 (68) | 2.5 |
| 40 (104) | 1.1 |
| 80 (176) | 0.3 |

<!-- Figure: ECT sensor immersed in coolant for resistance testing, source: FLA.pdf page 36 -->

3. If the resistance deviates from the standard value greatly, replace the sensor.

### Harness Inspection Procedure

**Step 1:**

Check for continuity of the ground circuit.
- Connector: Disconnected

| Result | Action |
|:-------|:-------|
| **OK** | → Go to Step 2 |
| **NG** | → Repair the harness. |

<!-- Figure: Harness side connector (H) continuity check with ohmmeter, source: FLA.pdf page 37 -->

**Step 2:**

Measure the power supply voltage.
- Connector: Disconnected
- Ignition switch: ON
- Voltage (V): 4.5–4.9V

| Result | Action |
|:-------|:-------|
| **OK** | → **END** |
| **NG** | → Repair the harness. |

<!-- Figure: Harness side connector (H) voltage measurement with voltmeter, source: FLA.pdf page 37 -->

### Troubleshooting Procedures

<!-- Figure: ECT troubleshooting flowchart, source: FLA.pdf page 38 -->

1. Engine: Running
2. Check the wiring connection. Is the connection OK?
   - **NO** → Repair the wiring.
   - **YES** → Continue.
3. Check the ECT Sensor. Is the ECT Sensor OK?
   - **NO** → Repair the ECT sensor.
   - **YES** → Continue.
4. Check the cooling system including THERMOSTAT opening state. (Refer to EM Group) Is it OK?
   - **NO** → Replace the THERMOSTAT.
   - **YES** → Continue.
5. Erase diagnostic trouble code from memory. Is same code No. present after rechecking?
   - **YES** → Replace PCM.

**Abbreviations:**
- DTC: Diagnosis Trouble Code
- PCM: Powertrain Control Module
- ECT: Engine Coolant Temperature

### Using Voltmeter

| Check Item | Coolant Temperature | Test Specification |
|:-----------|:-------------------:|:------------------:|
| Engine coolant temperature sensor output voltage | When 0°C | 4.05V |
| | When 20°C | 3.44V |
| | When 40°C | 2.72V |
| | When 80°C | 1.25V |

### Troubleshooting Hints

If the fast idle speed is not enough or the engine gives off dark smoke during the engine warm-up operation, the engine coolant temperature sensor might be the cause.

### Installation

1. Apply sealant LOCTITE 962T or equivalent to threaded portion.
2. Install engine coolant temperature sensor and tighten it to specified torque.

**Tightening torque:**
Engine coolant temperature sensor: **20–40 Nm (200–400 kg.cm, 14–29 lb.ft)**

3. Securely connect the harness connector.

---

## Mass Air Flow (MAF) Sensor
<!-- EFOC0360 -->

This hot film type air flow sensor is composed of a hot film sensor, housing, metering duct (hybrid, sensor element). Mass air flow rate is measured by detection of heat transfer from a hot film probe because the change of the mass air flow rate causes change in the amount of heat being transferred from the hot film probe surface to the air flow. The air flow sensor generates a pulse so it repeatedly opens and closes between the 5V voltage supplied from the engine control module. This results in the change of the temperature of the hot film probe and in the change of resistance.

### Circuit Diagram [2.7 V6]

<!-- Figure: MAF sensor circuit diagram showing mass air flow sensor connector (3-pin), harness side connector (A), connection to MFI Control relay and ECM pin 17. Includes output voltage vs. mass airflow graph showing: Idle=0.5V, 2000rpm=1.0V, range 100-700 kg/h, source: FLA.pdf page 40 -->

**MAF sensor connector:** 3-pin
**ECM connections:**
- Pin 17 → Signal (V)
- GND connection

**Output characteristics:**
- Idle: ~0.5V
- 2000 rpm: ~1.0V
- Range: 100–700 kg/h (approximately linear)

### Troubleshooting Procedures

<!-- Figure: MAF troubleshooting flowchart, source: FLA.pdf page 41 -->

1. Engine: Running
2. Check wiring harness and connection. Is it OK?
   - **NO** → Repair the harness and connector.
   - **YES** → Continue.
3. Check the IAT sensor. Is the sensor normal?
   - **NO** → Replace the sensor.
   - **YES** → Continue.
4. Erase any diagnostic trouble codes from memory. Is same code present after rechecking?
   - **OK** → Replace PCM.

**Abbreviations:**
- DTC: Diagnosis Trouble Code
- PCM: Powertrain Control Module

### Troubleshooting Hints

1. If the engine stalls occasionally, start the engine and shake the MAF sensor harness. If the engine stalls, check for poor contact at the MAF sensor connector.
2. If the MAF sensor output voltage is other than 0 when the ignition switch is turned on (do not start the engine), Check for a faulty MAF sensor or ECM.
3. If the engine can be idle even if the MAF sensor output voltage is out of specification, check for the following conditions:
   - Disturbed air flow to the MAF sensor, check for disconnected air duct, and clogged air cleaner filter.
   - Poor combustion in the cylinder, check for faulty ignition plug, ignition coil, injector, and incorrect compression.
4. Check the mounting direction of AFS.

| Check Item | Check Condition | Test Specification |
|:-----------|:---------------:|:------------------:|
| Mass air flow sensor output voltage | Idle rpm | 0.5V |
| | 2000 rpm | 1.0V |

> **NOTE**
> - *When the vehicle is new (within initial operation of about 500 km (300 miles)), the mass air flow sensor air quantity will be about 10% higher.*
> - *Use an accurate digital voltmeter.*
> - *Before checking, warm up the engine until the engine coolant temperature reaches 80 to 97°C (176 to 188°F).*

### Harness Inspection Procedure

**Step 1:**

Measure the power supply voltage.
- Connector: Disconnected.
- Ignition switch: ON.
- Voltage (V): Battery voltage.

| Result | Action |
|:-------|:-------|
| **OK** | → Go to Step 2 |
| **NG** | → Repair the harness. |

<!-- Figure: Harness side connector (A) voltage check with voltmeter, source: FLA.pdf page 42 -->

**Step 2:**

Check for an open circuit, or a short circuit to ground between the powertrain control module and the mass air flow sensor.
- PCM connector: Disconnected.
- Mass air sensor connector: Disconnected.

| Result | Action |
|:-------|:-------|
| **OK** | → Go to Step 3 |
| **NG** | → Repair the harness. |

<!-- Figure: Harness side connector (A) open/short circuit check, source: FLA.pdf page 42 -->

**Step 3:**

Check for continuity of the ground circuit.
- Connector: Disconnected.

| Result | Action |
|:-------|:-------|
| **OK** | → **END!** |
| **NG** | → Repair the harness. |

<!-- Figure: Harness side connector (A) ground continuity check with ohmmeter, source: FLA.pdf page 42 -->

---

## Intake Air Temperature (IAT) Sensor
<!-- EFOC0410 -->

The intake air temperature sensor (IAT Sensor), located in the intake air hose, is a thermistor sensor for detecting the intake air temperature. According to the intake air temperature information from the sensor, the ECM provides necessary fuel injection amount control.

### Circuit Diagram

**[2.7 V6]**

<!-- Figure: IAT sensor circuit diagram showing IAT side connector (2-pin), harness side connector (A), and wiring to ECM pins 23 (Sensor signal) and 22 (4V~5V reference through resistor). Source: FLA.pdf page 43 -->

**IAT sensor connector:** 2-pin
**ECM connections:**
- Pin 23 → Sensor signal
- Pin 22 → 4V~5V reference (through internal resistor)

### Troubleshooting Procedures

<!-- Figure: IAT troubleshooting flowchart, source: FLA.pdf page 44 -->

1. Engine: Running
2. Check the harness and connector. Is it OK?
   - **NO** → Repair the harness and connector.
   - **YES** → Continue.
3. Check the IAT sensor. Is the sensor normal?
   - **NO** → Replace the sensor.
   - **YES** → Continue.
4. Erase any diagnostic trouble codes from memory. Is same code present after rechecking?
   - **NO** → OK
   - **YES** → Replace PCM.

**Abbreviations:**
- DTC: Diagnosis Trouble Code
- PCM: Powertrain Control Module

### Troubleshooting Hints

The MIL is ON or the DTC is displayed on the HI-SCAN under the following conditions:

1. When the intake air temperature is detected as below -40°C or higher than 120°C
2. Input from intake air temperature sensor is below 0.1V or above 4.8V when engine is in a full warm-up condition.

### Using HI-SCAN

| Check Item | Data Display | Check Conditions | Intake Air Temperature | Test Specification |
|:-----------|:-------------|:-----------------|:----------------------:|:------------------:|
| Intake air temperature sensor | Air temperature | Ignition switch: ON or engine running | When -20°C (-4°F) | -20°C |
| | | | When 0°C (32°F) | 0°C |
| | | | When 20°C (68°F) | 20°C |
| | | | When 40°C (104°F) | 40°C |
| | | | When 80°C (176°F) | 80°C |

### Harness Inspection Procedure [2.7 V6]

**Step 1:**

Measure the power supply voltage of the IAT Sensor.
- Connector: Disconnected.
- Ignition switch: ON.
- Voltage: 4.8–5.2V.

| Result | Action |
|:-------|:-------|
| **OK** | → Go to Step 2 |
| **NG** | → Repair the harness. |

<!-- Figure: Harness side connector (A) voltage measurement with voltmeter, source: FLA.pdf page 45 -->

**Step 2:**

Check for an open circuit, or a short circuit to ground between the powertrain control module and the IAT sensor.
- PCM connector: Disconnected.
- IAT sensor connector: Disconnected.

| Result | Action |
|:-------|:-------|
| **OK** | → **END!** |
| **NG** | → Repair the harness. |

<!-- Figure: Harness side connector (A) open/short circuit check, source: FLA.pdf page 45 -->

### Sensor Inspection

1. Use the multimeter, measure the sensor resistance.
2. Measure the resistance between the IAT sensor terminal 1 and 2.

| IG.SW. ON | Temperature °C (°F) | Resistance (kΩ) |
|:----------|:-------------------:|:---------------:|
| | 0 (32) | 3.3 - 3.7 |
| | 20 (68) | 2.4 - 2.8 |
| | 40 (104) | 1.6 - 2.0 |
| | 80 (176) | 0.5 - 0.9 |

3. If the resistance deviates from the standard value, replace the intake air temperature sensor assembly.
