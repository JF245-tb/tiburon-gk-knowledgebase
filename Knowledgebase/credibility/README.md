# Source Credibility & Weighting System

This directory contains the scoring internals for evaluating external sources, contributors, and individual claims ingested into the knowledgebase. It extends the T1-T4 authority tier system defined in `ARCHITECTURE.md` by adding granular, numeric credibility scores *within* each tier.

---

## How It Works

Every claim in the knowledgebase has an `authority_tier` (1-4) from ARCHITECTURE.md. The credibility system adds a **composite score** (0-10) that provides finer resolution. Two T3 claims can now be compared: a stickied guide from Charlie-III (5.6) vs. a question post from a new user (2.6).

**The tier system is not replaced.** Tier promotion still follows the GitHub Issues workflow in ARCHITECTURE.md Section 7. Credibility scores help maintainers prioritize which claims to review first and help LLMs weight conflicting same-tier sources.

---

## Files in This Directory

| File | Purpose |
|------|---------|
| `sources.json` | External source registry — sites, wikis, manuals with base credibility scores |
| `contributors.json` | Known contributor registry — forum users with credibility weights |
| `forum-sections.json` | NewTiburon.com section mapping to KB topics + section-level modifiers |
| `scoring-algorithm.md` | Composite credibility formula with worked examples |
| `post-classification.md` | Post type definitions and their credibility modifiers |

---

## Quick Reference: Score Ranges

| Score | Effective Tier | Meaning |
|-------|---------------|---------|
| 10.0 | T1 | Factory manual — authoritative |
| 9.0-9.5 | T2 | OpenGK wiki / manufacturer datasheets |
| 5.5-8.0 | T3 | Vetted forum content, expert contributors |
| 0-5.4 | T4 | Unvetted posts, new users, web data |

---

## Adding a New Source

1. Open `sources.json`.
2. Add a new key under `"sources"` following the existing entries.
3. Set `authority_tier` based on source type (factory=T1, wiki=T2, forum=T3, web=T4).
4. Set `base_credibility` to the tier's canonical score, adjustable within range.
5. Fill `content_types[]` and optionally `coverage{}`.
6. Commit with a message referencing the source addition.

## Adding a New Contributor

1. Open `contributors.json`.
2. Copy the `_template` block and rename the key to the username.
3. Fill in metadata from the user's forum profile.
4. Calculate initial `credibility_weight` using the formula in `scoring-algorithm.md` Section 2.
5. Set `priority_contributor: true` only for maintainer-identified experts.
6. Commit.

## Scoring a Forum Post

1. Look up the source in `sources.json` → get `base_credibility` (S).
2. Look up the author in `contributors.json` → get `credibility_weight` (C). Default 2 if unknown.
3. Classify the post using `post-classification.md` → get post type modifier (P).
4. Look up the forum section in `forum-sections.json` → get `section_credibility_modifier` (F).
5. Apply the formula in `scoring-algorithm.md` → get `credibility_score`.
6. Record on the knowledge graph node as `credibility_score` + `credibility_breakdown`.

---

## Integration Points

- **ARCHITECTURE.md Section 12** — references this system
- **LLM-GUIDE.md** — directs AI models to check credibility when resolving conflicts
- **knowledge-graph-schema.md** — `credibility_score` and `credibility_breakdown` fields on `forum_post` and `part_number` nodes
- **forum/thread-index.json** — thread records carry `post_type`, `credibility_score`, `contributor_weights`
- **validation/** — test framework that uses forum questions to validate KB coverage

---

## Related Files

| File | Location |
|------|----------|
| Authority tiers | `ARCHITECTURE.md` Sections 1-3 |
| Trust ladder | `ARCHITECTURE.md` Section 2 |
| GitHub Issues workflow | `ARCHITECTURE.md` Section 7 |
| Knowledge graph schema | `common/knowledge-graph-schema.md` |
| Forum thread index | `forum/thread-index.json` |
| Validation test cases | `validation/test-cases.json` |
