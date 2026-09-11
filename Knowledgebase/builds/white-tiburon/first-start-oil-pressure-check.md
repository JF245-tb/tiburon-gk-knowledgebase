# White Tiburon — Pre-Start Oil Pressure Check (Crank-Only)
## New engine, intake manifold off, spark plugs out

**Car:** White Tiburon | **Config:** Phase 1 — stock ECU for engine control, AIM PDM 32 for power distribution, Haltech Elite 2500 powered in shadow/logging mode

> **This is a crank-only test, not a first start.** With the intake manifold off the engine cannot run, and it must not be allowed to try. The goal is: confirm the new short block builds and holds oil pressure, confirm nothing leaks under pressure, and (bonus) confirm the Haltech sees clean crank/cam sync on the new engine before anything fires.
>
> Plugs out is the right call — no compression means fast cranking, low starter load, and the oil pump gets to speed quickly.

---

## Cross-references

| Topic | File |
|---|---|
| Swap sequencing, break-in oil, pan/pickup inspection | `engine-swap-race-prep.md` |
| PDM Phase 1 fuse box taps, output map | `guides/pdm-build-guide.md` §"Phase 1 — PDM + Stock ECU" |
| Oil pressure sensor pins, +5V bus, CKP/CMP pins | `signal-routing.md` |
| Oil pump / pressure switch specs and torques | `common/shop-manual/engine-mechanical/lubrication-system.md` |
| Engine oil pressure spec, sealants, torques | `common/shop-manual/engine-mechanical/specifications.md` |
| Starter system, solenoid, starter relay | `common/shop-manual/_archive/engine-electrical.md` §"Starting System" |

---

## Relays vs. remote starter — what actually applies to this car

The usual "pull the fuel pump and ignition relays" trick assumes an OEM relay box. **On this car those relays are already out.** Per `guides/pdm-build-guide.md` §S.6, Phase 1 install pulled the OE main relay and the OE fuel pump relay and dropped PDM spade wires into their pin 87 sockets:

| OEM relay | Replaced by | What it feeds |
|---|---|---|
| Main relay (pin 87 socket) | **PDM MP1 (B2) + MP2 (B3)**, trigger `SafeIgnition` | Stock ECU switched power → injectors, coils, O2 heaters |
| Fuel pump relay (pin 87 socket) | **PDM HP3 (B24+B25)**, trigger 3s prime OR RPM > 50 | In-tank fuel pump |
| Starter | **PDM HP1 (B1+B13)** direct to solenoid S-terminal, trigger `Ch01 AND IGN AND NOT RPM` | Starter solenoid |

So the equivalent of "pull the relays" here is: **pull the MP1/MP2 spades out of the main relay pin 87 socket, and pull the HP3 spade out of the fuel pump relay pin 87 socket.** Same effect, same non-destructive reversibility. Disabling those outputs in Race Studio works too, but a physically removed spade can't be undone by a config you forgot you loaded.

Note the starter interlock: `STARTER_SAFE = Ch01 AND IGN AND NOT RPM`. The PDM start button **requires IGN on**, and IGN on is also what asserts `SafeIgnition` — the same variable that powers MP1/MP2. You cannot use the PDM start button while `SafeIgnition` is de-asserted, which is exactly why the spades (not the toggle) are the lever here.

### Recommended: remote starter, IGN on, MP1/MP2 + HP3 spades pulled

This combination gives full fuel/ignition isolation *and* a live instrument readout:

- **Remote starter at the solenoid** — cranks independent of the PDM logic chain, and lets you stand at the engine watching the gauge and the open ports instead of reaching for a dash button.
- **IGN toggle ON** — powers the Haltech (LP1), dash (LP2), cluster (LP6) and PDM logging, so oil pressure on AVI 3, RPM, and CAN traffic are all live and recorded.
- **MP1/MP2 spades out** — stock ECU has no switched power at all. No injector can open, no coil can charge. This is a hard electrical disconnect, not a software inhibit.
- **HP3 spade out** — fuel pump cannot prime, so the rail never sees pressure even if something else went wrong.
- Haltech D2/D3 (coil/injector Deutsch) stay unplugged per Phase 1, so the Haltech has no path to fire anything either.

> **Remote starter and HP1:** HP1 has an internal series diode, which should block current from a remote starter back-feeding into the PDM output. Don't rely on it — pull the HP1 ring terminal off the solenoid S post for the duration of the test and reinstall it after. One nut, removes all doubt.

