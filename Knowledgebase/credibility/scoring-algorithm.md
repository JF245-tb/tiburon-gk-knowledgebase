# Credibility Scoring Algorithm

This document defines the composite credibility formula that produces a numeric score (0.0-10.0) for any claim ingested into the knowledgebase. The score provides granularity *within* the T1-T4 authority tiers defined in `ARCHITECTURE.md`.

---

## 1. Inputs

| Variable | Symbol | Range | Source |
|----------|--------|-------|--------|
| Source base credibility | `S` | 0-10 | `credibility/sources.json` → `base_credibility` |
| Contributor weight | `C` | 0-7 | `credibility/contributors.json` → `credibility_weight` (default 2 if unknown) |
| Post type modifier | `P` | -1 to +2 | `credibility/post-classification.md` |
| Forum section modifier | `F` | -1 to +1 | `credibility/forum-sections.json` → `section_credibility_modifier` |
| Engagement signal | `E` | 0 or 1 | 1 if (views > 50,000 AND replies > 50 AND participants > 10) |
| Corroboration count | `K` | 0+ | Knowledge graph node `corroboration_count` |
| Trust ladder position | `T` | 0-4 | Numeric: community_report=0, multiple_reports=1, verified_fit=2, measured=3, factory_spec=4 |

---

## 2. New Contributor Initial Weight Formula

When adding a contributor not yet in `contributors.json`, calculate their starting weight:

```
initial_weight = 2    (base for any unknown contributor)

Additive modifiers (each +1, cumulative):
  +1  if role is moderator or administrator
  +1  if post_count >= 1000
  +1  if member tenure >= 5 years
  +1  if expertise_areas overlap with the claim's topic/system
  +1  if identified by maintainer as known expert (priority_contributor = true)

Maximum individual weight: 7
```

Nobody reaches 10 — that is reserved for factory manual data. The cap of 7 means even the most trusted individual contributor still ranks below OpenGK (9) or factory sources (10).

---

## 3. Composite Score Formula

### T1 / T2 Sources (Factory, OpenGK, Manufacturer Datasheets)

No modifiers — the base credibility passes through directly:

```
final_score = base_credibility
```

T1 = 10.0, OpenGK = 9.0, manufacturer datasheets = 9.0.

### T3 / T4 Sources (Forum, Web) — Full Formula

```
# Weighted combination of three factors:
#   30% source reputation, 40% contributor credibility, 30% post context
raw = (0.30 * S) + (0.40 * C) + (0.30 * (5 + P + F))

# Engagement bonus (popular thread is a weak signal, not proof)
raw = raw + (0.3 * E)

# Corroboration bonus (diminishing returns)
if K >= 3:  raw = raw + 0.5
if K >= 5:  raw = raw + 0.3   # total +0.8 for 5+ corroborations

# Trust ladder bonus (accumulated evidence)
trust_bonus = T * 0.5          # 0.0 to 2.0
raw = raw + trust_bonus

# Clamp to valid range
final_score = max(0.0, min(10.0, raw))
```

### Effective Tier Mapping

Map the composite score back to a display tier:

| Score Range | Effective Tier | Meaning |
|-------------|---------------|---------|
| >= 9.5 | T1 | Promoted to factory-equivalent (only if trust_level = factory_spec) |
| >= 8.0 | T2 | Strong community consensus with measurement evidence |
| >= 5.5 | T3 | Credible forum content from known contributors |
| < 5.5 | T4 | Unvetted, low confidence, or question posts |

**Important:** The effective tier is advisory. Actual tier promotion still requires the maintainer-driven GitHub Issues workflow (ARCHITECTURE.md Section 7). A high credibility score helps prioritize which claims to review first.

---

## 4. Worked Examples

### Example A — Stickied guide from Charlie-III in Engine Management

| Input | Value | Source |
|-------|-------|--------|
| S | 3 | newtiburon base_credibility |
| C | 5 | Charlie-III credibility_weight |
| P | +2 | stickied_guide |
| F | +1 | gk-engine-management section modifier |
| E | 1 | High views/replies (stickied post) |
| K | 0 | Not yet corroborated in KB |
| T | 0 | community_report |

```
raw = (0.30 * 3) + (0.40 * 5) + (0.30 * (5 + 2 + 1))
    = 0.9 + 2.0 + 2.4 = 5.3
raw = 5.3 + 0.3 + 0 + 0 = 5.6

final_score = 5.6   →  effective T3
```

