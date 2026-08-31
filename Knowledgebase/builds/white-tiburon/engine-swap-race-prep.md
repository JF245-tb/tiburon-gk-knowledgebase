# White Tiburon — Engine Swap + NCM Lemons Race Prep
## New engine goes in BEFORE Thursday's HPDE — HPDE = break-in + shakedown

**Context:** New short block ready (forged pistons/rods, new rings/lifters/seals, +0.5mm overbore machined). Quaife ATB LSD already installed in the "best" 6-speed Aisin transaxle. Old engine comes out **today (Monday)**, new engine goes in this week, and Thursday's HPDE is being used deliberately as the break-in and shakedown session for the new bottom end, clutch, and trans. Lemons race at **NCM** in two weeks (Sep 12–13).

> **What this means for sequencing:** you have ~3 days (Mon–Wed) to pull the old engine, mate the new one to the Quaife trans + clutch, install it, get fluids/fuel sorted, and put break-in miles on it before Thursday. That's tight. The plan below is ordered so that if something slips, it's the nice-to-have work that slips — not "car runs safely and doesn't leak" on Thursday morning.
>
> **Risk carried into Thursday, eyes open:** a brand-new short block, freshly assembled Quaife trans, and new clutch all get their first real load cycles at an HPDE only ~3 days after assembly, with minimal break-in mileage banked beforehand. That's the explicit point of using the HPDE this way — just don't also stack "new AN fuel system with fittings that haven't been leak-checked" or "new sway bar geometry nobody's driven" onto that same first session if Mon–Wed runs long. Push whichever of those slips to the weekend after.
>
> **Risk call held from before:** stay on stock ECU (Phase 1) through Thursday and through the race. Haltech gets wired and CAN-linked to the PDM this week but stays in shadow/logging mode — useful for watching oil pressure, coolant temp, and AFR live during Thursday's break-in without adding a second untested variable (new ECU control) on top of the new engine.

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

## Priority order for Mon–Wed (in case time runs short)

1. **Old engine out, new engine+Quaife trans+clutch mated and installed, running, no leaks.** Non-negotiable — this is the whole point of the week.
2. **Break-in time on the engine before Thursday** — even a couple hours of idle/light-load driveway/street time matters more than any bolt-on.
3. **Fuel system reconnected and leak-checked** — doesn't have to be the new AN system yet. If the 6AN PTFE + Radium FPR + quick-disconnect work isn't going to be done and pressure-tested in time, reconnect stock lines for Thursday and do the AN conversion this weekend instead. A rushed, untested fuel fitting is not a Thursday-morning risk worth taking.
4. **Front sway bar swap** — do it if the engine work goes smoothly; if not, it can wait for the weekend without touching Thursday.
5. **PDM harness finalization / starting the Haltech D1–D3 harness in hard-to-reach spots** — genuinely lowest priority this week. It's disconnected either way (Phase 1), so nothing breaks if it's incomplete for Thursday. Do it if there's slack, otherwise it's the first thing pushed to the weekend.

---

## MONDAY — Pull Old Engine, Mate New Engine to Trans + Clutch

### First thing, before the old engine comes out (15–30 min if there's time)
Haltech trigger sync check on the **old** engine, since this is the last chance:
- Haltech is already powered (LP1) and CAN-linked in Phase 1; D2/D3 (coil/injector Deutsch) are **not** plugged in, so this is zero-risk to the stock ignition.
- Crank the engine (or bump the starter) and watch Haltech NSP for clean crank sync (`RPM` reads) and cam home detection.
- Don't attempt an actual firing test on the car — that requires a Haltech IGN output driving a coil, and you don't want two systems both wired to try to fire the same coil. If you want to confirm a coil fires off a Haltech output, do it on the bench with a spare coil, separately, whenever there's downtime — it doesn't need to happen today.
- **Don't let this eat into engine-pull time.** Skip it without guilt if the morning is tight.

### Pull old engine (~2 hrs, per past experience)
Per `engine-mechanical/engine-block.md` §"Engine and Transaxle Assembly — Removal," the factory procedure drops the **engine + transaxle as one unit** after disconnecting driveshafts, subframe bolts, mounts, and all harness/hose/cable connections — not engine-then-trans separately.

- [ ] Disconnect battery/kill switch first
- [ ] Drain oil, coolant
- [ ] Disconnect all harness connectors, hoses, cables, driveshafts, exhaust
- [ ] Remove engine + transaxle mounting brackets, subframe bolts, roll stoppers
- [ ] Drop assembly as a unit, stage old engine/trans aside

