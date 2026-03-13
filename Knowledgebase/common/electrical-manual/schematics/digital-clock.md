---
source: SD.pdf
chapter: SD
section: SD-104 to SD-105
pages: 104-105
title: Digital Clock
---

# Digital Clock

**SD-104 -- Digital Clock (1) Schematic**
**SD-105 -- Component Location Index**

<!-- Figure: Digital clock circuit with memory power, ACC/ON power, and dimming, source: SD.pdf page 104 -->

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 18 (HOT at all times) | -- | -- | R | 0.5S |
| Fuse 27 (HOT in ACC or ON) | -- | -- | R/W | 0.5S |
| Digital clock (M11) | memory (B+) | -- | R | 0.5S |
| Digital clock (M11) | ACC/ON power | -- | R/W | 0.5S |
| Digital clock (M11) | dimmer ground | -- | B/W | 0.5S |
| Digital clock (M11) | ground | -- | B | 0.5S |
| Joint connector (M35) | -- | -- | R | 0.5S |
| Joint connector (M36) | -- | -- | B | 1.25B |

---

## Circuit Paths

### Clock Memory Power (Always Hot)
```
Battery (+) → BCM Box Fuse 18 (HOT at all times)
  → [R, 0.5S] → BCM-IM connector
  → [R, 0.5S] → Joint connector M35
  → [R, 0.5S] → Digital clock M11 (memory B+)
```

### Clock Operating Power (ACC/ON)
```
Battery (+) → BCM Box Fuse 27 (HOT in ACC or ON)
  → [R/W, 0.5S] → BCM-KM connector
  → [R/W, 0.5S] → Digital clock M11 (ACC/ON power input)
```

### Dimmer Circuit
```
Light switch (PARK or HEAD position)
  → [B/W, 0.5S] → Digital clock M11 (dimmer ground)
  → Dimming function activates (display dims)
```

### Ground Circuit
```
Digital clock M11 (ground) → [B, 0.5S] → Joint connector M36
  → [B, 1.25B] → GND (G11)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G11 | Center console area | Digital clock ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-IM | BCM passenger compartment connector | CL-8 |
| BCM-KM | BCM passenger compartment connector | CL-8 |

---

## Component Location Index (SD-105)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| M11 | Digital clock | CL-2 |
| M35 | Joint connector | CL-4 |
| M36 | Joint connector | CL-4 |

---

## Notes

- Battery voltage is applied at all times to the digital clock from Fuse 18 to provide clock memory.
- With the ignition switch in ACC or ON, battery voltage is applied to the clock through Fuse 27. The digital clock lights up and displays the time.
- With the light switch in PARK or HEAD, the light switch provides ground to the digital clock dimmer input and the display will dim.
- The See Illuminations reference on the dimmer line indicates this dimming path ties into the main illumination dimming network.
