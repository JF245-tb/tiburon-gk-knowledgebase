---
source: BE.pdf
chapter: BE
title: Power Door Locks
section_pages: 46-47
printed_pages: BE-45 to BE-46
note: >
  These PDF pages fall within the ETACS (Electronic Time and Alarm Control System)
  chapter. Content covers the disarm function, alarm function (European and
  non-European countries), and operation during alarm conditions. Filed under
  "power-door-locks" per extraction-script page mapping.
---

# ETACS — Anti-Theft Function (Continued)

## Disarm Function

Disarming can be performed while the alarm is armed, or alarming, or after alarming. The alarm can be disarmed by the following method:

- Pressing the unlock button on the TX key. The hazard lamps shall be flashed twice for 2 sec period of (cycle), 50% duty rate.

> **NOTE:** If there is a condition where a CAN RX and/or a sensor (e.g. an arm stay, then arm state should be immediately cancelled). This means that the driver is inside the vehicle before pushing TX lock, so the system should not arm.

In the disarm state the visible and audible warnings are disabled and start is enabled.

In the disarm state, if TX key unlock command is received, the hazard lamps are flashed for 2 seconds, for period of cycle 1 sec, 50% duty rate.

Disarm state cannot be reached using the door locks by key.

### Time Specification

| Parameter | Value |
|-----------|-------|
| T1 | 27 to 2 sec |
| T2 | 0.5 to 0.1 sec |

<!-- Figure: Disarm function timing diagram showing TX unlock, unlock command, disarm state, hazard lamp signals, source: BE.pdf page 46 -->

## Alarm Function

### 1) European Countries

Once armed, should any door, hood or the tailgate be opened, then:

- Audible (horn) and visual (hazard lamp) warnings are issued, for 27 seconds duration. The horn warning is continuously occurring during this period. The hazard lamps operate with 1 sec period, 50% duty rate.

The alarm is given in the case where a door is opened with a key.

### Time Specification

| Parameter | Value |
|-----------|-------|
| T1 | 27 to 2 sec |
| T3 | 75 to 1 sec |
| T3 | 0.5 to 0.1 sec |

<!-- Figure: European alarm timing diagram showing door/hood/tailgate, horn, hazard lamp, start inhibit signals, source: BE.pdf page 46 -->

### Non-European Countries

Once armed, should any door, hood or the tailgate be opened, then:

- Start relay drive output is disabled, so starting is inhibited.
- Audible (horn) and visual (hazard lamp) warnings are issued, for three cycles, each cycle 27 to 1 sec duration, on 1 to 1 sec, off. The horn warning is continuously occurring during this period. The hazard lamps operate with 1 sec period, 50% duty rate during the on period.

The alarm is given in the case where a door is opened with a key.

After this time, the system maintains the start inhibit state, where no audible and visual warnings are issued but engine starting is not possible.

<!-- Figure: Non-European alarm timing diagram, source: BE.pdf page 46 -->

## Operation During Alarm Conditions

### 1) Cancelling Audible Alarm with the Remote Transmitter

**CASE 1: Door Closed**

During or after alarming and then closing all doors and TX lock signal is received within 0.5 sec:

- The lock command is executed with 0.5 sec.
- Horn and start inhibition are OFF.
- Hazard lamp is flashed one time (period: 2 sec, duty 50%, within 2 sec).
- The state goes to arming mode (after a lock state check).
- The start is enabled.

### Time Specification

| Parameter | Value |
|-----------|-------|
| T1 | 0.5 sec |
| T1 | 1.0 to 0.2 sec |

<!-- Figure: Case 1 (Door Closed) timing diagram showing door SW, lock command, horn, start inhibit, hazard lamp, armed/alarming states, source: BE.pdf page 47 -->

**CASE 2: Door Open**

During or after alarming, with a door open and a TX lock signal is received. Then:

- The lock command is executed with 0.5 sec.

**ON:**
- Horn is disabled and start is enabled after continuation of actuator lock.

At this time, when the door is closed:

- Hazard lamp is flashed one time (period: 2 sec, duty 50%).
- The state goes to arming mode.

<!-- Figure: Case 2 (Door Open) timing diagram showing door SW, lock command, horn, start inhibit, hazard lamp, armed/alarming states, source: BE.pdf page 47 -->

### Time Specification

| Parameter | Value |
|-----------|-------|
| T1 | 0.5 sec |
| T1 | 1.0 to 0.2 sec |

### 2) New Alarm Conditions

Second alarm condition during alarming:

When another alarm occurs during alarming, the alarm continues to sound for the remaining time and sound for the renewed time of warning signal. The alarm continues to sound after the second alarm condition is removed.

New alarm condition occurs after alarming (with all entrances closed):

- The horn is ON 3 times (EC area; one time for 27 sec).
- Hazard ON.
- Start disabled.
- Hazard lamps flash during the ON time of horn.

New alarm condition occur after alarming (with any entrance open):

If another entrance is opened, the BCM keeps start disabled and there is no horn output.

<!-- Figure: New alarm conditions timing diagram, source: BE.pdf page 47 -->

### 3) Key Operation During Alarm

After the alarm state or start inhibit state are entered, if door warning switch on (key in ignition) and IGN 2 ON, if IGN 2 state is changed to OFF within 30 sec, remain in alarm state.

<!-- Figure: Key operation during alarm timing diagram, source: BE.pdf page 47 -->
