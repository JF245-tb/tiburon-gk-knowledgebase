# PT100 Temp Element — Pull-Up Voltage Tables

**Applies to:** Lowdoller Motorsports combo pressure/temp sensors (see `lowdoller-sensors.md`)
**Element:** PT100 platinum RTD — 100 Ω at 32 °F (0 °C), 138.51 Ω at 212 °F (100 °C), α = 0.00385
**Supply:** 5.000 V sensor reference (Haltech Elite 2500 34-pin **pin 9**, orange / AiM PDM **B16**)
**Pull-up in use: 1 kΩ.** The 2 kΩ column is reference only — see "Choosing the Pull-Up".

---

## Circuit

The temp element sits between the input pin and signal ground; the pull-up resistor sits
between the input pin and the 5 V reference. The input reads the divider node:

```
V_signal = 5.000 × R_sensor / (R_sensor + R_pullup)
```

Because the element is a *rising* resistance curve (PTC/RTD), signal voltage **increases**
with temperature — opposite of an OEM NTC sensor.

---

## Voltage vs Temperature

| Temp (°F) | Resistance (Ω) | Volts w/ 1k | mV w/ 1k | Volts w/ 2k |
|-----------|----------------|-------------|----------|-------------|
| -40 | 84.27 | 0.389 | 388.6 | 0.202 |
| -4 | 89.54 | 0.411 | 410.9 | 0.214 |
| 32 | 100 | 0.455 | 454.5 | 0.238 |
| 68 | 107.79 | 0.487 | 486.5 | 0.256 |
| 104 | 115.54 | 0.518 | 517.9 | 0.273 |
| 140 | 123.24 | 0.549 | 548.6 | 0.290 |
| 176 | 130.9 | 0.579 | 578.7 | 0.307 |
| 212 | 138.51 | 0.608 | 608.3 | 0.324 |
| 248 | 146.07 | 0.637 | 637.3 | 0.340 |
| 284 | 153.585 | 0.666 | 665.7 | 0.357 |
| 320 | 161.05 | 0.694 | 693.6 | 0.373 |
| 356 | 168.48 | 0.721 | 720.9 | 0.388 |
| 392 | 175.86 | 0.748 | 747.8 | 0.404 |
| 428 | 183.19 | 0.774 | 774.1 | 0.420 |
| 464 | 190.47 | 0.800 | 800.0 | 0.435 |
| 500 | 197.71 | 0.825 | 825.4 | 0.450 |

---

## AiM Race Studio 3 — mV or Ohm Input Type?

Race Studio custom sensors accept either input type. **The one you pick has to match how the
pull-up is actually wired**, because the two modes assume different circuits:

| | Use **Ohm** | Use **mV** |
|---|---|---|
| When | The PDM supplies the pull-up — sensor wired to a channel input and signal ground, nothing added | You wired your own 1 kΩ from the channel input to the 5 V reference (B16) |
| Table to enter | **Resistance column** — 84.27 Ω → −40 °F … 197.71 Ω → 500 °F | **mV column** — 389 mV → −40 °F … 825 mV → 500 °F |
| Depends on pull-up value? | No | Yes — table is only valid for 1 kΩ |
| Depends on Vref accuracy? | No | Yes — assumes 5.000 V |

**Prefer Ohm where the hardware allows it.** In Ohm mode the device does its own resistance
measurement, so the calibration stays correct regardless of what the pull-up value is and
regardless of reference-voltage drift. Ohm mode is also portable — the same table works on
the Haltech side, which wants resistance-vs-temperature as well.

**Do not mix them.** Selecting Ohm while an external pull-up is fitted puts that resistor in
the device's own measuring circuit and the computed resistance will be wrong. Selecting mV
with no external pull-up reads whatever the internal circuit produces, which is not this table.

### Bench check before trusting either table

With the sensor at a known temperature, back-probe the channel input to ground:

| Sensor at | Expect (1 kΩ, 5.000 V ref) |
|-----------|----------------------------|
| Room temp, ~68 °F | **≈ 0.487 V** (107.79 Ω) |
| Boiling water, 212 °F | **≈ 0.608 V** (138.51 Ω) |

If room temp reads ≈0.487 V, the 1 kΩ divider and the 5 V reference are both real and the mV
column is good. A reading near 2.5 V means no pull-up divider is present at all; a reading
well below 0.4 V means the pull-up is larger than 1 kΩ.

---

## Choosing the Pull-Up

| | 1 kΩ *(in use)* | 2 kΩ |
|---|---|---|
| Signal range (−40 to 500 °F) | 0.389 – 0.825 V | 0.202 – 0.450 V |
| Total span | 0.436 V | 0.248 V |
| Span per 100 °F (approx) | 0.081 V | 0.046 V |
| Sensor current at 500 °F | ~4.2 mA | ~2.3 mA |

The 1 kΩ pull-up gives roughly 1.76× the signal span. The whole curve already sits in the
bottom fifth of the 0–5 V input range, so resolution is the limiting constraint, not
self-heating — 1 kΩ is the right choice here. The 2 kΩ column is kept only for the case where
hardware forces a different pull-up (fixed internal resistor on some channel).

---

## Source

Derived from the PT100 resistance-vs-temperature table in `lowdoller-sensors.md`
(Lowdoller Motorsports published calibration). Voltages computed, not measured — confirm with
the bench check above before committing a calibration.
