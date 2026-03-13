---
source: HA.pdf
chapter: HA
title: Air Conditioning Part 2
section: Heater, Blower Controls, Blower and A/C Controls
pages: 37-61
vehicle: 2003 Hyundai Tiburon (GK)
---

# Heater

## Heater Unit

### Components

<!-- Figure: Heater unit exploded view, source: HA.pdf page 37 -->

1. Heater core
2. Heater/A evaporator case
3. Seal
4. Floor cover
5. Vent cover
6. Evaporator core
7. Bracket
8. Clip
9. Joint flange cap
10. Vent duct
11. Blower door
12. Defroster door
13. Blend door
14. Thermistor
15. Insulator
16. In-car air temp sensor
17. Stopper
18. Heater/A evaporator case
19. Floor door lever
20. Vent door lever
21. Mode joint lever
22. Defroster door lever
23. Temp. door arm
24. Temp. door lever
25. Temp. door lever
26. Mode actuator motor
27. Temp. actuator motor

### Removal

<!-- Figure: Heater hose and drain hose removal, source: HA.pdf page 38 -->

1. Disconnect the negative (-) battery terminal.
2. Drain the cooling water of the radiator.
3. Remove the heater hose and the drain hose.
4. Drain the refrigerant.
5. Disconnect the air conditioning suction hose and the liquid tube.
6. Remove the driver's seat and the passenger's seat.
7. Remove the cowl side trim and the front pillar trim.
8. Remove the air bag module.
9. Remove the steering wheel.
10. Remove the steering lower and upper shroud.
11. Remove the multi-function switch.

<!-- Figure: Driver side crash pad removal, source: HA.pdf page 39 -->

12. Remove the crash pad under cover for the driver side.
13. Remove the cluster housing.
14. Remove the cluster.
15. After removing the center facia panel, disconnect the connectors.
16. Remove the audio.
17. Remove the floor console upper cover.
18. Remove the floor console.
19. Remove the glove box.
20. Remove the glove box lamp connector and the lamp.

<!-- Figure: Main crash pad removal, source: HA.pdf page 40 -->

21. Remove the main crash pad mounting bolt.
22. Remove the main crash pad.
23. Remove the heater unit mounting nut.
24. Remove the heater unit.

### Installation

Installation is the reverse of the removal.

<!-- Figure: Installation overview, source: HA.pdf page 40 -->

---

## Blower Controls

### Sensor Checking

#### Thermistor and Pin Sensor

The thermistor and pin sensor will detect the core temperature, and internal air temperature, and command the compressor relay power to prevent the evaporator core from freezing. The thermistor and pin sensor will use the thermal negative characteristic.

#### 1. Thermistor (Manual)

1. Remove the glove box.
2. Start the engine.
3. Turn on the air conditioner.
4. Using the multimeter, check the output voltage at terminals 2 and 3 of the thermistor.

| Thermistor | Operating Temperature | Output Voltage |
|---|---|---|
| ON | 0.5 +/- 0.5 deg C | 12V |
| OFF | 2.5 +/- 0.5 deg C | 0V |

#### 2. Pin Sensor (Automatic)

This is the same method as the thermistor to check the pin sensor.

**Pin sensor temperature-resistance-output voltage characteristics:**

| Temp (deg C) | Resistance (k-ohm) | Output (V) | Temp (deg C) | Resistance (k-ohm) | Output (V) |
|---|---|---|---|---|---|
| -5 | 14.53 | 3.88 | 15 | 5.18 | 1.9 |
| -2 | 12.42 | 3.04 | 20 | 4.91 | 1.9 |
| 0 | 11.36 | 2.83 | 25 | 4.03 | 1.67 |
| 2 | 10.4 | 2.83 | 30 | 3.34 | 1.47 |
| 5 | 9.12 | 2.66 | 35 | 2.78 | 1.29 |
| 10 | 7.28 | 2.4 | 40 | 2.26 | 1.11 |

