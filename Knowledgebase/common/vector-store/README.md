# Vector Store — Implementation Guide
**Purpose:** Semantic search over the Tiburon knowledgebase. Enables queries like "what's the valve spring free height" or "how do I test the cam sensor" to find the right manual section without keyword matching.

---

## Architecture

```
Manual text (.md files)
        ↓
   [Chunker script]
        ↓
   chunks.jsonl        ← one JSON object per line, each with text + metadata
        ↓
[Embedding model]      ← OpenAI text-embedding-3-small, or local (nomic-embed-text, etc.)
        ↓
   Vector database     ← ChromaDB (local, free), or Pinecone/Weaviate (cloud)
        ↓
[Retrieval]            ← query → top-k chunks → feed to AI with knowledge graph context
```

---

## Chunk Schema

Every chunk stored in the vector DB carries this metadata alongside its embedding:

```json
{
  "chunk_id": "EMA-3-valve-spring",
  "source": "shop-manual",
  "chapter_code": "EMA",
  "chapter_label": "Engine Mechanical System (2.7 V6)",
  "page_ref": "EMA-3",
  "page_ref_end": "EMA-3",
  "section_code": null,
  "section_label": "Specifications Table",
  "section_type": "specification",
  "engine": "V6",
  "chunk_type": "specification",
  "component_tags": ["valve-spring", "valve"],
  "graph_node_ids": ["EMA-3", "sv-valve-spring-free-height", "sv-valve-spring-load", "comp-valve-spring"],
  "standard_values": [
    {"name": "Free height",       "value": "42.5 mm",        "limit": "41.5 mm"},
    {"name": "Load",              "value": "21.9 kg/35 mm",  "limit": "21.9 kg/34 mm"},
    {"name": "Out of squareness", "value": "Max 1.5°",       "limit": "Max 3°"}
  ],
  "cross_refs": ["EMA-72", "EMA-73"],
  "community_verified": false,
  "text": "Valve spring\nFree height  42.5 mm (1.6732 in.)  Limit: 41.5 mm (1.6339 in.)\nLoad  21.9 kg/35 mm (48.4 lb/1.3780 in.)  Limit: 21.9 kg/34 mm\nOut of squareness  Max 1.5°  Limit: Max 3°"
}
```

### Field Definitions

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `chunk_id` | string | ✓ | Stable, unique. Format: `{chapter_code}-{page}-{slug}` |
| `source` | string | ✓ | `shop-manual`, `electrical-manual`, `opengk`, `forum`, `hardware` |
| `chapter_code` | string | ✓ | EMA, EE, FLA, CC, CL, etc. |
| `chapter_label` | string | ✓ | Human-readable chapter name |
| `page_ref` | string | ✓ | First page of chunk (e.g., "EMA-3") |
| `page_ref_end` | string | | Last page if chunk spans pages |
| `section_code` | string | | Hyundai section code if printed (e.g., "EDHA2300") |
| `section_label` | string | ✓ | Section or subsection name |
| `section_type` | string | ✓ | `specification`, `torque`, `procedure`, `troubleshooting`, `diagram`, `general`, `index` |
| `engine` | string | ✓ | `V6`, `I4`, or `both` |
| `chunk_type` | string | ✓ | Same vocabulary as `section_type` |
| `component_tags` | string[] | | Slugified component names present in chunk |
| `graph_node_ids` | string[] | | IDs from `tiburon-knowledge-graph.json` that this chunk feeds |
| `standard_values` | object[] | | Structured extracted values (name, value, limit) |
| `cross_refs` | string[] | | Page references mentioned in this chunk |
| `community_verified` | boolean | | True if content confirmed by forum/community (for OpenGK/forum chunks) |
| `text` | string | ✓ | Raw text to embed |

---

## Chunking Strategy

### Hierarchical Chunking (recommended)

Match the manual's own hierarchy — don't split arbitrarily by token count:

1. **Level 1 (Chapter Index):** One chunk per chapter TOC. Small. Helps routing queries to the right chapter.
2. **Level 2 (Section):** One chunk per named section (e.g., "ENGINE BLOCK — EMA-20"). May span several pages.
3. **Level 3 (Subsection/Topic):** One chunk per subsection code or named topic. This is the primary retrieval unit.
4. **Level 4 (Spec table rows):** Each contiguous group of related specs extracted as a structured chunk with `standard_values` array.

