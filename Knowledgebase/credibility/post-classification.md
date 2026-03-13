# Post Classification System

This document defines post types and their credibility modifiers for forum content ingested into the knowledgebase. Modifiers are additive — they feed into the composite formula in `scoring-algorithm.md`.

---

## Post Types

| Post Type | Modifier | Detection Criteria |
|-----------|----------|-------------------|
| `stickied_guide` | **+2** | Pinned/stickied by moderators. Title often contains "HOW TO", "DIY", "GUIDE", "FAQ". Typically 100K+ views, 100+ replies. Long-lived, community-curated content. |
| `reference_compilation` | **+2** | Not necessarily stickied, but functions as a community reference. Title contains "OFFICIAL", "ULTIMATE", "LIST OF", "+++". Very high views (100K+), high participation. Often a master list or comparison of parts/specs. Treat like stickied_guide for scoring. |
| `build_log` | **+1** | Thread title contains "build", "project", "progress". Multi-page thread with photos. Single author narrative documenting a real build. |
| `technical_reply` | **+1** | Reply (not OP) from a `priority_contributor` or contributor with `credibility_weight >= 5`. Contains specific values, part numbers, or procedures. |
| `regular_discussion` | **0** | Normal thread post. Not stickied, not from a priority contributor. Baseline — no modifier up or down. |
| `parts_review` | **+1 / 0** | Thread about a specific part with fitment report. **+1** if includes install report with outcome. **0** if uninstalled review/opinion only. |
| `question_post` | **-1** | Thread started as a question. Title contains "?", "help", "issue", "problem", "anyone else". Author has < 50 posts. Low information value as a *source*, but valuable as a *test case* for the validation framework. |
| `necro_reply` | **0** | Reply to a thread that is > 3 years old and adds new data. Flag with `"age_gap": true` on the record. Old thread context may be outdated but the new reply may have current data. Requires human review. |

---

## Classification Rules

### When ingesting a thread

Each thread gets a primary `post_type` in `forum/thread-index.json`. Individual posts within a thread may have different types — for example, a `question_post` thread may contain a `technical_reply` from chase206. The thread-level type reflects the *originating post* character; reply-level types are tracked in `forum/threads/{id}/posts.json` if granular scoring is needed.

### Multiple types on one post

A post can only have one type. Use the **highest-modifier** type that applies:
- A stickied build log → `stickied_guide` (+2), not `build_log` (+1)
- A priority contributor answering a question → `technical_reply` (+1) for their specific post, even though the thread is `question_post` (-1)

### Engagement thresholds

The engagement signal `E` in the scoring formula is separate from post type, but correlated:

| Metric | Low | Medium | High |
|--------|-----|--------|------|
| Views | < 5,000 | 5,000-50,000 | > 50,000 |
| Replies | < 10 | 10-50 | > 50 |
| Participants | < 5 | 5-10 | > 10 |

`E = 1` only when ALL THREE are in the "High" column simultaneously. This is deliberately strict — a popular thread is a weak signal, not proof.

---

## Extraction Metadata Flags

Beyond post type, every ingested thread should carry these metadata flags in `forum/thread-index.json`. These are critical for filtering and routing content to the correct builds.

### Engine Applicability

| Flag | Values | Purpose |
|------|--------|---------|
| `engine` | `"V6"`, `"I4"`, `"both"`, `"unspecified"` | Which engine the thread's content applies to |

Many threads are written for one engine variant but the information *may* apply to the other. The `engine` flag records **what the thread claims**, not what we've verified independently. Cross-engine fitment is tracked separately in the knowledge graph via `source_vehicle` and `fit_notes` on `part_number` nodes.

**Example:** Thread 384866 (Toyota COP Ignition) is written for the I4 engine. The V6 uses the same coils (confirmed in our build), but the thread's mounting and wiring instructions are I4-specific. Flag as `"engine": "I4"` with a note.

### ECU Requirement

| Flag | Values | Purpose |
|------|--------|---------|
| `ecu_requirement` | `"stock"`, `"standalone"`, `"piggyback"`, `"reflash"`, `"any"` | What ECU setup is needed for the modification described |

This is critical for routing content between builds. The blue car (stock Siemens SIMK43) can only use `"stock"` or `"reflash"` content. The white car (Haltech Elite 2500) can use `"standalone"` content. Many forum posts assume stock ECU operation.

**Example:** COP conversion requires standalone ECU for coil-per-plug triggering. The supercharger Stage 2 requires the RIPP Black Box (piggyback). Headers are bolt-on with stock ECU.