<!-- Figure: Pin sensor temperature-resistance curve graph, source: HA.pdf page 41 -->

#### Water Temperature Sensor

1. The water temperature sensor, located at the heater core, detects coolant temperature flowing through heater core. It is a negative type thermistor; resistance will increase with lower temperatures, and decrease with higher temperatures.
2. The sensor will compare temperature settings with the IN-CAR air temperature or the ambient air temperature for motive heating control.

**CHECK:**

| Water temperature | Resistance |
|---|---|
| 25 deg C | 10 k-ohm |
| - | 2.0 k-ohm |

3. Electronic heating control:
   - At AUTO mode, discharge mode FLOOR or B/L, if coolant temperature is low, it will perform motive heating control to prevent cold air discharge toward the occupant.
   - Operation control:
     - Discharge mode FLOOR or B/L at AUTO control
     - Coolant temperature is low
   - Main condition:
     - Mode lever: DEF->MIX->AUTO
     - Blower level: AUTO LO->AUTO HI
     - Intake door: Ambient temperature

---

## Blower Unit

### Components

<!-- Figure: Blower unit exploded view, source: HA.pdf page 42 -->

- Inlet duct seal
- Air inlet duct case
- Inlet actuator motor
- Inlet door
- Blower upper case
- Blower seal
- Air filter
- Blower lower case
- Filter cover
- Resistor
- Hi-blower relay
- Power T/R
- Blower motor & wheel assembly
- Blower motor cooling tube

### Removal

1. Remove the main crash pad.
2. Disconnect the register and the blower motor connector.
3. Loosen the blower mounting nuts.
4. Remove the blower assembly.

### Installation

Installation is the reverse of removal.

### Disassembly

1. Disconnect the motor cooling tube.
2. Loosen the motor mounting screw.
3. Loosen the screw of the duct and the blower case.
4. Remove the duct.
5. Disconnect the case.
6. Remove the blower register.

### Reassembly

Reassembly is the reverse of removal.

### Air Filter Replacement

1. Remove the fixing pin of the glove box.
2. Remove the cover mounting bracket in the glove box.
3. Remove the filter cover.
4. Replace the filter.
5. Installation is the reverse of removal.

<!-- Figure: Blower unit removal and air filter replacement, source: HA.pdf page 43 -->

---

## Blower Motor

### Fresh Air Recirculation Switching Actuator

The intake selection switch is located on the control panel. Pressing the switch will shift between recirculation and fresh air modes.

<!-- Figure: Fresh air recirculation actuator location, source: HA.pdf page 44 -->

**CHECK:**

| Input | Output |
|---|---|
| 1 | 2 | Fresh/recirculation shifting |
| + | - | Recirculation |
| - | + | Fresh |

### Blower Motor Checking (Manual)

Connect the battery voltage and check the blower motor rotation.

### Blower Motor Checking (Automatic)

Connect battery voltage and check blower motor rotation.

#### Power T/R Checking

Operate the blower switch as AUTO->LOW->HIGH->AUTO, and measure voltage between pins 1 and 2.

**CHECK:**

| Fan | Motor Voltage |
|---|---|
| First speed | 3.8V |
| Second speed | 5.2V |
| Third speed | 6.7V |
| Fourth speed | 8.1V |
| Fifth speed | 9.5V |
| Sixth speed | 10.6V |
| Seventh speed | 13.5V |

<!-- Figure: Blower motor checking setup, source: HA.pdf page 44 -->

---

## Blower and A/C Controls (Manual)

### Schematic Diagram (Manual)

#### Schematic Diagram (Manual) (1)

<!-- Figure: Manual A/C schematic diagram sheet 1 - shows fuse connections, control module, blower motor relay, blower resistor, blower motor, and related wiring, source: HA.pdf page 45 -->

