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
    resp = requests.get(rss_url, timeout=10)
    resp.raise_for_status()
    soup = _make_soup(resp.content)
    items = []
    for item in soup.find_all('item')[:10]:
        title = item.title.text if item.title else ''
        link = item.link.text if item.link else ''
        pub = item.pubDate.text if item.pubDate else ''
        job = {
            'id': _make_id(title, link),
            'title': title,
            'company': '',
            'location': '',
            'url': link,
            'posted_at': pub,
            'source': rss_url
        }
        items.append(job)
    return items
