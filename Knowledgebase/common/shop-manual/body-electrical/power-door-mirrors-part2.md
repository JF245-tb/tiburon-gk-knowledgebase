---
source: BE.pdf
chapter: BE
section: BE-64 to BE-80
pages: 65-81
engine: V6
title: Power Door Mirrors (Part 2)
---

# Indicators and Gauges (continued)

## Fuel Sender

1. Using an ohmmeter, measure the resistance between terminals 1 and 3 at each float level.

| Float position | F | 1/2 | E |
|---|---|---|---|
| Resistance (ohm) | 6 | 32.5 | 97 |

<!-- Figure: Fuel sender float positions and resistance measurement, source: BE.pdf page 65 -->

2. Also check that the resistance changes smoothly when the float is moved from "E" to "F".

## Low Fuel Level Sensor

1. Connect a test lamp (12V, 3.4W) and the battery to the sensor. Immerse the sensor in water.

2. The lamp should be off while the thermistor is submerged in the water, and should illuminate when the sender is taken out of the water.

> **NOTE**
> If there is a malfunction, replace the fuel sender as an assembly.

> **CAUTION**
> After completing this test, wipe the sender dry and reinstall it in the fuel tank.

<!-- Figure: Low fuel level sensor test setup with 3.4W lamp and 12V battery, source: BE.pdf page 65 -->

## Engine Coolant Temperature Gauge

1. Disconnect the wiring connector from the engine coolant temperature sender in the engine compartment.

2. Turn the ignition switch ON. Check that the gauge needle indicates cold. Turn the ignition switch OFF.

3. Connect a 12V 3.4 watt test bulb between the harness side connector terminal 2 and ground.

4. Turn the ignition switch ON.

5. Verify that the test bulb flashes and that the indicator moves to HOT.

If operation is not as specified, replace the sender. Then recheck the system.

<!-- Figure: Engine coolant temperature gauge test setup, source: BE.pdf page 65 -->

## Engine Coolant Temperature Sender

1. Using an ohmmeter, measure the resistance between the terminal 2 and ground.

2. If the resistance value is not as shown in the table, replace the temperature sender.

| Temperature (deg C) | 60 | 85 | 110 | 125 |
|---|---|---|---|---|
| Resistance (ohm) | 143.4 | 58.1 | 26.9 | 17.5 |

<!-- Figure: Coolant temperature sender resistance table, source: BE.pdf page 65 -->

---

# Indicators and Gauges (continued)

## Oil Pressure Switch

1. Check that there is continuity between the switch's terminal and ground with the engine stopped.

2. Check that there is no continuity between the terminal and ground with the engine running.

3. If operation is not as specified, replace the switch.

<!-- Figure: Oil pressure switch with ohmmeter test, source: BE.pdf page 66 -->

## Oil Pressure Warning Lamp

1. Disconnect the connector from the warning switch and ground the terminal on the wire harness side connector.

2. Turn the ignition switch ON. Check that the warning lamp lights up. If the warning lamp doesn't light, test the bulb or inspect wire harness.

<!-- Figure: Oil pressure warning lamp test circuit with battery, source: BE.pdf page 66 -->

## Brake Fluid Level Warning Switch

1. Remove the connector from the switch located at the brake fluid reservoir.

2. Verify that continuity exists between switch terminals 1 and 2 while pressing down switch (float) with a rod.

<!-- Figure: Brake fluid level warning switch test, source: BE.pdf page 66 -->

## Brake Fluid Level Warning Lamp

1. Start the engine.

2. Release the parking brake.

3. Remove the connector from the brake fluid level warning switch.

4. Ground the connector at the harness side.

5. Verify that the warning lamp lights.

<!-- Figure: Brake fluid level warning lamp test, source: BE.pdf page 66 -->

## Parking Brake Switch

The parking brake switch is a push type located under the parking brake lever. To adjust, move the switch mount up and down to the optimal position.

1. Check that there is continuity between the terminal and switch body with the switch ON (Lever is pulled).

2. Check that there is no continuity between the terminal and switch body with the switch OFF (Lever is released).

If continuity is not as specified, replace the switch or inspect its ground connection.

<!-- Figure: Parking brake switch location, source: BE.pdf page 66 -->

---

## Seat Belt Warning Lamp

With the ignition switch turned ON, verify that the lamp glows.

| Seat belt condition | Warning lamp |
|---|---|
| Fastened | OFF |
| Not fastened | ON |

## Door Switch

Remove the door switch and check for continuity between the terminals.

**Connector [D05]**

