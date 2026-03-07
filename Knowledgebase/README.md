# 2003 Hyundai Tiburon (GK) Knowledgebase
## 24 Hours of Lemons — Dual V6 (Delta 2.7L) Race Cars

### The Cars

| | Blue Tiburon | White Tiburon |
|---|---|---|
| **Role** | Lower-tech test car | Primary race car (best equipment) |
| **ECU** | Stock Siemens (tuned via GKFlasher) | Haltech Elite 2500 |
| **PDM** | None (stock fuse box) | AIM PDM 32 |
| **Engine** | 2.7L V6 NA ("junkyard engine") | 2.7L V6 (TBD mods) |
| **Build profile** | `builds/blue-tiburon/build-profile.md` | `builds/white-tiburon/build-profile.md` |

---

### Directory Structure

```
Knowledgebase/
├── README.md                    ← This file
├── component-index.json         ← Component → file lookup
├── system-crossref.json         ← System → component → file mapping
├── knowledge-graph.json         ← Node/edge graph: components, signals, protocols
│
├── builds/                      ← Per-car build configs (separable, community-shareable)
│   ├── template/                ← Intake form for new builds
│   │   └── build-template.md
│   ├── white-tiburon/           ← Primary race car
│   │   ├── build-profile.md     ← Equipment list, known issues, maintenance log
│   │   ├── weekend-tasks.md     ← Phased build procedure + test gates
│   │   ├── signal-routing.md    ← End-to-end signal routing (sensor → wire → pin)
│   │   └── oil-analysis/        ← Blackstone oil reports (PDF)
│   └── blue-tiburon/
│       └── build-profile.md
│
├── common/                      ← Shared GK chassis knowledge (not build-specific)
│   ├── chassis/
│   │   └── gk-chassis-specs.md  ← G6BA engine, Aisin trans, dimensions, alignment
│   ├── engine-builds.md         ← Engine build plans (both cars)
│   ├── opengk/                  ← OpenGK community wiki (ECU, sensors, tuning)
│   │   ├── README.md
│   │   ├── sensor-information.md
│   │   ├── gkflasher.md
│   │   ├── ecm-pinouts.md
│   │   ├── ecm-identification.md
│   │   ├── fuel-injectors.md
│   │   ├── map-definitions.md
│   │   ├── can-bus-messages.md
│   │   ├── camshaft-specs.md
│   │   ├── valvetrain.md
│   │   ├── forced-induction-v6.md
│   │   ├── immobiliser.md
│   │   ├── body-control-module.md
│   │   ├── k-line.md
│   │   ├── chassis-identifiers.md
│   │   ├── smartra.md
│   │   ├── smartra-protocol.md
│   │   ├── w-line.md
│   │   └── test-bench-setup.md
│   ├── shop-manual/             ← Factory service manual (procedures, specs, torques)
│   │   ├── engine-mechanical.md
│   │   ├── engine-electrical.md
│   │   ├── fuel-system.md
│   │   ├── transaxle.md
│   │   ├── suspension-system.md
│   │   ├── brake-system.md
│   │   ├── body-electrical.md
│   │   ├── body-control-module.md
│   │   └── ... (14 chapters)
│   └── electrical-manual/       ← Electrical troubleshooting manual
│       ├── connector-configurations.md
│       ├── component-locations.md
│       ├── harness-layouts.md
│       └── schematic-diagrams.md
│
├── hardware/                    ← Aftermarket device documentation
│   ├── aim-pdm/
│   │   ├── pdm-pinout.md
│   │   ├── pdm-configuration-guide.md
│   │   └── race-studio-config-guide.md
│   ├── haltech/
│   │   ├── elite-2500-wiring-diagram--rev-6.md
│   │   ├── main-connector-26-pin-elite2500.md
│   │   ├── main-connector-34-pin-elite2500.md
│   │   └── rem-harness-diagram.md
│   └── sensors/
│       ├── lowdoller-sensors.md       ← Combo pressure/temp sensor specs & calibration
│       ├── cop-ignition.md            ← Toyota 90919-A2005 COP conversion
│       └── oem-cluster-integration.md ← OEM gauge cluster + Haltech/PDM wiring
│
└── fasteners/                   ← Bolt database (built progressively)
    ├── README.md
    ├── bolt-index.json          ← Primary query file
    ├── bin-labels.md            ← Printable bin labels
    ├── _templates/
    │   └── record-template.json
    └── bolts/
        └── {bolt_id}/
            ├── record.json
            └── *.jpg (spec, head, side, location)
```

