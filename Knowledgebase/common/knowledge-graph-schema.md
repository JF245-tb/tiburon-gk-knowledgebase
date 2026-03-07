# Tiburon GK Knowledge Graph — Schema Reference
**File:** `common/tiburon-knowledge-graph.json`
**Build graph:** `builds/{car}/build-knowledge-graph.json`

---

## Overview

Two complementary graphs:

| Graph | File | Scope |
|-------|------|-------|
| **Common** | `common/tiburon-knowledge-graph.json` | GK chassis, manuals, OEM components, part numbers, forum posts — shared across all builds |
| **Build** | `builds/{car}/build-knowledge-graph.json` | Car-specific wiring, ECU/PDM config, sensor assignments — swap out per build |

Each graph is a `{ nodes: [...], edges: [...] }` JSON object. Nodes and edges are addressable by `id`.

---

## Node Types

### `manual`
Source document (PDF chapter).

| Field | Type | Example |
|-------|------|---------|
| `id` | string | `"manual-ema"` |
| `type` | `"manual"` | |
| `label` | string | `"Engine Mechanical System (2.7 V6)"` |
| `chapter_code` | string | `"EMA"` |
| `engine` | `"V6"` \| `"I4"` \| `"both"` | `"V6"` |
| `source_pdf` | string | path to PDF |
| `md_file` | string | path to extracted `.md` |
| `pages` | number | `80` |

### `section`
A named section or subsection within a manual chapter. Directly maps to a page reference.

| Field | Type | Example |
|-------|------|---------|
| `id` | string | `"EMA-2"` |
| `type` | `"section"` | |
| `label` | string | `"Specifications"` |
| `page_ref` | string | `"EMA-2"` — the chapter+page label printed in the manual |
| `section_code` | string | `"EMCO100"` — Hyundai section identifier (if present) |
| `section_type` | `"index"` \| `"spec"` \| `"torque"` \| `"procedure"` \| `"troubleshooting"` \| `"diagram"` | |

### `subsection`
A named procedure or topic within a section.

| Field | Type | Example |
|-------|------|---------|
| `id` | string | `"EMA-EDHA2300"` |
| `type` | `"subsection"` | |
| `label` | string | `"Inspection"` |
| `page_ref` | string | `"EMA-20"` |
| `section_code` | string | `"EDHA2300"` |
| `parent_id` | string | id of parent section |

### `topic`
A specific subject within a section or subsection.

| Field | Type | Example |
|-------|------|---------|
| `id` | string | `"EMA-cylinder-block"` |
| `type` | `"topic"` | |
| `label` | string | `"Cylinder Block"` |
| `page_ref` | string | `"EMA-20"` |
| `parent_id` | string | id of parent subsection |

### `standard_value`
A measured specification, tolerance, or service limit. May appear in a front-of-chapter table (like EMA-3) and also within a specific procedure section.

| Field | Type | Example |
|-------|------|---------|
| `id` | string | `"sv-cylinder-bore"` |
| `type` | `"standard_value"` | |
| `label` | string | `"Cylinder Bore"` |
| `value` | string | `"86.7 mm (3.4134 in.)"` |
| `limit` | string \| null | `"0.05 mm (0.002 in.)"` — service limit beyond which replacement required |
| `unit` | string | `"mm"` |
| `engine` | `"V6"` \| `"I4"` \| `"both"` | |
| `table_page_ref` | string | `"EMA-3"` — where in the front-matter spec table this value appears |

### `torque_spec`
A tightening torque value for a specific fastener or component.

| Field | Type | Example |
|-------|------|---------|
| `id` | string | `"ts-cam-sprocket"` |
| `type` | `"torque_spec"` | |
| `label` | string | `"Camshaft Sprocket Bolt"` |
| `nm` | number | `100` |
| `nm_range` | string | `"90-110"` |
| `kgcm` | string | `"900-1100"` |
| `lbft` | string | `"65-80"` |
| `method` | string | `"standard"` \| `"torque-angle"` — for angle-spec bolts (e.g., main bearing +90°) |
| `angle_deg` | number \| null | `90` |
| `table_page_ref` | string | `"EMA-5"` |

### `component`
A vehicle component or sensor. The central linking node.

| Field | Type | Example |
|-------|------|---------|
| `id` | string | `"comp-cmp-sensor"` |
| `type` | `"component"` | |
| `label` | string | `"Camshaft Position Sensor"` |
| `aliases` | string[] | `["CMP sensor", "CMP", "cam position sensor"]` |
| `system` | string | `"engine"` |
| `subsystem` | string | `"engine-management"` |
| `engine` | `"V6"` \| `"I4"` \| `"both"` | |
| `oem_location` | string | physical description |

### `part_number`
An OEM or aftermarket part number.

| Field | Type | Example |
|-------|------|---------|
| `id` | string | `"pn-NGK-BKR5ES11"` |
| `type` | `"part_number"` | |
| `label` | string | `"NGK BKR5ES-11"` |
| `number` | string | `"BKR5ES-11"` |
| `source` | `"OEM"` \| `"NGK"` \| `"Champion"` \| `"OpenGK"` \| `"RockAuto"` | |
| `notes` | string | `"Unleaded, 2.7 V6"` |
| `url` | string \| null | link to product page |

