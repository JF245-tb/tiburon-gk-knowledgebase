# PT100 Temp Element — Pull-Up Voltage Tables

**Applies to:** Lowdoller Motorsports combo pressure/temp sensors (see `lowdoller-sensors.md`)
**Element:** PT100 platinum RTD — 100 Ω at 32 °F (0 °C), 138.51 Ω at 212 °F (100 °C), α = 0.00385
**Supply:** 5.000 V sensor reference (Haltech Elite 2500 34-pin **pin 9**, orange)

---

## Circuit

The temp element sits between the ECU input pin and signal ground; the pull-up resistor
sits between the ECU input pin and the 5 V reference. The input reads the divider node:

```
V_signal = 5.000 × R_sensor / (R_sensor + R_pullup)
```

Because the element is a *rising* resistance curve (PTC/RTD), signal voltage **increases**
with temperature — opposite of an OEM NTC sensor.

---

## Voltage vs Temperature

| Temp (°F) | Resistance (Ω) | Volts w/ 1k Pull-Up | Volts w/ 2k Pull-Up |
|-----------|----------------|---------------------|---------------------|
| -40 | 84.27 | 0.389 | 0.202 |
| -4 | 89.54 | 0.411 | 0.214 |
| 32 | 100 | 0.455 | 0.238 |
| 68 | 107.79 | 0.487 | 0.256 |
| 104 | 115.54 | 0.518 | 0.273 |
| 140 | 123.24 | 0.549 | 0.290 |
| 176 | 130.9 | 0.579 | 0.307 |
| 212 | 138.51 | 0.608 | 0.324 |
| 248 | 146.07 | 0.637 | 0.340 |
| 284 | 153.585 | 0.666 | 0.357 |
| 320 | 161.05 | 0.694 | 0.373 |
| 356 | 168.48 | 0.721 | 0.388 |
| 392 | 175.86 | 0.748 | 0.404 |
| 428 | 183.19 | 0.774 | 0.420 |
| 464 | 190.47 | 0.800 | 0.435 |
| 500 | 197.71 | 0.825 | 0.450 |

---

## Choosing the Pull-Up

| | 1 kΩ | 2 kΩ |
|---|---|---|
| Signal range (−40 to 500 °F) | 0.389 – 0.825 V | 0.202 – 0.450 V |
| Total span | 0.436 V | 0.248 V |
| Span per 100 °F (approx) | 0.081 V | 0.046 V |
| Sensor current at 500 °F | ~4.2 mA | ~2.3 mA |

**The 1 kΩ pull-up gives roughly 1.76× the signal span**, which is the more important factor
here — the whole curve already sits in the bottom fifth of the 0–5 V input range, so
resolution is the limiting constraint, not self-heating. Use 2 kΩ only if the hardware
forces it (fixed internal pull-up) or if sensor self-heating is a measured problem.

Whichever resistor is fitted, the matching voltage column above must be entered as the
custom calibration in Haltech NSP. **Mixing the table and the resistor skews the reading across the
entire range** — with a 2 kΩ resistor fitted, a sensor at 212 °F puts 0.324 V on the pin,
which falls off the bottom of the 1 kΩ table entirely (below its 0.389 V / −40 °F endpoint).

---

## Source

Derived from the PT100 resistance-vs-temperature table in `lowdoller-sensors.md`
(Lowdoller Motorsports published calibration). Voltages computed, not measured.
