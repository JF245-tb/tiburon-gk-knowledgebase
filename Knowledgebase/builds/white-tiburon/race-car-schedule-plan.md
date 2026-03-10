# White Tiburon — HPDE + Lemons Schedule Plan
## Mar 10 → Apr 10, 2026

---

## Timeline

| Date | Event |
|------|-------|
| **Mar 10** | Today — planning start |
| **Mar 27** | HPDE weekend (testing) |
| **Mar 28 – Apr 8** | Post-HPDE integration window (12 days) |
| **Apr 9 (Fri)** | Test day at track — validation only, limited changes possible |
| **Apr 10 (Sat)** | Lemons race |

---

## Strategy

### Priorities (in order)
1. **Reliability** — car must be mechanically sound for both events
2. **Test what matters** — anything going on the race car should see track time at the HPDE if possible
3. **No rework** — sensor installs, wiring, and mounting should carry forward to the final Haltech build
4. **No rushing Haltech** — the two weeks between HPDE and race is the right window for full ECU integration

### Key Decision: PDM-Only at HPDE, Haltech After

Run the HPDE on **stock ECU + PDM** with sensor logging and full telemetry. Switch to **full Haltech** in the 12-day window after HPDE. Rationale:

- The stock ECU is proven and reliable — no risk of a bad tune or wiring gremlin ruining the HPDE
- The PDM, telemetry, and comms systems are all independent of the Haltech (CAN1 bus runs PDM → Dash → SmartyCam → GPS → Podium regardless of engine ECU)
- The HPDE validates everything *except* the Haltech tune — coilovers, brakes, seat position, PDM power logic, telemetry, camera, comms
- Two weeks is enough time to do Phase 3 (Haltech integration) properly and debug without pressure
- Test day (Apr 9) validates the Haltech under track conditions before the race

### Deutsch Connector Sensor Strategy

Build a **sensor breakout harness** with an inline Deutsch connector for the 3 Lowdoller sensors (fuel, oil, coolant). Each sensor has 2 signal wires (pressure yellow + temp green) = **6 signal wires + shared 5V + shared GND = 8 wires total → use a Deutsch DT 8-pin or DTM 8-pin connector**.

| Wire | Assignment |
|------|-----------|
| 1 | Fuel pressure (yellow) |
| 2 | Fuel temp (green) |
| 3 | Oil pressure (yellow) |
| 4 | Oil temp (green) |
| 5 | Coolant pressure (yellow) |
| 6 | Coolant temp (green) |
| 7 | +5V supply (red, shared) |
| 8 | Signal GND (black+white, shared) |

**HPDE config:** Deutsch socket → pigtail to Haltech AVIs (power Haltech as passive sensor reader on CAN0, stock ECU still runs engine). The Haltech doesn't need to control anything — it just reads AVI 1–6 and broadcasts over CAN to the PDM/dash. This is low-risk because the Haltech isn't in the engine control loop.

**Race config:** Same Deutsch socket → same Haltech AVIs. No change needed. The Haltech is now also managing engine, but the sensor wiring is identical.

> **Net effect:** Sensor install is permanent. Zero rework when switching to full Haltech. The only "HPDE-specific" work is confirming the Haltech can passively read and broadcast sensor data, which doubles as a Phase 0 bench test anyway.

