# Tiburon GK Knowledgebase
**2003 Hyundai Tiburon (GK chassis) — Factory Manual + Knowledge Graph + MCP**

Structured technical reference for the GK-chassis Hyundai Tiburon. Combines factory service manual content, aftermarket device documentation, and a queryable knowledge graph. Designed to be served to any AI model via MCP for accurate, cited answers during build and diagnostic sessions.

---

## What's In Here

| Directory | Contents |
|-----------|----------|
| `Knowledgebase/` | Core KB: Markdown docs, knowledge graphs, diagrams, fastener database, hardware docs |
| `mcp/` | MCP server setup for AI model integration |
| `scripts/` | Extraction and scraping tools (PDF, forum, parts catalog) |

> **Note:** Source PDFs (factory shop manual, ETM, AIM/Haltech datasheets — 1.4GB+) are excluded from this repo (see `.gitignore`). Their content is extracted into `Knowledgebase/common/shop-manual/`, `Knowledgebase/common/electrical-manual/`, and `Knowledgebase/hardware/`.

---

## Quick Start

### For Builders

1. Browse `Knowledgebase/common/shop-manual/` for factory procedures and specs
2. Browse `Knowledgebase/builds/{car}/build-profile.md` for a specific car's equipment and wiring
3. Use the Mermaid diagrams in `Knowledgebase/common/diagrams/` for visual component traces
4. Search for specific values (e.g., "valve spring free height" → finds EMA-3 in `Knowledgebase/common/shop-manual/engine-mechanical/specifications.md`)

### For AI Models

See `mcp/SETUP-GUIDE.md` for a step-by-step walkthrough. The short version:

```bash
npm install -g @modelcontextprotocol/server-filesystem
npx @modelcontextprotocol/server-filesystem ./Knowledgebase
```

Add to your Claude Desktop config and the AI can read any file in the knowledgebase. See `mcp/README.md` for other client configs.

---

## Structure

```
Knowledgebase/
├── ARCHITECTURE.md      ← System design: authority tiers, trust ladder, build profiles
├── common/              ← GK chassis knowledge (shared across builds)
│   ├── shop-manual/     ← Factory procedures, specs, torques (V6 + I4)
│   ├── electrical-manual/ ← ETM connectors, locations, schematics
│   ├── opengk/          ← OpenGK community wiki (ECU tuning, sensors, immobilizer)
│   ├── chassis/         ← G6BA engine specs, Aisin trans ratios
│   ├── diagrams/        ← Mermaid component diagrams (clickable nodes)
│   ├── tiburon-knowledge-graph.json ← Structured component/spec graph
│   ├── knowledge-graph-schema.md    ← Schema documentation
│   └── vector-store/    ← Semantic search (planned)
├── builds/
│   ├── template/        ← Build profile template for new cars
│   ├── white-tiburon/   ← Haltech Elite 2500 + AIM PDM 32 build
│   └── blue-tiburon/    ← Stock Siemens SIMK43 build
├── hardware/
│   ├── aim/             ← AIM devices: PDM 32, Data Hub, GPS-08, SmartyCam, Podium, CAN keypad
│   ├── haltech/         ← Elite 2500 wiring diagrams + connector pinouts
│   └── sensors/         ← Aftermarket sensor specs and wiring
├── fasteners/           ← Bolt database with photos and measurements
└── forum/               ← Community knowledge — thread index + scraped posts
```

---

## Example Builds

| Car | ECU | Notes | Build file |
|-----|-----|-------|------------|
| White Tiburon | Haltech Elite 2500 + AIM PDM 32 | Full aftermarket engine management | `builds/white-tiburon/build-profile.md` |
| Blue Tiburon | Stock Siemens SIMK43 (GKFlasher) | OEM ECU with custom tune | `builds/blue-tiburon/build-profile.md` |

---

## Acknowledgments

- **Hyundai Motor Company** — factory service manual and electrical troubleshooting manual
- **OpenGK community** — ECU knowledge, sensor specs, tuning maps
- **AIM Sports** — PDM 32 documentation
- **Haltech** — Elite 2500 wiring documentation

---

See `ROADMAP.md` for planned additions including semantic search, forum data, and interchangeable parts.
