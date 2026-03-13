---
source: SD.pdf
chapter: SD
section: SD-114 to SD-121
pages: 114-121
title: Indicators and Gauges
---

# Indicators and Gauges

**SD-114 -- Indicators and Gauges (1) Schematic — Warning Indicators**
**SD-115 -- Indicators and Gauges (2) Schematic — Brake / ABS / Parking Brake**
**SD-116 -- Indicators and Gauges (3) Schematic — Door/Trunk/Seatbelt/DRL**
**SD-117 -- Indicators and Gauges (4) Schematic — MICOM (Auto Transaxle Indicators)**
**SD-118 -- Indicators and Gauges (5) Schematic — Gauges (Speedo/Tach/Fuel/Temp)**
**SD-119 -- Component Location Index (Part 1)**
**SD-120 -- Component Location Index (Part 2) / Circuit Description**
**SD-121 -- Memo (blank)**

---

## SD-114 — Warning Indicators (Sheet 1)

### Component Table — Warning Indicators

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 6 (IGN) | -- | -- | R/Y | 0.85S |
| Fuse 17 (IGN) | -- | -- | R/Y | 2.0B |
| Instrument cluster (M10) | -- | -- | -- | -- |
| BCM-MR connector | -- | -- | -- | -- |
| BCM-CE connector | -- | -- | -- | -- |
| Charging system | -- | -- | L | 0.85S |
| Oil pressure switch (C11/C111) | -- | -- | Y/R | 0.5S |
| Oil pressure switch (C115, 2.7L/1.6L) | -- | -- | Y/R | 0.5S |
| ECM (engine control module) | -- | -- | -- | -- |
| SRS air bag system | -- | -- | -- | -- |
| Dual-oil pressure control system | -- | -- | -- | -- |
| Electronic throttle control system | -- | -- | -- | -- |
| Immobilizer indicator | -- | -- | -- | -- |

### Circuit Paths — Warning Indicators

#### Check Engine (MIL) Indicator
```
Fuse 6 (IGN) → [R/Y, 0.85S] → Instrument cluster M10 (MIL lamp)
  → ECM (ground control) → GND
  ECM pulls indicator low when fault detected
```

#### Charging System Indicator
```
Fuse 17 (IGN) → [R/Y] → Instrument cluster M10 (charge indicator)
  → [L, 0.85S] → Alternator (L terminal)
  Indicator ON when alternator not charging (no voltage at L terminal)
```

#### Oil Pressure Indicator
```
Fuse 6 (IGN) → Instrument cluster M10 (oil pressure indicator)
  → [Y/R, 0.5S] → Oil pressure switch (C11/C111/C115)
  → GND (when oil pressure low, switch closes to ground)
```

#### SRS Air Bag Indicator
```
SRS air bag system → Instrument cluster M10 (SRS indicator)
  SRS module controls indicator via ground switching
```

#### Immobilizer Indicator
```
ECM → [via connector] → Instrument cluster M10 (immobilizer indicator)
  → GND (G13)
```

---

## SD-115 — Brake / ABS / Parking Brake Indicators (Sheet 2)

### Component Table — Brake Indicators

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Instrument cluster (M10) | -- | -- | -- | -- |
| Brake fluid level switch (C20/C120/C220) | -- | -- | P | 0.5S |
| Parking brake switch (M50) | -- | -- | P/B | 0.5S |
| ABS control module | -- | -- | -- | -- |
| Brake warning diode | -- | -- | -- | -- |
| Fuse 17 (IGN) | -- | -- | R/Y | -- |

### Circuit Paths — Brake Indicators

#### Brake Warning Indicator
```
Fuse 17 (IGN) → Instrument cluster M10 (brake warning indicator)
  → Diode → [P, 0.5S] → Brake fluid level switch (C20/C120/C220)
  → GND (when fluid low, switch closes)
  → Diode → [P/B, 0.5S] → Parking brake switch M50
  → GND (when parking brake engaged)
```

#### ABS Warning Indicator
```
ABS control module → Instrument cluster M10 (ABS indicator)
  → ABS module ground-controls indicator
  See Anti-Lock Brake System / Traction Control System
```

### Low Fuel Warning
```
Fuel sender → Instrument cluster M10 (low fuel indicator)
  Internal to cluster MICOM — triggers at low resistance (low fuel level)
```

---

## SD-116 — Door/Trunk/Seatbelt/DRL Indicators (Sheet 3)

### Component Table — Door/Trunk/DRL Indicators

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Instrument cluster (M10) | -- | -- | -- | -- |
| Multifunction switch (M01-2) | turn/hazard | -- | G/B, G/W | 0.5S |
| Door ajar switches (left/right) | -- | -- | -- | 0.5S |
| Trunk lid switch | -- | -- | Gr/W | 0.5S |
| DRL indicator | -- | -- | -- | -- |
| Seatbelt switch (M48) | -- | -- | P/L | 0.5S |
| Courtesy lamp / luggage room | -- | -- | -- | -- |

