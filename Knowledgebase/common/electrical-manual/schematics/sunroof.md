---
source: SD.pdf
chapter: SD
section: SD-144 to SD-147
pages: 144-147
title: Sunroof
---

# Sunroof

**SD-144 -- Sunroof (1) Schematic (LHD)**
**SD-145 -- Sunroof (2) Schematic (RHD)**
**SD-146 -- Component Location Index**
**SD-147 -- Memo**

---

## Sunroof (1) -- LHD Schematic (SD-144)

<!-- Figure: Sunroof circuit for LHD vehicles showing fuse power feeds, overhead console lamp switch, sunroof controller CPU with CF-12V relay, and sunroof motor, source: SD.pdf page 144 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 15 (IGN) | -- | -- | -- | 0.85S |
| Fuse 24 (B+ at all times) | -- | -- | -- | 2.0W |
| Overhead console lamp (M95) | open/close switch | -- | -- | 0.5S |
| Overhead console lamp (M95) | tilt up/down switch | -- | -- | 0.5S |
| Sunroof controller | CPU | -- | -- | -- |
| Sunroof controller | CF-12V relay | coil | -- | -- |
| Sunroof controller | CF-12V relay | contact 30 | -- | -- |
| Sunroof controller | CF-12V relay | contact 87 | -- | -- |
| Sunroof motor (M96) | terminal 1 | -- | -- | 2.0W |
| Sunroof motor (M96) | terminal 2 | -- | -- | 2.0W |
| BCM-LM connector | -- | -- | -- | -- |
| BCM-LR connector (LHD) | -- | -- | -- | -- |

### Circuit Paths

#### Sunroof Controller Constant Power (B+)
```
Battery (+) → Fuse 24 (B+ at all times) → [2.0W] → BCM-LR → Sunroof controller (B+)
```

#### Sunroof Controller Ignition Power
```
Ignition → Fuse 15 (IGN) → [0.85S] → BCM-LM → Sunroof controller (IGN)
```

#### Sunroof Switch Inputs to Controller
```
Overhead console lamp M95 (OPEN/CLOSE switch) → [0.5S] → Sunroof controller CPU (OPEN/CLOSE input)
Overhead console lamp M95 (TILT UP/DOWN switch) → [0.5S] → Sunroof controller CPU (TILT input)
```

#### Sunroof Controller CPU Internal
```
CPU (SUPPLY, GROUND, SIAP, GROUND) → Internal signals
  → CPU (SMALL/LARGE, HALL VCC, DIRECTION, LOCK1) → CF-12V relay coil control
```

#### Sunroof Motor Drive Circuit
```
Sunroof controller CF-12V relay (contact 87) → [2.0W] → Sunroof motor M96 (terminal 1)
Sunroof motor M96 (terminal 2) → [2.0W] → Sunroof controller (return)
  (Controller relay reverses polarity for OPEN/CLOSE/TILT directions)
```

#### Sunroof Controller Ground
```
Sunroof controller → [B] → GND (G01, G12)
```

---

## Sunroof (2) -- RHD Schematic (SD-145)

<!-- Figure: Sunroof circuit for RHD vehicles with BCM-MR connector routing instead of BCM-LR, otherwise identical to LHD, source: SD.pdf page 145 -->

### RHD Differences

- RHD uses BCM-MR connector instead of BCM-LR for power routing
- Uses SC08-10 sub-connector instead of SC08-LR
- All other circuit paths, wire colors, and wire sizes are identical to LHD

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G01 | Dash area | Sunroof controller ground | CL-33 |
| G12 | Dash area | Sunroof controller ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-LM | Body Control Module | CL-8 |
| BCM-MR | Body Control Module | CL-8 |

---

## Component Location Index (SD-146)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| M95 | Overhead consol lamp | CL-7 |
| M96 | Sunroof | CL-7 |

| Connector | Location Page |
|-----------|---------------|
| BCM-LM | CL-8 |
| BCM-MR | CL-8 |

| Ground ID | Location Page |
|-----------|---------------|
| G01 | CL-33 |
| G12 | CL-33 |

---

## Notes

- Battery voltage is supplied at all times to the sunroof controller from Fuse 24. Fuse 15 also supplies battery voltage when the ignition switch is ON.
- The overhead console lamp contains open/close and tilt up/tilt down switches. When one of them is depressed, the sunroof motor is operated by the CPU and relay of the sunroof controller.
- The sunroof controller contains a CPU and a CF-12V relay that controls motor direction and operation.
- The CPU monitors Hall sensor feedback from the motor to track sunroof position and limit travel.