Key circuit elements:
- HOT AT ALL TIMES: Fuse 14 (40A)
- Fuse 21
- Blower relay
- Control module connections
- Blower resistor
- Blower motor
- Power T/R connector

#### Schematic Diagram (Manual) (2)

<!-- Figure: Manual A/C schematic diagram sheet 2 - shows gas temperature sensor, rear window and console mirror defogger, A/C control switch circuits, temperature actuator and blend door actuator, source: HA.pdf page 46 -->

Key circuit elements:
- HOT AT ALL TIMES fuse connections
- Gas temperature sensor
- Rear window & console mirror defogger switch
- A/C "OFF" switch
- Tailgate "ON/OFF" switch
- Discharge "COOL" switch
- Mode control switches (FAN, COOL, FR-OD, VCU, FLR, DEF, PWR, VENT)
- Temperature actuator
- Blend door actuator

#### Schematic Diagram (Manual) (3)

<!-- Figure: Manual A/C schematic diagram sheet 3 - shows A/C compressor relay, thermostatic switch, dual pressure switch, A/C relay, condenser fan motor circuits, source: HA.pdf page 47 -->

Key circuit elements:
- Front Fuse #1, #2
- Gas temperature sensor connections
- Thermostatic switch
- A/C relay
- Dual pressure switch
- Condenser fan motor relay
- A/C compressor clutch
- A/C signal / A/C output connector

---

## Schematic Diagram (Automatic)

### Schematic Diagram (Automatic) (1)

<!-- Figure: Automatic A/C schematic diagram sheet 1 - shows fuse/relay connections, power transistor, blower motor, FATC module, source: HA.pdf page 48 -->

Key circuit elements:
- HOT AT ALL TIMES fuse connections
- Condenser fan relay
- Hi-blower relay
- Power transistor
- Blower motor
- FATC (Full Automatic Temperature Control) module
- To A/C relay connections

### Schematic Diagram (Automatic) (2)

<!-- Figure: Automatic A/C schematic diagram sheet 2 - shows intake actuator, mode control circuits, rear defogger, sunlight sensor, A/C auto control module, source: HA.pdf page 49 -->

Key circuit elements:
- Fuse connections
- Gas temperature sensor
- Intake actuator connections
- Mode actuator connections (Defrost, Floor, Vent)
- Photo sensor connector
- A/C auto control module
- Rear window & console mirror defogger
- Sun sensor (PHOTO sensor)

### Schematic Diagram (Automatic) (3)

<!-- Figure: Automatic A/C schematic diagram sheet 3 - shows humidity input, temperature actuator, blend door actuator, illumination, triple switch, source: HA.pdf page 50 -->

Key circuit elements:
- Temperature actuator (TEMP)
- Blend door actuator
- Humidity input
- Mode actuator signals (M/M-1 through M/M-4)
- Illumination connections
- To triple switch
- Seat illuminations

### Schematic Diagram (Automatic) (4)

<!-- Figure: Automatic A/C schematic diagram sheet 4 - shows A/C compressor, dual pressure switch, triple switch, condenser fan circuits, source: HA.pdf page 51 -->

Key circuit elements:
- Front Fuse #1, #2
- A/C relay
- Dual pressure switch
- Triple switch
- Condenser fan relay
- A/C compressor

---

## Control Panel

<!-- Figure: Control panel layout (standard), source: HA.pdf page 52 -->
<!-- Figure: Control panel layout (equipped with AQS), source: HA.pdf page 52 -->

Controls shown: TEMP, MODE, A/C, AUTO, OFF, A/QS (on AQS-equipped models)

### Control Unit Pin Configuration (Automatic)

<!-- Figure: Control unit connector pinout diagram with connectors A and B, source: HA.pdf page 53 -->

**Connector A:**

