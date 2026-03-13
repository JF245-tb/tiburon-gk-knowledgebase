---
source: SD.pdf
chapter: SD
section: SD-162 to SD-165
pages: 162-165
title: Daytime Running Lights
---

# Daytime Running Lights

**SD-162 -- Daytime Running Lights (1) Schematic -- Power Feed, Generator Signal, DRL Module, Relays**
**SD-163 -- Daytime Running Lights (2) Schematic -- BCM, Multifunction Switch, Headlamps, Tail Lamp Relay**
**SD-164 -- Component Location Index**
**SD-165 -- Memo**

---

## Daytime Running Lights (1) -- Power Feed and DRL Module (SD-162)

<!-- Figure: DRL power feed circuit showing fusible links, fuses, BCM connection, generator L-terminal signal, DRL control module, DRL relay, and headlamp relay connections, source: SD.pdf page 162 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fusible link 2 (B+ at all times) | -- | -- | R | 3.0W |
| Fusible link 3 (B+ at all times) | -- | -- | R | 2.0W |
| Fuse 8 (B+ at all times) | -- | -- | -- | 0.85S |
| Fuse 11 (IGN) | -- | -- | -- | 0.5S |
| BCM-CE connector | -- | -- | -- | -- |
| Generator (E02-2) | L terminal | -- | L/R | 0.5S |
| DRL control module (E57) | SUPPLY | -- | -- | 0.5S |
| DRL control module (E57) | GROUND | -- | B | 0.85S |
| DRL control module (E57) | SIGNAL | -- | L/R | 0.5S |
| DRL control module (E57) | SMALL/LARGE | -- | -- | 0.5S |
| DRL control module (E57) | HALL VCC | -- | -- | 0.5S |
| DRL control module (E57) | DIRECTION | -- | -- | 0.5S |
| DRL control module (E57) | LOCK1 | -- | -- | 0.5S |
| DRL resistor (E58) | -- | -- | -- | 0.85B |
| DRL relay | coil | -- | -- | 0.5S |
| DRL relay | contact 30 | -- | -- | 1.25B |
| DRL relay | contact 87 | -- | -- | 1.25B |
| Head lamp relay HIGH (E51) | coil | -- | -- | -- |
| Head lamp relay HIGH (E51) | contact | -- | -- | -- |
| Head lamp relay LOW (E46) | coil | -- | -- | -- |
| Head lamp relay LOW (E46) | contact | -- | -- | -- |
| ETACS module (E97) | -- | -- | -- | -- |

### Circuit Paths

#### DRL Control Module Power Supply
```
Battery (+) → Fusible link 3 → Fuse 11 (IGN) → [0.5S] → DRL control module E57 (SUPPLY)
DRL control module E57 (GROUND) → [B, 0.85S] → GND
```

#### Generator Running Signal to DRL Module
```
Generator E02-2 (L terminal) → [L/R, 0.5S] → BCM-CE → [0.5S]
  → DRL control module E57 (SIGNAL input)
```

#### DRL Relay Control
```
DRL control module E57 (relay output) → [0.5S] → DRL relay (coil)
DRL relay (coil ground) → GND
```

#### DRL Relay to Headlamp Feed
```
Battery (+) → Fusible link 2 → Fuse 8 (B+ at all times) → [1.25B] → DRL relay (contact 30)
DRL relay (contact 87) → [1.25B] → DRL resistor E58 → [0.85B]
  → Head lamp relay LOW E46 (contact 87 feed)
  → To low beam headlamps (reduced voltage through DRL resistor)
```

#### DRL Module to ETACS/BCM
```
DRL control module E57 → [0.5S] → ETACS module E97
  → Tail lamp relay control (for DRL tail lamp indication)
```

#### To Headlamp Relay Feed
```
DRL relay (contact 87) → To head lamp relay(s)
  → To headlamp feed path
```

---

## Daytime Running Lights (2) -- BCM, Switches, Headlamps (SD-163)

<!-- Figure: DRL circuit continuation showing BCM connections, multifunction light switch, parking/headlamp position, headlamp relay, tail lamp relay, joint connectors to left and right headlamps, source: SD.pdf page 163 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 14 (B+ at all times) | -- | -- | R | 2.0W |
| Fuse 7 (B+ at all times) | -- | -- | R | 2.0W |
| Multifunction switch (M01-2) | OFF | -- | -- | -- |
| Multifunction switch (M01-2) | PARK | -- | -- | 0.85S |
| Multifunction switch (M01-2) | HEAD | -- | -- | 0.85S |
| Multifunction switch (M01-2) | FLASH | -- | -- | -- |
| Head lamp relay LOW (E46) | contact 30 | -- | -- | 1.25B |
| Head lamp relay LOW (E46) | contact 87 | -- | -- | 1.25B |
| Head lamp relay HIGH (E51) | coil 85/86 | -- | -- | 0.85S |
| Tail lamp relay | coil | -- | -- | 0.5S |
| Tail lamp relay | contact 30 | -- | R | 2.0W |
| Tail lamp relay | contact 87 | -- | -- | 1.25B |
| Joint connector (E56) | -- | -- | -- | -- |
| Joint connector (M35) | -- | -- | -- | -- |
| Joint connector (M36) | -- | -- | -- | -- |
| BCM-CE connector | -- | -- | -- | -- |
| BCM-HM connector | -- | -- | -- | -- |
| SC08-CE connector | -- | -- | -- | -- |
| SC08-HM connector | -- | -- | -- | -- |
| Left head lamp (E07) | low beam | -- | -- | 1.25B |
| Right head lamp (E27) | low beam | -- | -- | 1.25B |
| Instrument cluster (M10-1) | -- | -- | -- | 0.85S |
| ETACS module (E97) | -- | -- | -- | -- |
| DRL connector (EM01) | -- | -- | -- | -- |

