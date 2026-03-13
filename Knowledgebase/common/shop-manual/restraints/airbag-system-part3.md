---
source: RT.pdf
chapter: RT
title: "Airbag System (Part 3)"
pages: 41-60
section: "Troubleshooting (continued), Airbag Module Disposal"
---

# Airbag System (Part 3)

## Troubleshooting (continued)

### Circuit Inspection - Short to Battery (continued)

**10. Check the SAB squib.**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the negative (-) terminal cable from the battery, and wait for 30 seconds.
3) Connect the SAB connector.
4) Connect the negative (-) terminal cable from the battery, and wait for 30 seconds.

<!-- Figure: SAB connector for short to battery test, source: RT.pdf page 41 -->

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

**11. Check the BPT's squib.**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the negative (-) terminal cable from the battery, and wait for 30 seconds.
3) Connect the BPT's connector.
4) Connect the negative (-) terminal cable to the battery, and wait for 30 seconds.

<!-- Figure: BPT connector for short to battery test, source: RT.pdf page 41 -->

**[CHECK]**

1) Turn the ignition switch to ON, and wait for 30 seconds.
2) Clear the malfunction code stored in the memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for 30 seconds.
4) Turn the ignition switch to ON, and wait for 30 seconds.
5) Using the Hi-Scan Pro, check for DTCs. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this procedure.

- **NG** --> Replace the BPT.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

**12. Check the Satellite sensors.**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the negative (-) terminal cable from the battery, and wait at least 30 seconds.
3) Connect the Satellite sensor connector.
4) Connect the negative (-) terminal cable from the battery, and wait at least 30 seconds.

<!-- Figure: Satellite sensor connector for short to battery test, source: RT.pdf page 42 -->

**[CHECK]**

1) Turn the ignition switch to ON, and wait for at least 30 seconds.
2) Clear the malfunction code stored in memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait at least 30 seconds.
4) Turn the ignition switch to ON, and wait at least 30 seconds.
5) Using the Hi-Scan Pro, check for DTCs. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this procedure.

- **NG** --> Replace the Satellite sensor.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

**13. Check the clock spring.**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the connector between the SRSCM and the clock spring.

<!-- Figure: Clock spring connector with High (+) and Low (-) pins labeled, source: RT.pdf page 42 -->

**[CHECK]**

Turn the ignition switch ON, and measure the voltage between the DAB high side and the body ground.

**Voltage: 0V**

- **NG** --> Replace the clock spring.
- **OK** --> Repair or replace the harness or the connector between the SRSCM and the clock spring.

---

### Circuit Inspection - DAB Resistance Too High / Too Low

#### DTCs: B1346 / B1347

| DTC | Description |
|---|---|
| B1346 | DAB resistance too high (R >= 6.70 Ohm) |
| B1347 | DAB resistance too low (R <= 1.06 Ohm) |

#### Circuit Description

The DAB squib circuit consists of the SRSCM, the clock spring, the DAB. It causes the airbag to deploy when the airbag deployment conditions are satisfied. The above DTCs are recorded when the DAB circuit is open or the DAB resistance too high or low is detected in the DAB squib circuit.

| DTC Detecting Condition | Trouble Area |
|---|---|
| Too high or low resistance between DAB high (+) wiring harness and DAB low (-) wiring harness of squib. | DAB squib |
| DAB malfunction | Clock spring |
| Clock spring malfunction | SRSCM |
| SRSCM malfunction | Wire harness |

#### Wiring Diagram

```
S ──┐
R ──┤         ┌────────────┐   High (+)  ┌───────────┐
S ──┤ SRSCM ──┤Clock Spring├────────────►│ DAB Squib │
C ──┤         └────────────┘   Low (-)   └───────────┘
M ──┘
```

<!-- Figure: DAB squib circuit wiring diagram through clock spring, source: RT.pdf page 43 -->

#### Inspection Procedure

**1. Preparation**

1) Disconnect the negative (-) terminal cable from the battery, and wait at least 30 seconds.
2) Remove the DAB module.
3) Disconnect the connectors of the PAB, left and right side airbags, belt pretensioners and satellite sensors.
4) Disconnect the SRSCM connector.

> **CAUTION**
> Place the DAB with the front surface facing upward.

**2. Check the DAB resistance.**

**[PREPARATION]**

Release the airbag activation prevention mechanism on the SRSCM side of the airbag squib side. Connect the dummy (0957A-38200) and dummy adapter (0957A-38400) to the clock spring side connector.

