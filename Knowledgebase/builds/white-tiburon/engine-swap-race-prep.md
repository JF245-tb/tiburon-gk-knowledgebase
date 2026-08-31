# White Tiburon — Engine Swap + NCM Lemons Race Prep
## Week of Mon Sep 1 → Race weekend Sep 12–13, 2026

**Context:** New short block ready (forged pistons/rods, new rings/lifters/seals, +0.5mm overbore machined). Quaife ATB LSD already installed in the "best" 6-speed Aisin transaxle. HPDE test day **Thursday** on the current (old-engine) setup; 24 Hours of Lemons race at **NCM** two weekends out.

> **Sequencing decision (confirm if wrong):** Keep the old engine in the car for Thursday's HPDE — it's the known-good, proven combo. Pull it Thursday evening/Friday, do the swap over the following weekend, then use the second week as shakedown/buffer before towing to NCM. This avoids debugging a brand-new short block, a freshly assembled LSD trans, a new clutch, a new fuel system, **and** new sway bar geometry all in the same session you're relying on for HPDE data.
>
> **Risk call embedded in this plan:** stay on stock ECU (Phase 1) through the race. Haltech gets fully wired and CAN-linked to the PDM this cycle but stays in shadow/logging mode — full Phase 2 engine control (per `guides/pdm-build-guide.md`) is explicitly a "next weekend" item in `weekend-tasks.md` and shouldn't be pulled forward onto a car carrying this much other new hardware into a race.

---

## Cross-references

| Topic | File |
|---|---|
| PDM/Haltech phase plan, Deutsch connector architecture | `guides/harness-design.md`, `guides/firewall-passthrough.md`, `guides/pdm-build-guide.md` |
| PDM bench/car test procedures | `guides/bench-test.md` |
| Sensor pin/cal tables | `signal-routing.md`, `hardware/sensors/lowdoller-sensors.md` |
| COP coil wiring | `hardware/sensors/cop-ignition.md` |
| Clutch specs/torques | `common/shop-manual/clutch-system/specifications.md` |
| Trans specs/torques | `common/shop-manual/transaxle/specifications.md` |
| Engine mount/transaxle mount torques, engine+trans removal procedure | `common/shop-manual/engine-mechanical/engine-block.md`, `.../specifications.md` |
| Front suspension / sway bar torques | `common/shop-manual/suspension-system/front-suspension.md`, `.../specifications.md` |
| Front stabilizer bar part numbers | `common/parts-catalog/chassis.md` → "FRONT STABILIZER BAR" |

---

## MON–WED — HPDE Prep + Opportunistic Harness/Trigger Work

Old engine stays in, stock ECU drives the car Thursday. Nothing this block should touch anything that has to work Thursday.

### Pre-track checklist
- [ ] Re-check torques from prior suspension/brake work (`weekend-tasks.md` P.1–P.7) — don't redo, just spot-check nothing backed off
- [ ] Fluids, tire pressures, brake pad/rotor check, fresh brake bleed if due
- [ ] PDM/AIM logging confirmed working for HPDE data capture (SmartyCam recording, Podium/RaceCapture, PDM channels) — this is free instrumentation data for evaluating the old engine one last time
- [ ] Pack chase truck/trailer, spares, tools for Thursday

### Haltech trigger + firing test on the old engine (only if time allows)
Per `guides/bench-test.md` / `weekend-tasks.md`: cam ✅, crank ✅, COP fire ✅ already bench-confirmed at some point — knock was still open. Two distinct tests, don't conflate them:

1. **Trigger sync validation (safe to do live, even engine running):** Haltech is already powered (LP1) and CAN-linked in Phase 1. With the stock ECU driving the car normally, watch Haltech NSP for clean crank sync (`RPM` locks) and cam home detection at cranking/idle. D2/D3 (coil/injector Deutsch) are **not plugged in** in Phase 1, so this is zero-risk to the stock ignition — Haltech is just listening.
2. **Firing test (bench only, engine OFF):** Do **not** parallel a Haltech IGN output onto a coil that's still wired to the stock ignition module/harness while the engine can run — you'd have two systems trying to drive the same coil. If you want to confirm a Haltech IGN output actually sparks, pull one spare Toyota 90919-A2005 coil, plug it into a spark tester or a grounded plug, and trigger it off one Haltech IGN1–6 output on the bench/key-on-engine-off. This validates the D2/D3 coil wiring plan without touching anything the HPDE car depends on.

Don't let this test slip the HPDE prep — it's explicitly "if there's time."

---

## THURSDAY — HPDE

Run on the current setup. Log everything (PDM + Haltech shadow data) — this is your last data set on the old bottom end and current sway bar before both change.

