---
source: SD.pdf
chapter: SD
section: SD-208 to SD-212
pages: 208-212
title: Blower and AC Controls (Automatic)
---

# Blower and AC Controls (Automatic)

**SD-208 -- Blower and A/C Controls (Automatic) (1) Schematic**
**SD-209 -- Blower and A/C Controls (Automatic) (2) Schematic**
**SD-210 -- Blower and A/C Controls (Automatic) (3) Schematic**
**SD-211 -- Blower and A/C Controls (Automatic) (4) Schematic**
**SD-212 -- Component Location Index**

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fusible link (HOT AT ALL TIMES) | -- | -- | R | 3.0W |
| Fuse 11 (HOT AT ALL TIMES) | -- | -- | R | 2.0B |
| Fuse 12 (HOT IN ON OR START) | -- | -- | R/Y | 2.0B |
| Fuse 15 (HOT AT ALL TIMES) | -- | -- | R | 2.0B |
| Blower relay (S1) | coil 85 | -- | G/B | 0.85S |
| Blower relay (S1) | coil 86 | -- | B | 0.85S |
| Blower relay (S1) | contact 30 | -- | R | 3.0W |
| Blower relay (S1) | contact 87 | -- | L/R | 3.0W |
| Blower motor (S3) | (+) | -- | L/R | 3.0W |
| Blower motor (S3) | (-) | -- | B | 2.0B |
| Power transistor (S4) | base | -- | -- | 0.85S |
| Power transistor (S4) | collector | -- | L/R | 3.0W |
| Power transistor (S4) | emitter | -- | B | 2.0B |
| A/C control module (M19-1) | -- | -- | -- | -- |
| A/C control module (M19-2) | -- | -- | -- | -- |
| Photo sensor (E72) | -- | -- | -- | 0.5S |
| Ambient temperature sensor (E73) | -- | -- | -- | 0.5S |
| In-car temperature sensor | -- | -- | -- | 0.5S |
| Humidity sensor (M50) | -- | -- | -- | 0.5S |
| Intake actuator (S3) | -- | -- | -- | 0.5S |
| Temperature actuator (S5) | -- | -- | -- | 0.5S |
| Blend door actuator (S6) | -- | -- | -- | 0.5S |
| Thermostatic switch (S7) | -- | -- | -- | 0.5S |
| A/C relay | coil | -- | -- | 0.85S |
| A/C relay | contact 30 | -- | R/Y | 2.0B |
| A/C relay | contact 87 | -- | -- | 0.85S |
| A/C compressor (2.0L: C24 / 2.7L: C124 / 1.6L: C224) | clutch | -- | Br/B | 1.0B |
| A/C pressure switch (2.0L: E25 / 2.7L: E26) | low | -- | R/B | 0.5S |
| A/C pressure switch | medium | -- | G/R | 0.5S |
| A/C pressure switch | high | -- | Br | 0.5S |
| ECM (2.0L: C33 / 2.7L: C133-4 / 1.6L: C233) | A/C request | -- | G/B | 0.5S |
| BCM-LR | -- | -- | -- | -- |
| BCM-IR | -- | -- | -- | -- |
| BCM-CS | -- | -- | -- | -- |

---

## Circuit Paths

### Blower Motor Power Circuit (Automatic Speed Control)
<!-- Figure: Power transistor-controlled blower speed, source: SD.pdf page 208 -->
```
Fusible link (HOT AT ALL TIMES) → [R, 3.0W] → Joint connector
  → Blower relay S1 (contact 30) → [R, 3.0W]
  → Blower relay S1 (contact 87) → [L/R, 3.0W]
  → Power transistor S4 (collector)
  → Power transistor S4 (emitter) → Blower motor S3 (+)
  → Blower motor S3 (-) → [B, 2.0B] → GND (G11)
```

### Blower Relay Coil Circuit
```
IGN switch ON → Fuse 12 → [R/Y, 2.0B]
  → A/C control module M19-1 (blower relay drive output)
  → [G/B, 0.85S] → Blower relay S1 (coil 85)
  → Blower relay S1 (coil 86) → [B, 0.85S] → GND
```

