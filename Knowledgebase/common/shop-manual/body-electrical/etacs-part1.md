---
source: BE.pdf
chapter: BE
title: ETACS (Part 1)
pages: 33-43
section: ETACS (Electronic Time and Alarm Control System)
---

# ETACS (Electronic Time and Alarm Control System)

## Description

Body Control Module (BCM) unify the functions of ETACS module, clock relay, chime bell, mirror folding unit, flasher unit, door lock relay, chime bell and keyless antenna. BCM provides diagnosis with Hi-Scan to find out input or output error.

<!-- Figure: Body Control Module (BCM) installed location, source: BE.pdf page 33 -->

## BCM Block Diagram

### Individual Control Module

- ETACS module
- Chime bell
- Mirror folding unit
- Immobilizer unit
- Flasher unit
- Relay box
- Keyless antenna
- Door lock relay
- Chime buzzer
- Junction box

### Integrated Module (BCM)

- Electronic control
  - ETACS module
  - Chime bell
  - Mirror folding unit
  - Immobilizer unit
  - Flasher unit
  - Keyless antenna
  - Door lock relay
  - Chime buzzer
- Power distribution
  - Junction box
  - Relay box

<!-- Figure: BCM block diagram showing individual control module to integrated module transition, source: BE.pdf page 33 -->

## Body Control Module (BCM)

<!-- Figure: BCM front view showing connector locations and fuse/relay positions, source: BE.pdf page 34 -->
<!-- Figure: BCM back view showing connector locations, source: BE.pdf page 34 -->

## BCM Terminal Connection

### Connector A

| Terminal No. | Description |
|---|---|
| 1 | NC |
| 2 | NC |
| 3 | FPD (IG1) |
| 4 | ESPS (IG1) |
| 5 | SEAT BELT BUCKLE (RH) |
| 6 | SEAT BELT BUCKLE (LH) |
| 7 | CRASH SIG |
| 8 | NC |
| 9 | AIRBAG DIAG (FROM ESPS) |
| 10 | AIRBAG WARNING IND |
| 11 | HAZARD COM RLY (IG2) |
| 12 | DRL UNIT NO2 (INT LAMP SOURCE) |
| 13 | FRONT WIPER RLY CONTROL |
| 14 | FR FOG RLY-S2 |
| 15 | TURN SIGNAL (FR) |
| 16 | TAIL AUTO CUT TO DRL |
| 17 | DRL UNIT |
| 18 | FR WIPER RLY(IG2) |

### Connector B

| Terminal No. | Description |
|---|---|
| 1 | NC |
| 2 | NC |
| 3 | NC |

### Connector C

| Terminal No. | Description |
|---|---|
| 1 | TURN SIGNAL (FL) |
| 10 | POSITION LAMP (RH) |
| 11 | POSITION LAMP (LH) |
| 12 | ABS MODULE(IG1) |
| 13 | ALT-L |
| 14 | FUSE & RLY BOX (IG2) |
| 15 | WIPER PARK OUTPUT |
| 16 | WASHER MOTOR |
| 17 | NC |
| 18 | NC |

### Connector D

| Terminal No. | Description |
|---|---|
| 1 | B+30A |
| 2 | TAILGATE LOCK SW |
| 3 | ASSIST DOOR LOCK SW |
| 4 | ASSIST DOOR SW |
| 5 | FOLDING SW |

### Connector E

| Terminal No. | Description |
|---|---|
| 1 | TAILGATE SW |
| 2 | NC |
| 3 | DRIVER DOOR LOCK SW |
| 4 | NC |
| 5 | DRIVER DOOR SW |
| 6 | NC |
| 7 | NC |
| 8 | NC |
| 9 | NC |
| 10 | SEAT BELT SW |
| 11 | NC |
| 12 | NC |

### Connector F (continued from E)