A respectable forum source. Needs corroboration to climb higher.

### Example B — Same guide after 5 corroborations + verified fit

Same inputs as A, but K=5 and T=2 (verified_fit):

```
raw = 5.3 + 0.3 + 0.8 + 1.0 = 7.4

final_score = 7.4   →  effective T3 (strong)
```

Approaching T2 territory. One more trust ladder step (measured) would push it to 7.9.

### Example C — Question post from new user in Exterior section

| Input | Value | Source |
|-------|-------|--------|
| S | 3 | newtiburon base_credibility |
| C | 2 | Unknown contributor (default weight) |
| P | -1 | question_post |
| F | -1 | gk-exterior section modifier |
| E | 0 | Low engagement |
| K | 0 | No corroboration |
| T | 0 | community_report |

```
raw = (0.30 * 3) + (0.40 * 2) + (0.30 * (5 - 1 - 1))
    = 0.9 + 0.8 + 0.9 = 2.6

final_score = 2.6   →  effective T4
```

Low credibility as a *source*. But valuable as a *test case* for the validation framework.

### Example D — OpenGK wiki entry

```
authority_tier = 2, base_credibility = 9
final_score = 9.0   →  effective T2
```

Passes through directly. No post-level modifiers for wiki sources.

### Example E — Technical reply from chase206 in V6 NA section

| Input | Value | Source |
|-------|-------|--------|
| S | 3 | newtiburon |
| C | 5 | chase206 credibility_weight |
| P | +1 | technical_reply (priority contributor, contains part numbers) |
| F | 0 | gk-v6-na section modifier |
| E | 0 | Normal thread |
| K | 0 | Fresh claim |
| T | 0 | community_report |

```
raw = (0.30 * 3) + (0.40 * 5) + (0.30 * (5 + 1 + 0))
    = 0.9 + 2.0 + 1.8 = 4.7

final_score = 4.7   →  effective T4
```

Even an expert's uncorroborated claim starts below T3 threshold. This is by design — individual claims need evidence before they're trusted. After 3 corroborations (K=3): 4.7 + 0.5 = 5.2, still T4. After verified_fit (T=2): 5.2 + 1.0 = 6.2, now T3.

---

## 5. LLM Query Behavior

When an AI model encounters multiple sources for the same claim:

1. **Sort by `authority_tier`** — lower tier number wins (T1 > T2 > T3 > T4).
2. **Within the same tier**, sort by `credibility_score` — higher score wins.
3. **If a T3 node has credibility_score >= 7.5 and no T1/T2 data exists**, present with moderate confidence and flag the tier.
4. **If a T3/T4 node contradicts T1/T2**, the T1/T2 source always wins regardless of credibility score.
5. **For build-specific overrides** (e.g., 170°F thermostat), the build profile takes precedence — see `builds/{car}/build-profile.json`.

---

## 6. Agent Task Entry Points

Scheduled agents that compute or update credibility scores should follow these workflows:

### Forum Ingestion Agent

```
1. Read credibility/sources.json → get source base_credibility
2. Read credibility/contributors.json → look up or create contributor entry
3. Read credibility/forum-sections.json → get section modifier
4. Read credibility/post-classification.md → classify post type
5. Compute credibility_score using this formula
6. Write to forum/thread-index.json with credibility fields
7. If claim is novel, add node to knowledge graph with credibility_score + credibility_breakdown
```

### Data Quality Audit Agent

```
1. Read forum/thread-index.json → iterate threads with credibility_score
2. For each thread, verify:
   - Contributor still exists in contributors.json
   - Post type classification is consistent with post-classification.md rules
   - credibility_score matches formula output (recompute and compare)
   - corroboration_count in knowledge graph matches GitHub Issues activity
3. Flag discrepancies in validation/coverage-gaps.md
4. Report summary: total threads audited, discrepancies found, scores recalculated
```

### KB Validation Test Agent

```
1. Read validation/test-cases.json → select test case(s)
2. Pose question to the knowledgebase (load LLM-GUIDE.md context)
3. Compare response to expected_answer_components
4. Record results in validation/test-results.json
5. Update validation/coverage-gaps.md with any new gaps
6. Report coverage_score and critical_coverage_score
```
