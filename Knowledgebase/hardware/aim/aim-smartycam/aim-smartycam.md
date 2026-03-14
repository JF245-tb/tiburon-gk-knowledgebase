# AIM SmartyCam 3 Series — Pinout, Configuration, and PDM Integration

**Source:** AIM SmartyCam 3 User Manual Rev 1.14 (`SmartyCam3_114_eng.pdf`)
**Application:** White Tiburon — HD video overlay camera connected to PDM CAN0 expansion bus via CAN Data Hub

---

## Overview

The AIM SmartyCam 3 is a self-contained HD video recorder (1920×1080) with CAN bus interface. It captures onboard footage and overlays real-time telemetry data received from a master device (PDM, MXG, MXL2, etc.) on the AIM CAN bus. It has an **internal rechargeable lithium battery** that can sustain the camera for a short period (~20 min) if external power is lost.

**Key capabilities:**
- Full HD recording: 1920×1080 @ 30fps (Sport) or 60fps (Dual/GP/GP Pro/Corsa)
- Internal lithium battery — survives brief power loss
- Records video + telemetry into a single `.mp4` file (data stored as metadata)
- Can operate standalone with GPS-08, or as slave to CAN master (PDM)
- Auto-starts recording when master device starts recording (when connected to master)
- MicroSD (Sport) or SD card (others) up to 2TB
- USB-C for RS3 config and video download (all except Sport — Sport uses SD card only)
- External power: **9–15V**, ~500–800mA typical

---

## Model Variants and Connectors

There are five SmartyCam 3 variants with different connectors. Identify your model from the label on the camera.

| Model | CAN/Power Connector | GPS Connection | USB | Notes |
|-------|---------------------|----------------|-----|-------|
| **Sport** | 1× 5-pin Binder 712 female (single connector — power + CAN) | Through 2-way Data Hub on same connector | None | MicroSD only; no display; most compact |
| **Dual** | 1× 22-pin Deutsch female harness | Via 22-pin harness "EXP" wires | USB-C + Ethernet | Dual camera, 3G-SDI video out |
| **GP** | 1× 7-pin Binder female (main) + 1× 5-pin Binder female labeled "EXP" | "EXP" 5-pin Binder connects to GPS/Data Hub | USB-C | Bullet camera; 3G-SDI video out |
| **GP Pro** | 2× 5-pin Deutsch male (blue key) | "EXP" port to GPS/Data Hub | USB-C | 64GB internal memory, 3G-SDI video out |
| **Corsa** | 1× 7-pin Binder female (main) + 1× 5-pin Binder female labeled "EXP" + 1× 5-pin Binder female labeled "GPS" | "EXP" to Data Hub OR "GPS" to GPS-08 direct | USB-C | Racing-focused; no video out |

> **Determine your model** — the "EXP" 5-pin Binder port is the AIM expansion bus connection for GP and Corsa. For the Sport, the single connector handles everything. Connect the Data Hub male cable to whichever port is labeled for GPS/expansion.

---

## 5-Pin Binder (EXP/CAN Port) — Pinout

All 5-pin Binder connections in the AIM ecosystem share the same standard pinout. The SmartyCam "EXP" port (or Sport single port) connects to the Data Hub:

| Pin | Signal | Notes |
|-----|--------|-------|
| 1 | CAN+ | CAN High |
| 2 | GND | Ground |
| 3 | +Vb | 12V power in — fed from Data Hub |
| 4 | CAN− | CAN Low |
| 5 | +VBext | External power — pass-through |

**Connector type (at SmartyCam):** 5-pin Binder 712 **female** (mates with male cable from Data Hub female port)

> **Note on Sport model:** The Sport uses a 2-way Data Hub to split the GPS-08 and power connections through its single 5-pin Binder port. For the GP/Corsa models with a 4-way hub, the "EXP" port connects directly to one of the hub's female device ports.

---

## 7-Pin Binder (Main Power Connector — GP and Corsa)

The SmartyCam 3 GP and Corsa have a separate **7-pin Binder female** connector for main power, video output, and additional signals. Pinout is image-only in the PDF (text not extractable). Key wires from the standard harnesses:

- **Red wire** → +12V external power (main power input)
- **Black wire** → GND

> Power the camera from **PDM LP3 (A16, 10A OVC)** via this connector if your model has the 7-pin main connector. If your model only has the 5-pin Binder (Sport), power comes through the Binder pin 3 via the Data Hub.

---

## Tiburon Build — Connection Topology

```
PDM LP3 (A16, SafeIgnition) ─────────────────────────────────→ SmartyCam 12V power
                                                                (7-pin Binder main, or via hub if Sport)

PDM CAN0 (A22/A11, 1 Mbps)
    │
    ▼ expansion cable (female Binder)
[4-Way Data Hub]
    │
    ├── Port 1 → GPS-08     (broadcasts speed, lat/long, G-forces on CAN0)
    │
    ├── Port 2 → SmartyCam  (receives overlay data from PDM; also gets GPS data from GPS-08 via same bus)
    │            (5-pin Binder "EXP" port)
    │
    ├── Port 3 → Podium module
    │
    └── Port 4 → (spare)
```

