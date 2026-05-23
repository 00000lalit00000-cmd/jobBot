from config import CHAT_ID
from notifier import send_message
from logger import setup_logging

logger = setup_logging()

def test_notify():
    if not CHAT_ID:
        logger.error('CHAT_ID not set in .env')
        return
    
    test_job = {
        'title': 'Python Developer - Remote',
        'company': 'Test Company',
        'location': 'Remote',
        'url': 'https://example.com/job/123',
        'source': 'Test Source'
    }
    
    try:
        message = f"*{test_job['title']}*\nCompany: {test_job['company']}\nLocation: {test_job['location']}\nSource: {test_job['source']}\n{test_job['url']}"
        send_message(CHAT_ID, message)
        logger.info('✅ Test notification sent successfully to Telegram!')
    except Exception as e:
        logger.error(f'❌ Failed to send test notification: {e}')

if __name__ == '__main__':
    test_notify()
