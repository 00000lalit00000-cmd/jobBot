<<<<<<< HEAD
import requests
from config import TELEGRAM_TOKENS, CHAT_IDS, TELEGRAM_PARSE_MODE, TELEGRAM_TOKEN
from logger import setup_logging

logger = setup_logging()


def send_message(chat_id, text, token=TELEGRAM_TOKEN, parse_mode=None):
    if parse_mode is None:
        parse_mode = TELEGRAM_PARSE_MODE
    if not token:
        raise RuntimeError('Telegram token not provided')
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text,
        'disable_web_page_preview': True
    }
    if parse_mode:
        payload['parse_mode'] = parse_mode

    resp = requests.post(url, json=payload, timeout=15)
    if resp.status_code == 400 and parse_mode:
        try:
            details = resp.json().get('description', '')
        except ValueError:
            details = resp.text or ''
        if 'parse' in details.lower() or 'entities' in details.lower():
            payload.pop('parse_mode', None)
            resp = requests.post(url, json=payload, timeout=15)
    resp.raise_for_status()
    return resp.status_code, resp.text


def broadcast_message(text):
    """Send `text` to all configured chat ids using all configured tokens.

    Behavior: for each token, send to every chat id. This allows multiple bots
    or multiple recipients. If no tokens or chat ids configured, raise.
    """
    if not TELEGRAM_TOKENS:
        raise RuntimeError('No TELEGRAM_TOKENS configured')
    if not CHAT_IDS:
        raise RuntimeError('No CHAT_IDS configured')

    results = []
    for token in TELEGRAM_TOKENS:
        for chat in CHAT_IDS:
            try:
                status, text_resp = send_message(chat, text, token)
                results.append((token, chat, status))
                logger.debug('Sent message token=%s chat=%s status=%s', token[:8], chat, status)
            except Exception as e:
                logger.exception('Failed sending with token=%s chat=%s: %s', token[:8], chat, e)
    return results
=======
import requests
from config import TELEGRAM_TOKEN, TELEGRAM_PARSE_MODE


def send_message(chat_id, text):
    if not TELEGRAM_TOKEN:
        raise RuntimeError('TELEGRAM_TOKEN not set')
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text,
        'disable_web_page_preview': True
    }
    if TELEGRAM_PARSE_MODE:
        payload['parse_mode'] = TELEGRAM_PARSE_MODE
    resp = requests.post(url, json=payload, timeout=15)
    resp.raise_for_status()
    return resp.status_code, resp.text
>>>>>>> origin/main
