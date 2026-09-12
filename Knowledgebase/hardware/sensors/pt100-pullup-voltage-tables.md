# PT100 Temp Element — Pull-Up Voltage Tables

**Applies to:** Lowdoller Motorsports combo pressure/temp sensors (see `lowdoller-sensors.md`)
**Element:** PT100 platinum RTD — 100 Ω at 32 °F (0 °C), 138.51 Ω at 212 °F (100 °C), α = 0.00385
**Supply:** 5.000 V reference — Haltech Elite 2500 34-pin **pin 9** (orange) / AiM PDM **B16**

**Two different pull-ups are in play. Use the column that matches the device:**

| Device | Pull-up | Column to use |
|--------|---------|---------------|
| Haltech Elite 2500 | **1 kΩ** (set in NSP) | mV w/ 1k |
| AiM PDM 32 | **2 kΩ** (internal, fixed) | mV w/ 2k |

Feeding one device the other's table is the single most likely way to get a wrong
temperature here — at 212 °F the two tables differ by 284 mV.

---

## Circuit

The temp element sits between the input pin and signal ground; the pull-up sits between the
input pin and the 5 V reference. The input reads the divider node:

```
V_signal = 5.000 × R_sensor / (R_sensor + R_pullup)
```

Because the element is a *rising* resistance curve (PTC/RTD), signal voltage **increases**
with temperature — opposite of an OEM NTC sensor.

---

## Voltage vs Temperature

| Temp (°F) | Resistance (Ω) | mV w/ 1k *(Haltech)* | mV w/ 2k *(PDM)* |
|-----------|----------------|----------------------|------------------|
| -40 | 84.27 | 389 | 202 |
| -4 | 89.54 | 411 | 214 |
| 32 | 100 | 455 | 238 |
| 68 | 107.79 | 487 | 256 |
| 104 | 115.54 | 518 | 273 |
| 140 | 123.24 | 549 | 290 |
| 176 | 130.9 | 579 | 307 |
| 212 | 138.51 | 608 | 324 |
| 248 | 146.07 | 637 | 340 |
| 284 | 153.585 | 666 | 357 |
| 320 | 161.05 | 694 | 373 |
| 356 | 168.48 | 721 | 388 |
| 392 | 175.86 | 748 | 404 |
| 428 | 183.19 | 774 | 420 |
| 464 | 190.47 | 800 | 435 |
| 500 | 197.71 | 825 | 450 |

Full-range span: **436 mV** on 1 kΩ, **248 mV** on 2 kΩ.

---

## AiM Race Studio 3 — Input Type

The PDM carries its own 2 kΩ pull-up, so **do not add an external resistor** on a PDM
channel. That also makes Ohm the better input type:

| | **Ohm** *(preferred)* | **mV** |
|---|---|---|
| Table to enter | Resistance column, 84.27 → 197.71 Ω | mV w/ 2k column, 202 → 450 mV |
| Conversion needed | None — Lowdoller's published numbers go in as-is | Yes, and only valid for 2 kΩ |
| Affected by pull-up tolerance | No | Yes — 1% of pull-up ≈ 5 °F |
| Affected by Vref sag | No | Yes — 2% sag ≈ 11–15 °F |
| Portable to the Haltech | Yes, same table | No, Haltech needs the 1k column |

In Ohm mode the PDM does its own resistance measurement, so the pull-up value never enters
the calibration and this whole conversion becomes unnecessary.

### Bench check

Back-probe the channel input to ground with the sensor at a known temperature:

| Sensor at | PDM (2 kΩ) | Haltech (1 kΩ) |
|-----------|------------|----------------|
| Room temp, ~68 °F | ≈ **0.256 V** | ≈ 0.487 V |
| Boiling water, 212 °F | ≈ **0.324 V** | ≈ 0.608 V |

If a PDM channel reads ~0.487 V at room temp, it is running a 1 kΩ pull-up, not 2 kΩ, and
the 1k column applies instead.

---

## Source

Derived from the PT100 resistance-vs-temperature table in `lowdoller-sensors.md`
(Lowdoller Motorsports published calibration). Voltages computed, not measured — confirm with
the bench check above before committing a calibration.
