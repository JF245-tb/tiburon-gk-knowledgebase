# Tune Change Request — Safe Endurance Calibration, 2.7L V6 SIMK43

**Purpose:** A change spec to hand to the tuners who did the original calibration. They have
the map definitions; this says what to change, by how much, why, and what to leave alone.
**Target:** Stock Siemens SIMK43, GKFlasher-flashable, 2.7L V6 Delta (G6BA).
**Use case:** 24 Hours of Lemons endurance racing, on a freshly rebuilt short block.

> **Fill in before sending.** Everything in *italics* is a blank only you or the tuners can
> fill. Most importantly the **ECU fingerprint** — without it they can't load the right
> definitions.

---

## 1. Car and ECU identification

Run this and paste the output into the request:

```bash
python3 scripts/verify-ecu-stock.py <your-dump>.bin
```

| Field | Value |
|---|---|
| ECU description (`ca6…`) | *fill from fingerprint* |
| Calibration (`G…`) | *fill from fingerprint* |
| Hardware revision (`5WY…`) | *fill from fingerprint* |
| ECU family / EEPROM size | *2 mbit 256 KiB or 4 mbit 512 KiB* |
| Baseline dump attached | *filename + date* |
| Currently stock or tuned? | *from the verification diff* |

**Attach the as-found dump.** They should work from the actual file in the car, not a
generic base.

---

## 2. What changed mechanically

This is the context they need to judge timing and fueling — not a request in itself.

| Item | Detail |
|---|---|
| Short block | **New** — forged pistons and rods, new rings, lifters, seals |
| Overbore | **+0.5 mm** (86.7 → 87.2 mm). 2,656 → ~2,687 cc, **+1.16 %** |
| Compression ratio | **Unknown — need the build sheet.** Stock is 10.0:1; forged piston dish volume may have moved it |
| Cams | *stock unless changed* |
| Valve springs | *stock unless changed* — OEM is 45 lb seat, 100–105 lb @ 8 mm lift |
| Ignition | Wasted spark, 3 coils (stock) |
| Intake / MAF | *unchanged on white; blue has a cold air intake* |
| Exhaust | Aftermarket headers, non-equal-length |
| Cats | *present / removed — affects the ignition-cut decision* |
| Fuel | *pump octane you'll actually run at the track* |
| Engine age | ~2 weeks, one HPDE break-in session |

**On the overbore specifically:** we are *not* asking for a displacement-based fuel rescale.
SIMK43 here is MAF-based — ignition maps are axed on `maf_hb`, there's an `id_maf_tab`, the
car has a hot-film MAF and no MAP sensor. The ECU meters from measured air mass, so +1.16 %
displacement is self-correcting, and it sits below injector variation and MAF tolerance
anyway. Flagging the bore only because it may have moved CR, which *is* a timing input.

---

## 3. Requested changes

Priority order. Items 1 and 4 are the ones that matter; 2 and 3 are optional.

### 3.1 Rev limiter — **primary request**

| Map | Current | Requested |
|---|---|---|
| `c_n_max` (ignition cut) | *read from cal* | **6,300 rpm** |
| `c_n_max_max` (fuel cut) | *read from cal* | **6,500 rpm** |
| `c_n_max_hys` | *read from cal* | ~150–200 rpm |
| `c_n_max_hys_max` | *read from cal* | ~150–200 rpm |

Keep `c_n_max` **below** `c_n_max_max` so ignition cut is the soft limiter and fuel cut is the
hard backstop. Hysteresis wide enough that the limiter doesn't oscillate.

**Why this costs nothing in lap time:** rated power is **181 hp @ 6,000 rpm**. The engine is
already past peak power at 6,000, so the RPM between 6,300 and stock limit is doing no useful
work. Post-shift landing points with the Aisin 6-speed at a 6,300 shift:

| Shift | Lands at |
|---|---|
| 2→3 | ~4,290 rpm |
| 3→4 | ~4,650 rpm |
| 4→5 | ~5,060 rpm |
| 5→6 | ~5,090 rpm |

All comfortably above the 4,000 rpm torque peak. *(Gear ratios are flagged unverified in our
notes — worth the tuners sanity-checking against real Aisin data.)*

**Why we want it lower:**
- Fresh rings and bearings with minimal break-in mileage
- Stock valve springs are modest (45 lb seat) — valve float risk at sustained high RPM
- **Interference engine** — a timing belt or valvetrain failure bends valves
- Known G6BA tendency toward oil consumption under sustained high RPM/load, and no factory
  oil cooler
- A 16-hour race is thousands of shifts; the limiter *will* get hit

**If cats are still fitted,** confirm ignition cut is acceptable — dumping unburnt fuel into a
live cat is hard on it. If that's a concern, bias more toward fuel cut.

### 3.2 WOT enrichment — *optional*

| Map | Request |
|---|---|
| `ip_ti_fl__n__amp` | Target **12.2–12.5:1 AFR (λ 0.83–0.85)** at WOT above ~4,500 rpm |

If the calibration is already in that band, leave it alone.

**Do not go richer than about 11.8:1.** Two real costs: bore wash on fresh rings and fuel
dilution in the oil (our Blackstone reports already show measurable fuel %), and range — a
60 L tank in an endurance race means enrichment converts directly into extra pit stops.

### 3.3 Full-load threshold — *optional, lowest priority*

| Map | Request |
|---|---|
| `id_tps_fl__n` | Consider lowering modestly so sustained high load enters open-loop enrichment sooner |