### Circuit Paths

#### Multifunction Switch -- HEAD Position (Normal Headlamps)
```
Multifunction switch M01-2 (HEAD) → [0.85S] → BCM-HM
  → Head lamp relay LOW E46 (coil) → Relay energized
  → Head lamp relay LOW E46 (contact 87) → [1.25B]
  → Joint connector E56/M35 → Left head lamp E07 (low beam)
  → Joint connector E56/M36 → Right head lamp E27 (low beam)
```

#### Multifunction Switch -- PARK Position (Tail Lamps)
```
Multifunction switch M01-2 (PARK) → [0.85S] → BCM-CE
  → Tail lamp relay (coil) → Relay energized
  → To tail lamp feed
```

#### DRL Mode -- Low Beams at Reduced Voltage
```
DRL relay (contact 87) → DRL resistor E58 → [reduced voltage]
  → Head lamp relay LOW E46 (contact 87) → [1.25B]
  → Left head lamp E07 (low beam, reduced brightness)
  → Right head lamp E27 (low beam, reduced brightness)
```

#### DRL Module Tail Lamp Relay Control
```
DRL control module E57 → [0.5S] → Tail lamp relay (coil control)
  → Controls tail lamps during DRL operation
```

#### Headlamp Ground
```
Left head lamp E07 (ground) → [B, 1.25B] → GND (G15)
Right head lamp E27 (ground) → [B, 1.25B] → GND (G15)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G01 | Dash area | DRL module ground | CL-33 |
| G11 | Dash area | BCM ground | CL-33 |
| G15 | Engine compartment | Headlamp grounds | CL-33 |
| G16 | Engine compartment | Relay grounds | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-CE | Body Control Module | CL-14 |
| BCM-DE | Body Control Module | CL-14 |
| BCM-HM | Body Control Module | CL-8 |
| EB01 | Engine compartment | CL-14 |
| EM01 | DRL connector | CL-9 |
| MA03 | Multifunction connector | CL-8 |

---

## Component Location Index (SD-164)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| E07 | Left head lamp | CL-10 |
| E02-2 | Generator (G,S) | CL-11 |
| E27 | Right head lamp | CL-11 |
| E46 | Head lamp relay (LOW) | CL-12 |
| E51 | Head lamp relay (HIGH) | CL-12 |
| E56 | Joint connector | CL-12 |
| E57 | DRL control module | CL-12 |
| E58 | DRL resistor | CL-13 |
| M01-2 | Multifunction switch | CL-2 |
| M10-1 | Instrument cluster | CL-3 |
| M35 | Joint connector | CL-4 |
| M36 | Joint connector | CL-4 |

| Connector | Location Page |
|-----------|---------------|
| BCM-CE | CL-14 |
| BCM-DE | CL-14 |
| BCM-HM | CL-8 |
| EB01 | CL-14 |
| EM01 | CL-9 |
| MA03 | CL-8 |

| Ground ID | Location Page |
|-----------|---------------|
| G01 | CL-33 |
| G11 | CL-33 |
| G15 | CL-33 |
| G16 | CL-33 |

---

## Notes

- For the visibility and safety of drivers, the daytime running lights will turn on automatically when the engine is running. Under this condition, the head lamps will illuminate at reduced brightness.
- The DRL control module detects the generator running signal (L terminal). When the engine is running, the DRL control module controls the low beam head lamps through the DRL relay coil. Battery voltage from fusible link (BATT) is supplied to the low beam head lamps through the DRL relay, reduced in voltage by the DRL resistor.
- In addition to the DRL relay control, the DRL control module controls the tail lamp relay (built in the ETACS module coil). Battery voltage is supplied to the circuit control of the head lamps.
- When the DRL module detects the engine running OFF signal, the DRL control module turns the lights off.
- When the DRL module detects the light switch ON (PARK or HEAD) signal, the DRL control module stops its function and normal headlamp/tail lamp operation takes over.
- The DRL resistor reduces voltage to the low beam headlamps during DRL mode, providing reduced-brightness operation that distinguishes DRL from normal headlamp operation.
