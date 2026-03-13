# PDM Build Guide — White Tiburon (Consolidated)
## AIM PDM 32 | Haltech Elite 2500 | Physical Switch Panel

**Car:** White 2003 Tiburon GK (2.7L V6 Delta / G6BA)
**Race series:** 24 Hours of Lemons

> **One Race Studio config for all phases.** All outputs are configured for Phase 2 from day one. Outputs with no load connected drive open circuits harmlessly. Phase transitions require rewiring, not reconfiguration. Phase 3 (CAN keypad) is the only config change.

---

## Phase Overview

| Phase | ECU | Relay Box | PDM Role | Reversibility |
|-------|-----|-----------|----------|---------------|
| **1** | Stock SIMK43 | Powered, relays pulled selectively | Smart fuse box + kill switch | Put relays back |
| **2** | Haltech Elite 2500 | Unpowered (leave mounted) | Full power distribution | Plug stock ECU back in, put relays back |
| **3** | Haltech Elite 2500 | Removed | Full power + CAN keypad | N/A — committed |

**Escape clause:** If Phase 1 trips the 120A breaker or shows excessive draw through relay spade connections, skip directly to Phase 2 (Haltech takes over engine, relay box bypassed entirely).

---

## Race Studio Configuration (Friday at Home)

> **Do this ONCE.** This config covers Phase 1 and Phase 2 with no changes. Phase 3 adds CAN2 keypad.

### Starting Point

1. Open `Webinar complete.zconfig` in Race Studio 3
2. **File → Save As** → `Tiburon_White_v1.zconfig`

### Channel Inputs

| PDM Input | Pin | Assignment | Type | Notes |
|-----------|-----|------------|------|-------|
| **IGN Input** | B23 | Ignition switch | Built-in | Latching toggle, 12V when ON |
| **Ch01** | B26 | Fan override | Digital, latching | 12V when ON |
| **Ch02** | B27 | Spare (was Wiper Low) | — | Available for future use |
| **Ch03** | B28 | Spare (was Wiper High) | — | Available for future use |
| **Ch04** | B29 | Coolsuit | Digital, latching | 12V when ON |
| **Ch05** | B30 | Defogger | Digital, latching | 12V when ON |
| **Ch06** | B31 | Horn | Digital, momentary | Phase 2+: momentary button, active = GND |
| **Ch07** | B32 | Headlights | Digital, latching | Phase 2+: toggle, 12V when ON |
| **Ch09** | B21 | Start button | Digital, momentary | Active = GND |
| **Ch11** | A26 | Brake light switch | Digital | Closed on press |

Ch08, Ch10, Ch12 are **spare**.

### Status Variables (Math Channels)

Configure all of these now — they work across all phases.

| Variable | Logic | Used By |
|----------|-------|---------|
| `SafeIgnition` | IGN input ON and stable (built-in) | Master permissive for engine outputs |
| `ENGINE_RUNNING` | CAN RPM > 50 (2s off-delay for stall protection) | Starter interlock, fuel pump, oil P alarm |
| `FUEL_PRIME` | 3s one-shot timer on SafeIgnition rising edge | Fuel pump prime on ignition ON |
| `FAN_TEMP_25` | CAN Coolant_T > 77°C (hysteresis −5°C, off at 72°C) | Fan 25% — 170°F thermostat opens here |
| `FAN_TEMP_50` | CAN Coolant_T > 82°C (hysteresis −5°C) | Fan 50% |
| `FAN_TEMP_75` | CAN Coolant_T > 87°C (hysteresis −5°C) | Fan 75% |
| `FAN_TEMP_100` | CAN Coolant_T > 92°C | Fan 98% — thermostat est. fully open |
| `FAN_FAILSAFE` | CAN Coolant_T signal timeout > 5s | Fan 98% failsafe (CAN lost) |
| `STARTER_SAFE` | Ch09 AND SafeIgnition AND NOT ENGINE_RUNNING | Safe to crank |
| `LOW_OIL_P` | CAN Oil_P < 15 PSI AND ENGINE_RUNNING AND RPM > 500 | Warning LED |
| `HIGH_COOLANT_T` | CAN Coolant_T > 95°C | Warning LED |
| `HIGH_OIL_T` | CAN Oil_T > 130°C | Warning LED |
| `LOW_FUEL_P` | CAN Fuel_P < 40 PSI AND ENGINE_RUNNING AND RPM > 500 | Warning LED |
| `MULTI_WARNING` | LOW_OIL_P OR HIGH_COOLANT_T OR HIGH_OIL_T OR LOW_FUEL_P | Red LED trigger |
| `WIPER_ACTIVE` | Ch02 OR Ch03 | Wiper switch state (future) |
| `WIPER_ACTIVE_DLY` | WIPER_ACTIVE with Delay Off = 3000ms | Stays TRUE 3s after switches off |
| `WIPER_PARKING` | WIPER_ACTIVE_DLY AND NOT WIPER_ACTIVE | 3s one-shot for park sweep (future) |

> **RPM > 500 guard** on oil/fuel alarms prevents false alarms at cranking and idle.
> **Wiper variables** are pre-configured but inactive until Ch02/Ch03 switches are installed. No relay needed — see wiper section below.

### ECU Stream (CAN1 — Haltech)

1. Go to **ECU Stream** tab
2. Select **Haltech CAN_V2_40** protocol
3. Bus: CAN1 (A30/A31), **500 kbps**
4. Enable **120Ω termination** if Haltech does not self-terminate
5. Leave **"Silent on CAN Bus"** OFF initially; enable if Haltech logs CAN errors
6. Enable channels: RPM, Coolant Temp (ECT), Oil Pressure, Oil Temp, Fuel Pressure, TPS, Vehicle Speed, Battery Voltage

> **Max 120 channels** in Race Studio ECU stream (Haltech protocol has ~267). Uncheck header row first, then manually enable only the channels listed above plus any logging channels you want.

### SmartyCam Stream

