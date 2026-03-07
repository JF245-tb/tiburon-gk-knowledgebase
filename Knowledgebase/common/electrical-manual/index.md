# Electrical Troubleshooting Manual — Index
**Vehicle:** 2003 Hyundai Tiburon (GK)
**Source PDFs:** `Electrical Troubleshooting Manual/` (repo root)

---

## Chapters

| Chapter | Code | Pages | PDF | Content |
|---------|------|-------|-----|---------|
| General Information | GI | 12 | `Electrical Troubleshooting Manual/GI.pdf` | Wire color codes, connector notation, how to use ETM |
| Connector Configurations | CC | 24 | `Electrical Troubleshooting Manual/CC.pdf` | Connector pinouts by harness section |
| Component Locations | CL | 34 | `Electrical Troubleshooting Manual/CL.pdf` | Physical location of each connector on the car |
| Harness Layouts | HL | 20 | `Electrical Troubleshooting Manual/HL.pdf` | Harness routing diagrams (visual — connector code positions) |
| Schematic Diagrams | SD | 212 | `Electrical Troubleshooting Manual/SD.pdf` | Full circuit schematics by system |

> **Note:** All content in this ETM is diagram-based. The `.md` files in this directory contain the chapter indexes only. For actual connector pinouts, component positions, and circuit traces, open the PDFs directly.

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

## Connector Code Format

Connectors in the ETM use codes like `C133-1`, `IS/129`, `M37`, `G14`:

| Prefix | Type | Example |
|--------|------|---------|
| `C` + number | Named connector (ECM, BCM, sensor) | `C133-1` = ECM main connector |
| `IS/` + number | Inspection / splice connector | `IS/129` |
| `M` + number | Multiplex / junction connector | `M37` |
| `G` + number | Ground point | `G14` = chassis ground point 14 |

Connector codes cross-reference between CC (pinout), CL (location), and SD (schematic) sections using the same code.
