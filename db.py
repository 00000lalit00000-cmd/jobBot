<<<<<<< HEAD
import sqlite3
from datetime import datetime

DB_PATH = 'jobs.db'


def _connect(path=DB_PATH):
    return sqlite3.connect(path)


def init_db(path=DB_PATH):
    conn = _connect(path)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id TEXT PRIMARY KEY,
        title TEXT,
        company TEXT,
        url TEXT,
        posted_at TEXT,
        source TEXT,
        seen_at TEXT
    )
    ''')
    conn.commit()
    conn.close()


def is_seen(job_id, path=DB_PATH):
    conn = _connect(path)
    cur = conn.cursor()
    cur.execute('SELECT 1 FROM jobs WHERE id = ?', (job_id,))
    found = cur.fetchone() is not None
    conn.close()
    return found


def save_job(job, path=DB_PATH):
    conn = _connect(path)
    cur = conn.cursor()
    cur.execute(
        'INSERT OR IGNORE INTO jobs (id, title, company, url, posted_at, source, seen_at) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (
            job.get('id'),
            job.get('title'),
            job.get('company'),
            job.get('url'),
            job.get('posted_at'),
            job.get('source'),
            datetime.utcnow().isoformat(),
        ),
    )
    conn.commit()
    conn.close()
=======
import sqlite3
from datetime import datetime

DB_PATH = 'jobs.db'


def _connect(path=DB_PATH):
    return sqlite3.connect(path)


def init_db(path=DB_PATH):
    conn = _connect(path)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id TEXT PRIMARY KEY,
        title TEXT,
        company TEXT,
        url TEXT,
        posted_at TEXT,
        source TEXT,
        seen_at TEXT
    )
    ''')
    conn.commit()
    conn.close()


def is_seen(job_id, path=DB_PATH):
    conn = _connect(path)
    cur = conn.cursor()
    cur.execute('SELECT 1 FROM jobs WHERE id = ?', (job_id,))
    found = cur.fetchone() is not None
    conn.close()
    return found


def save_job(job, path=DB_PATH):
    conn = _connect(path)
    cur = conn.cursor()
    cur.execute(
        'INSERT OR IGNORE INTO jobs (id, title, company, url, posted_at, source, seen_at) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (
            job.get('id'),
            job.get('title'),
            job.get('company'),
            job.get('url'),
            job.get('posted_at'),
            job.get('source'),
            datetime.utcnow().isoformat(),
        ),
    )
    conn.commit()
    conn.close()
>>>>>>> origin/main