1. Go to **SmartyCam Stream** tab
2. Enable SmartyCam on **CAN AiM** bus (CAN0, A22/A11)
3. Assign: RPM, Speed (GPS-08), Gear, Coolant Temp, Oil Pressure, TPS, Lat G, Long G

### CAN2 — Disable

Remove or disable the CAN Keypad 12 config. Delete all `*KYD` variables. CAN2 is unused until Phase 3.

### Output Map (All Phases)

| Output | Name | Pin(s) | Mode | MaxLoad | Inductive | PWM | Trigger |
|--------|------|--------|------|---------|-----------|-----|---------|
| **HP1** | Starter | A1+A13 | OVC | 20A | Yes | DC | STARTER_SAFE |
| **HP2** | Fan | A12+A23 | Fused | 35A | No | 100Hz | Fan PWM curve + Ch01 override |
| **HP3** | FuelPump | A24+A25 | OVC | 15A | Yes | DC | FUEL_PRIME OR ENGINE_RUNNING |
| HP4 | Spare | A34+A35 | — | — | — | — | — |
| **MP1** | InjPwr | A2 | OVC | 15A | Yes | DC | SafeIgnition |
| **MP2** | CoilPwr | A3 | OVC | 15A | No | DC | SafeIgnition |
| **MP3** | Horn | A4 | OVC | 10A | Yes | DC | Ch06 |
| **MP4** | BrakeLights | A5 | Fused | 10A | No | DC | Ch11 (always active) |
| **MP5** | TailLights | A6 | Fused | 10A | No | DC | SafeIgnition |
| **MP6** | Headlights | A7 | OVC | 15A | No | DC | Ch07 AND SafeIgnition |
| **MP7** | Coolsuit | A8 | OVC | 10A | Yes | DC | Ch04 AND SafeIgnition |
| **MP8** | Defogger | A9 | OVC | 10A | No | DC | Ch05 AND SafeIgnition |
| **LP1** | ECU_Power | A14 | OVC | 10A | No | DC | SafeIgnition |
| **LP2** | Dash | A15 | OVC | 10A | No | DC | SafeIgnition |
| **LP3** | SmartyCam | A16 | OVC | 10A | No | DC | SafeIgnition |
| **LP4** | Spare (was GPS) | A17 | OVC | 10A | No | DC | SafeIgnition |
| **LP5** | Wideband | A18 | OVC | 10A | No | DC | SafeIgnition |
| **LP6** | Cluster | A19 | OVC | 10A | No | DC | SafeIgnition |
| **LP7** | WarningLED | A20 | OVC | 5A | No | DC | MULTI_WARNING |
| **LP8** | AltExciter | A21 | OVC | 5A | No | DC | SafeIgnition |
| **MP9** | WiperLow | B4 | OVC | 10A | No | DC | Ch02 AND NOT Ch03 AND SafeIgnition |
| **MP10** | WiperHigh | B5 | OVC | 10A | No | DC | Ch03 AND SafeIgnition |
| **LP9** | WiperPark | B3 | OVC | 10A | No | DC | WIPER_PARKING AND SafeIgnition |

> **MP3 and MP6 repurposed** from wipers to horn and headlights. Wipers use MP9 (B4), MP10 (B5), LP9 (B3) on Connector B — relay-less park design using WIPER_PARKING math channel.

### HP2 Fan — Detailed Logic

```
Action 1: ON @ 25% duty  | Priority 1 | Trigger: FAN_TEMP_25 (>77°C)
Action 2: ON @ 50% duty  | Priority 2 | Trigger: FAN_TEMP_50 (>82°C)
Action 3: ON @ 75% duty  | Priority 3 | Trigger: FAN_TEMP_75 (>87°C)
Action 4: ON @ 98% duty  | Priority 4 | Trigger: FAN_TEMP_100 (>92°C) OR FAN_FAILSAFE
Manual:   ON @ 98% duty  | Priority 5 | Trigger: Ch01 (fan override toggle)

Soft Start: 1.0s (reduce inrush)
Hysteresis: 5°C per band (ON at threshold, OFF at threshold − 5°C)
Failsafe: CAN coolant_T lost > 5s → 98% duty
```

### HP1 Starter — Detailed Logic

```
Trigger: STARTER_SAFE
  = Ch09 AND SafeIgnition AND NOT ENGINE_RUNNING

OVC Retries: 1, Latch Off: 5s
Add 10s timeout: if HP1 ON > 10s → force off (motor protection)
HP1 has internal series diode (back-EMF protection)
```

### HP3 Fuel Pump — Detailed Logic

```
Trigger: FUEL_PRIME OR ENGINE_RUNNING

FUEL_PRIME:     3s one-shot on SafeIgnition rising edge
ENGINE_RUNNING: CAN RPM > 50 (2s off-delay for stall protection)

OVC Retries: 3 (pump may spike on initial prime)
Latch Off: 5s
No manual fuel override — cycle IGN off/on for 3s prime
```

### Wiper — Relay-Less Park Design (Future — Connector B)

Three PDM outputs replace the OEM park relay. The motor's internal cam disc handles park positioning.

**Motor wires:** Green = low speed, Yellow = high speed, Brown = park common, Black = ground/dynamic brake.

```
MP9  (B4)  → Green wire (low speed)   | Trigger: Ch02 AND NOT Ch03 AND SafeIgnition
MP10 (B5)  → Yellow wire (high speed)  | Trigger: Ch03 AND SafeIgnition
LP9  (B3)  → Brown wire (park sweep)   | Trigger: WIPER_PARKING AND SafeIgnition

Motor Black wire → chassis ground (always connected)
Motor Gray wire → leave disconnected (washer or unused)
```