### Circuit Paths — Door/Trunk/DRL

#### Left Turn / Right Turn Indicators
```
Multifunction switch M01-2 → [G/B, 0.5S] → Instrument cluster (left turn indicator)
Multifunction switch M01-2 → [G/W, 0.5S] → Instrument cluster (right turn indicator)
See Turn and Hazard Lamps (SD-172)
```

#### Door Ajar Indicator
```
Door switches → Instrument cluster M10 (door ajar indicator)
  Switches close to ground when door open
  Left front door / Right front door / Trunk lid
```

#### Trunk Open Indicator
```
Trunk lid switch → [Gr/W, 0.5S] → Instrument cluster M10 (trunk indicator)
  → GND when trunk open
```

#### Seatbelt Warning
```
Fuse (IGN) → Instrument cluster M10 (seatbelt indicator)
  → [P/L, 0.5S] → Seatbelt switch M48 → GND (when belt unbuckled)
```

#### DRL Indicator
```
See Courtesy Lamp / Luggage Room / DRL
Daytime running lamp control → Instrument cluster DRL indicator
```

---

## SD-117 — MICOM / Automatic Transaxle Indicators (Sheet 4)

### Component Table — A/T Indicators

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Instrument cluster (M10) | MICOM | -- | -- | -- |
| Automatic transaxle control system | -- | -- | -- | -- |
| SPORT indicator | -- | -- | -- | 0.5S |
| HOLD indicator | -- | -- | -- | 0.5S |
| Gear position indicators (P/R/N/D/3/2/L) | -- | -- | -- | -- |

### Circuit Paths — A/T Indicators
```
See Automatic Transaxle Control System
A/T control module → [multiple wires, 0.5S each] → Instrument cluster MICOM
  → Gear position display: P, R, N, D, 3, 2, L
  → SPORT mode indicator
  → HOLD mode indicator
```

#### MICOM Internal
```
Instrument cluster MICOM receives:
  - Vehicle speed signal
  - Tachometer signal
  - Fuel level input
  - Coolant temperature input
  - A/T gear position signals
  - Trip computer data
```

---

## SD-118 — Gauges (Sheet 5)

### Component Table — Gauges

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Instrument cluster (M10) | BCM-JM | -- | -- | -- |
| Speedometer (cross-coil gauge) | -- | -- | -- | -- |
| Tachometer (cross-coil gauge) | -- | -- | -- | -- |
| Fuel gauge (cross-coil gauge) | -- | -- | -- | -- |
| Coolant temperature gauge (cross-coil gauge) | -- | -- | -- | -- |
| Vehicle speed sensor | -- | -- | P/B | 0.5S |
| ECM (tach signal) | -- | -- | Y/L | 0.5S |
| Fuel sender and fuel pump motor (M55) | sender | -- | Y/B | 0.5S |
| Engine coolant temp sensor/sender (C11/C111) | sender | -- | Y | 0.5S |
| Fuse 17 (IGN) | -- | -- | R/Y | -- |

### Circuit Paths — Gauges

#### Speedometer
```
Vehicle speed sensor → [P/B, 0.5S] → Instrument cluster MICOM (speedometer)
  Speedometer drive circuit receives pulses from vehicle speed sensor
  Pulse rate increases as car accelerates
  Frequency and duration of input pulses are measured and displayed
```

#### Tachometer
```
ECM → [Y/L, 0.5S] → Instrument cluster MICOM (tachometer)
  Tachometer displays engine speed in RPM
  Voltage is applied to the tach input from the ECM
  Responds to frequency of voltage pulses, which vary with engine speed
```

#### Fuel Gauge
```
Fuse 17 (IGN) → Instrument cluster M10 (fuel gauge)
  → [Y/B, 0.5S] → Fuel sender (M55, in-tank) → GND
  Pointer moved by magnetic fields of two coils
  Both coils are at right angles to each other
  Battery voltage applied to coils through Fuse 17
  Magnetic fields controlled by fuel level sender
  Resistance: sender varies from ~6 ohm (full) to ~97 ohm (empty)
```

#### Engine Coolant Temperature Gauge
```
Fuse 17 (IGN) → Instrument cluster M10 (temp gauge)
  → [Y, 0.5S] → Engine coolant temperature sender (C11/C111) → GND
  Pointer moved by magnetic fields of two coils
  Magnetic fields controlled by coolant temperature sender
  Sender resistance varies from ~1070 ohm at 20°C to ~43 ohm at 115°C
```

### Gauge Outputs from Cluster

