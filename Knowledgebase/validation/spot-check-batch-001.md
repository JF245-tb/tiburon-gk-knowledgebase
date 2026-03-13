# Spot-Check Batch 001 — 2026-03-12

**Items:** 20 | **Source files:** 3 | **Categories:** wire colors, torque specs, dimensions, ECM pin assignments
**Result:** 17 verified ✅ | 3 mismatches 🔧 (TPS pinout, MAF wire color, CMP ECM pin)

## How to Use

1. Open each manual page listed below
2. Compare the **bold extracted value** to what you see on the page
3. Mark each item:
   - `[x]` = matches (correct extraction)
   - `[!]` = MISMATCH — write the correct value next to it
   - `[?]` = can't read clearly / ambiguous scan
4. After checking, tell Claude which items passed/failed — I'll update the `V` markers in source files and the spot-checks.json

---

## HIGH PRIORITY — Safety-Critical Wire Colors

These wire colors determine which fuse/circuit a sensor connects to. Wrong color = wrong circuit identification = potential wiring damage.

- [x] **SC-001** — SD.pdf p.78 → C113 (CKP) pin 2 signal wire = **Yellow (Y), 0.5mm** ✅
- [x] **SC-002** — SD.pdf p.78 → C114 (CMP) pin 3 ground wire = **Brown (Br), 0.5mm** ✅ *(confirmed — user physically verified black, brown, and orange wires on CMP connector)*
- [!] **SC-003** — SD.pdf p.78 → C112 (TPS) all 3 pins = 🔧 **MAJOR CORRECTION**
  - Pin 1: Was GND (B) → Actually **+5V ref (G/W, 0.5)**
  - Pin 2: Was Signal (G/W) → Actually **GND (B, 0.5)**
  - Pin 3: Was +5V (O) → Actually **TPS signal (L/Blue, 0.5)**
- [x] **SC-004** — SD.pdf p.78 → C113 (CKP) pin 1 power wire = **Orange (O), 0.5mm** ✅
- [!] **SC-005** — SD.pdf p.78 → C125 (MAF) pin 3 signal wire = 🔧 **0.5O = Orange wire, 0.5mm gauge** *(resolved: '0' was 'O' for Orange)*
- [x] **SC-006** — SD.pdf p.78 → C114 (CMP) pin 2 signal wire = **Black (B), 0.5mm** ✅ *(unusual for signal but confirmed — user physically verified black, brown, and orange wires)*

## HIGH PRIORITY — Safety-Critical Torque Specs

Wrong torque on structural bolts = engine failure. Multi-step angle torque specs are the most error-prone for OCR.

- [x] **SC-007** — EMA.pdf p.5 → Cylinder head bolt = **25 + (58-62°) + (43-47°) Nm** ✅
- [x] **SC-008** — EMA.pdf p.5 → Main bearing cap M10 = **27-33 + (90°+94°) Nm** ✅ *(also noted: M8 bolts = 13-19+(90°-94°) Nm)*
- [x] **SC-009** — EMA.pdf p.5 → Connecting rod bolt = **16-20 + (90°+94°) Nm** ✅

## MEDIUM PRIORITY — Commonly Queried Torque Specs

- [x] **SC-010** — EMA.pdf p.5 → Cam sprocket bolt = **90-110 Nm** ✅
- [x] **SC-011** — EMA.pdf p.5 → Flywheel bolt = **73-77 Nm** ✅
- [x] **SC-012** — EMA.pdf p.5-6 → Intake manifold to cylinder head = **19-21 Nm** ✅

## MEDIUM PRIORITY — ECM Pin Assignments

These pin numbers are used for Haltech wiring and OBD diagnostics. A wrong pin number = wrong signal routing.

- [x] **SC-013** — ecm-pinouts.md: C133-3 pin 8 = **CKP signal** ✅
- [!] **SC-014** — ecm-pinouts.md: C133-4 pin 6 = **CMP signal** → 🔧 **Actually pin 7** *(OpenGK wiki had pin 6 — wrong. SD extraction had pin 2 — also wrong. Physical verification = pin 7)*
- [x] **SC-015** — ecm-pinouts.md: C133-3 pin 19 = **TPS input** ✅ *(original SD extraction said pin 15 — ecm-pinouts.md pin 19 was correct)*
- [x] **SC-016** — ecm-pinouts.md: C133-3 pin 1 = **MAF input** ✅

## MEDIUM PRIORITY — Engine Dimensions

OCR struggles with multi-digit decimal values at 0.001mm precision.

- [x] **SC-017** — EMA.pdf p.2 → Cylinder bore = **86.7 mm** ✅ *(user reports 86.68 — manual rounds to 86.7)*
- [x] **SC-018** — EMA.pdf p.2 → Cam height intake = **43.95-44.15 mm**, limit **43.45 mm** ✅
- [x] **SC-019** — EMA.pdf p.2 → Cam journal diameter = **25.964-25.980 mm**, limit **25.914 mm** ✅
- [x] **SC-020** — EMA.pdf p.4 → Oil pressure minimum = **50 kPa (7.3 psi)** at **75-90°C** oil temp ✅

---

## Summary

| Category | Items | Verified | Mismatches | Rate |
|----------|-------|----------|------------|------|
| Wire colors | 6 | 4 | 2 (TPS pinout, MAF color) | 67% |
| Torque specs | 6 | 6 | 0 | 100% |
| ECM pins | 4 | 3 | 1 (CMP pin 6→7) | 75% |
| Dimensions | 4 | 4 | 0 | 100% |
| **Total** | **20** | **17** | **3** | **85%** |

### Error Patterns Identified
1. **Wire color/size confusion (0 vs O)** — OCR cannot distinguish. New extraction rule: always separate color and size into distinct columns.
2. **Pin swap from diagram orientation** — Connector face vs wiring diagram orientation causes pin 1/2/3 reversal. New rule: cross-reference at least 2 sources for sensor pinouts.
3. **ECM pin off-by-one** — Multiple sources had adjacent-but-wrong pin numbers (2, 6 → actual 7). New rule: flag when sources disagree, create spot-check.

See `extraction/pdf-extraction-guide.md` → "Known Extraction Pitfalls" for the full lessons learned and cross-validation rules added as a result of this batch.