> **CAUTION**
> Never attempt to measure the circuit resistance of the airbag module (squib) even if you are using the specified tester.

> **NOTE**
> Before checking the resistance, you have to insert the shorting bar insert plastic that is attached to the diagnosis checker into the SRSCM connector.

<!-- Figure: Dummy adapter connected to clock spring side connector, source: RT.pdf page 44 -->

**[CHECK]**

Measure the resistance between the DAB high (+) and low (-).

**1.80 Ohm <= R <= 3.40 Ohm**

- **NG** --> Go to step "4"
- **OK** --> (continue)

**3. Check the DAB squib.**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the negative (-) terminal cable from the battery, and wait for 30 seconds.
3) Connect the DAB connector.
4) Connect the negative (-) terminal cable to the battery, and wait for 30 seconds.

<!-- Figure: DAB connector, source: RT.pdf page 44 -->

**[CHECK]**

1) Turn the ignition switch to ON, and wait for at least 30 seconds.
2) Clear the malfunction code stored in the memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for 30 seconds.
4) Turn the ignition switch to ON, and wait for 30 seconds.
5) Using the Hi-Scan Pro, check the DTC. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this procedure.

- **NG** --> Replace the DAB.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

**4. Check the clock spring.**

**[PREPARATION]**

Disconnect the connector between the SRSCM clock spring, and connect the dummy connector (0957A-38200) and dummy adapter (0957A-38400) to the clock spring side connector.

> **NOTE**
> Before checking the resistance, you have to insert the shorting bar insert plastic that is attached to the diagnosis checker into the SRSCM connector.

<!-- Figure: Dummy adapter on clock spring side with SRSCM disconnected, source: RT.pdf page 45 -->

**[CHECK]**

Measure the resistance between the DAB high (+) and low (-).

**1.80 Ohm <= R <= 3.40 Ohm**

- **NG** --> Replace the clock spring.
- **OK** --> Repair or replace the harness or the connector between the SRSCM and the clock spring.

---

### Circuit Inspection - PAB Resistance Too High / Too Low

#### DTCs: B1352 / B1353

| DTC | Description |
|---|---|
| B1352 | PAB resistance too high (R >= 5.4 Ohm) |
| B1353 | PAB resistance too low (R <= 0.4 Ohm) |

#### Circuit Description

The PAB squib circuit consists of the SRSCM and PAB. It causes the airbag to deploy when the airbag deployment conditions are satisfied. The above DTCs are recorded when the PAB circuit is open or the PAB resistance too high or low is detected in the PAB squib circuit.

| DTC Detecting Condition | Trouble Area |
|---|---|
| Too high or low resistance between PAB high (+) wiring harness and PAB low (-) wiring harness of squib. | PAB squib |
| PAB malfunction | SRSCM |
| SRSCM malfunction | Wire harness |

#### Wiring Diagram

```
S ──┐
R ──┤              High (+)  ┌───────────┐
S ──┤ SRSCM ────────────────►│ PAB Squib │
C ──┤              Low (-)   └───────────┘
M ──┘
```

<!-- Figure: PAB squib circuit wiring diagram, source: RT.pdf page 46 -->

#### Inspection Procedure

**1. Preparation**

1) Disconnect the negative (-) terminal cable from the battery, and wait at least 30 seconds.
2) Remove the DAB module.
3) Disconnect the connectors of the PAB, left and right side airbags, belt pretensioners and satellite sensors.
4) Disconnect the SRSCM connector.

> **CAUTION**
> Place the DAB with the front surface facing upward.

**2. Check the PAB resistance.**

**[PREPARATION]**

Release the airbag activation prevention mechanism on the SRSCM side of the airbag squib side. Connect the dummy (0957A-38200) and dummy adapter (0957A-38400) to PAB connector of the SRSCM connector side.

> **NOTE**
> Before checking the resistance, you have to insert the shorting bar insert plastic that is attached to the diagnosis checker into the SRSCM connector.

<!-- Figure: Dummy adapter connected to PAB connector on SRSCM side, source: RT.pdf page 47 -->

**[CHECK]**

Measure the resistance between the PAB high (+) and the PAB low (-).

**1.6 Ohm <= R <= 2.8 Ohm**

- **NG** --> Repair or replace the harness between the SRSCM and the PAB.
- **OK** --> (continue)

**3. Check the PAB squib.**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the negative (-) terminal cable from the battery, and wait for 30 seconds.
3) Connect the PAB connector.
4) Connect the negative (-) terminal cable to the battery, and wait for 30 seconds.

