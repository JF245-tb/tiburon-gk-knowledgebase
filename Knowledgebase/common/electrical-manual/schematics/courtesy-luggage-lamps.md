---
source: SD.pdf
chapter: SD
section: SD-188 to SD-191
pages: 188-191
title: Courtesy, Luggage Room Lamp and Key Remind Switch
_note: >
  Index originally listed this as SD-198 to SD-199, but actual manual content
  is on SD-188 to SD-191. Pages 198-199 are Air Bag System (SRS) / Memo.
---

# Courtesy, Luggage Room Lamp and Key Remind Switch

**SD-188 -- Courtesy, Luggage Room Lamp and Key Remind Switch (1) Schematic**
**SD-189 -- Courtesy, Luggage Room Lamp and Key Remind Switch (2) Schematic**
**SD-190 -- Courtesy, Luggage Room Lamp and Key Remind Switch (3) Schematic**
**SD-191 -- Component Location Index**

<!-- Figure: Courtesy, Luggage Room Lamp and Key Remind Switch (1) schematic, source: SD.pdf page 188 -->
<!-- Figure: Courtesy, Luggage Room Lamp and Key Remind Switch (2) schematic, source: SD.pdf page 189 -->
<!-- Figure: Courtesy, Luggage Room Lamp and Key Remind Switch (3) schematic, source: SD.pdf page 190 -->
<!-- Figure: Component Location Index, source: SD.pdf page 191 -->

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 18 (B+ at all times) | -- | -- | R | 2.0B |
| Fuse 19 (B+ at all times) | -- | -- | R | 2.0B |
| Left door lamp (D08) | (+) | -- | R | 0.5S |
| Left door lamp (D08) | (-) | -- | B | 0.5S |
| Right door lamp (D18) | (+) | -- | R | 0.5S |
| Right door lamp (D18) | (-) | -- | B | 0.5S |
| Driver door switch (M53) | -- | -- | Br/W | 0.5S |
| Passenger door switch (M54) | -- | -- | Br/R | 0.5S |
| Overhead console lamp (M91) | (+) | -- | R | 0.5S |
| Overhead console lamp (M91) | door sw | -- | Br | 0.5S |
| Luggage room lamp switch (M94) | -- | -- | -- | -- |
| Luggage room lamp (M94) | (+) | -- | R | 0.5S |
| Luggage room lamp (M94) | (-) | -- | B | 0.5S |
| Front room lamp switch | -- | -- | -- | -- |
| Driver satellite sensor (D09) | -- | -- | -- | -- |
| Passenger satellite sensor (D10) | -- | -- | -- | -- |
| Key remind switch (M05) | -- | -- | L/R | 0.5S |
| Instrument cluster (M10-2) | -- | -- | -- | -- |
| BCM (Body Control Module) | BCM-MR | -- | -- | -- |
| BCM (Body Control Module) | BCM-JM | -- | -- | -- |
| BCM (Body Control Module) | BCM-AI | -- | -- | -- |
| BCM (Body Control Module) | BCM-LM | -- | -- | -- |
| Transponder | -- | -- | -- | -- |
| Joint connector (M35) | -- | -- | -- | -- |
| Joint connector (M45) | -- | -- | -- | -- |
| Joint connector (M46) | -- | -- | -- | -- |
| Joint connector (M58) | -- | -- | -- | -- |

---

## Circuit Paths

### Door Lamp Circuit (SD-188)
```
Battery (+) → Fuse 19 → [R, 2.0B] → BCM-KM
  → [R, 0.5S] → Left door lamp D08 (+)
  → Left door lamp D08 (-) → [B, 0.5S] → GND (G11)

Battery (+) → Fuse 19 → [R, 2.0B] → BCM-KM
  → [R, 0.5S] → Right door lamp D18 (+)
  → Right door lamp D18 (-) → [B, 0.5S] → GND (G11)
```

### Door Switch to BCM Circuit (SD-188)
```
Driver door switch M53 (door open = ground)
  → [Br/W, 0.5S] → BCM-MR (door ajar input)

Passenger door switch M54 (door open = ground)
  → [Br/R, 0.5S] → BCM-MR (door ajar input)
```

### Overhead Console Lamp (SD-188)
```
Battery (+) → Fuse 18 → [R, 2.0B] → BCM-KM
  → [R, 0.5S] → Overhead console lamp M91 (+)
  → Overhead console lamp M91 (door sw) → [Br, 0.5S] → BCM (door open signal)
  Front room lamp switch selects: OFF / DOOR / ON
```

