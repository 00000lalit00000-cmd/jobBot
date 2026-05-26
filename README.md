<<<<<<< HEAD
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

2. Copy `.env.example` to `.env` and update values, or use `config_secrets.py` for secret/source configuration:

```powershell
copy .env.example .env
```

3. Fill in the required values.

Option A: Configure in `.env` as before.

Option B: Create `config_secrets.py` and set the values there.

The following values are supported in `config_secrets.py`:
- `TELEGRAM_TOKEN`
- `CHAT_ID`
- `RSS_URLS`
- `INSTAGRAM_ACCOUNTS`
- `JOB_KEYWORDS`
- `SCHEDULE_CRON`
- `COMPANY_CAREER_PAGES`

4. Fill in `TELEGRAM_TOKEN`, `CHAT_ID`, and at least one source:

- `RSS_URLS` for RSS feeds
- `INSTAGRAM_ACCOUNTS` for Instagram accounts
- `JOB_KEYWORDS` to filter matching posts

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
=======
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
- `JOB_KEYWORDS` to filter matching posts

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
>>>>>>> origin/main
