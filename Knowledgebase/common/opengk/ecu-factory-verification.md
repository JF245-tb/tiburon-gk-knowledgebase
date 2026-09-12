# Verifying an ECU Is in Factory Configuration

**Purpose:** Confirm, before first startup, whether an installed Siemens ECU is stock or carries a tune.
**Applies to:** SIMK41 / SIMK43 (2.7L V6 Delta and 2.0L Beta), read over K-Line with GKFlasher.
**Tooling:** [GKFlasher](https://github.com/Dante383/GKFlasher) + `scripts/verify-ecu-stock.py` in this repo.

> **Everything in this procedure is read-only.** Nothing here writes to the ECU.
> Do not flash anything until the verification says you need to.

---

## The short version

```bash
# 1. Identify the ECU on the bench or in the car (ignition ON, engine not running)
python3 gkflasher.py -p kline -i /dev/ttyUSB0 --id

# 2. Dump it
python3 gkflasher.py -p kline -i /dev/ttyUSB0 --read -o blue-ecu-asfound.bin

# 3. Fingerprint + checksum audit
python3 scripts/verify-ecu-stock.py blue-ecu-asfound.bin

# 4. Download the matching factory bin named by step 3, then diff
python3 scripts/verify-ecu-stock.py blue-ecu-asfound.bin -r ca652051_G3N7TS0H_*.bin
```

---

## Why one check is not enough

There are three signals, and only the third is decisive. Understanding why matters, because
the first two produce false "looks stock" results.

| # | Check | Proves it's modified | Proves it's stock |
|---|-------|----------------------|-------------------|
| 1 | Identity strings | No | No |
| 2 | Checksum audit | **Yes** | No |
| 3 | Diff vs factory bin | **Yes** | **Yes** |

**1. Identity strings** (description / calibration / hardware revision) tell you *which* ECU
this is, so you know which factory bin to compare against. A GKFlasher tune normally leaves
these strings untouched — the tuner edits maps, not the version banner. A matching
calibration string means nothing on its own.

**2. Checksum audit** recomputes the CRC16 over each region and compares to the stored
value. A mismatch is proof the file was edited. But GKFlasher's `--correct-checksum`
fixes checksums automatically, and any competent tune will have valid checksums.
**A clean checksum result is not evidence of a stock ECU.**

**3. Diff against a known-good factory bin** is the real test. OpenGK hosts a library of
factory dumps, and a tune shows up as contiguous runs of differing bytes inside the
calibration zone.

---

## Step 1 — Connect and identify

The 2.7L V6 routes K-Line through the BCM (`BCM-IM` pin 19), so **the BCM must be powered**,
not just the ECU. See `k-line.md` for the routing detail. ECU address `0x11`, 10400 baud,
Fast Init.

Ignition ON, engine not running. On the blue car the ignition switch is deleted — power the
ECU and BCM through whatever replaces it before expecting comms.

```bash
python3 gkflasher.py -p kline -i /dev/ttyUSB0 --id
```

GKFlasher prints a banner on connect, before any operation:

```
[*] Trying to find calibration..
[*] Found! Description: ca652051, calibration: G3N7TS0H
```

Those two strings are read directly out of the EEPROM:

| Field | EEPROM address (2mbit) | EEPROM address (4mbit V6) |
|---|---|---|
| `calibration` | `0x48000` (calibration zone start) | `0x88000` |
| `description` | `0x48040` (zone start + 0x40) | `0x88040` |

`--id` additionally dumps the KWP2000 identification parameters (service `0x1A`), including
`0x8E` Calibration version and `0x8D` Program code version.

**Hardware note:** the OpenGK wiki's insistence on a genuine FTDI chipset predates
GKFlasher v1.0.5, which added CH340 support. FTDI is still the more reliable choice, and
CH340 adapters are not supported for BSL operations.

---

## Step 2 — Dump the ECU

```bash
python3 gkflasher.py -p kline -i /dev/ttyUSB0 --read -o blue-ecu-asfound.bin
```

A full read is 256 KiB (2mbit) or 512 KiB (4mbit) and takes a while over K-Line at 10400 baud.
`--desired-baudrate` can speed this up, but pre-2005 ECUs often reject it — see `gkflasher.md`.

Keep this dump. It is your rollback image if anything later goes wrong, and you cannot
recreate it once the ECU is flashed.

> Reading the calibration zone alone (`--read-calibration`) is faster and is enough for the
> diff, but GKFlasher pads partial reads to full EEPROM size with `0xFF`. The padding
> regions will then show as differences against a full factory bin. **Use a full `--read`**
> unless you are diffing two partial reads taken the same way.

---

## Step 3 — Fingerprint and checksum audit

```bash
python3 scripts/verify-ecu-stock.py blue-ecu-asfound.bin
```

```
[*] ECU type: SIMK41 / V6 2mbit

-- 1. FINGERPRINT --------------------------------------------------
    Description  : ca652051
    Calibration  : G3N7TS0H
    Hardware rev : 5WY1502B
    ECU ID       : HMC021147190609316577657601H

    Look for a reference bin named ca652051_G3N7TS0H_*.bin

-- 2. CHECKSUM AUDIT -----------------------------------------------
    Boot         stored=0xc9ac  computed=0xc9ac  OK
    Calibration  stored=0x44de  computed=0x44de  OK
    Program      stored=0x84bf  computed=0x84bf  OK
```

The equivalent audit using GKFlasher itself is `--correct-checksum <file>`, which prints
`Current X checksum: ..., new checksum: ...` for each region and then **prompts before
saving**. Answer `n` and the file is left untouched — verified non-destructive. The script
above just does the same arithmetic without the prompt, and with no dependencies.

---

## Step 4 — Get the matching factory reference

OpenGK hosts factory dumps at **<https://opengk.org/files/?dir=EEPROMS/Siemens>**, organised
by chassis and engine. For the Tiburon 2.7L V6 that is **`GK-27`**; the 2.0L is `GK-20`.

The filenames are built from the ECU's own identity fields, which is what makes this work:

```
ca652051_G3N7TS0H_6577715116_5WY1502B_G8_0524661407-HMC021147190609316577657601H.bin
└──┬───┘ └──┬───┘ └────┬───┘ └───┬──┘              └──────────┬───────────────┘
description │      part no.   hardware rev                 ECU ID string
        calibration
```

Every one of these is a real byte sequence in the dump — confirmed against
`ca652051_G3N7TS0H_...`:

| Filename field | EEPROM address | File offset |
|---|---|---|
| `ca652051` (description) | `0x48040` | `0x08040` |
| `G3N7TS0H` (calibration) | `0x48000` | `0x08000` |
| `6577715116` (part number) | `0x5005C` | `0x1005C` |
| `5WY1502B` (hardware rev) | `0x43F80` | `0x03F80` |
| `HMC0211471906...` (ECU ID) | `0x43F95` | `0x03F95` |

**Match on the first two fields** (`description_calibration`). Later fields vary between
individual ECUs of the same calibration and do not need to match.

If no reference exists for your exact calibration, skip to
[Comparing your own ECUs](#comparing-your-own-ecus-against-each-other) — that works without
any factory bin at all, and for your situation it is arguably the better test.

---

## Step 5 — Diff

```bash
python3 scripts/verify-ecu-stock.py blue-ecu-asfound.bin -r ca652051_G3N7TS0H_*.bin
```

A stock ECU:

```
    IDENTICAL -- byte-for-byte match with the reference.
  VERDICT: STOCK
```

A tuned ECU:

```
    256 differing bytes in 2 run(s):

    FILE START   FILE END        BYTES  REGION
    0x9a00       0x9a5f             96  CALIBRATION
    0xb120       0xb1bf            160  CALIBRATION

  VERDICT: MODIFIED -- 256 bytes differ inside the calibration zone
```

### Reading the output

The script clusters differing bytes into contiguous runs, because the *shape* of the
differences is what tells you what you are looking at:

- **Long contiguous runs inside the calibration zone** — a tune. Maps are contiguous tables,
  so editing one produces a solid block of differences. Ignition timing, rev limiter and MAF
  calibration all live here (see `map-definitions.md`).
- **Scattered single bytes** — adaptive / learned values, DTC storage, per-car data. Expected
  on any ECU that has run in a car.
- **Differences in the program zone** — unusual. The program zone is firmware, not tune data.
  Investigate before proceeding.

**One advantage specific to the 2.7L V6:** immobiliser data lives entirely in the BCM, not
the ECU (see `immobiliser.md`). A V6 ECU stores no VIN or key pairing, so a V6 calibration
zone diff comes out much cleaner than the 2.0L equivalent, where SMARTRA data is in the ECU
itself and *will* differ per car.

---

## Comparing your own ECUs against each other

With several ECUs on the shelf and one known to be tuned, you do not strictly need a factory
reference — the odd one out identifies itself. Dump each ECU, then compare them pairwise:

```bash
python3 scripts/verify-ecu-stock.py ecu-a.bin -r ecu-b.bin
```

Two untouched ECUs of the same calibration differ only in scattered adaptive bytes. The
tuned one differs from all the others in contiguous calibration-zone blocks.

Do this **before** any of them goes in a car, and label the physical ECUs as you go.

### ECU registry

Fill this in as you dump each one. The point is that you never have to do this
identification twice.

| ECU # | Physical label / mark | Description | Calibration | Hardware rev | Size | Dump file | Checksums | Verdict |
|-------|----------------------|-------------|-------------|--------------|------|-----------|-----------|---------|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |
| 4 | | | | | | | | |

---

## If the installed ECU turns out to be the tuned one

You have two options. Decide deliberately — do not reflexively flash before a first start.

**Option A — swap in a known-stock ECU.** Physically simplest, and it leaves the tuned ECU
intact for later. On the 2.7L V6 the ECU holds no immobiliser data, so swapping ECUs does
not require re-pairing keys; the BCM handles that side.

**Option B — flash the stock calibration back.** Only after you have dumped and safely
archived the ECU as-found:

```bash
python3 gkflasher.py -p kline -i /dev/ttyUSB0 --flash-calibration ca652051_G3N7TS0H_*.bin
```

GKFlasher compares the current calibration version against the file's and asks for
confirmation before writing. `--flash-calibration` writes only the tune zone and leaves the
program zone alone, which is what you want here.

**Before flashing anything:**
- Battery voltage must be stable. An interrupted write bricks the ECU. Use a charger, not a
  marginal battery — especially on the blue car with its rear-mounted battery and kill switch.
- Do not flash over a connection that has been dropping out.
- Confirm the reference bin's checksums pass (step 3) before writing it to an ECU.

After any flash, clear learned values so the ECU adapts from a known state:

```bash
python3 gkflasher.py -p kline -i /dev/ttyUSB0 --clear-adaptive-values
```

---

## Caveats

- **A checksum match does not mean stock.** Stated twice on purpose. This is the most common
  way people conclude an ECU is untouched when it is not.
- **A calibration-string match does not mean stock.** Tunes generally preserve the banner.
- **Hardware-level modifications are out of scope.** This procedure verifies flash contents
  over the diagnostic port. A chip-off reflash that restored the original identity strings, or
  physically modified hardware, would not be caught here. For the realistic case — a tune
  someone flashed with GKFlasher — the diff is conclusive.
- **Partial reads pad to full size with `0xFF`** and will produce spurious diffs. Always
  `--read` in full.
- The date-code split at **31 January 2003** changes upstream O2 sensor requirements (5V vs
  1V) between ECU revisions — see `ecm-identification.md`. If you swap ECUs across that
  boundary, the sensors have to match the ECU.

---

## References

- GKFlasher CLI reference — `gkflasher.md`
- K-Line routing and KWP2000 details — `k-line.md`
- ECU label decoding — `ecm-identification.md`
- Tuning map names — `map-definitions.md`
- Immobiliser architecture — `immobiliser.md`
- Factory EEPROM library — <https://opengk.org/files/?dir=EEPROMS/Siemens>
- GKFlasher source — <https://github.com/Dante383/GKFlasher>
