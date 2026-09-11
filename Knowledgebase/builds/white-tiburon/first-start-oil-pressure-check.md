# White Tiburon — Pre-Start Oil Pressure Check (Crank-Only)
## New engine, intake manifold off, spark plugs out

**Car:** White Tiburon
**Config for this test:** **Stock OE ECU** running the engine, stock relay box retained, **no Haltech**. AIM PDM 32 replaces the OE ECU (MFI control / main) relay and reads Lowdoller sensors only.

> **This is a crank-only test, not a first start.** With the intake manifold off the engine cannot run, and it must not get the chance. The goal is: confirm the new short block builds and holds oil pressure, and confirm nothing leaks under pressure.
>
> Plugs out is the right call — no compression means fast cranking, low starter load, and the oil pump comes up to speed quickly.

---

## Current configuration (supersedes the Haltech-based routing elsewhere in this build folder)

| Item | This test |
|---|---|
| Engine management | **Stock OE ECU**, everything stock |
| Haltech Elite 2500 | **Not used** — not in the loop at all |
| PDM role | Replaces the OE **ECU (MFI control / main) relay**; reads Lowdoller sensors |
| PDM sensors | Oil temp/pressure, fuel temp/pressure, trans temp/pressure, tire temp |
| Fuel pump relay | **Stock, in the relay box, ECM-driven** |

> ⚠️ **`signal-routing.md` does not describe this configuration.** It routes every Lowdoller sensor to a Haltech AVI with +5V from Haltech 34-pin pin 9. In this build the sensors go to **PDM channel inputs** with +5V from **PDM B16**. Treat the AVI tables in that file as not applicable until it's updated.

---

## Relays: what to pull, and what the PDM now owns

On a stock GK these are two separate relays, and both matter here:

| Relay | Feeds | Controlled by | Status in this build |
|---|---|---|---|
| **Main / MFI control / EGI main relay** ("ECU relay") | ECU switched power, **injectors, coils**, O2 heaters, MAF, purge solenoid, ISA | ECM main relay control (pin 67 / 23 depending on ECU variant) | **Being replaced by the PDM output** |
| **Fuel pump relay** | In-tank fuel pump | ECM fuel pump relay output (pin 69 / 10) | **Still stock in the relay box** |

**The fuel pump one is the one people forget.** Per `fuel-system/general.md`, the ECM "turns the fuel pump relay ON so that current is supplied to the fuel pump **while the engine is cranking** or running." With a stock ECU and a stock fuel pump relay, cranking runs the pump. On a fresh engine with the manifold off, that is exactly what you don't want.

### For this test

- [ ] **Pull the OE fuel pump relay** out of the relay box and set it on the bench where you'll see it. No pump, no rail pressure, nothing to squirt.
- [ ] **Leave the ECU relay position dead** — OE relay out, and the PDM output that replaces it either not yet connected or disabled in Race Studio 3. With no switched power at that socket, the ECU cannot power an injector or charge a coil no matter what it decides to do with its ground-side drivers.
- [ ] **Verify with a meter, don't trust the plan:** 0 V at the injector rail power feed and at the coil power feed, with everything switched on.

That gives you two independent layers (no fuel, no ignition/injector power) on a test where the cost of being wrong is a washed-down fresh bore or a fire near open intake ports.

> **Note on the ECU itself:** the ECU keeps a permanent B+ feed for memory regardless. That's fine and expected — it's the *switched* feed through the main relay that drives the coils and injectors, and that's the one you're keeping dead.

---

## Cranking it: use a remote starter

Use a **remote starter across the starter solenoid B+ and S terminals**. Two reasons:

1. **It's independent of however the start circuit is currently wired.** The OEM ignition cylinder was removed from this car and start moved to a momentary button; depending on where the PDM install currently stands, that button may route through PDM Ch01 → HP1 → solenoid S, or back through the OE starter relay. A remote starter at the solenoid works either way and doesn't depend on an interlock you'd have to go verify first.
2. **It puts you at the engine.** You want to be standing over the gauge and the open ports while it spins, not in the driver's seat.

If the PDM's HP1 output is already landed on the solenoid S post, **pull that ring terminal off for the duration of the test** and reinstall it after. One nut, and it removes any question of back-feeding the PDM output.

**Do not crank with fuel or ignition live just because the remote starter feels isolated** — it isn't. The remote starter only controls the starter. The fuel pump relay and ECU relay work above are what make the test safe, and they're required regardless of how you spin the engine.

---

## Oil pressure reading — use a mechanical gauge as the primary

The Lowdoller 899404 on a PDM channel has never seen a known pressure on this engine, and the channel calibration is new. Do not let an unvalidated sensor be the only thing telling you whether a fresh short block has oil pressure.

