Test end-to-end & deploy

Goal: Verify end-to-end flow and prepare a simple deployment (Docker/VPS).

Inputs:
- All modules implemented and tested locally

Outputs:
- `Dockerfile`, simple deployment instructions, and an end-to-end test plan
- Acceptance criteria: App runs in Docker and sends at least one test notification

Steps:
1. Create a minimal `Dockerfile` and `docker-compose.yml` if needed.
2. Document environment variables and how to run the container.
3. Run end-to-end test: start container, simulate a new job, verify Telegram message.
