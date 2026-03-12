# AIM PDM ECU Stream — Haltech CAN_V2_40 Channel Reference

**Protocol:** HALTECH - CAN_V2_40 (ver. 02.00.03) 1 Mbit/sec
**Available:** 267 channels · **Max enabled:** 120 · **Currently enabled:** 79 (confirmed)
**CAN Bus 120Ω Resistor:** ✅ Enabled · **Silent on CAN Bus:** ☐ Disabled

> ✅ = currently enabled in `Webinar_complete_02` config

---

## Enabled Channels Summary (79 active)

| CC ID | Name | Function | Unit | Freq | Purpose |
|---|---|---|---|---|---|
| CC01 | ECU RPM | Engine RPM | rpm | 10 Hz | ENGINE_RUNNING, starter interlock, alarm guards |
| CC02 | ECU ManifPress | Pressure | bar 0.001 | 10 Hz | MAP logging |
| CC03 | ECU CoolantPres | Pressure | bar 0.001 | 10 Hz | Coolant pressure (AVI5 Lowdoller) |
| CC04 | ECU ThrottlePos | Percent Throttle Load | % 0.01 | 10 Hz | PITLIMITER TPS override |
| CC05 | ECU OilPress | Oil Pressure | bar 0.01 | 10 Hz | LOW_OIL_P alarm |
| CC06 | ECU FuelPress | Fuel Press | bar 0.001 | 10 Hz | LOW_FUEL_P alarm |
| CC08 | ECU EngineDeman | Percent | % 0.01 | 10 Hz | Engine load |
| CC09 | ECU IgnAngLead | Angle | deg 0.1 | 10 Hz | Ignition advance |
| CC10 | ECU InjDT2 | Percent | % 0.01 | 10 Hz | Injector duty bank 2 |
| CC11 | ECU InjDT1 | Percent | % 0.01 | 10 Hz | Injector duty bank 1 |
| CC15 | ECU Avg Inj 1 | Injection Advance Time | ms | 10 Hz | Injection pulse width |
| CC16 | ECU Avg Inj 2 | Injection Advance Time | ms | 10 Hz | Injection pulse width |
| CC17 | ECU Avg inj 3 | Injection Advance Time | ms | 10 Hz | Injection pulse width |
| CC23 | ECU TrigSyncLev | Number | # | 10 Hz | Trigger sync health |
| CC24 | ECU TrigErrCount | Number | # | 10 Hz | Trigger error count |
| CC25 | ECU TrigCount | Number | # | 10 Hz | Trigger count |
| CC26 | ECU KnockLev2 | Number | # | 10 Hz | Knock level bank 2 |
| CC27 | ECU KnockLev1 | Number | # | 10 Hz | Knock level bank 1 |
| CC28 | ECU LateralG | Lateral Acceleration | g 0.01 | 10 Hz | IMU lateral |
| CC36 | ECU ExhCamAng1 | Angle | deg 0.1 | 10 Hz | Exhaust cam angle bank 1 (VVT) |
| CC37 | ECU ExhCamAng2 | Angle | deg 0.1 | 10 Hz | Exhaust cam angle bank 2 (VVT) |
| CC38 | ECU LongG | Inline Acceleration | g 0.01 | 10 Hz | IMU longitudinal |
| CC41 | ECU EngLimitAct | Numeric Status | # | 10 Hz | Rev limiter active flag |
| CC45 | ECU VehSpeed | Vehicle Speed | km/h | 10 Hz | PITLIMITER speed gate (97 km/h = 60 mph) |
| CC46 | ECU IntakeCamA1 | Angle | deg 0.1 | 10 Hz | Intake cam angle bank 1 (VVT) |
| CC47 | ECU IntakeCamA2 | Angle | deg 0.1 | 10 Hz | Intake cam angle bank 2 (VVT) |
| CC50 | ECU BaromPress | Pressure | bar 0.001 | 10 Hz | Barometric pressure |
| CC52 | ECU BatteryVolt | Battery Voltage | V 0.1 | 10 Hz | Battery health |
| CC65 | ECU Amb Air T | Temperature | C 0.1 | 10 Hz | Ambient air temp |
| CC66 | ECU Rel Humidity | Percent | % 0.01 | 10 Hz | Relative humidity |
| CC67 | ECU Abs Humidity | Number | # | 10 Hz | Absolute humidity |
| CC68 | ECU Spec Humi | Number | # | 10 Hz | Specific humidity |
| CC69 | ECU CoolantTemp | Water Temperature | F 0.1 | 5 Hz | Fan bands + HIGH_COOLANT_T alarm |
| CC70 | ECU AirTemp | Air Temperature | C 0.1 | 5 Hz | IAT (°C) |
| CC71 | ECU OilTemp | Oil Temperature | C 0.1 | 5 Hz | HIGH_OIL_T alarm |
| CC72 | ECU FuelTemp | Temperature | C 0.1 | 5 Hz | Fuel temperature |
| CC73 | ECU DiffOilTemp | Temperature | C 0.1 | 5 Hz | Diff/transaxle oil temp |
| CC74 | ECU GearOilTemp | Temperature | C 0.1 | 5 Hz | Gearbox oil temp |
| CC76 | ECU FuelLevel | Fuel Level | l 0.1 | 5 Hz | Fuel level display |
| CC77 | ECU FuelTrimSTB1 | Percent | % 0.01 | 5 Hz | Short-term fuel trim bank 1 |
| CC78 | ECU FuelTrimSTB2 | Percent | % 0.01 | 5 Hz | Short-term fuel trim bank 2 |
| CC79 | ECU FuelTrimLTB1 | Percent | % 0.01 | 5 Hz | Long-term fuel trim bank 1 |
| CC80 | ECU FuelTrimLTB2 | Percent | % 0.01 | 5 Hz | Long-term fuel trim bank 2 |
| CC91 | ECU CheckEngLtSw | Number | # | 10 Hz | Check engine light status |
| CC94 | ECU Oil Press Li | Number | # | 10 Hz | ECU oil pressure warning flag |
| CC103 | ECU BrakePedSw | Number | # | 10 Hz | Brake pedal switch |
| CC104 | ECU BatteryLtSw | Number | # | 10 Hz | Battery light switch |
| CC107 | ECU TPSAct | Numeric Status | # | 10 Hz | TPS active status |
| CC116 | ECU IgnitionSw | Number | # | 10 Hz | Ignition switch state |
| CC117 | PitLane SpLimErr | Number | # | 10 Hz | Pit lane speed limiter error |
| CC118 | PitLane SpdLimAc | Number | # | 10 Hz | Pit lane speed limiter active |
| CC119 | PitLane SpdLimSS | Number | # | 10 Hz | Pit lane set speed reference |
| CC134 | ECU TargLambda | Lambda | lambda 0.01 | 10 Hz | Target lambda |
| CC138 | ECU CrankCPress | Pressure | bar 0.001 | 10 Hz | Crankcase pressure |
| CC141 | ECU InjectionDT4 | Percent | % 0.01 | 10 Hz | Injector duty cycle 4 |
| CC142 | ECU IgnitionAng1 | Angle | deg 0.1 | 10 Hz | Ignition angle cyl 1 — per-cylinder knock retard visibility |
| CC143 | ECU IgnitionAng2 | Angle | deg 0.1 | 10 Hz | Ignition angle cyl 2 — per-cylinder knock retard visibility |
| CC144 | ECU RaceTimer | Time | ms | 10 Hz | Session timing |
| CC149 | ECU TorqCIgnCorr | Angle | deg 0.1 | 10 Hz | Torque ignition correction |
| CC166 | ECU Temperature | Temperature | C 0.1 | 5 Hz | ECU internal temp |
| CC167 | ECU Gear Sel Pos | Gear | gear | 10 Hz | Gear display |
| CC168 | ECU WIDEBAND B2 | Lambda | lambda 0.01 | 10 Hz | Wideband AFR bank 2 |
| CC169 | ECU WIDEBAND OVE | Lambda | lambda 0.01 | 10 Hz | Wideband AFR average/overall |
| CC170 | ECU WIDEBAND B1 | Lambda | lambda 0.01 | 10 Hz | Wideband AFR bank 1 |
| CC172 | ECU Inj Pres D | Pressure | bar 0.001 | 10 Hz | Injector pressure delta |
| CC173 | ECU Acc Ped Pos | Percent | % 0.01 | 10 Hz | Accelerator pedal position |
| CC210 | ECU VERTICAL G | Vertical Acceleration | g 0.01 | 10 Hz | IMU vertical |
| CC211 | ECU PITCH RATE | Pitch Rate | deg/s 0.1 | 10 Hz | IMU pitch rate |
| CC212 | ECU ROLL RATE | Roll Rate | deg/s 0.1 | 10 Hz | IMU roll rate |
| CC213 | ECU YAW RATE | Yaw Rate | deg/s 0.1 | 10 Hz | IMU yaw rate |
| CC215 | ECU PRFUELPUMP | Percent | % 0.01 | 5 Hz | Primary fuel pump duty |
| CC220 | ECU PRESS DIFF | Pressure | bar 0.001 | 10 Hz | Pressure differential |
| CC227 | ECU ENG LIM MAX | Angular Velocity | deg/s 0.1 | 10 Hz | Rev limiter threshold |
| CC247 | EngProtectSevLvl | Number | # | 10 Hz | Engine protection severity |
| CC248 | EngProtectReason | Number | # | 10 Hz | Engine protection reason code |
| CC249 | ECU PLIGHT STATE | Number | # | 10 Hz | Engine protection / fault flag |
| CC254 | ECU FUEL TRIPMT | Fuel Level | l 0.1 | 5 Hz | Fuel used — endurance reference |
| CC255 | Trip Meter | Distance | m 0.01 | 10 Hz | Distance |
| CC261 | ECU AIR TEMP | Air Temperature | F 0.1 | 10 Hz | IAT (°F) |

