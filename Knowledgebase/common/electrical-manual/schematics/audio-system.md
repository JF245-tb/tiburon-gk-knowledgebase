---
source: SD.pdf
chapter: SD
section: SD-150 to SD-157
pages: 150-157
title: Audio System
---

# Audio System

**SD-150 -- Audio System (1) HIGH, LHD**
**SD-151 -- Audio System (2) HIGH, LHD**
**SD-152 -- Audio System (3) HIGH, RHD**
**SD-153 -- Audio System (4) HIGH, RHD**
**SD-154 -- Audio System (5) LOW, LHD**
**SD-155 -- Audio System (6) LOW, RHD**
**SD-156 -- Component Location Index**
**SD-157 -- Memo**

---

## HIGH Grade (with Amplifier) -- LHD

<!-- Figure: Audio System (1) HIGH LHD - power, radio, front speakers, source: SD.pdf page 150 -->
<!-- Figure: Audio System (2) HIGH LHD - rear speakers, amp, sub, source: SD.pdf page 151 -->

### Component Table (HIGH LHD)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 3 (BATT) | -- | -- | R/W | 1.25Y |
| Fuse 27 (ACC/ON) | -- | -- | R/Y | 1.25Y |
| BCM-AM | -- | -- | -- | -- |
| BCM-FF | -- | -- | -- | -- |
| Audio (M18) | power B+ (BATT) | -- | R/W | 1.25Y |
| Audio (M18) | power B+ (ACC) | -- | R/Y | 1.25Y |
| Audio (M18) | ground | -- | B | 1.25Y |
| Audio (M18) | illumination | -- | G/R | 0.5S |
| Audio (M18) | left front speaker (+) | -- | L/R | 0.5S |
| Audio (M18) | left front speaker (-) | -- | L/W | 0.5S |
| Audio (M18) | right front speaker (+) | -- | L/B | 0.5S |
| Audio (M18) | right front speaker (-) | -- | L/Y | 0.5S |
| Audio (M18) | left rear speaker (+) | -- | L/O | 0.5S |
| Audio (M18) | left rear speaker (-) | -- | L/Br | 0.5S |
| Audio (M18) | right rear speaker (+) | -- | Br/W | 0.5S |
| Audio (M18) | right rear speaker (-) | -- | Br/R | 0.5S |
| Audio (M18) | antenna | -- | -- | -- |
| Antenna (roof) | signal | -- | -- | coax |
| Left front speaker (D02) | (+) | -- | L/R | 0.5S |
| Left front speaker (D02) | (-) | -- | L/W | 0.5S |
| Right front speaker (D12) | (+) | -- | L/B | 0.5S |
| Right front speaker (D12) | (-) | -- | L/Y | 0.5S |
| Left tweeter (E07 area) | (+) | -- | V/W | 0.5S |
| Left tweeter (E07 area) | (-) | -- | V/Y | 0.5S |
| Right tweeter (E27 area) | (+) | -- | V/R | 0.5S |
| Right tweeter (E27 area) | (-) | -- | V/B | 0.5S |
| AMP #1 (M63-1) | left front (+) | -- | L/R | 0.5S |
| AMP #1 (M63-1) | left front (-) | -- | L/W | 0.5S |
| AMP #1 (M63-1) | right front (+) | -- | L/B | 0.5S |
| AMP #1 (M63-1) | right front (-) | -- | L/Y | 0.5S |
| AMP #1 (M63-1) | left tweeter (+) | -- | V/W | 0.5S |
| AMP #1 (M63-1) | left tweeter (-) | -- | V/Y | 0.5S |
| AMP #1 (M63-1) | right tweeter (+) | -- | V/R | 0.5S |
| AMP #1 (M63-1) | right tweeter (-) | -- | V/B | 0.5S |
| AMP #2 (M63-2) | left rear (+) | -- | L/O | 0.5S |
| AMP #2 (M63-2) | left rear (-) | -- | L/Br | 0.5S |
| AMP #2 (M63-2) | right rear (+) | -- | Br/W | 0.5S |
| AMP #2 (M63-2) | right rear (-) | -- | Br/R | 0.5S |
| Left rear speaker (M70) | (+) | -- | L/O | 0.5S |
| Left rear speaker (M70) | (-) | -- | L/Br | 0.5S |
| Right rear speaker (M71) | (+) | -- | Br/W | 0.5S |
| Right rear speaker (M71) | (-) | -- | Br/R | 0.5S |
| Sub woofer (M88) | (+) | -- | Gr/R | 0.5S |
| Sub woofer (M88) | (-) | -- | Gr/B | 0.5S |
| Audio decoder (M17-1/M17-2) | -- | -- | -- | -- |

