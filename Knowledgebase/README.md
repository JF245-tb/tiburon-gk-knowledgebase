# Tiburon GK Knowledgebase

Structured technical reference for the GK-chassis Hyundai Tiburon (2003). Factory manual content is extracted into searchable Markdown and linked via a knowledge graph. Designed for use with AI models via MCP, or browsed directly on GitHub.

---

## Directory Structure

```
Knowledgebase/
├── LLM-GUIDE.md                 ← AI navigation guide — read this first for session start rituals
├── ARCHITECTURE.md              ← System design, authority tiers, trust ladder
│
├── common/                      ← GK chassis knowledge (shared across all builds)
│   ├── shop-manual/             ← Factory procedures, specs, torques — 18 chapters, each split
│   │   ├── engine-mechanical/      (EMA)
│   │   ├── engine-mechanical-i4/   (EM)
│   │   ├── fuel-system/            (FLA / FL)
│   │   ├── engine-electrical/      (EE)
│   │   ├── transaxle/              (TR)
│   │   ├── brake-system/           (BR)
│   │   ├── ... (18 chapter directories total, each with `_index.md`)
│   │   └── _archive/               ← Old monolithic OCR files (superseded)
│   ├── electrical-manual/       ← ETM connectors, locations, schematics
│   │   ├── index.md                     ← Chapter overview, wire colors, connector notation
│   │   ├── cc-connector-configurations.md ← Full CC extraction
│   │   ├── hl-harness-layouts.md          ← Full HL extraction
│   │   ├── component-locations.md         ← CL section (partial)
│   │   ├── connector-master-reference.md  ← Connector code ↔ CC/CL/HL/SD/FLA/graph node
│   │   └── schematics/                    ← 47 circuit files + `_index.md`
│   ├── opengk/                  ← OpenGK community wiki (ECU, sensors, tuning)
│   ├── chassis/
│   │   └── gk-chassis-specs.md  ← G6BA engine specs, Aisin ratios, dimensions
│   ├── diagrams/                ← Mermaid component diagrams
│   │   └── cam-sensor.md        ← CMP sensor signal path + connector + DTCs
│   ├── parts-catalog/           ← OEM parts catalog extraction (engine/chassis/electrical)
│   ├── tiburon-knowledge-graph.json ← Component/spec/procedure graph
│   ├── knowledge-graph-schema.md    ← Schema reference
│   └── vector-store/            ← Semantic search (planned — see ROADMAP.md)
│
├── builds/                      ← Per-car configuration
│   ├── template/
│   │   ├── build-template.md           ← Human intake form
│   │   └── build-profile-template.json ← Machine-readable template
│   ├── white-tiburon/
│   │   ├── README.md                   ← Session start for white-car work
│   │   ├── build-profile.md            ← Equipment, wiring, status
│   │   ├── build-profile.json          ← Machine-readable (load at AI session start)
│   │   ├── build-knowledge-graph.json  ← Build-specific graph overlay
│   │   ├── weekend-tasks.md            ← Phased build procedure + test gates
│   │   ├── signal-routing.md           ← End-to-end signal routing
│   │   ├── cluster-integration.md      ← OEM gauge cluster wiring
│   │   ├── guides/                     ← PDM/Race Studio build guides
│   │   ├── oil-analysis/               ← Blackstone oil reports (PDF)
│   │   └── diagrams/
│   │       └── fuel-pump.md            ← Fuel pump power + sensor path diagram
│   └── blue-tiburon/
│       ├── README.md                   ← Session start for blue-car work
│       └── build-profile.md
│
├── hardware/                    ← Aftermarket device documentation
│   ├── hardware-graph.json      ← Device capability graph (reusable across builds)
│   ├── aim/
│   │   ├── aim-pdm/             ← PDM 32 pinout + Race Studio config guide
│   │   ├── aim-datahub/         ← CAN Data Hub (2-way & 4-way)
│   │   ├── aim-gps08/           ← GPS-08 / GPS09c CAN GPS module
│   │   ├── aim-podium/          ← Podium Micro
│   │   ├── aim-smartycam/       ← SmartyCam 3 series
│   │   └── aim-can-keypad/      ← CAN keypad
│   ├── haltech/
│   │   ├── main-connector-26-pin-elite2500.md
│   │   ├── main-connector-34-pin-elite2500.md
│   │   ├── elite-2500-wiring-diagram--rev-6.md
│   │   └── rem-harness-diagram.md
│   └── sensors/
│       ├── lowdoller-sensors.md        ← Combo pressure/temp specs + calibration
│       └── cop-ignition.md             ← Toyota 90919-A2005 COP wiring
│
├── fasteners/                   ← Bolt database with photos and measurements
│   ├── README.md
│   ├── bolt-index.json
│   ├── bin-labels.md
│   └── _templates/record-template.json
│
├── forum/                       ← Community knowledge — thread index + scraped posts
│   ├── README.md
│   ├── thread-index.json
│   └── threads/{id}/            ← metadata.json + posts.json per thread
│
├── credibility/                 ← Source credibility scoring system
├── validation/                  ← KB coverage testing against forum questions
├── extraction/                  ← Extraction SOPs — start here for content ingestion
└── mcp/                         ← MCP server setup for AI model access
```

