---
source: EE.pdf
chapter: EE
section: EE-31 to EE-42
pages: 31-42
engine: All (I4 + V6)
title: Starting System
vehicle: 2003 Hyundai Tiburon (GK)
---

# Battery

## Battery Visual Inspection (1)

### 1. Checking Flow

1. Check for obvious damage such as a cracked or broken case or cover that could permit loss of electrolyte. Determine the cause of damage and correct as needed. Clean any corrosion with a solution of baking soda and water.

   - **O.K.** --> Inspect the height of electrolyte
   - **Not O.K.** --> Replace battery

2. Inspect the height of electrolyte.

   - **O.K.** --> Battery test
   - **Height difference is above 10mm between cells** --> Replace battery

3. Battery test.

   - **O.K. (11.0-12.9)** --> See below
   - **Shortage of electrolyte** --> Replace battery

4. Battery test results:

   - **Below 11.0V** --> Replace battery
   - **Above 12.5V** --> Starting system inspection

5. Load test (using battery tester):

   - **Below 11.0V** --> Replace battery
   - **O.K.** --> Battery is good

<!-- Figure: Battery visual inspection checking flow chart, source: EE.pdf page 31 -->

---

### 2. Checking Sheet

| Item | Trouble | Cause | Remedy | Decision of and battery |
|---|---|---|---|---|
| 1. Visual inspection | Battery terminal damage | Dealing carelessness; Bad tightening condition between battery cable and terminal | Replace | User: O |
| | Cover breakage | Dealing carelessness | Replace | User: O |
| | Electrolyte leakage | | | |
| | - Cover breakage | Cover breakage | Replace | User: O |
| | - Cover sealing part leakage | Bad cover sealing | Replace | Manufacturer: O |
| 2. Electrolyte height inspection | Electrolyte height between cells is over 10mm | Cell short; Malfunction caused by outer temperature | Replace | Manufacturer: O |
| | Shortage of electrolyte | Electrolyte loss caused by over-charge | Replace | Manufacturer: O |
| 3. Voltage inspection | 1. Battery voltage < 11.0V | 1. Over charge | Replace; Check the electric circuit | User: O |
| | 2. 12.5V < Battery voltage < 12.9 | 2. Normal | | |
| | 3. 12.0V < Battery voltage < 12.4V (Simple discharge) | 1. Insufficient charge | Battery Load Test (Refer to Load Test sheet) | |
| | 4. 11.0V < Battery voltage < 12.0V (Over discharge) | 2. Internal failure | Replace | User: O |
| | 5. Battery voltage > 11.0V | 1. Charge condition; 2. Let the battery alone on discharge condition for long period; 3. Short circuit | Replace | User: O |

---

### 3. Load Test

1. When discharging the battery during 15 seconds at half currency of C.C.P, the voltage of battery should be over the voltage as shown below.

#### Regulating Voltage Table

| Ambient Temperature | Voltage |
|---|---|
| above 20 deg C | 9.6V |
| 10 deg C | 9.5V |
| -10 deg C | 9.4V |
| 0 deg C | 9.3V |
| -4 deg C | 9.2V |
| -1 deg C | 9.1V |
| -7 deg C | 8.9V |
| -12 deg C | 8.8V |
| -18 deg C | 8.5V |

2. When the voltage is not within specification, test 2nd load test again, and if not, do the re-charge.

3. If the battery voltage (at above within 2 hours after re-charging) is over 12.5V and the voltage after load test is over the standard value, this battery can be used.

---

## Battery Visual Inspection (2)

1. Make sure ignition switch and all accessories are in the OFF position.
2. Disconnect the battery cables (negative first).
3. Remove the battery from the vehicle.

> **CAUTION:**
> Care should be taken in the event the battery case is cracked or leaking, to protect your skin from the electrolyte. Rubber gloves (not household type) should be worn when removing the battery.

4. Inspect the battery carrier for damage caused by the loss of acid from the battery. If acid damage is present, it will be necessary to clean the area with a solution of clean warm water and baking soda. Scrub the area with a stiff brush and wipe off with a cloth moistened with baking soda and water.
5. Clean the top of the battery with the same solution as described in Step(4).
6. Inspect the battery case and cover, for cracks. If cracks are present, the battery must be replaced.
7. Clean the battery posts with a suitable battery post cleaner.
8. Clean the inside surface of the terminal clamps with a suitable battery terminal cleaning tool. Replace damaged or frayed cables and broken terminal clamps.
9. Install the battery in the vehicle.
10. Connect the cable terminals to the battery post, making sure the top of the terminal are flush with the top of the post.
11. Tighten the terminal nut securely.
12. Coat all connections with light mineral grease after tightening.

> **CAUTION:**
> When batteries are being charged, an explosive gas forms beneath the cover of each cell. Do not smoke near batteries being charged or which have recently been charged. Do not break live circuits at the terminals of the batteries being charged. A spark will occur where the circuit is broken. Keep all open flames away from the battery.

<!-- Figure: Battery terminal post cleaning detail, source: EE.pdf page 33 -->
<!-- Figure: Battery case inspection, source: EE.pdf page 33 -->

---

