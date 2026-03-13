---
source: FLA.pdf
chapter: FLA
section: FLA-1 to FLA-5
pages: 1-5
engine: V6
title: Fuel System — Specifications
---

# Fuel System (2.7 V6)

## Table of Contents

- General .............................................................. FLA-2
- MFI Control System ............................................. FLA-20
- Troubleshooting for DTCs (Siemens EMS) .................. FLA-73

---

## GENERAL

### General Specifications

<!-- EFOC0010 -->

#### Throttle Body

| Item | Detail | Specifications |
|---|---|---|
| Throttle position sensor (TPS) | Type | Variable resistor |
| | Resistance at curb idle (2.7 V6) | 1.6 - 2.4 KΩ |
| | Output voltage at curb idle (2.7 V6) | 250 - 800 mV |
| Idle speed control (ISC) actuator | Type | Double Coil |
| | Resistance | 90 - 110 Hz |

#### Sensors

| Item | Detail | Specifications |
|---|---|---|
| Air flow sensor | Type (2.7 V6) | Hot Film sensor |
| Intake air temperature (IAT) sensor | Type (2.7 V6) | Thermistor |
| | Resistance | 2.33 - 2.97 KΩ at 20°C (68°F) |
| Engine coolant temperature (ECT) sensor | Type | Thermistor |
| | Resistance | 2.5 KΩ at 20°C (68°F) |
| | | 0.3 KΩ at 80°C (176°F) |
| Heated oxygen sensor (HO2S) | Type (2.7 V6) | Titanium |
| Vehicle speed sensor | Type | Hall effect |
| Camshaft position (CMP) sensor | Type | Hall effect |
| Crankshaft position (CKP) sensor | Type | Hall effect |

#### Actuators

| Item | Detail | Specifications |
|---|---|---|
| Injectors | Type, number (2.7 V6) | Electromagnetic type, 6 |
| | Resistance | 13 - 16Ω at 20°C (68°F) |
| Evaporative emission purge control solenoid valve | Type | Duty cycle type |

#### Fuel Pressure Regulator

| Item | Specifications |
|---|---|
| Pressure regulator | 300 ± 1.5 kPa (0.35 ± 0.06 kg/cm²) |

#### Fuel Tank

| Item | Specifications |
|---|---|
| Tank capacity | 55 liter (14.5 US gal, 12.1 Imp.gal) |
| Return system | Equipped |

#### Canister

| Item | Specifications |
|---|---|
| Volume/Nominal working capacity | 3.0 liter/150g |

---

### Sealant

<!-- EFA90020 -->

| Item | Specified sealant |
|---|---|
| Engine coolant temperature sensor | LOCTITE 962T or equivalent |

---

### Service Standards

<!-- EFOC0030 -->

| Item | Condition | Standard value |
|---|---|---|
| Basic ignition timing (2.7 V6) | | BTDC 12° ± 5° at curb idle |
| Curb idle speed, rpm (2.7 V6) | D-range (A/T) | 650 ± 100 |
| | P,N-range (A/C OFF) | 750 ± 100 |
| | A/T, M/T (A/C ON) | 800 ± 100 |
| Fuel pressure kPa (psi) | Vacuum hose disconnected | 330 - 350 (47-50) at curb idle |
| | Vacuum hose connected | Approx. 270 (38) at curb idle |
| Evap canister purge control solenoid valve resistance | | 20 - 32Ω |

---

### Tightening Torque

<!-- EFA90045 -->

| Item | Nm | Kg.cm | lb.ft |
|---|---|---|---|
| Delivery pipe installation bolt | 10 - 15 | 100 - 150 | 7 - 11 |
| Engine coolant temperature sensor | 20 - 40 | 200 - 400 | 14 - 29 |
| Heated oxygen sensor | 40 - 50 | 400 - 500 | 29 - 36 |
| Heated oxygen sensor connector bracket bolt | 8 - 12 | 80 - 120 | 5.8 - 8.7 |
| Fuel pressure regulator installation bolt | 4 - 6 | 40 - 60 | 2.9 - 4.4 |
| High pressure hose and fuel main pipe | 30 - 40 | 300 - 400 | 22 - 29 |
| High pressure hose and fuel filter | 25 - 35 | 250 - 350 | 18 - 25 |
| High pressure hose to delivery pipe | 3 - 4 | 30 - 40 | 2.2 - 3 |
| Fuel pump assembly to fuel tank | 2 - 3 | 20 - 30 | 1.4 - 2.2 |
| High pressure hose at fuel tank | 30 - 40 | 300 - 400 | 22 - 29 |
| Throttle body to surge tank | 15 - 20 | 150 - 200 | 11 - 14 |
| Accelerator arm bracket bolts | 8 - 12 | 80 - 120 | 5.8 - 8.7 |
| ISC actuator | 6 - 8 | 60 - 80 | 4.4 - 5.8 |
| Fuel sender to fuel tank | 2 - 3 | 20 - 30 | 1.4 - 2.2 |

---

### Special Tools

<!-- EFA90050 -->

| Tool (Number and name) | Use |
|---|---|
| 09353-38000 — Fuel pressure gauge adapter | Connection of fuel pressure gauge to delivery pipe for measurement of fuel pressure. |
| 09353-24100 — Fuel pressure gauge & hose | |

<!-- Figure: Fuel pressure gauge adapter illustration, source: FLA.pdf page 4 -->
<!-- Figure: Fuel pressure gauge & hose illustration, source: FLA.pdf page 4 -->

---

### Troubleshooting

<!-- EFA90060 -->

When troubleshooting an engine, it is important to start with an inspection of the basic systems. If one of the following conditions exists: (A) engine start failure, (B) unstable idling or (C) poor acceleration, begin by checking the following basic systems.

1. Power supply
   - Battery
   - Fusible link
   - Fuse

2. Body ground

3. Fuel supply
   - Fuel line
   - Fuel filter
   - Fuel pump

4. Ignition system
   - Spark plug
   - High-tension cable
   - Ignition coil

5. Emission control system
   - PCV system
   - Vacuum leak

6. Others
   - Ignition timing
   - Idle speed

Malfunctions in the MFI system are often caused by poor connections in the harness connectors. It is important to check all harness connectors and verify that they are securely connected.