Only if the tuners think closed loop lingers too long under sustained load. Same fuel-range
tradeoff as above. **Happy to skip this one.**

### 3.4 Ignition timing — **safety margin**

| Map | Request |
|---|---|
| `ip_iga_bas__n_32__maf_hb` | **−2°** in high-load / high-RPM cells only |
| `ip_iga_ref__n_32__maf_hb` | Same treatment, kept consistent |

Scope it to roughly **above 4,000 rpm and upper-load cells**, tapering to **zero change** at
low load. **Do not touch idle, cruise, or light load** — that hurts driveability and economy
and raises EGT for no benefit.

**Why:** final CR is unknown after the rebuild, track fuel octane is uncertain, and endurance
means sustained heat with no oil cooler. −2° is cheap insurance.

**Two constraints:**
- **Leave knock control enabled.** The G6BA has a knock sensor on the block and its retard
  strategy is a genuine safety net. This request is belt-and-braces on top of it, not a
  replacement.
- Don't overdo retard — later burn raises EGT, which brings its own problems.

---

## 4. Explicitly do not change

| Map | Why |
|---|---|
| `id_maf_tab` | MAF and intake are unchanged on the white car. The overbore does **not** justify a MAF rescale — the sensor measures actual airflow. Touching this without a MAF/intake change just de-calibrates the fueling. *(Blue car's cold air intake is a separate conversation.)* |
| `ip_iga_dif_min_bas` | CVVT high/low blending. **Base G6BA has no VVT** — not applicable to this engine. |
| Program zone | Calibration-zone changes only. No program/firmware writes. |

---

## 5. Questions for the tuners

1. **Do you have definitions for our exact calibration?** (fingerprint in §1) If not, what do
   you need from us — a full dump?
2. **What are the current `c_n_max` / `c_n_max_max` values?** We'd like to know the stock
   limiter before changing it.
3. **Is knock retard loggable** on this ECU? GKFlasher's datalogger exposes 14 parameters and
   none of them are knock, ignition advance, or fuel trims — so we can't verify timing safety
   with our own tooling. How would you want us to validate?
4. **Is the cooling fan on-temp adjustable** in the calibration? Lowering it would help in
   endurance. It isn't in the public map list.
5. **Confirm MAF vs MAP** for our calibration. Our notes say SIMK43 is MAF-based on most GK
   variants but MAP-based on some; the sensor list and map axes say MAF for ours, but you'd
   know for certain.
6. **Can you return it as a calibration-zone-only file** with checksums corrected?
7. Anything you'd add for endurance that we haven't asked about?

---

## 6. Acceptance checks when the file comes back

Before flashing anything, verify the returned file changed **only** what was agreed:

```bash
# checksums must pass on the returned file
python3 scripts/verify-ecu-stock.py tuner-return.bin

# diff the returned file against our own as-found dump
python3 scripts/verify-ecu-stock.py tuner-return.bin -r <our-as-found>.bin
```

- [ ] All region checksums report **OK**
- [ ] Fingerprint unchanged (same description / calibration / hardware rev)
- [ ] Diff shows changes confined to the **calibration zone** — any program-zone difference
      is a red flag, go back and ask
- [ ] Number and size of changed runs is consistent with the maps we asked for
- [ ] Our as-found baseline is archived somewhere durable before anything is written

Then flash **calibration only**, on a charger, not at a track:

```bash
python3 gkflasher.py -p kline -i /dev/ttyUSB0 --flash-calibration tuner-return.bin
python3 gkflasher.py -p kline -i /dev/ttyUSB0 --clear-adaptive-values
```

Full procedure and cautions: `common/opengk/ecu-factory-verification.md`.

---

## 7. Validation plan

1. **Bench or driveway first** — start, idle, confirm no new DTCs (`--read-dtcs`).
2. **Confirm the limiter lands where expected** in a safe place, in a low gear, before a
   session. This is the one change with an unambiguous observable.
3. **Log a session** with the Haltech in shadow mode — it has the knock sensors and the
   Innovate LM2 wideband, and it's a far better instrument than GKFlasher's logger.
4. **Check AFR under sustained load**, not just a single pull. Endurance failures come from
   heat soak over a stint.
5. **Oil analysis at the next change** — watch fuel dilution if enrichment went up.

> **Do this on a spare ECU first if you have a verified-stock one.** Then the car's known-good
> ECU stays untouched and swappable if anything misbehaves.

---

## 8. Caveats on this document

- Requested values are **starting points for discussion**, not prescriptions. The tuners can
  see the actual maps; we can't.
- We don't know the stock limiter values, the current WOT AFR target, or the post-rebuild CR.
  Those three would sharpen every number above.
- Our gear ratios are marked unverified in our own notes.
- Nothing here should be flashed on a race weekend. See
  `builds/ecu-verification-and-tune-plan.md`.

---

## Related

| Topic | File |
|---|---|
| Verify a dump / check a returned file | `common/opengk/ecu-factory-verification.md` |
| GKFlasher CLI reference | `common/opengk/gkflasher.md` |
| Map names | `common/opengk/map-definitions.md` |
| Engine specs, racing notes | `common/chassis/gk-chassis-specs.md` |
| Valve spring specs | `common/opengk/valvetrain.md` |
| Engine build and race sequencing | `builds/white-tiburon/engine-swap-race-prep.md` |
| Race-weekend plan | `builds/ecu-verification-and-tune-plan.md` |