# Starting System

## General Information

The starting system includes the battery, starter motor, speed control switch, ignition switch, inhibitor switch (A/T only), connection wires and the battery cables.

When the ignition key is turned to the start position, current flows and energizes the starter motor's solenoid coil. The solenoid plunger and clutch shift lever are activated, and the clutch pinion engages the ring gear. The contacts close and the starter motor cranks.

In order to prevent damage caused by excessive rotation of the starter armature when the engine starts, the clutch pinion gear overruns.

<!-- Figure: Starter motor assembly [I4], source: EE.pdf page 34 -->
<!-- Figure: Starter motor assembly [V6], source: EE.pdf page 34 -->

---

## Check Clutch Pedal (MT)

Check that pedal height, pedal freeplay and clutch pedal clevis pin play are correct. (Refer to clutch group.)

<!-- Figure: Clutch pedal and inhibitor switch location, source: EE.pdf page 34 -->

---

## Check Starter Relay

Remove the starter relay and check continuity between the terminals. If the continuity is not as specified, replace the relay.

| Condition | Terminals 85-86 (Coil) | Terminals 87-30 (Switch) |
|---|---|---|
| De-energized | -- | No continuity |
| Energized | Coil powered | Continuity |

<!-- Figure: Starter relay terminal layout showing terminals 85, 86, 87, and 30, source: EE.pdf page 34 -->
<!-- Figure: Starter relay photo, source: EE.pdf page 34 -->

---

## Check Ignition Lock Switch

Remove the ignition lock switch and check continuity between the terminals. If the continuity is not as specified, replace the switch.

| Condition | Terminal 1 | Terminal 2 |
|---|---|---|
| Pushed | Continuity | Continuity |
| Free | No continuity | No continuity |

<!-- Figure: Ignition lock switch continuity test, source: EE.pdf page 35 -->
<!-- Figure: Ignition lock switch dimensions: 12.0 +/- 0.3 mm (length), 2.0 +/- 0.3 mm (width), terminals 1 and 2, source: EE.pdf page 35 -->

---

## Removal and Installation

**TORQUE: Nm (kg.cm, lb.ft)**

| Fastener | Torque |
|---|---|
| Starter motor mounting bolts | 27-34 (275-346, 20-25) |

<!-- Figure: Starter motor removal on transaxle showing two mounting bolt locations, source: EE.pdf page 36 -->

### Removal Procedure

1. Disconnect the battery ground cable.
2. Remove the speedometer cable and the shift cable.
3. Disconnect the starter motor connector and terminal.
4. Remove the starter motor assembly.

### Installation

5. Installation is the reverse of removal.

---

## Components

The starter motor assembly consists of the following components:

- Solenoid
- Snap ring
- Packing A
- Ball
- Planetary gear
- Sun gear
- Planetary gear holder screws
- Ring gear
- Overrun clutch
- Stop ring
- Front bracket
- Screw
- Rear bracket
- Brush holder
- Armature
- Yoke assembly

<!-- Figure: Starter motor exploded view showing all components, source: EE.pdf page 37 -->

---

## Checking for Operation

### Pinion Gap Adjustment

#### Solenoid Adjustment Procedures for Pinion Gap Adjustment

1. Disconnect the field coil wire from the M-terminal of the solenoid.
2. Connect a 12V battery to the S-terminal and the M-terminal.
3. The pinion should move out.

> **CAUTION:**
> This test must be performed quickly (in less than 10 seconds) to prevent the coil from overheating.

4. Check the pinion for stopper clearance (pinion gap) with a feeler gauge.

**Pinion gap: 0.5-2.0 mm (0.02-0.079 in.)**

<!-- Figure: Pinion gap adjustment setup showing battery, switch, field coil wire, and solenoid connections, source: EE.pdf page 38 -->
<!-- Figure: Pinion gap measurement with feeler gauge showing stopper and pinion gap location, source: EE.pdf page 38 -->

5. If the pinion gap is out of specification, adjust by adding or removing gaskets between the solenoid and the front bracket.

---

### Magnetic Switch Pull-In Test

1. Disconnect the field coil wire from the M-terminal of the magnetic switch.
2. Connect a 12V battery between the S-terminal and the M (-) terminal.

> **CAUTION:**
> This test must be performed quickly (in less than 10 seconds) to prevent the coil from burning.

3. If the pinion moves out, then the pull-in coil is good. If it doesn't move out, replace the magnetic switch.

<!-- Figure: Magnetic switch pull-in test setup showing 12V battery and starter motor connections, source: EE.pdf page 38 -->

---

### Magnetic Switch Hold-In Test

1. Disconnect the field coil wire from the M-terminal of the magnetic switch.
2. Connect a 12V battery between the S-terminal and the body.

> **CAUTION:**
> This test must be performed quickly (in less than 10 seconds) to prevent the coil from burning.

3. If the pinion moves out, everything is in order. If the pinion moves back and forth repeatedly, the hold-in circuit is open. If it is open, replace the magnetic switch.

<!-- Figure: Magnetic switch hold-in test setup showing 12V battery and starter motor connections, source: EE.pdf page 38 -->

---

### Magnetic Switch Return Test

