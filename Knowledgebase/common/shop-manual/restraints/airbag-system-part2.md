---
source: RT.pdf
chapter: RT
title: "Airbag System (Part 2)"
pages: 21-40
section: "Troubleshooting"
---

# Airbag System (Part 2)

## Air Bag Module (Passenger Side) - continued

### Load Limiter

The load limiter is designed to relieve the impact force to an occupant chest of the seat belt webbing when the occupant is restrained by the seat belt during a crash. If the crash force reaches a certain value, the torsion bar in the pretensioned seat belt will deform and cause the webbing to extracted from the seat belt, thus, relieving the impact force.

<!-- Figure: Load limiter mechanism showing spindle, torsion bar, webbing retracted (Load < 5.5 kN) and torsion bar deformed (Load > 5.5 kN), source: RT.pdf page 21 -->

### Removal

1. Disconnect the battery negative (-) terminal.

> **CAUTION**
> Wait at least 30 seconds.

2. Remove the door scuff trim.

<!-- Figure: Door scuff trim removal, source: RT.pdf page 22 -->

3. Remove the quarter trim after removing seat belt lower anchor bolt.

<!-- Figure: Quarter trim removal, source: RT.pdf page 22 -->

4. Remove the upper anchor plate cover and upper anchor plate.

5. Remove the lower anchor plate and front seat belt.

> **CAUTION**
> 1. Never attempt to disassemble or repair the BPT.
> 2. Do not drop the BPT or allow contact with water, grease, oil.
> 3. Replace it if a dent, crack, deformation or rust is found.
> 4. Do not place anything on the BPT.
> 5. Do not expose the BPT to temperature over 87°C (189°F).
> 6. BPT functions one time only. Be sure to replace the BPT after it is deployed.
> 7. Be sure to wear gloves and safety goggles when handling the deployed BPT.

<!-- Figure: BPT caution illustration, source: RT.pdf page 22 -->

---

## Troubleshooting

### Diagnosis with Scan Tool

#### Check Procedures

1. Connect the Hi-Scan Pro DLC to the vehicle's data link connector located underneath the dash panel.

2. Turn the ignition key to the "ON" position and turn the Hi-Scan Pro ON.

3. Perform the SRS diagnosis according to the vehicle model configuration.

4. If a fault code is assured, then replace the component. Never attempt to repair the component.

5. If the Hi-Scan Pro finds that a component of the system is faulty, there is a possibility that the fault is not in the component, but in SRS wiring or connector.

<!-- Figure: Hi-Scan Pro connected to DLC under dash panel, source: RT.pdf page 23 -->

### Diagnostic Troubleshooting Flow

```
Gathering information from     Verify complaint
the customer            ──────────┐
                                  ├── Reoccurs ──────────────────┐
                                  └── Does not reoccur ──┐       │
                                                         │       │
                                  Check diagnostic       │       │
                                  trouble code           │       │
                                                         │       │
                          ┌───────────────────────────────┘       │
                          │                                       │
              No trouble code or    Diagnostic trouble    Check diagnostic
              can't communicate     code displayed        trouble code
              with Hi-Scan Pro             │                     │
                     │              Record diagnostic     Diagnostic trouble
                     │              trouble code(s)       code displayed ──┐
                     │              then erase them              │         │
                     │                     │              No trouble       │
                     │              Check trouble code    code             │
                     │              symptom                    │           │
                     │                     │                   │           │
                     │              Check diagnostic           │           │
                     │              trouble code               │           │
                     │                     │                   │           │
                     │              Diagnostic trouble         │           │
                     │              code displayed             │           │
                     │                     │                   │           │
                     ▼                     ▼                   ▼           │
              Inspection chart     Inspection chart for   Intermittent    │
              for trouble          diagnostic trouble     malfunction     │
              symptoms             codes                                  │
```

<!-- Figure: Diagnostic troubleshooting flowchart, source: RT.pdf page 24 -->

### Specification