---

## All Available Channels — Not Enabled

These 188 channels are available in the Haltech CAN_V2_40 protocol but not currently selected.
Enable any of these if needed (total enabled must remain ≤ 120).

### Engine / Fueling / Injection

| CC ID | Name | Function | Unit | Freq |
|---|---|---|---|---|
| CC18 | ECU Avg inj 4 | Injection Advance Time | ms | 10 Hz |
| CC40 | ECU LaunchFuEn | Percent | % 0.01 | 10 Hz |
| CC42 | ECU GenOut1DT | Percent | % 0.01 | 10 Hz |
| CC43 | ECU BoostCtrOut | Percent | % 0.01 | 10 Hz |
| CC48 | ECU FuelFlow | Fuel Flow | l/s | 10 Hz |
| CC49 | ECU FuReturn | Fuel Flow | l/s | 10 Hz |
| CC75 | ECU FuelCompos | Percent | % 0.01 | 5 Hz |
| CC140 | ECU InjectionDT3 | Percent | % 0.01 | 10 Hz |
| CC180 | ECU AXFUEL P3 | Number | # | 10 Hz |
| CC184 | ECU PRMFUEL OUT | Number | # | 10 Hz |
| CC185 | ECU AUXFUEL P1 | Number | # | 10 Hz |
| CC186 | ECU AXFUEL P2 | Number | # | 10 Hz |
| CC208 | ECU TOT FUEL USD | Fuel Level | l 0.1 | 10 Hz |
| CC214 | ECU AUX2FUELPUMP | Percent | % 0.01 | 5 Hz |
| CC216 | ECU AUX1FUEL PDC | Percent | % 0.01 | 5 Hz |
| CC217 | ECU AUX3FUELPUMP | Percent | % 0.01 | 5 Hz |
| CC260 | ECU H2O INJ DUTY | Percent | % 0.01 | 10 Hz |

