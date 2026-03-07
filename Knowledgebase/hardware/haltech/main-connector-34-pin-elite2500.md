# Haltech Elite 2500 — 34-Pin Connector (A)
**Source:** `Haltech/main-connector-34-pin-elite2500.pdf` + Haltech Support Center
**Harness:** HT-141304, Elite 2500 Premium Universal Harness 2.5m (8')

---

## Pinout — Looking Into Connector on ECU

| Pin | Wire Color | Connection | Notes |
|-----|-----------|------------|-------|
| 1 | V/BR | DPO 2 | 1A max, output to ground, **fixed 5V pull-up** |
| 2 | O/Y | AVI 4 | 0–5V signal input, switchable 1K pull-up |
| 3 | Y/B | IGN 1 | 1A max current |
| 4 | Y/R | IGN 2 | 1A max current |
| 5 | Y/O | IGN 3 | 1A max current |
| 6 | Y/G | IGN 4 | 1A max current |
| 7 | Y/BR | IGN 5 | 1A max current |
| 8 | Y/L | IGN 6 | 1A max current |
| **9** | **O (orange)** | **+5V DC sensor supply** | **100mA max — for 5V ratiometric sensors** |
| 10 | B | Battery ground | To vehicle battery negative (−) |
| 11 | B | Battery ground | To vehicle battery negative (−) |
| **12** | **O/W (orange/white)** | **+8V DC sensor supply** | **1A max — for 8V sensors, relays, solenoids** |
| 13 | P | 12V ignition input | 12V on IGN and cranking only |
| 14 | W | AVI 10 (TPS) | 0–5V signal input, switchable 1K pull-up |
| 15 | Y | AVI 9 (MAP) | 0–5V signal input, switchable 1K pull-up |
| 16 | O/B | AVI 2 | 0–5V signal input, switchable 1K pull-up |
| 17 | O/R | AVI 3 | 0–5V signal input, switchable 1K pull-up |
| 18 | V/B | DPO 1 | 1A max, output to ground, user-definable pull-up |
| 19 | L | INJ 1 | Current controlled, 0–8A peak, 0–2A hold |
| 20 | L/B | INJ 2 | Current controlled, 0–8A peak, 0–2A hold |
| 21 | L/BR | INJ 3 | Current controlled, 0–8A peak, 0–2A hold |
| 22 | L/R | INJ 4 | Current controlled, 0–8A peak, 0–2A hold |
| 23 | V/R | DPO 3 | 1A max, fixed 12V pull-up |
| 24 | B/Y | DPO 5 (Fuel Pump Trigger) | 1A max, fixed 12V pull-up |
| 25 | B/R | DPO 6 (ECR Out) | 1A max, fixed 12V pull-up |
| **26** | **R/L** | **ECU Injector Power Input** | **REQUIRED — 12V from injector power relay** |
| 27 | L/O | INJ 5 | Current controlled, 0–8A peak, 0–2A hold |
| 28 | L/Y | INJ 6 | Current controlled, 0–8A peak, 0–2A hold |
| 29 | L/G | INJ 7 | Current controlled, 0–8A peak, 0–2A hold |
| 30 | L/V | INJ 8 | Current controlled, 0–8A peak, 0–2A hold |
| 31 | G | Stepper 1 P1 / DPO | Hi/Lo side driver, 1A max |
| 32 | G/B | Stepper 1 P2 / DPO | Hi/Lo side driver, 1A max |
| 33 | G/BR | Stepper 1 P3 / DPO | Hi/Lo side driver, 1A max |
| 34 | G/R | Stepper 1 P4 / DPO | Hi/Lo side driver, 1A max |

## Key Notes

**Sensor Supplies — Two Different Voltages:**
- **Pin 9 = +5V DC** (100mA) — for all 5V ratiometric sensors (MAP, TPS, Lowdoller pressure sensors)
- **Pin 12 = +8V DC** (1A) — for 8V sensors, relays, solenoids

**Fuse Block (HT-030102):** Fuse 1: 10A ECU | Fuse 2: 20A Injection | Fuse 3: 15A Ignition | Fuse 4: 20A Fuel Pump | Fuse 5–6: Spare. Max 15A continuous / 20A peak per circuit.
