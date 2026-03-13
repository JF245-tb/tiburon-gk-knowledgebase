---
source: RT.pdf
chapter: RT
title: Airbag System (Part 1)
pages: RT-5 through RT-24
---

# Airbag System (Part 1)

## General (continued)

### A. DAB + PAB

**TO AVOID SERIOUS INJURY:**

- For maximum safety protection in all types of crashes, you must always wear your seat belts.
- Do not install rear-facing child restraint in the front passenger seat.
- Do not sit or lean unnecessarily close to the airbag.
- Do not place any objects over the airbag or between the airbag and yourself.
- See the owner's manual for further information and explanation.

### C. WARNING

Contents are poisonous and extremely flammable. Do not probe with electrical devices or otherwise tamper with them in any way. Servicing of this unit to be performed only by authorized personnel.

### E. CAUTION: SRS clock spring

This is not a repairable part. Do not disassemble or tamper. If defective, replace entire unit as per service manual instructions.

> **CAUTION:** Before removal of steering wheel, center the front wheels and remove the ignition key.

Failure to do so may damage the SRS clock spring and render SRS system inoperative, possibly resulting in serious injury to the driver.

> **CAUTION:** When replacing clock spring, turn rotor in opposite direction approximately 3 turns and align >>> mark.

Failure to follow instructions may render SRS System inoperative possibly resulting in serious driver injury.

### D. CAUTION: SRS

Before removal of steering gearbox, read service manual, center the front wheels and remove the ignition key.

Failure to do so may damage the SRS clock spring and render SRS system inoperative, possibly resulting in serious injury to the driver.

### B. Supplemental Restraint System (Airbag) Information

The airbag is a Supplemental Restraint System (SRS). You must always wear the seat belts. The airbag system condition is normal when the "SRS" lamp in the cluster flashes approximately once after the ignition key is turned on and then goes off.

If any of the following conditions occur, the system must be serviced:

- "SRS" lamp does not light up when the key is turned on.
- "SRS" lamp stays lit or flashes continuously.
- The airbag has deployed.

The airbag system must be inspected by an authorized dealer ten years after the vehicle manufacture date shown on the certification label, located on left front door opening area.

> **WARNING:** Failure to follow the above instructions may result in injury to you or other occupants in the vehicle. See the "SRS" section in Owner's Manual for more information about airbags.

### F. Side Airbag

- This car is equipped with a side airbag for each front seat.
- Do not use any accessory seat covers.
- Use of other seat covers could reduce the effectiveness of the side airbag.
- Do not install any accessories on the side or near the side airbag.
- Do not use excessive force on the side of the seat.
- For further information, see the owner's manual.

### G. CAUTION: Airbag ESPS Unit

Detach connector before unfastening. Assemble strictly according to manual instructions.

---

## Electrical System

The SRS airbag system has specialized electrical and electronic components. Therefore the airbag operating components should be handled very carefully.

### SRSCM (Supplemental Restraint System Control Module)

The SRSCM will deploy the airbag module(s) by sensing the frontal impact sensed by the sensor built in to the SRSCM.

1. **DC/DC converter:** The DC/DC converter in the power supply includes a step-up and a step-down converter, which provides the firing voltage for four firing circuits (DAB, PAB, SAB, and BPT). It also assures that if the existing voltage falls below a defined threshold, a reset is executed.

2. **Arming/sensing/firing sensor:** The arming/firing sensor built in to the arming/firing circuit has the function of arming the airbag circuit under all intended collision conditions and prevents any inadvertent deployment of the firing circuits (armed under normal driving conditions). The safing sensor is a dual-contact electromechanical cell switch that closes if it experiences a deceleration exceeding a specified threshold.

3. **Back-up power:** The SRSCM reserves an energy reserve to provide deployment energy for a short period when the vehicle voltage is low or if lost in a vehicle frontal crash.

4. **Malfunction detection:** The SRSCM continuously monitors SRS components when the ignition switch is turned on and detects possible malfunctions in the system. The malfunction can be displayed in the form of a diagnostic trouble codes using the Hi-Scan Pro.

5. **MIL (Malfunction Indication Lamp) notification:** If any fault is detected, the SRSCM sends a signal to the MIL (Malfunction Indication Lamp or Airbag warning driver) on the instrument cluster to alert the vehicle driver.

   The MIL indicator is the key item in notifying the driver of SRS faults. It verifies lamp and SRSCM operation by flashing 6 times when the ignition switch is first turned on.

6. **Malfunction recording:** Once a fault occurs in the system, the SRSCM records the fault in memory in the form of a DTC, which can only be erased by the Hi-Scan Pro.

