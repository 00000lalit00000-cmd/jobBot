import os
import unittest
from unittest.mock import patch
import notifier


class TestNotifier(unittest.TestCase):
    @patch('notifier.requests.post')
    def test_send_message(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = 'OK'
        with patch.dict(os.environ, {'TELEGRAM_TOKEN': 'fake-token'}):
            import importlib
            importlib.reload(notifier)
            status, text = notifier.send_message('1234', 'Hello')
            self.assertEqual(status, 200)
            self.assertEqual(text, 'OK')
            mock_post.assert_called_once()


if __name__ == '__main__':
    unittest.main()