### Discontinued Parts Flag

| Flag | Values | Purpose |
|------|--------|---------|
| `has_discontinued_parts` | `true` / `false` | Whether the thread references parts no longer available |
| `discontinued_parts` | string[] | List of discontinued products/manufacturers |
| `general_knowledge_value` | string | What general engineering knowledge survives beyond specific product availability |

Tiburon aftermarket support is largely discontinued. Most performance parts are no longer manufactured. Threads referencing these parts are still valuable for:
- Design parameters (tube diameter, boost pressure, flow rates)
- Engineering principles (equal-length headers vs log, centrifugal vs roots SC)
- Baseline performance expectations (HP/TQ gains by modification type)
- Compatible component specifications (injector size, fuel pump flow, intercooler sizing)
- Installation gotchas and lessons learned

**Example:** The V6 header thread lists 14+ manufacturers, most now defunct. But the thread preserves critical data: O2 bung locations, equal-length design advantages, typical HP gains (8-25hp), and ceramic coating benefits.

### Content Extraction Challenges

| Flag | Values | Purpose |
|------|--------|---------|
| `has_collapsed_content` | `true` / `false` | Whether the OP has a "See more" button hiding truncated content |
| `multi_page` | `true` / `false` | Whether the thread spans multiple pages |
| `page_count` | number \| null | Total pages if multi-page |
| `has_embedded_images` | `true` / `false` | Whether the thread contains images that carry information (diagrams, dyno charts, install photos) |

The "See more" button on NewTiburon (XenForo) collapses long OPs. **The collapsed content is often the most valuable part** — it typically contains the detailed specs, part numbers, and procedures. Any scraper or extraction agent MUST expand this content before extracting.

### Build Applicability

| Flag | Values | Purpose |
|------|--------|---------|
| `build_applicability` | string[] | Which builds can use this information |

Values: `"white-tiburon"` (Haltech/standalone), `"blue-tiburon"` (stock ECU), `"any-gk"` (platform-level), `"custom"` (requires specific hardware not in either build).

Derived from `engine` + `ecu_requirement` + thread content. If `ecu_requirement: "standalone"` and thread discusses V6, then `build_applicability: ["white-tiburon"]`.

---

## Agent Classification Workflow

When a scheduled agent ingests a new forum thread:

```
Phase 1: Content Extraction
1. Navigate to thread URL
2. Check for "See more" button on OP → expand before extracting (set has_collapsed_content: true)
3. Check page count → if multi-page, extract all pages
4. Note embedded images (dyno charts, install photos, diagrams)

Phase 2: Post Type Classification
5. Check if thread is stickied/pinned → stickied_guide (+2)
6. Check title keywords:
   - Contains "OFFICIAL", "ULTIMATE", "LIST OF", "+++", or functions as reference → reference_compilation (+2)
   - Contains "build", "project", "progress" → build_log (+1)
   - Contains "?", "help", "issue", "problem", "anyone else" → question_post (-1)
   - Contains "review", "installed", "fitment" → parts_review (+1/0)
7. Check author:
   - In contributors.json with priority_contributor = true → technical_reply (+1) if post contains specs
8. Default → regular_discussion (0)

Phase 3: Metadata Flags
9.  Determine engine applicability: scan for "V6", "I4", "2.7", "2.0", "G6BA", "Beta" keywords
10. Determine ECU requirement: scan for "standalone", "Haltech", "Megasquirt", "reflash", "GKFlasher", "piggyback"
11. Check for discontinued parts: scan for "out of business", "no longer available", "discontinued", dead URLs
12. Determine build applicability from engine + ecu_requirement combination

Phase 4: Reply Classification
13. Check reply author against contributors.json
14. Check reply content for part numbers, measurements, specific values
15. If priority contributor + technical content → technical_reply (+1)
16. Check reply age vs thread age → if gap > 3 years, flag age_gap: true
```

---

## Test Case Extraction

Posts classified as `question_post` are candidates for the validation test framework (`validation/test-cases.json`). The agent should:

1. Extract the question text from the OP
2. Identify which KB systems are relevant (engine, suspension, etc.)
3. Check if expert replies exist in the same thread
4. If expert replies exist, extract expected answer components
5. Create a test case entry with the question, expected components, and expert attribution

This creates a feedback loop: forum questions test our KB, expert answers reveal coverage gaps, and those gaps become new content targets.