| | Coil, Rs | Squib, Rs | Wiring harness, Rw | Connector terminal, Rt | Total resistance |
|---|---|---|---|---|---|
| **MIN** | | | | | |
| DAB | 0.24 | 1.7 | 0.05 | 0.0 | 1.99 |
| PAB | - | 1.8 | 0.05 | 0.0 | 1.85 |
| BPT | - | 1.8 | 0.06 | 0.0 | 1.86 |
| SAB | - | 1.8 | 0.05 | 0.0 | 1.85 |
| **MAX** | | | | | |
| DAB | 0.54 | 2.3 | 0.20 | 0.06 | 3.10 |
| PAB | - | 2.2 | 0.20 | 0.06 | 2.46 |
| BPT | - | 2.5 | 0.23 | 0.04 | 2.77 |
| SAB | - | 2.2 | 0.20 | 0.06 | 2.46 |

Unit: Ohm

<!-- Figure: Squib resistance circuit diagram showing Rs (squib resistance), Rt (terminal resistance), Rc (contact coil resistance), Rw (wiring harness resistance). R = Rs + Rt + Rw + Rc, source: RT.pdf page 25 -->

### Airbag Squib Resistance Limits

#### DAB

| Resistance Range | Description | Fault Detection |
|---|---|---|
| R <= 1.06 Ohm | Resistance too low | Fault definitely detected |
| 1.80 Ohm <= R <= 3.40 Ohm | Resistance within tolerance | Definitely no fault detected |
| R >= 6.70 Ohm | Resistance too high | Fault definitely detected |
| 1.06 Ohm < R < 1.80 Ohm / 3.40 Ohm < R < 6.70 Ohm | Tolerance band | Fault may or may not be detected |

#### PAB, SAB, BPT

| Resistance Range | Description | Fault Detection |
|---|---|---|
| R <= 0.4 Ohm | Resistance too low | Fault definitely detected |
| 1.6 Ohm <= R <= 2.8 Ohm | Resistance within tolerance | Definitely no fault detected |
| R >= 5.4 Ohm | Resistance too high | Fault definitely detected |
| 0.4 Ohm < R < 1.6 Ohm / 2.8 Ohm < R < 5.4 Ohm | Tolerance band | Fault may or may not be detected |

### Inspection Chart for Diagnostic Trouble Code

**OPTIONS: DAB + PAB + SAB + BPT**

| DTC No. | Fault description |
|---|---|
| B1111 | Battery voltage too high |
| B1112 | Battery voltage too low |
| B1346 | Driver airbag (DAB), Resistance too high |
| B1347 | Driver airbag (DAB), Resistance too low |
| B1348 | Driver airbag (DAB), Short to GND |
| B1349 | Driver airbag (DAB), Short to Battery |
| B1352 | Passenger airbag (PAB), Resistance too high |
| B1353 | Passenger airbag (PAB), Resistance too low |
| B1354 | Passenger airbag (PAB), Short to GND |
| B1355 | Passenger airbag (PAB), Short to Battery |
| B1361 | Driver seat belt pretensioner (DBPT), Resistance too high |
| B1362 | Driver seat belt pretensioner (DBPT), Resistance too low |
| B1363 | Driver seat belt pretensioner (DBPT), Short to GND |
| B1364 | Driver seat belt pretensioner (DBPT), Short Battery |
| B1367 | Passenger seat belt pretensioner (PBPT), Resistance too high |
| B1368 | Passenger seat belt pretensioner (PBPT), Resistance too low |
| B1369 | Passenger seat belt pretensioner (PBPT), Short to GND |
| B1370 | Passenger seat belt pretensioner (PBPT), Short to Battery |
| B1378 | Driver side airbag (DSAB), Resistance too high |
| B1379 | Driver side airbag (DSAB), Resistance too low |
| B1380 | Driver side airbag (DSAB), Short to GND |
| B1381 | Driver side airbag (DSAB), Short to Battery |
| B1382 | Passenger side airbag (PSAB), Resistance too high |
| B1383 | Passenger side airbag (PSAB), Resistance too low |
| B1384 | Passenger side airbag (PSAB), Short to GND |
| B1385 | Passenger side airbag (PSAB), Short to Battery |
| B1400 | Satellite left side sensor detect |
| B1401 | Satellite sensor left side short to GND |
| B1402 | Satellite sensor left side open/short to battery |
| B1403 | Satellite right side sensor detect |
| B1404 | Satellite sensor right side short to GND |
| B1405 | Satellite sensor right side open/short to battery |
| B1409 | Satellite left side sensor communication error |
| B1410 | Satellite right side sensor communication error |
| B1511 | Driver seat belt buckle switch open/short to battery |
| B1512 | Driver seat belt buckle switch short to GND |
| B1513 | Passenger seat belt buckle switch open/short to battery |
| B1514 | Passenger seat belt buckle switch short to GND |
| B1620 | Airbag unit internal failure |
| B1650 | SRSCM crash recorded |
| B1655 | Side airbag crash recorded |
| B1657 | Crash recorded-Belt pretensioner only |
| B1661 | ECU mismatching |
| B2500 | Warning lamp failure |