| Pin No. | Name | Remarks |
|---|---|---|
| 1 | ILLUMINATION (+) | - |
| 2 | ILLUMINATION (+) | - |
| 3 | MEMORY POWER | - |
| 4 | POWER TR (BASE) | - |
| 5 | BLOWER FEED BACK | - |
| 6 | GROUND | - |
| 7 | HUMIDITY | - |
| 8 | - | COOL |
| 9 | TEMPERATURE ACTUATOR | COOL |
| 10 | INTAKE ACTUATOR | FRESH |
| 11 | DEFOGGER SWITCH | - |
| 12 | HOT AT ON | - |
| 13 | GROUND | - |
| 14 | MODE ACTUATOR | VENT |
| 15 | MODE ACTUATOR | DEF |
| 16 | - | - |
| 17 | A/CON OUTPUT | - |
| 18 | HIGH BLOWER RELAY CONTROL | - |
| 19 | PHOTO SENSOR (+) | - |
| 20 | PHOTO SENSOR (-) | - |
| 21 | DEFOGGER SWITCH | - |

**Connector A (continued):**

| Pin No. | Name | Remarks |
|---|---|---|
| 22 | TEMPERATURE ACTUATOR | WARM |
| 23 | INTAKE ACTUATOR | REC |
| 24 | AQS SENSOR SIGNAL | - |
| 25 | ON INPUT | - |
| 26 | GROUND | - |

**Connector B:**

| Pin No. | Name | Remarks |
|---|---|---|
| 1 | INCAR SENSOR INPUT | - |
| 2 | A/CON SELECT | - |
| 3 | AMBIENT SENSOR | - |
| 4 | EVAPORATOR TEMPERATURE SENSOR SIGNAL | - |
| 5 | - | - |
| 6 | - | - |
| 7 | POWER (5V) | - |
| 8 | INCAR SENSOR | - |
| 9 | - | - |
| 10 | TEMPERATURE FEEDBACK SIGNAL | - |
| 11 | MODE FEEDBACK SIGNAL | - |
| 12 | - | - |
| 13 | - | - |
| 14 | - | - |
| 15 | - | - |
| 16 | SENSOR GROUND | - |

---

## Blower and A/C Controls (Automatic)

### Button Control and Operation Logic

All buttons should be back-up.

#### 1. TEMP (Temperature UP/DOWN)

- **Button:** TEMP (Set temperature / Display)
- **Display:** Set temperature display

**System Operation:**

1. Control the discharge air temperature by adjusting the set temperature.
2. Whenever you press the SWITCH, temperature is changed to 0.5 deg C higher or lower. (Click tone: the operation sound is made at 0.1 sec.)
3. Set 17 deg C (63 deg F) as MAX COOL, 32 deg C (90 deg F) as MAX HOT.
4. When the switch is turned ON from OFF, the set temperature is displayed as the same before OFF.
5. When changing the set temperature from 17.5 deg C to 17 deg C or from 31.5 deg C to 32 deg C, the operation sound is made 3 times at an interval of 0.15 sec.
6. If it is above 32 deg C or below 17 deg C, the operation sound is made 5 times at an interval of 0.15 sec.
7. When pushing the TEMP button several times, the set temperature is shifted to another step at an interval of 0.3 sec. When engaging the button continuously (keep pushing), only the first shift takes 0.7 sec, but the rest shifts take 0.3 sec.

**OFF SW AND SYSTEM OPERATION:**
- OFF: SYSTEM OFF
- TEMP: SET TEMPERATURE UP/DOWN

#### 2. AUTO

- **Button:** AUTO ("AUTO" Display)

**System Operation:**

1. Automatically control the following items corresponding to the set temperature:
   - DISCHARGE TEMPERATURE
   - MODE DOOR
   - INTAKE DOOR
   - BLOWER FAN SPEED
   - A/C
2. When the AUTO mode is off, the word AUTO should not come up.
3. After the AUTO mode, the system is automatically returned to the previously selected SW.

