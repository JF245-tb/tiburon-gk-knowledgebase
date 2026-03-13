# Forum & Web Source Extraction Guide

Step-by-step procedure for ingesting forum threads, wiki pages, and web sources into the knowledgebase with proper credibility scoring and metadata.

---

## Quick Reference: Ingestion Pipeline

```
1. Select thread/page → 2. Extract content → 3. Classify → 4. Score → 5. Write to KB → 6. Open GitHub Issue
```

---

## NewTiburon Forum Thread Ingestion

### Step 1: Select and Index the Thread

Add the thread to `forum/thread-index.json` with basic metadata:

```json
{
  "THREAD_ID": {
    "title": "Thread title",
    "url": "https://www.newtiburon.com/threads/...",
    "section": "gk-v6-na",
    "author": "username",
    "reply_count": null,
    "view_count": null,
    "participants": null,
    "has_priority_contributor": false,
    "tags": [],
    "scraped": false
  }
}
```

**Section IDs** come from `credibility/forum-sections.json`:
- `gk-v6-na`, `gk-v6-fi`, `gk-i4-na`, `gk-i4-fi`
- `gk-engine-management`, `gk-transmissions`, `gk-wheel-tire-suspension`
- `gk-exterior`, `gk-interior`, `gk-audio-security`

### Step 2: Extract Content

**Critical: Handle "See More" truncation.** Long OPs on NewTiburon (XenForo) are collapsed. The hidden content is usually the most valuable part.

**Manual extraction:**
1. Open thread URL in browser
2. Click "See more" to expand the full OP
3. If multi-page, navigate through all pages
4. Copy content into the data format below

**Browser-assisted extraction (using Claude in Chrome):**
1. Navigate to thread URL
2. **Immediately call `window.stop()`** via javascript_tool to freeze the page before ad-redirect scripts fire (newer threads have aggressive redirects)
3. Find and click "See more" button to expand OP (note: clicking "See more" can also trigger a redirect — call `window.stop()` again if needed)
4. Execute `scripts/forum-scraper.js` via javascript_tool to extract all posts in one shot
5. For multi-page threads, navigate to each page (repeating `window.stop()` each time)

**Data format:**

```
forum/threads/{thread-id}/
├── metadata.json
└── posts.json
```

**metadata.json:**
```json
{
  "thread_id": "384866",
  "title": "Toyota COP Ignition Setup",
  "url": "https://www.newtiburon.com/threads/toyota-cop-ignition-setup.384866/",
  "forum": "newtiburon",
  "section": "gk-engine-management",
  "author": "JonGTR",
  "created": "2014-07-15",
  "reply_count": 7,
  "view_count": 7200,
  "participants": 2,
  "page_count": 1,
  "is_stickied": false,
  "last_post_date": "2014-07-31",
  "last_post_by": "Charlie-III",
  "extracted": "2026-03-12",
  "extracted_by": "JF245-tb"
}
```

**posts.json:**
```json
[
  {
    "post_number": 1,
    "author": "JonGTR",
    "date": "2014-07-15",
    "is_op": true,
    "content": "Full text of the post...",
    "has_images": true,
    "image_descriptions": [
      "Photo of 6 Toyota COP coils installed on V6 valve cover"
    ]
  },
  {
    "post_number": 2,
    "author": "Charlie-III",
    "date": "2014-07-31",
    "is_op": false,
    "content": "Reply text...",
    "has_images": false
  }
]
```

### Step 3: Classify the Thread

Apply post type and metadata flags per `credibility/post-classification.md`:

```json
{
  "post_type": "build_log",
  "engine": "I4",
  "ecu_requirement": "standalone",
  "build_applicability": ["white-tiburon"],
  "has_collapsed_content": true,
  "has_discontinued_parts": false,
  "has_embedded_images": true
}
```

**Post type decision tree:**
1. Stickied/pinned? → `stickied_guide` (+2)
2. Title has "OFFICIAL", "ULTIMATE", "LIST OF", "++++"? → `reference_compilation` (+2)
3. Title has "build", "project", "progress"? → `build_log` (+1)
4. Title has "?", "help", "issue", "problem"? → `question_post` (-1)
5. Default → `regular_discussion` (0)

**Engine detection keywords:** "V6", "2.7", "G6BA", "Delta" → V6; "I4", "2.0", "Beta", "G4GC" → I4

**ECU requirement keywords:** "Haltech", "Megasquirt", "standalone", "AEM" → standalone; "GKFlasher", "reflash", "Hondata" → reflash; "RIPP Black Box", "piggyback", "FMU" → piggyback

### Step 4: Score for Credibility