7. **Data link connector:** SRSCM memory stored is linked through this connector located underneath the driver side crash pad to an external output device such as the Hi-Scan Pro.

8. After firing the airbag once, the SRSCM cannot be used again and must be replaced.

9. **Crash output:** The crash output is used to unlock the doors in case of a crash. The crash output is 0.020 A in OFF mode and 200mA in ON mode. During the unlock command, the switch is closed for 200 ms.

---

## SRSCM (Supplemental Restraints System Control Module)

### Inflator Module (DAB, PAB, SAB)

DAB (Driver airbag), PAB (Passenger airbag) module, DSAB (Driver side airbag), PSAB (Passenger side airbag).

<!-- Figure: Airbag system component overview showing DAB, PAB, clock spring, satellite sensor, SAB (option), BPT, and SRSCM locations in vehicle, source: RT.pdf page RT-7 -->

The inflator module consists of an inflator and cushion. The inflator is gas generator (pyrotec device) to push the airbag. When the vehicle is in a frontal or side crash of sufficient force to close the sensor of the SRSCM, current flows through the deployment loop. This current ignites the material and inflates the airbag.

**Handling Precautions:**

1. When removing the airbag module or handling a new airbag module, it should be placed with the pad top surface facing up. In this case, the twin-lock type connector lock lever should be in the locked state and care should be taken to place it so the connector will not be damaged. Do not store a steering wheel pad on top of another one. (Storing the pad with its metal surface up may lead to a serious accident if the airbag should inflate accidentally.)

2. Never measure the resistance of the airbag squib. (This may cause the airbag to deploy, which is very dangerous.)

3. Store the airbag module where the ambient temperature remains below 93°C (200°F), without high humidity and away from electrical noise.

4. During electric welding, disconnect the airbag under the steering column near the MULTI-FUNCTION SWITCH connector before starting work.

### SRS Harness

The SRS harness is wrapped in a yellow tube to be distinguished from other system harnesses. A shorting bar is included inside the wiring connectors of DAB, PAB, SAB and BPT inflator side. The shorting bar absorbs the current flow in the DAB, PAB, SAB and BPT module circuits when the connectors are disconnected. The circuits to the inflator module are shorted in this way to help prevent unwanted deployment of the airbag when servicing the airbag module.

### SRSCM Independent Lamp Activation

The SRS malfunction indication lamp (MIL) is located in the cluster giving information of SRS operating conditions by control signals from the SRSCM.

<!-- Figure: Instrument cluster showing SRS warning lamp location, source: RT.pdf page RT-8 -->

There are certain fault conditions in which the SRSCM (SRS Custom Module) cannot function and thus cannot control the operation of the lamp. In these cases, the lamp is directly activated by appropriate circuitry that operates independently of the SRSCM, as follows:

1. Loss of ignition voltage supply to the SRSCM: lamp turned on continuously.

2. Loss of internal operating voltage: lamp turned on continuously.

3. SRSCM not connected: lamp turned on through shorting bar in wiring harness connector.

### MIL Operating Method

| Condition | Display |
|---|---|
| Normal | Blink 6 times |
| Total failure frequency 1-4 | Turn on continuously |
| Active fault | Turn it on after 6 seconds |
| Total failure frequency > 4 | Turn it on continuously |
| Active fault | Turn it on continuously |

### Clock Spring

The clock spring (coil spring) consists of two current carrying coils. It is attached between the steering column and the steering wheel. It allows rotation of the steering wheel while maintaining continuous contact of the deployment loop through the inflator module.

<!-- Figure: Clock spring assembly showing internal coil mechanism, source: RT.pdf page RT-8 -->

The steering wheel must be fitted correctly to the steering column with the clock spring at the neutral position, otherwise cable disconnection and other troubles may result.

<!-- Figure: Exploded view of clock spring showing cover, rotor, gear, ring gear, upper case, lower case, and mark, source: RT.pdf page RT-9 -->

When the rotor is rotated clockwise.

### Satellite Sensor

The release system for the side airbag consists of a SRSCM installed in the center of the vehicle and two satellites -- one on the left-hand side and one on the right. Only the SRSCM is capable of deploying the airbags or the seat-belt pretensioners systems in the vehicle. In the dialog between the SRSCM and the satellite, it is the SRSCM that makes the deployment decision.

The SRSCM is supported with the side airbag function by two satellites, which act as intelligent acceleration sensors mounted in the side areas of the passenger compartment. These satellites continuously report the system status on the left and right-hand sides of the vehicle to the SRSCM.

