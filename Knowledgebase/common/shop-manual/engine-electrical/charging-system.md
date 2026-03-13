---
source: EE.pdf
chapter: EE
section: EE-17 to EE-30
pages: 17-30
engine: V6
title: Charging System
vehicle: 2003 Hyundai Tiburon (GK)
---

# Charging System

## General Information
<!-- EBAB0100 -->

The charging system includes a battery, generator with a built-in regulator, the charging indicator light and connecting wiring. The generator has three phase windings (three positive and three negative), each rectifying AC current to DC current. Therefore, DC current appears at generator "B" terminal.

In addition, the charging voltage of the generator is regulated by the battery voltage detection system. The main parts of the generator include the rotor, stator, rectifier, capacitor, brushes, and V-ribbed belt pulley. The brush holder contains a built-in electronic voltage regulator.

<!-- Figure: Generator cutaway showing rotor, rear bearing, stator, front bearing, and pulley, source: EE.pdf page 17 -->

<!-- Figure: Charging system schematic [H] showing fusible link, battery, and generator connections, source: EE.pdf page 17 -->

<!-- Figure: Charging system schematic [V6] showing fusible link, battery, and generator connections, source: EE.pdf page 17 -->

---

## Inspection

### Voltage Drop Test of Generator Output Wire
<!-- EBAB0130 -->

This test determines whether or not the wiring between the generator "B" terminal and the battery (+) terminal is good by the voltage drop method.

#### Preparation

1. Turn the ignition switch to "OFF".

> **NOTE:** To find abnormal conditions of the connection, actions should not be taken on the two terminals and each connection during the test.

2. Connect a digital voltmeter between the generator "B" terminal and battery (+) lead wire to the battery (+) terminal. Connect the (+) lead wire of the voltmeter to the "B" terminal and the (-) lead wire to the battery (+) terminal.

<!-- Figure: Voltmeter connection diagram for voltage drop test, source: EE.pdf page 17 -->

#### Conditions for the Test

1. Start the engine.
2. Switch on the headlamps, blower motor and so on. And then, read the voltmeter under this condition.

#### Result

1. The voltmeter may indicate the standard value.

**Standard value:** 0.2V max.

2. If the value of the voltmeter is higher than expected (above 0.2V max.), poor wiring is suspected. In this case check the wiring from the generator "B" terminal to the fusible link to the battery (+) terminal. Check for loose connections, color change due to an overheated harness, etc. Correct them before testing again.

<!-- Figure: Wiring check diagram [H], source: EE.pdf page 18 -->

3. Upon completion of the test, set the engine speed at idle, turn off the head lamps, blower motor and the ignition switch.

---

### Output Current Test [I4]

This test determines whether or not the generator gives an output current that is equivalent to the nominal output.

#### Preparation

1. Prior to the test, check the following items and correct as necessary:

    1) Check the battery installed in the vehicle to ensure that it is in good condition. The battery checking method is described in "BATTERY".

> **NOTE:** The battery that is used to test the output current should be one that has been partially discharged. With a fully charged battery, the test may not be conducted correctly due to an insufficient load.

    2) Check the tension of the generator drive belt. The belt tension check method is described in the section "GM or EM".

2. Turn off the ignition switch.
3. Disconnect the battery ground cable.
4. Disconnect the generator output wire from the generator "B" terminal.
5. Connect a DC ammeter (0 to 100A) in series between the "B" terminal and the disconnected output wire. Be sure to connect the (+) lead wire of the ammeter to the disconnected output wire.

> **CAUTION:** Tighten each connection securely, as a heavy current will flow. Do not rely on clips.

6. Connect a voltmeter (0 to 20V) between the "B" terminal and ground. Connect the (+) lead wire to the generator "B" terminal and (-) lead wire to a good ground.
7. Attach an engine tachometer and connect the battery ground cable.
8. Leave the engine hood open.

<!-- Figure: Output current test connections showing ammeter in series and voltmeter across B terminal to ground [V6], source: EE.pdf page 18 -->

#### Test

1. Check to see that the voltmeter reads as the same value as the battery voltage. If the voltmeter reads 0V and the open circuit in the wire between the generator "B" terminal and battery (+) terminal, a blown fusible link or poor grounding is suspected.
2. Start the engine and turn on the headlights.
3. Set the headlights to high beam and the heater blower switch to HIGH, quickly increase the engine speed to 2,500 rpm and read the maximum output current value indicated by the ammeter.