| Terminal | 1 | 2 | 3 |
|---|---|---|---|
| Position | | | |
| Free (Door open) | O------- | | -------O |
| Push (Door close) | | | |

<!-- Figure: Door switch connector D05 and continuity table, source: BE.pdf page 67 -->

## Seat Belt Switch

1. Remove the connector from the switch.

2. Check for continuity between terminals.

| Seat belt condition | Continuity |
|---|---|
| Fastened | Non-conductive (4-5) |
| Not fastened | Conductive (5) |

<!-- Figure: Seat belt switch inspection diagram, source: BE.pdf page 67 -->

---

# Multi Gauge

## General

Multi-gauge unit is located at the upper portion of audio system and it indicates engine torque, instantaneous fuel consumption, and battery voltage.

### 1. Engine torque gauge

It indicates the instantaneous torque variation according to RPM of the vehicle. Drive can notice the instantaneous torque variation with acceleration and deceleration speed, recently a lot of consumers want their sports car to have a torque gauge to indicate what the engine torque level easily. Engine torque gauge indicates the engine torque value by communicating CAN signals from engine ECU.

### 2. Instantaneous fuel consumption gauge

It indicates instantaneous fuel consumption according to the variation of the vehicle speed. The gauge indicates "0" if the vehicle speed is at 100km and fuel is consumed 10L. The lower the pointer of a pointer the number, the lower the vehicle spends fuel for driving, on the other hand, the higher it digits the number, the higher it does. Instantaneous fuel consumption gauge inputs the speed signal and fuel injection signal. Speed signal comes directly from the speed sensor and fuel injection signal is from the engine ECU.

At very low speeds, the instrument cannot practically calculate the instantaneous fuel consumption. If the vehicle speed is increasing by constant fuel quantity per hour, the gauge indicates the value lower and lower.

In case of the vehicle at idle, there is only fuel consumption with no signal, so the speed fuel consumption is beyond 20(L/100km), with the pointer at the below than it doesn't show the average fuel consumption but only the instantaneous one.

### 3. Volt gauge

Volt gauge makes a driver properly response during driving by displaying the battery voltage information. Before ignition turned on, when the key is inserted into "ignition switch on" position, it displays the battery voltage, after ignition key turned on, it displays the ignition voltage(= battery voltage).

If the voltage is at 8.5V or below, the pointer of the gauge moves to the lower than 8V and if it is at 16V or more, it moves to the lower than 16V.

If the input value is between 8.5V and 16V, the volt gauge shows the analog display. Each ignition voltage is displayed during the ignition key turned on.

<!-- Figure: Multi gauge general description, source: BE.pdf page 68 -->

## Specifications

| Items | Display | Input signal | Gauge operating type |
|---|---|---|---|
| Engine torque | 0~400 Nm | ECU engine (CAN communication) | Stepper motor |
| Instantaneous fuel consumption | 0~20 L/100Km | Speed signal, Fuel injection signal (CAN communication) | Stepper motor |
| Battery voltage | - | Battery voltage | Stepper motor |

## Components

<!-- Figure: Multi gauge unit showing torque gauge, fuel consumption gauge, voltage gauge, and connector M42, source: BE.pdf page 69 -->

### Pin Connection [M42]

| Pin No. | Description | Pin No. | Description |
|---|---|---|---|
| 1 | CAN (Low) | 7 | CAN (High) |
| 2 | - | 8 | - |
| 3 | Ignition (+) | 9 | Illumination (+) |
| 4 | Speed input | 10 | Illumination (-) |
| 5 | Fuel injection input | 11 | - |
| 6 | Battery voltage | 12 | Ground |

## Circuit Diagram

<!-- Figure: Multi gauge circuit diagram showing CAN interface, power supply, micro-com, torque gauge, instantaneous fuel consumption gauge, and voltage gauge with connector M42 pinout, source: BE.pdf page 70 -->

**Pin Functions:**
- Pin 1: CAN(low) -> CAN Interface
- Pin 7: CAN(high) -> CAN Interface
- Pin 6: Battery voltage -> Power Supply (via diode)
- Pin 3: Ignition
- Pin 2: NC
- Pin 4: Speed input -> MICRO-COM
- Pin 5: Fuel injection input -> MICRO-COM
- Pin 8: NC
- Pin 9: ILL (+) -> Illumination lamp
- Pin 10: ILL (-)
- Pin 11: NC
- Pin 12: GND

**Connector [M42]:**

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| 7 | 8 | 9 | 10 | 11 | 12 |

---

# Power Door Locks

## Components

<!-- Figure: Power door locks showing door lock knob and power door lock actuator locations on vehicle, source: BE.pdf page 71 -->

