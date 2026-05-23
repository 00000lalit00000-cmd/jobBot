Schedule jobs & orchestration

Goal: Run scrapers periodically and trigger notifications for new jobs.

Inputs:
- Scraper functions, notifier, and db

Outputs:
- `scheduler.py` that schedules scrapers using `APScheduler`
- Acceptance criteria: Scrapers run on a schedule and call notifier for unseen items

Steps:
1. Use `APScheduler` with `BackgroundScheduler` and cron-like intervals.
2. Add graceful shutdown handling and logging.
