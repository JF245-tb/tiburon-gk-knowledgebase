---
source: EE.pdf
chapter: EE
section: EE-10 to EE-16
pages: 10-16
engine: V6
title: Ignition System
---

# Ignition System

## General Information
<!-- EBOC0040 -->

Ignition timing is controlled by the electric control ignition timing system. The ignition timing data for the engine operating conditions are programmed in the memory of the engine control module (ECM).

The engine conditions (speed, load, warm-up condition, etc.) are detected by the various sensors. Based upon these sensor signals and the ignition timing data, signals to interrupt the primary current are sent to the power transistor. The ignition coil is activated and timing is controlled at the optimum point.

<!-- Figure: Ignition system overview showing ignition coil locations on 2.7L V6 and 2.0L I4 engines, source: EE.pdf page 10 -->

---

## Ignition System (DOHC — 2.0L I4)

### Ignition Coil
<!-- EBOC0010 -->

**1. Measurement of the primary coil resistance**
Measure the primary coil resistance between terminals 1 and 2.

**Standard value:** 0.5 ± 0.05 Ω

<!-- Figure: Primary coil terminal identification, source: EE.pdf page 11 -->

**2. Measurement of the secondary coil resistance**
Measure the resistance between the high-voltage terminals for the No.1 and No.4 cylinders, and between the high-voltage terminals for the No.2 and No.3 cylinders.

**Standard value:** 12.1 ± 1.8 kΩ

### Ignition Switch
<!-- EBOC0090 -->

#### Removal and Installation

1. Disconnect the negative battery terminal.
2. Remove the air bag module.

> **CAUTION:** The SRS system is designed to retain enough power to deploy air bag for about 30 seconds even after battery has been disconnected, so serious injury may result from unintended air bag deployment if service is done on the SRS system immediately after battery cable is disconnected.

3. Loosen the tapping screw and lift up horn pad and remove it.
4. Remove the lock nut and the washer.
5. Pulling the dynamic damper forward, lift it up and remove it.
6. Install the special tool (09561-11001) and remove the steering wheel.

> **CAUTION:** Do not hammer on the steering wheel to remove it.

7. Remove the steering column lower and upper shrouds.
8. Remove the lower cover.
9. Disconnect the connectors and remove the multifunction switch.
10. Remove the mounting bolts and separate ignition switch from steering column.

#### Inspection
<!-- EBOC0280 -->

1. Separate the connector located under the steering column.
2. Inspect the switch continuity between the terminals.
3. If continuity is not as specified, replace the switch.

**Ignition Switch Continuity Table:**

| Position | B1 | ACC | G1 | B2 | IG2 | ST |
|----------|----|----|----|----|-----|----|
| LOCK (Removed) | | | | | | |
| ACC (Inserted) | | | | L | | F |
| ON1 | | | | L | F | |
| START | O | O | O | | | |

- O = continuity between terminals
- RO = Round the locking bar
- RE = Return the locking bar
- L = Lock
- F = Free

**Door Warning Switch and Key Illumination:**

| Position | 4 | 3 | 2 | 1 | RO | RE |
|----------|---|---|---|---|----|----|
| LOCK (Removed) | | | | L | | F |
| ACC | | | F | F | | |
| ON1 | | | F | F | | |
| START | | | | | | |

#### Hints

If engine will not crank, determine whether the condition exists with the transaxle range switch in the "PARK" or in the "NEUTRAL" position.

If the "NO-CRANK" condition occurs in one shift lever position but not the other, a more probable cause is the transaxle range switch.

### Spark Plug Test
<!-- EBAA0060 -->

1. Remove the spark plug and reconnect it to the spark plug cable.
2. Ground the spark plug outer electrode and crank the engine.
3. Verify that there is an electrical discharge between the electrodes.

> **CAUTION:** When replacing the spark plug, use a resistor type.

<!-- Figure: Spark plug inspection — defective insulation vs good, source: EE.pdf page 13 -->

### Spark Plug Cables Test

1. Disconnect one at a time each of the spark plug cables while the engine is idling to check whether the engine's running performance changes or not.
2. Spray a fine mist of water on the secondary wires to observe any flashover.

> **CAUTION:** Wear rubber gloves while operating.

3. If the engine performance does not change, check the resistance of the spark plug, and check the spark plug itself.
4. Check the cap and outer shell for cracks.
5. Measure the resistance.

**For 2.7 Liter Engine — Spark Plug Cable Resistance (kΩ):**

| No. 1 | No. 2 | No. 3 | No. 4 | No. 5 | No. 6 |
|-------|-------|-------|-------|-------|-------|
| 4.39-5.59 | 2.28-3.43 | 3.49-5.24 | 1.9-2.86 | 3.25-4.87 | 1.3-1.95 |

> **NOTE:** Resistance should not be higher than 10,000 Ω per foot of cable. If resistance is higher, replace the cable.

---

## Ignition System (V6 — 2.7L)

### Installation of Spark Plug Cable (V6 2.7 Liter Engine)
<!-- EBAA0100 -->

Improper arrangement of spark plug cables will induce flashover between the cables, causing misfiring and surging at acceleration in high-speed operations. Therefore, be careful to arrange the spark plug cables properly as shown in the illustration.

<!-- Figure: V6 spark plug cable routing diagram showing cylinder numbering (1-6), front and rear bank cable paths, source: EE.pdf page 14 -->

### Ignition Coil (2.7L V6)
<!-- EBAA040 -->

**1. Measurement of the primary coil resistance**
Measure the resistance between connector terminals 1 and 2 (the coils at the No. 3 and No. 6 cylinder sides of the ignition coil, and between terminals 2 and 4 (the coils at the No. 1 and No. 4 cylinder sides), and between terminals 2 and 3 (the coils at the No.2 and No.5 cylinder sides).

**Standard value:** 0.74 ± 10% Ω

**2. Measurement of the secondary coil resistance**
Measure the resistance between the high-voltage terminal for the No. 3 and No. 6 cylinders, between the high-voltage terminals for the No. 1 and No. 4 cylinders and between the high-voltage terminals for the No.2 and No.5 cylinders.

**Standard value:** 13.3 ± 15% kΩ

> **CAUTION:** When measuring the resistance of the secondary coil, be sure to disconnect the connector of the ignition coil.

<!-- Figure: V6 ignition coil connector terminal identification (terminals 1-4), source: EE.pdf page 15 -->

### Inspection and Cleaning
<!-- EBAA0215 -->

1. Disconnect the spark plug cable from the spark plug.

> **NOTE:** Pull on the spark plug cable boot when removing the spark plug cable, not the cable, as it may be damaged.

2. Using the spark plug wrench, remove all of the spark plugs from the cylinder head.

> **NOTE:** Take care not to allow contaminants to enter through the spark plug holes.

3. Check the spark plugs for the following:
   1. Broken insulator
   2. Worn electrode
   3. Carbon deposits
   4. Damaged or broken gasket
   5. Condition of the porcelain insulator at the tip of the spark plug (carbon tracking)

4. Check the spark plug gap using a wire gap gauge, and adjust if necessary.

**Standard value:** Spark plug gap: 1.0-1.1 mm (0.039-0.043 in.)

<!-- Figure: Spark plug gap measurement diagram, source: EE.pdf page 16 -->

5. Re-insert the spark plug and tighten to the specified torque. If it is overtorqued, damage to the threaded portion of cylinder head may result.

**Tightening torque:** Spark plug: 20-30 Nm (200-300 kg.cm, 15-22 lb.ft)

> **NOTE:** When replacing the spark plug, use resistance plugs.