### Mate new engine to Quaife trans + clutch (bench work, same day)
Build this as a complete unit before it goes back in — matches how the old one came out.

- [ ] Verify short block prep: rings gapped/oriented, bearing clearances checked, lifters pre-oiled, all new seals confirmed, +0.5mm bore verified against the matched piston/ring set
- [ ] Clutch disc install — use alignment tool (**09411-25000** clutch disc guide or equivalent) to center the disc before the pressure plate goes on
- [ ] Lube per `clutch-system/specifications.md`: CASMOLY L9508 (or equivalent moly grease) on input shaft spline, release bearing bore, release-fork-to-pushrod contact, release bearing/fork fulcrum
- [ ] Pressure plate (clutch cover assembly) bolts, torque **15–22 Nm**, star pattern
- [ ] Mate trans case to clutch/bellhousing — **manual transaxle case to clutch housing bolt: 63–67 Nm**
- [ ] **Confirm engine-block-to-bellhousing case bolt torque** directly from the physical shop manual's engine-block install section — not fully captured in this KB yet, don't guess a number
- [ ] Confirm Quaife trans fluid spec/level before it goes back in (or plan to fill after install)

**Goal by end of Monday:** engine+trans+clutch assembled as a unit, ready to go in Tuesday morning. If the pull + mate goes fast, start the install Monday evening.

---

## TUESDAY — Install + First Start

### Install engine+trans assembly
- [ ] Reverse of Monday's removal — assembly in as a unit, subframe, mounts, roll stoppers
- [ ] Engine mounting insulator bolt **40–55 Nm**, mounting bracket nut/bolt **60–80 Nm**, support bracket stud **30–40 Nm**
- [ ] Transaxle mounting insulator bolt **90–110 Nm**, transaxle mounting bracket bolt **40–55 Nm**, transaxle mounting plate **10–12 Nm**
- [ ] Reconnect driveshafts — driveshaft nut (2.7L) **200–280 Nm**
- [ ] Reconnect exhaust, reconnect stock engine harness/injectors/coils (Phase 1 — stock ECU drives ignition/fuel)
- [ ] Refill oil, coolant, trans fluid; bleed clutch hydraulics, check clutch pedal free play (**6–13 mm** spec)

### Fuel system — reconnect (AN conversion if it fits, stock lines if it doesn't)
- [ ] **If time allows:** install Radium FPR/damper, run 6AN PTFE supply/return, add quick-disconnect fittings at the engine/chassis interface (2 points — supply and return — rated for fuel/EFI pressure), install fuel line tap + Lowdoller fuel sensor. **Pressure test and leak-check before first start** — non-negotiable on a fresh engine.
- [ ] **If time is short:** reconnect stock fuel lines, confirm no leaks, defer the AN/FPR/quick-disconnect work to this weekend.

### First start (if ready by end of day)
- [ ] Prime oil pressure before first crank (disable ignition/fuel, crank in short bursts until oil pressure shows)
- [ ] First start, immediate leak check (fuel, coolant, oil)
- [ ] Confirm stock ECU idle/operation normal, no fault codes
- [ ] Begin banking break-in time — idle and light load only at this stage

---

## WEDNESDAY — Break-In Miles + Final HPDE Prep

- [ ] If first start didn't happen Tuesday, do it first thing today — this is the last day to bank any break-in time before Thursday
- [ ] Short heat cycles, re-check for leaks after thermal expansion, re-check any torques disturbed by heat
- [ ] Front sway bar swap, **if not already done and if Mon/Tue went smoothly** — see procedure below
- [ ] PDM/Haltech harness work, **only if there's real slack left** — see procedure below
- [ ] Final HPDE prep: fluid levels, tire pressures, brake check, PDM/AIM logging confirmed working (SmartyCam, Podium, PDM channels) so Thursday's break-in data actually gets captured
- [ ] Pack trailer/tools/spares

### Front sway bar → smallest stock size (when there's time)
Two distinct Hyundai PNs exist in the parts catalog: `54811-2C000` and `54811-2C010` — **measure both bars' actual OD before assuming which is smaller**; the KB's shop-manual excerpt only documents one 23mm spec and doesn't disambiguate the two PNs by diameter.