| Terminal No. | Description |
|---|---|
| 1 | REAR FOG LAMP FEED |
| 2 | BACKUP LAMP |
| 3 | POWER OUTLET |
| 4 | OUTSIDE MIRROR |
| 5 | TAIL LAMP (RH) |
| 6 | DOOR LOCK FEED |
| 7 | NC |
| 8 | DOOR UNLOCK FEED |
| 9 | NC |
| 10 | TAIL LAMP (LH) |
| 11 | 4 DOOR SW |
| 12 | MIRROR UNFOLD |
| 13 | TURN SIGNAL (RL) |
| 14 | NC |
| 15 | LUGGAGE LAMP |
| 16 | NC |
| 17 | TURN SIGNAL (RR) |
| 18 | AMP |
| 19 | OUTSIDE MIRROR HEATER |
| 20 | MIRROR FOLD |
| 21 | REAR WIPER MOTOR (IG2) |
| 22 | TAILGATE OPEN SW |
| 23 | NC |

### Connector G

| Terminal No. | Description |
|---|---|
| 1 | POWER WINDOW SW |

### Connector H

| Terminal No. | Description |
|---|---|
| 1 | IMMOBILIZER ANTENNA 1 |
| 2 | NC |
| 3 | TURN SIGNAL SW (RH) |
| 4 | DOOR WARNING SW |
| 5 | TAIL SW |
| 6 | REAR FOG SW |
| 7 | CODE SAVER |
| 8 | NC |
| 9 | HOOD SW |
| 10 | NC |
| 11 | IMMOBILIZER ANTENNA 2 |
| 12 | EXPORT GND INPUT |
| 13 | TURN SIGNAL SW (LH) |
| 14 | AUTO LIGHT SW INPUT |
| 15 | NC |
| 16 | HEAD LAMP SW |
| 17 | FRONT FOG SW |
| 18 | HAZARD SW |
| 19 | REAR DEFOG SW |
| 20 | REAR FOG LAMP IND |

### Connector I

| Terminal No. | Description |
|---|---|
| 1 | AIR CONDITIONER SW |
| 2 | CLUSTER BATTERY CHARGE |
| 3 | CRUISE STOP SW |
| 4 | TCS SW (IG1) |
| 5 | CLUSTER (IG1) |
| 6 | CLUSTER (IG1) |
| 7 | CLUSTER (T/SIG LH OUT) |
| 8 | ECU (IG1) |
| 9 | CLUSTER (T/SIG RH OUT) |
| 10 | RR HTD SW (PDR INDICATOR) |
| 11 | CLUSTER (AIRBAG IND+IG1) |
| 12 | Hi-SCAN (B+) |
| 13 | DIGITAL CLOCK (ACC) |
| 14 | NC |
| 15 | EXTERNAL TAIL LAMP (RH) |
| 16 | Hi-SCAN (AIRBAG DIAGNOSIS) |
| 17 | AIR CONDITIONER (IG2) |
| 18 | AUTO LIGHT GND |
| 19 | DIAGNOSIS & CODE SAVING |
| 20 | IMMOBILIZER IND |

### Connector J

| Terminal No. | Description |
|---|---|
| 1 | SIREN CONTROL |
| 2 | NC |
| 3 | KEY INDE ILL |
| 4 | SPEED SENSOR |
| 5 | INTERIOR ILL |
| 6 | CLUSTER (AIRBAG WARNING IND) |
| 7 | DCT |
| 8 | DOOR AJAR |
| 9 | MULTI-FUNCTION INT |
| 10 | MULTI-FUNCTION INT (T) |
| 11 | AUTO LIGHT SIGNAL |
| 12 | SEAT BELT INDICATOR |
| 13 | OVER SPEED GND (CLUSTER) |
| 14 | NC |
| 15 | AUTO LIGHT SUPPLY |
| 16 | TAILGATE OPEN IND |

### Connector K

| Terminal No. | Description |
|---|---|
| 1 | CIGAR LIGHTER |
| 2 | WIPER LOW |
| 3 | WIPER HI |
| 4 | BACKUP SW |
| 5 | AUDIO (ACC) |
| 6 | MULTI-FUNCTION WASHER SW |
| 7 | BACKUP LAMP SW |
| 8 | START INHIBIT RELAY |
| 9 | SEAT HEATER SW(IG2) |
| 10 | JOINT MAIN 3 (B+) |
| 11 | STOP SW (B+) |
| 12 | MULTI GAUGE (IG1) |
| 13 | MULTI GAUGE (B+) |
| 14 | WIPER PARK/G |

