# Spot-Check Batch 001 — 2026-03-12

**Items:** 20 | **Source files:** 3 | **Categories:** wire colors, torque specs, dimensions, ECM pin assignments

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

- [ ] **SC-001** — SD.pdf p.78 → C113 (CKP) pin 2 signal wire = **Yellow (Y), 0.5mm**
- [ ] **SC-002** — SD.pdf p.78 → C114 (CMP) pin 3 ground wire = **Brown (Br), 0.5mm** *(previously misread as G/B — confirm correction)*
- [ ] **SC-003** — SD.pdf p.78 → C112 (TPS) pin 2 signal wire = **Green/White (G/W), 0.5mm**
- [ ] **SC-004** — SD.pdf p.78 → C113 (CKP) pin 1 power wire = **Orange (O), 0.5mm**
- [ ] **SC-005** — SD.pdf p.78 → C125 (MAF) pin 3 signal wire size = **0.50** *(or is this 0.5O meaning Orange?)*
- [ ] **SC-006** — SD.pdf p.78 → C114 (CMP) pin 2 signal wire = **Black (B), 0.5mm** *(unusual for a signal wire — verify)*

## HIGH PRIORITY — Safety-Critical Torque Specs

Wrong torque on structural bolts = engine failure. Multi-step angle torque specs are the most error-prone for OCR.

- [ ] **SC-007** — EMA.pdf p.5 → Cylinder head bolt = **25 + (58-62°) + (43-47°) Nm** *(3-step angle torque, cold engine)*
- [ ] **SC-008** — EMA.pdf p.5 → Main bearing cap M10 = **27-33 + (90°+94°) Nm**
- [ ] **SC-009** — EMA.pdf p.5 → Connecting rod bolt = **16-20 + (90°+94°) Nm**

## MEDIUM PRIORITY — Commonly Queried Torque Specs

- [ ] **SC-010** — EMA.pdf p.5 → Cam sprocket bolt = **90-110 Nm**
- [ ] **SC-011** — EMA.pdf p.5 → Flywheel bolt = **73-77 Nm**
- [ ] **SC-012** — EMA.pdf p.5-6 → Intake manifold to cylinder head = **19-21 Nm**

## MEDIUM PRIORITY — ECM Pin Assignments

These pin numbers are used for Haltech wiring and OBD diagnostics. A wrong pin number = wrong signal routing.

- [ ] **SC-013** — ecm-pinouts.md: C133-3 pin 8 = **CKP signal** *(cross-ref against SD.pdf p.78 ECM bottom row)*
- [ ] **SC-014** — ecm-pinouts.md: C133-4 pin 6 = **CMP signal** *(mfi-control-v6.md originally said pin 2 — which is correct?)*
- [ ] **SC-015** — ecm-pinouts.md: C133-3 pin 19 = **TPS input** *(original extraction said pin 15 — verify)*
- [ ] **SC-016** — ecm-pinouts.md: C133-3 pin 1 = **MAF input**

## MEDIUM PRIORITY — Engine Dimensions

OCR struggles with multi-digit decimal values at 0.001mm precision.

- [ ] **SC-017** — EMA.pdf p.2 → Cylinder bore = **86.7 mm (3.4133 in.)**
- [ ] **SC-018** — EMA.pdf p.2 → Cam height intake = **43.95-44.15 mm**, limit **43.45 mm**
- [ ] **SC-019** — EMA.pdf p.2 → Cam journal diameter = **25.964-25.980 mm**, limit **25.914 mm**
- [ ] **SC-020** — EMA.pdf p.4 → Oil pressure minimum = **50 kPa (7.3 psi)** at **75-90°C** oil temp
