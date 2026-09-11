# White Tiburon — Pre-Start Oil Pressure Check (Crank-Only, Minimum Config)
## New engine, intake manifold off, spark plugs out

**Car:** White Tiburon
**Engine management:** Stock OE ECU (not needed for this test), no Haltech
**Instruments:** Mechanical gauge in the **oil pressure switch port** + Lowdoller sensor in the **oil cooler sandwich plate**

> **This is a crank-only test, not a first start.** With the intake manifold off the engine cannot run, and it must not get the chance.
>
> Plugs out is the right call — no compression means fast cranking, low starter load, and the pump comes up to speed quickly.

---

## The minimum configuration

Using a remote starter, **you need essentially no vehicle electrical system.** The starter is the only thing that has to be energized, and a remote starter energizes it directly at the solenoid. That means the minimum setup is also the safest one: nothing else is powered, so nothing else can fire.

### What must be connected

| # | Item | Why |
|---|---|---|
| 1 | Battery → kill switch → 150A breaker → **starter B+** (2 AWG) | The only power path the test needs |
| 2 | Battery negative → chassis, **and engine block → chassis ground strap** | Starter current returns through the engine ground. Easiest bulletproof version: a jumper cable straight from battery negative to a clean spot on the block |
| 3 | **Remote starter** across solenoid B+ → S | Cranks it |
| 4 | Engine full of break-in oil, **pre-filled filter**, pan sealed, drain plug in | The thing being tested |
| 5 | **Mechanical gauge** in the oil pressure switch port | Primary instrument |
| 6 | **Lowdoller sensor** in the sandwich plate, powered and read (see below) | *Optional.* Secondary instrument + sensor validation |

**The mechanical gauge alone is a complete test.** Items 1–5 are the go/no-go. The Lowdoller is worth the five minutes it takes to read it with a multimeter — it's the sensor that will be reporting oil pressure at 6000 rpm at the track, and this is a free chance to confirm it works before you depend on it — but a missing or unwired sensor is no reason to delay the test.

### What you do NOT need connected

Ignition switch or IGN toggle · OE ECU · ECU/main relay · fuel pump relay (**pull it**) · PDM (unless you want it logging) · injectors · coils · cluster · fuel system · cooling system · alternator · Haltech · anything on the intake side.

**Cooling system:** crank-only, no combustion, no heat — you don't need coolant in it. Leaving it empty also means the disconnected throttle body coolant hoses aren't dribbling on the floor.

---

## Why minimum is also safest — and the 30 seconds of insurance worth spending

With the ignition never switched on, the ECU has no switched power, so it cannot open an injector or charge a coil, and the fuel pump relay never gets energized. The risk this test needs to manage — fuel or spark near open intake ports on a fresh engine — is designed out rather than managed.

Still do these two things, because they cost almost nothing and they protect against the one realistic failure mode (somebody reaches in and flips the IGN toggle "just to see the dash"):

- [ ] **Pull the OE fuel pump relay** and set it on the bench where you'll see it. Per `fuel-system/general.md`, the ECM energizes that relay **while the engine is cranking** — with a stock ECU and that relay in place, cranking runs the pump.
- [ ] **Leave the ECU (main / MFI control) relay position dead** — OE relay out, PDM replacement output disconnected or disabled.

---

## The two gauges will not agree. That is expected.

This matters more than it sounds, because the instinct will be to "fix" the disagreement by adjusting the Lowdoller calibration. Don't.

The two sensors are in **different places in the oil circuit**:

- The **oil pressure switch port** reads the main gallery — downstream of the filter.
- The **sandwich plate** sits at the filter mount, and depending on how that particular plate is ported internally it may read the **pump side, upstream of the filter**, or the filtered side.

If the plate picks up pre-filter pressure, it will read **higher** than the gallery gauge, and the gap is the pressure drop across the filter. That gap **widens when the oil is cold and thick** — which is exactly the condition you'll be testing in, with 20W-50 at shop temperature. A 5–15 psi spread while cranking cold would be unremarkable.

**Use them as two independent answers to "is there oil pressure," not as a calibration reference for each other.** If you want to calibrate the Lowdoller against the mechanical gauge properly, do it later with both sensors reading the *same* port, or at hot idle where the filter delta is small and stable.

What you're actually looking for from the pair:
- **Both read something** → the pump is picking up and the circuit is pressurized. This is the go/no-go.
- **Gallery gauge reads, sandwich plate doesn't** → suspect the sensor, its port, or its wiring — not the engine.
- **Sandwich plate reads, gallery gauge doesn't** → that's more interesting, and worth stopping for. It can mean the filter or the cooler circuit isn't passing oil through to the gallery.

---

## What pressure am I looking for?

**There is no factory cranking spec, and you shouldn't go looking for a number.** What you're reading is a *behavior*: pressure rises, then holds steady for as long as you crank, and does the same thing on the next burst.