> **NOTE**
> - The DAB is located in the steering wheel.
> - The PAB is located in the crash pad.
> - The DSAB is located in the left side of driver's seat.
> - The PSAB is located in the right side of passenger's seat.

---

### Circuit Inspection

#### DTC B1111 / B1112

| DTC | Description |
|---|---|
| B1111 | Battery voltage too high (VBatt >= 19.2V) |
| B1112 | Battery voltage too low (VBatt <= 7.2V) |

#### Circuit Description

The SRS is equipped with a voltage increase or decrease circuit (DC-DC converter) in the SRSCM in case the source voltage goes down or up. When the battery voltage is down or up the voltage increase or decrease circuit (DC-DC converter) section will voltage. The diagnosis voltage of the SRS is normal that its circuit is different to other circuits. When the SRS warning lamp remains lit up and the DTC is a B1111 or B1112 code, battery voltage too high or low is indicated. When voltage returns to normal, the SRS warning light automatically goes off and a malfunction is no longer indicated.

#### Inspection Procedure

**1. Preparation**

1) Disconnect the negative (-) terminal cable from the battery, and wait at least 30 seconds.
2) Remove the DAB module.
3) Disconnect the connectors of the PAB, left and right side airbags, belt pretensioners and satellite sensors.
4) Disconnect the SRSCM connector.

> **CAUTION**
> Place the DAB with the front surface facing upward.

**2. Check source voltage.**

1) Connect the negative (-) terminal cable to the battery.
2) Turn the ignition switch ON.

<!-- Figure: SRSCM connector pinout showing Connector S207, source: RT.pdf page 29 -->

**[CHECK]**

Measure voltage between the battery supply terminal 21 of the SRS connector and body ground.

**LIMIT: 9-16V**

- **NG** --> Check the harness between the battery and the SRSCM. Check the battery and charging system.
- **OK** --> (continue)

**3. Does the SRS warning light turn off?**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Connect the DAB module.
3) Connect the PAB connector, left and right side airbag, belt pretensioner and satellite connectors.
4) Connect the SRSCM connector.
5) Turn the ignition switch ON.

<!-- Figure: Instrument cluster showing SRS warning light, source: RT.pdf page 30 -->

**[CHECK]**

Check that the SRS warning light goes off.

- **NG** --> Check for DTCs. If a DTC is output, perform troubleshooting for the DTC. If B1111 or B1112 is output, replace the SRSCM.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

---

### Circuit Inspection - Short to Ground

#### DTCs: B1348, B1354, B1363, B1369, B1380, B1384, B1401, B1404

| DTC | Description |
|---|---|
| B1348 | DAB short to ground |
| B1354 | PAB short to ground |
| B1363 | DBPT short to ground |
| B1369 | PBPT short to ground |
| B1380 | DSAB short to ground |
| B1384 | PSAB short to ground |
| B1401 | Satellite sensor left side short to ground |
| B1404 | Satellite sensor right side short to ground |

