---
source: SD.pdf
chapter: SD
section: SD-166 to SD-169
pages: 166-169
title: Auto Lights
---

# Auto Lights

**SD-166 -- Auto Lights (1) Schematic -- BCM, Light Switch, Relays, Auto Light Sensor**
**SD-167 -- Auto Lights (2) Schematic -- Power Feed, Light Sensor, Rear Window**
**SD-168 -- Component Location Index**
**SD-169 -- Memo**

---

## Auto Lights (1) -- BCM, Light Switch, Relays (SD-166)

<!-- Figure: Auto lights circuit showing BCM connections, multifunction light switch in AUTO position, head lamp relay, tail lamp relay, dimmer/passing switch, and joint connector distribution to headlamps, source: SD.pdf page 166 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fusible link (HOT AT ALL TIMES) | -- | -- | R | 3.0W |
| Fuse 7 (B+ at all times) | -- | -- | R | 2.0W |
| Fuse 14 (B+ at all times) | -- | -- | R | 2.0W |
| BCM-CE connector | -- | -- | -- | -- |
| BCM-DE connector | -- | -- | -- | -- |
| SC08-CE connector | -- | -- | -- | -- |
| SC08-148 connector | -- | -- | -- | -- |
| Multifunction switch (M01-2) | AUTO | -- | -- | 0.85S |
| Multifunction switch (M01-2) | HEAD | -- | -- | 0.85S |
| Multifunction switch (M01-2) | PARK | -- | -- | 0.85S |
| Multifunction switch (M01-2) | FLASH | -- | -- | -- |
| Head lamp relay LOW (E46) | coil 85 | -- | -- | 0.85S |
| Head lamp relay LOW (E46) | coil 86 | -- | B | 0.85S |
| Head lamp relay LOW (E46) | contact 30 | -- | -- | 1.25B |
| Head lamp relay LOW (E46) | contact 87 | -- | -- | 1.25B |
| Head lamp relay HIGH (E51) | coil 85 | -- | -- | 0.85S |
| Head lamp relay HIGH (E51) | coil 86 | -- | B | 0.85S |
| Head lamp relay HIGH (E51) | contact 30 | -- | -- | 1.25B |
| Head lamp relay HIGH (E51) | contact 87 | -- | -- | 1.25B |
| Tail lamp relay | coil | -- | -- | 0.85S |
| Tail lamp relay | contact | -- | -- | -- |
| Dimmer/passing switch (M01-1) | HIGH | -- | -- | 0.85S |
| Dimmer/passing switch (M01-1) | FLASH | -- | -- | 0.85S |
| Joint connector (E56) | -- | -- | -- | -- |
| Joint connector (M35) | -- | -- | -- | 1.25B |
| Joint connector (M36) | -- | -- | -- | 1.25B |
| Instrument cluster (M10-1) | -- | -- | -- | 0.85S |
| Left head lamp (E07) | low beam | -- | -- | 1.25B |
| Right head lamp (E27) | low beam | -- | -- | 1.25B |
| EM01 connector | -- | -- | -- | -- |

### Circuit Paths

#### Multifunction Switch -- AUTO Position to BCM
```
Multifunction switch M01-2 (AUTO position) → [0.85S]
  → BCM-CE → BCM (auto light logic)
```

#### BCM Auto Light Relay Control -- Head Lamp
```
BCM (auto light output) → [0.85S] → Head lamp relay LOW E46 (coil 85)
Head lamp relay LOW E46 (coil 86) → [B, 0.85S] → GND
  → Relay energized when BCM determines low light conditions
```

#### BCM Auto Light Relay Control -- Tail Lamp
```
BCM (tail lamp output) → [0.85S] → Tail lamp relay (coil)
  → Tail lamp relay energized simultaneously with head lamp relay
```

#### Head Lamp Low Beam Feed (through Relay)
```
Battery (+) → Fusible link → Fuse 7 → [R, 2.0W]
  → Head lamp relay LOW E46 (contact 30)
  → Head lamp relay LOW E46 (contact 87) → [1.25B]
  → Joint connector E56 → M35 → Left head lamp E07 (low beam)
  → Joint connector E56 → M36 → Right head lamp E27 (low beam)
```

#### Head Lamp High Beam Feed (Dimmer Switch)
```
Battery (+) → Fusible link → Fuse 14 → [R, 2.0W]
  → Head lamp relay HIGH E51 (contact 30)
  → Head lamp relay HIGH E51 (contact 87) → [1.25B]
  → Left head lamp E07 (high beam)
  → Right head lamp E27 (high beam)
```

