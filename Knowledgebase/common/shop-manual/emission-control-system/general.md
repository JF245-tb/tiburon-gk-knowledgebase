---
source: EC.pdf
chapter: EC
section: EC-1 to EC-12
pages: 1-12
engine: V6
title: General — Specifications, Service Standard, Torque, Troubleshooting, Emission Controls Location, Schematic Drawings
---

<!-- EC-1 : Chapter title page -->

# General

## Specifications <!-- EC-2 -->

| Components | Function | Remarks |
|------------|----------|---------|
| **Crankcase Emission System** | | |
| Positive Crankcase Ventilation (PCV) valve | HC reduction | Variable flow rate type |
| **Evaporative Emission System** | | |
| Evaporative emission canister | HC reduction | |
| EVAP Canister Purge Solenoid Valve | | Duty control solenoid valve |
| **Exhaust Emission System** | | |
| MFI system (air-fuel mixture control device) | CO, HC, NOx reduction | Heated oxygen sensor feedback type |
| Three-way catalytic converter | CO, HC, NOx reduction | Monolithic type |

MFI : Multiport Fuel Injection
EVAP : Evaporative Emission

## Service Standard <!-- EC-2 -->

| Item | Specification |
|------|---------------|
| Evaporative emission canister purge solenoid valve coil resistance | 26 Ω (at 20°C (68°F)) |

## Tightening Torque <!-- EC-2 -->

| Item | Nm | kgf-cm | lb-ft |
|------|-----|--------|-------|
| Positive Crankcase Ventilation Valve | 8–12 | 80–120 | 6–8 |

## Troubleshooting <!-- EC-2 -->

| Symptom | Probable cause | Remedy |
|---------|---------------|--------|
| Engine will not start or hard to start | Vacuum hose disconnected or damaged | Repair or replace |
| | Malfunction of the EVAP Canister Purge Solenoid Valve | Repair or replace |
| Rough idle or engine stalls | Vacuum hose disconnected or damaged | Repair or replace |
| | Malfunction of the PCV valve | Replace |
| | Malfunction of the evaporative emission canister purge system | Check the system; if there is a problem, check related components parts |
| Excessive oil consumption | Positive crankcase ventilation line clogged | Check positive crankcase ventilation system |

---

## Emission Controls Location [1.6 I4] <!-- EC-3 -->

<!-- Figure: Engine bay photo — 1.6L I4 layout (top-down view) -->

## Emission Controls Location [2.0 I4] <!-- EC-3 -->

<!-- Figure: Engine bay photo — 2.0L I4 layout (top-down view) -->

Legend:
- A : PCV valve
- B : Purge control solenoid valve

## Emission Controls Location [2.7 V6] — Sensors and Components <!-- EC-4, EC-5 -->

<!-- Figure: EC-4 — Numbered sensor location photos (2.7 V6):
1. MAP & IAT
2. TBA (Throttle Body Assembly)
3. ECT
4. TPS
5. CMP
6. CKP
7. O2 sensor
8. PCV valve / Injector
9. (reserved)
11. Knock sensor
12. Transaxle Range Switch (Inhibitor Switch)
18. IG.COIL
-->

<!-- Figure: EC-5 — Engine bay photo (2.7 V6 top-down view) showing:
IAT, TPS, MAF, CKP, Ignition coil, Knock sensor, WTS, Injector, CMP -->

### Component Photos (2.7 V6) <!-- EC-5, EC-6 -->

| Label | Component |
|-------|-----------|
| A | PCV valve |
| B | EVAP Canister Purge Solenoid Valve |
| C | Two-way Valve |
| D | Catalytic Converter (MCC) |
| E | Catalytic Converter (UCC) |
| F | Evap. Canister |

<!-- Figure: EC-5 A — PCV valve photo -->
<!-- Figure: EC-5 B — EVAP Canister Purge Solenoid Valve photo -->
<!-- Figure: EC-5 C — Two-way Valve photo -->
<!-- Figure: EC-5 D — Catalytic Converter (MCC) photo -->
<!-- Figure: EC-6 E — Catalytic Converter (UCC) photo -->
<!-- Figure: EC-6 F — Evap. Canister photo -->

---

## Schematic Drawing [I4, EOBD] <!-- EC-7 -->

**INPUT:**
1. Manifold Absolute Pressure (MAP) Sensor & Intake Air Temp (IAT) Sensor
2. Engine Coolant Temp. (ECT) Sensor
3. Throttle Position Sensor (TPS)
4. Crankshaft Position (CKP) Sensor
5. Camshaft Position (CMP) Sensor
6. Heated Oxygen Sensor (HO2S-FR)
7. Heated Oxygen Sensor (HO2S-RR)
8. Accel. Position Sensor (Accel. Sensor)

**OUTPUT:**
1. Fuel Injector
2. Ignition Coil
3. Control Relay
4. Fuel Pump Relay
5. Purge Control Solenoid
6. Idle Speed Actuator (ISA)

<!-- Figure: EC-7 — I4 EOBD schematic showing ECM, control relay, ECM power, IG. switch, MAP & IAT, TPS, ECT, CKP, CMP, HO2S-FR, HO2S-RR, Accel. sensor, fuel tank, evap canister, muffler, catalyst -->

## Schematic Drawing [I4, NON-EOBD] <!-- EC-8 -->