**OFF SW AND SYSTEM OPERATION:**
- FAN UP/DOWN: BLOWER FAN SPEED MANUAL CONTROL
- MODE: DISCHARGE MODE MANUAL CONTROL
- A/C: A/C ON/OFF MANUAL CONTROL
- FIRE: FIRE MODE MANUAL CONTROL
- REC: REC MODE MANUAL CONTROL
- DEF: DEF MODE MANUAL CONTROL, A/C ON, FIRE

#### 3. AMB (Ambient Temperature Display)

- **Button:** AMB (Temperature display, The other display)

**System Operation:**

1. System is operated as the same before the AMB SW turned on.
2. If the AMB S/W is pushed, the other signals are not appeared but the word AMB and the ambient temperature are displayed for 5 sec, and then the display becomes the same as the AMB S/W is not pushed.

**OFF SW AND SYSTEM OPERATION:**
- AMB: If the AMB S/W is pushed once more when the ambient temperature is displayed, the ambient temperature is not appeared and the display becomes the same as the AMB S/W is not pushed.
- OTHER SWITCHES: If the other switch is pushed except for HEAT/DEF and in-car & ambient AQS, ambient temperature display is stopped and the pushed SW is activated.

#### 4. A/C (A/C ON/OFF Control)

- **Button:** A/C ("A/C" Disp. / "AUTO" Display)

**System Operation:**
- A/C ON/OFF

**OFF SW AND SYSTEM OPERATION:**
- A/C: A/C ON/OFF MANUAL CONTROL
- OFF: SYSTEM OFF
- AUTO: AUTO MODE AUTOMATIC CONTROL

#### 5. MODE

- **Button:** MODE (MODE DOOR: VENT / B/L / FLOOR / FIRE / DEF, FOCI Display)

**System Operation:**

1. Fix the MODE DOOR to one among VENT, B/L, FLOOR and MIX.
   - MODE OPERATION CONTROL ORDER: VENT -> B/L -> FLOOR -> MIX -> VENT
   - A MIX MODE: MIX FLOOR+MIX FIRE, A/C ON
   - DEF: DEF SPEED MANUAL CONTROL
   - MODE: VENT, B/L, FLOOR & MIX (repeat the order)
   - AUTO: AUTO MODE AUTOMATIC CONTROL

#### 6. DEF (Defroster Mode)

- **Button:** DEF ("DEF" / ON Display)

**System Operation:**

1. MODE DOOR: Fix to "DEF"
2. INTAKE DOOR: Fix to "FRE" (REC can be selected)
3. A/C: ON
4. A/C OUTPUT ON/OFF control: Corresponding to the detected temperature by EVAP SENSOR.
   - A/C output should be cut off at 3.5 deg C or below (ambient temperature).
   - (DISPLAY OFF, A/C SELECT SIGNAL OFF)
5. DEF is prior to "MAX HOT/COOL" function.
6. DEF is prior to "MAX MODE" control.

**OFF SW AND SYSTEM OPERATION:**
- AUTO: ALL SYSTEM AUTOMATIC CONTROL
- MODE: DISCHARGE MODE MANUAL CONTROL (DEF function off)
- A/C: A/C ON/OFF MANUAL CONTROL
- DEF: Return to the mode before the DEF S/W selection

#### 7. OFF

- **Button:** SYSTEM OFF (LCD ON)

**System Operation:**

1. BLOWER FAN SPEED OFF
2. A/C OFF
3. INTAKE DOOR: Fix to the mode before OFF
4. MODE DOOR: Fix to the mode before OFF
5. INTAKE CONTROL: Fix to the mode before OFF

- After "OFF", at REC, REC S/W ON (NON-AQS type):
  - Shift to FIRE MODE
  - REC INDICATOR ON
  - LCD OFF
  - OTHERS: OFF

- After "OFF", at FIRE, FIRE S/W ON (NON-AQS type):
  - Shift to FIRE MODE
  - REC INDICATOR ON
  - LCD OFF
  - OTHERS: OFF