### Circuit Paths (HIGH LHD)

#### Power Supply
```
Battery (+) → Fuse 3 (BATT) → [R/W, 1.25Y] → BCM-AM → Audio M18 (BATT B+)
  Constant power for memory retention

IGN switch ACC/ON → Fuse 27 → [R/Y, 1.25Y] → BCM-FF → Audio M18 (ACC B+)
  Operating power when ignition is in ACC or ON
```

#### Illumination
```
Tail lamp relay → [G/R, 0.5S] → Audio M18 (illumination input)
  Dimmer signal for display brightness — see Illumination circuit
```

#### Front Speaker Circuit (HIGH — through AMP)
```
Audio M18 (LF+) → [L/R, 0.5S] → Joint connector → AMP #1 M63-1 (LF in+)
Audio M18 (LF-) → [L/W, 0.5S] → Joint connector → AMP #1 M63-1 (LF in-)
AMP #1 M63-1 (LF out+) → [L/R, 0.5S] → Left front speaker D02 (+)
AMP #1 M63-1 (LF out-) → [L/W, 0.5S] → Left front speaker D02 (-)

Audio M18 (RF+) → [L/B, 0.5S] → Joint connector → AMP #1 M63-1 (RF in+)
Audio M18 (RF-) → [L/Y, 0.5S] → Joint connector → AMP #1 M63-1 (RF in-)
AMP #1 M63-1 (RF out+) → [L/B, 0.5S] → Right front speaker D12 (+)
AMP #1 M63-1 (RF out-) → [L/Y, 0.5S] → Right front speaker D12 (-)
```

#### Tweeter Circuit (HIGH — through AMP)
```
AMP #1 M63-1 (L tweeter out+) → [V/W, 0.5S] → Left tweeter (+)
AMP #1 M63-1 (L tweeter out-) → [V/Y, 0.5S] → Left tweeter (-)
AMP #1 M63-1 (R tweeter out+) → [V/R, 0.5S] → Right tweeter (+)
AMP #1 M63-1 (R tweeter out-) → [V/B, 0.5S] → Right tweeter (-)
```

#### Rear Speaker Circuit (HIGH — through AMP)
```
Audio M18 (LR+) → [L/O, 0.5S] → Joint connector → AMP #2 M63-2 (LR in+)
Audio M18 (LR-) → [L/Br, 0.5S] → Joint connector → AMP #2 M63-2 (LR in-)
AMP #2 M63-2 (LR out+) → [L/O, 0.5S] → Left rear speaker M70 (+)
AMP #2 M63-2 (LR out-) → [L/Br, 0.5S] → Left rear speaker M70 (-)

Audio M18 (RR+) → [Br/W, 0.5S] → Joint connector → AMP #2 M63-2 (RR in+)
Audio M18 (RR-) → [Br/R, 0.5S] → Joint connector → AMP #2 M63-2 (RR in-)
AMP #2 M63-2 (RR out+) → [Br/W, 0.5S] → Right rear speaker M71 (+)
AMP #2 M63-2 (RR out-) → [Br/R, 0.5S] → Right rear speaker M71 (-)
```

#### Sub Woofer Circuit (HIGH)
```
AMP #2 M63-2 (sub out+) → [Gr/R, 0.5S] → Sub woofer M88 (+)
AMP #2 M63-2 (sub out-) → [Gr/B, 0.5S] → Sub woofer M88 (-)
```

