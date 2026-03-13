# KB Validation & Testing Framework

This directory contains a test framework that uses real forum questions to validate knowledgebase coverage and accuracy. The system compares AI model answers (using only the KB) against expert forum responses to identify coverage gaps and measure improvement over time.

---

## How It Works

1. **Extract questions** from real NewTiburon forum threads (classified as `question_post` in `credibility/post-classification.md`)
2. **Identify expert responses** from priority contributors (Charlie-III, chase206, etc.)
3. **Break expert answers into components** — each discrete piece of advice becomes an expected answer component
4. **Run the question** against the knowledgebase via an AI model
5. **Score the response** against expected components: what was covered, what was missed, what was hallucinated
6. **Track gaps** for content development prioritization

---

## Files in This Directory

| File | Purpose |
|------|---------|
| `test-cases.json` | Forum questions with expected answer components and expert attribution |
| `test-results.json` | Run results: model, KB version, coverage scores, missed components |
| `coverage-gaps.md` | Human-readable gap analysis organized by system, linked to action items |
| `spot-checks.json` | Individual extracted values to verify against physical manuals |
| `spot-check-batch-001.md` | Human-readable checklist for first verification session (20 items) |

---

## Test Case Structure

Each test case in `test-cases.json` contains:

- **id**: Unique identifier (TC-001, TC-002, ...)
- **title**: Short description of the scenario
- **source_thread**: Forum, section, URL of the original question
- **question**: The actual question text (rephrased for clarity if needed)
- **engine**: V6 / I4 / both
- **systems**: Which KB systems are relevant (ignition, fuel, suspension, etc.)
- **difficulty**: common / intermediate / advanced / edge_case
- **expected_answer_components**: Array of discrete claims the KB should produce, each with:
  - `claim`: What the answer should say
  - `kb_source_file`: Where this data lives in the KB (null if gap)
  - `authority_tier`: Tier of the source (null if gap)
  - `critical`: Whether this component is essential to a correct answer
  - `coverage_gap`: true if the KB lacks this information
- **expert_responses**: Attribution to forum experts who provided the answer
- **scoring**: Summary metrics (total components, critical count, KB coverage %)

---

## Scoring Metrics

| Metric | Formula | Meaning |
|--------|---------|---------|
| `accuracy_score` | correct / (correct + hallucinated) | Are the things we say actually right? |
| `coverage_score` | components_answered / total_components | How much of the expert answer do we cover? |
| `critical_coverage_score` | critical_answered / critical_components | Do we cover the must-know items? |

**Targets** (aspirational, not enforced):
- `accuracy_score >= 0.95` — almost never say wrong things
- `coverage_score >= 0.70` — cover most of what experts say
- `critical_coverage_score >= 0.90` — almost never miss critical items

---

## Agent Task Entry Points

### KB Validation Test Agent (Scheduled)

Run this agent periodically (weekly or after significant KB additions) to measure coverage:

```
Entry point: validation/README.md (this file)

Workflow:
1. Read validation/test-cases.json
2. For each test case (or a subset):
   a. Load LLM-GUIDE.md as context (this is what a user's AI session would load)
   b. Load the relevant build profile if the question is build-specific
   c. Pose the question to the knowledgebase
   d. Compare response to expected_answer_components
   e. Score: accuracy, coverage, critical_coverage
3. Append results to validation/test-results.json
4. Update validation/coverage-gaps.md with any NEW gaps discovered
5. Report summary: tests run, average scores, new gaps found
```

### Forum Question Extraction Agent (Scheduled)

Run this agent to find new test cases from forum threads:

```
Entry point: validation/README.md (this file)

Workflow:
1. Read forum/thread-index.json → find threads with post_type = "question_post"
2. For each unprocessed question thread:
   a. Read the question from the OP
   b. Check if expert replies exist (author in credibility/contributors.json with priority_contributor = true)
   c. If yes: extract expected answer components from expert replies
   d. Create a new test case entry
   e. Classify by system and difficulty
3. Append new test cases to validation/test-cases.json
4. Report: test cases added, systems covered, experts referenced
```

### Extraction Spot-Check System

Complements the test-case system above. While test cases validate that the KB can *answer questions correctly*, spot-checks validate that individual *extracted values are correct*.

**Files:**
- `spot-checks.json` — structured list of values to verify, with exact manual page lookups
- `spot-check-batch-NNN.md` — human-readable checklist (print or reference in the shop)

**Verification markers used in source files** (added as `V` column in data tables):

| Marker | Meaning |
|--------|---------|
| `⬜` | Unverified — raw OCR/AI extraction |
| `✅` | Verified — human confirmed against physical manual |
| `⚠️` | Suspect — known or likely OCR error, needs re-check |
| `🔧` | Corrected — was wrong, now fixed |

**Workflow:**
1. Open `spot-check-batch-NNN.md` for the current batch
2. Open the physical manual to each specified page
3. Compare extracted value to what's on the page
4. Mark pass/fail in the batch file
5. Claude updates: `spot-checks.json` status, source file `V` markers, frontmatter `verified_fields` count

**Priority order:** Safety-critical values first (power wire colors, structural bolt torques), then commonly-queried values, then general dimensions/clearances.

---

### Data Quality Audit Agent (Scheduled)

Cross-references credibility scores with actual KB content:

```
Entry point: credibility/scoring-algorithm.md Section 6

Workflow:
1. Recompute credibility scores for all forum-sourced nodes
2. Verify contributor weights are current
3. Check for stale test results (last run > 30 days)
4. Flag any credibility_score drift (score changed by > 0.5 since last audit)
5. Report to validation/coverage-gaps.md
```

---

## Related Files

| File | Location | Purpose |
|------|----------|---------|
| Credibility system | `credibility/README.md` | How sources and contributors are scored |
| Scoring formula | `credibility/scoring-algorithm.md` | The composite formula used to weight claims |
| Post classification | `credibility/post-classification.md` | How forum posts are typed (guide vs question) |
| Forum thread index | `forum/thread-index.json` | Master index of ingested forum threads |
| KB architecture | `ARCHITECTURE.md` | Authority tiers, trust ladder, design intent |
| LLM guide | `LLM-GUIDE.md` | How AI models navigate the KB (loaded during test runs) |
