import unittest
from unittest.mock import patch, Mock
from scrapers.rss_scraper import fetch_rss_jobs


class TestRssScraper(unittest.TestCase):
    @patch('scrapers.rss_scraper.requests.get')
    def test_fetch_rss_jobs(self, mock_get):
        xml = '''<?xml version="1.0" encoding="UTF-8"?>
        <rss><channel>
            <item>
                <title>Python Developer</title>
                <link>https://example.com/jobs/1</link>
                <pubDate>Fri, 23 May 2026 12:00:00 GMT</pubDate>
            </item>
        </channel></rss>'''
        response = Mock()
        response.content = xml.encode('utf-8')
        response.raise_for_status = Mock()
        mock_get.return_value = response

        jobs = fetch_rss_jobs('https://example.com/feed')
        self.assertEqual(len(jobs), 1)
        self.assertEqual(jobs[0]['title'], 'Python Developer')
        self.assertEqual(jobs[0]['url'], 'https://example.com/jobs/1')
        self.assertTrue(jobs[0]['id'])


if __name__ == '__main__':
    unittest.main()
