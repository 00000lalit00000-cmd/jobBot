Add storage & deduplication

Goal: Store scraped job items and avoid duplicate notifications.

Inputs:
- Normalized job items from scrapers

Outputs:
- `db.py` with methods: `init_db()`, `save_job(job)`, `is_seen(job)`
- Acceptance criteria: Same job not notified twice within configured window

Steps:
1. Use SQLite with a simple schema storing `id`, `title`, `company`, `url`, `posted_at`, `seen_at`.
2. Implement hashing or composite unique constraint for deduplication.