### Ignition / Timing

| CC ID | Name | Function | Unit | Freq |
|---|---|---|---|---|
| CC14 | LaunchCtrlEndRPM | Number | # | 10 Hz |
| CC39 | ECU LaunchIgnRet | Angle | deg 0.1 | 10 Hz |
| CC147 | ECU TorDrRPMEI | Angle | deg 0.1 | 10 Hz |
| CC148 | ECU TorDrRPMIC | Angle | deg 0.1 | 10 Hz |

### Lambda / AFR

| CC ID | Name | Function | Unit | Freq |
|---|---|---|---|---|
| CC19 | ECU Lambda4 | Lambda | lambda 0.01 | 10 Hz |
| CC20 | ECU Lambda3 | Lambda | lambda 0.01 | 10 Hz |
| CC21 | ECU Lambda2 | Lambda | lambda 0.01 | 10 Hz |
| CC22 | ECU Lambda1 | Lambda | lambda 0.01 | 10 Hz |
| CC150 | ECU WIDEBAND S6 | Lambda | lambda 0.01 | 10 Hz |
| CC151 | ECU WIDEBAND S7 | Lambda | lambda 0.01 | 10 Hz |
| CC152 | ECU WIDEBAND S5 | Lambda | lambda 0.01 | 10 Hz |
| CC153 | ECU WIDEBAND S8 | Lambda | lambda 0.01 | 10 Hz |
| CC154 | ECU WIDEBAND S9 | Lambda | lambda 0.01 | 10 Hz |
| CC155 | ECU WIDEBAND S12 | Lambda | lambda 0.01 | 10 Hz |
| CC156 | ECU WIDEBAND S10 | Lambda | lambda 0.01 | 10 Hz |
| CC157 | ECU WIDEBAND S11 | Lambda | lambda 0.01 | 10 Hz |