<!-- Figure: PAB connector, source: RT.pdf page 47 -->

**[CHECK]**

1) Turn the ignition switch to ON, and wait for at least 30 seconds.
2) Clear the malfunction code stored in the memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for 30 seconds.
4) Turn the ignition switch to ON, and wait for 30 seconds.
5) Using the Hi-Scan Pro, check the DTC. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this procedure.

- **NG** --> Replace the PAB.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

---

### Circuit Inspection - SAB Resistance Too High / Too Low

#### DTCs: B1378, B1379, B1382, B1383

| DTC | Description |
|---|---|
| B1378 | DSAB Resistance too high (R >= 5.4 Ohm) |
| B1379 | DSAB Resistance too low (R <= 0.4 Ohm) |
| B1382 | PSAB Resistance too high (R >= 5.4 Ohm) |
| B1383 | PSAB Resistance too low (R <= 0.4 Ohm) |

#### Circuit Description

The SAB squib circuit consists of the SRSCM and SAB. It causes the airbag to deploy when the airbag deployment conditions are satisfied. The above DTCs are recorded when the SAB circuit is open or the SAB resistance too high or low is detected in the SAB squib circuit.

| DTC Detecting Condition | Trouble Area |
|---|---|
| Too high or low resistance between SAB high (+) wiring harness and SAB low (-) wiring harness of squib. | SAB squib |
| SAB malfunction | SRSCM |
| SRSCM malfunction | Wire harness |

#### Wiring Diagram

```
S ──┐
R ──┤              High (+)  ┌───────────┐
S ──┤ SRSCM ────────────────►│ SAB (LH)  │
C ──┤              Low (-)   └───────────┘
M ──┤              High (+)  ┌───────────┐
    └─────────────────────►  │ SAB (RH)  │
                   Low (-)   └───────────┘
```

<!-- Figure: SAB (LH and RH) squib circuit wiring diagram, source: RT.pdf page 49 -->

#### Inspection Procedure

**1. Preparation**

1) Disconnect the negative (-) terminal cable from the battery, and wait at least 30 seconds.
2) Remove the DAB module.
3) Disconnect the connectors of the PAB, left and right side airbags, belt pretensioners and satellite sensors.
4) Disconnect the SRSCM connector.

> **CAUTION**
> Place the DAB with the front surface facing upward.

**2. Check the SAB resistance.**

**[PREPARATION]**

Release the airbag activation prevention mechanism on the SRSCM side of the airbag squib side. Connect the dummy (0957A-38200) and dummy adapter (0957A-38400) to the SAB connector of the SRSCM connector side.

> **NOTE**
> Before checking the resistance, you have to insert the shorting bar insert plastic that is attached to the diagnosis checker into the SRSCM connector.

<!-- Figure: Dummy adapter connected to SAB connector on SRSCM side, source: RT.pdf page 50 -->

**[CHECK]**

Measure the resistance between the SAB high (+) and the SAB low (-).

**1.6 Ohm <= R <= 2.8 Ohm**

- **NG** --> Repair or replace the harness between the SRSCM and the SAB.
- **OK** --> (continue)

**3. Check the SAB squib.**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the negative (-) terminal cable from the battery, and wait for 30 seconds.
3) Connect the SAB connector.
4) Connect the negative (-) terminal cable to the battery, and wait for 30 seconds.

<!-- Figure: SAB connector, source: RT.pdf page 50 -->

**[CHECK]**

1) Turn the ignition switch to ON, and wait for at least 30 seconds.
2) Clear the malfunction code stored in the memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for 30 seconds.
4) Turn the ignition switch to ON, and wait for 30 seconds.
5) Using Hi-Scan Pro, check the DTC. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this procedure.

- **NG** --> Replace the SAB.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

---

### Circuit Inspection - BPT Resistance Too High / Too Low

#### DTCs: B1361, B1362, B1367, B1368

| DTC | Description |
|---|---|
| B1361 | DBPT Resistance too high (R >= 5.4 Ohm) |
| B1362 | DBPT Resistance too low (R <= 0.4 Ohm) |
| B1367 | PBPT Resistance too high (R >= 5.4 Ohm) |
| B1368 | PBPT Resistance too low (R <= 0.4 Ohm) |

#### Circuit Description

The BPT squib circuit consists of the SRSCM and BPT. It causes the airbag to deploy when the airbag deployment conditions are satisfied. The above DTCs are recorded when the BPT circuit is open or the BPT resistance too high or low is detected in the BPT squib circuit.

