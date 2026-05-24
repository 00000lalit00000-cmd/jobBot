from notifier import broadcast_message
from logger import setup_logging

logger = setup_logging()

def test_notify():
    test_job = {
        'title': 'Python Developer - Remote',
        'company': 'Test Company',
        'location': 'Remote',
        'url': 'https://example.com/job/123',
        'source': 'Test Source'
    }
    
    try:
        message = f"*{test_job['title']}*\nCompany: {test_job['company']}\nLocation: {test_job['location']}\nSource: {test_job['source']}\n{test_job['url']}"
        results = broadcast_message(message)
        if results:
            logger.info('✅ Test notification sent successfully to Telegram! Results: %s', results)
        else:
            logger.error('❌ No test notifications were sent. Please check TELEGRAM_TOKENS and CHAT_IDS in .env')
    except Exception as e:
        logger.error(f'❌ Failed to send test notification: {e}')

if __name__ == '__main__':
    test_notify()