### While cranking (cold, plugs out, 20W-50, gauge in the gallery port)

| Reading | Verdict |
|---|---|
| Comes up and holds steady, repeatable burst to burst | **Pass.** Commonly 20–40+ psi, but the steadiness matters more than the value |
| Low but rock-steady (say 10–15 psi) | **Not a failure.** Cranking is ~200–300 rpm — the pump is barely turning. Judge it at idle, not here |
| Needle erratic, fluctuating, won't settle | **Investigate.** Classic sign of the pickup drawing air — tube O-ring or gasket |
| Builds, then decays while still cranking | **Investigate.** Don't proceed |
| Nothing after ~30 seconds cumulative | **Stop cranking.** Work the causes in step 4 below |

Cold thick oil can also push the pump against its **relief valve**, so a high cold number isn't a fault. The KB does not record the G6BA relief valve pressure setting, so there's no threshold here to compare against.

### The numbers that actually matter come later

This test is cold, with no combustion, so **it cannot validate the running spec** — it only answers "does the oiling system work." Check these once it runs:

| Figure | Value | What it is |
|---|---|---|
| **G6BA factory minimum** | **≥ 50 kPa (7.3 psi)** at 75–90 °C oil temp | A pass/fail **floor**, not a health target. An engine sitting near this hot is in trouble, not in spec |
| GK **I4** book figure, for scale | 166 kPa (24.5 psi) at hot idle, 90–100 °C | Different engine — not a G6BA spec — but a realistic picture of what a healthy hot idle looks like |
| Common racer rule of thumb | ~10 psi per 1000 rpm, hot | Useful shape. At 6000+ rpm that's ~60 psi hot |

For a race weekend, **hot pressure at sustained high rpm is the number that matters**, not cranking and not cold idle. Cold idle on a fresh engine with 20W-50 will read high — that tells you very little.

---

## The oil cooler changes the timeline

The sandwich plate and cooler add volume — the plate, both lines, and the cooler core all have to fill before gallery pressure stabilizes. On a dry new build with cold thick oil, **expect pressure to take noticeably longer to come up than it would without the cooler.** Don't read a slow build as a failed pump in the first few seconds.

- **Pre-fill the cooler and lines** if you can get oil into them before assembly. This is the single biggest thing you can do to shorten the anxious part.
- If the sandwich plate is **thermostatic**, it will likely bypass the cooler while cold — less volume to fill, faster pressure. Worth knowing which type you have so you can predict the behavior instead of interpreting it live.
- The plate and cooler lines are **brand-new joints that have never seen pressure**, and they sit at full oil pressure. This test is their leak check too — that's a real bonus of doing it now rather than at first start.

---

## Reading the Lowdoller without wiring up the PDM

You do not need the PDM powered, configured, or even installed to get a number out of this sensor. Minimum version:

1. Feed the sensor's **red** wire 5 V from any bench supply — a lab supply, a USB breakout, a 5 V regulator off the battery.
2. Tie the **black** (pressure ground) to that supply's ground.
3. Put a multimeter on the **yellow** (pressure signal) wire, referenced to the same ground.
4. Convert: **PSI = (V − 0.5) × 37.5**. So 0.5 V = 0 psi, 2.0 V = 56 psi, 4.5 V = 150 psi.

That's the whole thing, and it sidesteps the entire PDM channel-assignment and calibration question for today.

**If you'd rather have it logged on the PDM**, the wiring is: red → **B16** (+5 V analog Vref), yellow → an analog-capable channel input, black → **B18 (GND)** — *not* B13/B14, which are P GND and carry output current. Calibration in RS3 is the same `(V − 0.5) × 37.5`. Note this means powering the PDM, which asserts IGN — so the fuel pump relay and ECU relay steps above stop being optional.

> The temp element (green/white) is PTC *resistive* and likely needs a pull-up the PDM may not provide — irrelevant today, since pressure is what you're testing. Detail in the build notes.

---

## Before test day — verify these fit

Cheap to check now, expensive to discover with the engine ready to crank:

- [ ] **Mechanical gauge adapter matches the oil pressure switch port thread.** The factory switch comes out with a 24 mm deep socket, but the KB does not record the port's thread spec — confirm against the physical part, not a parts-store guess.
- [ ] **Sandwich plate thread matches the OEM filter mount**, and the filter still seats fully on the plate.
- [ ] Gauge line long enough to route away from the belt and pulleys, and to be read from where you're standing.

---

## Pre-crank checklist