It monitors the acceleration sensor continuously. The test results are reported to the SRSCM by means of periodic status signals.

> **NOTE:** When the ignition is ON, never cause a sudden shock around the installation area of the satellite sensor by a hammer, etc. Otherwise it could cause the airbag system to unexpectedly deploy during servicing.

---

## System Component and Layout

<!-- Figure: System component layout showing locations of clock spring, PAB, DAB, BPT, and side airbag (when deployed) in the vehicle interior, source: RT.pdf page RT-10 -->

---

## SRSCM (SRS Control Module)

<!-- Figure: SRSCM location illustration showing module on floor center console, source: RT.pdf page RT-11 -->

---

## Airbag System (SRS) Wiring Diagram

<!-- Figure: Complete SRS wiring schematic showing FUSE 5, FUSE 3, instrument cluster connections, SRSCM connector, data link connector, shorting bar circuits, clock spring, DAB, PAB, SAB, BPT, satellite sensors, and passenger seat belt buckle switch connections, source: RT.pdf page RT-12 -->

---

## SRSCM Connector Pinout

### DAB, PAB, SAB, BPT

<!-- Figure: SRSCM 50-pin connector diagram showing pin layout (pins 1-50), source: RT.pdf page RT-13 -->

| Pin No. | Function | Input/Output |
|---|---|---|
| 1 | Not used | - |
| 2 | Not used | - |
| 3 | Not used | - |
| 4 | Not used | - |
| 5 | Passenger satellite sensor, High | Input |
| 6 | Driver satellite sensor, High | Input |
| 7 | Passenger side airbag, High | Input |
| 8 | Passenger side airbag, Low | Output |
| 9 | Driver side airbag, Low | Output |
| 10 | Driver side airbag, High | Output |
| 11 | Not used | - |
| 12 | Passenger airbag, Low | Output |
| 13 | Passenger airbag, High | Output |
| 14 | Passenger seat belt buckle switch, High | Input |
| 15 | Driver airbag, Low | Output |
| 16 | Driver airbag, High | Output |
| 17 | K-diagnostic line | Input/Output |
| 18 | Driver seat belt buckle switch, High | Input |
| 19 | Warning lamp | Output |
| 20 | GND | Input |
| 21 | Battery supply | Input |
| 22 | Passenger belt pretensioner, Low | Output |
| 23 | Passenger belt pretensioner, High | Output |
| 24 | Driver belt pretensioner, High | Output |
| 25 | Driver belt pretensioner, Low | Output |
| 26 | Not used | - |
| 27 | Not used | - |
| 28 | Not used | - |
| 29 | Not used | - |
| 30 | Passenger satellite sensor, Low | Input |
| 31 | Driver satellite sensor, Low | Input |
| 32-33 | Shorting bar | - |
| 34-35 | Shorting bar | - |
| 36 | Not used | - |
| 37-38 | Shorting bar | - |
| 39 | Passenger seat belt buckle switch, Low | Input |
| 40-41 | Shorting bar | - |
| 42 | Crash output | Output |
| 43 | Driver seat belt buckle switch, Low | Input |
| 44-45 | Shorting bar | - |
| 46 | Seat buckle switch | Output |
| 47-48 | Shorting bar | - |
| 49-50 | Shorting bar | - |

---

## Air Bag Module (Drive Side) and Clock Spring

### Components

<!-- Figure: Exploded view of driver-side airbag assembly showing clock spring, steering column, steering wheel, DAB module, and steering wheel lock nut, source: RT.pdf page RT-15 -->

**Torque Specifications:**

| Fastener | Torque |
|---|---|
| Steering wheel lock nut | 40-50 Nm (400-500 kg-cm, 29-36 lb-ft) |
| Steering wheel bolt | 4-6 Nm (40-60 kg-cm, 2.9-4.4 lb-ft) |

**TORQUE: Nm (kg-cm, lb-ft)**

### Removal

1. Disconnect the negative battery cable and keep secure from battery.

   > **CAUTION:** Wait at least 30 seconds after disconnecting the battery cable before doing any further work.

2. Remove the side protect cover of steering wheel and airbag module mounting bolts using a hexagonal wrench.

   <!-- Figure: Removing side protect cover and airbag mounting bolts, source: RT.pdf page RT-16 -->

3. When disconnecting the connector of the clock spring from the airbag module, pull the airbag's lock toward the outer side to spread it open.

   > **CAUTION:** When disconnecting the airbag module-clock spring connector, take care not to apply excessive force to it.

   <!-- Figure: Disconnecting clock spring connector from airbag module, source: RT.pdf page RT-16 -->

