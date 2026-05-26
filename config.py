<<<<<<< HEAD
import os
from dotenv import load_dotenv

load_dotenv()

# Optional separate configuration file for secrets and source lists.
# Use config_secrets.py to keep sensitive values out of .env.
try:
    import config_secrets as secrets
except ImportError:
    secrets = None


def _coalesce(*values):
    """Return the first value that is not empty or None."""
    for value in values:
        if value is None:
            continue
        if isinstance(value, str) and value.strip() == '':
            continue
        if isinstance(value, (list, tuple)) and len(value) == 0:
            continue
        return value
    return ''


def _split_list(value):
    """Split a string or list of values into a cleaned Python list.

    This helper accepts:
    - comma-separated strings
    - Python lists or tuples
    - values loaded from config_secrets.py

    URL inputs keep comma-separated query parameters intact.
    """
    if isinstance(value, (list, tuple)):
        return [str(item).strip() for item in value if item is not None and str(item).strip()]

    if not value:
        return []

    raw = str(value).strip()
    if not raw:
        return []

    is_url_list = 'http://' in raw or 'https://' in raw or 'www.' in raw or '://' in raw
    if not is_url_list:
        return [item.strip() for item in raw.split(',') if item.strip()]

    parts = []
    current = None
    for fragment in raw.split(','):
        fragment = fragment.strip()
        if not fragment:
            continue
        looks_like_url = fragment.startswith('http') or fragment.startswith('www') or '://' in fragment
        if current is None:
            current = fragment
        elif looks_like_url:
            parts.append(current)
            current = fragment
        else:
            current = current + ',' + fragment
    if current is not None:
        parts.append(current)

    return [item.strip() for item in parts if item.strip()]


def _normalize_database_url(value):
    if not value:
        return 'jobs.db'
    if value.startswith('sqlite:///'):
        return value.replace('sqlite:///', '', 1)
    if value.startswith('sqlite://'):
        return value.replace('sqlite://', '', 1)
    return value


TELEGRAM_TOKEN = _coalesce(
    os.getenv('TELEGRAM_TOKEN'),
    getattr(secrets, 'TELEGRAM_TOKEN', None) if secrets else None,
    ''
)
CHAT_ID = _coalesce(
    os.getenv('CHAT_ID'),
    getattr(secrets, 'CHAT_ID', None) if secrets else None,
    ''
)

# Backwards-compatible: allow multiple tokens / chat ids as comma-separated lists
TELEGRAM_TOKENS = _split_list(
    _coalesce(
        os.getenv('TELEGRAM_TOKENS'),
        getattr(secrets, 'TELEGRAM_TOKENS', None) if secrets else None,
        TELEGRAM_TOKEN,
    )
)
CHAT_IDS = _split_list(
    _coalesce(
        os.getenv('CHAT_IDS'),
        getattr(secrets, 'CHAT_IDS', None) if secrets else None,
        CHAT_ID,
    )
)

DATABASE_URL = _normalize_database_url(os.getenv('DATABASE_URL', 'jobs.db'))
RSS_URLS = _split_list(
    _coalesce(
        os.getenv('RSS_URLS'),
        getattr(secrets, 'RSS_URLS', None) if secrets else None,
        '',
    )
)
INSTAGRAM_ACCOUNTS = _split_list(
    _coalesce(
        os.getenv('INSTAGRAM_ACCOUNTS'),
        getattr(secrets, 'INSTAGRAM_ACCOUNTS', None) if secrets else None,
        '',
    )
)
COMPANY_CAREER_PAGES = _split_list(
    _coalesce(
        os.getenv('COMPANY_CAREER_PAGES'),
        getattr(secrets, 'COMPANY_CAREER_PAGES', None) if secrets else None,
        '',
    )
)
JOB_KEYWORDS = _split_list(
    _coalesce(
        os.getenv('JOB_KEYWORDS'),
        getattr(secrets, 'JOB_KEYWORDS', None) if secrets else None,
        'job,developer,engineer',
    )
)
SCHEDULE_CRON = _coalesce(
    os.getenv('SCHEDULE_CRON'),
    getattr(secrets, 'SCHEDULE_CRON', None) if secrets else None,
    '0 7 * * *',
)
SCRAPE_INTERVAL_MINUTES = int(os.getenv('SCRAPE_INTERVAL_MINUTES', '15'))
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
TELEGRAM_PARSE_MODE = os.getenv('TELEGRAM_PARSE_MODE', 'Markdown')

=======
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

>>>>>>> origin/main
