import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

from config import SCHEDULE_CRON, SCRAPE_INTERVAL_MINUTES
from logger import setup_logging
from main import run_once

logger = setup_logging()


def start_service():
    logger.info('Starting jobBot scheduler (cron: %s) - cron trigger commented, using interval trigger', SCHEDULE_CRON)
    scheduler = BackgroundScheduler()
    # Cron trigger (daily at configured time) - commented out by default
    # scheduler.add_job(run_once, CronTrigger.from_crontab(SCHEDULE_CRON), id='job_scrape_cron', replace_existing=True)

    # Interval trigger (every N minutes) - active by default. Controlled via SCRAPE_INTERVAL_MINUTES in .env
    scheduler.add_job(run_once, IntervalTrigger(minutes=SCRAPE_INTERVAL_MINUTES), id='job_scrape_interval', replace_existing=True)
    scheduler.start()
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        logger.info('Shutting down jobBot scheduler')
        scheduler.shutdown()


if __name__ == '__main__':
    start_service()
