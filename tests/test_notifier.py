import os
import unittest
from unittest.mock import patch
import notifier


class TestNotifier(unittest.TestCase):
    def test_send_message(self):
        with patch('notifier.requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.text = 'OK'
            with patch.dict(os.environ, {'TELEGRAM_TOKEN': 'fake-token'}):
                import importlib
                importlib.reload(notifier)
                status, text = notifier.send_message('1234', 'Hello')
                self.assertEqual(status, 200)
                self.assertEqual(text, 'OK')
                mock_post.assert_called_once()

    def test_send_message_fallbacks_to_plain_text_on_parse_error(self):
        error_resp = unittest.mock.Mock()
        error_resp.status_code = 400
        error_resp.json.return_value = {'description': "Bad Request: can't parse entities"}
        error_resp.text = 'Bad Request'

        success_resp = unittest.mock.Mock()
        success_resp.status_code = 200
        success_resp.text = 'OK'

        with patch.dict(os.environ, {'TELEGRAM_TOKEN': 'fake-token', 'TELEGRAM_PARSE_MODE': 'Markdown'}):
            import importlib
            import config
            with patch('notifier.requests.post') as mock_post:
                mock_post.side_effect = [error_resp, success_resp]
                importlib.reload(config)
                importlib.reload(notifier)
                status, text = notifier.send_message('1234', 'Hello')
                self.assertEqual(status, 200)
                self.assertEqual(text, 'OK')
                self.assertEqual(mock_post.call_count, 2)


if __name__ == '__main__':
    unittest.main()
