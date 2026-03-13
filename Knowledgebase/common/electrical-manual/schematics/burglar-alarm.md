---
source: SD.pdf
chapter: SD
section: SD-112 to SD-113
pages: 112-113
title: Burglar Alarm Horn System
---

# Burglar Alarm Horn System

**SD-112 -- Burglar Alarm Horn System (1) Schematic**
**SD-113 -- Component Location Index**

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse 13 (B+ at all times) | -- | -- | R | 2.0W |
| Burglar alarm horn relay (M39) | coil | -- | L/R | 0.5S |
| Burglar alarm horn relay (M39) | contact 30 | -- | R | 2.0W |
| Burglar alarm horn relay (M39) | contact 87 | -- | L/B | 0.85S |
| Burglar alarm horn (E17) | (+) | -- | L/B | 0.85S |
| Burglar alarm horn (E17) | (-) | -- | B | 0.85S |
| Hood switch 2.7L (C129) | -- | -- | Br/W | 0.5S |
| Hood switch 2.0L (C29) | -- | -- | Br/W | 0.5S |
| Hood switch 1.6L (C229) | -- | -- | Br/W | 0.5S |
| Tail gate unlock switch (R03) | -- | -- | V/Y | 0.5S |
| BCM (Body Control Module) | EF | -- | -- | -- |
| BCM (Body Control Module) | HM | -- | -- | -- |
| BCM (Body Control Module) | JM | -- | -- | -- |
| BCM (Body Control Module) | KM | -- | -- | -- |
| BCM (Body Control Module) | LM | -- | -- | -- |
| Left door lock actuator | -- | -- | -- | -- |
| Right door lock actuator | -- | -- | -- | -- |

---

## Circuit Paths

### Burglar Alarm Horn Power Circuit
```
Battery (+) → Fuse 13 → [R, 2.0W] → Burglar alarm horn relay M39 (contact 30)
  → Burglar alarm horn relay M39 (contact 87) → [L/B, 0.85S]
  → Burglar alarm horn E17 (+)
  → Burglar alarm horn E17 (-) → [B, 0.85S] → GND (G15)
```

### Burglar Alarm Relay Coil Circuit
```
BCM → [L/R, 0.5S] → Burglar alarm horn relay M39 (coil)
  → GND
```

### Hood Switch Input to BCM
```
Hood switch (C129 / 2.7L) → [Br/W, 0.5S] → BCM
  Hood switch terminal → GND (G06) when hood open
```

### Tail Gate Unlock Switch Input to BCM
```
Tail gate unlock switch (R03) → [V/Y, 0.5S] → BCM
```

### Door Lock Actuator Detect Circuits to BCM
```
Left door lock actuator → BCM (detection inputs)
Right door lock actuator → BCM (detection inputs)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G06 | Engine compartment | Hood switch ground | CL-32 |
| G11 | Dash area | BCM ground | CL-33 |
| G12 | Dash area | BCM ground | CL-33 |
| G15 | Engine compartment | Burglar alarm horn ground | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-EF | Body Control Module | CL-8 |
| BCM-HM | Body Control Module | CL-8 |
| BCM-JM | Body Control Module | CL-8 |
| BCM-KM | Body Control Module | CL-8 |
| BCM-LM | Body Control Module | CL-8 |
| EM01 | Engine compartment | CL-14 |
| MC01 | Main connector | CL-8 |
| MC101 | Main connector | CL-8 |
| MC201 | Main connector | CL-14 |
| MC202 | Main connector | CL-14 |
| MR02 | Rear connector | CL-9 |
| RR02 | Rear connector | CL-31 |

---

## Component Location Index (SD-113)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C29 | Hood switch (2.0L) | CL-24 |
| C129 | Hood switch (2.7L) | CL-23 |
| C229 | Hood switch (1.6L) | CL-28 |
| E17 | Burglar alarm horn | CL-10 |
| M39 | Burglar alarm horn relay | CL-4 |
| R03 | Tail gate unlock switch | CL-31 |

---

## Notes

- Battery voltage is applied at all times to the burglar alarm horn relay from Fuse 13.
- The BCM detects the left door lock actuator, right door lock actuator, tail gate unlock switch, and hood switch and sends a signal to the burglar alarm horn relay so as to operate the burglar alarm horn.
- The hood switch provides a ground signal to the BCM when the hood is open.
- For the 2.7L V6 build: the hood switch is C129 (location CL-23).