**How park works without a relay:**
1. **Wipers ON:** MP9 or MP10 powers Green/Yellow. Brown (LP9) is OFF (WIPER_PARKING = 0 because WIPER_ACTIVE = 1). Motor runs normally.
2. **Switches OFF:** WIPER_ACTIVE drops to 0. WIPER_ACTIVE_DLY stays 1 for 3s. WIPER_PARKING = 1. LP9 powers Brown → internal cam routes Brown→Yellow → motor sweeps to park.
3. **At park position:** Cam finger flips Brown→Black. Current flows through winding (~6-8A) as dynamic brake. Motor stops instantly.
4. **After 3s:** WIPER_ACTIVE_DLY expires → WIPER_PARKING = 0 → LP9 cuts Brown.

**Safety constraint:** Brown is NEVER powered while Green/Yellow are powered. `NOT WIPER_ACTIVE` in the WIPER_PARKING formula guarantees this — LP9 can only activate when Ch02 and Ch03 are both off.

> **LP9 OVC:** Set to 10A. The Brown→Black current through the motor winding is ~6-8A for the brief park duration. Well within limits.
> **Not installed yet.** Wiper switches (Ch02/Ch03) and motor connections will be added when wipers are needed. Config is pre-loaded.

### Protection Settings

| Output | Mode | MaxLoad | Inductive | OVC Retries | Latch Off | Soft Start |
|--------|------|---------|-----------|-------------|-----------|------------|
| HP1 Starter | OVC | 20A | Yes | 1 | 5s | No |
| HP2 Fan | Fused | 35A | No | — | — | 1.0s |
| HP3 FuelPump | OVC | 15A | Yes | 3 | 5s | No |
| MP1 InjPwr | OVC | 15A | Yes | 1 | 5s | No |
| MP2 CoilPwr | OVC | 15A | No | 1 | 5s | No |
| MP3 Horn | OVC | 10A | Yes | 1 | 5s | No |
| MP4 BrakeLights | Fused | 10A | No | — | — | No |
| MP5 TailLights | Fused | 10A | No | — | — | No |
| MP6 Headlights | OVC | 15A | No | 1 | 5s | No |
| MP7 Coolsuit | OVC | 10A | Yes | 1 | 5s | No |
| MP8 Defogger | OVC | 10A | No | 1 | 5s | No |
| LP1–LP6 | OVC | 10A | No | 1 | 5s | No |
| LP7 WarningLED | OVC | 5A | No | 1 | 5s | No |
| LP8 AltExciter | OVC | 5A | No | 1 | 5s | No |

### Alarm Thresholds (Tune on Track)

| Alarm | Threshold | Guard | Notes |
|-------|-----------|-------|-------|
| Low oil pressure | < 15 PSI | RPM > 500 | Factory min 7.3 PSI; normal hot idle ~20–30 PSI |
| High coolant temp | > 95°C | Always | 170°F thermostat; normal 77–87°C; fully open ~92°C |
| High oil temp | > 130°C | Always | Normal operating ~90–110°C |
| Low fuel pressure | < 40 PSI | RPM > 500 | Factory idle spec 46–49 PSI |
| Fan ON (25%) | > 77°C | Always | 170°F thermostat opens here |
| Fan 100% | > 92°C | Always | Thermostat est. fully open |
| Fan failsafe | CAN timeout 5s | Always | Full speed if CAN data lost |
| Starter timeout | > 10s continuous | Always | Motor protection |

> **Note:** Fan temp bands (`FAN_TEMP_25` etc.) depend on Haltech CAN coolant temp, which isn't available until Sunday SU.6 when Haltech CAN1 is connected. On Saturday (Phase 1A), these variables will read 0/inactive — this is expected. Fan runs on stock BCM relay Saturday.

### SmartyCam Config (Session B — USB-C to Camera)

After PDM config is transmitted, connect USB-C directly to SmartyCam 3 Corsa:

1. RS3 detects SmartyCam as separate device
2. **CAN Protocol** tab → select **AiM Default** (matches PDM Session A setting)
3. **Overlay** tab → position RPM (top center), Speed (bottom center), Water Temp, Oil Pressure, TPS, G-force meter
4. **Save → Transmit** config to camera
5. On camera menu: **MENU → SETTINGS → AUTO START REC → Enable**
6. Insert SD card (≥2 GB)

> SmartyCam config reference: `hardware/aim/aim-smartycam/aim-smartycam.md`

### Podium Micro Config (USB or Phone — RaceCapture App)

1. Connect Podium Micro via USB to PC (or phone via Bluetooth)
2. Open **RaceCapture** app
3. Set CAN baud rate to **1000000** (1 Mbps — matches AIM CAN0)
4. Select **AIM** preset for CAN channel mapping
5. Map minimum channels: Speed, Latitude, Longitude (+ RPM, ECT, Oil P, TPS if in preset)
6. **WiFi → AP mode:** Enable (creates hotspot for pit wall dashboard on phone/tablet)
7. **WiFi → STA mode:** Enter phone hotspot SSID + password (2.4 GHz only) for cloud streaming
8. Insert SD card (≥2 GB) for local logging

> Podium config reference: `hardware/aim/aim-podium/aim-podium-micro.md`

### Transmit PDM Config

1. Save `Tiburon_White_v1.zconfig`
2. Connect PDM via USB
3. Transmit configuration
4. Force-test each output in Race Studio Live Measures (no loads — verify logic triggers only)
5. Backup: copy `.zconfig` to `AIM PDM/` folder

---

## Fuel Pump Bench Test (Friday at Home)

### Wiring

```
PDM HP3 outputs:
  A24 ─────┬────── Pump positive (+)
  A25 ─────┘

  Battery GND ─── Pump negative (−)
```

Both A24 and A25 carry HP3 — connect both for full current capacity. Use 14 AWG minimum.

### Test Sequence

**1. Prime cycle**
- IGN off → IGN on
- HP3 activates for **3 seconds** then cuts
- Verify in Race Studio: `FUEL_PRIME` timer fires, pump runs, then stops
- If no prime: check `SafeIgnition` = 1, verify timer rising edge logic

**2. Current measurement**
- Force HP3 ON in Race Studio Live Measures
- Measure current: expected 5–10A continuous
- If > 15A: check pump for binding; HP3 OVC will cut at 15A
- Record peak draw for wire gauge confirmation

