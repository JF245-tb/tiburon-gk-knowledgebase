# PDM Sensor Harness — Current Race Config (PDM Only, No ECU)
## White Tiburon — AIM PDM 32 reading sensors directly, stock ECU runs the engine

**Purpose: clean, working gauges for next weekend's race — not a permanent
architecture decision.** Stock ECU keeps running the car exactly as it does today;
this is just getting the Lowdoller/tire/trans sensors off temporary Wago splices
and onto a real PDM-read harness so the dash shows good data. The full Haltech
takeover (Phase 2/3 in the older docs) is explicitly deferred, not abandoned —
this doc and the finalized Deutsch harness below are meant to be easy to build on
top of when that happens, not something that has to be undone first.

**Status: this is the active plan for the upcoming race.** It supersedes the combined
PDM + Haltech architecture described in `harness-design.md`, `pdm-build-guide.md`,
`signal-routing.md`, and `hardware/sensors/lowdoller-sensors.md` — those documents
describe a shelved Phase 2/3 plan (Haltech running the engine, PDM doing full power
distribution) that is not part of this build for now. Revisit them if that plan is
picked back up later.

**What changed from the old plan:**
- Stock ECU continues to run the engine — no Haltech engine control, no Haltech in
  the sensor path at all.
- Relay box stays in as-is; only the ECU relay is being replaced. PDM distributes
  power to nothing except one reserved output (see Connector A below).
- **PDM's main job is reading sensors** and broadcasting them over CAN to the AIM
  dash / SmartyCam / Podium for display and logging. No switch panel, no power
  output logic tied to these channels.
- MAP sensor removed (was AVI9 on the old Haltech plan — not carried over).
- Coolant sensor dropped. The old coolant bypass loops (throttle body feed, heater
  core loop) are being capped — heater core is removed and the TB is already
  blocked internally, so neither loop serves a function anymore. OE coolant sender
  + stock ECU remains the coolant temp reference.
- Tire temp (front left only), transmission fluid pressure/temp, and Innovate LM2
  wideband AFR added.
- CAN0 (GPS-08, SmartyCam, Podium) and the Ignition input are being kept — not a
  pure sensor-only build, PDM retains those plus one power output for SmartyCam.

---

## Sensor List

| Sensor | Model | Signals | Location |
|---|---|---|---|
| Fuel pressure/temp | Lowdoller 899404 (150 PSI combo) | 2 (P + T) | On regulator, strut tower mount — right side |
| Transmission pressure/temp | Lowdoller 899404 (150 PSI combo) | 2 (P + T) | Right side, grouped with fuel/tire |
| Tire temp | 6–24VDC supply / 0–5V output sensor (non-Lowdoller) | 1 (T only) | Front left tire only |
| Oil pressure/temp | Lowdoller 899404 (150 PSI combo) | 2 (P + T) | Left side of engine |
| Wideband AFR | Innovate LM2, Analog Out 1 | 1 (AFR only) | LM2 on electronics plate, passenger footwell — cockpit-side run, not part of either engine-bay Deutsch connector |

Coolant: **excluded.** MAP: **removed.**

---

## PDM Channel Map

The AIM PDM 32 has 12 total channel inputs but only **8 are true analog-capable
(0–5V/0–12V)** — Ch01–Ch08. Ch09–Ch12 are digital-only and unused here. Since the
PDM isn't driving a switch panel or output logic in this build, all 8 analog
channels are free for sensors.

| Channel | Signal | Notes |
|---|---|---|
| Ch01 | Fuel pressure | 899404, 0.5–4.5V ratiometric |
| Ch02 | Fuel temp | 899404, PTC resistive — needs custom sensor calibration in Race Studio (raw element swings only ~84–198Ω across full range; do not rely on the 10kΩ digital pull-up used for switch inputs) |
| Ch03 | Oil pressure | 899404, 0.5–4.5V ratiometric |
| Ch04 | Oil temp | 899404, PTC — custom sensor cal in Race Studio |
| Ch05 | Trans pressure | 899404, 0.5–4.5V ratiometric |
| Ch06 | Trans temp | 899404, PTC — custom sensor cal in Race Studio |
| Ch07 | Tire temp (FL) | 0–5V output |
| Ch08 | AFR (LM2 Analog Out 1) | 0–5V, 0V = 7.35 AFR / 5V = 22.39 AFR linear |