#### Dimmer/Passing Switch
```
Dimmer/passing switch M01-1 (HIGH position) → [0.85S]
  → Head lamp relay HIGH E51 (coil) → High beams ON
Dimmer/passing switch M01-1 (FLASH position) → [0.85S]
  → Head lamp relay HIGH E51 (coil) → High beams momentary ON
```

#### To Nighttime Light Switch Path
```
To nighttime/exterior light switch → [0.85S] → BCM-CE
```

---

## Auto Lights (2) -- Power Feed, Light Sensor (SD-167)

<!-- Figure: Auto lights continuation showing BCM overhead connector, power feed from fusible links through BCM, auto light sensor with photo-transistor, and rear window defroster proximity, source: SD.pdf page 167 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse (circuit fuse) | -- | -- | -- | -- |
| Power relay (E46) | -- | -- | -- | -- |
| BCM-HM connector | pin 19 | 19 | -- | 0.85S |
| BCM-LR connector | pin 1 | 1 | -- | 2.0W |
| BCM-UR connector | pin 10 | 10 | -- | 2.0W |
| BCM-JM connector | pin 7 | 7 | -- | 0.85S |
| Auto light sensor (M07) | power (+) | -- | -- | 0.5S |
| Auto light sensor (M07) | signal (output) | -- | -- | 0.5S |
| Auto light sensor (M07) | ground (-) | -- | B | 0.85S |
| Light sensor connector | -- | -- | -- | -- |

### Circuit Paths

#### Auto Light Sensor Power Supply
```
BCM → [0.5S] → Auto light sensor M07 (power +)
Auto light sensor M07 (ground) → [B, 0.85S] → GND (G12)
```

#### Auto Light Sensor Signal to BCM
```
Auto light sensor M07 (signal output) → [0.5S] → BCM-JM
  → BCM processes ambient light level
  → BCM controls head lamp relay and tail lamp relay accordingly
```

#### BCM Power Feed
```
Ground fusible → [2.0W] → BCM-LR pin 1 (constant power)
Ground fusible → [2.0W] → BCM-UR pin 10 (constant power)
```

#### BCM Ground
```
BCM → GND (G12, G11)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G11 | Dash area | BCM ground | CL-33 |
| G12 | Dash area | BCM ground, auto light sensor ground | CL-33 |
| G15 | Engine compartment | Headlamp grounds | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-CE | Body Control Module | CL-14 |
| BCM-1M | Body Control Module | CL-8 |
| BCM-JM | Body Control Module | CL-8 |
| BCM-LM | Body Control Module | CL-8 |
| BCM-LR | Body Control Module | CL-8 |
| EM01 | Engine compartment | CL-14 |

---

## Component Location Index (SD-168)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| E07 | Left head lamp | CL-10 |
| E27 | Right head lamp (H/LP) | CL-11 |
| E46 | Head lamp relay (LOW) | CL-12 |
| E51 | Head lamp relay (HIGH) | CL-12 |
| E56 | Joint connector | CL-12 |
| M01-2 | Multifunction switch | CL-2 |
| M10-1 | Instrument cluster | CL-3 |
| M07 | Auto light sensor | CL-4 |
| M35 | Joint connector | CL-4 |

| Connector | Location Page |
|-----------|---------------|
| BCM-CE | CL-8 |
| BCM-1M | CL-8 |
| BCM-JM | CL-8 |
| BCM-LM | CL-8 |
| BCM-LR | CL-8 |
| EM01 | CL-14 |

| Ground ID | Location Page |
|-----------|---------------|
| G11 | CL-33 |
| G12 | CL-33 |
| G15 | CL-33 |

---

## Notes

- For the visibility of the driver, the auto light sensor controls the headlamps and tail lamps automatically through the BCM relay coil control. When the light switch is in AUTO and the auto light sensor detects low intensity of illumination, ground is provided to the headlamp relays through the auto light sensor relay path.
- Battery voltage is supplied to the head lamps through the headlamp fuse and headlamp relay(s) high/low contacts.
- The auto light sensor sends output signals to the BCM, and the BCM controls the tail lamp relay. The headlamps and tail lamps can be controlled independently by using the light switch and dimmer/passing switch.
- When the multifunction switch is in the AUTO position, the BCM monitors the auto light sensor output and automatically engages headlamps and tail lamps based on ambient light levels.
- The auto light sensor is a photo-transistor type sensor mounted on the dashboard that detects ambient light intensity.
