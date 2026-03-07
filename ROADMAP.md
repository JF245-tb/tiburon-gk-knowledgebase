# Roadmap

Planned additions to the Tiburon GK Knowledgebase, in rough priority order.

---

## Stage 1 — MVP (Current)

- [x] Factory shop manual content extracted to Markdown (`common/shop-manual/`)
- [x] Electrical troubleshooting manual extracted (`common/electrical-manual/`)
- [x] OpenGK community wiki content (`common/opengk/`)
- [x] Knowledge graph with components, specs, procedures, and edges (`common/tiburon-knowledge-graph.json`)
- [x] Build-specific graph overlay (`builds/{car}/build-knowledge-graph.json`)
- [x] Machine-readable build profile for AI session context (`builds/{car}/build-profile.json`)
- [x] MCP server setup for AI model access (`mcp/`)
- [x] Mermaid component diagrams with clickable nodes (`common/diagrams/`, `builds/{car}/diagrams/`)
- [x] Fastener database schema and template (`fasteners/`)

---

## Stage 2 — Semantic Search

- [ ] `common/vector-store/chunker.py` — parse `.md` files into `chunks.jsonl`
- [ ] Local vector store (ChromaDB + `bge-small-en-v1.5`) — zero cost
- [ ] MCP search tool: `search_kb(query, top_k, filter_engine)` → returns ranked chunks
- [ ] Graph enrichment: chunk → `graph_node_ids` → follow edges for related context

See `common/vector-store/README.md` for schema and implementation options.

---

## Stage 3 — Community Input

Community contributions are tracked through GitHub Issues before being merged into the knowledge graph.

### Trust ladder (bottom to top)

| Level | Meaning |
|-------|---------|
| `community_report` | One person reports it |
| `multiple_reports` | ≥3 independent confirmations |
| `verified_fit` | Installed and working, with evidence |
| `measured` | Dimensional or electrical measurement provided |
| `factory_spec` | Confirmed in factory manual → becomes Tier 1 |

### GitHub Issues labels

| Label | Use |
|-------|-----|
| `community-review` | New forum claim needing vetting |
| `spec-error` | Incorrect spec reported |
| `part-number` | New or corrected part number |
| `procedure-verify` | Procedure step needs confirmation |
| `measurement` | Measurement needed or contributed |
| `forum-ingest` | Request to ingest a forum thread |
| `interchangeable-part` | Cross-vehicle compatibility claim |
| `help-wanted` | Open request for contribution |
| `verified` | Confirmed, ready to merge |

### Priority contributions needed

- Compatible replacement part numbers (CMP sensor, O2 sensors, wheel bearings)
- Race-prep procedure verification (alignment specs, brake bias)
- Forum thread ingestion (NewTiburon.com)
- Hands-on measurements (CMP sensor air gap, stock injector flow rate)

See `Knowledgebase/ARCHITECTURE.md` for full community input design.

---

## Stage 4 — Interchangeable Parts

Cross-vehicle part compatibility tracked as `interchangeable_with` edges in the knowledge graph, with `trust_level` and `source_vehicle` fields.

Example already documented: Toyota 90919-A2005 ignition coil (verified fit on G6BA).

Planned:
- [ ] CMP/CKP sensor cross-references
- [ ] O2 sensor cross-references
- [ ] Wheel bearing cross-references
- [ ] RockAuto and OEM parts site part number ingestion

---

## Stage 5 — Forum Data

- [ ] `forum/scraper.py` — Python scraper for NewTiburon.com (requests + BeautifulSoup4, 3–5s delay)
- [ ] Priority: posts by chase206 and other verified contributors
- [ ] Each post ingested as a chunk with `trust_level: "community_report"` and a GitHub Issue opened for review
- [ ] See `forum/README.md` for methodology and ethics policy