**Why not the PDM start button alone?** It works, but it forces `SafeIgnition` active, which means the only thing standing between a fresh engine and a squirt of fuel into open intake ports is the spade you pulled anyway. If you're pulling the spades either way, the remote starter is simply less to go wrong and puts you where you can see the engine.

**Why not remote starter with IGN off?** Cleanest isolation of all — nothing but the starter is energized — but the Haltech, dash, and cluster are all dead, so you get no electronic oil pressure reading and no log. Only choose this if you're running a mechanical gauge and nothing else.

---

## Use a mechanical gauge as the primary reading

The Lowdoller 899404 on AVI 3 has never been validated against a known pressure on this engine. Do not let a brand-new, uncalibrated sensor channel be the only thing telling you whether a fresh short block has oil pressure — that's the one measurement you cannot afford to get wrong.

- **Mechanical gauge = truth.** Thread it into the oil pressure switch / sender port.
- **Haltech AVI 3 = cross-check.** This test is also the free opportunity to validate the sensor calibration (`PSI = (V − 0.5) × 37.5`) against real numbers. Log both, compare.
- **OEM oil pressure switch → cluster lamp = third cheap indicator.** Lamp extinguishes at **20–40 kPa (2.9–5.8 psi)** per `lubrication-system.md`. Crude, but it's free and it's independent.
- If the block has only one 1/8" NPT port and the Lowdoller sensor is in it, **tee the port** so the mechanical gauge and the sensor both read. If you'd rather not tee on a fresh build, run the mechanical gauge alone for this test and validate the Lowdoller afterward.
- Sealant on the pressure switch / sender threads: **3M ATD No. 8660 or ThreeBond 1141E**. Torque **15–22 Nm (11–16 lb·ft)**. Don't let sealant get into the port.

---

## Pre-crank checklist

### A. Mechanical — oiling system
- [ ] Oil filter installed and **pre-filled** with break-in oil
- [ ] Crankcase filled to full with break-in oil (Valvoline VR1 20W-50, or Rotella T4 15W-40 conventional — per `engine-swap-race-prep.md`)
- [ ] Oil drain plug torqued **35–45 Nm**; magnetic plug if fitted
- [ ] Lower oil pan bolts torqued **10–12 Nm** in the manual's numbered sequence; pickup screen already inspected for assembly debris
- [ ] Oil pressure switch / sender installed with sealant, **15–22 Nm** — and confirm the port you used is a live gallery port
- [ ] Mechanical gauge fitted and its fitting tight
- [ ] Oil filter bracket, cooler lines (if any) torqued and leak-free