| DTC Detecting Condition | Trouble Area |
|---|---|
| Too high or low resistance between BPT high (+) wiring harness and BPT low (-) wiring harness of squib. | BPT squib |
| BPT malfunction | SRSCM |
| SRSCM malfunction | Wire harness |

#### Wiring Diagram

```
S ──┐
R ──┤              High (+)  ┌───────────┐
S ──┤ SRSCM ────────────────►│ BPT (LH)  │
C ──┤              Low (-)   └───────────┘
M ──┤              High (+)  ┌───────────┐
    └─────────────────────►  │ BPT (RH)  │
                   Low (-)   └───────────┘
```

<!-- Figure: BPT (LH and RH) squib circuit wiring diagram, source: RT.pdf page 51 -->

#### Inspection Procedure

**1. Preparation**

1) Disconnect the negative (-) terminal cable from the battery, and wait at least 30 seconds.
2) Remove the DAB module.
3) Disconnect the connectors of the PAB, left and right side airbags, belt pretensioners and satellite sensors.
4) Disconnect the SRSCM connector.

> **CAUTION**
> Place the DAB with the front surface facing upward.

**2. Check the BPT resistance.**

**[PREPARATION]**

Release the airbag activation prevention mechanism on the SRSCM side of the airbag squib side. Connect the dummy (0957A-38200) and dummy adapter (0957A-38400) to the BPT connector of the SRSCM connector side.

> **NOTE**
> Before checking the resistance, you have to insert the shorting bar insert plastic that is attached to the diagnosis checker into the SRSCM connector.

<!-- Figure: Dummy adapter connected to BPT connector on SRSCM side, source: RT.pdf page 52 -->

**[CHECK]**

Measure the resistance between the BPT high (+) and the BPT low (-).

**1.6 Ohm <= R <= 2.8 Ohm**

- **NG** --> Repair or replace the harness between the SRSCM and the BPT.
- **OK** --> (continue)

**3. Check the BPT squib.**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the negative (-) terminal cable from the battery, and wait for 30 seconds.
3) Connect the BPT connector.
4) Connect the negative (-) terminal cable to the battery, and wait for 30 seconds.

<!-- Figure: BPT connector, source: RT.pdf page 52 -->

**[CHECK]**

1) Turn the ignition switch to ON, and wait for at least 30 seconds.
2) Clear the malfunction code stored in the memory with the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for 30 seconds.
4) Turn the ignition switch to ON, and wait for 30 seconds.
5) Using Hi-Scan Pro, check the DTC. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this procedure.

- **NG** --> Replace the BPT.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

---

### Circuit Inspection - Satellite Sensor Defect / Communication Error

#### DTCs: B1400, B1403, B1409, B1410

| DTC | Description |
|---|---|
| B1400 | Satellite left side defect |
| B1403 | Satellite right side defect |
| B1409 | Satellite left communication error |
| B1410 | Satellite right communication error |

#### Circuit Description

The release system for the airbag consists of the SRSCM and two satellites - one on the left-hand side and one on the right. The above DTCs are recorded when a defect or communication error of the satellite is detected in the satellite circuit.

#### Wiring Diagram

```
S ──┐
R ──┤              High (+)  ┌─────────────────┐
S ──┤ SRSCM ────────────────►│ Satellite       │
C ──┤              Low (-)   │ Sensor (LH)     │
M ──┤                        └─────────────────┘
    │              High (+)  ┌─────────────────┐
    └─────────────────────►  │ Satellite       │
                   Low (-)   │ Sensor (RH)     │
                             └─────────────────┘
```

<!-- Figure: Satellite sensor (LH and RH) wiring diagram, source: RT.pdf page 53 -->

#### Inspection Procedure

**1. Preparation**

1) Disconnect the negative (-) terminal cable from the battery, and wait at least 30 seconds.
2) Remove the DAB module.
3) Disconnect the connectors of the PAB, left and right side airbags, belt pretensioners and satellite sensors.
4) Disconnect the SRSCM connector.

> **CAUTION**
> Place the DAB with the front surface facing upward.

**2. Check satellite circuit (communication error).**

**[PREPARATION]**

Check continuity between the SRSCM connector and the satellite connector as high (+) and high, low (-) and low (-).

**OK: Continuity**

- **NG** --> Repair or replace the harness between the SRSCM and the Satellite sensor.
- **OK** --> (continue)

<!-- Figure: SRSCM to satellite sensor connector continuity check, source: RT.pdf page 54 -->

