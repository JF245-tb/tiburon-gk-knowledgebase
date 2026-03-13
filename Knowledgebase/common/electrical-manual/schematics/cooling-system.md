---
source: SD.pdf
chapter: SD
section: SD-56 to SD-57
pages: 56-57
title: Cooling System
---

# Cooling System

**SD-56 -- Cooling System (1) Schematic**
**SD-57 -- Component Location Index**

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse/fusible link (HOT AT ALL TIMES) | -- | -- | R | -- |
| ECU fusible link (30A) | -- | -- | R | -- |
| RAD fusible link | -- | -- | R | -- |
| COND fusible link | -- | -- | R | -- |
| Joint connector | E56 | -- | R | -- |
| Engine control relay (E42) | coil | -- | B/W | 0.85S |
| Engine control relay (E42) | contact 30 | -- | R | 2.0B |
| Engine control relay (E42) | contact 87 | -- | B/W | 2.0B |
| Condenser fan relay #1 (E52/E43) | coil | -- | -- | 0.85S |
| Condenser fan relay #1 (E52/E43) | contact 30 | -- | R | 2.0B |
| Condenser fan relay #1 (E52/E43) | contact 87 | -- | -- | 2.0B |
| Condenser fan relay #2 (E43) | coil | -- | -- | 0.85S |
| Condenser fan relay #2 (E43) | contact 30 | -- | R | 2.0B |
| Condenser fan relay #2 (E43) | contact 87 | -- | -- | 2.0B |
| Radiator fan relay (E44) | coil | -- | -- | 0.85S |
| Radiator fan relay (E44) | contact 30 | -- | R | 2.0B |
| Radiator fan relay (E44) | contact 87 | -- | -- | 2.0B |
| Low-speed radiator fan relay | coil | -- | -- | -- |
| Low-speed radiator fan relay | contact | -- | -- | -- |
| Condenser fan motor (E21) | 1 | -- | L | 2.0B |
| Condenser fan motor (E21) | 2 | -- | B | 2.0B |
| Radiator fan motor (E11) | -- | -- | -- | 2.0B |
| Engine coolant temp sensor & sender (2.0L: C11 / 2.7L: C111) | 1 | signal | Br | 0.5S |
| Engine coolant temp sensor & sender (2.0L: C11 / 2.7L: C111) | 2 | ground | B/Y | 0.5S |
| Coolant temperature sensor (C112) | 1 | signal | Y/Br | 0.5L |
| Coolant temperature sensor (C112) | 2 | ground | G/Y(1) | 0.5L |

---

## ECM Connections (Bottom of SD-56)

| ECM Connector | Pin | Signal | Wire Color | Wire Size | Connected To |
|---------------|-----|--------|------------|-----------|-------------|
| C133-2 (2.0L) | -- | ECT sensor | Br | 0.5S | C11 coolant temp sensor |
| C133-4 (2.7L) | -- | ECT sensor | Br | 0.5S | C111 coolant temp sensor |
| C133-2 (2.0L) | -- | sensor ground | B/Y | 0.5S | C11 pin 2 |
| C133-4 (2.7L) | -- | sensor ground | B/Y | 0.5S | C111 pin 2 |
| C392-2 (2.0L) | -- | ECT2 signal | Y/Br | 0.5L | C112 coolant temp sender |
| C392 (2.7L) | -- | ECT2 signal | Y/Br | 0.5L | C112 coolant temp sender |
| -- | -- | ECT2 ground | G/Y(1) | 0.5L | C112 pin 2 |

### ECM Connector Pin Detail (Bottom Row, SD-56)