---

## How to Use

### Find a spec or procedure

Search the repo (GitHub search or `grep`) for the value or component name. Results link to the source file and page reference (e.g., `EMA-3`, `FLA-73`).

```
"valve spring free height"  →  common/shop-manual/engine-mechanical/specifications.md (EMA-3)
"P0340"                     →  common/shop-manual/fuel-system/dtc-troubleshooting.md (FLA-73)
"cam sensor connector"      →  common/diagrams/cam-sensor.md
```

### With an AI model (MCP)

Load `builds/{car}/build-profile.json` at session start — the AI will know your AVI assignments, PDM outputs, and wiring without being re-told each session. See `mcp/SETUP-GUIDE.md`.

### Add your own build

Copy `builds/template/build-profile-template.json` → `builds/{your-car}/build-profile.json` and fill in your equipment. The structure works for any GK-chassis Tiburon configuration, stock or modified.

---

## Shop Manual Chapter Codes

Each chapter below is a directory with a `_index.md` section map plus a `specifications.md` and topic files. See `LLM-GUIDE.md` for the full chapter list (18 total).

| Code | Chapter | Directory |
|------|---------|-----------|
| EMA | Engine Mechanical (V6) | `common/shop-manual/engine-mechanical/` |
| EM | Engine Mechanical (I4) | `common/shop-manual/engine-mechanical-i4/` |
| EE | Engine Electrical | `common/shop-manual/engine-electrical/` |
| FLA | Fuel System (V6) | `common/shop-manual/fuel-system/` |
| EC | Emission Control | `common/shop-manual/emission-control-system/` |
| TR | Transaxle | `common/shop-manual/transaxle/` |
| BR | Brake System | `common/shop-manual/brake-system/` |
| SS | Suspension | `common/shop-manual/suspension-system/` |
| ST | Steering | `common/shop-manual/steering-system/` |
| BE | Body Electrical | `common/shop-manual/body-electrical/` |
| GI | General Information | `common/shop-manual/general-information/` |
| CC | Connector Configurations | `common/electrical-manual/cc-connector-configurations.md` |
| CL | Component Locations | `common/electrical-manual/component-locations.md` |

---

## Engine Management Quick-Reference (G6BA 2.7L V6)

| Component | Key Files |
|-----------|-----------|
| Cam / crank sensors | `common/shop-manual/fuel-system/` (FLA-2, FLA-73), `common/diagrams/cam-sensor.md` |
| TPS | `common/shop-manual/fuel-system/` (FLA-3) |
| Coolant temp sensor | `common/shop-manual/engine-mechanical/` |
| Knock sensors | `common/shop-manual/engine-electrical/` |
| COP ignition | `hardware/sensors/cop-ignition.md` |
| Fuel pump circuit | `builds/white-tiburon/diagrams/fuel-pump.md` |
| Lowdoller sensors | `hardware/sensors/lowdoller-sensors.md` |
| Haltech 26-pin pinout | `hardware/haltech/main-connector-26-pin-elite2500.md` |
| Haltech 34-pin pinout | `hardware/haltech/main-connector-34-pin-elite2500.md` |
| AIM PDM 32 pinout | `hardware/aim/aim-pdm/pdm-pinout.md` |
| ECM (stock Siemens) | `common/opengk/ecm-pinouts.md` |