#### Antenna Circuit
```
Roof antenna → coaxial cable → Audio decoder M17-1 / M17-2 → Audio M18
```

#### Ground
```
Audio M18 (GND) → [B, 1.25Y] → GND (G05)
AMP #1 M63-1 (GND) → [B] → GND
AMP #2 M63-2 (GND) → [B] → GND
```

---

## HIGH Grade (with Amplifier) -- RHD

<!-- Figure: Audio System (3) HIGH RHD - power, radio, front speakers, source: SD.pdf page 152 -->
<!-- Figure: Audio System (4) HIGH RHD - rear speakers, amp, sub, source: SD.pdf page 153 -->

Same circuit topology as HIGH LHD. Power routing differs through BCM-AM / BCM-FF connectors for RHD harness. Speaker wiring colors and amplifier connections are identical.

---

## LOW Grade (without Amplifier) -- LHD

<!-- Figure: Audio System (5) LOW LHD, source: SD.pdf page 154 -->

### Component Table (LOW LHD)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 3 (BATT) | -- | -- | R/W | 1.25Y |
| Fuse 27 (ACC/ON) | -- | -- | R/Y | 1.25Y |
| BCM-AM | -- | -- | -- | -- |
| Audio (M18) | power B+ (BATT) | -- | R/W | 1.25Y |
| Audio (M18) | power B+ (ACC) | -- | R/Y | 1.25Y |
| Audio (M18) | ground | -- | B | 1.25Y |
| Audio (M18) | illumination | -- | G/R | 0.5S |
| Audio (M18) | left front speaker (+) | -- | L/R | 0.5S |
| Audio (M18) | left front speaker (-) | -- | L/W | 0.5S |
| Audio (M18) | right front speaker (+) | -- | L/B | 0.5S |
| Audio (M18) | right front speaker (-) | -- | L/Y | 0.5S |
| Audio (M18) | left rear speaker (+) | -- | L/O | 0.5S |
| Audio (M18) | left rear speaker (-) | -- | L/Br | 0.5S |
| Audio (M18) | right rear speaker (+) | -- | Br/W | 0.5S |
| Audio (M18) | right rear speaker (-) | -- | Br/R | 0.5S |
| Antenna (roof) | signal | -- | -- | coax |
| Left front speaker (D02) | (+) | -- | L/R | 0.85S |
| Left front speaker (D02) | (-) | -- | L/W | 0.85S |
| Right front speaker (D12) | (+) | -- | L/B | 0.85S |
| Right front speaker (D12) | (-) | -- | L/Y | 0.85S |
| Left rear speaker (M70) | (+) | -- | L/O | 0.85S |
| Left rear speaker (M70) | (-) | -- | L/Br | 0.85S |
| Right rear speaker (M71) | (+) | -- | Br/W | 0.85S |
| Right rear speaker (M71) | (-) | -- | Br/R | 0.85S |
| Left tweeter | (+) | -- | V/W | 0.5S |
| Left tweeter | (-) | -- | V/Y | 0.5S |
| Right tweeter | (+) | -- | V/R | 0.5S |
| Right tweeter | (-) | -- | V/B | 0.5S |

### Circuit Paths (LOW LHD)

#### Power Supply
```
Battery (+) → Fuse 3 (BATT) → [R/W, 1.25Y] → BCM-AM → Audio M18 (BATT B+)
  Constant power for memory retention

IGN switch ACC/ON → Fuse 27 → [R/Y, 1.25Y] → Audio M18 (ACC B+)
  Operating power when ignition is in ACC or ON
```

#### Front Speaker Circuit (LOW — direct drive, no AMP)
```
Audio M18 (LF+) → [L/R, 0.5S] → joint connector → Left front speaker D02 (+)
Audio M18 (LF-) → [L/W, 0.5S] → joint connector → Left front speaker D02 (-)

Audio M18 (RF+) → [L/B, 0.5S] → joint connector → Right front speaker D12 (+)
Audio M18 (RF-) → [L/Y, 0.5S] → joint connector → Right front speaker D12 (-)
```