#### Circuit Description

The squib circuit consists of the SRSCM, clock spring, DAB, PAB, SAB, BPT, and satellite sensors. It causes the SRS to deploy when the SRS deployment conditions are satisfied. The above DTCs are recorded when a short to ground is detected in a squib circuit.

| DTC Detecting Condition | Trouble Area |
|---|---|
| Short circuit in squib wire harness (to ground) | DAB squib |
| Squib malfunction | PAB squib |
| Clock spring malfunction | DSAB squib |
| SRSCM malfunction | PSAB squib |
| | BPT squib |
| | Satellite sensor |
| | Clock spring |
| | SRSCM |
| | Wire harness |

#### Wiring Diagram (Short to Ground)

```
         High (s) ┌──────────────┐
S ───────Low (s)──┤ DSAB or PSAB │
                  │    Squib     │
         High (s) ├──────────────┤
R ───────Low (s)──┤  DAB Squib   │
                  │              │
         High (s) ├──────────────┤
S ───────Low (s)──┤  PAB Squib   │
                  │              │
         High (s) ├──────────────┤
C ───────Low (s)──┤  BPT Squib   │
                  │              │
         High (s) ├──────────────┤
M ───────Low (s)──┤  Satellite   │
                  │  Sensors     │
                  └──────────────┘
```

<!-- Figure: SRSCM squib circuit wiring diagram (short to ground), source: RT.pdf page 31 -->

#### Inspection Procedure

**1. Preparation**

1) Disconnect negative (-) terminal cable from the battery, and wait at least 30 seconds.
2) Remove the DAB module.
3) Disconnect the connectors of the PAB, left and right side airbag, belt pretensioner and satellite sensor.
4) Disconnect the connector of the SRSCM.

> **CAUTION**
> Place the DAB with the front surface facing upward.

**2. Check DAB squib circuit.**

<!-- Figure: DAB squib connector measurement, source: RT.pdf page 32 -->

**[CHECK]**

For the connector (on the clock spring side) between clock spring and DAB, measure the resistance between DAB high and body ground.

**Resistance: infinity**

- **NG** --> Go to step "13"
- **OK** --> Go to step "8"

**3. Check the PAB squib circuit.**

<!-- Figure: PAB squib connector measurement, source: RT.pdf page 32 -->

**[CHECK]**

For the connector (on the SRSCM side) between SRSCM and PAB, measure the resistance between PAB high and body ground.

**Resistance: infinity**

- **NG** --> Repair or replace harness or connector between the SRSCM and the PAB.
- **OK** --> Go to step "9"

**4. Check PSAB and DSAB squib circuits.**

<!-- Figure: SAB squib connector measurement, source: RT.pdf page 32 -->

**[CHECK]**

For the connector (on the SRSCM side) between SRSCM and SABs, measure the resistance between the SABs high and body ground.

**Resistance: infinity**

- **NG** --> Repair or replace the harness between the SRSCM and the SAB.
- **OK** --> Go to step "10"

**5. Check the BPT's squib circuit.**

<!-- Figure: BPT squib connector measurement, source: RT.pdf page 33 -->

**[CHECK]**

For the connector (on the SRSCM side) between the SRSCM and BPT, measure the resistance between the BPT's high and body ground.

**Resistance: infinity**

- **NG** --> Repair or replace the harness between the SRSCM and the BPTs.
- **OK** --> Go to step "11"

**6. Check Satellite sensor circuit.**

<!-- Figure: Satellite sensor connector measurement, source: RT.pdf page 33 -->

**[CHECK]**

For the connector (on the SRSCM side) between the SRSCM and the Satellite sensor, measure the resistance between Satellite high and body ground.

**Resistance: infinity**

- **NG** --> Repair or replace the harness between the SRSCM and the Satellite sensor.
- **OK** --> Go to step "12"

