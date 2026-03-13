---
source: BE.pdf
chapter: BE
title: Power Door Mirrors Part 1
pages: 72-75
page_labels: BE-71 through BE-74
section: Power Door Mirrors
---

# POWER DOOR MIRRORS

## COMPONENTS

_ETOC1800_

<!-- Figure: Power door mirror assembly showing power door mirror connector on the mirror base (left) and power door mirror switch on the door trim panel (right), source: BE.pdf page 72 -->

- **Power door mirror connector** -- located at the base of the door mirror assembly
- **Power door mirror switch** -- mounted in the driver door trim panel

---

## POWER DOOR MIRROR SWITCH

### INSPECTION

_ETOC1850_

1. Remove the power door mirror switch from the door trim panel.

2. Check for continuity between the terminals in each switch position according to the table. If continuity is not as specified, replace the power door mirror switch.

#### Connector [D04] Pin Layout

```
     [D04]
  +--+--+--+
  | 1| 2| 3|
  +--+--+--+--+--+
  | 4| 5| 6| 7| 8|
  +--+--+--+--+--+
```

<!-- Figure: Connector D04 pin layout -- 3 pins on top row (1-3), 5 pins on bottom row (4-8), source: BE.pdf page 73 -->

#### Switch Continuity Table [D04]

Circles with a line between them indicate continuity between those terminals.

**LEFT HAND (L/R selector set to L):**

| Position | Connected Terminals |
|----------|---------------------|
| UP       | 1 --- 7             |
| DOWN     | 2 --- 7             |
| OFF      | (no continuity)     |
| LEFT     | 1 --- 6             |
| RIGHT    | 2 --- 6             |

**RIGHT HAND (L/R selector set to R):**

| Position | Connected Terminals |
|----------|---------------------|
| UP       | 3 --- 8             |
| DOWN     | 4 --- 8             |
| OFF      | (no continuity)     |
| LEFT     | 3 --- 7             |
| RIGHT    | 4 --- 7             |

---

## CIRCUIT DIAGRAM

_ETOC1900_

<!-- Figure: Power door mirror circuit diagram showing rear view of the switch assembly, connector [D04], left mirror connector [D06], and right mirror connector [D06]. The switch contains a L/R selector and 4-way directional joystick. Internal wiring routes battery voltage and ground through the joystick to the selected mirror motor pair, source: BE.pdf page 74 -->

The circuit diagram shows the power door mirror switch (rear view of switch assembly in door panel) with connections to:

- **Connector [D04]** -- 8-pin switch connector (wiring harness side)
- **Connector [D06]** -- Left mirror (Mirror L/H) motor assembly
- **Connector [D06]** -- Right mirror (Mirror R/H) motor assembly

The switch contains:

1. **L/R selector** -- routes the joystick outputs to either the left or right mirror
2. **4-way directional joystick** -- UP, DOWN, LEFT, RIGHT movement

Mirror motors are controlled by polarity reversal:
- The UP/DOWN motor pair controls mirror tilt (vertical axis)
- The LEFT/RIGHT motor pair controls mirror pan (horizontal axis)

#### Connector [D04] Circuit Diagram View

```
  [D04]
  +---+---+---+---+
  |   | X |   | X |
  +---+---+---+---+
```

<!-- Figure: Connector D04 viewed from circuit diagram (alternate pinout view), source: BE.pdf page 74 -->

---

## POWER DOOR MIRROR ACTUATOR

### INSPECTION

_ETOC1950_

1. Disconnect the power door mirror connector from the harness.

2. Apply battery voltage to each terminal as shown in the table and verify that the mirror operates properly.

#### Connector [D06] Overview

The D06 connector on each mirror assembly carries the following functions:

```
  Heater(+)
      |
  Heater(-)   Left/Right   Up/Down
```

<!-- Figure: Connector D06 showing pin orientation with heater terminals and motor terminals labeled, source: BE.pdf page 75 -->

#### Mirror Actuator Direction Table [D06]

Apply battery voltage (12V) across the indicated terminals. (+) = battery positive, (-) = battery negative.

| Position  | Terminal 6 | Terminal 7 | Terminal 8 |
|-----------|-----------|-----------|-----------|
| **UP**    | (+)       |           | (-)       |
| **DOWN**  | (-)       |           | (+)       |
| **OFF**   |           |           |           |
| **LEFT**  | (+)       | (-)       |           |
| **RIGHT** | (-)       | (+)       |           |

**Summary:**

- **UP/DOWN movement:** Apply 12V across terminals 6 and 8
  - UP: positive on 6, negative on 8
  - DOWN: negative on 6, positive on 8
- **LEFT/RIGHT movement:** Apply 12V across terminals 6 and 7
  - LEFT: positive on 6, negative on 7
  - RIGHT: negative on 6, positive on 7

---

### MIRROR FOLDING INSPECTION

<!-- Figure: Mirror folding inspection diagram showing resistance measurement points R1 and R2 at the mirror pivot base, source: BE.pdf page 75 -->

Measure resistance at the mirror folding motor connections on connector [D06].

#### Folding Motor -- Connector [D06]

| Measurement | Terminal 3 | Terminal 4 |
|-------------|-----------|-----------|
| R1          | (probe)   | (probe)   |
| R2          | (probe)   | (probe)   |

Check continuity/resistance across terminals 3 and 4 of connector [D06] for the folding motor circuit.

---

### MIRROR HEATER INSPECTION

_ETOC196C_

#### Heater -- Connector [D06]

| Position | Terminal 1 | Terminal 2 |
|----------|-----------|-----------|
| Heater   | (probe)   | (probe)   |

<!-- Figure: Connector D06 heater terminals 1 and 2, source: BE.pdf page 75 -->

Check the mirror heater by measuring resistance across terminals 1 and 2 of connector [D06]. If the heater element shows continuity (finite resistance), the heater is functioning. If open circuit (infinite resistance), replace the mirror assembly.

---

## Connector Summary

### [D04] -- Power Door Mirror Switch (8-pin)

| Pin | Function (LEFT HAND mode) | Function (RIGHT HAND mode) |
|-----|--------------------------|---------------------------|
| 1   | Joystick common (UP/LEFT) | --                        |
| 2   | Joystick common (DOWN/RIGHT) | --                     |
| 3   | --                        | Joystick common (UP/LEFT) |
| 4   | --                        | Joystick common (DOWN/RIGHT) |
| 5   | --                        | --                        |
| 6   | L/H mirror return (LEFT/RIGHT) | --                  |
| 7   | L/H mirror return (UP/DOWN) | R/H mirror return (LEFT/RIGHT) |
| 8   | --                        | R/H mirror return (UP/DOWN) |

### [D06] -- Power Door Mirror Connector (8-pin per mirror)

| Pin | Function         |
|-----|-----------------|
| 1   | Heater (+)       |
| 2   | Heater (-)       |
| 3   | Folding motor A  |
| 4   | Folding motor B  |
| 5   | --               |
| 6   | Mirror motor common |
| 7   | Left/Right motor |
| 8   | Up/Down motor    |
