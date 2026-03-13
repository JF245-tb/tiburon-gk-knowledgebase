---
source: SD.pdf
chapter: SD
section: SD-170 to SD-171
pages: 170-171
title: Headlamp Leveling Device
---

# Headlamp Leveling Device

**SD-170 -- Head Lamp Leveling Device (1) Schematic**
**SD-171 -- Component Location Index**

---

## Head Lamp Leveling Device (1) -- Schematic (SD-170)

<!-- Figure: Headlamp leveling circuit showing fuse power feed, headlamp leveling switch with variable resistor, joint connector, and left/right headlamp leveling actuators, source: SD.pdf page 170 -->

### Component Table

| Component | Connector | Pin | Wire Color | Wire Size |
|-----------|-----------|-----|------------|-----------|
| Fuse (B+ at all times) | -- | -- | -- | 0.5S |
| Headlamp leveling switch (M12) | power in | -- | G/R | 0.5S |
| Headlamp leveling switch (M12) | output (variable) | -- | -- | 0.85S |
| Headlamp leveling switch (M12) | ground | -- | B | 0.85S |
| Joint connector (M36) | -- | -- | -- | 0.85S |
| Head lamp relay LOW (E46) | contact 87 | -- | -- | -- |
| Left headlamp leveling actuator (E07) | power (+) | -- | -- | 0.85S |
| Left headlamp leveling actuator (E07) | signal | -- | -- | 0.85S |
| Left headlamp leveling actuator (E07) | ground (-) | -- | B | 0.85S |
| Right headlamp leveling actuator (E27) | power (+) | -- | -- | 0.85S |
| Right headlamp leveling actuator (E27) | signal | -- | -- | 0.85S |
| Right headlamp leveling actuator (E27) | ground (-) | -- | B | 0.85S |
| EM01 connector | -- | -- | -- | -- |

### Circuit Paths

#### Headlamp Leveling Switch Power Supply
```
Battery (+) → Fuse (B+ at all times) → [G/R, 0.5S]
  → EM01 → [0.5S] → Headlamp leveling switch M12 (power in)
```

#### Headlamp Leveling Switch to Actuators
```
Headlamp leveling switch M12 (variable output) → [0.85S]
  → EM01 → [0.85S] → Joint connector M36
  → [0.85S] → See Illumination path
  → [0.85S] → Left headlamp leveling actuator E07 (signal)
  → [0.85S] → Right headlamp leveling actuator E27 (signal)
```

#### Actuator Power from Head Lamp Relay
```
Head lamp relay LOW E46 (contact 87) → [1.25B]
  → Left headlamp leveling actuator E07 (power +)
  → Right headlamp leveling actuator E27 (power +)
  (Actuators only operate when low beam headlamps are ON)
```

#### Headlamp Leveling Actuator Ground
```
Left headlamp leveling actuator E07 (ground) → [B, 0.85S] → GND (G11)
Right headlamp leveling actuator E27 (ground) → [B, 0.85S] → GND (G11)
```

#### Switch Ground
```
Headlamp leveling switch M12 (ground) → [B, 0.85S] → GND (G11)
```

---

## Ground Points

| Ground ID | Location | Components | Location Page |
|-----------|----------|------------|---------------|
| G11 | Dash area | Headlamp leveling switch ground, actuator grounds | CL-33 |

---

## Connector Reference

| Connector | Description | Location Page |
|-----------|-------------|---------------|
| EM01 | Engine compartment connector | CL-14 |

---

## Component Location Index (SD-171)

| Component | Description | Location Page |
|-----------|-------------|---------------|
| E07 | Left head lamp | CL-10 |
| E27 | Right head lamp | CL-11 |
| E46 | Head lamp relay (LOW) | CL-12 |
| E56 | Joint connector | CL-12 |
| M12 | Head lamp leveling switch | CL-2 |
| M36 | Joint connector | CL-4 |

| Connector | Location Page |
|-----------|---------------|
| EM01 | CL-14 |

| Ground ID | Location Page |
|-----------|---------------|
| G11 | CL-33 |

---

## Notes

- The headlamps should be aimed properly according to the number of passengers and the loading weight in the luggage area. To adjust the headlamp beam level, rotate the headlamp leveling switch. The higher the number of the switch position, the lower the headlamp beam level. Always keep the headlamp beam at the proper leveling position, or the headlamps may dazzle other road users.
- When the light switch is in the HEAD position, battery voltage is supplied to the left/right headlamp leveling actuators through the headlamp relay(s) contact. The actuators operate based on the variable resistor position (built in the headlamp leveling switch) signal sent through a wire.
- The leveling switch contains a variable resistor that outputs a control signal proportional to switch position.
- Both left and right actuators receive the same control signal from the switch through the joint connector M36, ensuring both headlamps maintain the same beam angle.
