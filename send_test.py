import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT = os.getenv("CHAT_ID")

def send_test():
    if not TOKEN or not CHAT:
        print("Missing TELEGRAM_TOKEN or CHAT_ID in environment")
        return
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    resp = requests.post(url, json={"chat_id": CHAT, "text": "Hello from jobBot — test message"})
    print(resp.status_code, resp.text)

if __name__ == '__main__':
    send_test()