### B. Mechanical — openings and rotation
- [ ] Intake ports covered — clean foam plugs or lint-free rags, **counted and written down** so the same number comes back out
- [ ] Throttle body coolant hoses capped (they're disconnected with the manifold off) — or leave the cooling system empty, since this is crank-only
- [ ] Brake booster vacuum port, PCV, and any other open fittings capped so nothing falls in
- [ ] Spark plug holes left open (intentional) with a rag draped over to catch oil mist
- [ ] Engine can turn freely by hand, at least two full revolutions on the crank bolt, before the starter ever touches it
- [ ] Nothing loose on or near the belt, pulleys, or flywheel

### C. Drivetrain safety
- [ ] Transaxle in **neutral**, confirmed by hand at the shifter
- [ ] Wheels chocked, parking brake set
- [ ] Car on the ground or properly supported on stands — not on a jack
- [ ] Fire extinguisher within reach (no fuel or spark in this test, but the rule doesn't change)

### D. Electrical — required to crank
- [ ] Battery fully charged; charger or jump pack on it (repeated cranking drains fast)
- [ ] **Engine-to-chassis ground strap connected** — the single most common post-swap no-crank/slow-crank cause. Starter current returns through this
- [ ] Battery negative to chassis, clean and tight
- [ ] Kill switch ON, all 4 poles
- [ ] 150A breaker closed; 2 AWG kill switch → starter B+ / alternator B+ intact
- [ ] Starter motor bolted to the bellhousing, bolts torqued
- [ ] Starter B+ terminal nut **10–12 Nm**; S-terminal connection clean
- [ ] HP1 ring terminal **removed** from the solenoid S post if using a remote starter (reinstall after)
- [ ] 120A breaker → PDM Surlok (+) closed; PDM grounds G13/G14/G18 to chassis

### E. Electrical — must be dead before cranking
- [ ] **MP1 (B2) + MP2 (B3) spades pulled** from the OE main relay pin 87 socket → stock ECU, injectors, coils unpowered
- [ ] **HP3 (B24+B25) spade pulled** from the OE fuel pump relay pin 87 socket → fuel pump cannot run
- [ ] Haltech **D2/D3 unplugged** (Phase 1 default — verify, don't assume)
- [ ] Confirm with a meter at the injector rail and coil power bus: **0V with IGN on**. Verify it, don't trust the spade
- [ ] Fuel lines connected and dry-checked, or capped — if the AN conversion isn't finished, cap both ends rather than leaving open lines near an engine you're about to spin

### F. Electrical — needed for the reading to be worth anything
- [ ] IGN toggle ON → PDM `SafeIgnition` active, LP1/LP2/LP6 up
- [ ] Haltech powered: 26-pin pin 11 (LP1), IGN enable 34-pin pin 13, grounds 34-pin pins 10 + 11
- [ ] Lowdoller oil sensor wired: pressure → **34-pin pin 17** (AVI 3, O/R), temp → **34-pin pin 2** (AVI 4, O/Y), +5V red → **34-pin pin 9**, black/white grounds → **26-pin pins 14/15/16**
- [ ] CKP wired: **26-pin pin 1** (Trig+, Y shielded) / **26-pin pin 5** (−, G)
- [ ] CMP wired: **26-pin pin 2** (Home+, Y shielded) / **26-pin pin 6** (−, G)
- [ ] Haltech CAN1 → PDM B30/B31 connected; AIM dash on LP2 showing live data
- [ ] Race Studio / Haltech NSP logging armed **before** the first crank — this data is worth having

---

## Procedure

1. **Pre-prime before cranking, if you have a pre-luber.** Pressurizing the galleries through the oil pressure switch port fills the system and lets you leak-check without any starter wear, and gets oil to fresh bearings before they ever rotate under load. Strongly preferred on a new short block. If you don't have one, cranking is acceptable — the plugs are out and the load is light.
2. **Crank in 10–15 second bursts, 30–60 seconds rest between.** Starters have a duty cycle; a cooked starter on a car that needs to move is a bad trade.
3. **Watch the mechanical gauge.** With cold 20W-50 and no compression, expect pressure to come up within roughly 5–15 seconds of cranking, and to read well above idle spec — commonly 20–40+ psi while cranking. The factory figure of **50 kPa (7.3 psi) minimum applies at hot idle, 75–90 °C oil temp** — treat it as a floor for a running engine, not a cranking target.
4. **If nothing shows after ~30 seconds of total cranking, stop.** Do not keep cranking a dry engine. Check, in order: gauge/sender and the port it's in (easiest and most common), oil pump not primed on assembly, pickup tube gasket or O-ring leaking air, filter or bypass issue, oil level.
5. **While pressure is up, leak-check** the filter, filter bracket, pan rails, drain plug, sender/gauge fittings, and any cooler lines.
6. **Bonus — verify Haltech trigger sync on the new engine.** This is the check the swap plan wanted on the old engine. Watch NSP for a clean, stable `RPM` reading and cam home detection while cranking. Zero risk with D2/D3 unplugged, and it's far better to find a trigger problem now than during first start.
7. **Re-check oil level after cranking** — the filter and galleries have taken their share.
8. **Restore:** reinstall HP1 to the solenoid S post, reinsert MP1/MP2 and HP3 spades, remove and count out every intake port plug, then reinstall the manifold — **intake manifold to cylinder head 19–21 Nm**, surge tank to manifold 15–20 Nm, spark plugs 20–30 Nm.

---

## Notes

- Keep this crank-only. The temptation after a good pressure reading is to "just see if it fires" — it can't, the manifold is off, and putting fuel anywhere near open ports on a fresh engine is how a good day ends badly.
- Fuel washing cylinder walls on a new build is the other reason the fuel pump stays dead here: unburned fuel on fresh bores is actively bad for ring seating, independent of the fire risk.
- Log the cranking oil pressure trace. It becomes the baseline every later reading gets compared against.

---

*Created: 2026-09-11*
*Sources: `guides/pdm-build-guide.md` Phase 1 §S.6, `signal-routing.md`, `common/shop-manual/engine-mechanical/lubrication-system.md` (EMA-55–58), `.../specifications.md`, `common/shop-manual/_archive/engine-electrical.md`*
