import requests
from bs4 import BeautifulSoup
import hashlib
from datetime import datetime


def _make_id(title, url):
    return hashlib.sha1(f"{title}|{url}".encode('utf-8')).hexdigest()


def _make_soup(content):
    try:
        return BeautifulSoup(content, 'xml')
    except Exception:
        return BeautifulSoup(content, 'html.parser')


def fetch_rss_jobs(rss_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/rss+xml, application/xml, text/xml, */*'
    }
    resp = requests.get(rss_url, headers=headers, timeout=15)
    resp.raise_for_status()
    content_type = resp.headers.get('Content-Type', '')

    if 'application/json' in content_type or rss_url.endswith('.json'):
        data = resp.json()
        return _parse_json_feed(data, rss_url)

    soup = _make_soup(resp.content)
    items = []
    for item in soup.find_all('item')[:10]:
        title = item.title.text.strip() if item.title else ''
        link = item.link.text.strip() if item.link else ''
        pub = item.pubDate.text.strip() if item.pubDate else ''
        company = item.company.text.strip() if item.company else ''
        location = item.location.text.strip() if item.location else ''
        job = {
            'id': _make_id(title, link),
            'title': title,
            'company': company,
            'location': location,
            'url': link,
            'posted_at': pub,
            'source': rss_url
        }
        items.append(job)
    return items


def _parse_json_feed(data, rss_url):
    items = []
    if isinstance(data, dict):
        entries = data.get('jobs') or data.get('items') or []
    else:
        entries = data

    for entry in entries[:10]:
        title = entry.get('title') or entry.get('position') or entry.get('company') or ''
        link = entry.get('url') or entry.get('link') or entry.get('apply_url') or ''
        pub = entry.get('date') or entry.get('created_at') or ''
        company = entry.get('company') or ''
        job = {
            'id': _make_id(title, link),
            'title': title,
            'company': company,
            'location': entry.get('location', ''),
            'url': link,
            'posted_at': pub,
            'source': rss_url
        }
        if link:
            items.append(job)
    return items