> **NOTE:**
> - When the engine starts up, the charging current quickly drops. Therefore, the above operation must be done quickly to read the maximum current value correctly.

#### Result

- The ammeter reading may be higher than the limit value. If it is lower than the limit value and the generator output wire is in good condition, remove the generator from the vehicle and test it.

**Limit value (65A generator):** 63A min.

> **NOTE:**
> - The normal output current value is shown on the nameplate affixed to the generator body.
> - The output current value changes with the electrical load and the temperature of the generator itself. Therefore, the normal output current may not be obtained. If such is the case, keep the headlights on to cause discharge of the battery, or use the lights of another vehicle to increase the electrical load.
> - The normal output current may not be obtained if the temperature of the generator itself or ambient temperature is too high. In such a case, allow the generator to cool before testing.

4. Upon completion of the output current test, lower the engine speed to idle and turn off the ignition switch.
5. Disconnect the battery ground cable.
6. Remove the ammeter and voltmeter and the engine tachometer.
7. Connect the generator output wire to the generator "B" terminal.
8. Connect the battery ground cable.

---

### Regulated Voltage Test [I4]
<!-- EBAB0140 -->

The purpose of this test is to check that the electronic voltage regulator controls voltage correctly.

#### Preparation

1. Prior to the test, check the following items and correct if necessary:

   1. Check that the battery installed on the vehicle is fully charged. For battery checking method, see "BATTERY".
   2. Check the generator drive belt tension. For belt tension check, see "GM or EM" section.
   3. Turn ignition switch to "OFF".

2. Disconnect the battery ground cable.
3. Connect a digital voltmeter between the "S(L)" terminal of the generator and ground. Connect the (+) lead of the voltmeter to the "S(L)" terminal of the generator. Connect the (-) lead to good ground or the battery (-) terminal.
4. Disconnect the generator output wire from the generator "B" terminal.
5. Connect a DC ammeter (0 to 100A) in series between the "B" terminal and the disconnected output wire. Connect the (+) lead wire of the ammeter to the "B" terminal. Connect the (-) lead of the ammeter to the disconnected output wire.

<!-- Figure: Regulated voltage test connections showing ammeter, voltmeter, check engine connection, and ECM, source: EE.pdf page 19 -->

#### Test

1. Turn the ignition switch on and check to see that the voltmeter indicates the following value:

**Voltage:** Battery voltage

If it reads 0V, there is an open circuit in the wire between the generator "S(L)" terminal and the battery and the battery (+), or the fusible link is blown.

2. Start the engine. Keep all lights and accessories off.
3. Run the engine at a speed of about 2,500 rpm and read the voltmeter when the generator output current drops to 10A or less.

#### Result

1. If the voltmeter reading agrees with the value listed in the Regulating Voltage Table below, the voltage regulator is functioning correctly. If the reading is other than the standard value, the voltage regulator or the generator is faulty.

#### Regulating Voltage Table

| Voltage regulator ambient temperature (deg C) | Regulating voltage (V) |
|---|---|
| -20 (-4) | 14.2-15.4 |
| 20 (68) | 13.9-14.9 |
| 60 (140) | 13.4-14.6 |
| 80 (176) | 13.1-14.5 |

2. Upon completion of the test, reduce the engine speed to idle, and turn off the ignition switch.
3. Disconnect the battery ground cable.
4. Remove the voltmeter and ammeter and the engine tachometer.
5. Connect the generator output wire to the generator "B" terminal.
6. Connect the battery ground cable.

---

### Generator Output Line Voltage Drop Test [V6]
<!-- EBAB0150 -->

This test determines the condition of the wiring from the generator "B" terminal to the battery (+) terminal (including the fusible link).

1. Be sure to check the following before testing:
   - Generator installation and wiring connections
   - Generator drive belt tension
   - Fusible link

2. Allow access to the generator while the engine is running.
3. Turn the ignition switch to the OFF position.
4. Disconnect the negative battery cable.
5. Disconnect the generator output wire from the generator "B" terminal. Connect a DC test ammeter with a range of 0-100A in series between the "B" terminal and the disconnected output wire. Connect the (+) lead of the ammeter to the "B" terminal. Connect the (-) lead of the ammeter to the disconnected output wire.

