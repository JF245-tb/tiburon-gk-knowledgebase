# PDF Extraction Guide

Step-by-step procedure for extracting factory manuals, schematics, and hardware datasheets into the knowledgebase markdown format.

---

## Tool: `scripts/extract-pdf.py`

Requires `pymupdf`: `pip install pymupdf`

### Commands

```bash
# Check PDF info (page count, OCR status, dimensions)
python scripts/extract-pdf.py manifest "path/to/manual.pdf"

# Extract specific pages as PNG images
python scripts/extract-pdf.py extract "path/to/manual.pdf" --pages 2-7 --output .work/section-name/ --dpi 200

# Batch extract multiple sections at once
python scripts/extract-pdf.py batch "path/to/manual.pdf" \
  --sections "specs:2-7,engine-block:8-27,main-moving:28-41" \
  --output .work/chapter-code/
```

Each extraction creates a `manifest.json` in the output directory with page metadata.

### OCR vs Scanned PDFs

The tool detects whether a PDF has a text layer:
- **OCR version** (has text): Can extract text directly via pymupdf, but formatting is often messy
- **Scanned version** (no text): Extract as PNG images, then use Claude vision to read and format

**Preferred workflow:** Extract as PNG images regardless, then use Claude vision for structured extraction. This gives better table formatting and catches OCR errors.

---

## Shop Manual Extraction SOP

### Phase 1: Identify the Chapter

1. Run `manifest` to check page count and structure
2. Open the PDF and identify the chapter code (e.g., EMA = Engine Mechanical Assembly)
3. Map the section boundaries — look for section headers, typically:
   - Specifications/torque tables (first few pages)
   - Special tools (usually 1 page)
   - Technical content sections (bulk of chapter)

### Phase 2: Batch Extract Pages

```bash
# Example: Engine Mechanical chapter
python scripts/extract-pdf.py batch "Tiburon-Shop-Manual/EMA.pdf" \
  --sections "specs:2-7,special-tools:8,engine-block:9-27,main-moving:28-41,cooling:42-54,lubrication:55-58,intake-exhaust:59-68,cylinder-head:69-74,timing:75-80" \
  --output .work/ema/
```

### Phase 3: Create Directory and _index.md

Create the target directory and index file:

```
common/shop-manual/{chapter-name}/
├── _index.md              ← Section map (see template below)
├── specifications.md      ← Specs + torque tables + special tools
├── {section-name}.md      ← One file per major section
└── ...
```

**_index.md template** (copy from a completed chapter like `engine-mechanical/_index.md`):

```markdown
---
source: {CODE}.pdf
chapter: {CODE}
engine: V6 (2.7L Delta G6BA)
pages: {N}
vehicle: 2003 Hyundai Tiburon (GK)
extraction_method: claude_vision
extraction_date: {YYYY-MM-DD}
verification_status: unverified
verified_fields: 0
total_fields: 0
last_verified: null
---

# {Chapter Title} — {CODE}

## Sections

| Section | Pages | File |
|---------|-------|------|
| General — Specifications | {CODE}-2 to {CODE}-N | [specifications.md](specifications.md) |
| {Section Name} | {CODE}-X to {CODE}-Y | [{slug}.md]({slug}.md) |
```

### Phase 4: Extract Content via Claude Vision

For each section's PNG images, read them into Claude and extract structured markdown:

1. **Read the PNG images** from `.work/{chapter}/{section}/`
2. **Extract text** preserving the manual's structure:
   - Spec tables → markdown tables with proper headers
   - Procedures → numbered steps with sub-steps
   - Torque values → include all units (N-m, kg-cm, lb-ft)
   - Diagrams → describe what they show, note figure codes (e.g., EAHA010A)
   - Callout numbers → map to component names
3. **Write the section file** to `common/shop-manual/{chapter}/{section}.md`

### Phase 5: Add Verification Columns

All data tables with extractable specs/values MUST include a `| V |` verification column:

```markdown
| Item | Standard Value | Service Limit | V |
|------|---------------|---------------|---|
| Cylinder bore | 86.7 mm (3.4134 in.) | — | ⬜ |
```

Markers: `⬜` = unverified, `✅` = verified, `⚠️` = suspect, `🔧` = corrected.

After adding V columns, count the total `⬜` markers and update the frontmatter `total_fields` value.

