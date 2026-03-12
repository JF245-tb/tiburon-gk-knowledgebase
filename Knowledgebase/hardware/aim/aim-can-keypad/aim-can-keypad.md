# AIM CAN Keypad 12 (Blink Marine PKP-2600-SI)

**Manufacturer:** Blink Marine (AIM resells as "AIM CAN Keypad 12" — same hardware)
**Model:** PKP-2600-SI
**Datasheet:** `AIM PDM/PKP_2600_SI_Datasheet_REV1.pdf`
**Application:** White Tiburon — primary cockpit control panel, CAN2 bus

---

## Overview

12-key CAN keypad with RGB LED indicators and interchangeable 15 mm icon inserts.
IP67/IP69K rated — suitable for open cockpit / race car use.
CANopen / J1939 protocol. Connected to PDM CAN2 bus at 125 kbps.

---

## Electrical Specifications

| Parameter | Value |
|---|---|
| Supply voltage | 12–24V nominal (8–32V range) |
| Standby current | < 50 mA |
| Communication | CANopen, J1939 |
| MTBF | 204,291 hours (MIL-HDBK-217, ground mobile) |
| Operating temp | −40°C to +70°C |
| Storage temp | −40°C to +85°C |
| Ingress protection | IP67 / IP69K |
| Weight | 230 g (inserts excluded) |
| Switch life | 3 million operations per key |

---

## Connector — Deutsch DT04-4P

Standard 4-pin Deutsch connector, wire-side view:

```
  4   3
  1   2
```

| Pin | Wire Color | Function |
|---|---|---|
| 1 | Blue | CAN L |
| 2 | White | CAN H |
| 3 | Black | GND (negative battery) |
| 4 | Red | Vbatt (12–24V) |

> The device is polarity protected.

---

## PDM Wiring (White Tiburon)

Custom **5-pin Binder 712 female → 4-pin Deutsch DT04-4P male** cable.
Binder end plugs into PDM Connector A (black). Deutsch end plugs into keypad.

| PDM Pin | Connector | Signal | Binder Pin | Cable Color | Deutsch Pin | Keypad Color |
|---|---|---|---|---|---|---|
| **A21** | Black | LP8 (keypad power) | 1 | Red | 4 | Red (Vbatt) |
| **A28** | Black | CAN2 High | 2 | White | 2 | White (CAN H) |
| — | — | Spare | 3 | Yellow | — | — |
| **A29** | Black | CAN2 Low | 4 | Green | 1 | Blue (CAN L) |
| **B18** | **Grey** | GND | 5 | Black | 3 | Black (GND) |

> **Color mismatch:** Green (cable) → Blue (keypad) for CAN L. Label the loom.
> **GND note:** A10 is committed to the CAN0 expansion cable. Keypad GND uses B18 (grey connector) — same ground plane, different physical pin.
> **Do NOT use CAN0 (A11/A22)** — that bus is AIM expansion at 1 Mbps. Keypad requires CAN2 at 125 kbps.

### LP8 Power Output Config (Race Studio 3)

| Setting | Value |
|---|---|
| Output | LP8 (A21) |
| Name | `Keypad` |
| Mode | OVC Protected |
| Max load | 5A |
| Trigger | `SafeIgnition` |

---

## Physical Layout

**Dimensions:** 181.5 mm × 70.0 mm × 15.2 mm (7.15" × 2.76" × 0.60")
**Mounting footprint:** 135.5 mm (5.33") between studs × 16.3 mm (0.64") inset from edge
**Body depth:** 165.0 mm (6.50") along long axis
**Mounting:** 2× #10-32 UNC steel studs — max torque **1.8 Nm (16 lbf-in)**
**Gasket:** Rubber molded on backside acts as panel gasket — no separate seal required.

### Key Numbering (physical, face-on view)

```
[ 6 ][ 5 ][ 4 ][ 3 ][ 2 ][ 1 ]   ← top row
[12 ][11 ][10 ][ 9 ][ 8 ][ 7 ]   ← bottom row
```

Key 1 = top-right, Key 12 = bottom-left.

### Race Studio 3 Button Assignment (White Tiburon)

| Physical Key | RS3 ID | Function | Type | LED Rest | LED Active |
|---|---|---|---|---|---|
| 1 | K01 | Start | Momentary | White | Green |
| 2 | K02 | Horn | Momentary | White | Amber |
| 3 | K03 | Lights | Multistatus (3-pos) | White | Blue / Cyan |
| 4 | K04 | Coolsuit | Toggle | White | Cyan |
| 5 | K05 | Fan Override | Toggle | White | Red |
| 6 | K06 | Fuel Override | Toggle | White | Red |
| 7 | K07 | Pit Limiter | Toggle + timing | White | Green (armed) / Red (active) |
| 8 | K08 | Wiper | Multistatus (3-pos) | White | Blue / Cyan |
| 9 | K09 | Comms Yes/No | Toggle | White | Green |
| 10 | K10 | Pit-In Laps | Multistatus (4-pos) | White | White/Amber/Red |
| 11 | K11 | Spare | — | — | — |
| 12 | K12 | Spare | — | — | — |

> **Note:** The mapping of physical key numbers to Race Studio 3 K-numbers depends on how RS3 enumerates the keypad. Confirm physical layout after first connection with the PDM by pressing each key and observing which K-number lights up in Live Measures.

---

## CAN Bus Settings

| Setting | Value |
|---|---|
| Bus | CAN2 (PDM A28 H / A29 L) |
| Speed | 125 kbps |
| Protocol | CANopen (Device Profile 401d) / J1939 |
| Address | Configurable via Race Studio 3 or J1939 address claim |

---

## Mechanical Notes

- Vertical or horizontal mount — symmetrical design
- Inserts are interchangeable 15 mm; thousands of stock icons at blinkmarine.com
- Membrane compensation valve self-balances internal pressure with temperature changes
- Rubber backside gasket seals mounting holes against liquid intrusion
- Polarity protected — reversed power connection will not damage the device

---

## Related Files

| File | Contents |
|---|---|
| `AIM PDM/PKP_2600_SI_Datasheet_REV1.pdf` | Source datasheet (Blink Marine) |
| `hardware/aim/aim-pdm/pdm-pinout.md` | PDM connector pinout — CAN2, LP8, B18 locations |
| `builds/white-tiburon/guides/pdm-config.md` | Full PDM configuration including keypad button logic |
| `builds/white-tiburon/guides/pdm-session-1.md` | Step-by-step RS3 setup for CAN2 Keypad tab |
