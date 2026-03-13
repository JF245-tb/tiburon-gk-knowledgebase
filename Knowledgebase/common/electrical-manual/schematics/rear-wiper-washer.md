---
source: SD.pdf
chapter: SD
section: SD-110 to SD-111
pages: 110-111
title: Rear Wiper and Washer
---

# Rear Wiper and Washer

**SD-110 -- Rear Wiper & Washer (1) Schematic**
**SD-111 -- Component Location Index**

<!-- Figure: Rear wiper motor, washer motor, multifunction switch, rear wiper relay, and BCM integration, source: SD.pdf page 110 -->

---

## Component Table (SD-110)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 8 (HOT in ACC or ON) | -- | -- | R/L | 0.85S |
| Fuse 15 (HOT in ACC or ON) | -- | -- | W/R | 0.85S |
| Rear wiper relay (BCM internal) | coil | -- | -- | -- |
| Rear wiper motor (R13) | motor (+) | -- | G/R | 0.85S |
| Rear wiper motor (R13) | park switch | -- | G/B | 0.85S |
| Rear wiper motor (R13) | ground | -- | B | 0.85S |
| Washer motor -- rear (M76) | (+) | -- | W/R | 0.85S |
| Washer motor -- rear (M76) | (-) | -- | B | 0.85S |
| Multifunction switch (M01-1) | R.WIPER | -- | G/R | 0.85S |
| Multifunction switch (M01-1) | R.WASH | -- | W/R | 0.85S |
| Multifunction switch (M01-1) | INT/OFF/ON | -- | G/B | 0.85S |
| Joint connector (M34) | -- | -- | -- | -- |
| Joint connector (E24) | -- | -- | -- | -- |
| BCM-FF | -- | -- | -- | -- |
| BCM-KM | -- | -- | -- | -- |
| BCM-LR | -- | -- | -- | -- |

---

## Circuit Paths

### Rear Wiper Motor Power
```
Battery (+) -> BCM Box Fuse 8 (HOT in ACC or ON)
  -> [R/L, 0.85S] -> BCM-FF
  -> BCM internal rear wiper relay
  -> [G/R, 0.85S] -> BCM-KM
  -> [G/R, 0.85S] -> Joint connector M34
  -> [G/R, 0.85S] -> MR02 connector
  -> [G/R, 0.85S] -> Rear wiper motor R13 (motor input)
  -> [B, 0.85S] -> GND (G05)
```

### Rear Wiper Park Switch Circuit
```
Rear wiper motor R13 (park switch)
  -> [G/B, 0.85S] -> MR02 connector
  -> [G/B, 0.85S] -> Joint connector M34
  -> [G/B, 0.85S] -> BCM-KM
  -> BCM controls park position via internal relay switching
```

### Multifunction Switch -- Rear Wiper Control
```
Multifunction switch M01-1 (R.WIPER position: OFF/INT/ON)
  -> [G/R, 0.85S] -> BCM-KM
  -> BCM interprets switch position and controls rear wiper relay

INT position: BCM cycles rear wiper relay on/off per intermittent timing
ON position: BCM holds rear wiper relay closed for continuous operation
OFF position: BCM allows motor to run to park, then opens relay
```

### Rear Washer Motor Circuit
```
Battery (+) -> BCM Box Fuse 15 (HOT in ACC or ON)
  -> [W/R, 0.85S] -> Multifunction switch M01-1 (R.WASH position, push forward)
  -> [W/R, 0.85S] -> Joint connector M34
  -> [W/R, 0.85S] -> MR02 connector
  -> [W/R, 0.85S] -> Rear washer motor M76 (+)
Rear washer motor M76 (-) -> [B, 0.85S] -> GND (G06)
```

### Rear Washer + Wiper Interaction
```
When WASH position is selected:
  -> Rear intermittent wiper motor controls the operation of the washer motor
     through a relay coil
  -> Rear wiper operates several times after the washer fluid sprays
     onto the rear window
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G05 | Rear body | Rear wiper motor ground | CL-32 |
| G06 | Rear body | Rear washer motor ground | CL-32 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-CE | BCM engine compartment connector | CL-14 |
| BCM-FF | BCM fuse/relay connector | CL-8 |
| BCM-KM | BCM passenger compartment connector | CL-8 |
| EMC1 | Engine compartment connector | CL-14 |
| MM03 | Multifunction switch connector | CL-8 |
| MR02 | Rear body connector | CL-8 |
| MR62 | Rear body connector | CL-31 |

---

## Component Location Index (SD-111)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| E24 | Front & rear washer motor | CL-11 |
| M01-1 | Multifunction switch | CL-2 |
| M46 | Joint connector | CL-5 |
| M76 | Rear intermittent wiper motor | CL-6 |
| R13 | Rear wiper motor | CL-51 |

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-CE | BCM connector | CL-14 |
| BCM-FF | BCM connector | CL-8 |
| BCM-KM | BCM connector | CL-8 |
| EMC1 | Engine compartment connector | CL-14 |
| MM03 | Connector | CL-9 |
| MR02 | Rear connector | CL-8 |
| MR62 | Rear connector | CL-31 |

| Ground ID | Location Page |
|-----------|---------------|
| G05 | CL-32 |
| G06 | CL-32 |

---

## Notes

- The rear wiper switch has 3 positions: OFF, INT, and ON. Based on these switch position signals, the BCM controls the operation of the wiper motor through a relay coil.
- When the ON position is selected, the window wiper operates continuously.
- When the INT position is selected, the wiper operates intermittently.
- Rear washer operation: when the WASH position is selected, the rear intermittent wiper motor controls the operation of the washer motor through a relay coil. The rear wiper operates several times after the washer fluid sprays onto the rear window.
- Page SD-111 contains the component location index and circuit description text only.