- [ ] Remove stabilizer link nuts (**30–45 Nm** spec) and bracket bolts (**30–45 Nm** spec)
- [ ] Swap in smaller bar
- [ ] Set link length at ride height using the same zero-preload procedure used on the rear bar (`weekend-tasks.md` P.1): measure center-to-center at ride height, set adjustable end links to that length, links vertical, no preload
- [ ] Torque: stabilizer link nut **35–45 Nm**, bracket bolt **30–45 Nm**
- [ ] Flag for alignment check — shouldn't move camber/toe, but confirm before or after Thursday

### PDM harness / Haltech harness (when there's time)
- [ ] PDM: Lowdoller sensors (oil/coolant/fuel) installed and reading, MAP sensor in, sensor common buses wired, Haltech CAN1 ↔ PDM (B30/B31) verified in Race Studio Live Data
- [ ] Haltech: start D1 (12-pin: cam/crank/knock/IAT/MAP/TPS) and D2/D3 (coil/injector bank harnesses) per `harness-design.md` — build and route, **do not plug in**. Coil/injector power runs stay coiled & capped per `firewall-passthrough.md` Phase 1 spec.
- [ ] Whatever doesn't get finished rolls to the weekend without affecting Thursday — Haltech stays disconnected from engine control either way

---

## THURSDAY — HPDE = Break-In + Shakedown

Treat it as a break-in session first, a test day second:
- [ ] Vary RPM/load through the day per fresh-ring break-in practice — avoid long steady-state high-RPM stints in the first sessions
- [ ] Watch Haltech NSP (shadow mode) and PDM logging for oil pressure, coolant temp, AFR (once wideband's live), and CAN traffic — this is the troubleshooting opportunity, use it
- [ ] Between sessions: check for leaks (especially any fuel fittings touched this week), check oil level/condition, listen for anything new from the clutch or driveline
- [ ] Note anything to fix before the weekend build-out continues

---

## FRI–SUN (Sep 5–6 weekend) — Catch-Up + "Sleep the Stock ECU"

Everything deferred from Mon–Wed, plus addressing whatever Thursday surfaced. Stock ECU stays the one actually running the car — Haltech mounted alongside, wired, CAN-linked, but dormant on engine control.

- [ ] Finish AN fuel line conversion + Radium FPR + quick disconnects if not done pre-Thursday (pressure test before trusting it)
- [ ] Finish front sway bar swap if not done pre-Thursday
- [ ] Finish PDM harness (all Lowdoller sensors reading, CAN1 Haltech↔PDM confirmed, D4 8-pin Deutsch built)
- [ ] Continue/finish D1/D2/D3 Haltech harness build — still leave D2/D3 unplugged
- [ ] Address any Thursday findings (leaks, clutch adjustment, sway bar balance, noises)
- [ ] Oil change after initial break-in miles; send a sample for analysis (see `oil-analysis/` for prior Blackstone baseline)

---

## WEEK OF SEP 7–11 — Final Shakedown

- [ ] Continued break-in / shakedown drives
- [ ] Re-check/re-torque anything conventionally re-torqued after the first heat cycles
- [ ] Chase any remaining leaks, especially new AN fittings
- [ ] Post-sway-bar alignment check
- [ ] No Phase 2 Haltech engine-control switchover before the race — stays a post-race item
- [ ] Standard Lemons tech/safety prep, pack trailer

## SEP 12–13 — 24 Hours of Lemons @ NCM

Car races on stock ECU + PDM with a week-plus of break-in and shakedown behind the new engine/trans/clutch (and sway bar/fuel system if they made it in), Haltech fully wired and CAN-linked in shadow/logging mode for real race data ahead of the Phase 2 switchover later.

---

## Open items to resolve before/during the swap

1. **Front sway bar diameter** — confirm which PN (`54811-2C000` vs `54811-2C010`) is actually smaller by measuring, not by trim-level assumption.
2. **Engine-to-bellhousing case bolt torque** — not yet captured in this KB; pull from the physical manual's engine-block install section before final assembly.
3. **Quick-disconnect fitting spec** (brand/size) for the AN fuel lines — not yet documented anywhere in the KB; once chosen, worth adding to `builds/white-tiburon/build-profile.md` fuel system section for future swaps.
4. **Break-in procedure specifics** — if the machine shop or ring manufacturer gave a specific break-in protocol (RPM ranges, duration, re-torque schedule) with this build, it isn't captured in the KB — follow their sheet over the generic guidance above if it exists.
