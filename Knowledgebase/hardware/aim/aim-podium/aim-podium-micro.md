# Autosport Labs PodiumConnect Micro — Pinout, Configuration, and Integration

**Source:** [PodiumConnect Micro Wiki](https://wiki.autosportlabs.com/PodiumConnect_Micro)
**Application:** White Tiburon — real-time telemetry uplink on CAN0 expansion bus via CAN Data Hub port 3
**Serial:** 1QTV5KM (per build-profile.md)

---

## Overview

The PodiumConnect Micro is a compact telemetry bridge that streams CAN bus data to the Podium cloud platform via WiFi/cellular hotspot. It supports real-time dashboards (up to 50 Hz), predictive lap timing, and onboard SD logging (up to 100 Hz). It connects to the AIM CAN expansion bus and reads data broadcast by the PDM/GPS-08/SmartyCam.

**Key capabilities:**
- CAN 2.0 input: reads PDM telemetry, GPS, and ECU data from CAN0 bus
- WiFi 2.4 GHz (802.11b/g/n): AP mode, station mode, or both simultaneously
- Bluetooth LE: TPMS sensors (up to 16), heart rate, driver ID
- Onboard SD card: local logging at up to 100 Hz with network dropout buffering (~1 lap / 3 min)
- Lua scripting: 100 virtual channels for custom calculations
- Predictive lap timing with auto track detection (built-in database)
- Cloud streaming via Podium portal (requires account + streaming key)

---

## Physical Specifications

| Spec | Value |
|------|-------|
| Dimensions | 94 × 61 × 16 mm (3.7 × 2.4 × 0.63 in) |
| Weight | 100 g (3.6 oz) |
| IP Rating | IP65 |
| Operating temp | 0–65°C |
| Power input | 9–24V DC |
| Power consumption | 0.6W max |
| Current draw | ~50 mA @ 12V |

---

## Connector — M8 4-Pin

| Pin | Signal | Wire Color | Notes |
|-----|--------|------------|-------|
| 1 | CAN Low | White | CAN 2.0 data |
| 2 | Power | Red | 9–24V input |
| 3 | CAN High | Green | CAN 2.0 data |
| 4 | Ground | Black | Reference |

> **AIM Integration Cable:** An included Binder 5-pin male to M8 adapter cable connects directly to a Data Hub female port. CAN and power route through the hub — no separate power wire needed.

---

## AIM Integration Cable — Binder to M8 Pin Mapping

| Binder 5-Pin (Hub Female) | Signal | M8 4-Pin (Podium) |
|---------------------------|--------|--------------------|
| Pin 1 (CAN+) | CAN High | Pin 3 (Green) |
| Pin 2 (GND) | Ground | Pin 4 (Black) |
| Pin 3 (+Vb) | 12V Power | Pin 2 (Red) |
| Pin 4 (CAN−) | CAN Low | Pin 1 (White) |
| Pin 5 (+VBext) | Not connected | — |

> Power source: PDM A33 (+Vb out CAN) → Data Hub → Binder pin 3 → M8 pin 2. The Podium is powered whenever the PDM has battery power. At 50 mA draw this is negligible for sleep current.

---

## Tiburon Build — Connection Topology

```
PDM CAN0 (A22/A11, 1 Mbps)
    │
    ▼ expansion cable (female Binder)
[4-Way Data Hub]
    │
    ├── Port 1 → GPS-08        (broadcasts speed, lat/long, G-forces)
    ├── Port 2 → SmartyCam 3   (receives overlay data from PDM)
    ├── Port 3 → Podium Micro  (reads all CAN0 traffic, streams to cloud)
    └── Port 4 → (spare)

Power: Hub +Vb (from PDM A33) → Podium M8 pin 2
CAN: Hub CAN+/CAN− → Podium M8 pin 3/pin 1
```

**No dedicated PDM output needed** — Podium draws power from the CAN bus power rail via the Data Hub. Unlike the SmartyCam (which needs LP3 for its higher power draw), the Podium's 0.6W is easily sourced from the hub's +Vb pass-through.

---

## CAN Bus Configuration

| Parameter | Value |
|-----------|-------|
| Bus | CAN0 (AIM expansion, 1 Mbps) |
| Protocol | CAN 2.0 |
| Baud rate | 1 Mbps (must match AIM bus) |
| Termination | Software-controlled (enable if Podium is the last device on bus) |
| Max channels | 100 CAN channel mappings |

### Required Minimum Channels

These channel names must be defined **exactly** in the CAN mapping:

| Channel | Precision | Source on CAN0 |
|---------|-----------|----------------|
| Speed | 2 decimal (e.g., 33.24 kph) | GPS-08 broadcast |
| Latitude | 6 decimal (decimal degrees) | GPS-08 broadcast |
| Longitude | 6 decimal (decimal degrees) | GPS-08 broadcast |

### Additional Channels Available on CAN0

The PDM broadcasts ECU data (via SmartyCam Stream or direct CAN forwarding) that the Podium can map:

| Channel | Source |
|---------|--------|
| RPM | Haltech → CAN1 → PDM → CAN0 |
| Coolant Temp | Haltech → CAN1 → PDM → CAN0 |
| Oil Pressure | Haltech → CAN1 → PDM → CAN0 |
| TPS | Haltech → CAN1 → PDM → CAN0 |
| Lateral G | GPS-08 direct on CAN0 |
| Longitudinal G | GPS-08 direct on CAN0 |

> **Channel mapping:** The Podium must be configured to decode the AIM CAN protocol. Use the AIM preset in the RaceCapture app, or create a custom CAN mapping matching the PDM's SmartyCam Stream message IDs.

---

## Configuration — RaceCapture App

### Initial Setup (USB to PC)

1. Connect Podium Micro via USB to PC
2. Open **RaceCapture** app (Windows/macOS/Android/iOS)
3. Run first-time setup wizard
4. Set CAN baud rate to **1000000** (1 Mbps)
5. Select **AIM** preset for CAN channel mapping (or configure custom)
6. Map required channels: Speed, Latitude, Longitude at minimum
7. Configure WiFi:
   - **AP mode** for local dashboard viewing (phone connects to Podium)
   - **STA mode** for cloud streaming (Podium connects to your hotspot)
   - Both modes can run simultaneously

### Podium Cloud Setup

1. Create account at [podium.live](https://podium.live)
2. Generate streaming key in portal
3. Enter streaming key in RaceCapture app → Telemetry settings
4. Configure WiFi hotspot credentials (2.4 GHz only, no 5 GHz)
5. Set streaming rate: 1 / 5 / 10 Hz (10 Hz max)

### Dashboard Setup

- Dashboard refresh rate: up to 50 Hz (local WiFi connection)
- Use RaceCapture app on phone/tablet as pit wall dashboard
- Multiple clients can connect simultaneously in AP mode

---

## LED Status Indicators

| Indicator | Meaning |
|-----------|---------|
| Power icon | System powered on |
| Triangle (!) | Error detected |
| Cloud + arrow | Active telemetry streaming |
| ⇄ (two arrows) | CAN bus communication active |
| Top button LED | Data logging in progress |

---

## Bluetooth Features

| Feature | Notes |
|---------|-------|
| TPMS | Up to 16 tire pressure/temp sensors |
| Heart rate | Standard HRP protocol |
| Driver ID | BLE beacon identification |
| Default BT password | 123456 |

---

## Supported Integrations (Presets)

- AIM SmartyCam / PDM / MXG / MXL2
- MoTeC
- VBox (RaceLogic)
- AEM CD-7 with VDM
- Race Technology
- Custom via OBDII PID or manual CAN mapping

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| No CAN data (⇄ LED off) | Baud rate mismatch or no bus traffic | Set baud to 1 Mbps; verify PDM is on and CAN0 active |
| CAN active but no channels | Channel mapping wrong | Use AIM preset or verify custom CAN IDs match PDM SmartyCam Stream |
| No cloud streaming | WiFi not connected to hotspot | Verify 2.4 GHz hotspot; check SSID/password; check streaming key |
| No GPS data in Podium | GPS-08 not broadcasting on CAN0 | Verify GPS-08 powered and connected to hub; check GPS lock |
| Power LED off | No +Vb from hub | Check Data Hub connection; verify PDM powered; check M8 cable |
| SD card not logging | Card not inserted or full | Insert ≥2 GB SD card; check available space |
| Podium not detected via USB | Driver issue | Try different USB cable; install RaceCapture app drivers |

---

## Related Files

| File | Contents |
|------|----------|
| `hardware/aim/aim-datahub/aim-datahub.md` | Data Hub pinout — Podium connects to hub port 3 |
| `hardware/aim/aim-smartycam/aim-smartycam.md` | SmartyCam config — shares CAN0 bus with Podium |
| `hardware/aim/aim-gps08/aim-gps08.md` | GPS-08 — provides speed/position data Podium reads |
| `hardware/aim/aim-pdm/pdm-pinout.md` | PDM CAN0 pins (A22/A11/A33) |
| `builds/white-tiburon/guides/pdm-build-guide.md` | PDM RS3 config — SmartyCam Stream channels Podium can decode |
| `builds/white-tiburon/build-profile.md` | Build profile — Podium Micro SN: 1QTV5KM, mounted in passenger footwell |