**7. Check the SRSCM.**

**[PREPARATION]**

1) Connect the connector to the SRSCM.
2) Using a service wire, connect the DAB high and DAB low on the clock spring side of connector.
3) Using a service wire, connect the PAB high and low on the SRSCM side of connector.
4) Using a service wire, connect the SAB high and low on the SRSCM side connector between the SRSCM and the SAB.
5) Using a service wire, connect the BPT high and low on the SRSCM side connector between the SRSCM and the BPT.
6) Using a service wire, connect the satellite high and low on the SRSCM side connector between the SRSCM and the Satellite sensor.
7) Connect negative (-) terminal cable to battery, and wait at least 30 seconds.

<!-- Figure: SRSCM connector with service wires installed, source: RT.pdf page 33 -->

**[CHECK]**

1) Turn ignition switch to ON, and wait for at least 30 seconds.
2) Clear any codes stored in the memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for 30 seconds.
4) Turn the ignition switch to ON, and wait for 30 seconds.
5) Using the Hi-Scan Pro, check for DTCs. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this check.

- **NG** --> Replace the SRSCM.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

**8. Check the DAB squib.**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the negative (-) terminal cable from the battery, and wait for 30 seconds.
3) Connect the DAB connector.
4) Connect the negative (-) terminal cable to the battery, and wait for 30 seconds.

<!-- Figure: DAB connector, source: RT.pdf page 34 -->

**[CHECK]**

1) Turn the ignition switch to ON, and wait for at least 30 seconds.
2) Clear the malfunction code stored in the memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for 30 seconds.
4) Turn the ignition switch to ON, and wait for 30 seconds.
5) Using the Hi-Scan Pro, check for DTCs. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this procedure.

- **NG** --> Replace the DAB.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

**9. Check the PAB squib.**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the negative (-) terminal cable from the battery, and wait for 30 seconds.
3) Connect the PAB connector.
4) Connect the negative (-) terminal cable from the battery, and wait for 30 seconds.

<!-- Figure: PAB connector, source: RT.pdf page 34 -->

**[CHECK]**

1) Turn the ignition switch to ON, and wait for at least 30 seconds.
2) Clear the malfunction code stored in the memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for 30 seconds.
4) Turn the ignition switch to ON, and wait for 30 seconds.
5) Using the Hi-Scan Pro, check for DTCs. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this procedure.

- **NG** --> Replace the PAB.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

**10. Check the SABs squib.**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the negative (-) terminal cable from the battery, and wait for 30 seconds.
3) Connect the SAB connector.
4) Connect the negative (-) terminal cable from the battery, and wait for 30 seconds.

<!-- Figure: SAB connector, source: RT.pdf page 35 -->

**[CHECK]**

1) Turn the ignition switch to ON, and wait for at least 30 seconds.
2) Clear the malfunction code stored in the memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for 30 seconds.
4) Turn the ignition switch ON, and wait for 30 seconds.
5) Using the Hi-Scan Pro, check for DTCs. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this procedure.

- **NG** --> Replace the SAB.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

> **NOTE**
> Check the DSAB using the same procedure.

**11. Check BPT squib.**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the negative (-) terminal cable from the battery, and wait for 30 seconds.
3) Connect the BPT's connector.
4) Connect the negative (-) terminal cable from the battery, and wait for 30 seconds.

<!-- Figure: BPT connector, source: RT.pdf page 36 -->

**[CHECK]**

1) Turn the ignition switch to ON, and wait for at least 30 seconds.
2) Clear the malfunction code stored in the memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for at least 30 seconds.
4) Turn the ignition switch to ON, and wait for at least 30 seconds.
5) Using the Hi-Scan Pro, check for DTCs. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this procedure.

- **NG** --> Replace the BPT.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

**12. Check the Satellite sensors.**

**[PREPARATION]**

