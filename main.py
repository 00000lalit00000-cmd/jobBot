import logging
from config import CHAT_ID, RSS_URLS, INSTAGRAM_ACCOUNTS, COMPANY_CAREER_PAGES, JOB_KEYWORDS, DATABASE_URL
from logger import setup_logging
from db import init_db, is_seen, save_job
from notifier import send_message
from scrapers.rss_scraper import fetch_rss_jobs
from scrapers.insta_scraper import fetch_latest_posts
from scrapers.career_page_scraper import fetch_company_jobs

logger = setup_logging()


def _escape_text(text):
    if not text:
        return ''
    return text.replace('_', '\\_').replace('*', '\\*').replace('[', '\\[').replace(']', '\\]')


def format_job_message(job):
    lines = []
    title = job.get('title') or 'New job'
    lines.append(f'*{_escape_text(title)}*')
    if job.get('company'):
        lines.append(f'Company: {_escape_text(job.get("company"))}')
    if job.get('location'):
        lines.append(f'Location: {_escape_text(job.get("location"))}')
    if job.get('source'):
        lines.append(f'Source: {_escape_text(job.get("source"))}')
    if job.get('url'):
        lines.append(job.get('url'))
    return '\n'.join(lines)


def job_matches(job):
    if not JOB_KEYWORDS:
        return True
    text = ' '.join(filter(None, [job.get('title', ''), job.get('company', ''), job.get('text', '')])).lower()
    return any(keyword.lower() in text for keyword in JOB_KEYWORDS)


def _process_items(items):
    sent = 0
    for job in items:
        if not job.get('id') or not job.get('url'):
            continue
        if not job_matches(job):
            logger.debug('Job filtered out by keywords: %s', job.get('title'))
            continue
        if is_seen(job['id'], path=DATABASE_URL):
            logger.debug('Skipping already seen job: %s', job.get('id'))
            continue
        try:
            message = format_job_message(job)
            send_message(CHAT_ID, message)
            save_job(job, path=DATABASE_URL)
            sent += 1
            logger.info('Sent notification for %s', job.get('id'))
        except Exception as exc:
            logger.exception('Failed to notify job %s: %s', job.get('id'), exc)
    return sent


def run_once():
    init_db(path=DATABASE_URL)
    if not CHAT_ID:
        logger.error('CHAT_ID not set; set it in .env to receive messages')
        return
    if not RSS_URLS and not INSTAGRAM_ACCOUNTS and not COMPANY_CAREER_PAGES:
        logger.error('No RSS_URLS, INSTAGRAM_ACCOUNTS, or COMPANY_CAREER_PAGES configured; set them in .env')
        return

    total_sent = 0
    for rss_url in RSS_URLS:
        try:
            items = fetch_rss_jobs(rss_url)
            logger.info('Fetched %d items from RSS %s', len(items), rss_url)
            total_sent += _process_items(items)
        except Exception as exc:
            logger.exception('Failed to fetch RSS feed %s: %s', rss_url, exc)

    for username in INSTAGRAM_ACCOUNTS:
        try:
            items = fetch_latest_posts(username)
            logger.info('Fetched %d Instagram posts from %s', len(items), username)
            total_sent += _process_items(items)
        except Exception as exc:
            logger.exception('Failed to fetch Instagram posts for %s: %s', username, exc)

    for career_url in COMPANY_CAREER_PAGES:
        try:
            items = fetch_company_jobs(career_url)
            logger.info('Fetched %d jobs from company career page %s', len(items), career_url)
            total_sent += _process_items(items)
        except Exception as exc:
            logger.exception('Failed to fetch company career page %s: %s', career_url, exc)

    logger.info('run_once finished, notifications sent: %d', total_sent)


if __name__ == '__main__':
    run_once()
