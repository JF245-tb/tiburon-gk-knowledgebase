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

## Related

- `gk-chassis-specs.md` — platform overview, front MacPherson strut suspension
- `shop-manual/suspension-system/front-suspension.md` — OEM ball joint and tie rod removal/installation
- `shop-manual/suspension-system/specifications.md` — OEM torque specs