1) Turn the ignition to LOCK.
2) Disconnect negative (-) terminal cable from the battery, and wait at least 30 seconds.
3) Connect the Satellite sensor connector.
4) Connect the negative (-) terminal cable from the battery, and wait at least 30 seconds.

<!-- Figure: Satellite sensor connector, source: RT.pdf page 36 -->

**[CHECK]**

1) Turn the ignition switch to ON, and wait for at least 30 seconds.
2) Clear the malfunction code stored in the memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for at least 30 seconds.
4) Turn the ignition switch to ON, and wait for at least 30 seconds.
5) Using the Hi-Scan Pro, check for DTCs. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this procedure.

- **NG** --> Replace the Satellite sensor.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

**13. Check clock spring.**

**[PREPARATION]**

Disconnect connector between SRSCM and clock spring.

<!-- Figure: Clock spring connector, source: RT.pdf page 36 -->

**[CHECK]**

Measure resistance between the DAB high on the clock spring side of connector between clock spring and DAB and body ground.

**Resistance: infinity**

- **NG** --> Replace the clock spring.
- **OK** --> Repair or replace the harness or the connector between the SRSCM and the clock spring.

---

### Circuit Inspection - Short to Battery

#### DTCs: B1349, B1355, B1364, B1370, B1381, B1385, B1402, B1405

| DTC | Description |
|---|---|
| B1349 | DAB short to battery |
| B1355 | PAB short to battery |
| B1364 | DBPT short to battery |
| B1370 | PBPT short to battery |
| B1381 | DSAB short to battery |
| B1385 | PSAB short to battery |
| B1402 | Satellite left side short to battery |
| B1405 | Satellite right side short to battery |

#### Circuit Description

The squib circuit consists of the SRSCM, clock spring, DAB, PAB, DSAB, PSAB, BPT and satellite sensors. If it causes the SRS to deploy when the SRS deployment conditions are satisfied. The above DTCs are recorded when a B+ short is detected in the squib circuit.

| DTC Detecting Condition | Trouble Area |
|---|---|
| Short circuit in squib wire harness (to B+) | DAB squib |
| Squib malfunction | PAB squib |
| Clock spring cable malfunction | DSAB or PSAB squib |
| SRSCM malfunction | BPT squib |
| | Satellite sensor |
| | Clock spring |
| | SRSCM |
| | Wire harness |

#### Wiring Diagram (Short to Battery)

```
                  ┌──────────────────┐
         High (s) │ DSAB or PSAB     │
S ───────Low (s)──┤    Squib         │
                  │                  │
         High (s) ├──────────────────┤
R ───────Low (s)──┤  DAB Squib       │
                  │                  │
         High (s) ├──────────────────┤
S ───────Low (s)──┤  PAB Squib       │
                  │                  │
         High (s) ├──────────────────┤
C ───────Low (s)──┤  BPT Squib       │
                  │                  │
         High (s) ├──────────────────┤
M ───────Low (s)──┤  Satellite       │
                  │  Sensors         │
                  └──────────────────┘
```

<!-- Figure: SRSCM squib circuit wiring diagram (short to battery), source: RT.pdf page 37 -->

#### Inspection Procedure

**1. Preparation**

1) Disconnect negative (-) terminal cable from the battery, and wait at least 30 seconds.
2) Remove the DAB module.
3) Disconnect the connectors of the PAB, left and right side airbag, belt pretensioner and satellite sensor.
4) Disconnect the connector of the SRSCM.

> **CAUTION**
> Place the DAB with the front surface facing upward.

**2. Check DAB squib circuit.**

<!-- Figure: DAB squib connector voltage measurement, source: RT.pdf page 38 -->

**[CHECK]**

For the connector (on the clock spring side) between the clock spring and DAB, measure the voltage between DAB high and body ground.

**Voltage: 0 V**

- **NG** --> Go to step "13"
- **OK** --> Go to step "8"

**3. Check the PAB squib circuit.**

<!-- Figure: PAB squib connector voltage measurement, source: RT.pdf page 38 -->

