# CAN Keypad Configuration — Future Reference
## Preserved for When a CAN Keypad Is Added to the White Tiburon

> **Status:** CAN keypad is NOT installed on this car. All driver controls use a physical switch panel.
> This file preserves the planned keypad button assignments, LED colors, and variable names
> so they can be re-imported into Race Studio 3 when a keypad is connected.
>
> **Variable names are kept consistent** with the physical switch config. When a keypad is added,
> the trigger logic uses OR to combine both inputs:
> `STARTER_SAFE = (StarterKYD OR Ch01) AND SafeIgnition AND NOT ENGINE_RUNNING`
> This means both the keypad button and the physical switch work simultaneously.

---

## Hardware

| Item | Value |
|------|-------|
| Device | AIM CAN Keypad 12 (Blink Marine PKP-2600-SI) |
| Buttons | 12 RGB-backlit |
| Connector | 4-pin Deutsch DT04-4P |
| Bus | CAN2 (PDM A28 H / A29 L) — **125 kbps only** |
| Power | PDM LP8 (A21) — OVC Protected, 5A, SafeIgnition trigger |
| GND | PDM B18 (NOT A10 — that's reserved for CAN0 expansion cable) |
| Hardware spec | `hardware/aim/aim-can-keypad/aim-can-keypad.md` |

> **Do NOT wire keypad to CAN0 (A22/A11).** CAN0 runs AIM expansion devices at 1 Mbps. Keypad at 125 kbps on CAN0 = both buses fail.

---

## CAN2 Keypad Cable — Binder-to-Deutsch Custom Cable

| Binder Pin | Amazon Color | PDM Pin | Connector | Deutsch Pin | Keypad Color | Signal |
|-----------|-------------|---------|-----------|------------|-------------|--------|
| 1 | Red | A21 (LP8 — Keypad power) | Black | 4 | Red | Vbatt |
| 2 | White | A28 (CAN2 High) | Black | 2 | White | CAN H |
| 3 | Yellow | — | — | — | — | Spare — not connected |
| 4 | Green | A29 (CAN2 Low) | Black | 1 | Blue | CAN L |
| 5 | Black | B18 (GND) | Grey | 3 | Black | GND |

> Green (Binder) → Blue (Deutsch) for CAN L — only color mismatch. Label the loom.

---

## Button Assignments (K33–K44)

Race Studio 3 → CAN2 Keypad tab. Bus speed = **125 kbps**.

### K33 — Starter
- **Variable:** `StarterKYD`
- **Type:** Momentary — crank only while held
- Rest: label `RDY`, value `0`
- Active: label `CRNK`, value `1`
- Timing: NO

### K34 — Horn
- **Variable:** `HornKYD`
- **Type:** Momentary
- Rest: label `OFF`, value `0`
- Active: label `HORN`, value `1`

### K35 — Lights
- **Variable:** `LightsKYD`
- **Type:** Multistatus (3 positions)
- Position 0: label `OFF`, value `0`
- Position 1: label `LOW`, value `1`
- Position 2: label `HIGH`, value `2`

### K36 — Coolsuit
- **Variable:** `CoolsuitKYD`
- **Type:** Toggle
- Rest: label `OFF`, value `0`
- Active: label `ON`, value `1`

### K37 — Fan Override
- **Variable:** `FanKYD`
- **Type:** Toggle
- Rest: label `OFF`, value `0`
- Active: label `ON`, value `1`

### K38 — Fuel Override
- **Variable:** `FuelOverride`
- **Type:** Toggle
- Rest: label `OFF`, value `0`
- Active: label `ON`, value `1`

### K39 — Pit Limiter
- **Variable:** `PitLimiter_KYD`
- **Type:** Toggle + timing
- Rest: label `OFF`, value `0`
- Active: label `PIT`, value `1`
- Timing: YES
  - Short press: toggles state
  - Long press (2000 ms): label `CLEAR`, value `0` — forces OFF

### K40 — Comms
- **Variable:** `COMMS_YN`
- **Type:** Toggle
- Rest: label `NO`, value `0`
- Active: label `YES`, value `1`

### K41 — Pit-In Laps
- **Variable:** `PITIN_LAPS`
- **Type:** Multistatus (4 positions)
- Position 0: label `---`, value `0`
- Position 1: label `L+1`, value `1`
- Position 2: label `L+2`, value `2`
- Position 3: label `L+3`, value `3`

### K42 — Wiper
- **Variable:** `WiperKYD`
- **Type:** Multistatus (3 positions)
- Position 0: label `OFF`, value `0`
- Position 1: label `SLOW`, value `1`
- Position 2: label `FAST`, value `2`

### K43–K44 — Spare
Unconfigured.

---

## LED Color Assignments

**Available colors:** White · Red · Green · Blue · Amber · Magenta · Cyan

**Design rule:** Rest = White (uniform illumination). Active = function color (visible against white background).

### Simple Buttons

| Button | Function | Rest | Active |
|---|---|---|---|
| K33 | Starter | White | Green |
| K34 | Horn | White | Amber |
| K36 | Coolsuit | White | Cyan |
| K37 | Fan Override | White | Red |
| K38 | Fuel Override | White | Red |
| K40 | Comms | White | Green |

### K35 — Lights (Multistatus)

| Position | Label | Color |
|---|---|---|
| 0 | OFF | White |
| 1 | LOW | Blue |
| 2 | HIGH | Cyan |

### K39 — Pit Limiter (Two-Condition)

Priority order (highest first):
1. `PITLIMITER_ACTIVE = 1` → **Red** (limiter clamping speed)
2. `PitLimiter_KYD = 1` → **Green** (armed, speed gate not met)
3. Rest → **White**

### K41 — Pit-In Laps (Traffic Light Countdown)

| Position | Label | Color |
|---|---|---|
| 0 | --- | White |
| 1 | L+1 | Red |
| 2 | L+2 | Amber |
| 3 | L+3 | Green |

### K42 — Wiper (Multistatus)

| Position | Label | Color |
|---|---|---|
| 0 | OFF | White |
| 1 | SLOW | Blue |
| 2 | FAST | Cyan |

---

## Trigger Logic — Combined Keypad + Physical Switch

When keypad is installed, update these Math Channel triggers to use OR:

| Status Variable | Current (Physical Only) | With Keypad |
|---|---|---|
| `STARTER_SAFE` | Ch01 AND SafeIgnition AND NOT ENGINE_RUNNING | **(StarterKYD OR Ch01)** AND SafeIgnition AND NOT ENGINE_RUNNING |
| Fan low override | Ch02 | **(FanKYD OR Ch02)** |
| Fan high override | Ch03 | **(FanKYD OR Ch03)** |
| Coolsuit | Ch10 AND SafeIgnition | **(CoolsuitKYD OR Ch10)** AND SafeIgnition |
| Horn | Fuse box spade (Phase 1) | **HornKYD** → MP horn output |
| Lights | SafeIgnition (always on) | **LightsKYD** → position 1 = low, position 2 = high |
| Wiper | Ch05 AND NOT Ch06 / Ch06 | **(WiperKYD=1 AND NOT WiperKYD=2 OR Ch05 AND NOT Ch06)** / **(WiperKYD=2 OR Ch06)** |
| Fuel override | (none — cycle IGN) | **FuelOverride** → HP3 trigger |
| Pit limiter | (not available) | **PITLIMITER_SAFE AND NOT (TPS > 60)** |
| Comms | (not available) | **COMMS_YN** direct from K40 |
| Pit-in laps | (not available) | **PITIN_LAPS** direct from K41 |

---

## PDM Changes Required When Adding Keypad

1. **Enable CAN2** in Race Studio 3 → set speed to 125 kbps
2. **Re-enable LP8** as keypad power output (if repurposed — currently LP8 = AltExciter)
   - LP8 is currently used for alternator exciter. Either:
     - Use a different LP output for keypad power
     - OR move alt exciter to another spare output
3. **Add keypad buttons** per assignments above
4. **Add LED colors** per table above
5. **Update Math Channels** to OR keypad + physical switch inputs (see table above)
6. **Wire CAN2 cable** — Binder-to-Deutsch per table above

---

## Cross-References

| File | Contents |
|------|----------|
| `hardware/aim/aim-can-keypad/aim-can-keypad.md` | Full keypad hardware spec |
| `hardware/aim/aim-pdm/pdm-pinout.md` | CAN2 pins A28/A29, LP8 A21 |
| `guides/pdm-build-guide.md` | Current physical switch config, Race Studio walkthrough (authoritative) |
