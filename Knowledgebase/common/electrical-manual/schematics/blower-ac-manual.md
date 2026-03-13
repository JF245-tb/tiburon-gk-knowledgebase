---
source: SD.pdf
chapter: SD
section: SD-204 to SD-207
pages: 204-207
title: Blower and AC Controls (Manual)
---

# Blower and AC Controls (Manual)

**SD-204 -- Blower and A/C Controls (Manual) (1) Schematic**
**SD-205 -- Blower and A/C Controls (Manual) (2) Schematic**
**SD-206 -- Blower and A/C Controls (Manual) (3) Schematic**
**SD-207 -- Component Location Index**

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fusible link (HOT AT ALL TIMES) | -- | -- | R | 3.0W |
| Fuse 15 (HOT AT ALL TIMES) | -- | -- | R | 2.0B |
| Fuse 12 (HOT IN ON OR START) | -- | -- | R/Y | 2.0B |
| Blower relay (S1) | coil 85 | -- | G/B | 0.85S |
| Blower relay (S1) | coil 86 | -- | B | 0.85S |
| Blower relay (S1) | contact 30 | -- | R | 3.0W |
| Blower relay (S1) | contact 87 | -- | L/R | 3.0W |
| Blower resistor (S2) | -- | -- | -- | -- |
| Blower motor (S3) | (+) | -- | L/R | 3.0W |
| Blower motor (S3) | (-) | -- | B | 2.0B |
| Blower switch (M20) | OFF | -- | -- | -- |
| Blower switch (M20) | 1 (LO) | -- | L/W | 0.85S |
| Blower switch (M20) | 2 | -- | L/R(2) | 0.85S |
| Blower switch (M20) | 3 | -- | L/B | 0.85S |
| Blower switch (M20) | 4 (HI) | -- | L | 0.85S |
| A/C switch (M20) | -- | -- | G/B | 0.5S |
| A/C control module (M20) | illumination | -- | G | 0.5S |
| Power transistor | base | -- | -- | 0.85S |
| Power transistor | collector | -- | L/R | 3.0W |
| Power transistor | emitter | -- | B | 2.0B |
| A/C relay | coil 85 | -- | -- | 0.85S |
| A/C relay | coil 86 | -- | B | 0.85S |
| A/C relay | contact 30 | -- | R/Y | 2.0B |
| A/C relay | contact 87 | -- | -- | 0.85S |
| Thermostat switch | -- | -- | -- | 0.5S |
| A/C compressor (2.0L: C24 / 2.7L: C124 / 1.6L: C224) | clutch | -- | Br/B | 1.0B |
| A/C pressure switch (triple switch) (2.0L: E25 / 2.7L: E26) | low | -- | R/B | 0.5S |
| A/C pressure switch (triple switch) | medium | -- | G/R | 0.5S |
| A/C pressure switch (triple switch) | high | -- | Br | 0.5S |
| ECM (2.0L: C33 / 2.7L: C133-4 / 1.6L: C233) | A/C request | -- | G/B | 0.5S |
| ECM | A/C relay control | -- | -- | 0.85S |
| Temperature actuator (S5) | -- | -- | -- | 0.5S |
| Blend door actuator (S6) | -- | -- | -- | 0.5S |
| Intake actuator (S3 area) | -- | -- | -- | 0.5S |

---

## Circuit Paths

### Blower Motor Power Circuit
<!-- Figure: Blower relay and motor power path with resistor, source: SD.pdf page 204 -->
```
Fusible link (HOT AT ALL TIMES) → [R, 3.0W] → Joint connector
  → Blower relay S1 (contact 30) → [R, 3.0W]
  → Blower relay S1 (contact 87) → [L/R, 3.0W]
  → Blower resistor S2 (speed 1/2/3) or bypass (speed 4)
  → Blower motor S3 (+) → [B, 2.0B] → GND (G11)
```

### Blower Relay Coil Circuit
```
IGN switch ON → Fuse 12 → [R/Y, 2.0B]
  → Blower switch M20 (any ON position: 1, 2, 3, or 4)
  → [G/B, 0.85S] → Blower relay S1 (coil 85)
  → Blower relay S1 (coil 86) → [B, 0.85S] → GND
```

### Blower Speed Control (Resistor Network)
<!-- Figure: Blower switch speed positions through resistor, source: SD.pdf page 204 -->
```
Blower switch position 1 (LO): [L/W, 0.85S] → Blower resistor S2 (full resistance)
  → Blower motor — lowest speed

Blower switch position 2: [L/R(2), 0.85S] → Blower resistor S2 (partial resistance)
  → Blower motor — medium-low speed

Blower switch position 3: [L/B, 0.85S] → Blower resistor S2 (minimal resistance)
  → Blower motor — medium-high speed

Blower switch position 4 (HI): [L, 0.85S] → Bypasses resistor entirely
  → Blower motor — full speed (direct from relay)
```

### A/C Switch Input to ECM
<!-- Figure: A/C switch request to ECM, source: SD.pdf page 206 -->
```
A/C switch M20 (ON) → [G/B, 0.5S] → ECM (A/C request input)
  ECM evaluates conditions (engine running, pressure OK, etc.)
  → ECM drives A/C relay coil → [B, 0.85S] → GND
```