---

## THU EVENING / FRI — Pull Old Engine

Budgeted ~2 hrs per past experience. Per `engine-mechanical/engine-block.md` §"Engine and Transaxle Assembly — Removal," the factory procedure drops the **engine + transaxle as one unit** on a jack/T-M fixture after disconnecting driveshafts, subframe bolts, mounts, and all harness/hose/cable connections — not a separate engine-then-trans pull. Plan the new engine's installation the same way (build it as a complete engine+trans+clutch unit first, then install as one assembly) rather than dropping the engine in and mating the trans in the car.

- [ ] Disconnect battery/kill switch first
- [ ] Drain oil, coolant
- [ ] Disconnect all harness connectors, hoses, cables, driveshafts, exhaust per engine-block.md removal sequence
- [ ] Remove engine + transaxle mounting brackets, subframe bolts, roll stoppers
- [ ] Drop assembly as a unit
- [ ] Stage old engine/trans aside (core, spare, or teardown later — not this week's problem)

---

## FRI/SAT — Mate New Engine to Quaife Trans + Clutch (Bench Work, Before It Goes Back In)

Do this on a stand/cherry picker, not in the car — matches how it'll go back in as a unit.

- [ ] Verify short block prep: rings gapped/oriented, bearings clearance-checked, lifters pre-oiled, all new seals (front/rear main, cam, etc.) confirmed installed per machine shop notes, +0.5mm bore verified against the piston/ring set that was matched to it
- [ ] Clutch disc install — use alignment tool (spec tool **09411-25000** clutch disc guide, or equivalent generic alignment shaft) to center the disc before pressure plate goes on
- [ ] Lube per `clutch-system/specifications.md`: CASMOLY L9508 (or equivalent moly grease) on input shaft spline, release bearing bore, release-fork-to-cylinder-pushrod contact point, release bearing/fork fulcrum contact
- [ ] Pressure plate (clutch cover assembly) bolts, torque **15–22 Nm**, star pattern
- [ ] Mate trans case to clutch/bellhousing — **manual transaxle case to clutch housing bolt: 63–67 Nm** (`transaxle/specifications.md`)
- [ ] **Confirm the engine-block-to-bellhousing case bolt torque** in `engine-mechanical/engine-block.md` installation section before final torque — not fully captured in this KB yet, don't guess a number, check the manual page directly
- [ ] Confirm Quaife trans fluid level/spec before it goes back in (or plan to fill after install if easier access)

---

## SAT/SUN — Install Engine+Trans Assembly + Everything Else "While It's Out"

This is the batch of work that only makes sense with the bay wide open. Order matters less than getting all of it done before buttoning up.

### Engine/trans install
- [ ] Reverse of the removal procedure — assembly in as a unit, subframe, mounts, roll stoppers
- [ ] Engine mounting insulator bolt **40–55 Nm**, mounting bracket nut/bolt **60–80 Nm**, support bracket stud **30–40 Nm**
- [ ] Transaxle mounting insulator bolt **90–110 Nm**, transaxle mounting bracket bolt **40–55 Nm**, transaxle mounting plate **10–12 Nm**
- [ ] Reconnect driveshafts — driveshaft nut (2.7L) **200–280 Nm**
- [ ] Reconnect exhaust, reconnect stock engine harness/injectors/coils (Phase 1 — stock ECU still drives ignition/fuel)
- [ ] Refill oil, coolant, trans fluid; check clutch hydraulic bleed (clutch pedal free play spec **6–13 mm**)

### Front sway bar → smallest stock size
Two distinct Hyundai PNs exist in the parts catalog: `54811-2C000` (listed V6+I4 in some ranges) and `54811-2C010` (V6-only in the same date range) — **measure both bars' actual OD before assuming which is smaller**; the KB's shop-manual excerpt only documents one 23mm spec and doesn't disambiguate the two PNs by diameter. Don't install on part-number naming alone.

- [ ] Remove stabilizer link nuts (**30–45 Nm** install spec) and bracket bolts (**30–45 Nm** install spec) on old bar
- [ ] Swap in smaller bar, same bushing/bracket hardware unless bar OD differs enough to need different bushings
- [ ] Set link length at ride height using the same zero-preload procedure already used on the rear bar (`weekend-tasks.md` P.1): measure center-to-center at ride height, set adjustable end links to that length so links sit vertical with no preload
- [ ] Torque: stabilizer link nut **35–45 Nm**, bracket bolt **30–45 Nm**
- [ ] Flag for post-swap alignment check — shouldn't move camber/toe, but confirm

### Fuel system — 6AN PTFE + Radium FPR + quick disconnects
- [ ] Install Radium FPR/damper on fuel rail
- [ ] Run new 6AN PTFE supply and return lines
- [ ] Add inline quick-disconnect fittings at the engine/chassis interface (recommend exactly 2: supply and return, both at a fixed point like the firewall or subframe crossmember) — this is new scope beyond what's documented in the KB; it mirrors the Deutsch-connector philosophy already used for the electrical harness (`harness-design.md`) — pick disconnects rated for fuel/EFI pressure, not generic AN quick-connects
- [ ] Cut return line, install line tap + Lowdoller fuel pressure/temp sensor (PN 899404) per existing plan (`weekend-tasks.md` SU.3) if not already done
- [ ] Pressure test / leak check before first start — this is a fresh fuel system on a fresh engine, don't skip it

### PDM harness — finalize
Whatever's left open from `weekend-tasks.md` Sunday tasks:
- [ ] Oil, coolant, fuel Lowdoller sensors installed and reading (AVI 1–6)
- [ ] MAP sensor installed, vacuum line connected
- [ ] All sensor commons wired (+5V bus, signal GND bus)
- [ ] Haltech CAN1 ↔ PDM (B30/B31) verified — CAN_V2_40 traffic visible in Race Studio Live Data
- [ ] D4 8-pin Deutsch (all 3 Lowdoller sensors) built and connected

### Haltech harness — start the hard-to-reach parts now, leave disconnected
Per `harness-design.md`, build order SU.9: build D1 (12-pin: cam/crank/knock/IAT/MAP/TPS) and the D2/D3 bank harnesses (coil+injector triggers, 8-pin each) now while the bay is open, since this is exactly the access window the harness was designed around ("pull 4 connectors + 2 grounds + starter = engine is free" only works if D1–D4 exist).
- [ ] D1 — chassis-side 12-wire cable + engine-side pigtails to cam/crank/knock/IAT/MAP/TPS, terminate both ends
- [ ] D2/D3 — chassis-side cables (IGN + INJ triggers, MP1/MP2 power branches) + engine-side pigtails to the 6 coil connectors + 6 injector connectors, ground ring terminals to head bolts — **build and route, do not plug in.** Coil/injector power runs stay coiled & capped per `firewall-passthrough.md` Phase 1 spec
- [ ] MP1/MP2 splice points prepped (3-way and 2-way) but not connected

### First start on stock ECU ("sleep the stock ECU running this weekend")
- [ ] Prime oil pressure before first crank (disable ignition/fuel, crank in short bursts until oil pressure shows) — verify via the now-wired Lowdoller oil pressure sensor in Haltech NSP even though Haltech isn't driving anything yet
- [ ] First start, check for fuel/coolant/oil leaks immediately
- [ ] Confirm stock ECU idle/operation normal, no fault codes
- [ ] Short heat cycle, re-check for leaks after thermal expansion
- [ ] Verify Haltech NSP is reading live sensor data in shadow mode (oil P/T, coolant P/T, fuel P/T, MAP, CAN traffic to PDM) even though it isn't controlling the engine

---

## WEEK OF SEP 7–11 — Shakedown Before NCM

- [ ] Short break-in drives — vary RPM/load per fresh ring break-in practice, avoid extended idle
- [ ] Re-check/re-torque anything conventionally re-torqued after first heat cycle (confirm with machine shop's build sheet if they specified anything — head fasteners, etc.)
- [ ] Send oil sample for analysis after break-in (Blackstone — see `oil-analysis/` for prior baseline reports)
- [ ] Chase any leaks (fuel AN fittings especially — new system, new fittings)
- [ ] Continue Haltech harness work as time allows — still not a race-week Phase 2 switchover
- [ ] Post-sway-bar-swap alignment check
- [ ] Standard Lemons tech/safety prep, pack trailer

## SEP 12–13 — 24 Hours of Lemons @ NCM

Car runs the race on stock ECU + PDM (proven config), new engine/trans/clutch/sway bar/fuel system all shaken down for a week beforehand, Haltech fully wired and CAN-linked in shadow/logging mode for real race data ahead of the Phase 2 switchover later.

---

## Open items to resolve before/during the swap

1. **Front sway bar diameter** — confirm which PN (`54811-2C000` vs `54811-2C010`) is actually smaller by measuring, not by trim-level assumption.
2. **Engine-to-bellhousing case bolt torque** — not yet captured in this KB; pull from the physical manual's engine-block install section before final assembly.
3. **Quick-disconnect fitting spec** (brand/size) for the AN fuel lines — not yet documented anywhere in the KB; once chosen, worth adding to `builds/white-tiburon/build-profile.md` fuel system section for future swaps.
