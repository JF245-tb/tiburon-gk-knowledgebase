---
title: Siemens ECM Connector Pinouts
source: OpenGK wiki
source_urls:
  - https://opengk.org/index.php?title=Siemens_5WY_2_Connector_Pinout
  - https://opengk.org/index.php?title=Siemens_5WY_5_Connector_Pinout
chapter: ECM Pinouts
extraction_method: web_fetch
extraction_date: 2026-03-07
verification_status: spot_checked
verified_fields: 4
total_fields: 78
last_verified: 2026-03-12
---

# Siemens ECM Connector Pinouts
**Source:** https://opengk.org/index.php?title=Siemens_5WY_2_Connector_Pinout & Siemens_5WY_5_Connector_Pinout

---

## 5WY 2 Connector (81-pin, used on 2.0L L4)

### SIMK41 2MBit (MAP-based)

| Pin | Type | Function | V |
|-----|------|----------|---|
| 1-2 | GND | Ground | ⬜ |
| 3 | Input | Memory Power Supply (ECM Fuse) | ⬜ |
| 4 | Output | Ignition Coil #1 & #4 | ⬜ |
| 5 | Output | Ignition Coil #2 & #3 | ⬜ |
| 6-7 | I/O | CAN Bus Low/High | ⬜ |
| 8-9 | Output | O2 Heater (B1/S1, B1/S2) | ⬜ |
| 10 | Input | Knock Sensor Signal | ⬜ |
| 14, 21 | Input | Battery (SNSR Fuse) | ⬜ |
| 17-18 | Input | Wheel Speed Sensor (RF) | ⬜ |
| 22 | Input | On/Start Input | ⬜ |
| 23-24 | Output | Injector #4 & #1 | ⬜ |
| 25 | Output | Canister Purge Valve | ⬜ |
| 27 | GND | CKP Sensor Ground | ⬜ |
| 29 | Input | CKP Sensor Signal | ⬜ |
| 30 | GND | Knock/CMP Shared Ground | ⬜ |
| 31 | Input | ECT (Coolant Temp) | ⬜ |
| 32 | Input | TPS Signal | ⬜ |
| 33 | Input | Fuel Tank Pressure Signal | ⬜ |
| 34, 38 | GND | Fuel Tank/TPS Grounds | ⬜ |
| 39 | Input | Vehicle Speed | ⬜ |
| 42-43 | Input | O2 Signals (B1/S2, B1/S1) | ⬜ |
| 44 | Output | Fuel Tank Pressure & MAP Power | ⬜ |
| 45 | Output | TPS Power (5V) | ⬜ |
| 47 | I/O | Immobilizer W-Line | ⬜ |
| 48 | GND | MAP Ground | ⬜ |
| 50 | Input | AC Signal | ⬜ |
| 51 | Input | AC Pressure Switch | ⬜ |
| 55 | GND | Ignition Coil Shield Ground | ⬜ |
| 56 | Input | IAT Signal | ⬜ |
| 58 | Input | AC Switch On | ⬜ |
| 59 | GND | O2/ECT Shared Ground | ⬜ |
| 60 | Input | MAP Signal | ⬜ |
| 61-62 | Output | Injector #3 & #2 | ⬜ |
| 64-65 | Output | Fan Relay (High/Low) | ⬜ |
| 66 | Output | Engine RPM Signal | ⬜ |
| 67 | Input | Main Relay Control | ⬜ |
| 68 | Output | AC Relay | ⬜ |
| 69 | Output | Fuel Pump Relay | ⬜ |
| 70 | Output | MIL (Check Engine Light) | ⬜ |
| 72 | Input | CMP Sensor Signal | ⬜ |
| 75 | Output | Fuel Consumption Signal | ⬜ |
| 76 | I/O | K-Line (OBD2 Diagnostics) | ⬜ |
| 78 | Output | IACV Close | ⬜ |
| 79 | Output | CCV Control | ⬜ |
| 80 | Output | IACV Open | ⬜ |
| 81 | Output | Immobilizer Indicator | ⬜ |

### SIMK43 4MBit (MAF-based) — Key Differences from SIMK41
- Pin 11: CVVT Oil Control Valve output
- Pin 30: CMP Sensor Ground (separate, not shared)
- Pin 37, 48: O2/MAF Sensor Grounds (separate)
- Pin 52: Oil Temperature Sensor Signal
- Pin 54: Knock Sensor Ground
- Pin 60: MAF Signal (replaces MAP)
- Pin 73: ECT Ground (separate)
- Pin 76: Oil Temp Sensor Ground

**⚠️ WARNING: SIMK41 and SIMK43 pinouts are DIFFERENT! Using the wrong ECM/harness will cause damage!**

---

## 5WY 5 Connector (Multi-connector, used on 2.7L V6)

### C133-1: Voltage Supply (9-pin)
| Pin | AWG | Function | V |
|-----|-----|----------|---|
| 1 | 20 | Ignition switch signal input | ⬜ |
| 2-3 | 20 | Diagnostic / K-Line | ⬜ |
| 4 | 14 | ECM ground | ⬜ |
| 5-6 | 14 | Power stage ground | ⬜ |
| 7 | 20 | Battery voltage supply | ⬜ |
| 8-9 | 14 | Battery voltage post-relay | ⬜ |

### C133-2: Peripherals (24-pin)
| Pin | AWG | Function | V |
|-----|-----|----------|---|
| 1, 7, 13, 19 | 20 | Heated O2 sensor heater outputs | ⬜ |
| 14-18 | 20 | O2 sensor inputs (various banks) | ⬜ |
| 17 | 20 | Fuel consumption signal output | ⬜ |
| 20-24 | 20 | O2 sensor grounds | ⬜ |
| 23 | 20 | Main relay control | ⬜ |

### C133-3: Engine (52-pin)
| Pin | AWG | Function | V |
|-----|-----|----------|---|
| 1 | 20 | MAF sensor input | ✅ |
| 8 | 20 | CKP sensor input | ✅ |
| 10 | 20 | TPS 5V supply output | ⬜ |
| 19 | 20 | TPS input | ✅ |
| 22, 24 | 20 | Temperature sensor outputs | ⬜ |
| 26, 29-32 | 20 | Knock sensor inputs/grounds | ⬜ |
| 33-38 | 20 | Fuel injector outputs (cyl 1-6) | ⬜ |
| 42 | 20 | Purge control solenoid PWM | ⬜ |
| 45-47, 52 | 20 | Intake manifold & ISC outputs | ⬜ |

### C133-4: Vehicle (40-pin)
| Pin | AWG | Function | V |
|-----|-----|----------|---|
| 4 | 20 | Fuel tank pressure sensor supply | ⬜ |
| 7 | 20 | CMP sensor input | 🔧 |
| 10 | 20 | Fuel pump relay output | ⬜ |
| 13 | 20 | TPS PWM output | ⬜ |
| 17 | 20 | Engine speed signal output | ⬜ |
| 18, 40 | 20 | Cooling fan relays | ⬜ |
| 23-25 | 20 | AC switch inputs | ⬜ |
| 29 | 20 | AC compressor relay output | ⬜ |
| 36-37 | 20 | CAN bus high/low | ⬜ |
| 39 | 20 | Wheel speed sensor input | ⬜ |

### C133-5: Ignition (9-pin)
| Pin | AWG | Function | V |
|-----|-----|----------|---|
| 1-3 | 14 | Ignition coil outputs | ⬜ |
| 5 | 16 | Ignition coil shield ground | ⬜ |
