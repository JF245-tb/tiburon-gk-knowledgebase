# AIM CAN Data Hub — 2-Way and 4-Way

**Source:** `Pinout_DataHub_101_eng.pdf` (AIM Sports, Release 1.01)
**Application:** White Tiburon — connects GPS-08, SmartyCAM, and Podium module to PDM CAN0 expansion bus

---

## Overview

The AIM CAN Data Hub is a **passive CAN bus repeater/splitter**. It has no processor, no USB port, no firmware, and no standalone configuration. It is electrically transparent — all CAN+/CAN- signals and power rails are simply connected together across all ports.

> **Critical:** The hub cannot be connected to a PC via USB — it has no USB interface. You cannot "read" the hub directly in RS3. RS3 sees the **devices connected to the hub** (GPS-08, SmartyCAM), not the hub itself.

---

## Variants

| Model | Male ports (master) | Female ports (devices) |
|-------|--------------------|-----------------------|
| 2-way | 1× 5-pin male Binder | 2× 5-pin female Binder |
| 4-way | 1× 5-pin male Binder | 4× 5-pin female Binder |

---

## Connector Pinout — All Ports (Male and Female)

Both the male (master) connector and all female (device) connectors share the same pin assignment. The hub is straight-through on all signals.

| Pin | Signal | Notes |
|-----|--------|-------|
| 1 | CAN+ | CAN High data line |
| 2 | GND | Ground |
| 3 | +Vb | Power (12V) — fed from master device, distributed to all device ports |
| 4 | CAN− | CAN Low data line |
| 5 | +VBext | External power input — passed through |

**Connector type:** 5-pin Binder 712 series
- Master port: **male** Binder (connects to PDM expansion cable female, or SmartyCAM, etc.)
- Device ports: **female** Binder (connects to GPS-08, SmartyCAM, Podium male cables)

---

## Physical Identification

- Red cable with red/black wires visible on the hub body — these are the +VBext power leads
- The male connector end is the "input" / master side
- All female connectors are "output" / device sides — identical pinout

---

## Tiburon Build — Connection Topology

```
PDM expansion cable (female Binder, CAN0)
        │
        ▼
[CAN Data Hub — male Binder port]
        │
        ├── Female port 1 → GPS-08
        ├── Female port 2 → SmartyCAM
        ├── Female port 3 → Podium module
        └── Female port 4 → (spare)
```

Power flows: PDM A33 (+Vb out CAN) → Hub pin 3 (+Vb) → distributed to all device ports
CAN bus: PDM **CAN AiM** (A22 H / A11 L) ↔ Hub CAN+/CAN− ↔ all connected devices at 1 Mbps

---

## PDM Expansion Cable ↔ Hub Male — Pin Mapping

When the PDM's female expansion cable mates with the hub's male connector:

> **Note on connector orientation:** The user-confirmed continuity pin numbers reflect the Binder connector viewed from the solder/back side. When the male and female physically mate, the CAN signals align correctly — CAN0 High (A22) connects to hub CAN+, CAN0 Low (A11) connects to hub CAN−, +Vb out (A33) powers the hub, GND (A10) grounds it, and +Vb ext (A32) connects to hub's +VBext pass-through.

| PDM Conn A Pin | Signal | Hub Signal | Hub Pin |
|---------------|--------|-----------|---------|
| A22 | CAN0 High | CAN+ | 1 |
| A11 | CAN0 Low | CAN− | 4 |
| A33 | +Vb out CAN | +Vb | 3 |
| A10 | GND | GND | 2 |
| A32 | +Vb ext CAN | +VBext | 5 |

---

## CAN Bus Notes

- **Speed:** 1 Mbps (AIM internal protocol)
- **Termination:** The hub itself has no built-in termination resistors. Termination must be provided at the two **ends** of the bus — typically at the PDM and at the last device. Check individual device documentation for built-in termination.
- **Bus topology:** The hub creates a star topology from a single PDM CAN0 connection. All devices share the same CAN bus segment.

---

## RS3 Configuration — What to Expect

| Item | Where in RS3 (PDM config) |
|------|--------------------------|
| GPS-08 channels (speed, lat/long, heading) | Should appear automatically in **Channels** tab once bus is live |
| SmartyCAM overlay data (what PDM sends TO cam) | **SmartyCam Stream** tab |
| Hub configuration | **None required** — hub is transparent |
| GPS-08 device config | None required. GPS-08 auto-broadcasts speed, position, and G-force data on CAN AiM bus when powered. Channels appear in PDM Channels tab when bus is live. |

> **Making PDM the master over SmartyCAM:** Configured in RS3 → SmartyCam Stream tab. The PDM sends RPM, speed, temperatures, and other channels to the SmartyCAM for video overlay. See `aim-smartycam.md` for SmartyCam pinout and configuration.

---

## Troubleshooting

| Symptom | Likely Cause |
|---------|-------------|
| Hub "not detected" in RS3 | Expected — hub has no RS3 presence. Check DEVICES (GPS-08, SmartyCam) not the hub |
| USB connection to hub fails | Hub has no USB port. Cannot connect directly |
| PDM can't see GPS/SmartyCam on bus | Check: (1) devices powered, (2) CAN bus termination, (3) CAN AiM bus is always-on at 1 Mbps — no RS3 configuration needed for the bus itself |
| GPS channels not in PDM Channels tab | Verify bus is live — GPS-08 broadcasts automatically when powered and on bus |

---

## Related Files

| File | Contents |
|------|----------|
| `hardware/aim/aim-pdm/pdm-pinout.md` | PDM CAN expansion cable pinout — CAN0 signals |
| `hardware/aim/aim-smartycam/aim-smartycam.md` | SmartyCAM pinout, RS3 config, master device setup |
| `builds/white-tiburon/guides/pdm-config.md` | CAN bus assignments — CAN0 AIM expansion bus |
| `hardware/aim/aim-gps08/aim-gps08.md` | GPS-08 pinout, CAN behavior, part numbers |
| `Pinout_DataHub_101_eng.pdf` | Source AIM document — original pinout diagrams |
