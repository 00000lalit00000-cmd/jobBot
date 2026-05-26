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