- **Mechanical gauge = truth.** Thread it into the oil pressure switch / sender port.
- **PDM channel = cross-check**, and this test is the free opportunity to validate the calibration against real numbers. Log both and compare.
- **OEM oil pressure switch → cluster lamp = a third, independent indicator.** Lamp extinguishes at **20–40 kPa (2.9–5.8 psi)** per `lubrication-system.md`. Crude, but free.
- If the block has one 1/8" NPT port and the Lowdoller is in it, **tee it** so gauge and sensor both read — or run the mechanical gauge alone for this test and validate the sensor afterward.
- Sender/switch thread sealant: **3M ATD No. 8660 or ThreeBond 1141E**, torque **15–22 Nm (11–16 lb·ft)**. Keep sealant out of the port.

### Wiring the oil sensor to the PDM

| Lowdoller 899404 wire | Goes to | Note |
|---|---|---|
| Red (+5V) | **PDM B16** (+5V Analog Vreference) | Not Haltech pin 9 — that's the old plan |
| Yellow (pressure signal) | A PDM **analog-capable** channel input | 0.5–4.5 V ratiometric — native fit for a 0–5 V input |
| Black (pressure GND) | **PDM B18 (GND)** | **Not** B13/B14 — those are P GND and carry output current |
| Green (temp signal) | Analog channel input | See the pull-up caveat below |
| White (temp GND) | **PDM B18 (GND)** | Same |

Race Studio 3 calibration for the pressure element: **PSI = (V − 0.5) × 37.5**, range 0–150 PSI.

> **Ground the sensors to B18, not to the P GND pins.** Power-ground pins carry output current, and the voltage drop across them offsets every ratiometric reading referenced to them. This is the most common cause of "the gauge reads different when the fan kicks on."

---

## Two constraints worth knowing before you finish the sensor install

Neither blocks this test, but both bite later, and the wiring decisions get made now.

**1. The PTC temp elements may not read without a pull-up.** The Lowdoller pressure elements output 0.5–4.5 V and drop straight onto an analog input. The **temp** elements are PTC *resistive* — they need a pull-up to form a divider and produce a voltage. Haltech AVIs have configurable internal pull-ups, which is what the old plan relied on. The PDM 32 docs in this KB describe its channel inputs as **0–5 V / 0–12 V or digital** and say nothing about a resistive or pull-up mode. Before you count on oil/fuel/trans temp reading: confirm in Race Studio 3 whether those inputs offer a pull-up, and if not, plan on an external pull-up resistor to the B16 5 V rail per temp channel. **Oil pressure is unaffected — it works as-is, so this test is fine.**

**2. You are going to run out of PDM inputs.** Per `pdm-configuration-guide.md`, of the PDM 32's 12 channel inputs only **8 are analog-capable** (the other 4 are digital-only), plus 2 speed inputs.

- Your sensor list is **7 analog signals** — oil P, oil T, fuel P, fuel T, trans P, trans T, tire temp. That fits the 8 analog channels with exactly **one to spare**.
- That leaves **1 analog + 4 digital = 5 inputs** for the switch panel, which `build-profile.md` lists as **10 switches** (start, fan low, fan high, headlights, wiper low, wiper high, brake, coolsuit, defogger, horn).
- Five inputs, ten switches. Something has to give: a CAN keypad (config already preserved in `guides/keypad-config-future.md`) frees channel inputs, or some loads go back to conventional relays, or some sensors get dropped.

Also: **the KB doesn't record which specific channel numbers are the analog-capable 8.** Confirm that from the PDM32 user guide before assigning pins — discovering it after the harness is built and loomed is an expensive way to learn it.

> Two smaller doc discrepancies noticed while checking this, worth correcting when the routing docs get updated: `signal-routing.md` lists Ch11/Ch12 at B26/B27, but the pinout has Ch11 = **A26** and Ch12 = **A27** (B26/B27 are Ch01/Ch02). And the pinout's "12 channel inputs" vs. the configuration guide's "8 analog + 4 digital" are the same 12 — the 8/4 split is the one that constrains the build.

---

## Pre-crank checklist

### A. Mechanical — oiling system
- [ ] Oil filter installed and **pre-filled** with break-in oil
- [ ] Crankcase filled to full with break-in oil (Valvoline VR1 20W-50, or conventional Rotella T4 15W-40 — per `engine-swap-race-prep.md`)
- [ ] Oil drain plug torqued **35–45 Nm**; magnetic plug if fitted
- [ ] Lower oil pan bolts torqued **10–12 Nm** in the manual's numbered sequence; pickup screen already inspected for assembly debris
- [ ] Oil pressure switch / sender installed with sealant, **15–22 Nm** — and confirm the port is a live gallery port
- [ ] Mechanical gauge fitted, fitting tight
- [ ] Oil filter bracket and any cooler lines torqued and leak-free