### Connector L

| Terminal No. | Description |
|---|---|
| 1 | GND 1 |
| 2 | NC |
| 3 | BLOWER MOTOR |
| 4 | IG SW (IG1) |
| 5 | GND 2 |
| 6 | WIPER SW POWER |
| 7 | IG SW (ACC) |
| 8 | IG SW (IG2) |

### Connector M

| Terminal No. | Description |
|---|---|
| 1 | SUN ROOF (IG2) |
| 2 | ROOM LAMP (B+) |
| 3 | ROOF LAMP DECAY CONTROL |
| 4 | ECM |
| 5 | DOOR WARNING FOR S/ROOF |
| 6 | S/ROOF & ROOM LAMP GND |
| 7 | ECM MIRROR |
| 8 | SUN ROOF MOTOR (B+) |

## Fuse

| Fuse No. | Capacity | Connection Circuit |
|---|---|---|
| 1 | 20A | Ignition coil (2.7L), Electronic chrome mirror |
| 2 | 20A | A&P |
| 3 | 10A | Back-up lamp switch, Transaxle range switch |
| 4 | 10A | Instrument cluster (AIRBAG IND) |
| 5 | 15A | Air bag control module, Seat belt buckle switch |
| 6 | 10A | Mirror defogger |
| 7 | 10A | Hazard relay |
| 8 | 15A | Rear wiper motor, Rear wiper relay |
| 9 | 10A | Right tail lamps |
| 10 | 20A | Front wiper motor, Front wiper relay |
| 11 | 10A | Blower relay, Blower motor |
| 12 | 30A | Defogger relay |
| 13 | 15A | Stop lamp switch, Folding/unfolding relay |
| 14 | 10A | Left tail lamps |
| 15 | 10A | A/C control module, Blower relay |
| 16 | 10A | TCM, Multi gauge unit, TCM, Vehicle speed sensor |
| 17 | 10A | Instrument cluster (Power), Pre-excitation resistor |
| 18 | 10A | Room lamp, Clock, Audio, Data link connector, Multi gauge unit |
| 19 | 20A | Power window relay |
| 20 | 15A | Trunk lid switch |
| 21 | 10A | A/C relay, ABS sensor, Head lamp relay |
| 22 | 10A | Rear fog lamp |
| 23 | 15A | Trunk lid switch |
| 24 | 15A | Sunroof, Power door lock/Unlock relay |
| 25 | 20A | Seat warmer |
| 26 | 10A | ABS control module, TCS switch |
| 27 | 10A | Audio, Digital clock |

## BCM Circuit Diagram

<!-- Figure: BCM circuit diagram (full schematic), source: BE.pdf page 39 -->

## ETACS Function Inspection

### 1. Vehicle Speed Sensing Intermittent Wiper

Vehicle speed is determined by number of speed sensor pulse input in one second. The current speed and the previous speed for the vehicle is to be compared. The higher of the two values is to be used in the intermittent time calculation. The previous value is updated every second.

When Ignition 2 is on and the wiper switch is in the intermittent position, the wiper is driven at the speed dependent intermittent time. A single wipe is achieved by driving the wiper relay until the park switch is also taken over unless the dwell time between wipes is too short, in this case it would be on all the time. This avoids unnecessary clicking of the wiper relay.

IG2 must be on for this function to operate. When the washer switch is on for more than 0.5 sec, the wiper output is activated immediately. The length of time the washer switch is held is then evaluated to determine the number of swipes required. If the washer switch is on for more than 0.2 but less than 0.6 sec, then wiper performs a single swipe. As an example, if the washer switch is held for more than 0.6 sec, wiper performs 1 current swipe and then performs another two swipes.

If washer switch is on less than 0.2 seconds make no wiper action.

During intermittent wiping, a wiper linkage wipe has higher priority.

During start condition (IG1 on and IG2 off) washer input to be ignored. This is to prevent quality problem of single wipe occurring during starting of car.

<!-- Figure: Intermittent wiper timing diagram, source: BE.pdf page 40 -->