Follow `credibility/scoring-algorithm.md`:

1. Look up source base credibility: `credibility/sources.json` → newtiburon = 3
2. Look up contributor: `credibility/contributors.json` → get weight (default 2)
3. Get post type modifier from Step 3
4. Get section modifier: `credibility/forum-sections.json`
5. Compute: `raw = (0.30 * S) + (0.40 * C) + (0.30 * (5 + P + F)) + bonuses`

Add to thread-index.json:
```json
{
  "credibility_score": 5.6,
  "contributor_weights": { "Charlie-III": 5 }
}
```

### Step 5: Add Claims to Knowledge Graph (if applicable)

If the thread contains verifiable technical claims (part numbers, specs, fitment data):

1. Create `part_number` or `forum_post` node in the appropriate knowledge graph
2. Include `credibility_score` and `credibility_breakdown` fields
3. Set `authority_tier: 3`, `trust_level: "community_report"`, `corroboration_count: 0`

### Step 6: Open GitHub Issue for Vetting

Per `ARCHITECTURE.md` Section 7:
1. Open Issue with label `community-review` (or `forum-ingest`)
2. Include: thread URL, post author, claim quoted, credibility score
3. Community confirms or challenges the claim
4. Maintainer updates trust_level as corroboration accumulates

---

## OpenGK Wiki Ingestion

OpenGK content is T2 (base credibility 9/10). Simpler pipeline:

1. **Fetch the wiki page** via web fetch or manual copy
2. **Extract technical content** into `common/opengk/{topic}.md`
3. **Spot-check against T1** — if the wiki claim can be verified against factory manual, note it
4. **Add to knowledge graph** with `authority_tier: 2`, `source: "opengk"`
5. **No GitHub Issue needed** unless the claim contradicts T1 data

### OpenGK Content Structure

OpenGK is a MediaWiki organized by:
- General (VIN decoder, immobilizer, BCM, instrument cluster)
- Communication protocols (K-Line, CAN Bus)
- ECM Tuning (GKFlasher, firmware flashing)
- Hardware (L4 2.0L, V6 2.7L — PCB layouts, pinouts)
- Parts Compatibility (sensors, fuel injectors, camshafts)
- Downloads (firmware files, tools)

---

## Question Posts → Validation Test Cases

When extracting a `question_post` thread that has expert replies:

1. Add the thread to `forum/thread-index.json` as normal
2. Also create a test case in `validation/test-cases.json`:
   - Extract the question from the OP
   - Identify which KB systems are relevant
   - Parse expert replies into expected answer components
   - Note which components the KB currently covers vs gaps
3. Update `validation/coverage-gaps.md` with any new gaps

See `validation/README.md` for the test case schema and `validation/test-cases.json` for TC-001 as a worked example.

---

## Discontinued Parts Handling

When a thread references discontinued products:

1. Set `has_discontinued_parts: true` in thread-index.json
2. List specific items in `discontinued_parts[]`
3. Write a `general_knowledge_value` string capturing what survives:
   - Design parameters (dimensions, flow rates, boost levels)
   - Engineering principles (why equal-length headers matter)
   - Performance baselines (typical HP/TQ gains)
   - Compatible component specs (injector size, fuel pump flow)
   - Installation lessons learned

**Do not discard discontinued product threads.** The Tiburon aftermarket is largely dead — these threads preserve irreplaceable engineering knowledge.

---

## Batch Scraping Pipeline (10+ threads/day)

### Overview

The optimized pipeline uses a reusable JavaScript extractor (`scripts/forum-scraper.js`) that runs in any browser tab on a NewTiburon thread page. It returns structured JSON matching our `metadata.json` + `posts.json` format in a single execution.

**Throughput target:** 10 threads/day using 3-4 parallel agents.

### The Extraction Script

**File:** `scripts/forum-scraper.js`

The script is a self-contained IIFE that:
1. Clicks all "See more" expand buttons on the page
2. Extracts metadata (title, author, dates, page count, stickied status) from DOM
3. Extracts every post (author, date, content, images, post number)
4. Replaces images with `[IMAGE: alt]` placeholders
5. Collapses quotes into `[QUOTE author: preview...]` markers
6. Returns a JSON string with `{metadata, posts, _page_participants}`
7. Copies the result to clipboard as a convenience

**Usage via Claude in Chrome:**
```
1. Navigate to thread URL
2. Execute scripts/forum-scraper.js content via javascript_tool
3. Parse the returned JSON
4. Write metadata.json and posts.json to forum/threads/{id}/
```