## Power Door Lock Actuators

### Inspection

1. Disconnect the actuator connector from the wiring harness.

2. Apply battery voltage (12V) to each terminal as shown in the table and verify that the actuator operates correctly.

**Connector [D06]**

| Position | Terminal 3 | Terminal 4 |
|---|---|---|
| Front left [D06] - Lock | (+) | (-) |
| Front left [D06] - Unlock | (-) | (+) |
| Front right [D16] - Lock | (+) | (-) |
| Front right [D16] - Unlock | (-) | (+) |

<!-- Figure: Power door lock actuator connector D06 pinout, source: BE.pdf page 71 -->

---

# Power Door Mirrors

## Components

<!-- Figure: Power door mirrors showing power door mirror connector on mirror assembly and power door mirror switch on door panel, source: BE.pdf page 72 -->

## Power Door Mirror Switch

### Inspection

1. Remove the power door mirror switch from the door trim panel.

2. Check for continuity between the terminals in each switch position according to the table. If continuity is not as specified, replace the power door mirror switch.

**Connector [D04]**

| | 1 | 2 | 3 |
|---|---|---|---|
| 4 | 5 | 6 | 7 | 8 |

**Continuity Table [D04]:**

| Class | Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| LEFT HAND | UP | O-- | | | --O | | | | |
| | DOWN | | O-- | | --O | | | | |
| | OFF | | | | | | | | |
| | LEFT | O-- | | | | --O | | | |
| | RIGHT | | O-- | | | --O | | | |
| RIGHT HAND | UP | | | | | | O-- | | --O |
| | DOWN | | | | | | | O-- | --O |
| | OFF | | | | | | | | |
| | LEFT | | | | | | O-- | | --O |
| | RIGHT | | | | | | | O-- | --O |

(O----O indicates continuity between terminals)

<!-- Figure: Power door mirror switch continuity table, source: BE.pdf page 73 -->

## Circuit Diagram

<!-- Figure: Power door mirror circuit diagram showing switch D04, mirror left motor (Up/Down, Left/Right), mirror right motor (Up/Down, Left/Right), and connector D06/D06, source: BE.pdf page 74 -->

The circuit diagram shows the power door mirror switch [D04] with connections to:
- Left mirror motors (Up/Down and Left/Right)
- Right mirror motors (Up/Down and Left/Right)
- Connectors [D04] and [D06]

**Connector [D04]:**

| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 | 7 | 8 |

## Power Door Mirror Actuator

### Inspection

1. Disconnect the power door mirror connector from the harness.

2. Apply battery voltage to each terminal as shown in the table and verify that the mirror operates properly.

**Connector [D06] - Mirror Motor:**

| Terminal | 6 | 7 | 8 |
|---|---|---|---|
| Position | | | |
| UP | (+) | | (-) |
| DOWN | (-) | | (+) |
| OFF | | | |
| LEFT | (+) | (-) | |
| RIGHT | (-) | (+) | |

Heater(+): Left/Right
Heater(-): Up/Down

<!-- Figure: Power door mirror actuator connector D06 and test table, source: BE.pdf page 75 -->

## Mirror Heater Inspection

**Connector [D06]:**

| Terminal | 1 | 2 |
|---|---|---|
| Position | | |
| Heater | (+) | (-) |

<!-- Figure: Mirror heater test connection at D06, source: BE.pdf page 75 -->

## Mirror Folding Inspection

<!-- Figure: Mirror folding mechanism showing R1 and R2 rotation points, source: BE.pdf page 75 -->

---

# Power Windows

## Components

<!-- Figure: Power windows components showing power window motor and power window switch locations on vehicle, source: BE.pdf page 76 -->

## Power Window Motor

### Inspection

Connect the motor terminals directly to battery voltage (12V) and check that the motor operates smoothly. Next, reverse the polarity and check that the motor operates smoothly in the reverse direction. If the operation is abnormal, replace the motor.

<!-- Figure: Power window motor bench test setup, source: BE.pdf page 76 -->

## Power Window Switch

### Circuit Diagram

<!-- Figure: Power window switch circuit diagram showing power window main switch and power window sub switch, with connectors D04, D06, and D15, including window lock switch, driver folding switch, and tail lamp switch connections, source: BE.pdf page 77 -->

### Inspection

#### Power Window Main Switch

1. Remove the switch from the door trim panel.

2. Check for continuity between the terminals. If continuity is not as specified in the table, replace the power window switch.

**Connector [D06]:**

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|