**3. Check the satellite sensor (defect).**

**[PREPARATION]**

1) Turn the ignition switch to LOCK.
2) Disconnect the negative (-) terminal cable from the battery, and wait for 30 seconds.
3) Connect the satellite connector.
4) Connect the negative (-) terminal cable to the battery, and wait for 30 seconds.

<!-- Figure: Satellite sensor connector with Satellite (LH) and Satellite (RH) labeled, source: RT.pdf page 54 -->

**[CHECK]**

1) Turn the ignition switch to ON, and wait for at least 30 seconds.
2) Clear the malfunction code stored in the memory of the Hi-Scan Pro.
3) Turn the ignition switch to LOCK, and wait for 30 seconds.
4) Turn the ignition switch to ON, and wait for 30 seconds.
5) Using the Hi-Scan Pro, check DTC. **There is no DTC.**

> **[HINT]**
> Codes other than these may be output at this time, but they are not relevant to this check.

- **NG** --> Replace the Satellite sensor.
- **OK** --> From the results of the above inspection, the malfunctioning part can now be considered normal.

---

### Circuit Inspection - Seat Belt Buckle Switch

#### DTCs: B1511, B1512, B1513, B1514

| DTC | Description |
|---|---|
| B1511 | Driver seat belt switch open/short to Battery |
| B1512 | Driver seat belt switch short to GND |
| B1513 | Passenger seat belt switch open/short to Battery |
| B1514 | Passenger seat belt switch short to GND |

#### Circuit Description

This system decides whether the seat belt of the driver or passenger are locked and then prevent the belt pretensioner deploying on crash.

#### Inspection Procedure

**1. Preparation**

**2. Check buckle switch sensor circuit (Short to GND/Battery).**

<!-- Figure: Seat belt switch connector locations (driver and passenger), source: RT.pdf page 55 -->

**[CHECK]**

Measure the voltage and resistance of the seat belt switch high and body ground between the SRSCM connector and the seat belt switch connector.

**Resistance: infinity**
**Voltage: 0V**

- **NG** --> Repair or replace the harness between the SRSCM and the seat belt switch.
- **OK** --> (continue)

**3. Check the seat belt switch.**

<!-- Figure: Seat belt switch, source: RT.pdf page 55 -->

**[CHECK]**

Check the resistance with the switch on and off.

| Condition | Resistance |
|---|---|
| SWITCH OPEN (Belted) | R = 4 kOhm +/- 10% |
| SWITCH OPEN (Unbelted) | R = 1 kOhm +/- 10% |

- **NG** --> Replace the seat belt switch.
- **OK** --> From the results of the above inspection the malfunctioning part can now be considered normal.

---

### Circuit Inspection - Warning Lamp Failure

#### DTC: B2500

| DTC | Description |
|---|---|
| B2500 | Warning lamp failure |

#### Circuit Description

The SRS warning lamp is located in the cluster. When the ignition switch is turned ON, it illuminates for about 6 seconds after the ignition switch is turned ON, and then turns off automatically. If there is a malfunction in the airbag system, the SRS lights up to inform the driver of the abnormality. The SRSCM shall measure the voltage at the airbag SRI (Malfunction Indicator Lamp) output pin, both when the lamp is on and when the lamp is off, to detect whether the commanded state matches the actual state.

#### Inspection Procedure

**1. Check the fuse.**

**[PREPARATION]**

1) Remove airbag fuse and airbag warning lamp fuse from the fuse box.
2) Inspect the state of the fuses.
3) Replace if necessary.

**2. Check the SRS warning lamp circuit.**

**[PREPARATION]**

1) Connect the negative (-) terminal cable to the battery.
2) Turn the ignition switch to ON.

<!-- Figure: SRSCM connector showing Connector S207, pins for SRS MIL, source: RT.pdf page 56 -->

**[CHECK]**

1) Measure voltage at the harness side connector of the SRSCM.

**Voltage: 9-16 V**

- **NG** --> Check the SRS warning light bulb/repair the SRS warning light circuit.
- **OK** --> (continue)

**2. Check the SRS SRI (Service Reminder Indicator).**

**OK: SRS SRI ON**

- **NG** --> If no fault is found in wiring or connector, replace the SRSCM.
- **OK** --> From the results of the above inspection, the part can now be considered to be normal.

---

### Circuit Inspection - SRSCM Malfunction

#### DTCs: B1620, B1650, B1655, B1657, B1661