**3. Voltage at pump**
- Measure pump + to − while running
- Should be within 0.5V of supply voltage
- > 1V drop: check connections or wire gauge

**4. Prime repeat test**
- IGN off, wait 5s, IGN on → should prime again
- Confirm one-shot timer resets properly

---

## Phase 1 — PDM + Stock ECU

### Concept

PDM acts as a smart fuse box with kill switch integration. Stock ECU and BCM remain connected and running. PDM replaces specific relays via spade connectors into pin 87 sockets. BCM continues to control horn, headlights, and (initially) fans through stock relays.

**What PDM controls in Phase 1:**
- Engine power via main relay pin 87 (coils, injectors, O2 sensors)
- Fuel pump via fuel pump relay pin 87
- Starter via solenoid S-terminal
- Alternator exciter via cut D+ wire
- Brake lights, tail lights
- Accessories (Haltech, dash, cameras, LM2, cluster)
- Fan (after CAN verified — see Phase 1B below)
- Warning LED

**What stays on stock relays (BCM controls):**
- Horn (steering wheel button → BCM → horn relay)
- Headlights (stalk switch → BCM → headlight relay)
- Fan (initially, until CAN data verified)

### Phase 1 Load Estimate

| Load Group | Est. Draw | Notes |
|------------|-----------|-------|
| MP1/MP2 (main relay → stock ECU circuits) | 15–25A | ECU + injectors + coils + O2 heaters |
| HP3 (fuel pump) | 5–10A | Continuous while running |
| HP1 (starter) | 15–20A | Momentary only |
| HP2 (fan, when added) | 10–35A | PWM dependent on temp |
| LP1–LP8 + MP4/MP5 | 10–15A | Accessories + lights |
| **Total (no fan, no starter)** | **~40–50A** | Well under 120A breaker |
| **Total (with fan peak)** | **~75–85A** | Comfortable margin |
| **Total (worst case all)** | **~105A** | Still under 120A; starter is momentary |

### Phase 1A — Core Install (Saturday Morning)

#### S.1 Mount Electronics Plate

All electronics on a single plate in passenger footwell: PDM, Haltech, Podium Micro (SN: 1QTV5KM), Innovate LM2.

- [ ] Bolt/rivet plate into passenger footwell
- [ ] Mount PDM (vibration-isolated)
- [ ] Mount Haltech Elite 2500
- [ ] Mount Podium Micro
- [ ] Mount Innovate LM2

#### S.2 Kill Switch Wiring

Kill switch already mounted left of steering wheel. 2 AWG cable already run to large terminal A.

```
Battery (+) ─── 2 AWG ─── Kill Switch [Large Terminal A]
                                │
                          [Jumper] to [Small Terminal A]
                                │
                     Kill Switch [Large Terminal B] ───┬─── 2 AWG ─── 150A Breaker ─── Starter B+ / Alt B+
                                │                      │
                                │                      └─── 4 AWG ─── 120A Breaker ─── PDM Surlok (+)
                                │
                     Kill Switch [Small Terminal B] ─── IGN toggle ───┬─── PDM B23 (IGN input)
                                                                      └─── Haltech 34-pin pin 13 (ECU IGN)
```

- [ ] Verify jumper: large terminal A → small terminal A
- [ ] Large terminal B → 150A breaker → starter B+ / alternator B+ (2 AWG)
- [ ] Large terminal B → 120A breaker → PDM Surlok (+) (4 AWG)
- [ ] Small terminal B → IGN toggle switch
- [ ] IGN toggle → PDM B23 AND Haltech 34-pin pin 13 (P wire)
- [ ] Connect PDM Surlok power cable
- [ ] Connect PDM grounds: B13, B14, B18 to chassis

#### S.3 Switch Panel Wiring

```
Switch Panel Layout (Phase 1)
==============================

Latching toggles:
  [IGN]  [FAN]  [COOL]  [DEFOG]  (2 spare positions)

Momentary:
  [START]                         (RED warning LED)
```

- [ ] IGN toggle → B23 (already wired in S.2)
- [ ] Start button → Ch09 (B21), momentary, active = GND
- [ ] Fan override → Ch01 (B26), latching, active = 12V
- [ ] Coolsuit → Ch04 (B29), latching, active = 12V
- [ ] Defogger → Ch05 (B30), latching, active = 12V
- [ ] Brake light switch → Ch11 (A26), closed on press
- [ ] Warning LED → LP7 (A20)

> **Phase 2 additions:** Add horn button → Ch06 (B31) and headlight toggle → Ch07 (B32) when BCM is unplugged.

#### S.4 First Power-Up

- [ ] Kill switch ON, IGN toggle ON → PDM powers up
- [ ] Connect laptop USB → Race Studio Live Data
- [ ] Verify `SafeIgnition` = 1
- [ ] Flip each toggle → verify correct channel input in Live Data
- [ ] Press START → verify `STARTER_SAFE` activates (ENGINE_RUNNING = 0)
- [ ] IGN toggle OFF → verify `SafeIgnition` = 0, all outputs drop
- [ ] Kill switch OFF → verify total power loss

> **GATE: All switches verified before connecting any loads.**

#### S.5 Dash + LVDS

- [ ] Mount AIM 10" dash
- [ ] Connect LVDS cable (PDM Rosenberger → dash)
- [ ] Verify dash powers up and shows live data

#### S.6 Fuse Box Connections — Core

**Main Relay (MP1 + MP2 → OE main relay pin 87):**
- [ ] Locate OE main relay in underhood fuse box
- [ ] Pull the relay
- [ ] Insert MP1 (A2) wire into pin 87 socket
- [ ] Insert MP2 (A3) wire into same pin 87 socket (parallel)
- [ ] IGN on → verify stock ECU powers up; IGN off → ECU loses power
- [ ] **Test:** Stock dash lights, check engine light, fuel gauge all work

