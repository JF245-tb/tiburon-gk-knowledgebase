# GK Tiburon — Knuckle Taper Measurements (Ball Joint & Tie Rod End)

**Purpose:** Sizing heim pins / spherical rod ends to replace OEM joints in the front knuckle.
Measurements taken with calipers — inherently approximate for tapered blind holes. Log additional sessions to refine.

Formula: `half_angle = arctan((D_large − D_small) / 2 / depth)` → included angle = 2 × half_angle

---

## Lower Arm Ball Joint Bore

### Raw Measurements — Session 1 (2026-05-09)

| Dimension | Measurement |
|-----------|-------------|
| Top (small) diameter | 14.3 mm |
| Bottom (large) diameter | 16.5 mm |
| Hole depth | 20.6 mm |

### Calculated Taper

| Parameter | Value |
|-----------|-------|
| Diameter difference | 2.2 mm |
| Half-angle (per side) | 3.057° |
| **Included angle** | **6.11°** |
| As 1:X ratio | **1:9.4** |

### Comparison to Common Tapers

| Standard | Included Angle | Delta | Notes |
|----------|---------------|-------|-------|
| **1:10** | 5.72° | **+0.39°** | Closest match |
| 1:8 (common SAE ball joint) | 7.15° | −1.04° | Many US domestic vehicles |
| SAE 7° (3°30' per side) | 7.00° | −0.89° | Very common US truck/car |

**Assessment:** Closest to **1:10**. Given caliper error in a blind tapered hole, 1:8 is also plausible. Test-fit a tapered pin before committing. Start with **14mm × 1:10** shank.

OEM torque: **60–72 Nm (43–52 lb-ft)**

### Additional Measurement Sessions

| Session | Date | Top Ø | Bottom Ø | Depth | Method |
|---------|------|-------|----------|-------|--------|
| 1 | 2026-05-09 | 14.3 mm | 16.5 mm | 20.6 mm | Calipers |
| 2 | — | — | — | — | — |

---

## Tie Rod End Bore

### Raw Measurements — Session 1 (2026-05-09)

| Dimension | Measurement |
|-----------|-------------|
| Top (small) diameter | 12.5 mm |
| Bottom (large) diameter | 15.25 mm |
| Hole depth | 17.5 mm |

### Calculated Taper

| Parameter | Value |
|-----------|-------|
| Diameter difference | 2.75 mm |
| Half-angle (per side) | 4.493° |
| **Included angle** | **8.99°** |
| As 1:X ratio | **1:6.4** |

### Comparison to Common Tapers

| Standard | Included Angle | Delta | Notes |
|----------|---------------|-------|-------|
| **1:6** | 9.53° | **−0.54°** | Closest match |
| 1:7 | 8.17° | +0.81° | Next closest |
| 1:8 (common SAE ball joint) | 7.15° | +1.83° | Common but unlikely here |
| SAE 7° (3°30' per side) | 7.00° | +1.99° | — |

**Assessment:** Closest to **1:6**, within caliper measurement margin. Notably steeper taper than the ball joint bore (9° vs 6°) — these two bores use **different taper standards**. Start with a **12.5mm × 1:6** tapered shank for sourcing.

OEM torque: **22–35 Nm (18–25 lb-ft)**

### Additional Measurement Sessions

| Session | Date | Top Ø | Bottom Ø | Depth | Method |
|---------|------|-------|----------|-------|--------|
| 1 | 2026-05-09 | 12.5 mm | 15.25 mm | 17.5 mm | Calipers |
| 2 | — | — | — | — | — |

---

## Summary Comparison

| Joint | Included Angle | Closest Standard | Small End Ø | Notes |
|-------|---------------|-----------------|-------------|-------|
| Lower arm ball joint | 6.11° | 1:10 | 14.3 mm | Shallower taper |
| Tie rod end | 8.99° | 1:6 | 12.5 mm | Steeper taper, smaller pin |

The two bores are **not the same taper** — don't assume interchangeability when sourcing heim pins.

---

---

## Verification Plan

### Why calipers aren't enough

Measuring inside a tapered blind hole with calipers introduces error because the jaw tips don't seat consistently at the same depth on each reading. Measured error vs. predicted values for known tapers is ~0.14–0.38mm — enough to mistake a 1:8 for a 1:10. The methods below eliminate that ambiguity.

### Option 1 — OEM stud measurement (do this first)

Buy the MOOG replacement parts. The tapered shank is external and easy to measure accurately at multiple points with calipers. This gives you the OEM taper from the part itself without needing precision gauges.

| Part | Expected MOOG P/N | Cost est. |
|------|------------------|-----------|
| Lower arm ball joint | K90349 (verify fitment for 2003 GK V6) | ~$20–35 |
| Tie rod end (outer) | ES3493 or similar (verify) | ~$15–25 |

Measure the stud at the top and bottom of the tapered section and calculate the same way as the bore measurements. Cross-check against the two candidate standards.

### Option 2 — Taper plug gauges + Prussian blue

Precision-ground plugs at exact taper ratios. Coat with Prussian blue / layout dye, insert into bore, rotate 1/4 turn, pull. Uniform dye removal = correct taper. One-sided contact = wrong ratio.

Buy the two bracketing candidates for each bore:

| Bore | Gauge 1 | Gauge 2 | Why |
|------|---------|---------|-----|
| Ball joint | 1:10 | 1:8 | Measured 6.11° sits between them |
| Tie rod end | 1:6 | 1:7 | Measured 8.99° sits between them |

Source: MSC Industrial, McMaster-Carr, Travers Tool. ~$25–60 per gauge. A set of all 4 = ~$100–200.

### Option 3 — Telescoping bore gauge + outside micrometer

Telescoping gauges seat flat at a controlled depth and give a true internal diameter at that specific point. Measure at the top, middle, and bottom of each bore, then recalculate the taper. Tightens error to ±0.05mm vs ±0.3mm+ with calipers.

Decent Starrett or Mitutoyo telescoping set: $60–100. Requires an outside micrometer to read.

### Recommended sequence

1. **Buy the MOOG parts** — cheapest, fastest, you need them anyway
2. **Measure the OEM studs** externally with calipers — should be definitive for the ball joint
3. **If tie rod stud is still ambiguous**, buy the 1:6 and 1:7 taper plug gauges and test with Prussian blue

---

## Cross-Platform Reference

### Same-platform candidates (highest confidence)

These share the GK/EF-era Hyundai corporate suspension platform and are most likely to use the same taper specs:

| Vehicle | Notes |
|---------|-------|
| Hyundai Elantra XD (2001–2006) | Same corporate generation, MacPherson front |
| Kia Spectra (2004–2009) | Corporate sibling |
| Kia Optima / Magentis (2001–2006) | EF-derived platform |
| Hyundai Sonata EF (1998–2005) | Platform predecessor, shares lower arm design |

If a Tiburon GK ball joint stud matches an Elantra XD stud by measurement, that confirms the taper and opens up a much larger aftermarket parts pool for test fits.

### Tie rod end — steeper taper (~1:6)

The ~9° tie rod taper is steeper than most US domestic tie rod ends (which tend toward 7°–7.15°). Vehicles known to use steeper metric tie rod tapers that may be worth measuring for comparison:

| Vehicle | Basis for suggestion |
|---------|---------------------|
| Honda Civic EK / CR-V RD (1996–2001) | Known to run steeper tie rod taper than US-market norm |
| Mazda Protegé / 323 (BJ/BG gen) | Similar era JDM platform |
| VW Golf / Jetta Mk4 (1999–2005) | European metric taper standards, steeper than SAE |

> **Caveat:** The cross-platform suggestions above are based on platform and engineering lineage knowledge, not confirmed taper measurements. Treat as starting points for test-fits, not confirmed matches.

---

## Related

- `gk-chassis-specs.md` — platform overview, front MacPherson strut suspension
- `shop-manual/suspension-system/front-suspension.md` — OEM ball joint and tie rod removal/installation
- `shop-manual/suspension-system/specifications.md` — OEM torque specs