> **All 8 analog channels are now committed — zero headroom left.** Adding AFR
> used the last spare (Ch08). Any future sensor (2nd tire zone, brake combo, a
> coolant tap) needs something else moved off first.

> PTC calibration table (same for all Lowdoller temp elements) is in
> `hardware/sensors/lowdoller-sensors.md` — reuse those resistance-vs-temperature
> values when building the custom sensor cal in Race Studio, just pointed at PDM
> channels instead of Haltech AVIs.

---

## Supply / Ground — PDM's Own Pins

No Haltech pins are used anywhere in this harness. Reference pins are on PDM
Connector B (Grey):

| Function | PDM Pin | Used By |
|---|---|---|
| +5V Analog Vref | B16 | Shared bus — all 3 Lowdoller combo sensors' red wires |
| Signal/clean GND | B18 | Shared bus — Lowdoller black+white returns, tire temp black wire, LM2 AFR signal ground (Yellow) |
| +Vb switched 12V | B17 | Tire temp red wire only (needs 6–24V, can't share the 5V bus) |
| Ignition input | B23 | Ignition switch — feeds the built-in `SafeIgnition` software channel for session start/stop marking in the log. Nothing is gated on it (no outputs), it's purely a log reference now. |

**Tire temp sensor pinout** (per sensor datasheet):

| Wire | Function | Destination |
|---|---|---|
| Red | Supply, 6–24VDC | PDM B17 (+Vb) |
| Black | Clean sensor ground | PDM B18 (shared clean GND bus) |
| White | Output signal, 0–5VDC | Ch07 |
| Clear (shield) | Chassis ground | Chassis, **not** the clean-GND bus — kept separate to avoid coupling shield-return noise into the shared analog sensor signals |

**LM2 AFR wiring** (cockpit-side, short run — does not go through either engine-bay
Deutsch connector). Confirmed against the official LM-2 User Manual (Innovate
doc #31-0008, Appendix C & §5.3) — this is the correct cable and it's wired as a
differential output referenced to ground (their "Diagram 2": device with a
grounded/single-ended analog input, which is what the PDM channel is):

| LM2 Wire | Function | Destination |
|---|---|---|
| Lime Green | Analog Out 1 (+) | Ch08 (B33) |
| Yellow | Analog Out 1 (−) | PDM B18 (shared clean GND bus) — **must** land on ground per the manual, this isn't optional on a differential output |

**Cable: P/N 3811** ("Analog Cable," 14 stripped leads) — already correct in this
doc, confirmed against the manual's Appendix C pinout and Appendix F kit
contents list.

**Calibration already at factory default — verify, don't assume.** Single-channel
LM-2 units ship with Analog Out 1 set to 0V = AFR 7.35, 5.0V = AFR 22.39 (exactly
what Ch08 is configured for above), but this is set via the **LM Programmer PC
software** (Analog Out 1 tab, over USB), not a front-panel menu on the LM-2
itself — there's no on-unit way to check it. If anyone has ever touched this
setting, it won't be what's assumed here. Two-minute check with LM Programmer
before trusting the AFR numbers.

**LM2 power (12V) does NOT come from the PDM.** Tap it from an existing
switched-ignition fused point in the stock harness/relay box — it's a small draw
(~1–2A) and this keeps the PDM's one reserved power output free for SmartyCam
(see Connector A below). Full LM2 cable 3811 pinout reference:
`guides/harness-design.md` → "Innovate LM2 Wiring" (wiring/pinout still accurate
even though that doc's AVI destination is superseded).

---

## Connector A (Black) — CAN0 Bus + Reserved Power Output

Kept for GPS-08, SmartyCam, and Podium — all three plug directly into the CAN
expansion Data Hub together, so SmartyCam does **not** need a separate PDM power
output after all (superseding the earlier assumption that it did). The reserved
power output is therefore unassigned — open for whatever the "just in case" use
turns out to be.

| Pin | Function |
|---|---|
| A22 | CAN0 High |
| A11 | CAN0 Low |
| A33 | +Vb out CAN — powers GPS-08, SmartyCam, and Podium through the Data Hub |
| A10 | GND (CAN0 expansion cable ground) |
| *(reserved)* | One power output pin held in reserve, purpose TBD |

(A32, +Vb ext CAN, skipped — documented as "typically unused.")

---

## Deutsch Connector Groups

Grouped by physical location to minimize the number of cable runs converging on
the PDM — two trunks instead of five individual sensor leads.

### Right Side — Fuel + Trans + Tire Temp (12-pin Deutsch)

| Pin | Signal |
|---|---|
| 1 | Fuel pressure (yellow) |
| 2 | Fuel temp (green) |
| 3 | Trans pressure (yellow) |
| 4 | Trans temp (green) |
| 5 | Tire temp signal (white) |
| 6 | Shared +5V (fuel + trans red wires) |
| 7 | Shared clean GND (fuel + trans black/white, tire temp black) |
| 8 | Tire temp +Vb supply (red) |
| 9 | Tire temp shield drain (clear → chassis GND) |
| 10–12 | Spare |

9 of 12 pins used, 3 spare.

### Left Side — Oil Only (4-pin Deutsch)

| Pin | Signal |
|---|---|
| 1 | Oil pressure (yellow) |
| 2 | Oil temp (green) |
| 3 | Shared +5V (red) |
| 4 | Shared clean GND (black/white) |

All 4 pins used — no spares on this one unless you want to size up for future
expansion (a 6-pin leaves room to add something else on this side later).

---

## Race Studio Configuration

The PDM is doing sensor readout as its main job, so the layered logic in
`pdm-configuration-guide.md` (Status Variables → Trigger Commands → Power
Outputs) doesn't apply here — SmartyCam, GPS-08, and Podium all get power
through the CAN0 Data Hub directly, not a PDM-triggered output. The one reserved
power output (Connector A) has no assigned purpose yet, so nothing to configure
for it either. The core work is configuring the 8 Channel Inputs as analog
sensors and making sure they reach the dash/logger over CAN.

> **Field names below follow the pattern used for the old Digital Status channel
> configs in `pdm-build-guide.md`, adapted for Analog mode.** Exact field labels
> for a Race Studio "Custom Sensor" analog channel haven't been screenshot-verified
> in this KB yet (everything documented previously was Digital Status for
> switches) — confirm against the live UI or the PDM32 user guide's channel-input
> section on first setup, and correct this doc from what you actually see.

### Step 0 — Strip Out What No Longer Applies

- [ ] **Disable/remove the ECU Stream (CAN1) config** — no Haltech, nothing to receive on that bus
- [ ] **Leave CAN2 disabled** — no keypad
- [ ] **Delete or disable all old switch-panel Status Variables / Trigger Commands / Power Outputs** — nothing in this build drives an output off PDM logic; GPS-08/SmartyCam/Podium power through the CAN0 Data Hub, not a PDM output
- [ ] Keep **CAN0 (CAN AiM, 1 Mbps)** active and configured — GPS-08, SmartyCam, and Podium are staying in this build

### Ch01 — `FuelPress`

| Field | Value |
|---|---|
| Name | `FuelPress` |
| Mode | Analog |
| Input range | 0–5V |
| Calibration | Linear, 2-point: 0.5V = 0 PSI, 4.5V = 150 PSI |
| Units | PSI |
| Sampling Frequency | 10 Hz |
| Log values | ✅ Yes |

### Ch02 — `FuelTemp`

| Field | Value |
|---|---|
| Name | `FuelTemp` |
| Mode | Analog |
| Calibration | Custom resistance table — PTC curve from `hardware/sensors/lowdoller-sensors.md` (84.27Ω @ −40°F → 197.71Ω @ 500°F) |
| Units | °F |
| Sampling Frequency | 2 Hz |
| Log values | ✅ Yes |

> Confirm what bias/pull-up Race Studio applies for a channel in this mode —
> the digital-input 10kΩ pull-up used for switches would be far too high a
> reference for an ~84–198Ω element and would flatten the signal to a few tens
> of millivolts across the whole range. See Open Items.

### Ch03 — `OilPress`

Same as Ch01 (`FuelPress`): 0.5V = 0 PSI, 4.5V = 150 PSI, 10 Hz, log ✅.

### Ch04 — `OilTemp`

Same as Ch02 (`FuelTemp`): PTC custom table, 2 Hz, log ✅.

### Ch05 — `TransPress`

Same as Ch01 (`FuelPress`): 0.5V = 0 PSI, 4.5V = 150 PSI, 10 Hz, log ✅.

### Ch06 — `TransTemp`

Same as Ch02 (`FuelTemp`): PTC custom table, 2 Hz, log ✅.

### Ch07 — `TireTempFL`

| Field | Value |
|---|---|
| Name | `TireTempFL` |
| Mode | Analog |
| Input range | 0–5V |
| Calibration | **Unknown — sensor's voltage-to-temperature transfer function not yet in this KB.** The pinout gives supply/ground/signal wiring only, no scaling curve. |
| Units | TBD |
| Sampling Frequency | 5 Hz |
| Log values | ✅ Yes |

> Until the transfer function is known, log this channel as a raw 0–5V value
> (no calibration applied) so the data isn't lost — just won't read in actual
> degrees on the dash until the curve is entered. Check the sensor's datasheet/
> listing for a linear range (e.g. "0–5V = X–Y °F") or a table like the PTC one.

### Ch08 — `AFR`

| Field | Value |
|---|---|
| Name | `AFR` |
| Mode | Analog |
| Input range | 0–5V |
| Calibration | Linear, 2-point: 0V = 7.35 AFR, 5V = 22.39 AFR |
| Units | AFR (or λ if you'd rather log lambda directly) |
| Sampling Frequency | 10 Hz |
| Log values | ✅ Yes |

### Getting Channels to the Dash

Configuring the channel isn't enough by itself — confirm each one is included in
whatever CAN0 broadcast/display list feeds the AIM dash (same mechanism already
used for SmartyCam overlay channels in `hardware/aim/aim-smartycam/aim-smartycam.md`),
and add them to a dash page so they're actually visible to the driver, not just
logged.

---

## Bypass Loop Disposition (Coolant)

Both the throttle-body coolant feed and the heater-core loop are being **capped
into dead-legs** rather than left flowing — neither the heater core (removed) nor
the TB coolant passages (blocked) need flow anymore. No sensor is being installed
in either capped stub for now; the OE coolant sender + stock ECU remains the
temperature reference. If a coolant channel is wanted later, threading a sensor
into one of these capped stubs is still on the table — see prior discussion: a
true dead-leg (zero flow) equalizes to actual system pressure, so it's a
reasonably good pressure tap despite being a former bypass branch. Would need a
free PDM analog channel, which there currently isn't one to spare without giving
up the Ch08 headroom.

---

## Open Items

- **PTC resistive sensor reading on PDM channel inputs** — confirmed to be handled
  via custom sensor calibration in Race Studio (per build decision). Worth a bench
  check with one sensor before committing all four temp channels to this scheme.
- **Tire temp voltage-to-temperature curve unknown** — need the sensor's datasheet
  scaling to calibrate Ch07 in Race Studio. Wire it and log raw volts in the
  meantime rather than waiting on this.
- **Exact Race Studio field names for Analog/Custom Sensor channel config
  unverified** — everything previously documented in this KB was Digital Status
  mode (switches). Confirm against the live UI on first setup and correct the
  per-channel tables above if the actual fields differ.
- **Reserved power output on Connector A has no assigned purpose** — SmartyCam
  turned out not to need it (powers through the CAN0 Data Hub like GPS/Podium).
  Confirm what "keep one power output just in case" was actually for before
  wiring anything to it.
- Trans sensor confirmed as Lowdoller 899404 combo (same as fuel/oil).
- Zero spare analog channels remain after adding AFR (Ch08). Any future sensor
  addition needs something else moved off first.
- **LM2 Analog Out 1 calibration should be verified in LM Programmer** before
  race day — it's assumed to still be at factory default (0V=7.35 AFR,
  5V=22.39 AFR) but there's no way to confirm that from the LM-2 itself.

---

## Cross-References

| File | Status |
|---|---|
| `guides/harness-design.md` | Describes shelved PDM+Haltech Deutsch architecture (D1–D4, coil/injector banks) — not current |
| `guides/pdm-build-guide.md` | Describes shelved PDM+Haltech Race Studio config (fan/switch outputs, ECU Stream) — not current |
| `signal-routing.md` | Describes shelved Haltech AVI assignments — not current |
| `hardware/sensors/lowdoller-sensors.md` | Sensor specs/PTC calibration table still accurate — reuse the resistance table, ignore the Haltech AVI assignment section |
| `hardware/aim/aim-pdm/pdm-pinout.md` | PDM connector pinout — still accurate, source for B16/B17/B18 references above |