| Signal | Wire Color | Size | Destination |
|--------|-----------|------|-------------|
| Speed pulse | P/B | 0.5S | To turn signal / hazard module |
| Tach from ECM | Y/L | 0.5S | ECM connector |
| Fuel sender | Y/B | 0.5S | Fuel sender & fuel pump motor M55 |
| Coolant temp sender | Y | 0.5S | Engine coolant temp sensor/sender |

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G01 | Engine compartment | Oil pressure switch ground | CL-32 |
| G11 | Dash area | Instrument cluster ground | CL-33 |
| G13 | Dash area | Instrument cluster ground, immobilizer | CL-33 |
| G20 | Rear area | Fuel sender ground | CL-34 |
| G23 | Rear area | Fuel sender ground | CL-34 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-EF | Body Control Module | CL-8 |
| BCM4-JM | Body Control Module | CL-8 |
| MC01 | Main connector | CL-8 |
| MC101 | Main connector | CL-8 |
| MC201 | Main connector | CL-8 |
| IM01 | Immobilizer connector | CL-8 |

---

## Component Location Index (SD-119 / SD-120)

### Components

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C11 | Engine coolant temperature sensor & sender (2.0L) | CL-18 |
| C15 | Oil pressure switch (2.0L) | CL-19 |
| C20 | Brake fluid level sensor (2.0L) | CL-19 |
| C111 | Engine coolant temperature sensor & sender (2.7L) | CL-22 |
| C115 | Oil pressure switch (2.7L/1.6L) | CL-23 |
| C120 | Brake fluid level sensor (2.7L) | CL-23 |
| C200 | Engine coolant temperature sensor & sender (1.6L) | CL-27 |
| C215 | Oil pressure switch (1.6L) | CL-27 |
| C220 | Brake fluid level sensor (1.6L) | CL-27 |
| C203 | ECM (1.6L) | CL-28 |
| M10-1 | Instrument cluster | CL-6 |
| M10-2 | Instrument cluster | CL-5 |
| M10-3 | Instrument cluster | CL-4 |
| M55 | Joint connector | CL-8 |
| M48 | Seat belt switch | CL-9 |
| M50 | Parking brake switch | CL-9 |
| M55 | Fuel sender & fuel pump motor | CL-9 |

### Connectors

| Connector | Location Page |
|-----------|---------------|
| BCM-EF | CL-8 |
| BCM4-JM | CL-8 |
| MC01 | CL-8 |
| MC101 | CL-8 |
| MC201 | CL-8 |
| IM01 | CL-8 |

### Grounds

| Ground ID | Location Page |
|-----------|---------------|
| G01 | CL-32 |
| G11 | CL-33 |
| G13 | CL-33 |
| G20 | CL-34 |
| G23 | CL-34 |

---

## Notes

### Indicator Bulb Check
- The operation of individual indicators is stated below.
- At IGN ON, each indicator lamp illuminates briefly (bulb check), then goes off if the system is normal.
- See each circuit schematic diagram for individual system details.

### Oil Pressure Indicator
- Battery voltage is applied to the indicator bulb from Fuse 17 with the ignition in ON or START.
- When the oil pressure is low, the oil pressure switch closes, providing ground to the indicator. The indicator is on.
- Oil pressure will not present when the engine is not running, and the indicator remains illuminated until oil pressure rises.

### Low Fuel Indicator
- Battery voltage is applied to the indicator bulb from Fuse 17 with ignition in ON or START.
- The thermistor in the fuel gauge sender is near the bottom of the tank. When fuel level is low, resistance decreases, providing ground to the indicator bulb, causing it to illuminate.

### Brake Indicator
- When the ignition switch is in ON or START, battery voltage is applied from Fuse 17 to the brake warning light.
- When the brake is applied, the seat belt chimes and provides a ground for the indicator.
- The brake fluid level switch also provides a ground when the parking brake is applied.
- The brake fluid level switch provides ground to the indicator if the brake fluid level is low.
- Check brake fluid level before adding fluid.

### Speedometer
- Speedometer: switch in ON and START, the speedometer drive circuit receives pulses from the vehicle speed sensor. The pulse rate increases as the car accelerates.
- The frequency and duration of these input pulses are measured and displayed by the speedometer.

### Tachometer
- The tachometer displays engine speed in RPM. Voltage is applied to the tachometer by the ECM. The tachometer responds to the frequency of the voltage pulses, which vary according to engine speed.

### Fuel Gauge
- The pointer of the fuel gauge is moved by the magnetic fields of two coils. Both coils are at right angles to each other. Battery voltage is applied to the coils through Fuse 17, generating the magnetic fields. Controlled by the fuel level sender, causes the gauge needle to move. Resistance from sender at empty is approximately 97 ohm, at full approximately 6 ohm.

### Engine Coolant Temperature Gauge
- Battery voltage is applied to the coils through Fuse 17, generating the magnetic fields. The magnetic fields, controlled by the engine coolant temperature sender, cause the sender series current through the gauge coils to change. The fuel gauge sender resistance varies from approximately 1070 ohm at 20 degrees C to approximately 43 ohm at 115 degrees C.