### B. Mechanical — openings and rotation
- [ ] Intake ports covered — clean foam plugs or lint-free rags, **counted and written down** so the same number comes back out
- [ ] Throttle body coolant hoses capped (they're off with the manifold) — or leave the cooling system empty, since this is crank-only
- [ ] Brake booster vacuum port, PCV, and any other open fittings capped so nothing falls in
- [ ] Spark plug holes left open (intentional), rag draped over to catch oil mist
- [ ] Engine turns freely by hand — at least two full revolutions on the crank bolt before the starter ever touches it
- [ ] Nothing loose on or near the belt, pulleys, or flywheel

### C. Drivetrain safety
- [ ] Transaxle in **neutral**, confirmed by hand at the shifter
- [ ] Wheels chocked, parking brake set
- [ ] Car on the ground or on proper stands — not on a jack
- [ ] Fire extinguisher within reach

### D. Electrical — required to crank
- [ ] Battery fully charged, with a charger or jump pack on it (repeated cranking drains fast)
- [ ] **Engine-to-chassis ground strap connected** — the single most common post-swap no-crank / slow-crank cause; starter current returns through it
- [ ] Battery negative to chassis, clean and tight
- [ ] Kill switch ON, all 4 poles; 150A breaker closed; 2 AWG to starter B+ intact
- [ ] Starter motor bolted to the bellhousing, bolts torqued
- [ ] Starter B+ terminal nut **10–12 Nm**; S-terminal connection clean
- [ ] PDM HP1 ring terminal **removed** from the solenoid S post if it's already landed there (reinstall after)
- [ ] Remote starter leads in hand, insulated, and long enough to stand clear of the belt

### E. Electrical — must be dead before cranking
- [ ] **OE fuel pump relay pulled** from the relay box
- [ ] **ECU (main / MFI control) relay position dead** — OE relay out, PDM replacement output disconnected or disabled in Race Studio 3
- [ ] **Meter-verified: 0 V at the injector rail feed and the coil power feed** with everything switched on. Verify it; don't infer it
- [ ] Fuel lines connected and dry-checked, or capped at both ends — no open fuel lines near an engine you're about to spin

### F. Electrical — needed for the reading to be worth anything
- [ ] PDM powered: Surlok (+) via the 120A breaker; grounds landed
- [ ] PDM **IGN input B23** asserted so the PDM is awake and logging
- [ ] Lowdoller oil sensor wired per the table above — **+5V from B16, signal grounds to B18**
- [ ] Oil pressure channel calibrated in Race Studio 3: `PSI = (V − 0.5) × 37.5`
- [ ] Logging armed **before** the first crank — this trace is your baseline for every later reading

---

## Procedure

1. **Pre-prime before cranking, if you have a pre-luber.** Pressurizing the galleries through the oil pressure switch port fills the system and lets you leak-check with zero starter wear, and it gets oil to fresh bearings before they rotate under load. Strongly preferred on a new short block. Without one, cranking is acceptable — plugs are out, load is light.
2. **Crank in 10–15 second bursts, 30–60 seconds rest between.** Starters have a duty cycle, and a cooked starter on a car that needs to move is a bad trade.
3. **Watch the mechanical gauge.** Cold 20W-50, no compression: expect pressure within roughly 5–15 seconds of cranking, reading well above idle spec — commonly 20–40+ psi while cranking. The factory figure of **50 kPa (7.3 psi) minimum applies at hot idle, 75–90 °C oil temp** — a floor for a running engine, not a cranking target.
4. **If nothing shows after ~30 seconds of total cranking, stop.** Don't keep cranking a dry engine. Check, in order: gauge/sender and the port it's in (easiest and most common), oil pump not primed at assembly, pickup tube gasket or O-ring drawing air, filter or bypass issue, oil level.
5. **While pressure is up, leak-check** the filter, filter bracket, pan rails, drain plug, sender and gauge fittings, and any cooler lines.
6. **Compare the PDM channel against the mechanical gauge** and trim the calibration now, while you have a known reference on the same port.
7. **Re-check oil level after cranking** — the filter and galleries have taken their share.
8. **Restore:** reinstall the HP1 ring terminal, reinstall the fuel pump relay, restore the ECU relay feed, remove and **count out** every intake port plug, then reinstall the manifold — **intake manifold to cylinder head 19–21 Nm**, surge tank to manifold 15–20 Nm, spark plugs 20–30 Nm.
9. **Expect stored DTCs.** Cranking with the manifold off means MAF, IAT, TPS and ISA are all disconnected — the ECU will log codes and light the CEL. Normal. Clear them once everything is back together, and don't let them mask a real code later.

---

## Notes

- Keep this crank-only. The temptation after a good pressure reading is to "just see if it fires" — it can't, the manifold is off, and putting fuel anywhere near open ports on a fresh engine is how a good day ends badly.
- Fuel washing cylinder walls is the other reason the pump stays dead: unburned fuel on fresh bores is actively bad for ring seating, independent of the fire risk.
- Log the cranking oil pressure trace. It becomes the baseline every later reading gets compared against.

---

*Created: 2026-09-11*
*Sources: `hardware/aim/aim-pdm/pdm-pinout.md`, `hardware/aim/aim-pdm/pdm-configuration-guide.md`, `common/shop-manual/engine-mechanical/lubrication-system.md` (EMA-55–58), `.../specifications.md`, `common/shop-manual/fuel-system/general.md`, `common/opengk/ecm-pinouts.md`*