- After "OFF", at AQS, AQS/REC S/W ON (AQS type):
  - Shift to REC MODE
  - AQS OFF
  - REC INDICATOR ON
  - LCD OFF
  - OTHERS: OFF

- After "OFF": AQS ON -> AQS LOGIC
- After "OFF": AMB S/W ON
  - OFF: The word "AMB" & ambient temperature display for 5 sec, and then off.

**OFF SW AND SYSTEM OPERATION:**
- AUTO: AUTO MODE AUTOMATIC CONTROL
- A/C:
  - BLOWER: SPEED: Return to MANUAL LOW
  - OTHERS: Return to the mode before OFF
- A/C:
  - A/C ON
  - OTHERS: Return to the mode before OFF
- MODE:
  - MODE: The mode before OFF
  - OTHERS: Return to the mode before OFF
- DEF:
  - MODE: DEF
  - A/C: ON
  - INTAKE: FIRE
  - OTHERS: Return to the mode before OFF
- TEMP:
  - TEMP: The mode before OFF
  - OTHERS: Return to the mode before OFF

#### 8. REC (Recirculation)

- **Button:** REC / IND ON ("AUTO" Display)

**System Operation:**

1. When operating the REC, S/W from FIRE MODE, to the INTAKE DOOR to REC MODE or when operating the REC S/W from REC MODE, fix to the FIRE MODE.

**OFF SW AND SYSTEM OPERATION:**
- REC: FIRE MODE MANUAL CONTROL
- OFF SW: ALL MODES (POSSIBLE TO OPERATE)
- AUTO: AUTOMATIC CONTROL (if or REC)

#### 9. FAN BLOWER (Fan Speed UP/DOWN)

**System Operation:**

1. BLOWER MOTOR & POWER: motor speed is switched by the current variation of the POWER TRANSISTOR.
2. At AUTO MODE, if FAN is operated UP/DOWN, the FAN SPEED is UP/DOWN on the basis of the present FAN LEVEL.
3. At OFF, if the other SW except for "FAN" is turned ON, the FAN SPEED is gradually increased from LOW to TARGET SPEED.
4. Fan speed level and voltage:
   - AUTO COOLER: No level (4.5V - Bv)
   - AUTO HEATER: No level (4.5V - Bv)
   - MANUAL FAN SPEED: 7th level (4.5V - Bv)
5. The first shift to another step takes 0.7 sec. If the button is continually engaged, the third shift takes 0.7 sec. And then the next ones take 0.3 sec per each.
6. At MANUAL, 7th level when the UP S/W is pushed or at MANUAL 1st level when the DOWN S/W is pushed, the operation sound is made 5 times at an interval of 0.15 sec.
7. When shifting 6 to 7 level, or 2 to 1 level, the operation sound is internally made each 0.15 sec.

**OFF SW AND SYSTEM OPERATION:**
- AUTO: AUTO MODE AUTOMATIC CONTROL
- OFF: SYSTEM OFF
- FAN UP/DOWN: BLOWER FAN SPEED MANUAL CONTROL

#### 10. DEFOG (Rear Glass Defogger)

**System Operation:**

1. If the DEFOG SW is pushed, the rear glass defogger operation signal is output to the ETACS and the ETACS turns the DEFOG IND on by the FATC indication.
2. While operating the rear glass defogger, if DEF DEFOG SW is pushed again, ETACS turns off the rear glass defogger and turns the DEFOG IND off.
3. After operating the rear glass defogger for 15 minutes by ETACS, DEFOG function is automatically off.

**OFF SW AND SYSTEM OPERATION:**
- DEFOG: Push the second DEFOG SW, DEFOG function is off.

---

### System Control Features

#### Signal I/O for Each Control Feature

