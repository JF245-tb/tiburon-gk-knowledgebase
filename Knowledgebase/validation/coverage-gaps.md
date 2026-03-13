# KB Coverage Gaps

Gaps identified by running validation test cases against the knowledgebase. Organized by system. Each gap is a candidate for new content — either from forum ingestion, manual extraction, or hands-on measurement.

---

## How This File Is Updated

1. **Automated:** Scheduled validation agents append new gaps after each test run.
2. **Manual:** Maintainer adds gaps discovered during research or build work.
3. **Resolved:** When content is added to cover a gap, move the entry to the "Resolved" section at the bottom with the file path and date.

---

## Open Gaps

### Ignition System

| Gap | Source | Test Case | Priority | Notes |
|-----|--------|-----------|----------|-------|
| Throttle body bracket position during reassembly | TC-001 (Charlie-III) | TC-001 | High | Common mistake after plug service. Bracket goes against TB only, not between intake and TB. No shop manual warning. |
| TB-area connector swap risk (black vs dark grey pair) | TC-001 (Charlie-III) | TC-001 | High | Two physically similar connectors near throttle body can be swapped. No shop manual callout. |
| Ground strap access context during plug service | TC-001 (Charlie-III) | TC-001 | Medium | Ground distribution exists in ETM schematics but not cross-linked to ignition service procedures. |
| Coil pack brand quality ranking | TC-001 (chase206) | TC-001 | Medium | OEM part numbers exist but explicit "use OEM/NTK only, avoid cheap aftermarket" guidance is not in KB. |
| Champion spark plug listed as valid — contradicts experts | TC-001 / RUN-001 | TC-001 | **High** | `pn-spark-plug-champion-v6-unleaded` (RC10YPYP4) in knowledge graph from factory manual. Charlie-III + chase206 say Champion has wrong internal resistance for 2.7L Delta ignition → causes rough idle. Add warning or deprecate node. |
| Brake cleaner spray method for vacuum leak detection | TC-001 (chase206) | TC-001 | Low | Vacuum leak diagnosis procedures exist in fuel-system/ but the field-expedient "spray brake cleaner and listen for RPM dip" method is not documented. |

### Engine Mechanical

*(No gaps identified yet)*

### Fuel System

*(No gaps identified yet)*

### Suspension

*(No gaps identified yet)*

### Drivetrain

*(No gaps identified yet)*

### Electrical / ECU

*(No gaps identified yet)*

---

## Resolved Gaps

| Gap | Resolved By | File | Date |
|-----|-------------|------|------|
| *(none yet)* | | | |

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total open gaps | 6 |
| Critical gaps (High priority) | 3 |
| Test cases run | 1 |
| Last validation run | 2026-03-12 (RUN-001) |
| KB coverage (TC-001) | 42% (2.5/6 components) |
| KB critical coverage (TC-001) | 33% (1/3 critical components) |
| KB accuracy (TC-001) | 83% (Champion plug listing is misleading) |
