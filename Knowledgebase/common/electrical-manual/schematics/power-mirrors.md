---
source: SD.pdf
chapter: SD
section: SD-128 to SD-131
pages: 128-131
title: Power Outside Mirrors
---

# Power Outside Mirrors

**SD-128 -- Power Outside Mirrors (1) Schematic**
**SD-129 -- Component Location Index**
**SD-130 -- Rear Window & Outside Mirror Defogger (1) Schematic**
**SD-131 -- Rear Window & Outside Mirror Defogger Component Location Index**

---

## Power Outside Mirrors -- Schematic (SD-128)

<!-- Figure: Power outside mirrors circuit with selector/position switch and dual mirror motors, source: SD.pdf page 128 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 23 (IGN / ACC) | -- | -- | -- | 0.85S |
| Outside mirror switch (D04) | selector (L/R) | -- | -- | -- |
| Outside mirror switch (D04) | position (UP/DN/L/R) | -- | -- | -- |
| Left outside mirror motor (D06) - UP/DN | (+) | -- | G/W | 0.85S |
| Left outside mirror motor (D06) - UP/DN | (-) | -- | G/B | 0.85S |
| Left outside mirror motor (D06) - L/R | (+) | -- | L/W | 0.85S |
| Left outside mirror motor (D06) - L/R | (-) | -- | L/Y | 0.85S |
| Right outside mirror motor (D16) - UP/DN | (+) | -- | G/R | 0.85S |
| Right outside mirror motor (D16) - UP/DN | (-) | -- | G/Y | 0.85S |
| Right outside mirror motor (D16) - L/R | (+) | -- | L/R | 0.85S |
| Right outside mirror motor (D16) - L/R | (-) | -- | L/B | 0.85S |

### Circuit Paths

#### Mirror Power Supply
```
Battery (+) → Fuse 23 (IGN/ACC) → [0.85S] → Outside mirror switch D04 (power in)
```

#### Left Mirror Selected -- UP Position
```
Outside mirror switch D04 → [G/W, 0.85S] → Left mirror D06 UP/DN motor (+)
Left mirror D06 UP/DN motor (-) → [G/B, 0.85S] → Outside mirror switch D04 → GND
```

#### Left Mirror Selected -- DOWN Position
```
Outside mirror switch D04 → [G/B, 0.85S] → Left mirror D06 UP/DN motor (-)
Left mirror D06 UP/DN motor (+) → [G/W, 0.85S] → Outside mirror switch D04 → GND
```

#### Left Mirror Selected -- LEFT Position
```
Outside mirror switch D04 → [L/W, 0.85S] → Left mirror D06 L/R motor (+)
Left mirror D06 L/R motor (-) → [L/Y, 0.85S] → Outside mirror switch D04 → GND
```

#### Left Mirror Selected -- RIGHT Position
```
Outside mirror switch D04 → [L/Y, 0.85S] → Left mirror D06 L/R motor (-)
Left mirror D06 L/R motor (+) → [L/W, 0.85S] → Outside mirror switch D04 → GND
```

#### Right Mirror Selected -- UP Position
```
Outside mirror switch D04 → [G/R, 0.85S] → Right mirror D16 UP/DN motor (+)
Right mirror D16 UP/DN motor (-) → [G/Y, 0.85S] → Outside mirror switch D04 → GND
```

#### Right Mirror Selected -- DOWN Position
```
Outside mirror switch D04 → [G/Y, 0.85S] → Right mirror D16 UP/DN motor (-)
Right mirror D16 UP/DN motor (+) → [G/R, 0.85S] → Outside mirror switch D04 → GND
```

#### Right Mirror Selected -- LEFT Position
```
Outside mirror switch D04 → [L/R, 0.85S] → Right mirror D16 L/R motor (+)
Right mirror D16 L/R motor (-) → [L/B, 0.85S] → Outside mirror switch D04 → GND
```

#### Right Mirror Selected -- RIGHT Position
```
Outside mirror switch D04 → [L/B, 0.85S] → Right mirror D16 L/R motor (-)
Right mirror D16 L/R motor (+) → [L/R, 0.85S] → Outside mirror switch D04 → GND
```

### Mirror Switch Position Table

| Selector | Position | Motor Active | Polarity |
|----------|----------|-------------|----------|
| LEFT | UP | D06 UP/DN | G/W (+), G/B (-) |
| LEFT | DOWN | D06 UP/DN | G/B (+), G/W (-) |
| LEFT | LEFT | D06 L/R | L/W (+), L/Y (-) |
| LEFT | RIGHT | D06 L/R | L/Y (+), L/W (-) |
| RIGHT | UP | D16 UP/DN | G/R (+), G/Y (-) |
| RIGHT | DOWN | D16 UP/DN | G/Y (+), G/R (-) |
| RIGHT | LEFT | D16 L/R | L/R (+), L/B (-) |
| RIGHT | RIGHT | D16 L/R | L/B (+), L/R (-) |

---

## Rear Window & Outside Mirror Defogger -- Schematic (SD-130)

