---
source: SD.pdf
chapter: SD
section: SD-10 to SD-17
pages: 10-17
title: Power Distribution
---

# Power Distribution

**SD-10 -- Power Distribution (1) -- Battery to E/R Box Fusible Links**
**SD-11 -- Power Distribution (2) -- Ignition Switch to BCM Fuse Box**
**SD-12 -- Power Distribution (3) -- BCM Fuse Box to Body Modules**
**SD-13 -- Power Distribution (4) -- E/R Box to Ignition Coils (2.7L)**
**SD-14 -- Power Distribution (5) -- E/R Box to Fuel Injectors and Sensors (2.7L Bank 1)**
**SD-15 -- Power Distribution (6) -- E/R Box to Fuel Injectors and Sensors (2.7L Bank 2)**
**SD-16 -- Power Distribution (7) -- E/R Box to Fuel Injectors and Sensors (2.0L / 1.6L)**
**SD-17 -- Power Distribution (8) -- BCM Box to Passenger Fuse Outputs**

---

## Power Distribution (1) -- SD-10

### Circuit Path: Battery to E/R Box

```
Battery (+) → [R, 20B] → Generator B terminal (E28)
Battery (+) → [R, 8.0B] → E/R Box Fusible Links:
  → BATT 100A (FL) → Generator
  → BATT 50A (FL) → Generator
  → COND 30A (FL) → Condenser fan relay
  → RAD 30A (FL) → Radiator fan relay
  → BLOW 30A (FL) → Blower relay
  → ECM 30A (FL) → Engine control relay
  → IGN 30A (FL) → Ignition switch feed
  → ABS1 30A (FL) → ABS module
  → ABS2 30A (FL) → ABS module
```

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Battery (+) | E28 | -- | R | 20B |
| Generator | E28 | B | R | 20B |
| Battery ground | -- | -- | B | 20B |
| Battery ground cable | -- | -- | B | 8.0B |
| Fusible link (BATT 100A) | -- | -- | R | 8.0B |
| Fusible link (BATT 50A) | -- | -- | R | 5.0B |
| E/R Box | EC01 (2.0L) | -- | -- | -- |
| E/R Box | EC102 (2.7L) | -- | -- | -- |
| E/R Box | EC202 (1.6L) | -- | -- | -- |

### Lower Bus Bar

```
E/R Box bus → [R, 2.0RB] → E28 (Generator)
E/R Box bus → [R, 2.0RB] → E56 (Joint connector)
E/R Box bus → [R, 0.5C] → EC01/EC102/EC202
```

### Ground Path

```
Battery (-) → [B, 20B] → Battery ground (chassis)
Battery (-) → [B, 8.0B] → Engine block ground
```

---

## Power Distribution (2) -- SD-11

### Circuit Path: E/R Box to Ignition Switch to BCM Fuse Box

```
E/R Box (IGN 30A fusible link) → [R, 5.0B] → E/R Box bus
  → [R, 2.0R] → EM01 (Joint connector)
  → [R, 2.0R] → Ignition switch (M04)
```

### Ignition Switch Output Positions

| Position | Output Wire | Size | Destination |
|----------|-------------|------|-------------|
| BATT (B) | R | 2.0B | Direct battery (always hot) |
| ACC | R/B | 2.0B | Accessory circuits |
| IGN1 (IG1) | Y/R | 2.0B | ECM, fuel system, ignition |
| IGN2 (IG2) | Y/B | 2.0B | BCM, body electronics |
| START (ST) | R/B | 1.25B | Start relay, clutch/range switch |

### BCM Fuse Box Feed

```
Ignition switch (IG1) → [Y/R, 2.0B] → BCM-LR → Fusing Station
Ignition switch (IG2) → [Y/B, 2.0B] → BCM-LR → Fusing Station

To: Passenger Compartment Fuse Outlets
  → FUSE 1 → FUSE 2 → FUSE 3 → FUSE 4 → FUSE 5 → FUSE 6
  → FUSE 7 → FUSE 8 → FUSE 9 → FUSE 10 → FUSE 11 → FUSE 12
  → FUSE 13 → FUSE 14 → FUSE 15 → FUSE 16 → FUSE 17 → FUSE 18
  → FUSE 19 → FUSE 20 → FUSE 21 → FUSE 22 → FUSE 23 → FUSE 24
  → FUSE 25 → FUSE 26 → FUSE 27
```

