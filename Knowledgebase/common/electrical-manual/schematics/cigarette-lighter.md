---
source: SD.pdf
chapter: SD
section: SD-102 to SD-103
pages: 102-103
title: Cigarette Lighter
---

# Cigarette Lighter

**SD-102 -- Cigarette Lighter (1) Schematic**
**SD-103 -- Component Location Index**

<!-- Figure: Cigarette lighter circuit with illumination and ashtray lamp, source: SD.pdf page 102 -->

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 23 (HOT in ACC or ON) | -- | -- | R/O | 0.85S |
| Cigarette lighter (M31) | power | 3 | R/O | 0.85S |
| Cigarette lighter (M31) | illumination | 2 | R/O | 0.5S |
| Cigarette lighter (M31) | ground | 1 | B | 0.5S |
| Ashtray illumination lamp | (+) | -- | R/O | 0.5S |
| Ashtray illumination lamp | (-) | -- | B | 0.5S |

---

## Circuit Paths

### Cigarette Lighter Power Circuit
```
Battery (+) → BCM Box Fuse 23 (15A, HOT in ACC or ON)
  → [R/O, 0.85S] → BCM-KM connector pin 1
  → [R/O, 0.85S] → Cigarette lighter M31 pin 3 (power, PUSH-ON element)
  → Heating element → [B, 0.5S] → GND (G11)
```

### Illumination Circuit
```
See Illuminations → [R/O, 0.5S] → Cigarette lighter M31 pin 2 (ILL.)
  → Illumination lamp → [B, 0.5S] → GND (G11)
Cigarette lighter M31 pin 2 → [R/O, 0.5S] → Ashtray illumination lamp (+)
  → Ashtray illumination lamp (-) → [B, 0.5S] → GND (G11)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G11 | Center console area | Cigarette lighter ground, ashtray illumination ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-KM | BCM passenger compartment connector | CL-8 |

---

## Component Location Index (SD-103)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| M31 | Cigarette lighter | CL-3 |

---

## Notes

- Battery voltage is applied from Fuse 23 (15A) when the ignition switch is in ACC or ON.
- When the lighter element is depressed (push), it completes the circuit to ground through the heating element.
- When the element becomes sufficiently heated, it is spring-released and the circuit opens.
- The illumination lamp and ashtray lamp share the same illumination feed and ground path through G11.