> **Legacy directories** — `cars/`, `opengk/`, `shop-manual/`, `electrical-manual/`, `aim-pdm/`, `haltech/`, `signal-routing.md` (root) — are preserved in place. New canonical locations are under `builds/`, `common/`, and `hardware/`. Legacy directories can be removed once GitHub migration is confirmed.

---

### How to Use This Knowledgebase

**Quick lookup workflow:**
1. **Check `component-index.json`** — maps every sensor/actuator/connector to relevant files
2. **For a specific build** — start at `builds/{car}/build-profile.md`
3. **For GK chassis/engine info** — check `common/chassis/` and `common/opengk/`
4. **For wiring/connector pinouts** — `common/electrical-manual/` + `hardware/haltech/` + `hardware/aim-pdm/`
5. **For fasteners** — `fasteners/bolt-index.json`
6. **Signal routing end-to-end** — `builds/white-tiburon/signal-routing.md`

---

### Key External Resources

| Resource | URL | Local Copy |
|----------|-----|------------|
| OpenGK Wiki | https://opengk.org/ | `common/opengk/` |
| GKFlasher | https://github.com/Dante383/GKFlasher | `common/opengk/gkflasher.md` |
| NewTiburon Forum | https://www.newtiburon.com/ | `forum/` *(planned scrape — see below)* |
| AIM Sports Webinar | https://www.youtube.com/watch?v=sResCgHlDYI | `hardware/aim-pdm/pdm-configuration-guide.md` |

---

### Shop Manual Code → Chapter Mapping

| Code | Chapter | File |
|------|---------|------|
| BCM | Body Control Module | `common/shop-manual/body-control-module.md` |
| BE | Body Electrical | `common/shop-manual/body-electrical.md` |
| BR | Brake System | `common/shop-manual/brake-system.md` |
| CH | Clutch System | `common/shop-manual/clutch-system.md` |
| DS | Driveshaft And Axle | `common/shop-manual/driveshaft-and-axle.md` |
| EC | Emission Control | `common/shop-manual/emission-control-system.md` |
| EE | Engine Electrical | `common/shop-manual/engine-electrical.md` |
| EM | Engine Mechanical | `common/shop-manual/engine-mechanical.md` |
| FL | Fuel System | `common/shop-manual/fuel-system.md` |
| GI | General Information | `common/shop-manual/general-information.md` |
| HA | HVAC | `common/shop-manual/heating-ventilation-air-conditioning.md` |
| RT | Restraints | `common/shop-manual/restraints.md` |
| SS | Suspension | `common/shop-manual/suspension-system.md` |
| ST | Steering | `common/shop-manual/steering-system.md` |
| TR | Transaxle | `common/shop-manual/transaxle.md` |

---

### Engine Management Quick-Reference (V6 Delta 2.7L)

| Component | Key Files |
|-----------|-----------|
| Cam/crank sensors | `common/shop-manual/emission-control-system.md`, `common/shop-manual/engine-mechanical.md` |
| Knock sensor | `common/shop-manual/body-electrical.md` |
| TPS | `common/shop-manual/emission-control-system.md` |
| Coolant temp | `common/shop-manual/engine-mechanical.md`, `common/shop-manual/body-electrical.md` |
| COP ignition | `hardware/sensors/cop-ignition.md` |
| Fuel pump | `common/shop-manual/body-electrical.md`, `common/shop-manual/fuel-system.md` |
| Lowdoller sensors | `hardware/sensors/lowdoller-sensors.md` |
| Haltech connector pinouts | `hardware/haltech/main-connector-26-pin-elite2500.md`, `hardware/haltech/main-connector-34-pin-elite2500.md` |
| AIM PDM pinout | `hardware/aim-pdm/pdm-pinout.md` |
| ECM (stock) | `common/opengk/ecm-pinouts.md`, `common/opengk/ecm-identification.md` |

---

### Notes

- **V6 Focus:** Both race cars use the 2.7L V6 Delta. I4-specific content exists in factory manual files but is labeled as such.
- **Visual Diagrams:** For visual circuit tracing, reference original PDFs in `LARGEFILE Searchable_Manuals/`. Text extracts capture connector codes and pin labels only.
- **MCP Access:** This knowledgebase is designed to be served via `mcp-server-filesystem` for use with any AI model (Claude, OpenAI-compatible, Gemini, etc.) — see `mcp/README.md` for setup.