<!-- Figure: Rear window defogger and outside mirror defogger heater circuit with BCM-controlled relay, source: SD.pdf page 130 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 13 (B+ at all times) | -- | -- | R | 2.0W |
| Fuse 9 (B+ at all times) | -- | -- | -- | -- |
| Defogger relay coil | 85 | -- | -- | 0.5S |
| Defogger relay coil | 86 | -- | B | 0.85S |
| Defogger relay contact | 30 | -- | R | 2.0W |
| Defogger relay contact | 87 | -- | -- | 1.25B |
| Rear window defogger (+) (R15) | (+) | -- | -- | 1.25B |
| Rear window defogger (-) (M65) | (-) | -- | B | 2.0W |
| Left outside mirror heater (D06) | (+) | -- | -- | 0.85S |
| Left outside mirror heater (D06) | (-) | -- | B | 0.85S |
| Right outside mirror heater (D16) | (+) | -- | -- | 0.85S |
| Right outside mirror heater (D16) | (-) | -- | B | 0.85S |
| BCM (defogger relay control) | -- | -- | -- | 0.5S |
| A/C control module - Auto (M19-1) | -- | -- | -- | -- |
| A/C control module - Manual (M20) | -- | -- | -- | -- |

### Circuit Paths

#### Defogger Relay Power Supply
```
Battery (+) → Fuse 13 → [R, 2.0W] → Defogger relay (contact 30)
```

#### Defogger Relay Coil Control (BCM)
```
BCM → [0.5S] → Defogger relay (coil 85)
Defogger relay (coil 86) → [B, 0.85S] → GND
```

#### Rear Window Defogger Circuit
```
Defogger relay (contact 87) → [1.25B] → Rear window defogger R15 (+)
Rear window defogger M65 (-) → [B, 2.0W] → GND (G01)
```

#### Left Outside Mirror Heater Circuit
```
Defogger relay (contact 87) → [0.85S] → Left mirror heater D06 (+)
Left mirror heater D06 (-) → [B, 0.85S] → GND (G01/G02)
```

#### Right Outside Mirror Heater Circuit
```
Defogger relay (contact 87) → [0.85S] → Right mirror heater D16 (+)
Right mirror heater D16 (-) → [B, 0.85S] → GND (G01/G02)
```

#### A/C Module Defogger Signal
```
A/C control module (M19-1 Auto / M20 Manual) → BCM (defogger request)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G01 | Dash area | Rear window defogger, mirror defogger grounds | CL-32 |
| G02 | Dash area | Mirror defogger ground | CL-32 |
| G11 | Dash area | BCM ground | CL-33 |
| G12 | Dash area | BCM ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-1F | Body Control Module | CL-8 |
| BCM-GF | Body Control Module | CL-8 |
| BCM-IM | Body Control Module | CL-8 |
| BCM-LM | Body Control Module | CL-8 |
| BCM-MR | Body Control Module | CL-8 |
| MD01 | Door connector | CL-8 |
| MD02 | Door connector | CL-8 |
| MD03 | Door connector | CL-8 |
| MD04 | Door connector | CL-8 |
| FR01 | Rear connector | CL-31 |
| SC08-GF | Sub-connector | CL-8 |
| SC08-IM | Sub-connector | CL-8 |
| SC08-MR | Sub-connector | CL-8 |

---

## Component Location Index (SD-129, SD-131)

### Power Outside Mirrors (SD-129)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| D04 | Outside mirror switch | CL-30 |
| D06 | Left outside mirror & mirror folding motor | CL-30 |
| D16 | Right outside mirror & mirror folding motor | CL-30 |

| Connector | Location Page |
|-----------|---------------|
| BCM-1F | CL-8 |
| MD01 | CL-8 |
| MD02 | CL-8 |
| MD03 | CL-8 |
| MD04 | CL-8 |

| Ground ID | Location Page |
|-----------|---------------|
| G01 | CL-32 |

### Rear Window & Outside Mirror Defogger (SD-131)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| D06 | Left outside mirror & mirror folding motor | CL-30 |
| D16 | Right outside mirror & mirror folding motor | CL-30 |
| M19-1 | A/C control module (Auto A/C) | CL-3 |
| M20 | A/C control module (Manual A/C) | CL-3 |
| M45 | Joint connector | CL-4 |
| M65 | Rear window defogger (-) | CL-31 |
| R15 | Rear window defogger (+) | CL-31 |

| Connector | Location Page |
|-----------|---------------|
| BCM-GF | CL-8 |
| BCM-IM | CL-8 |
| BCM-LM | CL-8 |
| BCM-MR | CL-8 |
| MD01 | CL-8 |
| MD03 | CL-8 |
| MD04 | CL-8 |
| MR01 | CL-8 |
| FR01 | CL-31 |

| Ground ID | Location Page |
|-----------|---------------|
| G01 | CL-32 |
| G02 | CL-32 |
| G08 | CL-32 |
| G11 | CL-33 |
| G12 | CL-33 |

---

## Notes

- The outside mirrors are controlled by the power door mirror switch (D04) on the driver door panel.
- The selector switch selects LEFT or RIGHT mirror; the position switch controls UP/DOWN/LEFT/RIGHT.
- The mirror motors are reversible DC motors; polarity reversal changes direction.
- Battery voltage is applied through Fuse 23 (IGN/ACC) -- mirrors only operate with ignition on.
- The BCM controls the rear window defogger and outside mirror heaters through the defogger relay.
- When the rear window defogger switch is pressed (ON) and the engine is running, the BCM energizes the defogger relay coil for 20 minutes.
- The defogger relay supplies battery voltage to the rear window defogger grid, left mirror heater, and right mirror heater simultaneously.
- The A/C control module can also request defogger activation through the BCM.
