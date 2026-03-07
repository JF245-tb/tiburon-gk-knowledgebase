# Tiburon GK Knowledgebase
**2003 Hyundai Tiburon GK — 24 Hours of Lemons Race Car Build**

A community knowledgebase for the GK-chassis Hyundai Tiburon, maintained by racers for racers. Combines factory service manual content, aftermarket device documentation, community forum knowledge, and AI-queryable structured data.

---

## What's In Here

| Directory | Contents |
|-----------|----------|
| `Knowledgebase/` | Core KB: Markdown docs, knowledge graphs, bolt database, diagrams |
| `Tiburon-Shop-Manual/` | Original factory shop manual PDFs (chapter PDFs, 1–20MB each) |
| `Electrical Troubleshooting Manual/` | Original ETM PDFs (schematic diagrams, component locations) |
| `Electrical Excerpts/` | Specific hand-picked ETM pages for quick reference |
| `AIM PDM/` | AIM PDM 32 original documentation |
| `Haltech/` | Haltech Elite 2500 documentation |
| `mcp/` | MCP server setup for AI model integration |

> **Note:** `LARGEFILE Searchable_Manuals/` (OCR'd PDFs, 1.4GB) is excluded from this repo. Its text content is already extracted into `Knowledgebase/common/shop-manual/` and `Knowledgebase/common/electrical-manual/`.

---

## Quick Start

### For Builders (Human)

1. Browse `Knowledgebase/builds/{car}/build-profile.md` for a specific car setup
2. Browse `Knowledgebase/common/shop-manual/` for factory procedures and specs
3. Use the Mermaid diagrams in `Knowledgebase/common/diagrams/` and `Knowledgebase/builds/{car}/diagrams/` for visual wiring traces
4. Search GitHub for specific values (e.g., "valve spring free height" → finds EMA-3 in engine-mechanical.md)

### For AI Models

See `mcp/README.md` for MCP filesystem server setup — works with Claude, OpenAI-compatible models, and any MCP client. No cloud hosting, no API keys, zero ongoing cost.

```bash
npm install -g @modelcontextprotocol/server-filesystem
npx @modelcontextprotocol/server-filesystem ./Knowledgebase
```

### For Community Contributors

- **Add a forum thread** → `Knowledgebase/forum/thread-index.json` + create `forum/threads/{id}/` folder
- **Add a bolt** → `Knowledgebase/fasteners/bolt-index.json` + create `fasteners/bolts/{bolt_id}/` folder with 4 photos
- **Add a build** → Copy `Knowledgebase/builds/template/build-template.md` → `builds/{your-car}/build-profile.md`
- **Verify forum content** → Open a GitHub Issue with label `community-review` to vet technical claims
- **Report incorrect spec** → Open a GitHub Issue with label `spec-error`

---

## Structure

```
Knowledgebase/
├── common/          ← Shared GK chassis knowledge
│   ├── shop-manual/ ← Factory procedures, specs, torques (V6 + I4)
│   ├── electrical-manual/ ← ETM connectors, locations, schematics
│   ├── opengk/      ← Community wiki (ECU tuning, sensors, immo)
│   ├── chassis/     ← G6BA engine specs, Aisin trans ratios
│   ├── diagrams/    ← Mermaid component diagrams (clickable)
│   ├── tiburon-knowledge-graph.json ← Structured component graph
│   ├── knowledge-graph-schema.md    ← Schema documentation
│   └── vector-store/ ← Semantic search implementation (local, free)
├── builds/
│   ├── template/    ← Intake form for new builds
│   ├── white-tiburon/ ← Haltech Elite 2500 + AIM PDM 32 build
│   │   ├── build-profile.md
│   │   ├── weekend-tasks.md (phased build procedure)
│   │   ├── signal-routing.md
│   │   ├── build-knowledge-graph.json
│   │   └── diagrams/  ← Build-specific wiring diagrams
│   └── blue-tiburon/
├── hardware/
│   ├── aim-pdm/     ← PDM 32 pinout + Race Studio config guide
│   ├── haltech/     ← Elite 2500 wiring diagrams + connector pinouts
│   └── sensors/     ← COP coil wiring, Lowdoller sensor specs
├── fasteners/       ← Bolt database (built progressively)
└── forum/           ← NewTiburon.com community knowledge
```

---

## Cars

| Car | ECU | PDM | Build file |
|-----|-----|-----|------------|
| White Tiburon (primary race car) | Haltech Elite 2500 | AIM PDM 32 | `Knowledgebase/builds/white-tiburon/build-profile.md` |
| Blue Tiburon (test car) | Stock Siemens SIMK43 (GKFlasher) | None | `Knowledgebase/builds/blue-tiburon/build-profile.md` |

---

## Community Review

Forum-derived content starts with `"community_verified": false` in the knowledge graph. To verify:
1. Open a GitHub Issue with label `community-review`
2. Tag the specific claim (quote the `chunk_id` from `forum/thread-index.json` or node id from the graph)
3. Provide a source (another thread, personal experience, manual reference)
4. A maintainer sets `"community_verified": true` once confirmed

---

## Acknowledgments

- **OpenGK community** — sensor specs, ECU knowledge, tuning maps
- **NewTiburon.com** — forum community knowledge (especially chase206 for fabrication and race prep)
- **Hyundai Motor Company** — factory service manual and electrical troubleshooting manual
- **AIM Sports** — PDM 32 documentation and webinar content
- **Haltech** — Elite 2500 wiring documentation