| DTC | Description |
|---|---|
| B1620 | Airbag unit internal failure |
| B1650 | SRSCM crash recorded |
| B1655 | Side airbag crash recorded |
| B1657 | Crash recorded-Belt pretensioner only |
| B1661 | ECU mismatching |

#### Circuit Description

The SRSCM shall also cyclically monitor the following:

1. Functional readiness of the firing circuit activation transistors.
2. Adequacy of deployment energy reserves.
3. Safing sensor integrity / detection of faulty closure.
4. Plausibility of accelerometer signal.
5. Operation of SRSCM components.

The timely completion of all tests is monitored by a separate hardware watchdog. During normal operation, the watch dog is triggered periodically by the SRSCM. If the SRSCM fails to trigger the watchdog, the watchdog will reset the SRSCM and activate the SRI (Service Reminder Indicator). The SRSCM must be replaced once the fault codes mentioned above are confirmed.

---

## Airbag Module Disposal

### Field Deployment Procedures

> **CAUTION**
> When handling the deployed airbag be careful that not the dust enters your eyes and always wear gloves to avoid direct contact with the dust.

### Airbag Remote Deployment Devices

| Tool Number / Name | Use |
|---|---|
| Deployment tool (0957A-34100A) | Deployment inside the vehicle (if the vehicle will no longer be driven) |
| DAB DEPLOYMENT ADAPTER HARNESS: | |
| DAB, BPT: 0957A-38500 | |
| PAB, SAB: 0957A-38100 | |

<!-- Figure: Deployment tool illustration, source: RT.pdf page 58 -->

### Disposal Plan

| CASE | DISPOSAL PLAN |
|---|---|
| Abnormal problems in airbag module | Deploy and discard |
| Car scrapping (DAB, PAB, SAB, BPT) | Deploy the airbag module with the SST |
| Crash (Deployed) | Discard |

### Airbag Module Disposal Procedures

Before disposing of a vehicle equipped with an airbag, or prior to disposing of the airbag module, be sure to first follow the procedures described below to deploy the airbag.

### Undeployed Airbag Module Disposal

> **CAUTION**
> 1. If the vehicle is to be scrapped, junked, or otherwise disposed of, deploy the airbag inside the vehicle.
> 2. Since there is a loud noise when the airbag is deployed, avoid residential areas whenever possible. If anyone is nearby, give warning of the deployment.
> 3. Since a large amount of smoke is produced when the airbag is deployed, select a well ventilated site. Moreover, never attempt the test near a fire or smoke sensor.

#### Deployment Inside the Vehicle

**When vehicle will no longer be driven:**

1. Open all windows and doors of the vehicle. Move the vehicle to an isolated spot.

2. Disconnect the negative (-) and positive (+) battery cables from the battery terminals, and then remove the battery from the vehicle.

> **CAUTION**
> Wait at least 30 seconds after disconnecting the battery cable before doing any further work.

3. Remove the center crash pad side cover.

4. Remove Airbag SRSCM connector.

5. Connect deployment tool to the connector of each module.

<!-- Figure: Deployment tool connected to SRSCM connector area, source: RT.pdf page 59 -->

6. At location as far away from the vehicle as possible, press the push button (removed from the vehicle) to deploy the airbag.

> **CAUTION**
> 1. Before deploying the airbag in this manner, first check to be sure that there is no one in or near the vehicle. Wear safety glasses.
> 2. The inflator will be quite hot immediately following the deployment, so wait at least 30 minutes to allow it to cool before attempting to handle it. Although not poisonous, do not inhale gas from airbag deployment. (For deployed Airbag Module Disposal Procedures see below.)
> 3. If the airbag fails to deploy after the procedure above are followed, do not go near the module. Contact your local distributor.

### Deployed Airbag Module Disposal Procedures

After deployment, the airbag module should be disposed of in the same manner as any other scrap part, except that the following points should be carefully noted during disposal:

1. The inflator will be quite hot immediately following deployment, so wait at least 30 minutes to allow it to cool before attempting to handle it.

2. Do not put water or oil on the airbag after deployment.

3. There may be adhered to the deployed airbag module, material that could irritate the eyes and/or skin, so wear gloves and safety glasses when handling a deployed airbag module. If despite these precautions, the material contacts your eyes or skin, immediately rinse the affected area with a large amount of clean water. If any irritation develops, seek medical attention.

4. Tightly seal the airbag module in a strong vinyl bag for disposal.

<!-- Figure: Deployed airbag module sealed in vinyl bag, source: RT.pdf page 60 -->

5. Be sure to always wash your hands after completing this operation.
