# COP Ignition Conversion — Toyota 90919-A2005
**Car:** White Tiburon (G6BA 2.7L V6 Delta)
**Status:** 🔲 Planned — parts selected, not yet installed
**Source:** https://www.newtiburon.com/threads/toyota-cop-ignition-setup.384866/ (JonGTR, Jul 2014)

---

## Overview

Replacing the stock 3-coil wasted spark system with 6× Toyota smart coils (coil-on-plug).
The Haltech Elite 2500 has 6 independent ignition outputs (IGN1–6), enabling full **sequential COP** — one coil per cylinder, individually triggered.

This eliminates wasted spark (firing twice per revolution per coil pair) and allows:
- Individual per-cylinder timing control
- Larger spark plug gap capability (especially important under boost)
- Better dwell control and coil energy management
- Cleaner engine bay (removes stock ignition module bracket)

---

## Coil Part Number

**Selected: Toyota 90919-A2005** (confirmed by JonGTR on NewTiburon.com)

Compatible alternatives (same connector, different boot length/mount):
| Part Number | Notes |
|-------------|-------|
| **90919-A2005** | ✅ Confirmed fitment on GK Tiburon |
| 90080-19015 | Alternative — same connector |
| 90919-02239 | Alternative |
| 90080-19023 | Alternative |
| 90919-02234 | Alternative |

Available from: Toyota dealerships, junkyards, eBay. Total cost for 6 coils well under $100 used.
Found on: Toyota 1.8L, 2.4L, 2.5L, 5.7L engines (various years).

---

## Coil Connector Pinout (4-pin, each coil)

| Pin | Signal | Wire Color (coil side) | Description |
|-----|--------|----------------------|-------------|
| **A** | Ground | Black | Coil chassis GND → engine block or head |
| **B** | Ignition Trigger | Blue | ECU ground-side trigger (from Haltech IGN output) |
| **C** | IGN Feedback / AUX | Cyan/Light Blue | Optional: diagnostic feedback. Leave open if not used. |
| **D** | 12V+ Switched Power | Red | 12V from PDM (common bus, all 6 coils shared) |

**Note:** Source of truth is the JonGTR wiring diagram (shared via NewTiburon.com thread, drawing date 2014-07-29). Title: "TOYOTA COROLLA COIL WIRING — HYUNDAI H BETA" — diagram shows Beta (4-cyl) layout but connector pinout and trigger scheme applies to Delta V6 as well.

---

## Wiring Diagram — V6 Sequential COP

```
PDM MP2 (12V switched) ────────────────────────────────── D (all 6 coils, shared bus)

Engine block GND ───────────────────────────────────────── A (all 6 coils, shared bus)

Haltech 34-pin pin 3  (IGN 1, Y/B wire) ─────────────── B  Coil 1
Haltech 34-pin pin 4  (IGN 2, Y/R wire) ─────────────── B  Coil 2
Haltech 34-pin pin 5  (IGN 3, Y/O wire) ─────────────── B  Coil 3
Haltech 34-pin pin 6  (IGN 4, Y/G wire) ─────────────── B  Coil 4
Haltech 34-pin pin 7  (IGN 5, Y/BR wire) ────────────── B  Coil 5
Haltech 34-pin pin 8  (IGN 6, Y/L wire) ─────────────── B  Coil 6

Pin C (feedback) ────────────────────────────────────────── Open (or to Haltech diagnostic input)
```

**Wire gauge:**
- 12V bus (D, shared): 16–18 AWG main run, 20 AWG branch to each coil
- Trigger signal (B): 22–24 AWG
- Ground bus (A): 16–18 AWG main run, 20 AWG branch to each coil

---

## Mating Connector

Toyota/Denso 4-pin smart coil connector. Source pigtails from:
- OEM harness from donor Toyota engine (junkyard)
- Aftermarket plug-and-play pigtails (search "Toyota smart coil connector pigtail")

---

## Haltech NSP Configuration

⚠️ **Must update ignition configuration in NSP when switching from wasted spark to COP:**

| Setting | Old (wasted spark) | New (COP sequential) |
|---------|-------------------|---------------------|
| Ignition mode | Wasted spark | Sequential COP |
| Number of coils | 3 | 6 |
| Ignition outputs | IGN 1–3 only | IGN 1–6 |
| Dwell time | ~3.5ms (stock coil) | **~2.1ms** (Toyota smart coil) |
| Coil type | External igniter | Smart coil (internal igniter) |

**Firing order (G6BA V6):** Verify in shop-manual/engine-mechanical.md — confirm correct IGN1–6 assignment per cylinder.

⚠️ Setting incorrect dwell on a smart coil (too long) will **overheat and damage the coil**. Smart coils have built-in igniter — they control their own dwell internally. Set ECU dwell to ~2.1ms as directed. Verify with oscilloscope on first startup.

---

## Coil Mounting

The G6BA Delta V6 spark plugs are accessed through plug wells in the cam covers (two banks of 3).
The Toyota 90919-A2005 coil is a pencil-type coil that inserts directly into the plug well.

**Mounting checklist:**
- [ ] Measure plug well diameter and depth — verify coil body fits without binding
- [ ] Confirm rubber seal/boot condition on each coil
- [ ] Torque coils to spec or use retention clip if provided
- [ ] Remove OEM ignition module bracket and three wasted-spark coil assemblies

---

## PDM Changes

The PDM MP2 assignment (Ignition Coil 12V Rail) stays the same — it now feeds 6 coils instead of 3.
Verify PDM MP2 current rating is sufficient: 6 × Toyota coil peak current.
Mid-power outputs on AIM PDM32 are rated ~10–15A continuous — should be adequate for 6 smart coils.

---

## Key References
- Wiring diagram: JonGTR (NewTiburon.com, 2014) — "Toyota Corolla Coil Wiring" schematic
- Thread: https://www.newtiburon.com/threads/toyota-cop-ignition-setup.384866/
- Haltech IGN output pins: `signal-routing.md` (Ignition section)
- PDM MP2 assignment: `aim-pdm/pdm-pinout.md`
