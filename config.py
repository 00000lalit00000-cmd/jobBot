import os
from dotenv import load_dotenv

load_dotenv()


def _split_list(value):
    return [item.strip() for item in value.split(',') if item.strip()]


def _normalize_database_url(value):
    if not value:
        return 'jobs.db'
    if value.startswith('sqlite:///'):
        return value.replace('sqlite:///', '', 1)
    if value.startswith('sqlite://'):
        return value.replace('sqlite://', '', 1)
    return value


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '')
CHAT_ID = os.getenv('CHAT_ID', '')
DATABASE_URL = _normalize_database_url(os.getenv('DATABASE_URL', 'jobs.db'))
RSS_URLS = _split_list(os.getenv('RSS_URLS', ''))
INSTAGRAM_ACCOUNTS = _split_list(os.getenv('INSTAGRAM_ACCOUNTS', ''))
COMPANY_CAREER_PAGES = _split_list(os.getenv('COMPANY_CAREER_PAGES', ''))
JOB_KEYWORDS = _split_list(os.getenv('JOB_KEYWORDS', 'job,developer,engineer'))
SCHEDULE_CRON = os.getenv('SCHEDULE_CRON', '0 7 * * *')
SCRAPE_INTERVAL_MINUTES = int(os.getenv('SCRAPE_INTERVAL_MINUTES', '15'))
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
TELEGRAM_PARSE_MODE = os.getenv('TELEGRAM_PARSE_MODE', 'Markdown')

