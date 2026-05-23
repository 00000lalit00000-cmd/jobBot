import requests
from bs4 import BeautifulSoup
import hashlib
import re


def _make_id(url):
    return hashlib.sha1(url.encode('utf-8')).hexdigest()


def fetch_company_jobs(career_page_url):
    """
    Generic scraper for company career pages.
    Looks for job listings and links on the page.
    """
    jobs = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        resp = requests.get(career_page_url, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, 'html.parser')

        # Look for job listings by common patterns
        job_links = soup.find_all('a', href=re.compile(r'(job|career|position|opening)', re.I))

        for link in job_links[:10]:
            title = link.get_text(strip=True)
            href = link.get('href')

            if not title or not href:
                continue

            # Make absolute URL
            if href.startswith('http'):
                job_url = href
            else:
                base = '/'.join(career_page_url.split('/')[:3])
                job_url = base + href if href.startswith('/') else career_page_url.rstrip('/') + '/' + href

            job = {
                'id': _make_id(job_url),
                'title': title[:100],
                'company': career_page_url.split('//')[1].split('/')[0],
                'url': job_url,
                'posted_at': '',
                'source': f'Career Page: {career_page_url}',
                'location': '',
            }
            if job not in jobs:
                jobs.append(job)

    except Exception as e:
        pass

    return jobs