| Position | ECM Pin | Signal Name | Wire Color | Wire Size |
|----------|---------|-------------|------------|-----------|
| 64 | C392 (2L) | -- | Br | 0.5S |
| 38 | -- | -- | G/R | 0.5Y |
| 50 | -- | -- | B/Y | 0.5S |
| 51 | C392 (2L) | -- | Y/Br | 0.5L |
| -- | -- | -- | 2.0L/W(2) | -- |
| -- | -- | -- | 1.0B/W(2) | -- |
| -- | -- | -- | 0.5/B/O | -- |
| -- | -- | -- | G/Y(1) | 0.5L |

---

## Circuit Paths

### Engine Control Relay Circuit
```
Fusible link (HOT AT ALL TIMES) → [R] → Engine control relay E42 (contact 30)
  → E42 (contact 87) → [B/W, 2.0B] → Fan relay coils power supply
```

### Radiator Fan Circuit (High Speed)
```
RAD fusible link → [R, 2.0B] → Radiator fan relay E44 (contact 30)
  → E44 (contact 87) → [2.0B] → Radiator fan motor E11 → GND
ECM controls → Radiator fan relay E44 coil → [B, 0.85S] → GND (G15)
```

### Condenser Fan Circuit
```
COND fusible link → [R, 2.0B] → Condenser fan relay #1 (contact 30)
  → Condenser fan relay #1 (contact 87) → [L, 2.0B] → Condenser fan motor E21
  → [B, 2.0B] → GND (G14)
```

### Coolant Temperature Sensor to ECM
```
ECT sensor (C111 pin 1) → [Br, 0.5S] → C392 → ECM (C133-4)
ECT sensor (C111 pin 2) → [B/Y, 0.5S] → ECM sensor ground
```

### Coolant Temperature Sender to ECM/Cluster
```
Coolant temp sender (C112 pin 1) → [Y/Br, 0.5L] → C392 → ECM
Coolant temp sender (C112 pin 2) → [G/Y, 0.5L] → ECM sensor ground
```

---

## Ground Points

| Ground ID | Location | Components |
|-----------|----------|------------|
| G14 | Engine compartment | Condenser fan motor ground |
| G15 | Engine compartment | Fan relay coil grounds, ECM-related grounds |

---

## Component Location Index (SD-57)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C11 | Engine coolant temperature sensor & sender (2.0L) | CL-18 |
| C33 | ECM (2.0L) | CL-20 |
| C111 | Engine coolant temperature sensor & sender (2.7L) | CL-22 |
| C133-2 | ECM (2.7L) | CL-25 |
| C133-4 | ECM (2.7L) | CL-25 |
| C211 | Engine coolant temperature sensor & sender (1.6L) | CL-23 |
| C233 | ECM (1.6L) | CL-24 |
| E11 | Radiator fan motor | CL-10 |
| E21 | Condenser fan motor | CL-11 |
| E42 | Engine control relay | CL-12 |
| E43 | Condenser fan relay #2 | CL-12 |
| E44 | Radiator fan relay | CL-12 |
| E52 | Condenser fan relay #1 | CL-12 |
| E56 | Joint connector | CL-12 |

### Connectors

| Connector | Location Page |
|-----------|---------------|
| EC01 | CL-14 |
| EC02 | CL-14 |
| EC101 | CL-14 |
| EC102 | CL-14 |
| EC201 | CL-14 |

### Grounds

| Ground ID | Location Page |
|-----------|---------------|
| G15 | CL-33 |
| G16 | CL-33 |

---

## Notes

- The ECM (Engine Control Module) controls the operation of the radiator fan motor and the condenser fan motor through relay (radiator fan relay and condenser fan relays) control.
- The ECM monitors coolant temperature through the engine coolant temperature sensor.
- The module also monitors A/C operation through the A/C switch ON input and the A/C pressure switch input. Using these input signals, the module controls the coil of the appropriate relays (condenser fan relays and radiator fan relay) to provide optimal cooling fan operation.
- **V6 build note:** For the 2.7L, the coolant temp sensor is C111, ECM connector is C133-4. The condenser fan relay #1 is E52 (same ID as the start solenoid in the starting system section -- context-dependent).