### Special Cases

- **Front-of-chapter spec tables (EMA-2 to EMA-5):** Create one chunk per logical group (general specs, valve specs, piston specs, torques). Each chunk gets a `standard_values` array.
- **DTC tables (FLA-73+):** One chunk per DTC code row or small group. Tag with the DTC code in `component_tags`.
- **Schematic diagrams:** Chunk by circuit/system. Text is wire labels and connector codes — useful for "what connector code is the cam sensor" queries.
- **Forum posts:** One chunk per post. Set `source: "forum"` and `community_verified: false` until reviewed.

### Chunk Size Guidelines

- Aim for 200–600 tokens per chunk
- Never split a spec table row across chunks
- Prefer keeping a procedure's steps together (split at sub-procedures, not mid-step)
- Index chunks can be < 100 tokens — that's fine

---

## Implementation Options

### Option A: Local (Zero Cost)

```bash
pip install chromadb sentence-transformers
```

Use `nomic-ai/nomic-embed-text-v1` or `BAAI/bge-small-en-v1.5` for embedding (both free, run locally).

```python
import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./vector-store/chroma")
collection = client.get_or_create_collection("tiburon-kb")

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

# Load chunks
import json
chunks = [json.loads(line) for line in open("chunks.jsonl")]

collection.add(
    ids=[c["chunk_id"] for c in chunks],
    embeddings=model.encode([c["text"] for c in chunks]).tolist(),
    documents=[c["text"] for c in chunks],
    metadatas=[{k: v for k, v in c.items() if k != "text" and not isinstance(v, (list, dict))} for c in chunks]
)
```

### Option B: OpenAI Embeddings

```python
from openai import OpenAI
client = OpenAI()  # uses OPENAI_API_KEY env var

def embed(text):
    return client.embeddings.create(input=text, model="text-embedding-3-small").data[0].embedding
```

Cost: ~$0.02 per 1M tokens. The full knowledgebase is probably under 500k tokens — under $0.01 total.

### Option C: MCP Integration

Once the vector store is built, expose it as an MCP tool alongside `mcp-server-filesystem`:

```json
{
  "mcpServers": {
    "tiburon-kb": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "./Knowledgebase"]
    },
    "tiburon-search": {
      "command": "python",
      "args": ["./vector-store/mcp-server.py"]
    }
  }
}
```

The search MCP tool would expose: `search_kb(query, top_k=5, filter_engine="V6")` → returns ranked chunks + metadata.

---

## Query → Graph Enrichment

When a chunk is retrieved, enrich the context with the knowledge graph:

1. Get `graph_node_ids` from the chunk metadata
2. Look up those nodes in `tiburon-knowledge-graph.json`
3. Follow edges to find related nodes (e.g., standard_value → applies_to → component → procedure_for → sections)
4. Include the enriched context in the prompt

Example: Query "valve spring" → retrieves EMA-3 spec chunk → graph lookup → finds `comp-valve-spring` → edges point to `EMA-72` (diagram) and `EMA-73` (installation) → AI gets all three in context.

---

## Files in This Directory

| File | Contents |
|------|----------|
| `README.md` | This file — schema and implementation guide |
| `chunks.jsonl` | *(generated)* One chunk per line, structured per schema above |
| `chroma/` | *(generated)* ChromaDB persistent storage |
| `chunker.py` | *(planned)* Script to parse `.md` files and produce `chunks.jsonl` |
| `mcp-server.py` | *(planned)* MCP server exposing `search_kb` tool |

---

## Roadmap

1. **Now:** Use `mcp-server-filesystem` for file-level access (already set up in `mcp/`)
2. **Next:** Write `chunker.py` to parse the shop manual and electrical manual `.md` files into `chunks.jsonl`
3. **Then:** Embed chunks locally with ChromaDB + `bge-small-en-v1.5`
4. **Later:** Add OpenGK content (part numbers, sensor specs) as additional chunks with `source: "opengk"`
5. **Community:** Add forum scrapes as chunks with `community_verified: false`, create GitHub Issues review workflow