### Phase 6: Quality Checks

After extraction, verify:
- [ ] All spec values match the PDF (spot-check 5-10 values)
- [ ] Torque tables have all three unit columns AND a V column
- [ ] Page references are correct (e.g., "EMA-42" maps to correct content)
- [ ] Section headings match the manual's section codes
- [ ] Cross-references to other chapters are noted (e.g., "See FLA-20 for injector specs")
- [ ] Frontmatter includes all fields: source, chapter, section, pages, title, engine, extraction_method, extraction_date, verification_status, verified_fields, total_fields, last_verified
- [ ] Generate 5-10 spot-check items in `validation/spot-checks.json` for the new file's critical values

---

## Markdown Formatting Conventions

### Spec Tables

```markdown
| Item | Standard Value | Service Limit | V |
|------|---------------|---------------|---|
| Cylinder bore | 86.7 mm (3.4134 in.) | — | ⬜ |
| Piston-to-bore clearance | 0.02-0.04 mm (0.0008-0.0016 in.) | 0.05 mm (0.002 in.) | ⬜ |
```

### Torque Tables

```markdown
| Fastener | N-m | kg-cm | lb-ft | V |
|----------|-----|-------|-------|---|
| Camshaft sprocket bolt | 90-110 | 900-1100 | 65-80 | ⬜ |
```

### Procedures

```markdown
## Removal

1. Disconnect the negative battery terminal.
2. Remove the air cleaner assembly.
   a. Disconnect the air intake hose.
   b. Remove the 3 mounting bolts.
3. Disconnect the coolant temperature sensor connector (C105-2).

> **CAUTION:** Do not reuse the cylinder head gasket.

> **NOTE:** Refer to EMA-42 for coolant system drain procedure.
```

### Diagrams and Figures

```markdown
*Figure EAHA010A — Valve spring installation. Callouts: (1) retainer, (2) valve spring, (3) spring seat, (4) oil seal.*
```

When a diagram contains measurements or specifications, extract those into the text. When it's a visual-only diagram (e.g., component location), describe what it shows.

### Section Codes

Preserve the Hyundai section identifier codes when present (e.g., `EMCO100`, `EDHA2300`). These enable precise cross-referencing.

---

## Schematic Extraction (ETM SD.pdf)

Schematics follow a different pattern — each circuit becomes a structured file with:

1. **Circuit title and SD page range**
2. **Component table** — every component in the circuit with:
   - Component name
   - Connector code (e.g., C133-1)
   - Pin number
   - Wire color and gauge
3. **Circuit path** — trace from power source through components to ground
4. **Ground points** — physical location codes
5. **Related fuses and relays** — with ratings

See `common/electrical-manual/schematics/mfi-control-v6.md` for a completed example.

---

## Hardware Datasheet Extraction

Hardware datasheets (AIM, Haltech, etc.) extract differently:

1. **Pinout tables** are the primary target — extract complete pin assignments
2. **CAN bus configuration** — protocol, baud rate, message IDs
3. **Power requirements** — voltage, current draw per output
4. **Connector types** — physical connector part numbers and pin counts

Output goes to `hardware/{manufacturer}/{device}/` following existing patterns (e.g., `hardware/aim/aim-pdm/pdm-pinout.md`).

Hardware datasheets are **T2 authority** for the specific device (manufacturer data), but **T2 for GK Tiburon fitment context** (how it connects to the car is build-specific).

---

## Working Directory

All intermediate extraction files (PNG images, manifests) go in `.work/` which is gitignored:

```
scripts/.work/
├── ema/          ← Engine Mechanical pages
│   ├── specs/
│   ├── engine-block/
│   └── manifest.json
├── fla/          ← Fuel System pages
└── ...
```

Final markdown files go in their permanent locations under `common/shop-manual/`, `common/electrical-manual/`, or `hardware/`.

---

## Chapters Completed vs Pending

**Completed (split into section files):**
- EMA — Engine Mechanical (V6) — 9 section files
- FLA — Fuel System — 6 section files
- SD — Schematic Diagrams — 37 circuit files

**Pending (need split extraction):**
- EM (I4 Engine Mechanical), EE, EC, CL, TR, DA, SS, ST, BR, BE, BD, HA, RT, GI, BCM

See `extraction/README.md` for the full status table.