> **NOTE:**
> An inductive type ammeter which enables measurements to be taken without disconnecting the generator output wire is recommended. Using this equipment will lessen the possibility of a voltage drop caused by a loose "B" terminal connection.

6. Connect a digital-type voltmeter between the generator "B" terminal and the battery (+) terminal. Connect the (+) lead of the voltmeter to the "B" terminal. Connect the (-) lead of the voltmeter to the battery (+) cable.
7. Reconnect the negative battery cable.
8. Connect a tachometer or the scan tool.
9. Start the engine.
10. With the engine running at approx. 2,500 rpm, turn the headlights and other lights on and off to adjust the generator load on the ammeter slightly above 30A.

**Limit: max. 0.3V**

> **NOTE:**
> When the generator output is high and the value displayed on the ammeter does not decrease to 30A, set the voltmeter to a higher range and read the value on the voltmeter. In this case the limit becomes max. 0.4V.

11. If the value displayed on the voltmeter is still above the limit, a fault in the generator output wire may exist. Check the wiring between the generator "B" terminal and the battery (+) terminal (including fusible link). If any connector or harness terminal has become discolored due to overheating, repair, then test again.

<!-- Figure: Generator output line voltage drop test setup showing generator, voltmeter, ammeter, and battery connections, source: EE.pdf page 21 -->

12. After the test, run the engine at idle.
13. Turn off all lights and turn the ignition switch to the OFF position.
14. Disconnect the tachometer or the scan tool.
15. Disconnect the negative battery cable.
16. Disconnect the ammeter and voltmeter.
17. Connect the generator output wire to the generator "B" terminal.
18. Connect the negative battery cable.

---

### Output Current Test [V6]
<!-- EBAB0160 -->

This test determines if the generator output current is normal.

#### Preparation

1. Before testing, be sure to check the following:
   - Generator installation and wiring connections
   - Battery
   - Generator drive belt tension
   - Fusible link
   - Abnormal noise from the generator while the engine is running

> **NOTE:**
> The battery used should be slightly discharged. The load needed by a fully-charged battery is insufficient for an accurate test.

2. Turn the ignition switch to the OFF position.
3. Disconnect the negative battery cable.
4. Disconnect the generator output wire from the generator "B" terminal. Connect a DC test ammeter with a range of 0-100A in series between the "B" terminal and the disconnected output wire. Connect the (+) lead of the ammeter to the "B" terminal. Connect the (-) lead of the ammeter to the disconnected output wire.

> **CAUTION:**
> Never use clips. Use bolts and nuts to connect the line. Otherwise, loose connections (e.g. using clips) may lead to a serious accident because of high current.

> **NOTE:**
> An inductive type ammeter which enables measurements to be taken without disconnecting the generator output wire is recommended.

5. Connect a voltmeter with a range of 0-20V between the generator "B" terminal and the ground. Connect the (+) lead of the voltmeter to the "B" terminal, and then connect the (-) lead of the voltmeter to the ground.
6. Connect the negative battery cable.
7. Connect a tachometer or the scan tool.
8. Leave the hood open.
9. Check that the reading on the voltmeter is equal to battery voltage.

> **NOTE:**
> If the voltage is 0 V, the cause is probably an open circuit in the wire or fusible link between the generator "B" terminal and the battery (+) terminal.

10. Start the engine, and turn the headlights on.
11. Switch the headlights to high beam, turn the heater blower switch to high, increase the engine speed to approx. 2,500 rpm, and read the maximum current output displayed on the ammeter.

**Limit: 70% of nominal output current**

> **NOTE:**
> - For the nominal current output, refer to the Generator Specifications page EE-2.
> - Because the current from the battery will drop soon after the engine is started, steps 10 and 11 should be carried out as quickly as possible in order to obtain the maximum current output value.
> - The current output value will depend on the electrical load and the temperature of the generator body.
> - If insufficient electrical load is used while testing, the specified level of current may not be output, even though the generator is normal. In such a case, increase the electrical load by leaving the headlights on with the engine off to discharge the battery before testing.
> - The nominal level of current may not be output if the temperature of the generator body and/or ambient temperature is too high. In such a case, allow the generator to cool before testing.

12. The reading on the ammeter should be above the limit value. If the reading is below the limit value and the generator output wire is OK, remove the generator from the engine and check the generator.
13. Run the engine at idle speed after the test.
14. Turn the ignition switch to the OFF position.
15. Disconnect the tachometer or the scan tool.
16. Disconnect the negative battery cable.
17. Disconnect the ammeter and voltmeter.
18. Connect the generator output wire to the generator "B" terminal.
19. Connect the negative battery cable.