**CAN bus:** All devices on CAN0 at 1 Mbps. PDM = master. SmartyCam = slave. Hub is passive/transparent.

---

## Configuration — Two Separate RS3 Sessions

SmartyCam configuration requires **two distinct RS3 sessions**:

| Session | RS3 Connected To | What It Configures |
|---------|------------------|--------------------|
| **A — PDM config** | USB to PDM | SmartyCam Stream tab: which channels PDM broadcasts to SmartyCam |
| **B — SmartyCam config** | USB-C to SmartyCam (or SD card) | CAN Protocol, Overlay layout, video settings, GPS, start/stop conditions |

**Order:** Either session can be done first. Both are required for full functionality. Session A (PDM side) is where most setup time is spent.

---

## Session A: PDM RS3 Config → SmartyCam Stream Tab

**Connected via USB to PDM. Navigate to SmartyCam Stream tab (rightmost tab).**

### RS3 SmartyCam Stream Tab Fields

| Field | Setting | Notes |
|-------|---------|-------|
| Enabled | **Yes** | Must be ON for PDM to transmit to SmartyCam |
| CAN Bus | **CAN AiM** | AIM expansion bus — SmartyCam is on CAN AiM bus via Data Hub |
| Protocol | **AiM Default** or **Advanced** | Default covers most channels; Advanced allows custom channel set |
| Stream name | Give a recognizable name | Saved with PDM config |

**Setting individual channels:** Click each channel slot → a panel shows all channels/sensors that match that function. If you can't find the channel you need, check **"Enable all channels for functions"** — this reveals all available channels, not just type-matched ones. *(Source: PDM32 User Guide §18)*

### Default Protocol Channels (AiM Default)

AiM Default Protocol sends a fixed channel set sufficient for most installations. Channels the PDM can include:

| SmartyCam Channel | PDM Source | Notes |
|-------------------|-----------|-------|
| Engine Speed (RPM) | CAN1 — Haltech | Received by PDM from Haltech ECU Stream |
| Speed | CAN0 — GPS-08, or CAN1 Haltech | GPS-08 ground speed preferred |
| Gear | CAN1 — Haltech | Calculated by Haltech |
| Water Temperature | CAN1 — Haltech (AVI6, Lowdoller ECT) | In °C |
| Oil Pressure | CAN1 — Haltech (AVI3, Lowdoller oil P) | In PSI or bar |
| Throttle Position | CAN1 — Haltech (AVI10, TPS) | 0–100% |
| Lateral G | CAN0 — GPS-08 | GPS-08 broadcasts G forces |
| Longitudinal G | CAN0 — GPS-08 | GPS-08 broadcasts G forces |

> **Flow:** Haltech → CAN1 → PDM ECU Stream → PDM SmartyCam Stream → CAN0 → SmartyCam overlay. PDM acts as a bridge; SmartyCam receives Haltech data without any direct Haltech–SmartyCam connection.

### Advanced Protocol

If you need channels not in the default set:
1. In PDM RS3 config → SmartyCam Stream → select **Advanced**
2. Create a custom stream: define CAN message IDs and byte assignments
3. Name and save the protocol
4. In the SmartyCam's own RS3 config (Session B) → CAN Protocol tab → import the saved protocol
5. Map imported channels to overlay fields

---

## Session B: SmartyCam RS3 Config (USB-C to SmartyCam or SD Card)

**Connected via USB-C directly to SmartyCam (GP/Corsa/GP Pro) or via SD card (Sport/all models).**

### How to Load Config via SD Card (All Models)
1. In RS3, create/edit SmartyCam config → press **Save**
2. Insert SmartyCam SD card into PC
3. Press **Transmit** — RS3 writes config to SD card
4. Re-insert SD card into SmartyCam
5. On SmartyCam: **MENU → UPDATE → CONFIGURATION**

### How to Load Config via USB-C (GP, GP Pro, Corsa, Dual)
1. Power SmartyCam, connect USB-C to PC
2. RS3 detects camera
3. Edit config → **Save** → **Transmit**
4. On SmartyCam 3 Dual: **MENU → UPDATE → CONFIGURATION** (other models apply automatically)

### RS3 SmartyCam Config Tabs

| Tab | When Required | What to Set |
|-----|---------------|-------------|
| **Overlay** | Always | Position of RPM, speed, temp, G-force displays on video frame |
| **CAN Protocol** | Connected to master only | Select AiM Default or import Advanced protocol to match PDM stream |
| **Parameters** | Standalone only | Start/stop recording conditions (RPM threshold, speed threshold) |
| **ECU Stream** | Standalone with ECU only | Select ECU CAN protocol (GP/Dual/Corsa) — not used when PDM is master |

**For Tiburon build (PDM is master):**
- Set **Overlay** tab → position RPM, speed, water temp, oil P, TPS, G-force overlays
- Set **CAN Protocol** tab → select **AiM Default** (or import Advanced protocol if custom stream)
- **Parameters** and **ECU Stream** tabs: not required — PDM is master, recording is controlled by PDM

