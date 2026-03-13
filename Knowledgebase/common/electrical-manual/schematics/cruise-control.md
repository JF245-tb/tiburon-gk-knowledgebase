---
source: SD.pdf
chapter: SD
section: SD-200 to SD-203
pages: 200-203
title: Cruise Control System
---

# Cruise Control System

**SD-200 -- Cruise Control System (1) Schematic**
**SD-201 -- Cruise Control System (2) Schematic**
**SD-202 -- Component Location Index**
**SD-203 -- Memo (blank)**

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 16 (HOT IN ON OR START) | -- | -- | R/Y | 0.85S |
| Fuse 17 (IGN/ON) | -- | -- | R/Y | 2.0B |
| Fuse 14 (HOT AT ALL TIMES) | -- | -- | R | 2.0B |
| Fuse 15 (HOT AT ALL TIMES) | -- | -- | R | 2.0B |
| Cruise control main switch (M01-3) | ON | -- | L/R | 0.5S |
| Cruise control main switch (M01-3) | indicator | -- | L/W | 0.5S |
| Multifunction switch (M01-1) | cruise set/coast | -- | L/Y | 0.5S |
| Multifunction switch (M01-1) | cruise resume/accel | -- | L/B | 0.5S |
| Multifunction switch (M01-1) | cruise cancel | -- | L | 0.5S |
| Instrument cluster (M10) | cruise indicator | -- | L/W | 0.5S |
| Cruise control module | main sw input | -- | L/R | 0.5S |
| Cruise control module | set/coast input | -- | L/Y | 0.5S |
| Cruise control module | resume/accel input | -- | L/B | 0.5S |
| Cruise control module | cancel input | -- | L | 0.5S |
| Cruise control module | stop lamp sw input | -- | G/W | 0.5S |
| Cruise control module | VSS input | -- | P/B | 0.5S |
| Cruise control module | actuator vent | -- | Br/W | 0.85S |
| Cruise control module | actuator vacuum | -- | Br/R | 0.85S |
| Cruise control module | actuator release | -- | Br | 0.85S |
| Cruise clutch pedal position switch (M7) | -- | -- | G/W | 0.5S |
| Stop lamp switch (2.0L: C32 / 2.7L: C132) | -- | -- | G/W | 0.5S |
| Vehicle speed sensor | -- | -- | P/B | 0.5S |
| Cruise control actuator | vent solenoid | -- | Br/W | 0.85S |
| Cruise control actuator | vacuum solenoid | -- | Br/R | 0.85S |
| Cruise control actuator | release solenoid | -- | Br | 0.85S |
| TCM (2.0L: C39-1 / 2.7L: C136-1) | cruise input | -- | -- | 0.5S |
| Burglar alarm relay (MA1) | -- | -- | -- | -- |
| BCM-KM | -- | -- | -- | -- |

---

## Circuit Paths

### Cruise Control Power Supply
<!-- Figure: Cruise control module power feed, source: SD.pdf page 200 -->
```
IGN switch ON → Fuse 16 → [R/Y, 0.85S] → Cruise control module (power)
```

### Cruise Main Switch Circuit
<!-- Figure: Main switch input to cruise module, source: SD.pdf page 200 -->
```
IGN switch ON → Fuse 17 → [R/Y, 2.0B] → Multifunction switch M01-3 (cruise main)
  → Cruise control main switch ON → [L/R, 0.5S]
  → Cruise control module (main sw input)
```

### Cruise Indicator Lamp Circuit
```
Cruise control module → [L/W, 0.5S] → Instrument cluster M10 (cruise indicator)
```

### Cruise Control Switch Inputs (Set / Resume / Cancel)
<!-- Figure: Cruise stalk inputs to module through clock spring, source: SD.pdf page 200 -->
```
Multifunction switch M01-1 (set/coast) → [L/Y, 0.5S] → Cruise control module (set/coast)
Multifunction switch M01-1 (resume/accel) → [L/B, 0.5S] → Cruise control module (resume/accel)
Multifunction switch M01-1 (cancel) → [L, 0.5S] → Cruise control module (cancel)
```

### Stop Lamp Switch Input (Cruise Cancel)
```
Fuse 14 (HOT AT ALL TIMES) → [R, 2.0B] → Stop lamp switch C32/C132
  → [G/W, 0.5S] → Cruise control module (stop lamp sw input)
  Brake pedal depressed → opens circuit → cruise cancels
```

### Cruise Clutch Pedal Switch (Manual Transaxle Cancel)
```
Cruise clutch pedal position switch (M7) → [G/W, 0.5S]
  → Cruise control module (clutch input)
  Clutch pedal depressed → opens circuit → cruise cancels
```