### Courtesy Lamp Dimming (SD-189)
```
BCM senses door switch inputs (M53, M54)
  → BCM controls ground path to door lamps and overhead console lamp
  → Lamps fade on when door opens, fade off after door closes (timed delay via BCM)
```

### Door Ajar Signal to Cluster (SD-189)
```
Driver door switch M53 → [Br/W, 0.5S] → BCM-AI
  → BCM → Instrument cluster M10-2 (door ajar indicator)

Passenger door switch M54 → [Br/R, 0.5S] → BCM-AI
  → BCM → Instrument cluster M10-2 (door ajar indicator)
```

### Luggage Room Lamp (SD-189)
```
Battery (+) → Fuse 18 → [R, 2.0B]
  → [R, 0.5S] → Luggage room lamp M94 (+)
  → Luggage room lamp switch (trunk open = closed circuit)
  → Luggage room lamp M94 (-) → [B, 0.5S] → GND (G02)
```

### Key Remind Switch (SD-189)
```
Key remind switch M05 (key inserted)
  → [L/R, 0.5S] → joint connector M58 → BCM-LM
  → BCM → chime / warning if door opened with key in ignition
  → Instrument cluster M10-2 (key-in indicator)
```

### Ignition Key Illumination (SD-190)
```
Battery (+) → Fuse 18 → [R, 2.0B]
  → [R, 0.5S] → BCM-KM → BCM-DE → BCM-JB
  → Transponder → Ignition key hole illumination
  → BCM senses door open → illuminates key hole for 10 sec
```

### Key Remind to BCM (SD-190)
```
Key remind switch M05 → [L/R, 0.5S] → BCM-LM
  → BCM processes key-in-ignition signal
  → If driver door opens with key inserted → chime warning
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G01 | Dash area | BCM ground | CL-32 |
| G02 | Rear area | Luggage room lamp ground | CL-32 |
| G06 | Rear area | Rear lamp grounds | CL-32 |
| G11 | Dash area | Door lamp grounds, courtesy lamp ground | CL-33 |
| G12 | Dash area | Instrument cluster ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-DE | Body Control Module | CL-14 |
| BCM-EE | Body Control Module | CL-14 |
| BCM-FF | Body Control Module | CL-8 |
| BCM-AI | Body Control Module | CL-8 |
| BCM-JM | Body Control Module | CL-6 |
| BCM-KM | Body Control Module | CL-6 |
| BCM-LM | Body Control Module | CL-8 |
| BCM-MR | Body Control Module | CL-8 |
| MC02 | Dash connector | CL-8 |
| MR02 | Rear connector | CL-8 |
| RR02 | Rear connector | CL-31 |

---

## Component Location Index (SD-191)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| D08 | Left door lamp | CL-30 |
| D18 | Right door lamp | CL-30 |
| M05 | Key remind switch | CL-2 |
| M10-2 | Instrument cluster | CL-2 |
| M35 | Joint connector | CL-4 |
| M45 | Joint connector | CL-4 |
| M46 | Joint connector | CL-5 |
| M53 | Left door switch | CL-5 |
| M54 | Right door switch | CL-5 |
| M58 | Joint connector | CL-4 |
| M91 | Overhead console lamp | CL-7 |
| M94 | Luggage room lamp switch | CL-7 |

---

## Notes

### Courtesy Lamps and Room Lamp
- Battery voltage is applied at all times from Fuse 18 to the front room lamp, map lamps, door ajar lamps, trunk warning indicators, and luggage lamp.
- When the appropriate switch (door switch) is activated (door open), a ground path is provided to the respective lamp, causing the lamp to go on.
- The front room lamp has a three-position switch: OFF, DOOR, and ON. In the DOOR position the lamp comes on when either door is opened. In the ON position the lamp stays on continuously.
- The front room lamp can also be turned off so that it will not come on with the door opens.
- They are turned on and off manually via the front room lamp switch.

### Courtesy Lamp Fade
- The BCM controls the courtesy lamp fade-on and fade-off timing.
- When a door opens, the BCM provides a ground path that ramps up (fade on).
- After the door closes, the BCM maintains the ground for a timed delay then gradually removes it (fade off).

### Ignition Key Reminder
- It presents the door's key BCM signal. When the key is inserted into the ignition key hole, the key remind switch closes.
- Battery voltage is applied at all times from Fuse 18 to the key remind circuit.
- When the driver's side or passenger side door is opened, the ignition key hole illumination goes on. After that, if the door is closed or 10 sec have passed, the illumination is off after about 10 sec. The signal is controlled by BCM.

### Key Hole Illumination
- When the driver's side or passenger side door is opened, the ignition key hole illumination goes on briefly (approximately 10 seconds).
- The signal is controlled by BCM via the transponder circuit.