4. Remove the drive side airbag module.

   > **CAUTION:** The removed airbag module should be stored in a clean, dry place with the pad cover face up.

   <!-- Figure: Removed driver airbag module stored pad-side up, source: RT.pdf page RT-16 -->

5. Remove the steering wheel using SST (09561-11002).

   > **CAUTION:** Do not hammer on the steering wheel. Doing so may damage the collapsible column mechanism.

   <!-- Figure: Removing steering wheel with SST 09561-11002, source: RT.pdf page RT-16 -->

### Inspection

#### Airbag Module

> **CAUTION:** Never attempt to measure the circuit resistance of the airbag module (squib) even if you are using the specified tester. If the circuit resistance is measured with a tester, accidental airbag deployment will result in serious personal injury.

Dispose the old one according to the specified procedure. If any improper parts are found during the following inspection, replace the airbag module with a new one.

1. Check pad cover for dents, cracks or deformities.

2. Check the airbag module for denting, cracking or deformation.

3. Check hooks and connectors for damage, terminals for deformities, and harness for binds.

4. Check airbag inflator case for dents, cracks or deformities.

   <!-- Figure: Airbag module inspection points, source: RT.pdf page RT-17 -->

5. Install the airbag module to the steering wheel to check for fit or alignment with the wheel.

   <!-- Figure: Airbag module installed on steering wheel for fit check, source: RT.pdf page RT-17 -->

#### Clock Spring

1. If, as a result of the following checks, even one abnormal point is discovered, replace the clock spring with a new one.

2. Check connectors and protective tube for damage, and terminals for deformities.

   <!-- Figure: Clock spring inspection, source: RT.pdf page RT-17 -->

---

## Air Bag Module (Passenger Side)

### Removal

> **NOTE:**
> 1. Never attempt to disassemble or repair the airbag module.
> 2. Do not drop the airbag module or allow contact with water, grease or oil. Replace it if a dent, crack, deformation or rust are detected.
> 3. The airbag module should be stored on a flat surface and placed so that the pad surface is facing upward. Do not place anything on top of it.
> 4. Do not expose the airbag module to temperatures over 93°C (200°F).
> 5. An undeployed airbag module should only be disposed in accordance with the procedure.
> 6. Never attempt to measure the circuit resistance of the airbag module (squib) even if you are using the specified tester. If the circuit resistance is measured with a tester, accidental airbag deployment will result in serious personal injury.
> 7. Whenever the PAB is deployed it should be replaced together with the crash pad, as it tears the expansion wire. The squib is shut down if the PAB is deployed making the connector wire useless.

1. Disconnect the battery negative (-) terminal cable.

   > **CAUTION:** Wait at least 30 seconds.

   <!-- Figure: Disconnecting battery negative terminal, source: RT.pdf page RT-18 -->

2. Remove the glove box.

3. Disconnect the PAB module connector.

4. Remove the crash pad assembly and then undo the PAB module. (Refer to the BD section)

5. The skin of the passenger airbag module is integrated with the crash pad, therefore, the crash pad must be replaced if the PAB deploys.

---

## Pretensioner Seat Belt

### Components

<!-- Figure: Exploded view of pretensioner seat belt assembly with 52 numbered components, source: RT.pdf page RT-19 -->

| No. | Part | No. | Part |
|---|---|---|---|
| 1 | Cover (L/H) | 27 | Distance sheet |
| 2 | Bearing plate (L/H) | 28 | Pinion gear |
| 3 | Retractor base | 29 | Label |
| 4 | Sensor spring | 30 | Tub cover (T/R) (L/H) |
| 5 | Web sensor spring | 31 | Lock G element (L,S) (L/H) |
| 6 | Sensor spring holder | 32 | Spring holder (L/H) |
| 7 | Inertia mass | 33 | Tube |
| 8 | Ball (L/H) | 34 | Bush shaft |
| 9 | Pawl | 35 | Bracket (L/H) |
| 10 | Gear/generator | 36 | Holding (L/H) |
| 11 | Tube spring | 37 | Lock disc spring |
| 12 | Piston | 38 | Normal spring |
| 12 | Tube (L/H) | 39 | Stay shaft |
| 13 | Ball stopping spring | 40 | Solenoid assy |
| 14 | Ball trap (L/H) | 41 | Return spring |
| 15 | Screw | 42 | Bearing G lever (L/H) |
| 16 | Rivet | 43 | Lock G element (L,S) (L/H) |
| 17 | Rewinding spring | 44 | -- |
| 18 | G spring holder (L/H) | 45 | -- |
| 19 | Washer | 46 | -- |
| 20 | Felt | 47 | -- |
| 21 | Retaining washer (L/H) | 48 | -- |
| 22 | Lock disc spring | 49 | Torsion bar (R/H) |
| 23 | Locking element (L/H) | 50 | Torsion bar (L/H) |
| 24 | Spindle (L/H) | 51 | Tread head (knot stop) (L/H) |
| 25 | Rack | 52 | -- |
| 26 | Pinion gear | -- | -- |

