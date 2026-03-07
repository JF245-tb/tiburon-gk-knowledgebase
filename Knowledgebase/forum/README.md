# NewTiburon Forum Data
**Source:** https://www.newtiburon.com/
**Purpose:** Preserve community knowledge from key contributors for LLM lookup during builds.

---

## Status

| Phase | Status |
|-------|--------|
| Priority contributor list | In progress |
| Scraping methodology defined | In progress |
| Initial scrape | ☐ Not started |
| Data structured for LLM | ☐ Not started |

---

## Priority Contributors

Posts from these contributors are scraped and indexed first. They have the highest signal-to-noise ratio for technical content.

| Username | Known expertise | Priority |
|----------|----------------|----------|
| chase206 | Engine builds, suspension, race prep | **High** |
| *(add others)* | | |

**How to add:** Add a row with the username and what they're known for. The scraper will weight their posts higher in the index.

---

## Scraping Methodology

### What to Scrape

Target thread sections (V6 / GK-specific content only):
- Engine & Drivetrain
- Electrical & ECU
- Suspension & Handling
- Racing / Track
- Fabrication

Exclude:
- For Sale / Wanted
- I4 / GK2-specific threads (unless also V6-relevant)
- Off-topic / General Chat

### Thread Selection Criteria

1. **Priority contributor started or replied** — always include
2. **High reply count** (>15 replies) — likely contains useful debate/refinement
3. **Pinned/sticky** threads — official community wisdom
4. **Keywords:** G6BA, 2.7L, V6, Delta, Haltech, AIM, Lemons, endurance, COP, knock sensor, etc.

### Data Format

Each scraped thread is saved as:
```
forum/threads/{thread-id}/
├── metadata.json       ← thread title, URL, date, reply count
└── posts.json          ← array of {author, date, post_number, content}
```

`forum/thread-index.json` — searchable index of all threads (title, URL, contributor list, tags).

---

## Scraping Tools

### Option A: Manual (no cost, no risk)
1. Open thread in browser
2. Copy post content into `posts.json` template
3. Fill `metadata.json`
4. Tag with relevant keywords

### Option B: Python script (semi-automated)
Uses `requests` + `BeautifulSoup4` with a politeness delay (3–5 seconds between requests).
Does NOT bypass login walls or rate limiting.

```bash
pip install requests beautifulsoup4
python forum/scraper.py --thread-url "https://www.newtiburon.com/threads/..." --output forum/threads/
```

Script respects `robots.txt` and adds a `User-Agent` identifying itself.

### Option C: HTTrack / wget (mirror)
Full section mirror — useful for bulk download but creates large files. Not recommended as primary method since unstructured HTML is harder for LLMs.

---

## Legal / Ethical Notes

- NewTiburon.com is a public forum — posts are publicly accessible without login for most content
- The scrape is for personal/community use in a private/semi-private knowledgebase, not re-publication
- Individual post attribution is preserved (author field in `posts.json`)
- If a contributor asks to have their posts removed, delete the relevant `posts.json` entries
- Do not scrape at a rate that would stress the server — 3+ second delays between requests
- Check `robots.txt` at `https://www.newtiburon.com/robots.txt` before running automated scraping

---

## Index Structure

`forum/thread-index.json`:
```json
{
  "_meta": {
    "source": "https://www.newtiburon.com/",
    "last_scraped": "",
    "priority_contributors": ["chase206"]
  },
  "threads": {
    "484870": {
      "title": "Big Strong Arms — Front Lower Control Arms for the Lemons Tiburons",
      "url": "https://www.newtiburon.com/threads/big-strong-arms-front-lower-control-arms-for-the-lemons-tiburons.484870/",
      "section": "Racing / Track",
      "reply_count": 0,
      "has_priority_contributor": true,
      "tags": ["control-arms", "fabrication", "lemons", "heim-joint", "suspension"],
      "scraped": false
    }
  }
}
```

---

## Related Files

| File | Contents |
|------|----------|
| `forum/thread-index.json` | Searchable index of all threads |
| `forum/threads/{id}/metadata.json` | Thread metadata |
| `forum/threads/{id}/posts.json` | Post content |
| `forum/scraper.py` | Semi-automated scraping script (planned) |