#### Time Specification

| Parameter | Value |
|---|---|
| T1 | 0.5 sec. |
| T2 | 0.6 - 0.8 sec. (Time of wiper motor 1 rotation) |
| T3 | At vehicle speed = 0km/h |
| | 2.6+/-2 sec. (VR=0%)-10.8 sec. (VR=50%+) |
| | At vehicle speed = 100km/h or more |
| | Delay 2sec (VR=0%)-10.0,1sec (VR=50%) |

Wipe stall time can be set in EEPROM and its units are 100ms.

During INT operation, if the time between initiating and concluding a wipe is greater than Wipe stall time then the wiper motor is also considered to have stalled. In this case, the current wipe is terminated and INT operation is cancelled until either of the following events occurs:

- The wiper stalk has moved from the OFF position.
- The ignition has been switched off.

### 2. Rear Wiper Operation

<!-- Figure: Rear wiper operation diagram, source: BE.pdf page 40 -->

### 3. Snow Build Up Wiper Bounce Prevention (Snow Mode)

Without this feature, as snow builds up at the base of the windscreen, it becomes more difficult for the wiper arms to completely reach the park position. Once the wipers have been turned off and the wipers have returned to the park position, the compacted snow is able to drive the wiper arms back up and reactivate the park switch. This, in turn, drives the wiper arms towards park again and the cycle repeats itself. This feature is required to prevent wiper bounce from happening when snow has accumulated on the windscreen.

#### Detection of Wiper Bounce

If the BCM detects that the wipers have parked more than a maximum amount times within a time period then wiper bounce is detected. The maximum amount of timer can be set in EEPROM using the variable wipe snow park. The time can also be set in EEPROM using the variable wipe snow time. The units of wipe snow time is milliseconds.

#### Bounce Prevention

If wiper bounce has been detected then the wiper bounce prevention relay is driven to open circuit. The wiper bounce relay is in series with the park switch and thus can prevent automatic parking. This relay is normally closed.

#### Termination of Bounce Prevention

Termination is achieved by ceasing to drive the wiper bounce relay to open circuit. Bounce prevention can be terminated in the following ways:

- Ignition off. The power source for the wiper motor is derived from IG2, thus there will be no drive to park with ignition off. As such bounce prevention is not required.
- The wiper stalk has moved from the OFF position.

### 4. Wiper Motor Stall Protection

This feature offers some protection to the wiper motor if ice has frozen the wiper blades to the windscreen or the wipers have jammed for some other reason. During low and high wiper selection, no protection is offered since the stalk drives the wiper motor directly.

If the wiper motor has not parked within wipe stall time, then wiper motor is considered to have stalled. In this case, the wiper bounce relay is driven to open circuit until either of the following events occurs:

- The ignition has been switched to the off position.
- The wipers have returned the park position by a manual operation (Low or high speed selected).
- The wiper stalk has moved from the OFF position.

### 5. Knob Activated Central Locking

If either the drivers door lock or the assistant door lock is moved from the locked position to the unlocked position then all other door locks will follow, but the tailgate will not change state. Conversely, if the drivers door lock or the assistant door lock is moved from the unlocked position to the locked position then all other door locks will follow. Locking and unlocking is achieved by driving the door lock motors in the respective direction for 0.5 seconds.

Installation of the battery should not change the state of the locks.

<!-- Figure: Knob activated central locking diagram showing driver door lock, assist door lock, and all doors lock/unlock outputs, source: BE.pdf page 41 -->

#### Time Specification

T1: 0.5+/-0.1 sec.

### 6. Ignition Key Reminder (Locking of Key in Vehicle Prevention)

If the key is in the ignition and the driver's door or assist door is open and the vehicle is locked using driver's knob or assist knob, then the central locking system will issue an unlock pulse of duration 1 second to the all doors thus preventing locking of the vehicle.

If it is not inhibited, then the central locking shall issue a minimum of 3 pulses of 0.5 second duration to unlock the doors. After the third pulse, if door lock knob becomes unlocked, stop the next pulse. If vehicle speed is greater than 5 km/h, ignition key reminder function is disabled.

