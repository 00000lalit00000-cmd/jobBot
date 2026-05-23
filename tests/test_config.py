import os
import unittest
import importlib
from unittest.mock import patch


class TestConfig(unittest.TestCase):
    def test_env_parsing(self):
        env = {
            'TELEGRAM_TOKEN': 'abc',
            'CHAT_ID': '123',
            'RSS_URLS': 'https://example.com/feed, https://another.com/feed',
            'INSTAGRAM_ACCOUNTS': 'acct1, acct2',
            'JOB_KEYWORDS': 'python, remote',
            'SCRAPE_INTERVAL_MINUTES': '10',
            'LOG_LEVEL': 'DEBUG'
        }
        with patch.dict(os.environ, env, clear=False):
            import config
            importlib.reload(config)
            self.assertEqual(config.TELEGRAM_TOKEN, 'abc')
            self.assertEqual(config.CHAT_ID, '123')
            self.assertEqual(config.RSS_URLS, ['https://example.com/feed', 'https://another.com/feed'])
            self.assertEqual(config.INSTAGRAM_ACCOUNTS, ['acct1', 'acct2'])
            self.assertEqual(config.SCRAPE_INTERVAL_MINUTES, 10)
            self.assertEqual(config.LOG_LEVEL, 'DEBUG')


if __name__ == '__main__':
    unittest.main()