**INPUT:**
1. Manifold Absolute Pressure (MAP) Sensor & Intake Air Temp (IAT) Sensor
2. Engine Coolant Temp. (ECT) Sensor
3. Throttle Position Sensor (TPS)
4. Crankshaft Position (CKP) Sensor
5. Camshaft Position (CMP) Sensor
6. Knock Sensor (KS)
7. Heated Oxygen Sensor (HO2S-FR)

**OUTPUT:**
1. Fuel Injector
2. Ignition Coil
3. Control Relay
4. Fuel Pump Relay
5. Purge Control Solenoid
6. Valve (ICTV)
7. Idle Speed Actuator (ISA)

<!-- Figure: EC-8 — I4 NON-EOBD schematic -->

## Schematic Drawing [I4, NON-EOBD] (Leaded) <!-- EC-9 -->

**INPUT:**
1. Manifold Absolute Pressure (MAP) Sensor & Intake Air Temp (IAT) Sensor
2. Engine Coolant Temp. (ECT) Sensor
3. Throttle Position Sensor (TPS)
4. Crankshaft Position (CKP) Sensor
5. Camshaft Position (CMP) Sensor
6. Knock Sensor (KS)

**OUTPUT:**
1. Fuel Injector
2. Ignition Coil
3. Control Relay
4. Fuel Pump Relay
5. Purge Control Solenoid
6. Valve (ICTV)
7. Idle Speed Actuator (ISA)

<!-- Figure: EC-9 — I4 NON-EOBD Leaded schematic -->

---

## Schematic Drawing [2.7 V6, EOBD] <!-- EC-10 -->

**INPUT:**
1. Heated Oxygen Sensor (HO2S)
2. MAT FLM Sensor
3. Intake Air Temp. Sensor
4. Vehicle Speed Sensor
5. Engine Coolant Temp. Sensor
6. CKP Sensor
7. TPS Sensor
8. Camshaft Position Sensor
9. CMP Sensor
10. Knock Sensor

**SWITCH:**
a. Ignition Switch
b. Battery Voltage
c. Vehicle Speed Sensor
d. A/C Switch
e. "P/N" Switch (A/T Only)
f. Fuel Pump Relay Signal

**OUTPUT:**
1. Fuel Injector
2. Ignition Coil
3. Cooling Fan
4. Fuel Pump Relay
5. EVAP Canister Purge Solenoid Valve
6. ISCV
7. A/C Relay
8. MIL
9. Section Trans Control
10. Diagnosis

PCM : Powertrain Control Module
EVAP : Evaporative Emission
UCC : Underbody Catalytic Converter
MCC : Manifold Catalytic Converter

<!-- Figure: EC-10 — 2.7 V6 EOBD schematic showing Main Relay, ECM, Fuel Pump Relay, Fuel Pressure Regulator, Air cleaner, Canister, Fuel Tank, UCC, MCC -->

## Schematic Drawing [2.7 V6, NON-EOBD] <!-- EC-11 -->

**INPUT:**
1. Heated Oxygen Sensor (HO2S)
2. MAT FLM Sensor
3. Intake Air Temp. Sensor
4. Vehicle Speed Sensor
5. Engine Coolant Temp. Sensor
6. CKP Sensor
7. TPS Sensor
8. Camshaft Position Sensor
9. CMP Sensor
10. Knock Sensor

**SWITCH:**
a. Ignition Switch
b. Battery Voltage
c. Vehicle Speed Sensor
d. A/C Switch
e. "P/N" Switch (A/T Only)
f. Fuel Pump Relay Signal

**OUTPUT:**
1. Fuel Injector
2. Ignition Coil
3. Cooling Fan
4. Fuel Pump Relay
5. EVAP Canister Purge Solenoid Valve
6. ISCV
7. A/C Relay
8. Ignition Trans Control
9. Diagnosis

ECM : Engine Control Module
EVAP : Evaporative Emission
UCC : Under floor catalytic converter

<!-- Figure: EC-11 — 2.7 V6 NON-EOBD schematic showing Main Relay, ECM, P/REG, 2 way valve, IG. switch, Fuel Pump Relay, Fuel Filter, Air cleaner, Canister, Fuel Tank, UCC -->

## Schematic Drawing [2.7 V6, NON-EOBD] (Leaded) <!-- EC-12 -->

**INPUT:**
1. MAT FLM Sensor
2. Intake Air Temp. Sensor
3. MAP Sensor
4. Vehicle Speed Sensor
5. Engine Coolant Temp. Sensor
6. Throttle Position Sensor
7. Camshaft Position Sensor
8. CKP Sensor
9. CMP Sensor
10. Knock Sensor
11. EGT Sensor

**SWITCH:**
a. Ignition Switch
b. Battery Voltage
c. Vehicle Speed Sensor
d. A/C Switch
e. "P/N" Switch (A/T Only)
f. Fuel Pump Relay Signal
g. Variable Resistor

**OUTPUT:**
1. Fuel Injector
2. Ignition Coil
3. Cooling Fan
4. Fuel Pump Relay
5. EVAP Canister Purge Solenoid Valve
6. ISCV
7. A/C Relay
8. Ignition Trans Control
9. Diagnosis

ECM : Engine Control Module
EVAP : Evaporative Emission

<!-- Figure: EC-12 — 2.7 V6 NON-EOBD Leaded schematic showing Main Relay, ECM, P/REG, 2 way valve, IG. switch, Fuel Pump Relay, Fuel Filter, Air cleaner, Canister, Fuel Tank -->
