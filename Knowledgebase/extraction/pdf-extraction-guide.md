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
3. **Apply pitfall checks** (see "Known Extraction Pitfalls" below):
   - Separate wire color from wire size into distinct columns
   - Flag any `0.5O`/`0.50`-style ambiguities as `⚠️`
   - For pin numbers, cross-reference against ecm-pinouts.md
   - For sensor pinouts, verify pin 1 function against at least one other source
4. **Write the section file** to `common/shop-manual/{chapter}/{section}.md`

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
- [ ] **Cross-validation** (if file contains ECM pins or sensor pinouts):
  - [ ] Run Sensor Pinout Triangle check (Rule 1) — SD vs FLA vs ecm-pinouts.md
  - [ ] Run ECM Pin Uniqueness check (Rule 2) — no duplicate pin assignments
  - [ ] Run Wire Color Consistency check (Rule 3) — same wire, same color at both ends
  - [ ] Run Connector Pin Count Match (Rule 4) — matches connector-master-reference.md
  - [ ] Flag any values matching known OCR confusions (5↔9, 6↔8, 0↔O, B↔Br)
  - [ ] Mark flagged values as `⚠️` in V column rather than `⬜`

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

---

## Known Extraction Pitfalls (Lessons from Spot-Check Batch 001)

The first 20-item spot-check session (2026-03-12) found **3 mismatches in 20 checks** — a 15% error rate. The errors clustered around specific, predictable failure modes. All future extractions MUST check for these patterns.

### Pitfall 1: Wire Color vs Wire Size — The '0' / 'O' Confusion

**Problem:** In Hyundai ETM wire notation, `0.5O` means "0.5mm gauge, Orange wire." But OCR reads `0.5O` as `0.50` (numeric), losing the wire color entirely.

**Example:** MAF signal wire (SC-005) was extracted as `0.50` — ambiguous. Correct reading: `0.5O` = Orange wire, 0.5mm gauge.

**Rule:** When extracting wire sizes from schematics:
- If a wire notation ends in a letter that could be zero (O, D, possibly G), flag it as `⚠️` and note the ambiguity
- Always separate wire color and wire size into distinct columns: `| Wire Color | Wire Size |`
- Cross-check: Does the wire color make sense for the circuit? (e.g., sensor signals are often specific colors per Hyundai convention)

### Pitfall 2: Pin Swap Errors — When All Pins Are Wrong

**Problem:** The TPS (SC-003) had all 3 pins wrong. Pin 1 and 2 functions were swapped, and pin 3 had the wrong wire color. This was a single-point-of-failure error — one wrong assumption about pin numbering cascaded to all pins.

**Root cause:** FLA-46 has a pin diagram where the physical pin layout doesn't match the left-to-right reading order. The extraction assumed left-to-right = pin 1, 2, 3 when the connector face orientation was reversed.

**Rule:** For sensor connector pinouts:
- NEVER assume pin numbering from visual position alone
- Cross-reference at least 2 sources: schematic (SD.pdf) + component diagram (FLA chapter) + connector table (CC section)
- If pin functions seem "backwards" (e.g., ground on pin 1 when +5V is usually pin 1), flag as `⚠️` and note in the extraction
- For 3-pin sensors: the standard Hyundai pattern is Power/Signal/Ground but TPS is an exception (+5V/GND/Signal)

### Pitfall 3: ECM Pin Number Errors — Multiple Sources, Multiple Answers

**Problem:** CMP signal ECM pin was listed as pin 2 (SD.pdf extraction), then pin 6 (OpenGK wiki), but physically verified as **pin 7**. Three sources, three wrong answers.

**Root cause:** SD.pdf schematics show ECM pins in a bottom row with poor labeling. OCR misreads pin numbers easily. OpenGK wiki is community-maintained (T2 authority) and can have transcription errors.

**Rule:** For ECM pin assignments:
- Always prefer physical manual page verification over any digital source
- When two sources disagree on a pin number, mark BOTH as `⚠️ CONFLICT` and create a spot-check item
- ECM pin numbers adjacent to the correct one (±1-2) are the most common error — check neighbors
- The `ecm-pinouts.md` file (OpenGK source) should never be treated as ground truth without SD.pdf cross-reference

### Pitfall 4: OCR Digit Substitution

**Problem:** TPS ECM pin was extracted as pin 15 from SD.pdf, but correct pin is 19. Similar-looking digits are routinely swapped by OCR.

**Common OCR confusions in this manual set:**
| Reads as | May actually be | Context |
|----------|----------------|---------|
| 5 | 9 | Pin numbers (1-52 range) |
| 6 | 8 | Pin numbers |
| 1 | 7 | Pin numbers, especially with serifs |
| 0 (zero) | O (letter) | Wire color codes |
| B (Black) | Br (Brown) | Wire colors — always check if Br exists |
| G/B | G/W | Slash notation wire colors |

**Rule:** For any pin number or wire color that appears in a safety-critical table:
- Compare against the ecm-pinouts.md (OpenGK) value as a sanity check
- If the values differ, don't auto-resolve — create a spot-check item
- Flag digits that are common OCR confusions (5/9, 6/8, 1/7) with `⚠️` for priority verification

---

## Cross-Validation Rules (Mandatory for New Extractions)

Every new extraction that contains ECM pin assignments or sensor pinouts MUST pass these cross-checks before the file can be considered complete:

### Rule 1: Sensor Pinout Triangle

For each sensor, verify the pinout appears consistently across 3 sources:

```
SD.pdf (schematic) ←→ FLA chapter (component diagram) ←→ ecm-pinouts.md (OpenGK)
```

If any two disagree on pin number, wire color, or function → `⚠️ CONFLICT` → create spot-check item.

### Rule 2: ECM Pin Uniqueness

Each ECM pin should have exactly ONE function. After extraction:
- Scan all `C133-x pin N` references in the file
- Check for duplicates (same pin, different function = extraction error)
- Check for gaps (pin referenced in schematic but missing from ecm-pinouts.md = potential data loss)

### Rule 3: Wire Color Consistency

The same wire should be the same color at both ends:
- Sensor side: Color listed in the sensor connector pinout table
- ECM side: Color listed in the ECM connector table (Master ECM Pinout Table)
- If they differ → flag and investigate (could be a splice point, or could be an error)

### Rule 4: Connector Pin Count Match

The number of pins in a pinout table must match `connector-master-reference.md`:
- If the reference says C113 has 3 pins, the pinout table must have exactly 3 rows
- If they don't match → investigate (could be unused pins, or missing data)

### Rule 5: Quick-Reference Table Audit

After any correction to a detailed pinout table:
- Also update the Quick Reference summary table at the top of the file
- Also update the knowledge graph `quick_pinout` for that component
- Also update `LLM-GUIDE.md` Quick Spec Reference if the value appears there
- The spot-check JSON note should list all files that were corrected

> **Principle:** Every fact must live in exactly one authoritative location, with all other references pointing back to it or being derived copies. When a correction is made, ALL derived copies must be updated in the same commit.