---

### Regulated Voltage Test [V6]
<!-- EBAB0170 -->

This test determines if the voltage regulator is correctly controlling the generator output voltage.

#### Preparation

1. Be sure to check the following:
   - Generator installation and wiring connections
   - Battery fully charged
   - Generator drive belt tension
   - Fusible link
   - Abnormal noise from the generator while the engine is running

2. Turn the ignition switch to the OFF position.
3. Disconnect the negative battery cable.
4. Connect a digital-type voltmeter between the generator "B" terminal and the ground. Connect the (+) lead of the voltmeter to the "B" terminal. Connect the (-) lead of the voltmeter to a secure ground or to the battery (-) terminal.
5. Disconnect the generator output wire from the generator "B" terminal.
6. Connect a DC test ammeter with a range of 0-100A in series between the "B" terminal and the disconnected output wire.

<!-- Figure: Regulated voltage test circuit diagram showing load, ammeter, voltmeter, charging warning light, generator relay, generator, engine control module, and battery connections, source: EE.pdf page 23 -->

Connect the (+) lead of the ammeter to the "B" terminal. Connect the (-) lead of the ammeter to the disconnected output wire.

7. Reconnect the negative battery cable.
8. Connect a tachometer or the scan tool. Check that the reading on the voltmeter is equal to the battery voltage.

> **NOTE:**
> If the voltage is 0 V, the cause is probably an open circuit in the wire or fusible link between the generator "B" terminal and the battery (+) terminal.

9. Make sure all lights and accessories are off.
10. Start the engine.
11. Increase the engine speed to approx. 2,500 rpm.
12. Read the voltmeter when the current output of the generator becomes 10A or less.
13. If the voltage reading conforms to the value in the voltage regulation table, the voltage regulator is operating normally. If the voltage is not within the standard value, a malfunction of the voltage regulator or of the generator exists.

---

## Battery
<!-- EBA90170 -->

### Description

1. The maintenance-free battery is, as the name implies, totally maintenance free and has no removable battery cell caps. The battery is completely sealed, except for small vent holes in the cover.

2. Water is never added to the maintenance-free battery.

<!-- Figure: Maintenance-free battery, source: EE.pdf page 24 -->

---

## Generator

### Removal and Installation
<!-- EBOC0190 -->

#### [I4]

**Torque specifications:**

| Fastener | Torque |
|---|---|
| Brace assembly | 1.2-1.5 kg.m |
| Adjusting bolt | 2.0-2.5 kg.m |
| Lower mounting bolt | 2.0-2.5 kg.m |

<!-- Figure: I4 generator removal showing brace assembly, adjusting bolt, and generator mounting, source: EE.pdf page 25 -->

#### [2.7 V6]

**Torque specifications:**

| Fastener | Torque: Nm (kg.cm, lb.ft) |
|---|---|
| Adjusting bolt | 12-15 (120-150, 9-11.3) |
| Support bolt | 20-25 (200-250, 15-18.6) |

<!-- Figure: V6 generator removal showing adjusting bolt, support bolt, and generator position on engine, source: EE.pdf page 25 -->

---

### Disassembly and Reassembly
<!-- EBOC0190 -->

#### Component Overview

The generator assembly consists of the following components:

- Front housing
- Screw (4EA)
- Pulley
- Hex nut
- Front bearing
- Retainer
- Rotor assembly
- Rear bearing
- Rectifier
- Molded clip / B terminal
- Spacer
- Bolt (4EA)
- Flange
- Stator assembly
- Rear housing
- Regulator assembly
- Cover

<!-- Figure: Generator exploded view showing all components -- front housing, screw (4EA), pulley, hex nut, front bearing, retainer, rotor assembly, rear bearing, rectifier, molded clip/B terminal, spacer, bolt (4EA), flange, stator assembly, rear housing, regulator assembly, cover, source: EE.pdf page 26 -->

#### Disassembly

1. Remove the four through bolts.
2. Insert a flat screwdriver between the front bracket and stator core, and pry downward.

> **CAUTION:**
> Do not insert the screwdriver too deeply, as there is a danger of damaging the stator coil.

3. The rear cover may be hard to remove because a ring is used to lock the outer race of the rear bearing. To facilitate removal of rear cover, heat just the bearing box section with a 200W soldering iron.

