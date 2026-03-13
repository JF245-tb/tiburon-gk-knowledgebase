---
source: SD.pdf
chapter: SD
section: SD-50 to SD-51
pages: 50-51
title: Starting System
---

# Starting System

**SD-50 -- Starting System (1) Schematic**
**SD-51 -- Component Location Index**

---

## Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Battery (+) terminal | E28 | -- | R | 20B |
| Battery ground | -- | -- | B | 20B |
| Fusible link (80A) | -- | -- | R | 5.0B |
| Fusible link (50A) | -- | -- | R | 3.0B |
| Joint connector | E56 | -- | R | 2.0B |
| Ignition switch (M04) | -- | ST | R/B | 1.25B |
| Start relay (E41) | coil 85 | -- | R/Y | 1.25B |
| Start relay (E41) | coil 86 | -- | B | 0.85S |
| Start relay (E41) | contact 30 | -- | R | 2.0B |
| Start relay (E41) | contact 87 | -- | R/Y | 2.0B |
| Burglar alarm relay (M41) | coil | -- | R/Y | 3.0W |
| Burglar alarm relay (M41) | contact | -- | R/Y | 3.0W |
| Starter solenoid (E52/E67) | S terminal | -- | R/Y | 2.25B |
| Starter motor (E53/E68) | B terminal | -- | R | 8.0B |
| Flywheel magnetic lever | -- | -- | -- | -- |
| Overrunning clutch | -- | -- | -- | -- |
| Starter clutch pedal position switch (C17/C117) | 1 | -- | R/B | 1.25B |
| Starter clutch pedal position switch (C17/C117) | 2 | -- | R/Y | 1.25B |
| Transaxle range switch (C31/C101) | -- | -- | R/B | 2.0W |
| Engine control relay (E42) | -- | -- | -- | -- |

### 2.0L-Specific

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Transaxle range switch | C31 | -- | R/B | 2.0W |
| Starter clutch pedal position switch | C17 | -- | R/B | 1.25B |
| Joint connector | C41 | -- | -- | -- |
| Start solenoid | E67 | -- | R/Y | 2.0B |
| Starter motor (+) | E68 | -- | R | 8.0B |

### 2.7L-Specific

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Transaxle range switch | C101 | -- | R/B | 2.0W |
| Starter clutch pedal position switch | C117 | -- | R/B | 1.25B |
| Joint connector | C141 | -- | -- | -- |
| Start solenoid | E52 | -- | R/Y | 2.0B |
| Starter motor (+) | E53 | -- | R | 8.0B |

---

## Circuit Paths

### Main Start Circuit (Manual Transaxle)
```
Battery (+) E28 → [R, 20B] → Fusible link 80A → [R, 5.0B] → Fusible link 50A → [R, 3.0B]
  → Joint connector E56 → [R, 2.0B] → Start relay E41 (contact 30)
  → Start relay E41 (contact 87) → [R/Y, 2.0B] → Starter solenoid S terminal
  → Starter motor B terminal ← [R, 8.0B] ← Battery (+) direct
```

### Start Relay Coil Circuit
```
IGN SW (ST position) → [R/B, 1.25B] → Starter clutch pedal position switch (C17/C117)
  → [R/Y, 1.25B] → Burglar alarm relay (M41) → [R/Y] → Start relay E41 coil
  → [B, 0.85S] → GND (G15)
```

### Start Relay Coil Circuit (Automatic Transaxle)
```
IGN SW (ST position) → [R/B, 2.0W] → Transaxle range switch (C31/C101, P/N position)
  → [R/Y, 1.25B] → Burglar alarm relay (M41) → Start relay E41 coil
  → [B, 0.85S] → GND (G15)
```

### ECM Feed (from Start Relay)
```
Start relay E41 → [R/Y] → ECM via connectors:
  EC01/2 (2L) → BCM-LM
  EC01/1 (RL) → BCM-KM
  MC01/2 (2L) → OCH-KM
  MC01/1 (RL) → OCH-KM
```

---

## Ground Points

| Ground ID | Location | Components |
|-----------|----------|------------|
| G15 | Engine compartment | Start relay coil ground, battery ground cable |

---

## Connector Reference (from SD-51)

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| BCM-KM | Body Control Module | CL-8 |
| BCM-LM | Body Control Module | CL-8 |
| EC01 | Engine compartment connector | CL-14 |
| EE01 | Engine compartment connector | CL-14 |
| EE03 | Engine compartment connector | CL-14 |
| EM01 | Engine compartment connector | CL-14 |
| MC01 | Engine compartment connector | CL-8 |
| MC101 | Engine compartment connector | CL-8 |
| MC201 | Engine compartment connector | CL-8 |

---

## Component Location Index (SD-51)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| C31 | Transaxle range switch (2.0L) | CL-18 |
| C17 | Starter clutch pedal position switch (2.0L) | CL-19 |
| C41 | Joint connector (2.0L) | CL-21 |
| C101 | Transaxle range switch (2.7L) | CL-21 |
| C117 | Starter clutch pedal position switch (2.7L) | CL-23 |
| C141 | Joint connector (2.7L) | CL-25 |
| E28 | Battery (+) terminal | CL-11 |
| E41 | Start relay | CL-12 |
| E56 | Joint connector | CL-12 |
| E52 | Start solenoid (2.7L) | CL-13 |
| E53 | Starter motor (+) (2.7L) | CL-13 |
| E67 | Start solenoid (2.0L) | CL-13 |
| E68 | Starter motor (+) (2.0L) | CL-13 |
| M04 | Ignition switch | CL-2 |
| M41 | Burglar alarm relay | CL-4 |

---

## Notes

- Battery voltage is applied at all times from the positive battery terminal to the ignition switch and the normally open start relay contacts.
- When the ignition switch is turned to START and the transaxle range switch (automatic transaxle) is in P/N position or the starter clutch pedal position switch (manual transaxle) is closed, battery voltage is applied through the burglar alarm relay to the starter relay coil.
- The start relay coil energizes, the start relay contacts close, and battery voltage is applied to the starter solenoid. The motor engages to start the engine.
- For the 2.7L V6 build: the starter solenoid is E52, starter motor is E53.
