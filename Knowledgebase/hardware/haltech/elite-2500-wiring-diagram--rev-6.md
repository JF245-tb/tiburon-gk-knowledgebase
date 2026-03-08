# Haltech Elite 2500 Wiring Diagram — Rev 6
**Source:** `Haltech/Elite 2500 Wiring Diagram - Rev 6.pdf`

> This is a full wiring schematic showing example connections for all ECU circuits.
> The raw diagram text is not useful as a lookup reference — use the connector pinout files instead.
> For the White Tiburon's specific wire routing, see `builds/white-tiburon/signal-routing.md`.

---

## Key Reference Files

| What you need | File |
|---|---|
| 34-pin connector (A) — injectors, ignition, power, AVI | `hardware/haltech/main-connector-34-pin-elite2500.md` |
| 26-pin connector (B) — crank/cam, knock, CAN, AVI | `hardware/haltech/main-connector-26-pin-elite2500.md` |
| End-to-end signal traces for white Tiburon | `builds/white-tiburon/signal-routing.md` |
| Full schematic diagram (visual) | `Haltech/Elite 2500 Wiring Diagram - Rev 6.pdf` |

---

## Wiring Diagram Highlights (from Rev 6)

### Fuse Block (HT-030102) — 6 Circuits
| Fuse | Rating | Circuit |
|------|--------|---------|
| 1 | 10A | ECU power |
| 2 | 20A | Injection |
| 3 | 15A | Ignition |
| 4 | 20A | Fuel pump |
| 5–6 | — | Spare |

### Power Distribution (34-pin Connector A)
- **Pin 9** (O) = +5V DC, 100mA — ratiometric sensors (MAP, TPS, Lowdoller pressure)
- **Pin 12** (O/W) = +8V DC, 1A — 8V sensors, relays, solenoids
- **Pin 13** (P) = 12V Ignition input — 12V on IGN and cranking only
- **Pins 10/11** (B) = Battery ground — connect both to battery negative
- **Pin 26** (R/L) = ECU Injector Power Input — **required**, 12V from injector relay/fuse

### Signal Grounds (26-pin Connector B)
- **Pins 14/15/16** (B/W) = Signal ground — all sensor grounds here

### CAN Bus (26-pin Connector B)
- **Pin 23** (W) = CAN H → PDM CAN0 (A22) at 500 kbps
- **Pin 24** (L) = CAN L → PDM CAN0 (A11) at 500 kbps

### Ignition Outputs (34-pin Connector A)
- Pins 3–8: IGN 1–6 (Y/B, Y/R, Y/O, Y/G, Y/BR, Y/L) — 1A max, ground-side trigger
- Pins 17–18 (26-pin): IGN 7–8 (Y/V, Y/GY) — not used on G6BA 6-cyl

### Injector Outputs (34-pin Connector A)
- Pins 19–22, 27–28: INJ 1–6 (L, L/B, L/BR, L/R, L/O, L/Y) — current controlled, 0–8A peak

### DPO Assignments (typical)
| DPO | Pin | Wire | Pull-up | Common use |
|-----|-----|------|---------|------------|
| DPO 1 | A18 | V/B | User-defined | Tacho output |
| DPO 2 | A1 | V/BR | Fixed 5V | Speed output |
| DPO 3 | A23 | V/R | Fixed 12V | Available |
| DPO 4 | B19 | V/O | Fixed 12V | Available / REM enable |
| DPO 5 | A24 | B/Y | Fixed 12V | Fuel pump trigger |
| DPO 6 | A25 | B/R | Fixed 12V | ECR out |