#### Tweeter Circuit (LOW — direct drive)
```
Audio M18 (L tweet+) → [V/W, 0.5S] → Left tweeter (+)
Audio M18 (L tweet-) → [V/Y, 0.5S] → Left tweeter (-)

Audio M18 (R tweet+) → [V/R, 0.5S] → Right tweeter (+)
Audio M18 (R tweet-) → [V/B, 0.5S] → Right tweeter (-)
```

#### Rear Speaker Circuit (LOW — direct drive, no AMP)
```
Audio M18 (LR+) → [L/O, 0.5S] → joint connector → Left rear speaker M70 (+)
Audio M18 (LR-) → [L/Br, 0.5S] → joint connector → Left rear speaker M70 (-)

Audio M18 (RR+) → [Br/W, 0.5S] → joint connector → Right rear speaker M71 (+)
Audio M18 (RR-) → [Br/R, 0.5S] → joint connector → Right rear speaker M71 (-)
```

#### Ground
```
Audio M18 (GND) → [B, 1.25Y] → GND (G05)
```

---

## LOW Grade (without Amplifier) -- RHD

<!-- Figure: Audio System (6) LOW RHD, source: SD.pdf page 155 -->

Same circuit topology as LOW LHD. Power routing differs through BCM connectors for RHD harness. Speaker wiring colors are identical. No amplifier or sub woofer in LOW grade.

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G05 | Center console area | Audio unit ground | CL-32 |
| G12 | Rear shelf / trunk | Amplifiers, sub woofer | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-FF | Body Control Module | CL-8 |
| BCM-AM | Body Control Module | CL-8 |
| MD01 | Dash connector | CL-4 |
| MD03 | Dash connector | CL-4 |
| MD04 | Dash connector | CL-4 |
| MM01 | Rear connector | CL-8 |
| MM02 | Rear connector | CL-8 |
| MR01 | Rear connector | CL-9 |

---

## Component Location Index (SD-156)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| D02 | Left front speaker | CL-30 |
| D11 | Left tweeter speaker | CL-30 |
| D12 | Right front speaker | CL-30 |
| D17 | Right tweeter speaker | CL-30 |
| M18 | Audio | CL-3 |
| M17-1 | Audio (BECKER) #1 | CL-3 |
| M17-2 | Audio (BECKER) #2 | CL-3 |
| M35 | Joint connector | CL-4 |
| M63-1 | AMP #1 (HIGH) | CL-4 |
| M63-2 | AMP #2 (HIGH) | CL-4 |
| M88 | Sub woofer | CL-6 |
| M70 | Left rear speaker | CL-4 |
| M71 | Right rear speaker | CL-4 |

---

## Notes

### Audio Power Supply
- The audio receives battery voltage at all times from Fuse 3 to maintain memory function. Fuse 27 supplies battery voltage to the audio when the ignition switch is in ACC or ON for audio operation and display.
- The audio is grounded at G05(RHD model) or G12(LHD model).
- Refer to the shop manual, section BE for details.

### HIGH vs LOW Grade Differences
- HIGH grade includes AMP #1 (M63-1) for front speakers and tweeters, AMP #2 (M63-2) for rear speakers and sub woofer.
- LOW grade drives all speakers directly from the head unit -- no external amplifiers or sub woofer.
- Speaker wire colors are the same between grades. The HIGH grade inserts amplifiers in the signal path via joint connectors.

### Speaker Wire Color Summary
| Channel | (+) Color | (-) Color |
|---------|-----------|-----------|
| Left front | L/R | L/W |
| Right front | L/B | L/Y |
| Left rear | L/O | L/Br |
| Right rear | Br/W | Br/R |
| Left tweeter | V/W | V/Y |
| Right tweeter | V/R | V/B |
| Sub woofer (HIGH only) | Gr/R | Gr/B |
