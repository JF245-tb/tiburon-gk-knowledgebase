# Electrical Troubleshooting Manual — Index
**Vehicle:** 2003 Hyundai Tiburon (GK)
**Source:** Hyundai Electrical Troubleshooting Manual (ETM) — GI, CC, CL, HL, SD chapters

---

## Chapters

| Chapter | Code | Pages | Status | File(s) |
|---------|------|-------|--------|---------|
| General Information | GI | 12 | Summarized below | This file |
| Connector Configurations | CC | 24 | Extracted | [`cc-connector-configurations.md`](cc-connector-configurations.md) |
| Component Locations | CL | 34 | Partial | [`component-locations.md`](component-locations.md) |
| Harness Layouts | HL | 20 | Extracted | [`hl-harness-layouts.md`](hl-harness-layouts.md) |
| Schematic Diagrams | SD | 212 | Complete (47 circuits) | [`schematics/_index.md`](schematics/_index.md) |

For the fastest way to go from a connector code or component name to every relevant section (CC pin count, CL location, SD schematic page, FLA shop-manual page, knowledge-graph node), start at [`connector-master-reference.md`](connector-master-reference.md) instead of browsing chapters individually.

---

## How to Use This Manual

To trace a circuit:

1. **SD** — Find the circuit schematic by system name (e.g., "MFI Control System 2.7L" → `schematics/mfi-control-v6.md`)
2. **CC** — Look up the connector code shown on the schematic to get pin assignments
3. **CL** — Look up the connector code to find its physical location on the vehicle
4. **HL** — Harness routing diagrams show how connectors relate spatially

---

## Wire Color Abbreviations (GI chapter)

| Code | Color |
|------|-------|
| B | Black |
| W | White |
| R | Red |
| G | Green |
| L | Blue |
| Y | Yellow |
| Br | Brown |
| O | Orange |
| Gr / GY | Gray |
| P / V | Violet / Purple |
| Lg | Light Green |
| Sb | Sky Blue |

Two-color wires: primary color listed first (e.g., `B/W` = Black with White tracer).

---

## Connector Notation

- **Connector views** are shown from the terminal side (wire entry) unless marked otherwise
- **Pin numbering** starts at top-left, reads left-to-right, top-to-bottom
- **Male/female** designation: connector body on harness side = female; component side = male

## Connector Code Format

Connectors in the ETM use codes like `C133-1`, `IS/129`, `M37`, `G14`:

| Prefix | Type | Example |
|--------|------|---------|
| `C` + number | Named connector (ECM, BCM, sensor) | `C133-1` = ECM main connector |
| `IS/` + number | Inspection / splice connector | `IS/129` |
| `M` + number | Multiplex / junction connector | `M37` |
| `G` + number | Ground point | `G14` = chassis ground point 14 |

Connector codes cross-reference between CC (pinout), CL (location), and SD (schematic) sections using the same code.
