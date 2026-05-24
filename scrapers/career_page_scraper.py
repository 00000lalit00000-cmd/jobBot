import hashlib
import re
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

JOB_TITLE_KEYWORDS = re.compile(
    r'\b(engineer|developer|manager|analyst|designer|scientist|architect|consultant|specialist|programmer|product|security|data|software|devops|qa|quality|frontend|backend|fullstack|mobile|cloud|machine learning|ml|sre|site reliability|support)\b',
    re.I,
)
GENERIC_TITLE_BLACKLIST = re.compile(
    r'\b(careers?|jobs?|home|about|blog|locations?|contact|faq|help|sign in|newsletter|apply now|learn more|opportunities|opportunity|team|culture|life at|our values|events?)\b',
    re.I,
)
CANDIDATE_PAGE_PATTERN = re.compile(r'(jobs?|careers?|positions|roles|openings|opportunities|apply|search)', re.I)
EXTERNAL_BOARD_PATTERN = re.compile(
    r'(greenhouse\.io|lever\.co|workable\.com|smartrecruiters\.com|jobvite\.com|icims\.com|breezy\.hr|recruitee\.com|google\.com/careers|amazon\.jobs|microsoft\.com/en-us/careers|apple\.com/careers|linkedin\.com/careers)',
    re.I,
)


def _make_id(url):
    return hashlib.sha1(url.encode('utf-8')).hexdigest()


def _normalize_url(base_url, href):
    if not href:
        return ''
    return urljoin(base_url, href.strip())


def _looks_like_job_title(text):
    if not text:
        return False
    return bool(JOB_TITLE_KEYWORDS.search(text))


def _looks_generic_title(text):
    if not text:
        return False
    return bool(GENERIC_TITLE_BLACKLIST.search(text))


def _looks_like_job_page(url):
    if not url:
        return False
    return bool(CANDIDATE_PAGE_PATTERN.search(url)) or bool(EXTERNAL_BOARD_PATTERN.search(url))


def _fetch_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    return BeautifulSoup(resp.content, 'html.parser')


def _dedupe_jobs(jobs):
    seen = set()
    deduped = []
    for job in jobs:
        if job['id'] in seen:
            continue
        seen.add(job['id'])
        deduped.append(job)
    return deduped


def fetch_company_jobs(career_page_url, depth=0, visited=None):
    if visited is None:
        visited = set()
    if career_page_url in visited or depth > 1:
        return []
    visited.add(career_page_url)

    jobs = []
    candidate_pages = []
    try:
        soup = _fetch_soup(career_page_url)
        for link in soup.find_all('a', href=True):
            href = link.get('href').strip()
            if not href or href.startswith('#') or href.lower().startswith('javascript:'):
                continue

            job_url = _normalize_url(career_page_url, href)
            title = link.get_text(' ', strip=True)
            if not title:
                continue

            if _looks_like_job_title(title) and not _looks_generic_title(title):
                jobs.append({
                    'id': _make_id(job_url),
                    'title': title[:100],
                    'company': urlparse(career_page_url).netloc,
                    'url': job_url,
                    'posted_at': '',
                    'source': f'Career Page: {career_page_url}',
                    'location': '',
                })
            elif _looks_like_job_page(job_url) and not _looks_generic_title(title):
                candidate_pages.append(job_url)

        jobs = _dedupe_jobs(jobs)

        if jobs:
            return jobs

        for page_url in candidate_pages[:5]:
            jobs.extend(fetch_company_jobs(page_url, depth=depth + 1, visited=visited))

    except Exception:
        return []

    return _dedupe_jobs(jobs)
