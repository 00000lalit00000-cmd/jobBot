import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from config import SCHEDULE_CRON
from logger import setup_logging
from main import run_once

logger = setup_logging()


def start_service():
    logger.info('Starting jobBot scheduler with cron: %s', SCHEDULE_CRON)
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_once, CronTrigger.from_crontab(SCHEDULE_CRON), id='job_scrape', replace_existing=True)
    scheduler.start()
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        logger.info('Shutting down jobBot scheduler')
        scheduler.shutdown()


if __name__ == '__main__':
    start_service()
