---
source: EE.pdf
chapter: EE
section: EE-43 to EE-46
pages: 43-46
engine: V6
title: Cruise Control System
---

# Cruise Control System

## System Block Diagram
<!-- EDAH200 -->

<!-- Figure: Cruise control system block diagram showing signal flow between components, source: EE.pdf page 43 -->

```
Throttle body ──> Accelerator pedal ──> Diagnostic connector
                                              |
Throttle valve                          Cruise control switch
                                              |
ELC 4-speed ────────────────────> Resume/Accel / Set/Coast
Automatic transaxle                           |
control module                          Actuator & unit assembly ──> Cancel switches
                                              |
                                        Vehicle speed sensor
```

*CC = Cruise Control

## Component Parts and Function Outline
<!-- EDAH200 -->

| Component Part | Function |
|---|---|
| Vehicle speed sensor | Converts vehicle speed to pulses. |
| Cruise control module (CCM) | Receives signals from sensor and control switch; CCM controls all automatic speed control function. |
| Actuator | Regulates the throttle valve to the set opening by signals from the CCM. |
| Control switch | |
| - CRUISE main switch | Switch for automatic speed control power supply. |
| - SET/RESUME switch | Controls automatic speed control functions by SET (COAST) and RESUME (ACCEL). |
| - CRUISE main switch indicator | Illuminates when CRUISE main switch is ON (Built into cluster). |
| Cancel switch | Sends cancel signals to the CCM. |
| Stop lamp switch / Clutch switch (M/T) | Cancels cruise. |
| Transaxle range switch | Controls the overdrive ON and OFF, based on signals from the CCM for the CC. |
| Data link connector | By connecting the voltmeter or scan tool, control module diagnostic codes may be read. |

## Components Location
<!-- EDCC030 -->

<!-- Figure: Cruise control switch and SET/RESUME switch on steering wheel, source: EE.pdf page 44 -->
<!-- Figure: Cruise control switch close-up on steering column, source: EE.pdf page 44 -->
<!-- Figure: Vehicle speed sensor location on transaxle, source: EE.pdf page 44 -->
<!-- Figure: Clutch pedal position switch location, source: EE.pdf page 44 -->
<!-- Figure: Stop lamp switch location on brake pedal bracket, source: EE.pdf page 44 -->

## Components
<!-- EDBC040 -->

<!-- Figure: Engine bay view showing cruise control cable routing and actuator assembly, source: EE.pdf page 45 -->

1. Accelerator cable and throttle assembly connection
2. Cruise control cable and pulley assembly connection
3. Actuator unit connector
4. Pulley assembly
5. Actuator unit

## Removal and Installation
<!-- EDBA017 -->

1. Remove the battery negative terminal.
2. Disconnect the accelerator cable and cruise control cable from throttle assembly by turning throttle lever to full open position.
3. Disconnect the accelerator cable from accelerator pedal connection.
4. Remove the accelerator cable mounting bolts.

<!-- Figure: Accelerator cable removal at pedal connection, source: EE.pdf page 45 -->

5. Remove the actuator and unit assembly mounting bolt.
6. Installation is the reverse order of removal.

## Inspection
<!-- EDBA030 -->

### Condition

- Turn A/C and all lights OFF. Inspect and adjust at no load.
- Warm the engine until idle is stabilized. Confirm that the idle speed is at the specified RPM.
- Turn the ignition switch OFF.

### Procedure

1. Confirm there are no sharp bends in the cables.
2. Depress the accelerator pedal and check if the throttle lever moves smoothly from fully closed to fully open.
3. Check the inner cables for correct slack.
4. If there is too much slack or no slack, adjust the play by the following procedures.

### Service Hint

1. If the cable is very loose, the loss of speed going uphill will be large.
2. If the cable is too tight, idle RPM will be high.

## Cable Adjustment

1. Assemble the cable to actuator and unit assembly.
2. Tighten nut "b" after pulling the cable tightly.
3. Back nut "b" off one turn.
4. Tighten nut "a".
5. Cable should have approximately 1mm of slack with the actuator and unit against the stop.

<!-- Figure: Cable adjustment diagram showing nut "a" and nut "b" positions on actuator, source: EE.pdf page 46 -->

## Parts Inspection
<!-- EDBC060 -->

### Stop Lamp Switch

After operating the stop lamp switch, check for continuity between the terminals.

| Condition | Terminals 1-2 | Terminals 3-4 |
|---|---|---|
| Not pushed (pedal released) | Continuity | No continuity |
| Pushed (pedal depressed) | No continuity | Continuity |

<!-- Figure: Stop lamp switch terminal identification and continuity test setup, source: EE.pdf page 46 -->

**Connector circuits:**
- Terminals 1-2: Cruise circuit -- closed at rest (cruise enabled), opens when brake pedal is pressed (cancels cruise)
- Terminals 3-4: Stop lamp circuit -- open at rest (lamps off), closes when brake pedal is pressed (lamps on)

<!-- Figure: Stop lamp switch connector pin diagram showing cruise circuit (pins 1-2) and stop lamp circuit (pins 3-4), source: EE.pdf page 46 -->