If door warning switch is off and ignition input is on then ignition key reminder function is disabled.

<!-- Figure: Ignition key reminder timing diagram, source: BE.pdf page 42 -->

#### Time Specification

| Parameter | Value |
|---|---|
| T1 | 1 sec. |
| T2 | 0.5 sec. |
| T3 | Max. 5 sec. |

### 7. Key Operated Warning (key in Ignition Reminder Chime)

If the key is in ignition key cylinder and the drivers door is opened, the chime bell sounds. This tone is the same as the seatbelt warning chime and over speed warning chime. The chime sound is generated with a 600 Hz drive, amplitude modulated with an exponentially decaying envelope of time constant 1.0+/-0.25 sec. After ignition is turned on or the key is removed, the chime stops immediately.

<!-- Figure: Key operated warning timing diagram, source: BE.pdf page 42 -->

### 8. Auto Light Function

Light must be turned on 500+/-100 msec. after the input light to the light sensor has been lowered. Lights must be turned off 3+/-1 sec. after the input light to the light sensor has been raised. The headlamps must be turned on 300msec before the tail lamps are switched off. When the headlight switch is in the auto position and light intensity fulfilling the table below is detected, the tail lamp and the head lamp will be turned on. These figures are based upon the use of unfitted auto glass.

If the auto light switch is not fitted on the vehicle, or the switch is rotated from the ON to the AUTO position each time that the light sensor may be out of calibration, as per the following table.

If the option select input is grounded, both the headlamps and the tail lamps shall illuminate when the voltage drops below the tail lamp threshold. When the voltage rises above the tail lamp threshold, both the headlamps and the tail lamps shall extinguish.

| | Tail Lamp | Head Lamp |
|---|---|---|
| ON | 1.17+/-0.8V | 0.61+/-0.09V |
| OFF | 3.47+/-0.10V | 1.00+/-0.06V |

### 9. Rear Delay Control (Rear Defogger Control)

When the engine is running (Alternator L high) & the rear defog switch is pushed, the BCM will switch the rear defog relay output on for 20 min. max duration.

If the rear defog switch is pressed again during this time, or the engine stalls, the rear defog relay is switched off immediately.

<!-- Figure: Rear defogger control timing diagram, source: BE.pdf page 42 -->

#### Time Specification

T1: 20+/-1 msec.

### 10. Tail Lamp Auto Cut

When key is in the ignition key cylinder and tail lamp is switched on and the driver's door is opened, after 3 seconds and then opening of the driver's doors will turn off and set tail lamps. If either door is opened first, followed by removing key from ignition, then tail lamp is switched off.

If tail lamps have been cut automatically, and the tail lamp switch is turned off and on, then tail lamp is switched on and auto cut function is cancelled. If tail lamps have been cut automatically, and the ignition key is inserted, then tail lamps are turned on.

<!-- Figure: Tail lamp auto cut timing diagram, source: BE.pdf page 43 -->

### 11. Power Window Timer

When Ignition 2 is on, the power window relay output is turned on immediately.

When Ignition 2 is turned off the power window feed is maintained on for 30 seconds and then turned off. If the driver or assist door is opened during 30 sec interval the output shall be turned off immediately. If doors are open and Ignition 2 is then turned on, the output shall be turned on immediately. If doors are open and Ignition 2 is then turned off, the output shall be turned off immediately.

<!-- Figure: Power window timer timing diagram, source: BE.pdf page 43 -->

#### Time Specification

T1: 30+/-3 sec.

### 12. Ignition Key Hole Illumination

When the drivers door is open, the ignition key illumination is turned on.

When the drivers door is closed, illumination is on for 10 sec., then off.

When the assist door is open, the ignition key illumination is turned on.

When assist door is closed, illumination is on for 10 sec., then off.

The key illumination is extinguished immediately when ignition is turned on.

Locking of the vehicle from the transmitter (arm state) shall extinguish ignition key illumination.

<!-- Figure: Ignition key hole illumination timing diagram, source: BE.pdf page 43 -->

#### Time Specification

| Parameter | Value |
|---|---|
| T1 | 10+/-1 sec. |
| T2 | 0 - 10 sec. |