---

## Power Distribution (3) -- SD-12

### Circuit Path: BCM Box to Body Module Relays

```
BCM Box fuse outputs →
  → Blower relay
  → Defogger relay
  → Headlamp relay (Hi)
  → Headlamp relay (Lo)
  → Door lock relay
  → Door unlock relay
  → Window relay
  → A/C relay
  → Start relay
  → Wiper relay
```

### Component Table

| Component | Connector | Wire Color | Wire Size |
|-----------|-----------|------------|-----------|
| Blower relay | E40 | -- | 2.0B |
| Defogger relay | -- | -- | 1.25B |
| A/C relay | E56 | -- | 0.85S |
| Headlamp relay (Hi) | -- | -- | 1.25B |
| Headlamp relay (Lo) | -- | -- | 1.25B |
| ABS module | E37 | -- | 2.0B |
| ECM relay | E42 | -- | -- |
| Power window relay | -- | -- | 2.0B |
| BCM box (BCM-LR) | -- | -- | -- |

---

## Power Distribution (4) -- SD-13

### Circuit Path: E/R Box to Ignition Coils (2.7L V6)

```
E/R Box (ECM 30A FL) → Engine control relay (E42)
  → [Y/R, 2.0R] → EC102 (2.7L bus)
  → splits to:
    → [Y/R, 1.25B] → Ignition coil #1 (C136-1)
    → [Y/R, 1.25B] → Ignition coil #2
    → [Y/R, 1.25B] → Ignition coil #3
    → [Y/R, 1.25B] → Ignition coil #4
    → [Y/R, 1.25B] → Ignition coil #5
    → [Y/R, 1.25B] → Ignition coil #6
```

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Engine control relay | E42 | -- | Y/R | 2.0B |
| Condenser fan relay | -- | -- | -- | 2.0B |
| Radiator fan relay | -- | -- | -- | 2.0B |
| EC102 (2.7L) bus | EC102 | -- | Y/R | 2.0R |
| Ignition coil #1 | C136-1 | -- | Y/R | 1.25B |
| ECM (2.7L) | C133-1 | -- | -- | 0.5C |
| Condenser (#1) | -- | -- | -- | -- |

### Circuit Path to ECM and Condenser

```
E/R Box → ECM 30A FL → [Y/R] → ECM (C133-1)
E/R Box → COND 30A FL → Condenser fan motor
```

---

## Power Distribution (5) -- SD-14

### Circuit Path: ECM Relay to Injectors and Sensors (2.7L Bank 1)

```
Engine control relay (E42) →
  → [R, 5.0B] → E/R fuse box bus
  → E/R fuse INJ (15A) → [Y/R, 1.25B] → Joint connector (E56)
    → Injector #1 (C204-1)
    → Injector #3 (C204-3)
    → Injector #5 (C204-5)

  → E/R fuse SNSR (15A) → [Y/B] → Joint connector (E56)
    → Camshaft position sensor (C214)
    → Crankshaft position sensor (C216)
    → Oxygen sensor (C218 / Bank 1)
    → EGR (C213)
```

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| INJ fuse (15A) | -- | -- | Y/R | 1.25B |
| SNSR fuse (15A) | -- | -- | Y/B | -- |
| Joint connector | E56 | -- | -- | -- |
| Injector #1 | C204-1 | -- | Y/R | 0.85S |
| Injector #3 | C204-3 | -- | Y/R | 0.85S |
| Injector #5 | C204-5 | -- | Y/R | 0.85S |
| Canister purge valve | C215 | -- | Y/R | 0.5C |
| Power steering pressure switch | -- | -- | -- | 0.5C |
| Crankshaft position sensor | C216 | -- | Y/B | 0.5C |
| Oxygen sensor (Bank 1) | C218 | -- | -- | 0.5C |
| EGR valve | C213 | -- | -- | 0.5C |
| ECM | C133-1 | -- | -- | -- |

---

## Power Distribution (6) -- SD-15

### Circuit Path: ECM Relay to Injectors and Sensors (2.7L Bank 2)

```
Engine control relay (E42) →
  → E/R fuse INJ (15A) → [Y/R, 1.25B] → Joint connector
    → Injector #2 (C204-2)
    → Injector #4 (C204-4)
    → Injector #6 (C204-6)

  → E/R fuse SNSR (15A) →
    → Camshaft position sensor (Bank 2)
    → Oxygen sensor (C148 / Bank 2, upstream OBD1)
    → Oxygen sensor (C148 / Bank 2, downstream OBD2)
    → ETV (Electronic throttle)
    → CKPS (Exterior)
```

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Injector #2 | C204-2 | -- | Y/R | 0.85S |
| Injector #4 | C204-4 | -- | Y/R | 0.85S |
| Injector #6 | C204-6 | -- | Y/R | 0.85S |
| Oxygen sensor (Bank 2, upstream) | C148 | -- | -- | 0.5C |
| Oxygen sensor (Bank 2, downstream) | C148 | -- | -- | 0.5C |
| Camshaft position sensor (Bank 2) | -- | -- | -- | 0.5C |
| Joint connector | C140E | -- | -- | -- |
| CKPS (exterior) | C148 | -- | -- | 0.5C |

---

## Power Distribution (7) -- SD-16

### Circuit Path: E/R Box to Injectors and Sensors (2.0L / 1.6L)

```
Engine control relay →
  → E/R fuse INJ (15A) → [Y/R]
    → Injector #1 (C204-1)
    → Injector #2 (C204-2)
    → Injector #3 (C204-3)
    → Injector #4 (C204-4)

  → E/R fuse SNSR (15A) →
    → Idle speed actuator (C206)
    → Camshaft position sensor
    → Crankshaft position sensor
    → Oxygen sensor
    → Coolant temperature sensor (ECT)
```

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Injector #1 | C204-1 | -- | Y/R | 0.85S |
| Injector #2 | C204-2 | -- | Y/R | 0.85S |
| Injector #3 | C204-3 | -- | Y/R | 0.85S |
| Injector #4 | C204-4 | -- | Y/R | 0.85S |
| Idle speed control actuator | C206 | -- | -- | 0.5C |
| Camshaft position sensor | -- | -- | -- | 0.5C |
| Crankshaft position sensor | -- | -- | -- | 0.5C |
| Purge control solenoid valve | -- | -- | -- | 0.5C |
| Coolant temperature sensor (LPI) | C216 | -- | -- | 0.5C |
| Joint connector | C240E | -- | -- | -- |

---

## Power Distribution (8) -- SD-17

### Circuit Path: BCM Box to Passenger Fuse Outputs

```
Battery (+) → BATT FL (E/R) → [R] → BCM Box direct feed:
  → Door lock relay → FUSE 19 (30A) → Power windows
  → Defogger relay → FUSE 12 (30A) → Rear defogger
  → Washer/heater relay

Ignition switch (IG1) → BCM-OF →
  → FUSE 1 (20A) → Ignition coil (2.7L)
  → FUSE 16 (10A) → ECM, TCM, VSS
  → FUSE 17 (10A) → Instrument cluster (power)

Ignition switch (IG2) → BCM-OF →
  → FUSE 5 (15A) → A/C control module
  → FUSE 6 (15A) → Mirror defogger
  → FUSE 10 (20A) → Wiper motor
```

### Component Table

| Component | Connector | Wire Color | Wire Size |
|-----------|-----------|------------|-----------|
| BCM-OF | -- | -- | 2.0B |
| Washer motor | M01 | -- | 0.85S |
| Relay (window) | -- | -- | 2.0B |
| Rear window defogger | -- | -- | 2.0B |
| Blower motor relay | -- | -- | 2.0B |

---

## Ground Points

| Ground ID | Location | Wire Size |
|-----------|----------|-----------|
| Battery ground (E/R) | Engine block | 20B |
| Battery ground (chassis) | Front chassis | 8.0B |

---

## Notes

- Power distribution (1) through (3) trace the main battery feed through the E/R box fusible links, through the ignition switch, and into the BCM passenger fuse box.
- Power distribution (4) through (7) show the engine control relay feeding the fuel injectors, ignition coils, and engine sensors for each engine variant (2.7L V6, 2.0L I4, 1.6L I4).
- Power distribution (8) shows the BCM box relay outputs to passenger comfort circuits.
- The 2.7L V6 uses connectors EC102 and C133-1/C136-3 for the engine compartment bus.
- The 2.0L uses EC01 and C33 for the engine compartment bus.
- The 1.6L uses EC202 and C233 for the engine compartment bus.