### `connector`
An electrical connector identified by harness code.

| Field | Type | Example |
|-------|------|---------|
| `id` | string | `"conn-C133-1"` |
| `type` | `"connector"` | |
| `label` | string | `"ECM Main Connector C133-1"` |
| `connector_code` | string | `"C133-1"` |
| `harness` | string | `"engine"` \| `"main"` \| `"control"` \| `"door"` |
| `pin_count` | number | |
| `etm_page_ref` | string | page in electrical manual where pinout appears |
| `etm_section` | string | harness section code |

### `diagram`
A figure, diagram, or illustration referenced in the manuals.

| Field | Type | Example |
|-------|------|---------|
| `id` | string | `"diag-EMA-72"` |
| `type` | `"diagram"` | |
| `label` | string | `"Valve Spring Installation"` |
| `page_ref` | string | `"EMA-72"` |
| `figure_code` | string | `"EAHA010A"` — Hyundai figure code if present |

### `forum_post`
A community forum post from a verified contributor.

| Field | Type | Example |
|-------|------|---------|
| `id` | string | `"ntcom-484870-p3"` |
| `type` | `"forum_post"` | |
| `thread_id` | string | `"484870"` |
| `post_number` | number | `3` |
| `author` | string | `"chase206"` |
| `url` | string | |
| `summary` | string | brief description of technical content |

---

## Edge Types

| Relationship | Source → Target | Meaning |
|-------------|-----------------|---------|
| `chapter_of` | section → manual | Section belongs to this manual chapter |
| `subsection_of` | subsection → section | Subsection belongs to this section |
| `topic_of` | topic → subsection | Topic within this subsection |
| `table_specifies` | section → standard_value | Front-of-chapter spec table defines this value |
| `procedure_contains` | section/subsection → standard_value | This spec appears in the procedure |
| `diagram_illustrates` | diagram → topic/subsection | Diagram shows this |
| `applies_to` | standard_value → component | This spec applies to this component |
| `torque_for` | torque_spec → component | This torque spec applies to this fastener/component |
| `procedure_for` | section/subsection → component | This section describes install/remove/inspect for component |
| `pinout_in` | connector → section | Connector pinout appears in this ETM section |
| `wired_to` | component → connector | Component connects via this connector |
| `has_part` | component → part_number | OEM or compatible part number |
| `replaces` | part_number → part_number | This part replaces another |
| `mentioned_in` | component → forum_post | Forum post discusses this component |
| `cross_ref` | section → section | Manual cross-reference (e.g., "see also EE-14") |

---

## Vector Store Chunk Schema

Each text chunk stored for embedding carries this metadata:

```json
{
  "chunk_id": "EMA-3-valve-spring",
  "source": "shop-manual",
  "chapter_code": "EMA",
  "chapter_label": "Engine Mechanical System (2.7 V6)",
  "page_ref": "EMA-3",
  "section_code": null,
  "section_label": "Specifications Table",
  "engine": "V6",
  "chunk_type": "specification",
  "component_tags": ["valve-spring", "valve"],
  "standard_values": [
    {"name": "Free height", "value": "42.5 mm", "limit": "41.5 mm"},
    {"name": "Load", "value": "21.9 kg/35 mm", "limit": "21.9 kg/34 mm"},
    {"name": "Out of squareness", "value": "Max 1.5°", "limit": "Max 3°"}
  ],
  "cross_refs": ["EMA-72", "EMA-73"],
  "text": "... raw chunk text ..."
}
```

### `chunk_type` values
| Type | Content |
|------|---------|
| `specification` | Standard values, tolerances, limits table |
| `torque` | Tightening torque table |
| `procedure` | Step-by-step removal/installation/inspection |
| `troubleshooting` | DTC table or symptom/cause/remedy |
| `diagram` | Text description of a diagram (figure codes, labels) |
| `general` | General information, safety, tools |
| `index` | Chapter index / table of contents |

---

## Build Knowledge Graph

See `builds/{car}/build-knowledge-graph.json` for car-specific graph.

Additional node types for builds:

### `ecu_pin`
| Field | Example |
|-------|---------|
| `id` | `"haltech-26-pin-23"` |
| `type` | `"ecu_pin"` |
| `connector` | `"26-pin"` |
| `pin_number` | `23` |
| `function` | `"CAN H"` |
| `wire_color` | `"W"` |

### `pdm_output`
| Field | Example |
|-------|---------|
| `id` | `"pdm-hp1"` |
| `type` | `"pdm_output"` |
| `name` | `"HP1"` |
| `pdm_pins` | `["A1", "A13"]` |
| `load` | `"Starter motor"` |
| `trigger` | `"STARTER_SAFE"` |
| `current_limit_a` | `20` |

### Additional build edges:
| Relationship | Source → Target |
|-------------|-----------------|
| `powered_by` | component → pdm_output |
| `signals_to` | component → ecu_pin |
| `can_receives` | pdm_output → `can_variable` |

---

## Authoring Notes

- Use `graph-editor.py` (planned) to add nodes/edges without editing JSON directly
- Node IDs are stable — never rename after creation (other files reference them)
- Add `"community_review": "pending"` to any forum-derived node for GitHub Issues review flow
- Source `"OpenGK"` nodes should include `url` pointing to the specific opengk.org page