### A. Oiling system
- [ ] Crankcase filled with break-in oil (Valvoline VR1 20W-50, or conventional Rotella T4 15W-40 — per `engine-swap-race-prep.md`)
- [ ] Oil filter **pre-filled** and torqued **12–16 Nm (9–12 lb·ft)**, gasket oiled, old gasket confirmed gone from the mount
- [ ] Sandwich plate installed, center bolt/adapter tight, both gasket faces seated; cooler lines tight
- [ ] Cooler and lines pre-filled if possible
- [ ] Oil drain plug **35–45 Nm**; lower oil pan bolts **10–12 Nm** in the numbered sequence
- [ ] Mechanical gauge in the switch port, sealant on the threads (**3M ATD No. 8660 or ThreeBond 1141E**), snug — don't overtighten into an aluminum port
- [ ] **OEM oil pressure switch wire insulated and tied back** — the switch is out, and a live wire dangling near the block is a short waiting to happen
- [ ] Lowdoller sensor in the sandwich plate, wired per whichever method above

### B. Openings and rotation
- [ ] Intake ports covered — clean foam plugs or lint-free rags, **counted and written down** so the same number comes back out
- [ ] Brake booster port, PCV, and any other open fittings capped
- [ ] Spark plug holes left open (intentional), rag draped over to catch oil mist
- [ ] **Engine turns freely by hand** — at least two full revolutions on the crank bolt before the starter touches it
- [ ] Nothing loose near the belt, pulleys, or flywheel; gauge line routed clear

### C. Drivetrain and safety
- [ ] Transaxle in **neutral**, confirmed by hand at the shifter
- [ ] Wheels chocked, parking brake set, car on the ground or proper stands
- [ ] Fire extinguisher within reach

### D. Electrical — the short list
- [ ] Battery charged, charger or jump pack on it
- [ ] **Engine-to-chassis ground strap connected** (or jumper cable direct to the block) — most common post-swap no-crank cause
- [ ] Kill switch ON, 150A breaker closed, starter B+ cable tight (terminal nut **10–12 Nm**)
- [ ] Starter bolted up, bolts torqued
- [ ] PDM HP1 ring terminal off the solenoid S post if it's already landed there
- [ ] **Fuel pump relay pulled; ECU relay position dead**
- [ ] Remote starter leads insulated and long enough to keep your hands clear of the belt

---

## Procedure

1. **Pre-prime first if you have a pre-luber.** Pressurizing through the switch port before cranking fills the galleries, the filter, the plate and the cooler with zero starter wear, gets oil to fresh bearings before they rotate under load, and leak-checks the new plate and cooler joints statically. On a new short block with an added cooler circuit, this is worth real effort to arrange.
2. **Crank in 10–15 second bursts, 30–60 seconds rest.** Starters have a duty cycle.
3. **Watch the mechanical gauge.** Pressure should appear within roughly 5–15 seconds of cranking — allow extra time for the cooler circuit to fill. See "What pressure am I looking for?" above for how to read it; the short version is that steady and repeatable beats any particular number.
4. **If nothing shows after ~30 seconds of total cranking, stop.** Don't keep cranking a dry engine. Check in order: gauge and the port it's in, oil pump not primed at assembly, pickup tube gasket or O-ring drawing air, sandwich plate or cooler circuit not passing oil, oil level.
5. **With pressure up, leak-check everything** — and pay particular attention to the sandwich plate faces, the cooler line fittings, and the cooler itself, since those are the joints with no history. Then the filter, pan rails, drain plug, and gauge fitting.
6. **Note both readings and the spread between them.** Write it down. That spread, at a known oil temperature, is useful reference data later.
7. **Re-check oil level** — the filter, plate, lines and cooler have all taken their share, and on a cooler-equipped engine that's a meaningful amount.
8. **Restore:** fuel pump relay back in, ECU relay feed restored, HP1 ring terminal back on, every intake port plug removed and **counted out**, then the manifold — **intake manifold to cylinder head 19–21 Nm**, surge tank to manifold 15–20 Nm, spark plugs 20–30 Nm.
9. **Decide what lives in the switch port.** If the mechanical gauge stays, the OEM low-oil-pressure cluster lamp is gone for good — worth a deliberate decision rather than a default, on a car that races.

---

## Notes

- Keep this crank-only. The temptation after a good reading is to "just see if it fires" — it can't, the manifold is off, and fuel near open ports on a fresh engine is how a good day ends badly.
- Fuel washing cylinder walls is the other reason the pump stays dead: unburned fuel on fresh bores is bad for ring seating, independent of the fire risk.
- The oil cooler and sandwich plate are not yet recorded in `build-profile.md` — worth adding once the plumbing is final.

---

*Created: 2026-09-11*
*Sources: `common/shop-manual/engine-mechanical/lubrication-system.md` (EMA-55–58), `.../engine-block.md` (filter torque), `.../specifications.md`, `common/shop-manual/fuel-system/general.md`, `hardware/aim/aim-pdm/pdm-pinout.md`, `hardware/sensors/lowdoller-sensors.md`*
