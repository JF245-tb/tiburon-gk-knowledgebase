---
source: SD.pdf
chapter: SD
section: SD-138 to SD-139
pages: 138-139
title: Power Outside Mirror Folding
---

# Power Outside Mirror Folding

**SD-138 -- Power Outside Mirror Folding System (1) Schematic**
**SD-139 -- Component Location Index**

<!-- Figure: Power outside mirror folding system with BCM folding/unfolding relays, left and right mirror motors, and folding switch in left power window switch, source: SD.pdf page 138 -->

---

## Component Table (SD-138)

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 13 (HOT AT ALL TIMES) | -- | -- | R | 0.85S |
| BCM folding relay (internal) | coil | -- | -- | -- |
| BCM folding relay (internal) | contact | -- | L/O | 0.85S |
| BCM unfolding relay (internal) | coil | -- | -- | -- |
| BCM unfolding relay (internal) | contact | -- | L/Br | 0.85S |
| Left power window switch (D05) | mirror fold button | -- | L/O | 0.5S |
| Left power window switch (D05) | mirror unfold button | -- | L/Br | 0.5S |
| Left outside mirror & mirror folding motor (D06) | fold (+) | -- | L/O | 0.85S |
| Left outside mirror & mirror folding motor (D06) | fold (-) | -- | L/Br | 0.85S |
| Left outside mirror & mirror folding motor (D06) | ground | -- | B | 0.85S |
| Right outside mirror & mirror folding motor (D16) | fold (+) | -- | L/O | 0.85S |
| Right outside mirror & mirror folding motor (D16) | fold (-) | -- | L/Br | 0.85S |
| Right outside mirror & mirror folding motor (D16) | ground | -- | B | 0.85S |
| BCM-EF | -- | -- | -- | -- |
| BCM-FF | -- | -- | -- | -- |
| BCM-LM | -- | -- | -- | -- |

---

## Circuit Paths

### Folding Relay Power Supply
```
Battery (+) -> Fuse 13 (HOT AT ALL TIMES)
  -> [R, 0.85S] -> BCM-FF
  -> BCM internal folding relay (contact 30)
  -> BCM internal unfolding relay (contact 30)
```

### Mirror Fold Operation
```
Left power window switch D05 (fold button pressed)
  -> [L/O, 0.5S] -> BCM-EF
  -> BCM energizes folding relay
  -> [L/O, 0.85S] -> BCM-LM
  -> [L/O, 0.85S] -> MD01 connector
  -> [L/O, 0.85S] -> Left mirror folding motor D06 (fold +)
  -> [L/O, 0.85S] -> MD02 connector
  -> [L/O, 0.85S] -> Right mirror folding motor D16 (fold +)

Return path:
  Left mirror D06 (fold -) -> [L/Br, 0.85S] -> MD01 -> GND via BCM unfolding relay (open)
  Right mirror D16 (fold -) -> [L/Br, 0.85S] -> MD02 -> GND via BCM unfolding relay (open)
```

### Mirror Unfold Operation
```
Left power window switch D05 (unfold button pressed)
  -> [L/Br, 0.5S] -> BCM-EF
  -> BCM energizes unfolding relay
  -> [L/Br, 0.85S] -> BCM-LM
  -> [L/Br, 0.85S] -> MD01 connector
  -> [L/Br, 0.85S] -> Left mirror folding motor D06 (fold -)
  -> [L/Br, 0.85S] -> MD02 connector
  -> [L/Br, 0.85S] -> Right mirror folding motor D16 (fold -)

Return path:
  Left mirror D06 (fold +) -> [L/O, 0.85S] -> MD01 -> GND via BCM folding relay (open)
  Right mirror D16 (fold +) -> [L/O, 0.85S] -> MD02 -> GND via BCM folding relay (open)
```

### Mirror Motor Polarity Reversal
```
FOLD: BCM applies +12V on L/O wire, grounds L/Br wire -> motors fold mirrors inward
UNFOLD: BCM applies +12V on L/Br wire, grounds L/O wire -> motors unfold mirrors outward
(H-bridge relay configuration inside BCM reverses motor polarity)
```

### Mirror Motor Grounds
```
Left mirror folding motor D06 -> [B, 0.85S] -> GND (G01)
Right mirror folding motor D16 -> [B, 0.85S] -> MD02 -> MDHI connector -> GND (G12)
Door switch ground -> [B, 0.5S] -> GND (G11)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G01 | Under dash, driver side | Left mirror folding motor ground | CL-32 |
| G11 | Rear body / interior | Switch ground, right mirror path | CL-33 |
| G12 | Rear body / interior | Right mirror folding motor ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-EF | BCM door connector | CL-8 |
| BCM-FF | BCM fuse/relay connector | CL-8 |
| BCM-LM | BCM mirror connector | CL-8 |
| MD01 | Driver door connector | CL-8 |
| MD02 | Passenger door connector | CL-8 |

---

## Component Location Index (SD-139)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| D05 | Left power window switch | CL-30 |
| D06 | Left outside mirror & mirror folding motor | CL-30 |
| D16 | Right outside mirror & mirror folding motor | CL-30 |

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-EF | BCM connector | CL-8 |
| BCM-FF | BCM connector | CL-8 |
| BCM-LM | BCM connector | CL-8 |
| MD01 | Door connector | CL-8 |
| MD02 | Door connector | CL-8 |

| Ground ID | Location Page |
|-----------|---------------|
| G01 | CL-32 |
| G11 | CL-33 |
| G12 | CL-33 |

---

## Notes

- Battery voltage is supplied at all times to the folding and unfolding relays from Fuse 13.
- The folding and unfolding relays of BCM control the operation of the outside mirror folding motors (left/right) by the folding switch.
- The fold/unfold button is integrated into the left power window switch assembly (D05) on the driver door.
- Motor polarity is reversed by the BCM H-bridge relay pair to change between fold and unfold directions.
- Both left and right mirrors fold/unfold simultaneously.