### A/C Compressor Clutch Circuit
<!-- Figure: A/C relay and compressor clutch drive, source: SD.pdf page 206 -->
```
IGN switch ON → Fuse 12 → [R/Y, 2.0B] → A/C relay (contact 30)
  → A/C relay (contact 87) → [Br/B, 1.0B]
  → A/C compressor clutch C24/C124/C224 → [B, 0.85S] → GND
```

### A/C Relay Coil Circuit
```
ECM (A/C relay output) → A/C relay (coil 85)
  → A/C relay (coil 86) → [B, 0.85S] → GND
  ECM grounds the relay coil after a short delay to adjust idle speed
```

### A/C Pressure Switch (Triple Switch) Circuit
<!-- Figure: Triple pressure switch inputs to ECM and relay control, source: SD.pdf page 206 -->
```
A/C pressure switch (triple switch) E25/E26:
  Low pressure switch → [R/B, 0.5S] → ECM
  Medium pressure switch → [G/R, 0.5S] → ECM (condenser fan speed control)
  High pressure switch → [Br, 0.5S] → ECM (compressor cutoff / high-speed fan)
```

### Thermostat Switch Circuit
<!-- Figure: Evaporator thermostat feedback to A/C module, source: SD.pdf page 206 -->
```
Thermostat switch (evaporator temp sensor) → [0.5S]
  → A/C control module M20 (thermostat input)
  Cycles compressor to prevent evaporator freeze-up
```

### Temperature / Blend Door Actuator Circuits (SD-205)
<!-- Figure: HVAC actuator control from A/C control module, source: SD.pdf page 205 -->
```
A/C control module M20 → Temperature actuator S5
  Pins: WARM / COOL / SW-COOL / SW-V/D
  → [0.5S] multiple wires to actuator motor

A/C control module M20 → Blend door actuator S6
  → [0.5S] multiple wires to actuator motor

A/C control module M20 → Intake actuator
  → [0.5S] → Intake door position control

See Rear Window & Outside Mirror Defogger → from Fuse 12
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G11 | Dash area | Blower motor ground, A/C control module ground | CL-33 |
| G12 | Dash area | Temperature/blend door actuator grounds | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-CE | Body Control Module | CL-14 |
| BCM-M | Body Control Module | CL-8 |
| BCM-KM | Body Control Module | CL-8 |
| EC01 | Engine compartment | CL-14 |
| EC101 | Engine compartment | CL-14 |
| EC201 | Engine compartment | CL-14 |
| MC101 | Multifunction switch area | CL-14 |
| MC03 | Multifunction switch | CL-8 |

---

## Component Location Index (SD-207)

### Components

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C24 | A/C compressor (2.0L) | CL-20 |
| C33 | ECM (2.0L) | CL-24 |
| C124 | A/C compressor (2.7L) | CL-22 |
| C133 | ECM (2.7L) | CL-24 |
| C224 | A/C compressor (1.6L) | CL-23 |
| C233 | ECM (1.6L) | CL-24 |
| E25 | Triple switch (2.0L/1.6L) | CL-11 |
| E26 | Triple switch (2.7L) | CL-11 |
| E46 | Joint connector | CL-12 |
| S1 | Blower relay | CL-17 |
| S2 | Blower resistor | CL-17 |
| S3 | Intake actuator | CL-17 |
| S4 | Power transistor | CL-17 |
| S5 | Temperature actuator | CL-17 |
| S6 | Blend door actuator | CL-17 |
| S7 | Thermostatic switch | CL-17 |
| M20 | A/C control module | CL-3 |
| M51 | Blower switch | CL-4 |
| M56 | Joint connector | CL-4 |

### Connectors

| Connector | Location Page |
|-----------|---------------|
| BCM-CE | CL-14 |
| BCM-M | CL-8 |
| BCM-KM | CL-8 |
| EC01 | CL-14 |
| EC101 | CL-14 |
| EC201 | CL-14 |
| EM01 | CL-14 |
| MC101 | CL-14 |
| MC03 | CL-8 |
| MR03 | CL-9 |

### Grounds

| Ground ID | Location Page |
|-----------|---------------|
| G11 | CL-33 |
| G12 | CL-33 |

---

## Notes

### Blower Control
- With the ignition switch in ON and the blower switch in any position except OFF, the blower relay coil energizes and the blower relay contacts close.
- Battery voltage is then applied to the blower motor through the blower resistor and the blower switch.
- As the blower switch is moved from OFF to HI, resistance of the resistor (in the circuit path to the blower motor) will decrease, and battery voltage applied to the blower motor will increase. This will increase the blower motor speed.
- When the blower switch is in HI, all of the resistance is bypassed and the maximum voltage is applied to the blower motor so that it runs at the highest speed.

### A/C Control
- With the ignition switch in ON and the blower switch in any position except OFF, the blower relay coil energizes and the blower relay contacts close.
- Battery voltage is then applied to the blower motor through the blower resistor and the blower switch.
- Battery voltage is applied to the A/C switch through Fuse 15.
- With the A/C switch in ON, the Engine Control Module (ECM) will ground the coil of the A/C relay after a short delay to adjust idle speed.
- Battery voltage will then be applied to the compressor clutch through the closed contacts of the A/C relay. The A/C compressor runs.
- Refer to the shop manual, section HA for details.

### Triple Pressure Switch
- The triple switch monitors A/C refrigerant pressure at three thresholds:
  - Low pressure: disengages compressor clutch (insufficient refrigerant)
  - Medium pressure: activates condenser fan medium speed
  - High pressure: activates condenser fan high speed or cuts compressor off (over-pressure)