**Multi-page threads:**
```
For each page (1..N):
  1. Navigate to thread URL + /page-{N}
  2. Execute extractor → get posts for that page
  3. Append posts to accumulated array
Merge: metadata from page 1, concatenated posts from all pages
Set metadata.participants = count of unique authors across all pages
```

### Parallel Agent Strategy

For maximum throughput, split threads across 3-4 concurrent agents:

```
Agent 1: Threads A, B, C (small — 1-2 pages each)
Agent 2: Threads D, E (medium — 3-5 pages)
Agent 3: Thread F (large — 8+ pages, all pages)
Agent 4: Thread G, H (small — 1-2 pages)
```

**Agent prompt template:**
```
Scrape the following NewTiburon forum threads into the knowledgebase.

For each thread:
1. Navigate to the thread URL using Claude in Chrome
2. Execute this JavaScript to extract posts: [paste scripts/forum-scraper.js]
3. Parse the returned JSON
4. Write metadata.json to Knowledgebase/forum/threads/{thread_id}/metadata.json
5. Write posts.json to Knowledgebase/forum/threads/{thread_id}/posts.json
6. For multi-page threads, navigate to each page and run the extractor again,
   then merge all posts into a single posts.json

Threads to scrape:
- {thread_id}: {url} ({page_count} pages)
- {thread_id}: {url} ({page_count} pages)
```

### Per-Thread Time Budget

| Thread Size | Pages | Est. Time | Notes |
|-------------|-------|-----------|-------|
| Small (1 page) | 1 | 30-45s | Navigate + extract + write |
| Medium (2-5 pages) | 2-5 | 1-3 min | Per-page navigation adds ~30s each |
| Large (6+ pages) | 6+ | 3-8 min | Consider scraping page 1 only for initial pass |

**Optimization rules:**
- Batch small threads (1-2 pages) into groups of 3-4 per agent
- Give large threads (8+ pages) their own dedicated agent
- For reference threads (stickied guides), scrape ALL pages — the content is worth it
- For question threads with <5 useful posts, page 1 is usually sufficient

### Post-Scrape Checklist

After all agents complete:

```
For each newly scraped thread:
  [ ] metadata.json exists with all fields populated
  [ ] posts.json has correct post count
  [ ] Classify post_type per credibility/post-classification.md
  [ ] Compute credibility_score per credibility/scoring-algorithm.md
  [ ] Update forum/thread-index.json: scraped=true, scores, contributor_weights
  [ ] If question_post with expert replies → create validation test case
  [ ] If coverage gap found → add to validation/coverage-gaps.md
```

---

## Agent Entry Points

### Forum Ingestion Agent (Scheduled)

```
Entry point: extraction/forum-extraction-guide.md (this file)
Extraction tool: scripts/forum-scraper.js

Workflow:
1. Read forum/thread-index.json for threads with scraped: false
2. Read scripts/forum-scraper.js for the extraction template
3. Split unscraped threads into batches by size (see Parallel Agent Strategy)
4. For each thread:
   a. Navigate to URL via Claude in Chrome
   b. Execute forum-scraper.js → parse JSON result
   c. For multi-page: repeat for each page, merge posts
   d. Write metadata.json + posts.json to forum/threads/{id}/
   e. Classify post type and compute credibility score
   f. Update thread-index.json: scraped=true, all metadata
5. Report: threads processed, scores assigned, gaps found
```

### New Thread Discovery Agent (Scheduled)

```
Entry point: extraction/forum-extraction-guide.md (this file)

Workflow:
1. Read credibility/forum-sections.json for target sections
2. Read credibility/contributors.json for priority contributor list
3. Search NewTiburon for recent threads matching:
   - Priority contributor posted
   - High reply count (>15)
   - Stickied/pinned
   - Keywords from forum/README.md thread selection criteria
4. For each new thread found:
   a. Check if already in thread-index.json (skip if yes)
   b. Add to thread-index.json with basic metadata
   c. Flag as scraped: false for the ingestion agent
5. Report: new threads discovered, sections covered
```

---

## Related Files

| File | Purpose |
|------|---------|
| `forum/README.md` | Forum data overview, scraping tools, legal notes |
| `forum/thread-index.json` | Master thread index |
| `credibility/sources.json` | Source base credibility scores |
| `credibility/contributors.json` | Contributor weights |
| `credibility/forum-sections.json` | Section → KB topic mapping |
| `credibility/scoring-algorithm.md` | Composite credibility formula |
| `credibility/post-classification.md` | Post types, metadata flags, classification workflow |
| `validation/test-cases.json` | Question posts as KB test cases |
| `validation/coverage-gaps.md` | Gap analysis from test runs |