> **CAUTION:**
> Do not use a heat gun as it may damage the diode assembly.

> **CAUTION:**
> Be careful that the vise jaws do not damage the rotor.

4. Secure the rotor in a vise with its pulley side up.
5. Remove the pulley nut, spring washer, pulley, and spacer.
6. Remove the front bracket and two seals.
7. Remove the rotor from the vise.
8. Remove the brush holder screws, rectifier screws, and nut from the "B" terminal.
9. Remove the stator assembly from the rear bracket.
10. Detach the slinger from the brush holder.
11. When the stator is to be removed, unsolder the three stator leads to the main diodes on the rectifier.

> **CAUTION:**
> 1. When soldering or unsoldering, make sure that heat from soldering iron is not transmitted to the diode for a long period.
> 2. Do not exert excessive force on the leads of the diodes.

12. When separating the rectifier from the brush holder, unsolder the two plates soldered to the rectifier.

<!-- Figure: Disassembly steps showing screwdriver insertion for separation, source: EE.pdf page 27 -->
<!-- Figure: Vise clamping of rotor assembly, source: EE.pdf page 27 -->
<!-- Figure: Brush holder and slinger removal, source: EE.pdf page 27 -->
<!-- Figure: Rectifier solder plate separation detail, source: EE.pdf page 27 -->

---

### Inspection

#### Rotor
<!-- EBOC0200 -->

**1. Continuity test**

Check the rotor coil for continuity. Make sure there is continuity between the slip rings.

If resistance is extremely low, there is a short. If there is no continuity or if there is a short circuit, replace the rotor assembly.

**Resistance value:** Approx. 3.1 ohm

<!-- Figure: Multimeter continuity test between rotor slip rings, source: EE.pdf page 28 -->

**2. Ground test**

Check the rotor coil for a ground. Check that there is no continuity between the slip ring and the core. If there is continuity, replace the rotor assembly.

<!-- Figure: Multimeter ground test between slip ring and rotor core, source: EE.pdf page 28 -->

**3. Grounding test (coil-to-core)**

Check the coil for grounding. Check that there is no continuity between the coil and the core. If there is continuity, replace the stator assembly.

<!-- Figure: Grounding test on rotor coil, source: EE.pdf page 28 -->

---

#### Stator

1. Make a continuity check on the stator coil. Check that there is continuity between the coil leads. If there is no continuity, replace the stator assembly.

---

#### Rectifiers

**Positive rectifier test**

Check for continuity between the positive rectifier and stator coil lead connection terminal with an ohmmeter. The ohmmeter should read continuity in only one direction. If there is continuity in both directions, a diode is shorted.

Replace the rectifier assembly.

<!-- Figure: Positive rectifier continuity test, source: EE.pdf page 28 -->

**Negative rectifier test**

Check for continuity between the negative rectifier and the stator coil lead connection terminal. The ohmmeter should read continuity in only one direction. If there is continuity in both directions, the diode is shorted, and the rectifier assembly must be replaced.

<!-- Figure: Negative rectifier continuity test, source: EE.pdf page 28-29 -->

---

#### Diode Trio Test

Check the three diodes for continuity by connecting an ohmmeter to both ends of each diode. Each diode should have continuity in only one direction.

If continuity is present in both directions, the diode is defective and the heatsink assembly must be replaced.

<!-- Figure: Diode trio test with ohmmeter, source: EE.pdf page 29 -->

---

### Brush Replacement

1. Measure the length of the brush protrusion shown in the illustration, and replace the brush if the measured value is below the limit value.

**Limit: 2 mm (0.08 in.) or less**

<!-- Figure: Brush protrusion measurement diagram showing 2mm limit dimension, source: EE.pdf page 29 -->

2. The brush can be removed if the solder of the brush lead wire is removed.
3. When installing a new brush, insert the brush into the holder, and then solder the lead wire.

<!-- Figure: Brush holder detail showing brush and lead wire solder point, source: EE.pdf page 29 -->

---

### Reassembly

Perform reassembly in the reverse procedure of disassembly. Pay attention to the following:

Before the rotor is attached to the rear bracket, insert a wire through the small hole in the rear bracket to lock the brush. After the rotor has been installed, the wire can be removed.

<!-- Figure: Rear bracket showing wire insertion point for brush lock during reassembly, source: EE.pdf page 30 -->