### Start/Stop Recording (Connected to Master)
When SmartyCam is set to receive from a master and **Auto Start Rec** is enabled (MENU → SETTINGS → AUTO START REC):
- SmartyCam **starts recording when the master starts recording data**
- SmartyCam **stops recording when master stops**
- No manual button press needed on the camera

This is the recommended mode for the Tiburon. Enable **Auto Start Rec** in SmartyCam's menu.

---

## CAN Bus Behavior and LEDs

### DATA LED (SmartyCam 3 Dual — 3 LEDs on front)

| LED Color | Meaning |
|-----------|---------|
| Solid Green | CAN1 data active |
| Solid Blue | CAN2 data active |
| Solid Cyan | Both CAN1 and CAN2 active |
| Solid Red | Expected CAN data missing (check bus) |
| Blinking Blue | USB connected, no CAN |

For GP/Corsa/GP Pro (1 LED):
| LED Color | Meaning |
|-----------|---------|
| Green solid | CAN ECU traffic detected |
| Green/Blue solid | CAN EXP traffic detected |
| Flashing | External power, battery charging |

> CAN timeout: If no data detected for **5 continuous seconds**, the camera considers the bus inactive.

---

## Power Notes

| Spec | Value |
|------|-------|
| External power range | 9–15V |
| Internal battery | ~20 min runtime (all models) |
| Auto power OFF | 1/5/15/30 min after idle (configurable) — default 5 min |
| Auto power ON | Triggered when external power is applied |

**USB-C connector is NOT a power input** (Dual/GP/GP Pro/Corsa). Power comes from the dedicated Binder/Deutsch power connector only.

---

## RS3 and the SmartyCam — Where to Find Settings

When working in PDM's RS3 config:

| RS3 Tab | SmartyCam Relevance |
|---------|---------------------|
| **SmartyCam Stream** | ← Configure here: enable, CAN bus, channels to send |
| **Channels** | GPS-08 channels appear here automatically when CAN0 is live |
| **CAN Expansions** | **NOT used** — SmartyCam is not a CAN Expansion module |
| **CAN2 Keypad** | Not related to SmartyCam |
| **ECU Stream** | Haltech → PDM (CAN1); not SmartyCam |

> **SmartyCam does not appear in CAN Expansions.** CAN Expansions is for AIM wideband/lambda/channel expansion modules only.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| SmartyCam not powering on | External power not reaching camera | Verify LP3 output is ON (SafeIgnition active). Check 7-pin main power connector wiring |
| No video overlay data | SmartyCam Stream not configured or CAN0 not live | Enable SmartyCam in PDM RS3 → SmartyCam Stream tab; verify CAN0 bus active |
| DATA LED solid red | Expected CAN data missing | CAN0 bus not active; verify PDM transmitting; check bus termination |
| GPS channels not overlaid | GPS-08 not on CAN0 or not detected | Verify GPS-08 powered and on hub; check Channels tab in PDM RS3 for GPS channels |
| SmartyCam not detected in RS3 (PC session) | USB-C not connected or wrong RS3 session | Connect USB-C to SmartyCam (not PDM); RS3 should auto-detect as separate device |
| Config not loading to camera | Loading via SD card: wrong procedure | Follow SD card transmit sequence exactly (save → transmit to SD → move to camera → MENU→UPDATE→CONFIG) |
| Camera not auto-starting recording | AUTO START REC not enabled | MENU → SETTINGS → AUTO START REC → enable |
| Overlay shows zeros on all channels | PDM SmartyCam Stream not transmitting | Retransmit PDM config; verify SmartyCam Stream tab enabled and CAN0 selected |

---

## Technical Specifications — Quick Reference

| Spec | Sport | GP / Corsa |
|------|-------|-----------|
| Video | 1920×1080 @ 30fps | 1920×1080 @ 60fps |
| External power | 9–15V | 9–15V |
| Power connector | 5-pin Binder 712 female (single) | 7-pin Binder (main) + 5-pin Binder "EXP" |
| CAN connector | 5-pin Binder 712 (same as power) | 5-pin Binder "EXP" labeled port |
| Config interface | SD card only | USB-C or SD card |
| Display | 128×128 px | 2.4" 240×320 px |
| Waterproof | IP65 | IP65 |
| Weight | 200g | 280–320g |

---

## Related Files

| File | Contents |
|------|----------|
| `hardware/aim/aim-datahub/aim-datahub.md` | Data Hub pinout and CAN topology — SmartyCam connects via hub |
| `hardware/aim/aim-pdm/pdm-pinout.md` | PDM CAN0 pins (A11/A22/A33) for expansion bus |
| `builds/white-tiburon/guides/pdm-build-guide.md` | Full PDM RS3 config including SmartyCam Stream setup |
| `hardware/aim/aim-gps08/aim-gps08.md` | GPS-08 pinout, CAN behavior, mounting notes |
| `SmartyCam3_114_eng.pdf` | Source AIM document — pinout diagrams (image-only, not text-searchable) |
