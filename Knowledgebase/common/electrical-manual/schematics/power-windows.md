---
source: SD.pdf
chapter: SD
section: SD-140 to SD-143
pages: 140-143
title: Power Windows
---

# Power Windows

**SD-140 -- Power Windows (1) Schematic -- Relay and Power Feed**
**SD-141 -- Power Windows (2) Schematic -- Switches and Motors**
**SD-142 -- Component Location Index**
**SD-143 -- Memo**

---

## Power Windows (1) -- Relay and Power Feed (SD-140)

<!-- Figure: Power window relay power feed from BCM fuse box through power window relay to left power window switch, source: SD.pdf page 140 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 19 (B+ at all times) | -- | -- | -- | -- |
| Power window relay | coil 85 | -- | -- | 0.85S |
| Power window relay | coil 86 | -- | B | 0.85S |
| Power window relay | contact 30 | -- | -- | 2.0W |
| Power window relay | contact 87 | -- | -- | 2.0W |
| BCM-GF connector | -- | -- | -- | -- |
| SCM-LE connector | -- | -- | -- | 2.0W |
| SCM-GF connector | -- | -- | -- | 0.85S |
| Ground G21 | -- | -- | B | 0.85S |

### Circuit Paths

#### Power Window Relay Power Supply
```
Battery (+) → Fuse 19 (B+ at all times, BCM Box) → [2.0W] → Power window relay (contact 30)
  → Power window relay (contact 87) → [2.0W] → SCM-LE → To left power window switch
```

#### Power Window Relay Coil Circuit
```
Ignition → [0.85S] → SCM-GF → Power window relay (coil 85)
Power window relay (coil 86) → [B, 0.85S] → GND (G21)
```

#### Power Feed Distribution
```
Power window relay (contact 87) → [2.0W] → Junction
  → [2.0R] → MD01 pin 14 → To left power window switch
  → [2.0R] → To right power window switch
```

---

## Power Windows (2) -- Switches and Motors (SD-141)

<!-- Figure: Power window switch and motor circuits for all four windows showing left power window master switch, individual window switches, and four window motors, source: SD.pdf page 141 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Left power window switch (D01) | power in | -- | -- | 2.0R |
| Left power window switch (D01) | lock switch | -- | -- | 0.85S |
| Left power window motor (D01) | (+) | -- | -- | 2.0R |
| Left power window motor (D01) | (-) | -- | -- | 2.0R |
| Right power window switch (D05) | -- | -- | -- | 0.85S |
| Right power window motor (D11) | (+) | -- | -- | 2.0R |
| Right power window motor (D11) | (-) | -- | -- | 2.0R |
| Left rear window switch (D03) | -- | -- | -- | -- |
| Right rear window switch (D13) | -- | -- | -- | -- |
| Driver power window master switch | -- | -- | -- | -- |

### Circuit Paths

#### Left Power Window Motor Circuit
```
Left power window switch D01 → [2.0R] → Left window motor D01 terminal 1
Left window motor D01 terminal 2 → [2.0R] → Left power window switch D01
  (switch reverses polarity for UP/DOWN)
```

#### Right Power Window Motor Circuit (from Master Switch)
```
Left power window master switch → [2.0R] → MD01 → Right window motor D11 terminal 1
Right window motor D11 terminal 2 → [2.0R] → MD01 → Left power window master switch
```

#### Right Power Window Motor Circuit (from Passenger Switch)
```
Right power window switch D05 → [2.0R] → Right window motor D11 terminal 1
Right window motor D11 terminal 2 → [2.0R] → Right power window switch D05
  (switch reverses polarity for UP/DOWN)
```

#### Window Lock Function
```
Left power window switch (lock) → disables passenger window switches
  → Power feed interrupted to passenger switch inputs
```

#### Illumination
```
See Illumination → [0.85S] → Left power window switch illumination
See Illumination → [0.85S] → Right power window switch illumination
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G01 | Dash area | Window motor grounds | CL-32 |
| G21 | -- | Power window relay coil ground | -- |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-GF | Body Control Module | CL-8 |
| MD01 | Left door connector | CL-8 |
| MD03 | Left door connector | CL-8 |
| MC03 | Multifunction connector | CL-8 |

---

## Component Location Index (SD-142)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| D01 | Left power window motor | CL-30 |
| D05 | Left power window switch | CL-30 |
| D11 | Right power window motor | CL-30 |
| D13 | Right power window switch | CL-30 |

| Connector | Location Page |
|-----------|---------------|
| BCM-GF | CL-8 |
| MD01 | CL-8 |
| MC03 | CL-8 |

| Ground ID | Location Page |
|-----------|---------------|
| G21 | CL-32 |

---

## Notes

- A permanent magnet motor operates each of the four power windows. Each motor raises or lowers the glass when voltage is applied to it. The direction the motor turns depends on the polarity of the supply voltage.
- The left power window switch controls all the power window motors. Each window switch controls only one of the power window motors. If the lock switch is activated, the passenger windows can only be controlled from the left power window switch.
- Battery voltage is applied to the coil and the contacts of the power window relay at all times. The coil of the relay is grounded through the body control module.
- Battery voltage is then supplied to the left power window switch through the closed relay contacts.
- With the power window relay energized, battery voltage is supplied to the passenger window switches as long as the lock switch in the left power window switch is OFF (not depressed). When the passenger windows switch is operated, battery voltage is applied to one terminal of the power window motor. The other terminal is grounded through the window switch and the main switch. The power window motor runs to drive the window.