**Fuel Pump Relay (HP3 → fuel pump relay pin 87):**
- [ ] Pull OEM fuel pump relay
- [ ] Insert HP3 (A24+A25) wire into pin 87 socket
- [ ] IGN on → listen for 3-second fuel prime → off
- [ ] Verify in Race Studio: `FUEL_PRIME` fires, `FuelSV` active → inactive

**Starter (HP1 → solenoid S-terminal):**
- [ ] Run HP1 (A1+A13) wire directly to starter solenoid S-terminal (10 AWG, ring terminal)
- [ ] Press START (Ch09) → engine cranks; release → stops
- [ ] Start engine → press START again → should NOT engage (RPM interlock)

> **Direct to solenoid is more reliable than fuse box spade for starter.** HP1 has internal series diode — no additional protection needed. Leave OEM starter relay in place as backup (can be used if PDM fails).

#### S.7 Alternator Exciter (LP8)

- [ ] Locate OEM alternator D+ exciter wire (~18 AWG at alternator Yazaki connector)
- [ ] Confirm with multimeter: 12V with IGN on, 0V with IGN off
- [ ] Cut exciter wire; leave length on both ends
- [ ] Fuse box side → wire to PDM LP8 (A21)
- [ ] Alternator D+ side → remains connected to alternator

#### S.8 CAN0 Expansion Bus — AIM Devices + Podium

> The Data Hub is a passive star splitter — each device plugs into its own hub port. GPS-08 and Podium get power through the hub's +Vb rail (PDM A33, always on). SmartyCam Corsa needs **separate 12V** from LP3 (A16) via its 7-pin main power connector — the 5-pin EXP port carries CAN data only.

**Physical connections:**
- [ ] Verify CAN0 expansion cable: A22 (H) / A11 (L) / A33 (+Vb) / A10 (GND)
- [ ] Connect AIM CAN Data Hub (4-way) male port to expansion cable
- [ ] Hub port 1 → GPS-08 (5-pin Binder male cable)
- [ ] Hub port 2 → SmartyCam 3 Corsa EXP port (5-pin Binder — CAN data only)
- [ ] Hub port 3 → Podium Micro (Binder-to-M8 adapter cable)
- [ ] Wire LP3 (A16) → SmartyCam 7-pin main power connector (Red = +12V, Black = GND)

**Mounting:**
- [ ] Mount GPS-08 (roof/cowl — clear sky view, antenna face up)
- [ ] Mount SmartyCam (windshield or roll bar bracket)
- [ ] Podium Micro already on electronics plate (S.1)

**Verification:**
- [ ] IGN on → LP3 active → SmartyCam powers up (LED shows CAN activity: green/blue solid)
- [ ] GPS-08 powers up automatically via hub +Vb (LED on)
- [ ] Podium powers up via hub +Vb (power LED on, CAN ⇄ LED active)
- [ ] RS3 Live Data → CAN AiM bus shows traffic
- [ ] GPS channels appear in RS3 Channels tab after satellite lock (~30s outdoors)
- [ ] Connect phone to Podium AP WiFi → RaceCapture app shows channel tiles

> **Podium is NOT visible in Race Studio.** It's an Autosport Labs device, not AIM. Verify via the RaceCapture app (phone/tablet), not RS3. See `hardware/aim/aim-podium/aim-podium-micro.md` for config.

> **LP4 (A17):** Listed as "GPS" in output map but GPS-08 gets power through the hub's +Vb rail (A33, always on). LP4 is currently a spare — repurpose if needed for another accessory.

### Test Gate — Phase 1A (Saturday)

| Test | Expected | Pass? |
|------|----------|-------|
| SafeIgnition toggles with IGN switch | ON/OFF clean | |
| Fuel prime (3s) on IGN on | HP3 on 3s then off | |
| Engine cranks via Ch09 START | Starter engages | |
| Engine starts and runs | ENGINE_RUNNING = 1 | |
| Starter interlock while running | No crank | |
| Alternator charging | 13.8–14.4V at battery | |
| Kill switch kills everything | Engine dies, power drops, alt stops | |
| Fan works via stock relay | BCM controls fan normally | |
| Horn works via steering wheel | BCM controls horn normally | |
| Headlights work via stalk | BCM controls headlights normally | |
| Brake lights via pedal | MP4 on (test with IGN off too) | |
| Tail lights automatic | MP5 on with SafeIgnition | |
| Warning LED | LP7 triggers on forced alarm | |
| Dash shows live data | LVDS working | |

> **GATE: Car starts, runs, and stops reliably. Kill switch kills everything. Fan/horn/lights work through stock BCM.**

### Phase 1B — CAN + Sensors + Fan Migration (Sunday)

After sensors are installed and Haltech CAN data is confirmed flowing to PDM.

#### SU.1–SU.5 Sensor Installation

> Full sensor installation procedure in `weekend-tasks.md` (SU.1–SU.5). Combination sensors (oil/coolant/fuel pressure+temp) wire to Haltech AVIs.

#### SU.6 Verify CAN1 (Haltech → PDM)

- [ ] Connect Haltech 26-pin pins 23/24 (CAN H/L) → PDM A30/A31 (CAN1)
- [ ] Power Haltech from PDM LP1 (A14)
- [ ] Verify in Race Studio Live Data: RPM, Coolant Temp, Oil Pressure visible
- [ ] Confirm `FAN_TEMP_25` through `FAN_TEMP_100` react to live coolant temp
- [ ] Confirm `MULTI_WARNING` triggers when alarm thresholds crossed (force values in NSP)

> **GATE: CAN data flowing before moving fan to PDM control.**

#### SU.7 Move Fan to PDM Control

Now that CAN temp data is confirmed, move fan from stock relay to PDM.

**Option A — Through relay socket (reversible, try first):**
- [ ] Pull OEM fan relay
- [ ] Insert HP2 (A12+A23) wire into fan relay pin 87 socket (12 AWG)
- [ ] Test: warm up engine → verify fan bands activate at correct temps