### Vehicle Speed Sensor Input
<!-- Figure: VSS feed to cruise module, source: SD.pdf page 200 -->
```
Vehicle speed sensor → [P/B, 0.5S] → Cruise control module (VSS input)
  (See VSS schematic for full sensor circuit)
```

### Cruise Control Actuator Outputs
<!-- Figure: Actuator solenoid drive from cruise module, source: SD.pdf page 201 -->
```
Cruise control module (vent) → [Br/W, 0.85S] → Cruise control actuator (vent solenoid)
Cruise control module (vacuum) → [Br/R, 0.85S] → Cruise control actuator (vacuum solenoid)
Cruise control module (release) → [Br, 0.85S] → Cruise control actuator (release solenoid)
  All solenoid grounds → [B, 0.85S] → GND (G20, G23)
```

### TCM Signal (A/T Only)
<!-- Figure: Cruise to TCM link for shift management, source: SD.pdf page 201 -->
```
Cruise control module → [0.5S] → Joint connector
  → TCM C39-1 (2.0L) / C136-1 (2.7L) (cruise active signal)
  Prevents transaxle from continuously downshifting/upshifting on hills
```

### Cruise Control Module — Stop Lamp / Brake Input (SD-201)
```
Fuse 15 (HOT AT ALL TIMES) → [R, 2.0B] → BCM-KM
  → [G/W, 0.5S] → Stop lamp switch → Cruise control module
  → Also feeds stop lamp circuit (see Starting System for brake interlock)
```

### Motor Driver / Actuator Detail (SD-201)
<!-- Figure: Cruise actuator motor drive circuit and solenoids, source: SD.pdf page 201 -->
```
Fuse 14 → Joint connector → Cruise control actuator power
Cruise control module → Motor driver → Cruise control actuator
  → Vent solenoid: [Br/W, 0.85S]
  → Vacuum solenoid: [Br/R, 0.85S]
  → Release: [Br, 0.85S]
  Actuator ground → [B, 0.85S] → GND (G20)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G20 | Dash area | Cruise control module ground, actuator ground | CL-34 |
| G23 | Dash area | Cruise control actuator ground | CL-34 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-M | Body Control Module | CL-8 |
| BCM-KM | Body Control Module | CL-8 |
| MC01 | Multifunction switch | CL-8 |
| MC03 | Multifunction switch | CL-8 |
| MC101 | Multifunction switch | CL-14 |
| MC103 | Multifunction switch | CL-8 |
| MC203 | Multifunction switch | CL-8 |

---

## Component Location Index (SD-202)

### Components (2.0L)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C32 | Stop lamp switch (2.0L) | CL-20 |
| C35 | Cruise clutch pedal position switch (2.0L) | CL-20 |
| C39-1 | TCM (2.0L) | CL-21 |
| C41 | Joint connector (2.0L) | CL-21 |

### Components (2.7L)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C132 | Stop lamp switch (2.7L) | CL-21 |
| C135 | Cruise clutch pedal position switch (2.7L) | CL-21 |
| C136-1 | TCM (2.7L) | CL-21 |
| C141 | Joint connector (2.7L) | CL-21 |

### Common Components

| Component | Description | Location Page |
|-----------|-------------|---------------|
| M01-3 | Multifunction switch | CL-2 |
| M10-1 | Instrument cluster | CL-2 |
| M56 | Ignition switch | CL-2 |
| MA1 | Burglar alarm relay | CL-4 |

### Connectors

| Connector | Location Page |
|-----------|---------------|
| BCM-M | CL-8 |
| BCM-KM | CL-8 |
| MC01 | CL-8 |
| MC101 | CL-14 |
| MC03 | CL-8 |
| MC103 | CL-8 |
| MC203 | CL-8 |

### Grounds

| Ground ID | Location Page |
|-----------|---------------|
| G20 | CL-34 |
| G23 | CL-34 |

---

## Notes

### System Overview
- The cruise control system uses mechanical and electronic devices to maintain vehicle speed at a driver-selected setting.
- The cruise control module receives signals from the cruise main switch, the stop lamp switch, the cruise control switch (set/coast, resume/accel, cancel), the transaxle range switch (A/T), the cruise clutch pedal position switch (M/T), and the vehicle speed sensor.
- The cruise control module sends signals to the cruise control actuator and the transaxle control module (A/T).

### Cruise Engage / Cancel
- With cruise engaged, the cruise control module sends a signal to the TCM that prevents the transaxle from continuously downshifting and upshifting to maintain the set vehicle speed when going up a long grade or hill.
- The cruise control module incorporates a self-diagnostic feature.

### Cancel Inputs
- Brake pedal depressed (stop lamp switch opens)
- Clutch pedal depressed (cruise clutch pedal switch opens -- M/T only)
- Cruise cancel switch on multifunction stalk
- Vehicle speed drops below approximately 40 km/h (25 mph)
- Ignition switch turned OFF