**[CHECK]**

For the connector (on the SRSCM side) between the SRSCM and PAB, measure the voltage between the PAB high and body ground.

**Voltage: 0 V**

- **NG** --> Repair or replace the harness between the SRSCM and the PAB.
- **OK** --> Go to step "9"

**4. Check the SAB squib circuit.**

<!-- Figure: SAB squib connector voltage measurement, source: RT.pdf page 38 -->

**[CHECK]**

For the connector (on the SRSCM side) between SRSCM and SAB, measure the voltage between the SAB high and body ground.

**Voltage: 0 V**

- **NG** --> Repair or replace the harness between the SRSCM and the SAB.
- **OK** --> Go to step "10"

**5. Check the BPTs squib circuits.**

<!-- Figure: BPT squib connector voltage measurement, source: RT.pdf page 39 -->

**[CHECK]**

For the connector between SRSCM and BPTs, measure the voltage between the BPTs high and body ground.

**Voltage: 0 V**

- **NG** --> Repair or replace the harness between the SRSCM and the BPTs.
- **OK** --> Go to step "11"

**6. Check Satellite sensor circuit.**

<!-- Figure: Satellite sensor connector voltage measurement, source: RT.pdf page 39 -->

**[CHECK]**

For the connector between the SRSCM and the Satellite sensor, measure the voltage between the Satellite sensor high and body ground.

**Voltage: 0 V**

- **NG** --> Repair or replace the harness between the SRSCM and the Satellite sensor.
- **OK** --> Go to step "12"

**7. Check the SRSCM.**

**[PREPARATION]**

1) Connect the connector to the SRSCM.
2) Using a service wire, connect the DAB high and low on the clock spring side of connector between the clock spring and the DAB.
3) Using a service wire, connect the PAB high and low on the SRSCM side of connector.
4) Using a service wire, connect the SAB high and low on the SRSCM side connector between the SRSCM and the SAB.
5) Using a service wire, connect the BPT high and low on the SRSCM side connector between the SRSCM and the BPT.
6) Using a service wire, connect the satellite high and low on the SRSCM side connector between the SRSCM and the Satellite sensor.
7) Connect negative (-) terminal cable to battery, and wait at least 30 seconds.

<!-- Figure: SRSCM connector with service wires for short to battery test, source: RT.pdf page 39 -->

**[CHECK]**

1) Turn ignition switch to ON, and wait for at least 30 seconds.
2) Clear the malfunction code stored in memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for at least 30 seconds.
4) Turn the ignition switch to ON, and wait for 30 seconds.
5) Using the Hi-Scan Pro, check for DTCs. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this check.

- **NG** --> Replace the SRSCM.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

**8. Check the DAB squib.**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the negative (-) terminal cable from the battery, and wait for 30 seconds.
3) Connect the DAB connector.
4) Connect the negative (-) terminal cable to the battery, and wait for 30 seconds.

<!-- Figure: DAB connector for short to battery test, source: RT.pdf page 40 -->

**[CHECK]**

1) Turn the ignition switch ON, and wait for at least 30 seconds.
2) Clear the malfunction code stored in the memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for 30 seconds.
4) Turn the ignition switch ON, and wait for 30 seconds.
5) Using the Hi-Scan Pro, check for DTCs. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this procedure.

- **NG** --> Replace the DAB.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

**9. Check the PAB squib.**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the negative (-) terminal cable from the battery, and wait for 30 seconds.
3) Connect the PAB connector.
4) Connect the negative (-) terminal cable from the battery, and wait for 30 seconds.

<!-- Figure: PAB connector for short to battery test, source: RT.pdf page 40 -->

**[CHECK]**

1) Turn the ignition switch to ON, and wait for at least 30 seconds.
2) Clear the malfunction code stored in the memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for 30 seconds.
4) Turn the ignition switch ON, and wait for 30 seconds.
5) Using the Hi-Scan Pro, check for DTCs. **There is no DTC.**
