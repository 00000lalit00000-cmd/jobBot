from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time
import os

from dotenv import load_dotenv
load_dotenv()

from db import init_db

def start_scheduler(job_fn, interval_minutes=15):
    init_db()
    scheduler = BackgroundScheduler()
    scheduler.add_job(job_fn, IntervalTrigger(minutes=interval_minutes))
    scheduler.start()
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
