# GK Tiburon — Ball Joint Taper (Knuckle Hole)

**Purpose:** Sizing a heim pin / spherical rod end to replace the OEM lower arm ball joint in the front knuckle.

---

## Raw Measurements — Session 1 (2026-05-09)

Measured with calipers. Measurement accuracy is approximate — caliper access to a tapered hole is inherently imprecise. Log additional sessions below to refine.

| Dimension | Measurement |
|-----------|-------------|
| Top (small) diameter | 14.3 mm |
| Bottom (large) diameter | 16.5 mm |
| Hole depth | 20.6 mm |

---

## Calculated Taper

From the measurements above:

| Parameter | Value |
|-----------|-------|
| Diameter difference | 2.2 mm |
| Half-angle (per side) | 3.057° |
| **Included angle** | **6.11°** |
| Taper ratio | 0.1068 mm/mm |
| As 1:X ratio | **1:9.4** |

Formula: `half_angle = arctan((D_large - D_small) / 2 / depth)`

---

## Comparison to Common Automotive Tapers

| Standard | Included Angle | Delta from Measured | Notes |
|----------|---------------|--------------------|----|
| **1:10** | 5.72° | **+0.39°** | Closest match |
| 1:8 (common SAE ball joint) | 7.15° | −1.04° | Many US domestic vehicles |
| SAE 3°30' per side (7° included) | 7.00° | −0.89° | Very common US truck/car ball joints |
| Morse Taper #0 | 2.98° | +3.13° | Machine tool, not automotive |
| ISO metric taper pin 1:50 | 1.15° | +4.97° | Not automotive |

**Assessment:** The measured taper of ~6.1° (1:9.4) falls between the two most common automotive ball joint tapers (1:8 and 1:10). It is closest to **1:10**, but given caliper measurement uncertainty in a blind tapered hole, either 1:8 or 1:10 is plausible until verified with a taper gauge or test pin.

---

## Interpretation / Sizing Notes

- The OEM Hyundai GK front knuckle ball joint bore is not a well-documented taper in community sources.
- 1:10 taper is a reasonable starting assumption for sourcing a heim pin or tapered shank — verify with a test-fit before committing.
- If sourcing a heim pin with a tapered shank: look for a **14mm × 1:10** or **14mm × 1:8** tapered shank and test-fit before final selection.
- Ream to a standard taper if needed after confirming which standard fits best.

---

## Additional Measurement Sessions

> Log future measurements here to refine or cross-check the above.

### Session 2 — (date TBD)

| Dimension | Measurement |
|-----------|-------------|
| Top (small) diameter | — |
| Bottom (large) diameter | — |
| Hole depth | — |
| Method | — |

---

## Related

- `gk-chassis-specs.md` — platform overview, front MacPherson strut suspension
- `shop-manual/suspension-system/front-suspension.md` — OEM ball joint removal/installation procedure
- Torque: lower arm ball joint to knuckle = **60–72 Nm (43–52 lb-ft)**
