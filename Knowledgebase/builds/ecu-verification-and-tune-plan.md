# Race Weekend — GKFlasher Verification, ECU Dumps, and the Tune Question

**Scope:** Both Tiburons, both on stock Siemens SIMK43 (white car held at Phase 1 per
`white-tiburon/engine-swap-race-prep.md`). Track laptop, NCM Lemons weekend.
**Context:** White car has a fresh short block — forged pistons/rods, **+0.5 mm overbore**,
roughly two weeks and one HPDE old.

---

## The short answer on tuning

**Don't flash a modified calibration this weekend.** Two independent reasons, both verified
against the tooling rather than assumed:

1. **The overbore does not need a tune change.** SIMK43 is MAF-based. It meters fuel from
   *measured* air mass, so +1.2 % displacement is self-correcting. Math in
   [§3](#3-the-overbore-question).
2. **You have no tool that can make a targeted edit.** GKFlasher has no map editor and no
   definition file exists publicly. Details in [§4](#4-what-a-safe-tune-would-actually-take).

Parts 1 and 2 below — verifying the install and dumping both ECUs — are genuinely worth
doing and carry almost no risk. That is the work for this weekend. Section 4 covers what a
rev-limit change would really involve if you still want it, as a project for after the race.

---

## 1. Verify the GKFlasher install — do this before you need it

Do all of this **at the hotel or at home, not in the paddock.** Every step here works with no
car attached.

### 1.1 Assume no usable internet at the track

This is the step people skip. Pre-stage everything offline:

- [ ] GKFlasher installed and launching
- [ ] **Reference bins downloaded** for whatever calibrations the two cars turn out to run.
      You will not know which until you dump them, so grab the whole GK-27 directory — it is
      40 files and they are small. `file-repository.md` has the layout.
- [ ] `scripts/verify-ecu-stock.py` copied to the laptop (pure Python, no dependencies)
- [ ] This repo cloned locally

```bash
# grab the whole GK-27 reference set while you still have bandwidth
mkdir -p ~/gk27-reference && cd ~/gk27-reference
# (filenames listed at https://opengk.org/files/?dir=EEPROMS/Siemens/GK-27)
```

### 1.2 Install checks

```bash
python3 -V                      # 3.11.x per the wiki guide
cd GKFlasher && git log -1      # know which version you're on
python3 -m pip install -r requirements.txt
python3 gkflasher.py --help     # argparse loads = deps are satisfied
```

Current upstream is **v1.0.99**. If your laptop copy is much older, updating is a
*pre-weekend* activity, not a paddock one — a fresh `git pull` that breaks a dependency at
the track is exactly the failure you don't want.

### 1.3 Adapter check

- [ ] Adapter enumerates: `ls /dev/ttyUSB*` (Linux) or Device Manager → COM port (Windows)
- [ ] Note the exact port name — it goes in `-i`
- [ ] Confirm the chipset. FTDI preferred; **CH340 works since v1.0.5** but is *not*
      supported for BSL, which is the recovery path if a flash ever goes wrong
- [ ] Pack a spare adapter and a spare USB cable if you have them

### 1.4 Offline dry run — proves the whole toolchain without a car

Run the verification path end-to-end against a downloaded factory bin. If this works, the
only untested variable left at the track is the physical connection.

```bash
# fingerprint + checksum audit on a known-good reference
python3 scripts/verify-ecu-stock.py ~/gk27-reference/ca652051_G3N7TS0H_*.bin

# expect: all three regions OK, fingerprint matching the filename
```

- [ ] Laptop charged, and a way to charge it in the paddock
- [ ] Practise the whole sequence once so you are not reading docs with a hot car waiting

---

## 2. Pull and verify both ECUs

Reading is **read-only and safe**. Nothing in this section writes to an ECU.

### 2.1 Connection notes specific to these cars

- 2.7 V6 routes K-Line through the **BCM** (`BCM-IM` pin 19) — the BCM must be powered, not
  just the ECU. See `common/opengk/k-line.md`.
- **Blue car has no ignition switch** (start button conversion). Power the ECU and BCM
  through whatever replaces it before expecting comms.
- Ignition **ON, engine not running**.
- A full read over K-Line at 10400 baud is slow. Don't start one five minutes before a
  session.

### 2.2 Per car

```bash
# identify first — cheap, and tells you which reference bin you need
python3 gkflasher.py -p kline -i /dev/ttyUSB0 --id

# full dump (256 KiB or 512 KiB depending on ECU family)
python3 gkflasher.py -p kline -i /dev/ttyUSB0 --read -o white-2026-09-12-asfound.bin
python3 gkflasher.py -p kline -i /dev/ttyUSB0 --read -o blue-2026-09-12-asfound.bin
```

Use `--read` (full), not `--read-calibration`. Partial reads pad with `0xFF` and produce
spurious diffs against a full reference.

### 2.3 Verify

```bash
python3 scripts/verify-ecu-stock.py white-2026-09-12-asfound.bin
python3 scripts/verify-ecu-stock.py white-2026-09-12-asfound.bin -r ~/gk27-reference/<matching>.bin
```

Full procedure and how to read the diff output: `common/opengk/ecu-factory-verification.md`.

### 2.4 Record it

Fill in the registry in `ecu-factory-verification.md` and **commit the dumps somewhere
durable** — they are your rollback images and you cannot recreate them after a flash.

| Car | Description | Calibration | Hardware rev | Checksums | Verdict |
|-----|-------------|-------------|--------------|-----------|---------|
| White (fresh engine) | | | | | |
| Blue | | | | | |
| Spare #1 | | | | | |
| Spare #2 | | | | | |

**Do the spares too, if they're in the trailer.** You wanted to know which of several ECUs
is the tuned one — this weekend is a good excuse to settle it while the laptop is out, and a
verified-stock spare in the trailer is worth real money to you if an ECU dies at the track.

### 2.5 Free diagnostic while you're connected

```bash
python3 gkflasher.py -p kline -i /dev/ttyUSB0 --read-dtcs
```

Zero risk, and on a fresh engine a stored code between sessions is worth knowing about.
Worth running after each session.

---

## 3. The overbore question

**Nothing needs to change in the calibration for the bore. Here is why.**

### The numbers

| | Stock | +0.5 mm |
|---|---|---|
| Bore × stroke | 86.7 × 75.0 mm | 87.2 × 75.0 mm |
| Displacement | 2,656 cc | ≈ 2,687 cc |
| Per cylinder | 442.7 cc | 447.8 cc |

Area scales with bore squared: (87.2 / 86.7)² = **+1.16 %**. About 31 cc total.

### Why the ECU absorbs it automatically

SIMK43 on the V6 is a **MAF-based** system, not speed-density:

- The ignition maps are axed on MAF — `ip_iga_bas__n_32__maf_hb`, `ip_iga_ref__n_32__maf_hb`
  (`maf_hb` = MAF high byte).
- There is a MAF calibration table, `id_maf_tab`.
- The sensor list has a hot-film MAF (Siemens `5WK9643`) and **no MAP sensor**.
- GKFlasher's own logger reports "Air Flow Rate from Mass Air Flow Sensor (kg/h)".

A speed-density ECU infers airflow from RPM, manifold pressure and an assumed displacement —
change displacement and its assumption is wrong, so you rescale. **A MAF-based ECU measures
the air directly.** The bigger bore pulls 1.16 % more air, the MAF sees 1.16 % more air, and
fuel is metered accordingly. No table knows or cares what the displacement is.

On top of that, 1.16 % is well inside the noise floor: injector-to-injector variation,
MAF sensor tolerance, and closed-loop O2 authority are all larger. Long-term fuel trim alone
would absorb this without you ever noticing.

> **Where a rebuild *can* matter:** compression ratio, cam timing, and piston design — not
> bore. If the forged pistons changed the dish volume enough to move CR meaningfully off
> stock 10.0:1, that affects knock margin. That is a question for the build sheet and the
> piston spec, not something you fix by scaling a fuel table for displacement. If CR went
> *up* materially, the honest mitigation this weekend is octane, not a flash.

---

## 4. What a "safe tune" would actually take

### 4.1 The blocker: there is no map definition file

Verified, not assumed:

- **GKFlasher has no map editor.** It reads and writes whole zones — calibration, program,
  or an address range. Searching the source for map/XDF/definition handling returns nothing.
- **The OpenGK wiki's Map Definitions page is names only.** All 776 bytes of it: ten map
  names with one-line descriptions. No addresses, no offsets, no scaling, no axes.
- **No XDF exists in the OpenGK file repository.** A crawl of the whole tree turned up
  TunerPro Free's *installer* under `Tools/`, but no definition file to load into it.

So "lower the rev limiter a bit" decomposes into: find `c_n_max` somewhere in a 32 KiB
calibration zone, work out its scaling and byte order, edit it, fix the checksum, and flash.
Finding it is a reverse-engineering session with a datalogger and a lot of patience. **That
is not a paddock task on race weekend.**

### 4.2 Why flashing at a track is the wrong risk

Even with a known-good file:

- **An interrupted write bricks the ECU.** Flashing needs stable voltage for the whole
  write. A race car in a paddock — rear-mounted battery, kill switch, marginal charge after a
  session — is close to the worst environment for that. A bricked ECU ends your weekend, and
  the recovery path is BSL, which your CH340 adapter can't even do.
- **You can't verify the result.** GKFlasher's logger exposes 14 parameters: O2 B1S1, MAF,
  ECT, oil temp, IAT, TPS, adapted TPS, battery voltage, cranking signal, closed-throttle
  status, part-load status, vehicle speed, engine speed, target idle. **No knock, no ignition
  advance, no fuel trims.** You cannot confirm a timing change is safe with the tool that
  made it.
- **The stock calibration is the most validated file that ECU will ever run.** Hyundai put
  more validation into it than anyone can replicate trackside. For a fresh engine you want to
  *not* blow up, "factory" is a strong default.

### 4.3 What actually buys safety margin this weekend

Ranked by effect per unit of risk:

1. **Higher-octane fuel.** The single biggest knock-margin lever available with no tools and
   no risk. On a fresh engine of uncertain final CR, this is the move.
2. **Temperature management.** Oil and coolant. Watch the AEM oil temp/pressure gauges; heat
   soak across a long Lemons stint is a more realistic engine-killer than detonation from a
   1 % displacement change.
3. **Driver discipline on revs.** A short-shift agreement among drivers costs nothing,
   applies instantly, is reversible, and is strictly safer than a rev-limit flash — the
   limiter is a backstop, not a strategy.
4. **Monitoring.** The Haltech in shadow mode is your real instrument here — it has the knock
   sensors and the Innovate LM2 wideband. GKFlasher's logger is a weak substitute. Log
   sessions and review between stints.
5. **`--read-dtcs` between sessions.** Free, instant, read-only.

### 4.4 If you still want a lower rev limit — the post-race path

Reasonable goal for a fresh engine; just not a weekend job. Sequence:

1. Dump a known-stock calibration and keep it untouched as the baseline.
2. Locate `c_n_max` / `c_n_max_max` by bracketing: flash a candidate change **on a bench ECU
   or a spare**, not the car's, and observe where the cut lands.
3. Confirm scaling and hysteresis behaviour (`c_n_max_hys`, `c_n_max_hys_max`).
4. Correct the checksum, verify with `verify-ecu-stock.py` that the *only* differences are
   the bytes you intended, then flash.
5. Record the offsets in `common/opengk/map-definitions.md` so this is a solved problem next
   time.

Do this on a spare ECU with the car's known-good dump archived. A lead worth chasing:
`github.com/cfhammargren/hyundai-gk-tuning` is linked from the OpenGK file repository footer
and may hold definitions — it returned 403 from here, so it needs checking from a normal
connection.

---

## Go / no-go

**Green light, do it:**
- Verifying the install offline
- Dumping both cars and any spares
- Running the verification script and filling in the registry
- `--read-dtcs` between sessions

**Red light this weekend:**
- Flashing any modified calibration
- Flashing anything at all, unless an ECU has failed and you are restoring a known-good dump
  to a spare — and even then, do it with a charger on the battery, not after a session

**Abort a read if:** comms keep dropping, battery is low, or a session is about to be called.
A half-finished read costs you nothing; a half-finished write costs you the weekend.

---

## Related

| Topic | File |
|---|---|
| Full verification procedure | `common/opengk/ecu-factory-verification.md` |
| GKFlasher CLI, immo, recovery ops | `common/opengk/gkflasher.md` |
| Factory bin library and tools | `common/opengk/file-repository.md` |
| K-Line routing, BCM pass-through | `common/opengk/k-line.md` |
| Map names | `common/opengk/map-definitions.md` |
| Engine build, break-in, race sequencing | `builds/white-tiburon/engine-swap-race-prep.md` |
| Verification tool | `scripts/verify-ecu-stock.py` |