> **NOTE:**
> This test must be performed quickly (in less than 10 seconds) to prevent the coil from burning.

1. Disconnect the field coil wire from the M-terminal of the magnetic switch.
2. Connect a 12V battery between M-terminal and the body.
3. Pull the pinion out and release it. If the pinion returns quickly to its original position, everything is in order. If it doesn't, replace the magnetic switch.

<!-- Figure: Magnetic switch return test showing field coil wire and battery connections, source: EE.pdf page 39 -->

---

### Free Running Test

1. Place the starter motor in a vise equipped with soft jaws and connect a fully-charged 12-volt battery to the starter motor as follows:
2. Connect a test ammeter (100-ampere scale) and a carbon pile rheostat as shown in the illustration.

<!-- Figure: Free running test setup showing carbon pile rheostat, ammeter, battery, starter motor, and voltmeter connections, source: EE.pdf page 39 -->

3. Connect a voltmeter (15-volt scale) across the starter motor.
4. Rotate the carbon pile to the off position.
5. Connect the battery cable from battery's negative post to the starter motor body.
6. Adjust the carbon pile until battery voltage reads 11 volts.
7. Confirm that the maximum amperage is within the specifications and that the starter motor turns smoothly and freely.

**Current: Max. 90 Amps**

**Speed: Min. 3,000 rpm**

---

## Inspection

### Checking the Commutator

1. Place the armature on a pair of V-blocks, and check the run-out by using a dial gauge.

**Standard value:**
Armature run-out: 0.05 mm (0.002 in.)

**Limit:**
Armature run-out: 0.1 mm (0.0039 in.)

<!-- Figure: Armature run-out check on V-blocks with dial gauge, source: EE.pdf page 39 -->

2. Check the outer diameter of the commutator.

**Standard value:**
Outer diameter of the commutator: 29.4 mm (1.157 in.)

**Limit:**
Outer diameter of the commutator: 28.4 mm (1.118 in.)

<!-- Figure: Commutator outer diameter measurement, source: EE.pdf page 39 -->

3. Check the depth of the undercut between segments.

**Standard value:**
Depth of the undercut between segments: 0.5mm (0.020 in.)

**Limit:**
Depth of the undercut between segments: 0.2mm (0.079 in.)

<!-- Figure: Commutator undercut depth measurement showing segment and undercut, source: EE.pdf page 40 -->

---

### Brush Holder

Check for continuity between the brush holder and the brush holder.

The normal condition is no continuity.

<!-- Figure: Brush holder continuity check with ohmmeter, source: EE.pdf page 40 -->

---

### Overrunning Clutch

1. While holding the clutch housing, rotate the pinion. The drive pinion should rotate smoothly in one direction, but should not rotate in the opposite direction. If the clutch does not function properly, replace the overrun clutch assembly.

2. Inspect the pinion for wear or burns. If the pinion is worn or burned, replace the overrun clutch assembly. If the pinion is damaged, also inspect the ring gear for wear or burns.

<!-- Figure: Overrunning clutch rotation check, source: EE.pdf page 40 -->

---

### Front and Rear Bracket Bushing

Inspect the bushing for wear or burns. If the bushing is worn or burned, replace the front bracket assembly or the rear bracket assembly.

---

## Reassembly of the Stop Ring and Snap Ring

Using a suitable pulling tool, pull the overrunning clutch stop ring over the snap ring.

<!-- Figure: Stop ring and snap ring reassembly using pulling tool, source: EE.pdf page 40 -->

---

## Cleaning the Starter Motor Parts

1. Do not immerse parts in cleaning solvent. Immersing the yoke and field coil assembly and/or armature will damage the insulation. Wipe these parts with a cloth only.

2. Do not immerse the drive unit in cleaning solvent. The overrun clutch is pre-lubricated at the factory and solvent will wash lubrication from the clutch.

3. The drive unit may be cleaned with a brush moistened with cleaning solvent and wiped dry with a cloth.

<!-- Figure: New brush diagram showing pigtail, solenoid, and note to make sure that solder does not stick on brush surface, source: EE.pdf page 41 -->

---

## Replacement of Brushes and Springs

1. Brushes that are worn out, or oil-soaked, should be replaced.

2. When replacing field coil brushes, crush worn out brushes with pliers, taking care not to damage the pigtail.

<!-- Figure: Brush wear limit line diagram, source: EE.pdf page 41 -->

3. Sand the pigtail end with sandpaper to ensure good soldering.

4. Insert the pigtail into the hole provided in the new brush and solder it. Make sure that the pigtail and excess solder do not come out onto the brush surface.

5. When replacing the ground brush, slide the brush from the brush holder by prying the retaining spring back.

---

## Disassembly

### Removal of the Snap Ring and Stop Ring

1. Press the stop ring using a socket.

<!-- Figure: Stop ring pressed down with socket tool on armature shaft, source: EE.pdf page 42 -->

2. After removing the snap ring (using snap-ring pliers), remove the stop ring and the overrunning clutch.

<!-- Figure: Snap ring removal with snap-ring pliers showing overrunning clutch on shaft, source: EE.pdf page 42 -->