### Function of Pretensioner

When a vehicle crashes with a certain degree of frontal impact, the gas generator will ignite on an electrical firing signal from the SRSCM (Supplemental Restraint System Control Module).

Gas from the gas generator causes movement of the piston in the manifold case (cylinder), which operates the rack gear.

The rack gear, rotates a piston gear and a pinion rotates the planet gear(s).

Finally, the webbing is retracted by the retractor that has been wound by the planet gear and pinion gear to reduce the severity of injury to the front seat occupant by restraining the seat belt webbing. This prevents the occupant from thrusting forward and hitting the steering wheel or the instrument panel when the vehicle crashes.

<!-- Figure: Pretensioner function showing gas generator, spring, bolts, ball stopper, tube, and three states (initial state, operating state, exploited state), source: RT.pdf page RT-20 -->

### Load Limiter

The load limiter is designed to relieve the impact force to an occupant's chest of the seat belt webbing when the occupant is restrained by the seat belt during a crash. If the crash force reaches a certain value, the torsion bar in the pretensioned seat belt will deform and cause the webbing to be extracted from the seat belt, thus, relieving the impact force.

<!-- Figure: Load limiter operation showing spindle, torsion bar, webbing retracted state (Load < 5.5 kN) and torsion bar deformed state (Load > 5.5 kN), source: RT.pdf page RT-21 -->

**Load limiter threshold: 5.5 kN**

### Removal (Belt Pretensioner)

1. Disconnect the battery negative (-) terminal.

   > **CAUTION:** Wait at least 30 seconds.

   <!-- Figure: Battery disconnect, source: RT.pdf page RT-22 -->

   > **CAUTION:**
   > 1. Never attempt to disassemble or repair the BPT.
   > 2. Do not drop the BPT or allow contact with water, grease, oil.
   > 3. Replace it if a dent, crack, deformation or rust is detected.
   > 4. Do not place anything on the BPT.
   > 5. Do not expose the BPT to temperature over 87°C (200°F).
   > 6. BPT functions one time only. Be sure to replace the BPT after it is deployed.
   > 7. Be sure to wear gloves and safety goggles when handling the deployed BPT.

2. Remove the door scuff trim.

   <!-- Figure: Door scuff trim removal, source: RT.pdf page RT-22 -->

3. Remove the quarter trim after removing seat belt lower anchor bolt.

   <!-- Figure: Quarter trim removal, source: RT.pdf page RT-22 -->

4. Remove the upper anchor plate cover and upper anchor plate.

5. Remove the lower anchor plate and front seat belt.

---

## Troubleshooting

### Diagnosis with Scan Tool

#### Check Procedures

1. Connect the Hi-Scan Pro DLC to the vehicle's data link connector located underneath the dash panel.

2. Turn the ignition key to the "ON" position and turn the Hi-Scan Pro ON.

3. Perform the SRS diagnosis according to the vehicle model configuration.

4. If a fault code is assured, then replace the component. Never attempt to repair the component.

5. If the Hi-Scan Pro finds that a component of the system is faulty, there is a possibility that the fault is not in the component, but in SRS wiring or connector.

<!-- Figure: Hi-Scan Pro connected to DLC under dash panel, source: RT.pdf page RT-23 -->

### Diagnostic Troubleshooting Flow

<!-- Figure: Diagnostic troubleshooting flowchart, source: RT.pdf page RT-24 -->

**Flow:**

1. Gather information from the customer.
2. Verify complaint: Reoccurs or Does not reoccur.
3. Check diagnostic trouble code.
   - **No trouble code or can't communicate with Hi-Scan Pro** --> Inspection chart for trouble symptoms.
   - **Diagnostic trouble code displayed** --> Record diagnostic trouble code(s) then erase them --> Check trouble code symptom --> Check diagnostic trouble code.
     - **No trouble code** --> Intermittent malfunction.
     - **Diagnostic trouble code displayed** --> Inspection chart for diagnostic trouble codes.
   - **Does not reoccur, check diagnostic trouble code:**
     - **Diagnostic trouble code displayed** --> Record diagnostic trouble code(s) then erase them (continue flow above).
     - **No trouble code** --> Intermittent malfunction.