### Speed / Gear / Driveline

| CC ID | Name | Function | Unit | Freq |
|---|---|---|---|---|
| CC12 | ECU WheelSlip | Speed Limiter | km/h 0.1 | 10 Hz |
| CC13 | ECU WheelDiff | Speed Limiter | km/h 0.1 | 10 Hz |
| CC29 | ECU TurboSpd1 | Angular Velocity | deg/s 0.1 | 10 Hz |
| CC32 | ECU WheelSpdFR | Wheel Speed | km/h | 10 Hz |
| CC33 | ECU WheelSpdRL | Wheel Speed | km/h | 10 Hz |
| CC34 | ECU WheelSpdRR | Wheel Speed | km/h | 10 Hz |
| CC35 | ECU WheelSpdFL | Wheel Speed | km/h | 10 Hz |
| CC44 | ECU Gear | Gear | gear | 10 Hz |
| CC112 | ECU DriveshaRPM | Angular Velocity | deg/s 0.1 | 10 Hz |
| CC120 | ECU TurboSpdS2 | Angular Velocity | deg/s 0.1 | 10 Hz |
| CC145 | ECU TorqDrvsRPMT | Angular Velocity | deg/s 0.1 | 10 Hz |
| CC146 | ECU TorqDrvsRPME | Angular Velocity | deg/s 0.1 | 10 Hz |
| CC171 | ECU Gear 2 | Gear | gear | 10 Hz |

### Pressure

| CC ID | Name | Function | Unit | Freq |
|---|---|---|---|---|
| CC07 | ECU WastegaPress | Pressure | bar 0.001 | 10 Hz |
| CC30 | ECU BrakePress | Brake Circuit Pressure | bar 0.1 | 10 Hz |
| CC31 | ECU NOSPressS1 | Pressure | bar 0.001 | 10 Hz |
| CC51 | ECU TargBoostLev | Pressure | bar 0.001 | 10 Hz |
| CC121 | ECU NOSPressS4 | Pressure | bar 0.001 | 10 Hz |
| CC122 | ECU NOSPressS3 | Pressure | bar 0.001 | 10 Hz |
| CC123 | ECU NOSPressS2 | Pressure | bar 0.001 | 10 Hz |
| CC139 | ECU GearbOilPres | Pressure | bar 0.001 | 10 Hz |
| CC174 | ExhManifPress | Exhaust Air Pressure | bar 0.001 | 10 Hz |
| CC218 | ECU BRAKE P FRON | Percent | % 0.01 | 10 Hz |
| CC219 | ECU BRAKE P REAR | Percent | % 0.01 | 10 Hz |
| CC221 | ECU BRAKEPRSREAR | Pressure | bar 0.001 | 10 Hz |
| CC229 | ECU FRONTLEFT PR | Pressure | bar 0.001 | 5 Hz |
| CC230 | ECU FRNT RGHT PR | Pressure | bar 0.001 | 5 Hz |
| CC231 | ECU LEFT REAR PR | Pressure | bar 0.001 | 5 Hz |
| CC232 | ECU RGHT REAR PR | Pressure | bar 0.001 | 5 Hz |
| CC241 | ECU FT RACC PRES | Pressure | psi 0.1 | 5 Hz |
| CC242 | ECU RT RACC PRES | Pressure | bar 0.001 | 5 Hz |