| Control Item | Input | Output | Remarks |
|---|---|---|---|
| Required discharge temperature | Auto SW, A/C SW, TEMP SW, INCAR sensor, AMB sensor, Photo sensor, Water temperature sensor, thermo sensor, TEMP actuator. | TEMP actuator | - |
| Mode control | AUTO SW, MODE SW, TEMP SW, DEF SW, Blower SW, OFF SW, INCAR sensor, AMB sensor, Photo sensor, Water temperature sensor, thermo sensor, Power TR. | Blower motor, Power TR, Hi-blower relay | Blower Switch Manual selection: Control in priority |
| Mode door control | AUTO SW, MODE SW, DEF SW, DEF SW, Blower SW, OFF SW, TEMP SW, INCAR sensor, AMB sensor, Photo sensor. | Mode actuator | - |
| Intake control | AUTO SW, A/C SW, DEF SW, TEMP SW, OFF SW, Intake SW, INCAR sensor, AMB sensor, Photo sensor, Power TR. | Mode actuator | - |
| Compressor control | AUTO SW, A/C SW, DEF SW, TEMP SW, OFF SW, INCAR sensor, AMB sensor, Photo sensor. | Compressor relay | - |

> **Note:** During MIX mode, the A/C may operate during DEF or MIX mode. In order to enable dehumidification, the driver may select A/C OFF during the A/C on period.

---

### Control Specification

| Control Item | Control Features | Remarks |
|---|---|---|
| Required discharge temperature | Required temperature determined by the set temperature and the injected sensor value. | - |
| Auto control | Required discharge temperature is determined by the set temperature and the injected sensor value. The feature will use the required discharge temperature to perform the auto control of temp. actuator, mode actuator, intake actuator, blower mode and compressor control. | - |
| IN-CAR temperature correction | Upon detecting rapid changes of temperature from the INCAR sensor, it will gradually correct the incar temperature value. | +1 deg C UP/4sec delay, -1 deg C DOWN/4sec delay |
| AMB temperature correction | Upon detecting rapid changes of temperature from the AMB sensor, it will gradually correct the ambient temperature value. | +1 deg C UP/3min delay, -1 deg C DOWN/4sec delay |
| Photo correction | Upon detecting rapid changes of photo intensity from the PHOTO sensor, it will gradually correct the photo intensity value. | 350->1000W/m2/1min delay, 350->1000W/m2/3min delay |
| TEMP door control | It does the automatic control to maintain the optimum TEMP door opening (0%~100%). It will be computed by the set temperature set and the input signal from each sensor. | The set temperature range: 17 deg C~32 deg C, 0.5 deg C step (63 deg F~90 deg F, 1 deg F step) |

---

| Control Item | Control Features | Remarks |
|---|---|---|
| Blower speed | Automatic control of the blower speed. The target value will be computed by the set temperature and the input signal from each sensor. (7 levels may be selected in case of manual selection.) | Auto mode blower low voltage (Manual low voltage: 3.8), Auto mode heater blower HI speed: 10.6V |
| Electro-motive mode control | During auto control, it will raise the permitted voltage of blower motor gradually in order to improve comfortability. | 6 seconds for shifting LO->MAX HI |
| Photo compensation | During auto control, it will compensate the blower level and the discharge temperature according to the photo intensity detected from the PHOTO sensor at VENT or B/L mode. PHOTO compensation will begin after 5 seconds when ignition on. | - |
| Mode door control | Automatic control of air discharge based on the required discharge temperature. It will be computed by the temperature setting and the input signal from each sensor. In case of manual selection: (VENT->B/L->FLOOR->VENT) | At OFF in AUTO mode, MODE door will maintain the AUTO control condition. At OFF in manual mode, MODE door will maintain the manual control condition. |
| MIX mode control (in auto control) | If the ambient temperature is -17 deg C or less in AUTO mode, discharge mode will be controlled at MIX. (When front window glass is defogged.) | Entering MIX mode, A/C will operate. |
| INTAKE door control | Auto control of intake mode based on the required discharge temperature that will be computed by the temperature setting and the input signal from each sensor. | Shift to REC when selecting REC button at FRE condition (LED on). Shift to FRE when selecting FRE button at REC condition (LED off). |
| INTAKE control at OFF | The intake door will shift to the REC position when switching the system off in auto-condition, and maintain the previous condition at OFF at manual condition. | FRE/REC manual selection will be enabled at OFF. REC indicator will come on at OFF at AUTO mode. |
| Compressor auto control | Control automatically the compressor on/off state corresponding to the set temperature and the input signal from each sensor. | When selecting the AUTO SW, the compressor is controlled to ON/OFF. When selecting the DEF SW, the compressor is controlled to "ON". |
| Compressor clutch on/off control based on refrigerant temperature | If EVAP sensor temperature is below than 0.5 deg C, the compressor will be ON and the temperature is 3 deg C or higher, with the compressor OFF. | - |
| MAX HOT | When selecting the set temperature 32 deg C at AUTO mode, MAX HOT will be performed. It will prevail over MIX mode control. | TEMP door: MAX HOT, MODE door: FLOOR mode, INTAKE door: FRE mode, Compressor: OFF, Blower speed: AUTO HI (10.6V) |
| MAX COOL | When selecting the set temperature 17 deg C at AUTO mode, MAX COOL will be performed. | TEMP door: MAX COOL, MODE door: FLOOR mode, INTAKE door: REC mode, Compressor: On, Blower speed: MAX HI |

