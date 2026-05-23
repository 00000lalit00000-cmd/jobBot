import os
import tempfile
import unittest
from db import init_db, is_seen, save_job


class TestDb(unittest.TestCase):
    def test_save_and_is_seen(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = os.path.join(tmpdir, 'test_jobs.db')
            init_db(path=db_path)
            job = {
                'id': 'abc123',
                'title': 'Test Engineer',
                'company': 'Example Co',
                'url': 'https://example.com/job/1',
                'posted_at': '2026-01-01T00:00:00Z'
            }
            self.assertFalse(is_seen('abc123', path=db_path))
            save_job(job, path=db_path)
            self.assertTrue(is_seen('abc123', path=db_path))


if __name__ == '__main__':
    unittest.main()
