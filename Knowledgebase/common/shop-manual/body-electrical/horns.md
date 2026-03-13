---
source: BE.pdf
chapter: BE
title: Horns
section_pages: 44-45
printed_pages: BE-43 to BE-44
note: >
  These PDF pages fall within the ETACS (Electronic Time and Alarm Control System)
  chapter. Content covers room lamp, seat belt warning, over speed warning chime,
  folding mirror control, rear fog lamp control, and the beginning of the anti-theft
  function. Filed under "horns" per extraction-script page mapping.
---

# ETACS (Electronic Time and Alarm Control System) — Continued

## Room Lamp (Illuminated Entry with Fade)

When the front door (driver side) is opened, the room lamp is turned on.

When front door is closed, or is left open for 5.5 seconds, the room lamp brightness fades out over approximately 0.5 seconds.

When the seat door is closed, the room lamp will drop to 75% intensity then fade out over 5.5 to 5 seconds.

If the ignition 2 is switched on when room light is fading out, the room lights switch off immediately.

If the door-open signal is on for less than 0.1 seconds, the room lamp functions as door-open detection.

Lamps must not flicker during fade operation, if a door opens or closes.

When transmitter (TX) unlock is received, room lamps are turned on in less than 0.1 second for maximum 30 seconds.

While room lamp is on due to TX unlock, if another TX unlock is received, then room lamp is again on for 30 seconds.

When TX lock/unlock mode is executed during 30-second TX unlock, lamp is turned off immediately.

If TX lock (2-arm state) is received during fade-out, the room lamp is switched off immediately.

Door locking functions should not be influenced by room lamp delay functions.

### Time Specification

| Parameter | Value |
|-----------|-------|
| T1 | 5.5 to 5 sec |
| T2 | 30 sec |

<!-- Figure: Room lamp timing diagram showing door switch, station/fade states, source: BE.pdf page 44 -->

## Seat Belt Warning

### 1) Seat Belt Warning Indicator

Whenever the ignition 1 is turned on the seat belt warning indicator is illuminated for total time 6 seconds, with period 0.6 sec and duty rate 50%. It is not extinguished if the seat belt is sensed as fastened.

If ignition 1 is already on and the seat belt is removed, the indicator is illuminated for total time 6 seconds, with period 0.6 sec and duty rate 50%.

If ignition 1 is switched off in while the indicator is illuminated, the illumination is switched off immediately.

### 2) Seat Belt Warning Chime

Whenever the ignition 1 is turned on the seat belt warning chime is sounded for total time 6 sec, with period 0.6 sec and duty 50%. The warning chime is silenced immediately if the seat belt is sensed as fastened.

If ignition 1 is already on and the seat belt is removed, the chime is sounded for total time 6 seconds, with period 0.6 sec and duty rate 50%.

If ignition 1 is switched off in while the chime is sounding, the chime is switched off immediately.

<!-- Figure: Seat belt warning timing diagram (ONE BELL pattern), source: BE.pdf page 44 -->

### Time Specification

| Parameter | Value |
|-----------|-------|
| T1 | 6 x 1 sec |
| T2 | 0.4 to 0.1 sec |
| T3 | 0.3 to 0.1 sec |

## Over Speed Warning Chime

If the IGN2 is on, and the over speed input is grounded by cluster, chime is sounded until over speed input by cluster is opened.

<!-- Figure: Over speed warning timing diagram (CHIME BELL pattern), source: BE.pdf page 44 -->

## Folding Mirror Unit

If ACC is on, with each press of the folding mirror switch, the mirror fold and unfold outputs will operate alternatively for 16 to 0.4 sec. A second press of the button during an output shall cause the opposite output to be issued.

The folding mirror switch is pressed within 30 seconds after the ACC signal is removed, the mirror outputs (folding or unfolding) will operate for 16 sec. If, during the mirror operation, the folding mirror switch is pressed again then the opposite operation will commence. If the ACC signal is present and the button is pressed again, if the ACC signal is removed, the folding motor mirror will operate for a further 16 sec.

The mirror will operate for a further 16 to 0.4 sec.

### Time Specification

| Parameter | Value |
|-----------|-------|
| T1 | 30 sec |
| T2 | 16 to 0.4 sec |

<!-- Figure: Folding mirror timing diagram showing mirror switch, mirror fold, mirror unfold signals, source: BE.pdf page 45 -->

## Rear Fog Lamp Control

When IGN is on and:
- Tail lamps are on by switch or auto light or front fog switch is on, then if rear fog switch is connected the rear fog lamps are turned on.

<!-- Figure: Rear fog lamp control timing diagram showing IGN, headlamp, tail lamp, front fog SW, rear fog SW, rear fog lamp signals, source: BE.pdf page 45 -->

## Anti-Theft Function

### 1) Arming

By pressing the remote key lock button will result in a 0.5-second pulse issued to lock all doors.

Pressing the remote keypad unlock button once will result in a 0.5-second unlock pulse issued to unlock all doors.

As part of the arming sequence the alarm first enters a pre-armed state before fading into the armed state. The pre-armed state can be reached from the following states: the start inhibit state or the disarmed (ignition) state. The arming of the alarm can be achieved by a press of the lock button on the remote key.

In the pre-armed state the visible and audible warnings are disabled.

This system enters, and stays in it is in the pre-armed state, until 0.6 sec, check armed. The lock outputs go to arm state, actuator lock, the alarm enters the armed state (no key in ignition), warning switch (no key in ignition).

On entering the arm state, a single flash of the hazard lamps is given, period of cycle 2 second, duty rate 50%.

If TX lock signal is received when a door, tail gate or hood is open, then lock output is given and a flash of the hazard lamps.

After the armed state is entered, if a lock signal is received then a single flash of the hazard lamps is given, period of cycle 2 second, duty rate 50%.

The pre-armed state cannot be reached by locking the car with the keys.

### Time Specification

| Parameter | Value |
|-----------|-------|
| T1 | Max 2 sec |
| T3 | 1.0 to 0.2 sec |

<!-- Figure: Anti-theft arming timing diagram showing TX lock, lock command, arm state, hazard lamp signals, source: BE.pdf page 45 -->