### Temperature

| CC ID | Name | Function | Unit | Freq |
|---|---|---|---|---|
| CC53 | ECU EGTSensor1 | Exhaust Temperature | C 0.1 | 10 Hz |
| CC54 | ECU EGTSensor2 | Exhaust Temperature | C 0.1 | 10 Hz |
| CC55 | ECU EGTSensor3 | Exhaust Temperature | C 0.1 | 10 Hz |
| CC56 | ECU EGTSensor4 | Exhaust Temperature | C 0.1 | 10 Hz |
| CC57 | ECU EGTSensor7 | Exhaust Temperature | C 0.1 | 10 Hz |
| CC58 | ECU EGTSensor5 | Exhaust Temperature | C 0.1 | 10 Hz |
| CC59 | ECU EGTSensor6 | Exhaust Temperature | C 0.1 | 10 Hz |
| CC60 | ECU EGTSensor8 | Exhaust Temperature | C 0.1 | 10 Hz |
| CC61 | ECU EGTSensor9 | Exhaust Temperature | C 0.1 | 10 Hz |
| CC62 | ECU EGTSensor10 | Exhaust Temperature | C 0.1 | 10 Hz |
| CC63 | ECU EGTSensor11 | Exhaust Temperature | C 0.1 | 10 Hz |
| CC64 | ECU EGTSensor12 | Exhaust Temperature | C 0.1 | 10 Hz |
| CC233 | ECU FRLEF TYR TM | Temperature | F 0.1 | 5 Hz |
| CC234 | ECU RERIGH TY TM | Temperature | C 0.1 | 5 Hz |
| CC235 | ECU REARLF TY TM | Temperature | C 0.1 | 5 Hz |
| CC236 | ECU FRRIGH TY TM | Temperature | C 0.1 | 5 Hz |

### Suspension / Shock

| CC ID | Name | Function | Unit | Freq |
|---|---|---|---|---|
| CC158 | Shock FL raw | Shock Position | mm | 10 Hz |
| CC159 | Shock FR raw | Shock Position | mm | 10 Hz |
| CC160 | Shock RL raw | Shock Position | mm | 10 Hz |
| CC161 | Shock RR raw | Shock Position | mm | 10 Hz |
| CC162 | ECU Shock RR | Shock Position | mm | 10 Hz |
| CC163 | ECU Shock RL | Shock Position | mm | 10 Hz |
| CC164 | ECU Shock FR | Shock Position | mm | 10 Hz |
| CC165 | ECU Shock FL | Shock Position | mm | 10 Hz |

### Timing / Session

| CC ID | Name | Function | Unit | Freq |
|---|---|---|---|---|
| CC114 | ECU TurboTimer | Time | ms | 10 Hz |
| CC115 | ECU TurbTimerEng | Time | ms | 10 Hz |
| CC144 | ECU RaceTimer | Time | ms | 10 Hz |

### Switches / Status / Limiters