### Power Transistor Speed Control
<!-- Figure: A/C control module drives power transistor base for variable blower speed, source: SD.pdf page 208 -->
```
A/C control module M19-1 → [0.85S] → Power transistor S4 (base)
  A/C control module varies base current to control blower speed continuously
  (No discrete speed steps — infinite variation from LO to HI)
  The function of the power transistor is that of the blower resistor in manual A/C
```

### A/C Control Module Power Supply
```
Fuse 11 (HOT AT ALL TIMES) → [R, 2.0B] → BCM-CS → A/C control module M19-1 (B+ keep-alive)
Fuse 12 (HOT IN ON OR START) → [R/Y, 2.0B] → A/C control module M19-1 (IGN power)
```

### Sensor Inputs to A/C Control Module (SD-208 / SD-210)
<!-- Figure: Temperature and environmental sensor inputs, source: SD.pdf page 208 -->
```
Photo sensor E72 → [0.5S] → A/C control module M19-1 (sunload input)
Ambient temperature sensor E73 → [0.5S] → A/C control module M19-1 (ambient temp)
In-car temperature sensor → [0.5S] → A/C control module M19-1 (cabin temp)
Humidity sensor M50 → [0.5S] → A/C control module M19-1 (humidity input)
```

### A/C Switch / Request to ECM
<!-- Figure: A/C request from control module to ECM, source: SD.pdf page 210 -->
```
A/C control module M19-1 (A/C request output) → [G/B, 0.5S]
  → ECM C33/C133-4/C233 (A/C request input)
  ECM evaluates conditions → drives A/C relay coil
```

### A/C Compressor Clutch Circuit
<!-- Figure: A/C relay and compressor, source: SD.pdf page 211 -->
```
Fuse 12 (HOT IN ON OR START) → [R/Y, 2.0B] → A/C relay (contact 30)
  → A/C relay (contact 87) → [Br/B, 1.0B]
  → A/C compressor clutch C24/C124/C224 → [B, 0.85S] → GND
```

### A/C Relay Coil Circuit
```
From A/C compressor relay control:
  ECM (A/C relay output) → A/C relay (coil 85)
  → A/C relay (coil 86) → [B, 0.85S] → GND
```

### A/C Pressure Switch (Triple Switch) Circuit
<!-- Figure: Triple pressure switch to ECM, source: SD.pdf page 211 -->
```
A/C pressure switch E25/E26:
  Low pressure → [R/B, 0.5S] → ECM (low-pressure cutoff)
  Medium pressure → [G/R, 0.5S] → ECM (condenser fan speed)
  High pressure → [Br, 0.5S] → ECM (compressor cutoff / high-speed fan)
```

### HVAC Door Actuators (SD-209 / SD-210)
<!-- Figure: Mode/blend/temp door actuator control, source: SD.pdf page 209 -->
```
A/C control module M19-2 → Intake actuator S3
  → [0.5S] → Multiple wires for intake (recirc/fresh) position

A/C control module M19-2 → Temperature actuator S5
  → [0.5S] → Multiple wires for temp door position

A/C control module M19-2 → Blend door actuator S6
  → [0.5S] → Multiple wires for blend door position

Actuator feedback signals → A/C control module M19-2
  (potentiometer position signals for closed-loop control)
```

### Rear Window & Outside Mirror Defogger (SD-209)
<!-- Figure: Defogger relay through A/C control module, source: SD.pdf page 209 -->
```
Fuse 15 (HOT AT ALL TIMES) → Blower relay → Joint connector
  → A/C control module M19-1 → Defogger relay control
  → Rear window defogger + Outside mirror heater
  → GND (G11)
```

### Illumination Feed (SD-210)
```
See Illuminations schematic → [G, 0.5S] → A/C control module M19-1 (illumination input)
```

