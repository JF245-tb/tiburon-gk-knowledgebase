---
source: SD.pdf
chapter: SD
section: SD-148 to SD-149
pages: 148-149
title: Trunk Lid Opener
---

# Trunk Lid Opener

**SD-148 -- Trunk Lid Opener (1) Schematic**
**SD-149 -- Component Location Index**

---

## Trunk Lid Opener (1) -- Schematic (SD-148)

<!-- Figure: Trunk lid opener circuit from BCM fuse box Fuse 20 through trunk lid switch to trunk lid solenoid with ground at G06, source: SD.pdf page 148 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 20 (B+ at all times) | BCM-FF pin 22 | 22 | Y | 0.85S |
| Trunk lid switch (D10) | pin 1 | 1 | Y | 0.85S |
| Trunk lid switch (D10) | pin 2 | 2 | L | 0.85S |
| Trunk lid solenoid (R01) | pin 1 | 1 | L | 0.85S |
| Trunk lid solenoid (R01) | pin 3 | 3 | B | 0.85S |

### Circuit Paths

#### Trunk Lid Opener Power Circuit
```
Battery (+) → Fuse 20 (15A, B+ at all times, BCM Box)
  → BCM-FF pin 22 → [Y, 0.85S]
  → MD01 pin 11 → [Y, 0.85S]
  → Trunk lid switch D10 pin 1
```

#### Trunk Lid Switch to Solenoid
```
Trunk lid switch D10 pin 2 → [L, 0.85S]
  → MD01 pin 12 → [L, 0.85S]
  → MR02 pin 3 → [L, 0.85S]
  → RR02 pin 3 → [L, 0.85S]
  → Trunk lid solenoid R01 pin 1
```

#### Trunk Lid Solenoid Ground
```
Trunk lid solenoid R01 pin 3 → [B, 0.85S] → GND (G06)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G06 | Trunk area | Trunk lid solenoid ground | CL-32 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-FF | Body Control Module fuse box | CL-8 |
| MD01 | Door/dash connector | CL-8 |
| MR02 | Mid-body connector | CL-9 |
| RR02 | Rear body connector | CL-31 |

---

## Component Location Index (SD-149)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| D10 | Trunk lid switch | CL-30 |
| R01 | Trunk lid solenoid | CL-31 |

| Connector | Location Page |
|-----------|---------------|
| BCM-FF | CL-8 |
| MD01 | CL-8 |
| MR02 | CL-9 |
| RR02 | CL-31 |

| Ground ID | Location Page |
|-----------|---------------|
| G06 | CL-32 |

---

## Notes

- Battery voltage is supplied at all times to the trunk lid switch through Fuse 20 (15A).
- When the trunk lid switch is pushed (ON), current is applied to the trunk lid solenoid and the trunk lid is opened.
- The circuit is simple: constant B+ through the momentary switch directly to the solenoid, with a chassis ground at G06 in the trunk area.
- Wire routing passes through connectors MD01, MR02, and RR02 from the dash area to the trunk.