| CC ID | Name | Function | Unit | Freq |
|---|---|---|---|---|
| CC92 | ECU Neutral SW | Number | # | 10 Hz |
| CC93 | ECU Reverse Sw | Number | # | 10 Hz |
| CC95 | ECU Laun Ctr Sw | Number | # | 10 Hz |
| CC96 | ECU TC Ctrl EN | Number | # | 10 Hz |
| CC97 | ECU LaunchCtrAct | Number | # | 10 Hz |
| CC98 | ECU AuxRPMLimSw | Number | # | 10 Hz |
| CC99 | ECU ClutchSw | Number | # | 10 Hz |
| CC100 | ECU TorqueRedAct | Number | # | 10 Hz |
| CC101 | ECU FlatShSw | Number | # | 10 Hz |
| CC102 | ECU TC Ctr Act | Number | # | 10 Hz |
| CC105 | ECU GearSwitch | Numeric Status | # | 10 Hz |
| CC106 | ECU DecelCutActi | Numeric Status | # | 10 Hz |
| CC109 | ECU ABS ERROR | Number | # | 10 Hz |
| CC110 | ECU ABS ACTIVE | Number | # | 10 Hz |
| CC111 | ECU ABS ARMED | Number | # | 10 Hz |
| CC135 | ECU Torque Man K | Number | # | 10 Hz |
| CC136 | NitroStOutSt | Numeric Status | # | 10 Hz |
| CC175 | ECU CRUI CTRL IN | Number | # | 10 Hz |
| CC176 | ECU Cru Last T S | Speed Limiter | km/h 0.1 | 10 Hz |
| CC177 | ECU Cruise Trg S | Speed Limiter | km/h 0.1 | 10 Hz |
| CC178 | ECU Crui Spd Err | Speed Limiter | km/h 0.1 | 10 Hz |
| CC179 | ECU Cruise Ctr S | Number | # | 10 Hz |
| CC181 | ECU ANTISWITCHST | Number | # | 10 Hz |
| CC182 | ECU ANTILAG O ST | Number | # | 10 Hz |
| CC183 | ECU TCTRL SWITCH | Number | # | 10 Hz |
| CC209 | ECU ROLLANTISWIC | Number | # | 10 Hz |
| CC222 | ECU CUT PERC | Percent | % 0.01 | 10 Hz |
| CC223 | ECU ENG LIM METH | Number | # | 10 Hz |
| CC224 | ECU RPM LIM METH | Number | # | 10 Hz |
| CC225 | ECU EN LIM F | Number | # | 10 Hz |
| CC226 | ECU RPM LIM F | Number | # | 10 Hz |
| CC228 | ECU CUT PERC F | Number | # | 10 Hz |
| CC250 | ECU HEAD LIGHT S | Number | # | 10 Hz |
| CC251 | ECU HBEAM L STAT | Number | # | 10 Hz |
| CC252 | ECU LEFT IND STA | Number | # | 10 Hz |
| CC253 | ECU RIGHT IN ST | Number | # | 10 Hz |

### Nitrous

| CC ID | Name | Function | Unit | Freq |
|---|---|---|---|---|
| CC187 | ECU NITROUSEN1S | Number | # | 10 Hz |
| CC188 | ECU NITROUSEN1OU | Number | # | 10 Hz |
| CC189 | ECU NITROUSEN2S | Number | # | 10 Hz |
| CC190 | ECU NITROUSE2O | Number | # | 10 Hz |
| CC191 | ECU NITROUSE3S | Number | # | 10 Hz |
| CC192 | ECU NITROUSE3O | Number | # | 10 Hz |
| CC193 | ECU NITROUSE4S | Number | # | 10 Hz |
| CC194 | ECU NITROUSE4O | Number | # | 10 Hz |
| CC195 | ECU NITROV1S | Number | # | 10 Hz |
| CC196 | ECU NITROV1O | Number | # | 10 Hz |
| CC197 | ECU NITROV2S | Number | # | 10 Hz |
| CC198 | ECU NITROV2O | Number | # | 10 Hz |
| CC199 | ECU NITROV3S | Number | # | 10 Hz |
| CC200 | ECU NITROV3O | Number | # | 10 Hz |
| CC201 | ECU NITROV4S | Number | # | 10 Hz |
| CC202 | ECU NITROV4O | Number | # | 10 Hz |
| CC265 | ECU NOS BOTTLE | Number | # | 10 Hz |

### Water Injection

| CC ID | Name | Function | Unit | Freq |
|---|---|---|---|---|
| CC137 | WaterInj AdvOutS | Number | # | 10 Hz |
| CC203 | ECU WATINJSS EN | Number | # | 10 Hz |
| CC204 | ECU WATINJOS EN | Number | # | 10 Hz |
| CC205 | ECU WAT INJSS OV | Number | # | 10 Hz |
| CC206 | ECU WATINJ OVOS | Number | # | 10 Hz |

