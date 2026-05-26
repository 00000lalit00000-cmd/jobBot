# jobBot ΓÇö Job notification app

Minimal app to monitor job sources (RSS feeds, Instagram accounts) and send notifications to Telegram.

## Quick start

1. Create virtualenv and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install --upgrade pip
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and update values:

```powershell
copy .env.example .env
```

3. Fill in `TELEGRAM_TOKEN`, `CHAT_ID`, and at least one source:

- `RSS_URLS` for RSS feeds
- `INSTAGRAM_ACCOUNTS` for Instagram accounts
- `COMPANY_CAREER_PAGES` for company career pages
- `JOB_KEYWORDS` to filter matching posts

If `RSS_URLS` or `COMPANY_CAREER_PAGES` are not set in `.env`, the app will use the default fallback lists:

- `rss_urls.txt` — contains 200 RSS/feed sources
- `company_career_pages.txt` — contains 400 company career page URLs

These fallback files are loaded from `config.py` when the corresponding environment variables are empty.

4. Run the notifier once:

```powershell
python send_test.py
python main.py
```

## Run as scheduler service

```powershell
python service.py
```

This will run scraping periodically every `SCRAPE_INTERVAL_MINUTES`.

To stop the running scheduler, press `Ctrl+C` in the PowerShell window where `service.py` is running.

## Tests

```powershell
python -m unittest discover tests
```