---

| Control Item | Control Features | Remarks |
|---|---|---|
| Electromotive heating control | If the air temperature > the in-car temperature by 3 deg C at B/L or FLOOR in AUTO mode, and the water temperature sensor input is 58 deg C or less, it will affect the electromotive heating control to prevent outside cold air from flowing toward the feet of passengers. As the coolant temperature rises, the MODE door will shift to DEF->MIX->AUTO. MODE: Manual selection is enabled. INTAKE door: At AUTO control or manual selection mode. Blower speed: Manual selection is enabled (No re-entry). | Operation release: 10 minutes after ignition on/in case of temperature mode selection fast B/L, it will apply the blower speed auto function. After pressing blower switch when water temperature sensor selection is 58 deg C or higher. In pressing MODE switch, in Upper DREG pressing DEF switch. |
| Cooling control (A/C on mode) | In order to prevent hot air from the VENT or B/L in AUTO cooling control (A/C on mode), the blower speed will be operated at LOW for approx. 3 seconds before entering the AUTO control. If the EVAP sensor detects a temperature 58 deg C or less, blower will operate at any time. | - |
| MAX HOT | If the above condition is satisfied, electromotive cooling control will operate at any time. | When the initial battery connection and ignition is ON, it will operate at AUTO mode. (A/C will not operate.) |
| Air Quality Sensor System (AQS) | The AQS system will detect the hazardous elements and odors contained in the air. If the harmful element concentration is higher than standard, the system will output a LOW signal (0V) to the FATC. If the concentration is within the standard value, the system will output a HI signal (5V) to the FATC. Corresponding to the signal from the AQS, it will control the INTAKE door as follows to prevent the inflow of harmful gas in FATC. | When IGN 2 ON, the AQS assembly will be started during the preheating. AQS will output 0V (signal) during preheating. IGN2 ON, it will check circuit break on the AQS assembly's signal line for approx. 7 seconds during the preheating, irrespective of the AQS switch condition. |

**AQS Intake Door Control:**

| Condition | INTAKE Door Position |
|---|---|
| LOW | REC |
| HI | FRE |

---

| Control Item | Control Features | Remarks |
|---|---|---|
| Initialization Upon battery-on | When supplying the initial power, it will operate in the initial condition. | When the initial ignition ON after battery connection, the system will operate at the set temperature 25 deg C and at AUTO mode. |
| Memory | When removing ignition key, it will store FATC's operating condition. | When IGN ON after IGN OFF during FATC operation, the system will operate at the previous before the ignition off. |