### Outputs / Motor Control

| CC ID | Name | Function | Unit | Freq |
|---|---|---|---|---|
| CC81 | ECU THERM FAN 3O | Number | # | 10 Hz |
| CC82 | ECU TRAC CT LIGH | Number | # | 10 Hz |
| CC83 | ECU THERM FAN 4O | Number | # | 10 Hz |
| CC84 | ECU AIR CTRL OUT | Number | # | 10 Hz |
| CC85 | ECU AIR CTRL REQ | Number | # | 10 Hz |
| CC86 | ECU ROTTRIM POT1 | Number | # | 10 Hz |
| CC87 | ECU THERM FAN 2O | Number | # | 10 Hz |
| CC88 | ECU THERM FAN 1O | Number | # | 10 Hz |
| CC89 | ECU ROTTRIM POT2 | Number | # | 10 Hz |
| CC90 | ECU ROTTRIM POT3 | Number | # | 10 Hz |
| CC108 | Handbrake St | Number | # | 10 Hz |
| CC207 | ECU CUT PERC MTH | Number | # | 10 Hz |
| CC256 | ECU OUTPUT3 | Numeric Status | # | 10 Hz |
| CC257 | ECU OUTPUT2 | Numeric Status | # | 10 Hz |
| CC258 | ECU OUTPUT1 | Numeric Status | # | 10 Hz |
| CC259 | ECU OUTPUT0 | Numeric Status | # | 10 Hz |
| CC262 | ECU MOTOR CTRL3 | Number | # | 10 Hz |
| CC263 | ECU MOTOR CTRL2 | Number | # | 10 Hz |
| CC264 | ECU MOTOR CTRL1 | Number | # | 10 Hz |
| CC266 | ECU EXH CUTOUT | Number | # | 10 Hz |
| CC267 | ECU PD16 PROTO | Number | # | 10 Hz |

### Diagnostics / Generic

| CC ID | Name | Function | Unit | Freq |
|---|---|---|---|---|
| CC124 | ECU GenericSen1 | Number | # | 10 Hz |
| CC125 | ECU GenericSen2 | Number | # | 10 Hz |
| CC126 | ECU GenericSen3 | Number | # | 10 Hz |
| CC127 | ECU GenericSen4 | Number | # | 10 Hz |
| CC128 | ECU GenericSen5 | Number | # | 10 Hz |
| CC129 | ECU GenericSen6 | Number | # | 10 Hz |
| CC130 | ECU GenericSen7 | Number | # | 10 Hz |
| CC131 | ECU GenericSen8 | Number | # | 10 Hz |
| CC132 | ECU GenericSen9 | Number | # | 10 Hz |
| CC133 | ECU GenericSen10 | Number | # | 10 Hz |
| CC243 | ECU FLTA LEAKDT | Number | # | 5 Hz |
| CC244 | ECU FRTA LEAKDC | Number | # | 5 Hz |
| CC245 | ECU RLTA LEAKDC | Number | # | 5 Hz |
| CC246 | ECU RRTA LEAKDC | Number | # | 5 Hz |
| CC237 | ECU FLTS BATTVOL | Voltage | mV | 5 Hz |
| CC238 | ECU FRTS BATTVOL | Voltage | mV | 5 Hz |
| CC239 | ECU RLTS BATTVOL | Voltage | mV | 5 Hz |
| CC240 | ECU RRTS BATTVOL | Voltage | mV | 5 Hz |

---

## Notes

- **CC30 ECU BrakePress** is NOT enabled — brake pressure comes from AVI7 Lowdoller sensor via direct Haltech AVI channel, not this CAN channel
- **CC142/CC143 IgnitionAng1/IgnitionAng2** — both enabled; worthwhile for per-cylinder knock retard visibility paired with CC26/CC27 knock levels
- **CC260 ECU H2O INJ DUTY** — explicitly excluded (no water injection on this car)
- **Total headroom:** 79 enabled of 120 max → 41 slots remaining for future channels
- Config file: `Webinar_complete_02` (tab name visible in Race Studio title bar)
