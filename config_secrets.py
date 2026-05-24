"""Optional per-install configuration for jobBot.

Place your secret values and source lists here instead of keeping them in .env.

This file is imported by config.py if present. Values set here are used when no
corresponding environment variable is provided.

Do not commit your real token/chat IDs to version control. config_secrets.py is
ignored by .gitignore once you add real values.
"""

# Telegram bot settings
TELEGRAM_TOKEN = ''  # Your bot token goes here
CHAT_ID = ''         # Your Telegram chat id

# Optional: support multiple bot tokens and chat ids in a separate list.
# If one of the above single values is populated, it is still used.
TELEGRAM_TOKENS = []
CHAT_IDS = []

# Job sources
RSS_URLS = [
    'https://remoteok.com/remote-jobs.rss?tags=python',
    'https://weworkremotely.com/categories/remote-programming-jobs.rss?query=python',
]
INSTAGRAM_ACCOUNTS = []
COMPANY_CAREER_PAGES = [
    'https://www.google.com/careers',
    'https://www.amazon.jobs/',
]

# Filtering and schedule
JOB_KEYWORDS = ['python', 'developer', 'engineer', 'java', 'nodejs', 'react', 'fullstack']
SCHEDULE_CRON = '0 7 * * *'
