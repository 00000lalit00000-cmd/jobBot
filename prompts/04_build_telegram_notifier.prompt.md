Build Telegram notifier

Goal: Implement a small module that sends messages to your Telegram bot using token from environment.

Inputs:
- `TELEGRAM_TOKEN` and `CHAT_ID` environment variables

Outputs:
- `notifier.py` with `send_message(text)` function
- Acceptance criteria: `send_test.py` uses `notifier.send_message` successfully

Steps:
1. Create `notifier.py` with a minimal HTTP wrapper around `sendMessage`.
2. Add `send_test.py` to call it.