**Option B — Direct to fan motor (if relay socket has too much resistance):**
- [ ] Run HP2 (A12+A23) directly to fan motor connector
- [ ] Leave OEM fan relay in place as backup (can be reinstalled)
- [ ] Test: same as Option A

- [ ] Verify fan override toggle (Ch01) → 98% duty
- [ ] Verify fan failsafe: disconnect Haltech CAN temporarily → fan goes to 98% after 5s
- [ ] Reconnect CAN

#### SU.8 Full System Test

- [ ] Start car → all CAN data flowing
- [ ] Drive around → fan cycles with temp, all gauges work
- [ ] Kill switch test → everything dies
- [ ] All switches function correctly
- [ ] Record: peak fan current, total PDM current (POTotCurrent)

### Phase 1 — What Stays on Stock Relays

| Load | Why It Stays | Phase 2 Migration |
|------|-------------|-------------------|
| Horn | BCM + steering wheel button works perfectly | MP3 (A4) + Ch06 button |
| Headlights | BCM + stalk switch works, has features (delay, hi/lo) | MP6 (A7) + Ch07 toggle |

These loads move to PDM in Phase 2 when BCM is unplugged. The outputs (MP3, MP6) are already configured in Race Studio — just need physical wiring and switch panel additions.

---

## Phase 2 — PDM + Haltech ECU

### Concept

Haltech takes over engine control. Stock ECU and BCM are unplugged but left mounted for easy reversal. The OE relay box is unpowered — PDM outputs go directly to loads. Deutsch connectors D2 (coils) and D3 (injectors) plug in. Horn and headlights move to PDM since BCM is disconnected.

### What Changes from Phase 1

| Item | Phase 1 | Phase 2 |
|------|---------|---------|
| Engine ECU | Stock SIMK43 (connected) | Haltech Elite 2500 (active) |
| Stock ECU | Powered via MP1/MP2 → main relay pin 87 | Unplugged, mounted |
| BCM | Connected and active | Unplugged, mounted |
| MP1 wire | OE main relay pin 87 | D3 pin 7 → injector rail + Haltech 34-pin pin 26 |
| MP2 wire | OE main relay pin 87 | D2 pin 7 → COP coil Pin D common bus (all 6 coils) |
| HP3 wire | Fuel pump relay pin 87 | Direct to fuel pump (or leave on relay socket) |
| Coils | Stock harness (OE ECU drives) | D2 Deutsch → 6× Toyota 90919-A2005 via Haltech IGN 1–6 |
| Injectors | Stock harness (OE ECU drives) | D3 Deutsch → 6× injectors via Haltech INJ 1–6 |
| Horn | BCM + steering wheel | MP3 (A4) → horn relay pin 87 or direct; Ch06 button |
| Headlights | BCM + stalk switch | MP6 (A7) → headlight relay pin 87 or direct; Ch07 toggle |
| Relay box | Powered, relays pulled selectively | Unpowered — all relays can go back in (no current) |
| Race Studio config | **No change** | **No change** |

### Transition Procedure

> **Reversibility:** To go back to Phase 1, plug stock ECU + BCM back in, reconnect MP1/MP2 to main relay pin 87, pull D2 + D3 Deutsch connectors, remove Ch06/Ch07 switches. Relay box powers back up normally.

**Step 1 — Disconnect stock ECU**
- [ ] Unplug stock ECU connectors (C133-1 through C133-4)
- [ ] Leave ECU mounted in place
- [ ] Label all connectors for reversal

**Step 2 — Disconnect BCM**
- [ ] Unplug BCM connector
- [ ] Leave BCM mounted
- [ ] Note: horn (steering wheel button) and headlights (stalk) will no longer function through stock path

**Step 3 — Reroute MP1 (injector power)**
- [ ] Pull MP1 spade from OE main relay pin 87 socket
- [ ] Connect MP1 (A2) to D3 pin 7 (chassis side of injector Deutsch)
- [ ] D3 pin 7 splices to both injector rail 12V and Haltech 34-pin pin 26 (R/L, injector power sense)

**Step 4 — Reroute MP2 (coil power)**
- [ ] Pull MP2 spade from OE main relay pin 87 socket
- [ ] Connect MP2 (A3) to D2 pin 7 (chassis side of coil Deutsch)
- [ ] D2 pin 7 → Pin D common bus on all 6 Toyota COP coils

**Step 5 — Put main relay back**
- [ ] Re-insert the OE main relay (slot is now empty, relay box unpowered — relay does nothing)
- [ ] This keeps the relay socket tidy and available if reverting

**Step 6 — Connect Deutsch harnesses**
- [ ] Plug in D2 (coil harness) — engine side already connected to coils
- [ ] Plug in D3 (injector harness) — engine side already connected to injectors
- [ ] Verify D1 (engine sensors) connected — cam, crank, knock, IAT, MAP, TPS to Haltech
- [ ] Verify D4 (Lowdoller sensors) connected — oil/coolant/fuel to Haltech AVIs

**Step 7 — Add horn + headlight controls**
- [ ] Add momentary horn button → Ch06 (B31)
- [ ] Add latching headlight toggle → Ch07 (B32)
- [ ] Wire MP3 (A4) → horn (direct to horn or through relay socket)
- [ ] Wire MP6 (A7) → headlights (direct or through relay socket)

**Step 8 — First fire on Haltech**
- [ ] Haltech powered via LP1 (A14)
- [ ] Verify base tune loaded in Haltech NSP
- [ ] IGN on → fuel prime → press START → engine fires
- [ ] Confirm idle, check for fault codes
- [ ] Verify all CAN data flowing (RPM, temps, pressures)

### Test Gate — Phase 2