**Alternative (if you don't want Haltech powered at HPDE at all):** Skip sensor logging at the HPDE — sensors are physically installed and plumbed, just not reading. You still validate coilovers/brakes/seat/telemetry. Sensor logging starts when Haltech goes live post-HPDE. The Deutsch connector still eliminates rework either way.

---

## Phase Schedule

### PHASE A — Finish Mechanical Basics (Mar 10–14)
*Get the must-do items knocked out early so nothing blocks HPDE readiness.*

- [ ] **Finish floor cut + seat brackets** — almost done, complete this first
- [ ] **Change brake pads (front)** — inspect front bearings while rotors are off (P2.6)
- [ ] **Build Deutsch sensor harness** — crimp sensor-side pigtails, build the 8-pin breakout, leave ECU-side pigtails for Phase B

> **Gate:** Floor done, brakes done, sensor harness built and labeled.

### PHASE B — PDM + Sensors + Telemetry (Mar 15–22)
*Install and test everything that will be validated at the HPDE. Stock ECU stays in charge of the engine.*

#### B1: Sensor Install (Mar 15–17)
- [ ] Install Lowdoller oil sensor during oil change (P2.1)
- [ ] Install Lowdoller coolant sensor on tee during coolant flush (P2.2)
- [ ] Install Lowdoller fuel sensor with Radium FPR + 6AN PTFE lines (P2.3)
- [ ] Connect all 3 sensors to Deutsch breakout harness
- [ ] Route ECU-side pigtail from Deutsch to Haltech AVI 1–6
- [ ] Power Haltech (LP1 from PDM) — confirm AVI readings in NSP at rest

#### B2: PDM Logic Tests (Mar 17–19)
Run through adapted Phase 1 tests from `weekend-tasks.md` — stock ECU runs engine, PDM controls power distribution:

- [ ] P1.1 — Power-up sequence, LP1–LP6 outputs, keypad LEDs
- [ ] P1.2 — CAN Keypad all buttons (can skip starter/fuel tests until wired)
- [ ] P1.3 — Fuel pump logic (if HP3 wired)
- [ ] P1.4 — Fan PWM logic
- [ ] P1.5 — Warning LED logic
- [ ] P1.8 — Brake lights

Optional for HPDE (nice to have, not critical):
- [ ] P1.6 — Start car via PDM (HP1 → starter solenoid)
- [ ] P1.7 — Alternator exciter via PDM (MP6)

#### B3: Telemetry + Comms (Mar 19–22)
- [ ] Mount AIM GPS module — connect to CAN1 daisy chain
- [ ] Mount SmartyCam3 Corsa — connect to CAN1, power from LP3
- [ ] Mount PodiumConnect Micro — connect to CAN1
- [ ] Confirm CAN1 chain: PDM → Dash → SmartyCam → GPS → Podium
- [ ] Test GPS lock and lap timing
- [ ] Test SmartyCam video recording + data overlay
- [ ] Test PodiumConnect live telemetry feed
- [ ] Configure K09/K10 (comms Yes/No, pit-in laps) and verify in PodiumConnect
- [ ] Test radios — range check, noise with engine running, PTT integration if applicable
- [ ] Confirm Haltech CAN0 → PDM sensor broadcast shows on dash (fuel/oil/coolant P+T)

> **Gate:** PDM controls power. Telemetry chain works end-to-end. Sensor data visible on dash. Comms confirmed. Car starts and runs reliably on stock ECU.

### PHASE C — Coilovers + HPDE Prep (Mar 23–26)
*Coilovers arrive and get installed in the 3–4 day window before HPDE.*

- [ ] Install coilovers (3–4 days)
- [ ] Set initial ride height and corner balance (if scales available)
- [ ] Check alignment — at minimum verify toe is safe for track use
- [ ] Shakedown drive — confirm no rubbing, no weird noises, brakes feel right
- [ ] Top off all fluids
- [ ] Load tools, spares, safety gear for HPDE
- [ ] Final systems check: PDM power-up, telemetry recording, camera, GPS, comms

> **Gate:** Car is mechanically complete and electronically validated for HPDE.

### Mar 27 — HPDE Weekend

**Primary validation goals:**
- [ ] Coilover behavior — ride quality, body roll, bottoming, rebound
- [ ] Brake feel with new pads — bedding procedure, fade characteristics
- [ ] Seat position — head clearance to cage, visibility, harness fit
- [ ] PDM reliability — no spurious faults, fan logic works under heat, fuel pump prime consistent
- [ ] Sensor data under load — oil pressure at temp, coolant pressure, fuel pressure stability
- [ ] SmartyCam video + data overlay quality
- [ ] GPS accuracy and lap timing
- [ ] PodiumConnect live data feed from pit
- [ ] Radio clarity at speed
- [ ] Note any suspension settings to adjust (spring preload, compression/rebound if adjustable)

**Collect a punch list** of everything that needs addressing before the race.

### PHASE D — Haltech Integration (Mar 28 – Apr 6)
*10 days to do this properly. No rush. Follow Phase 3 from `weekend-tasks.md`.*

#### D1: Pre-Integration Prep (Mar 28–29)
- [ ] Review HPDE punch list — fix any mechanical issues first
- [ ] Complete any remaining Phase 0 bench tests (P0.1 knock, P0.3 CAN broadcast)
- [ ] Confirm Haltech base map is loaded and settings are correct in NSP

#### D2: Wiring Cutover (Mar 30 – Apr 1)
This is the point of no return — stock ECU goes offline.

- [ ] Move injector wiring from stock ECU → Haltech INJ1–6
- [ ] Install COP (Toyota 90919-A2005 ×6) — wire triggers to Haltech IGN1–6
- [ ] Move crank/cam from stock ECU → Haltech
- [ ] Move TPS → Haltech AVI 10
- [ ] Disconnect stock ECU power — Haltech ECU now powered from LP1
- [ ] Reconnect IGN switch → Haltech pin 13 + PDM B23
- [ ] Sensor Deutsch connector — **no change needed**, already connected to Haltech AVIs
- [ ] Install MAP sensor (drill/tap plenum) — wire to AVI 9
- [ ] Connect wideband (Innovate LM2) → available Haltech AVI, power from LP5

#### D3: First Fire + Tuning (Apr 2–4)
- [ ] First fire on Haltech — base tune, target stable idle
- [ ] Verify all Phase 1 PDM tests still pass with Haltech running
- [ ] Street drive — confirm drivability, throttle response, shifting
- [ ] Verify CAN0 data flow: Haltech → PDM → Dash (RPM, ECT, oil P, fuel P, TPS)
- [ ] Tune wideband target AFR at idle and light cruise
- [ ] Check for fault codes, sensor drift, CAN errors

#### D4: Validation + Polish (Apr 5–6)
- [ ] Extended drive — heat cycle, confirm fan staging works at real temps
- [ ] Confirm fuel pump prime and run logic under real conditions
- [ ] Verify warning LED triggers at real thresholds
- [ ] Full telemetry chain test: Haltech → PDM → Dash → SmartyCam → GPS → Podium
- [ ] Clean and label harness — zip-tie routing, confirm no chafe on steering/suspension
- [ ] Spare parts and consumables list for race weekend

> **Gate:** Engine runs reliably on Haltech. All PDM logic confirmed. Telemetry chain validated end-to-end. No fault codes.

### PHASE E — Race Prep (Apr 7–9)

#### Apr 7–8: Final Prep
- [ ] Address any remaining punch list items
- [ ] Final fluid check (oil, coolant, brake fluid, fuel)
- [ ] Torque check: wheels, suspension bolts, seat brackets, cage bolts
- [ ] Pack tools, spares, fire bottle, safety gear, pit equipment
- [ ] Charge all batteries (SmartyCam, radio, phone/tablet for PodiumConnect)
- [ ] Export/backup Race Studio config and Haltech NSP tune to USB

#### Apr 9 (Friday): Test Day at Track
- [ ] Validation only — confirm Haltech runs clean under track load
- [ ] Monitor oil pressure/temp, coolant pressure/temp, fuel pressure at sustained RPM
- [ ] Verify telemetry + camera recording for full sessions
- [ ] Final suspension adjustments if needed (this is the last chance)
- [ ] **No major wiring or plumbing changes** — if something is broken, assess whether it's fixable at the track or needs a fallback plan

#### Apr 10: Race
- [ ] Send it

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Coilovers arrive late | Floor, brakes, PDM, sensors, telemetry are all independent — keep working. Worst case: run stock suspension at HPDE, install coilovers post-HPDE. Still get tested at Apr 9 test day. |
| Haltech won't start/idle | Stock ECU is still wired up through HPDE. If Haltech integration fails, reconnect stock ECU for the race. Lose COP and MAP but car runs. Sensor Deutsch connector works either way. |
| PDM fault at HPDE | PDM is connected via spade connectors on fuse box pin 87 — can be disconnected in minutes. Stock fuse box still powers everything. |
| Telemetry CAN bus issue | Each CAN bus is independent (CAN0=Haltech, CAN1=AIM devices, CAN2=Keypad). A failure on one doesn't affect the others. SmartyCam can record standalone video even without CAN data. |
| Sensor thread doesn't fit | Test-fit all sensors before fluids go in. The coolant sensor is M12x1.5 — confirm it fits the tee before committing. |

---

## What Gets Tested Where

| Item | HPDE (Mar 27) | Test Day (Apr 9) | Race (Apr 10) |
|------|:---:|:---:|:---:|
| Coilovers | First track test | Validated | Race |
| Brake pads | Bedding + fade test | Confirmed | Race |
| Seat/floor/brackets | Comfort + safety check | Confirmed | Race |
| PDM power logic | Full test under load | Confirmed | Race |
| Sensor data (fuel/oil/coolant) | Live logging via Haltech passive | Confirmed w/ Haltech active | Race |
| SmartyCam3 Corsa | Video + overlay test | Confirmed | Race |
| GPS + lap timing | Accuracy test | Confirmed | Race |
| PodiumConnect telemetry | Live feed test | Confirmed | Race |
| Radios | Range + clarity test | Confirmed | Race |
| Haltech (engine mgmt) | *Not installed yet* | First track validation | Race |
| COP ignition | *Not installed yet* | With Haltech | Race |
| Wideband AFR | *Not installed yet* | With Haltech | Race |

---

## Summary

**HPDE (Mar 27):** Mechanically complete car (coilovers, brakes, seat) with PDM power management, full telemetry stack, and sensor logging. Stock ECU runs the engine. Test everything except Haltech.

**Post-HPDE (Mar 28 – Apr 8):** Clean Haltech integration with 10+ days and zero pressure. Sensor Deutsch connector means no re-wiring of sensors.

**Test Day (Apr 9):** Haltech validation under track load. No major changes — just confirm and tune.

**Race (Apr 10):** Everything proven.
