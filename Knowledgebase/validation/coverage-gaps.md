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
| EE-15 coil connector terminal figure not extracted | Manual extraction | — | **High** | `engine-electrical/ignition-system.md` has only a placeholder comment for the V6 coil terminal-ID drawing. Physical pin positions for terminals 1-4 are unknown from the KB. Workaround (electrical pin ID via common feed at terminal 2) added to that file; re-extract EE.pdf p.15 to close properly. |
| C118 pin count contradiction | ETM CC-18 vs EE-15 | — | **High** | `electrical-manual/cc-connector-configurations.md` lists C118 as 2-pin populated in a 4-pin CR04F027 housing. EE-15 describes four terminals (1-4) with terminal 2 as the shared feed — consistent with 3 wasted-spark primaries + 1 common. One source is wrong; verify against a physical connector. |
| mfi-control-v6.md ignition coil tables are unreliable | ETM SD-81 extraction | — | **High** | The "Ignition Coils (C118 to C116)" section lists **four** coils; the V6 wasted-spark pack has **three**. C116 is the front oxygen sensor per `hl-harness-layouts.md` (two places), not a coil. Wire colour/size columns in that table are internally inconsistent (e.g. colour `R` with size `1.25G/B`). Do not use for coil wire identification until re-extracted. |

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