| Test | Expected | Pass? |
|------|----------|-------|
| Engine starts on Haltech | Clean idle, no faults | |
| All CAN data flowing | RPM, temps, pressures in Race Studio | |
| Fan PWM tracks coolant temp | Correct bands at correct temps | |
| Fuel pump runs while engine running | HP3 active, correct current | |
| Starter interlock | No crank while running | |
| Kill switch kills everything | Engine dies, all power drops | |
| Horn via Ch06 button | MP3 sounds horn | |
| Headlights via Ch07 toggle | MP6 lights on/off | |
| Brake lights | MP4 on pedal press (works with IGN off) | |
| Tail lights | MP5 on with SafeIgnition | |
| Warning LED on alarm | LP7 triggers correctly | |
| OE cluster still works | Tach from Haltech DPO 1, speedo from OEM VSS | |
| Wideband AFR reading | LM2 → AVI 8 shows lambda | |
| **Reversal test:** plug stock ECU back in | Car runs on stock ECU | |

### Deutsch Connector Reference (Phase 2 Harnesses)

> Full harness design with pin maps: `guides/harness-design.md`

**D1 — Engine Sensors (12-pin):** Cam, crank, knock, IAT, MAP, TPS
**D2 — Coil Harness (8-pin):** IGN 1–6 triggers + MP2 power + ground
**D3 — Injector Harness (8-pin):** INJ 1–6 signals + MP1 power
**D4 — Lowdoller Sensors (8-pin):** Oil/coolant/fuel pressure+temp, +5V, GND

**Phase 1 note:** D2 and D3 are built during Phase 1 but NOT plugged in. Stock ECU drives coils/injectors through OE harness. When switching to Phase 2, disconnect stock coil/injector connectors, plug in D2 + D3, reroute MP1/MP2.

---

## Phase 3 — CAN Keypad + OE Removal

### Concept

Full commitment to PDM + Haltech. OE ECU, BCM, and relay box physically removed. CAN keypad adds redundant driver controls alongside physical switches. Direct wiring to all loads — no relay sockets.

### What Changes from Phase 2

| Item | Phase 2 | Phase 3 |
|------|---------|---------|
| Stock ECU | Mounted, unplugged | Removed |
| BCM | Mounted, unplugged | Removed |
| Relay box | Unpowered, relays in place | Removed |
| CAN2 | Unused | CAN Keypad 12 (125 kbps) |
| Fan wiring | Through relay socket or direct | Direct only |
| Horn wiring | Through relay socket or direct | Direct only |
| Headlights | Through relay socket or direct | Direct only |
| Wipers | Not installed | MP9 (B4) / MP10 (B5) via keypad or toggle |
| Race Studio config | **UPDATE REQUIRED** | Add CAN2 keypad + OR triggers |

### Race Studio Config Changes

1. **Enable CAN2** → 125 kbps, AIM CAN Keypad 12 protocol
2. **Add keypad buttons** K33–K42 (see `guides/keypad-config-future.md` for full assignments)
3. **Add keypad power output** — use a spare LP (LP9 B3 or repurpose)
4. **Update Math Channel triggers** to OR keypad + physical switch:

| Trigger | Phase 2 | Phase 3 |
|---------|---------|---------|
| STARTER_SAFE | Ch09 AND SafeIgnition AND NOT ENGINE_RUNNING | **(StarterKYD OR Ch09)** AND SafeIgnition AND NOT ENGINE_RUNNING |
| Fan override | Ch01 | **(FanKYD OR Ch01)** |
| Coolsuit | Ch04 AND SafeIgnition | **(CoolsuitKYD OR Ch04)** AND SafeIgnition |
| Horn | Ch06 | **(HornKYD OR Ch06)** |
| Headlights | Ch07 AND SafeIgnition | **(LightsKYD OR Ch07)** AND SafeIgnition |

5. **Add new features** (keypad-only):
   - Fuel override (K38 → FuelOverride toggle → HP3 additional trigger)
   - Pit limiter (K39 → PITLIMITER_SAFE + TPS gating → Haltech CAN output)
   - PodiumConnect comms (K40), pit-in laps (K41)

6. **Add wipers** if needed (relay-less park design):
   - MP9 (B4) → Green (low), MP10 (B5) → Yellow (high), LP9 (B3) → Brown (park)
   - Math channels: WIPER_ACTIVE, WIPER_ACTIVE_DLY (3s delay off), WIPER_PARKING — already configured
   - Trigger: WiperKYD positions OR physical toggles on Ch02/Ch03
   - Motor Black wire → chassis ground. No external relay needed.

### CAN2 Keypad Wiring

| PDM Pin | Connector | Signal | Keypad Side |
|---------|-----------|--------|-------------|
| A28 (CAN2 H) | Black | CAN H | Deutsch pin 2 (White) |
| A29 (CAN2 L) | Black | CAN L | Deutsch pin 1 (Blue) |
| LP power output | Black | +12V | Deutsch pin 4 (Red) |
| B18 (GND) | Grey | GND | Deutsch pin 3 (Black) |

> Full keypad config preserved in `guides/keypad-config-future.md` — button assignments, LED colors, variable names, cable pinout.

### Direct Wiring (Relay Box Removed)

With the relay box removed, all loads wire directly to PDM outputs:

| Load | PDM Output | Wiring |
|------|-----------|--------|
| Fan motor | HP2 (A12+A23) | Direct to fan motor connector, 12 AWG |
| Fuel pump | HP3 (A24+A25) | Direct to pump, 14 AWG |
| Starter | HP1 (A1+A13) | Direct to solenoid S, 10 AWG (already done) |
| Horn | MP3 (A4) | Direct to horn, 16 AWG |
| Headlights | MP6 (A7) | Direct to headlight connector, 14 AWG |
| Wiper low | MP9 (B4) | Direct to motor Green wire, 16 AWG |
| Wiper high | MP10 (B5) | Direct to motor Yellow wire, 16 AWG |
| Wiper park | LP9 (B3) | Direct to motor Brown wire, 16 AWG |

---

## Reference — Kill Switch States

| Kill Switch | IGN Toggle | State |
|-------------|-----------|-------|
| OFF | Any | Dead — all power cut, engine stops, alternator stops |
| ON | OFF | PDM has Surlok power (Race Studio config/testing), SafeIgnition = 0 |
| ON | ON | SafeIgnition = 1, all ignition-gated outputs active |

