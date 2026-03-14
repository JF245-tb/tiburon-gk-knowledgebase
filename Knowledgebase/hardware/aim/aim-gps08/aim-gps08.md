# AIM GPS-08 — Pinout and Configuration

**Source:** AIM Sports product documentation; PDM32 tech sheet Ver. 1.17; SmartyCam 3 manual Rev 1.14
**Application:** White Tiburon — GPS module connected to PDM CAN AiM expansion bus via 4-way Data Hub

> **Note:** The GPS-08 is an older AIM GPS module. AIM's current equivalent is the **GPS09c**, referenced in the PDM32 tech sheet (Ver. 1.17). The GPS-08 and GPS09c share the same 5-pin Binder interface and CAN protocol. Either will work with the PDM.

---

## Overview

The AIM GPS-08 (and GPS09c) is a standalone GPS receiver that broadcasts position, speed, and motion data on the AIM CAN bus at 1 Mbps. It requires no configuration in Race Studio 3 — it auto-broadcasts all channels when powered.

**Broadcasts:**
- Latitude / Longitude
- Speed (km/h, mph)
- Heading / course
- Altitude
- Number of satellites locked
- Lateral G-force
- Longitudinal G-force
- GPS status / fix quality

**Key behaviors:**
- Powers on automatically when 12V is applied
- Begins broadcasting within ~30 seconds of acquiring satellite lock
- Channels appear automatically in PDM's Channels tab when CAN AiM bus is live
- SmartyCam receives GPS data via the shared CAN AiM bus (through Data Hub) — no separate GPS wire to SmartyCam

---

## Connector — 5-Pin Binder 712

The GPS-08 connects via a **5-pin Binder 712 male** cable to one of the Data Hub's female ports.

| Pin | Signal | Notes |
|-----|--------|-------|
| 1 | CAN+ | CAN High — AIM CAN AiM bus at 1 Mbps |
| 2 | GND | Ground |
| 3 | +Vb | 12V power in — fed from Data Hub pin 3 |
| 4 | CAN− | CAN Low |
| 5 | n.c. | Not connected *(confirmed: PinoutGPS08_eng.pdf)* |

> **Pin 5 difference from Data Hub:** The 4-way Data Hub uses pin 5 as +VBext (power pass-through). The GPS-08 leaves pin 5 unconnected. The Binder male cable from the hub to the GPS-08 will have pin 5 wired but the GPS-08 ignores it — this is normal and expected.

**Connector at GPS-08:** 5-pin Binder 712 **male** (mates with Data Hub female port)

---

## Tiburon Build — Connection

```
PDM A33 (+Vb out CAN) ────→ Data Hub pin 3 (+Vb) ────→ GPS-08 pin 3 (+Vb)
PDM CAN AiM (A22/A11) ↔ Data Hub CAN+/CAN− ↔ GPS-08 CAN+/CAN−
```

- GPS-08 connects to **Data Hub female port 1** (any port — all are identical)
- Power and CAN from the hub — no dedicated power wire to GPS
- GPS antenna must have clear sky view — route antenna cable as needed

---

## Race Studio 3 — No Configuration Required

The GPS-08 is **not configured** in the PDM's RS3 session. It is not listed in CAN Expansions and has no RS3 setup tab.

| RS3 Location | What You'll See |
|--------------|----------------|
| **Channels** tab | GPS speed, lat/long, heading, altitude, G-forces appear automatically when bus is live |
| **CAN Expansions** tab | GPS-08 does NOT appear here — this tab is for analog/lambda expansion modules only |
| **SmartyCam Stream** tab | Assign GPS-08 speed and G-force channels to SmartyCam overlay slots |

**To confirm GPS-08 is working:**
1. Power the system (IGN on)
2. In RS3 PDM config → Channels tab
3. GPS channels should appear after satellite lock (~30 sec outdoors)
4. Check Live Measures → GPS speed should show a valid value when moving

---

## GPS Antenna Notes

- The GPS-08 has an integrated patch antenna on its top face — must face skyward
- Keep away from metal surfaces directly above the antenna (blocks satellite signal)
- Typical mounting: on roof, windshield dash area, or top of roll cage
- Minimum 5 satellites locked for reliable G-force data; aim for 8+
- GPS09c variant uses an external antenna (SMA connector) — more flexible mounting

---

## Part Numbers

| Item | Part Number |
|------|-------------|
| GPS-08 (integrated antenna) | `X40GPS090050` (50 cm cable) |
| GPS-08 (integrated antenna) | `X40GPS090130` (130 cm cable) |
| GPS-08 (integrated antenna) | `X40GPS090200` (200 cm cable) |
| GPS-08 (integrated antenna) | `X40GPS090400` (400 cm cable) |
| GPS Roof mount (remote antenna) | `X40GPS09R200` / `X40GPS09R400` |

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| No GPS channels in RS3 Channels tab | Bus not live or GPS not powered | Verify LP4 output ON (SafeIgnition); verify hub wiring; check CAN AiM bus |
| GPS channels present but show zeros | No satellite lock | Move outdoors; wait ~30 sec; check antenna orientation (face up) |
| Speed reads incorrectly | GPS ground speed vs. wheel speed conflict | GPS-08 ground speed is more accurate — use for SmartyCam overlay |
| G-force data erratic | Insufficient satellites | Need 5+ for reliable G-forces; 8+ recommended |
| GPS-08 appears in CAN Expansions | — | Not expected — GPS-08 does not show up there |

---

## Related Files

| File | Contents |
|------|----------|
| `hardware/aim/aim-datahub/aim-datahub.md` | Data Hub pinout — GPS-08 connects via hub to PDM CAN AiM |
| `hardware/aim/aim-smartycam/aim-smartycam.md` | SmartyCam receives GPS G-force and speed channels via CAN AiM |
| `hardware/aim/aim-pdm/pdm-pinout.md` | PDM CAN AiM pins (A22/A11/A33) — expansion bus |
| `builds/white-tiburon/guides/pdm-build-guide.md` | LP4 (GPS power) output assignment |
