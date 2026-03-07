# Tiburon GK Knowledgebase

Structured technical reference for the GK-chassis Hyundai Tiburon (2003). Factory manual content is extracted into searchable Markdown and linked via a knowledge graph. Designed for use with AI models via MCP, or browsed directly on GitHub.

---

## Directory Structure

```
Knowledgebase/
├── ARCHITECTURE.md              ← System design, authority tiers, trust ladder
│
├── common/                      ← GK chassis knowledge (shared across all builds)
│   ├── shop-manual/             ← Factory procedures, specs, torques
│   │   ├── engine-mechanical.md    (EMA / EM)
│   │   ├── engine-electrical.md    (EE)
│   │   ├── fuel-system.md          (FLA / FL)
│   │   ├── emission-control-system.md (EC)
│   │   ├── transaxle.md            (TR)
│   │   ├── suspension-system.md    (SS)
│   │   ├── brake-system.md         (BR)
│   │   └── ... (14 chapters total)
│   ├── electrical-manual/       ← ETM connectors, locations, schematics
│   │   ├── connector-configurations.md
│   │   ├── component-locations.md
│   │   ├── harness-layouts.md
│   │   └── schematic-diagrams.md
│   ├── opengk/                  ← OpenGK community wiki (ECU, sensors, tuning)
│   ├── chassis/
│   │   └── gk-chassis-specs.md  ← G6BA engine specs, Aisin ratios, dimensions
│   ├── diagrams/                ← Mermaid component diagrams
│   │   └── cam-sensor.md        ← CMP sensor signal path + connector + DTCs
│   ├── tiburon-knowledge-graph.json ← Component/spec/procedure graph
│   ├── knowledge-graph-schema.md    ← Schema reference
│   └── vector-store/            ← Semantic search (planned — see ROADMAP.md)
│
├── builds/                      ← Per-car configuration
│   ├── template/
│   │   ├── build-template.md           ← Human intake form
│   │   └── build-profile-template.json ← Machine-readable template
│   ├── white-tiburon/
│   │   ├── build-profile.md            ← Equipment, wiring, status
│   │   ├── build-profile.json          ← Machine-readable (load at AI session start)
│   │   ├── build-knowledge-graph.json  ← Build-specific graph overlay
│   │   ├── weekend-tasks.md            ← Phased build procedure + test gates
│   │   ├── signal-routing.md           ← End-to-end signal routing
│   │   ├── oil-analysis/               ← Blackstone oil reports (PDF)
│   │   └── diagrams/
│   │       └── fuel-pump.md            ← Fuel pump power + sensor path diagram
│   └── blue-tiburon/
│       └── build-profile.md
│
├── hardware/                    ← Aftermarket device documentation
│   ├── aim-pdm/
│   │   ├── pdm-pinout.md
│   │   ├── pdm-configuration-guide.md
│   │   └── race-studio-config-guide.md
│   ├── haltech/
│   │   ├── main-connector-26-pin-elite2500.md
│   │   ├── main-connector-34-pin-elite2500.md
│   │   └── elite-2500-wiring-diagram--rev-6.md
│   └── sensors/
│       ├── lowdoller-sensors.md        ← Combo pressure/temp specs + calibration
│       ├── cop-ignition.md             ← Toyota 90919-A2005 COP wiring
│       └── oem-cluster-integration.md  ← OEM gauge cluster wiring
│
├── fasteners/                   ← Bolt database with photos and measurements
│   ├── README.md
│   ├── bolt-index.json
│   ├── bin-labels.md
│   └── bolts/{bolt_id}/         ← Per-bolt: record.json + 4 photos
│
└── forum/                       ← Community knowledge (planned — see ROADMAP.md)
    └── demo.md                  ← Example: AI + grounded knowledgebase
```

---

## How to Use

### Find a spec or procedure

Search the repo (GitHub search or `grep`) for the value or component name. Results link to the source file and page reference (e.g., `EMA-3`, `FLA-73`).

```
"valve spring free height"  →  common/shop-manual/engine-mechanical.md (EMA-3)
"P0340"                     →  common/shop-manual/fuel-system.md (FLA-73)
"cam sensor connector"      →  common/diagrams/cam-sensor.md
```

### With an AI model (MCP)

Load `builds/{car}/build-profile.json` at session start — the AI will know your AVI assignments, PDM outputs, and wiring without being re-told each session. See `mcp/SETUP-GUIDE.md`.

### Add your own build

Copy `builds/template/build-profile-template.json` → `builds/{your-car}/build-profile.json` and fill in your equipment. The structure works for any GK-chassis Tiburon configuration, stock or modified.

---

## Shop Manual Chapter Codes

| Code | Chapter | File |
|------|---------|------|
| EMA | Engine Mechanical (V6) | `common/shop-manual/engine-mechanical.md` |
| EM | Engine Mechanical (I4) | same file, I4 sections |
| EE | Engine Electrical | `common/shop-manual/engine-electrical.md` |
| FLA | Fuel System (V6) | `common/shop-manual/fuel-system.md` |
| FL | Fuel System (I4) | same file |
| EC | Emission Control | `common/shop-manual/emission-control-system.md` |
| TR | Transaxle | `common/shop-manual/transaxle.md` |
| BR | Brake System | `common/shop-manual/brake-system.md` |
| SS | Suspension | `common/shop-manual/suspension-system.md` |
| ST | Steering | `common/shop-manual/steering-system.md` |
| EE | Engine Electrical | `common/shop-manual/engine-electrical.md` |
| BE | Body Electrical | `common/shop-manual/body-electrical.md` |
| GI | General Information | `common/shop-manual/general-information.md` |
| CC | Connector Configurations | `common/electrical-manual/connector-configurations.md` |
| CL | Component Locations | `common/electrical-manual/component-locations.md` |

---

## Engine Management Quick-Reference (G6BA 2.7L V6)

| Component | Key Files |
|-----------|-----------|
| Cam / crank sensors | `common/shop-manual/fuel-system.md` (FLA-2, FLA-73), `common/diagrams/cam-sensor.md` |
| TPS | `common/shop-manual/fuel-system.md` (FLA-3) |
| Coolant temp sensor | `common/shop-manual/engine-mechanical.md` |
| Knock sensors | `common/shop-manual/engine-electrical.md` |
| COP ignition | `hardware/sensors/cop-ignition.md` |
| Fuel pump circuit | `builds/white-tiburon/diagrams/fuel-pump.md` |
| Lowdoller sensors | `hardware/sensors/lowdoller-sensors.md` |
| Haltech 26-pin pinout | `hardware/haltech/main-connector-26-pin-elite2500.md` |
| Haltech 34-pin pinout | `hardware/haltech/main-connector-34-pin-elite2500.md` |
| AIM PDM 32 pinout | `hardware/aim-pdm/pdm-pinout.md` |
| ECM (stock Siemens) | `common/opengk/ecm-pinouts.md` |