---

## Reference — CAN Bus Configuration

### CAN0 — AIM Expansion (A22 H / A11 L)

| Setting | Value |
|---------|-------|
| Speed | 1 Mbps |
| Devices | CAN Data Hub (star topology) → GPS-08 (port 1), SmartyCam (port 2), Podium (port 3) |
| Cable | Pre-wired CAN expansion harness (5-pin Binder, 22 AWG) |
| Power | A33 (+Vb out CAN, always on) powers GPS-08 + Podium via hub. SmartyCam powered separately via LP3 (A16, SafeIgnition). |
| Note | Dash connects via LVDS, not CAN0 |

### CAN1 — Haltech ECU (A30 H / A31 L)

| Setting | Value |
|---------|-------|
| Speed | 500 kbps |
| Protocol | Haltech CAN_V2_40 |
| Termination | 120Ω at PDM end if Haltech doesn't self-terminate |
| Silent on CAN | OFF initially; enable if Haltech logs CAN errors |
| Haltech wiring | 26-pin pin 23 (W) → A30; pin 24 (L) → A31 |
| Note | A30/A31 shared with RS232 — RS232 unavailable when CAN1 active |

### CAN2 — Unused (Phase 1/2) / Keypad (Phase 3)

| Setting | Value |
|---------|-------|
| Pins | A28 (H) / A29 (L) |
| Speed | 125 kbps (when keypad connected) |
| Phase 1/2 | Disabled |
| Phase 3 | AIM CAN Keypad 12 |

> **CRITICAL:** Never wire CAN2 devices to CAN0 (A11/A22). CAN0 = 1 Mbps. Mixing speeds = both buses fail.

---

## Reference — PDM Physical Connections by Phase

### Connector A (Black) — All Phases

| Pin | Output | Load | Ph1 | Ph2 | Ph3 |
|-----|--------|------|-----|-----|-----|
| A1+A13 | HP1 | Starter solenoid S | Direct | Direct | Direct |
| A2 | MP1 | Power | Main relay pin 87 | D3 pin 7 (inj) | Direct to inj rail |
| A3 | MP2 | Power | Main relay pin 87 | D2 pin 7 (coils) | Direct to coil bus |
| A4 | MP3 | Horn | Not connected | Horn relay/direct | Direct |
| A5 | MP4 | Brake lights | Connected | Same | Same |
| A6 | MP5 | Tail lights | Connected | Same | Same |
| A7 | MP6 | Headlights | Not connected | Relay/direct | Direct |
| A8 | MP7 | Coolsuit | Connected | Same | Same |
| A9 | MP8 | Defogger | Connected | Same | Same |
| A12+A23 | HP2 | Fan | Ph1B: relay/direct | Direct | Direct |
| A14 | LP1 | Haltech ECU | Connected | Same | Same |
| A15 | LP2 | Dash | Connected | Same | Same |
| A16 | LP3 | SmartyCam | Connected | Same | Same |
| A17 | LP4 | GPS | Connected | Same | Same |
| A18 | LP5 | LM2 Wideband | Connected | Same | Same |
| A19 | LP6 | Cluster | Connected | Same | Same |
| A20 | LP7 | Warning LED | Connected | Same | Same |
| A21 | LP8 | Alt exciter | Connected | Same | Same |
| A24+A25 | HP3 | Fuel pump | Relay pin 87 | Direct | Direct |

### Connector B (Grey) — Wiper + Phase 3 Additions

| Pin | Output | Load | Ph3 |
|-----|--------|------|-----|
| B3 | LP9 | Wiper Park (Brown) | Direct to motor Brown wire |
| B4 | MP9 | Wiper Low (Green) | Direct to motor Green wire |
| B5 | MP10 | Wiper High (Yellow) | Direct to motor Yellow wire |

---

## Reference — Switch Panel by Phase

### Phase 1 Panel (6 positions + 1 momentary + 1 LED)

```
[IGN]  [FAN]  [COOL]  [DEFOG]  [____]  [____]
[START]                                  (LED)
```

### Phase 2 Panel (8 positions + 1 momentary + 1 LED)

```
[IGN]  [FAN]  [COOL]  [DEFOG]  [HORN]  [LIGHTS]
[START]                                  (LED)
```

> Horn = momentary (not latching). Headlights = latching toggle.

### Phase 3 Panel — Same + CAN Keypad

Physical panel remains as backup. CAN keypad provides redundant controls with LED feedback.

---

## Cross-References

| File | Contents |
|------|----------|
| `guides/harness-design.md` | Deutsch connector pin maps, wire routing, bundle sizing |
| `guides/bench-test.md` | Additional bench test procedures and notes log |
| `guides/keypad-config-future.md` | Full CAN keypad button/LED/variable config for Phase 3 |
| `guides/pdm-session-1.md` | Step-by-step Race Studio 3 walkthrough |
| `signal-routing.md` | End-to-end signal trace for every wire |
| `weekend-tasks.md` | Current weekend build tasks (sensor install, harness fab) |
| `hardware/aim/aim-pdm/pdm-pinout.md` | Full 35-pin ×2 connector pinout |
| `hardware/aim/aim-pdm/pdm-configuration-guide.md` | Logic stack theory, PWM examples |
| `hardware/aim/aim-smartycam/aim-smartycam.md` | SmartyCam 3 pinout, RS3 config, overlay setup |
| `hardware/aim/aim-podium/aim-podium-micro.md` | PodiumConnect Micro pinout, RaceCapture config, CAN mapping |
| `hardware/aim/aim-datahub/aim-datahub.md` | CAN Data Hub star topology, pin mapping |
| `hardware/aim/aim-gps08/aim-gps08.md` | GPS-08 pinout, CAN behavior, mounting |
| `hardware/sensors/lowdoller-sensors.md` | Sensor specs, PTC calibration |
| `hardware/sensors/cop-ignition.md` | Toyota COP coil pinout |
