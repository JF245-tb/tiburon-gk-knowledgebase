# Hardware — Device Reference Documentation

**Rule:** This directory contains **generic device documentation only** — pinouts, wiring diagrams, and specs that apply to any installation of a given device. Car-specific configuration guides live in `builds/{car}/`.

| What belongs here | What belongs in `builds/{car}/` |
|---|---|
| Haltech Elite 2500 connector pinout | Which Haltech pin connects to which sensor on a specific car |
| AIM PDM 32 connector pinout | Race Studio config guide for a specific car |
| Lowdoller sensor wiring spec | Which AVI input a specific sensor is assigned to |
| Toyota COP coil connector pinout | COP wiring for a specific ignition setup |

---

## Contents

### `haltech/` — Haltech Elite 2500

| File | Contents |
|---|---|
| `main-connector-26-pin-elite2500.md` | Full 26-pin connector reference: triggers, AVI, DPO, CAN, signal grounds |
| `main-connector-34-pin-elite2500.md` | Full 34-pin connector reference: ignition (IGN1–6), injectors (INJ1–6), sensor supply, AVI |
| `elite-2500-wiring-diagram--rev-6.md` | Rev 6 wiring diagram highlights (fuse block, power pins, CAN, ignition outputs) |
| `rem-harness-diagram.md` | Remote harness (REM) wiring diagram |

### `aim/` — AIM Sports Devices

All AIM Sports hardware lives here. The `hardware-graph.json` at the root of `hardware/` captures device capabilities and connectivity for the full AIM system.

#### `aim/aim-pdm/` — AIM PDM 32

| File | Contents |
|---|---|
| `pdm-pinout.md` | Full 35-pin ×2 connector pinout (Conn A and B); CAN bus pin assignments (CAN0=A22/A11, CAN1=A30/A31, CAN2=A28/A29) |
| `pdm-configuration-guide.md` | Logic architecture: keypads → status variables → triggers → outputs; PWM fan example; PDM32 + 10" dash specs |

#### `aim/aim-datahub/` — AIM CAN Data Hub

| File | Contents |
|---|---|
| `aim-datahub.md` | 2-way and 4-way hub pinout (5-pin Binder 712); passive bus splitter; PDM ↔ GPS-08 / SmartyCam / Podium topology; PDM expansion cable ↔ hub pin mapping |

#### `aim/aim-gps08/` — AIM GPS-08 / GPS09c

| File | Contents |
|---|---|
| `aim-gps08.md` | 5-pin Binder 712 pinout (pin 5 = n.c., confirmed from AIM PDF); auto-broadcast channels (speed, GPS, G-forces); no RS3 config required; part numbers for all cable lengths |

#### `aim/aim-smartycam/` — AIM SmartyCam 3 Series

| File | Contents |
|---|---|
| `aim-smartycam.md` | All 5 model variants and connectors (Sport/Dual/GP/GP Pro/Corsa); RS3 two-session workflow (PDM SmartyCam Stream tab + SmartyCam USB-C/SD config); channel assignment table; LED behavior; troubleshooting |

> **Adding AIM devices:** Podium module, LCU-One CAN wideband, and future AIM accessories go in new subfolders under `aim/`. Add a node to `hardware-graph.json` for each new device.

### `sensors/` — Sensors & Actuators

| File | Contents |
|---|---|
| `lowdoller-sensors.md` | Combo sensor specs (Lowdoller 899402–899409): PTC thermistor, pressure range, wiring, +5V supply |
| `cop-ignition.md` | Toyota 90919-A2005 COP: connector pinout (A=GND, B=trigger, C=feedback, D=12V), dwell, NSP settings |

---

## Car-Specific Config Lives Here

| Car | Config files |
|---|---|
| White Tiburon | `builds/white-tiburon/guides/` — Race Studio config guide + session 1 walkthrough |
| White Tiburon | `builds/white-tiburon/cluster-integration.md` — OEM cluster wiring into Haltech |