### Transaxle Signal (SD-210)
<!-- Figure: To transaxle module for idle-up coordination, source: SD.pdf page 210 -->
```
A/C control module M19-1 → [0.5S] → To Traxle Switch
  (Coordinates A/C load signal for idle speed adjustment)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G11 | Dash area | Blower motor ground, A/C control module ground | CL-33 |
| G12 | Dash area | Actuator grounds, sensor grounds | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-CE | Body Control Module | CL-14 |
| BCM-M | Body Control Module | CL-8 |
| BCM-KM | Body Control Module | CL-8 |
| BCM-LR | Body Control Module | CL-8 |
| BCM-IR | Body Control Module | CL-8 |
| BCM-CS | Body Control Module | CL-8 |
| EC01 | Engine compartment | CL-14 |
| EC101 | Engine compartment | CL-14 |
| EC201 | Engine compartment | CL-14 |
| EM01 | Engine compartment | CL-14 |
| MC101 | Multifunction switch | CL-14 |
| MC03 | Multifunction switch | CL-8 |
| MR03 | Rear connector | CL-9 |
| MM01 | Mirror connector | CL-9 |

---

## Component Location Index (SD-212)

### Components

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C24 | A/C compressor (2.0L) | CL-20 |
| C33 | ECM (2.0L) | CL-24 |
| C133-4 | ECM (2.7L) | CL-25 |
| C200 | A/C compressor (1.6L) | CL-23 |
| E25 | Triple switch (2.0L/1.6L) | CL-11 |
| E26 | Triple switch (2.7L) | CL-11 |
| E56 | Joint connector | CL-12 |
| E72 | Photo sensor | CL-17 |
| E73 | Ambient temperature sensor | CL-17 |
| S1 | Blower relay | CL-17 |
| S3 | Intake actuator | CL-17 |
| S4 | Power transistor | CL-17 |
| S5 | Temperature actuator | CL-17 |
| S6 | Blend door actuator | CL-17 |
| S7 | Thermostatic switch | CL-17 |
| M19-1 | A/C control module | CL-3 |
| M19-2 | A/C control module | CL-3 |
| M35 | Joint connector | CL-4 |
| M45 | Joint connector | CL-4 |
| M50 | Humidity sensor | CL-7 |

### Connectors

| Connector | Location Page |
|-----------|---------------|
| BCM-CE | CL-14 |
| BCM-M | CL-8 |
| BCM-KM | CL-8 |
| BCM-LR | CL-8 |
| EC01 | CL-14 |
| EC101 | CL-14 |
| EM01 | CL-14 |
| MC101 | CL-14 |
| MC03 | CL-8 |
| MR03 | CL-9 |
| MM01 | CL-9 |
| MR06 | CL-9 |

### Grounds

| Ground ID | Location Page |
|-----------|---------------|
| G11 | CL-33 |
| G12 | CL-33 |

---

## Notes

### Automatic A/C Overview
- The A/C control module receives inputs from the A/C sensors (in-car temperature, photo sensor, thermostatic switch, humidity sensor, ambient sensor, etc.) and controls the function of the air conditioning system.
- The A/C control module and various sensors provide accurate control of the air mixture using blend door actuator, temperature actuator, and intake actuator under all operating conditions.
- The function of the power transistor is that of the blower resistor in manual A/C.

### Blower Speed Control (Auto vs Manual)
- In automatic mode, the A/C control module drives the power transistor base signal to continuously vary blower motor speed (no discrete steps).
- The power transistor replaces the blower resistor used in the manual system.
- The A/C control module determines the optimal blower speed based on the difference between set temperature and cabin temperature, sunload, and ambient temperature.

### Sensor Functions
- **Photo sensor (E72):** Measures sunlight intensity (sunload) for automatic temperature compensation.
- **Ambient temperature sensor (E73):** Measures outside air temperature.
- **In-car temperature sensor:** Measures cabin air temperature.
- **Humidity sensor (M50):** Measures cabin humidity for defog/dehumidification control.
- **Thermostatic switch (S7):** Monitors evaporator temperature to prevent freeze-up.

### Differences from Manual A/C
- Automatic system uses power transistor (S4) instead of blower resistor (S2) for stepless speed control.
- Automatic system has additional sensor inputs (photo, ambient, in-car temp, humidity).
- Automatic system uses A/C control module (M19-1/M19-2) with two connectors instead of simple switch panel (M20).
- Door actuators have feedback potentiometers for closed-loop position control.
- Blower relay coil is driven by the A/C control module rather than a manual blower switch.