| Terminal | FRONT LEFT | | FRONT RIGHT | |
|---|---|---|---|---|
| Position | 2 | 10 | 4 | 7 | 2 | 10 | 5 | 1 | 2 | 7 |
| UP | O--O | | O--O | | | | O--O | | | |
| OFF | | | | | | | | | | |
| DOWN | O--O | | O--O | | | | O--O | | | |

<!-- Figure: Power window main switch connector D06 continuity table, source: BE.pdf page 78 -->

#### Power Window Sub Switch

**Connector [D15]:**

| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 | 7 | 8 |

| Terminal | 6 | 8 | 7 | 1 |
|---|---|---|---|---|
| Position | | | | |
| UP | O----- | | -----O | |
| OFF | | | | |
| DOWN | | O----- | -----O | |

<!-- Figure: Power window sub switch connector D15 continuity table, source: BE.pdf page 78 -->

#### Window Lock Switch

**Connector [D06]:**

| Terminal | 5 | 10 |
|---|---|---|
| Position | | |
| NORMAL | O----------O |
| LOCK | |

<!-- Figure: Window lock switch continuity, source: BE.pdf page 78 -->

#### Mirror Folding Switch

**Connector [D06]:**

| Terminal | 1 | 7 |
|---|---|---|
| Position | | |
| FOLD | O----------O |
| UNFOLD | O----------O |

<!-- Figure: Mirror folding switch continuity, source: BE.pdf page 78 -->

---

# Rear Window Defogger

## Rear Window Defogger Printed Heater

### Inspection

> **CAUTION**
> Wrap tin foil around the end of the voltmeter test lead to prevent damaging the heater line. Apply finger pressure on the tin foil, moving the tin foil along the grid line to check for open circuits.

<!-- Figure: Rear window defogger printed heater inspection setup showing twister probe, finger pressure, printed heater line, and tin foil, source: BE.pdf page 79 -->

1. Turn on the defogger switch and use a voltmeter to measure the voltage of each heater line at the glass center point. If a voltage of approximately 6V is indicated by the voltmeter, the heater line of the rear window is considered satisfactory.

<!-- Figure: Voltmeter showing 6 volts (approximately) at center point with 4 volts on each side, source: BE.pdf page 79 -->

2. If a heater line is burned out between the center point and (+) terminal, the voltmeter will indicate 12V.

<!-- Figure: Burned out point near positive terminal showing 12 Volts reading, source: BE.pdf page 79 -->

3. If a heater line is burned out between the center point and (-) terminal, the voltmeter will indicate 0V.

<!-- Figure: Burned out point near negative terminal showing 0V reading, source: BE.pdf page 79 -->

4. To check open circuits, slowly move the test lead in the direction that the open circuit seems to exist. Try to find a point where a voltage is generated or changes to 0V. The point where the voltage has changed is the open-circuit point.

<!-- Figure: Voltage change location indicating open circuit point, source: BE.pdf page 79 -->

5. Use an ohmmeter to measure the resistance of each heater line between a terminal and the center of a grid line, and between the same terminal and the center of the adjacent grid line. Compare the values. The section with the broken heater line will have a resistance twice as that in other sections. In the affected section, move the test lead to a position where the resistance sharply changes.

<!-- Figure: Ohmmeter measurement showing section with broken grid line having twice resistance, with positive terminal side (Section A) and negative terminal side (Section B), source: BE.pdf page 80 -->

### Repair of Broken Heater Line

Prepare the following items:

1. Conductive paint.
2. Paint thinner.
3. Masking tape.
4. Silicone remover.

5. Using a thin brush:
   Wipe the glass adjacent to the broken heater line, clean with silicone remover and attach the masking tape as shown. Shake the conductive paint container well, then apply the paint with the brush. Remove the tape and allow sufficient time for drying before applying power. For a better finish, scrape away excess deposits with a knife after the paint has completely dried. (Allow 24 hours.)

<!-- Figure: Masking tape placement for heater line repair, source: BE.pdf page 80 -->

---

# Windshield Wiper/Washer

## Components

<!-- Figure: Windshield wiper/washer components showing wiper motor & linkage assembly, motor wiring harness connector, cap nut, cap, wiper arm & blade locations on vehicle, source: BE.pdf page 81 -->

**Tightening Torques: Nm (kg-cm, lb-ft)**

| Component | Torque |
|---|---|
| Bolt (wiper motor & linkage to cowl) | 7-11 (70-110, 5.1-8.0) |
| Cap nut | 23-33 (230-390, 16.9-20.6) |
| Cap | 23-29 (230-290, 16.9-20.6) |
