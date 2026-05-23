Implement job scrapers

Goal: Build scrapers for chosen job sources (RSS/APIs/HTML) that return normalized job items.

Inputs:
- Source URLs and filters from scope step

Outputs:
- One or more scraper modules returning job dicts: `{id, title, company, location, url, posted_at, source}`
- Acceptance criteria: Scraper returns recent items and handles errors gracefully

Steps:
1. Prefer RSS or public APIs for reliability.
2. For HTML-only sites, use `requests` + `BeautifulSoup`.
3. Add simple tests/mock data.
