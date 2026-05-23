Add config, logging & tests

Goal: Add configuration handling, structured logging, and basic tests for core modules.

Inputs:
- Existing modules and `.env.example`

Outputs:
- `config.py` to load env vars, `logging` configured, and a `tests/` folder with unit tests
- Acceptance criteria: Tests run locally and config loads from `.env`

Steps:
1. Use `python-dotenv` to load `.env` for local development.
2. Configure `logging` with `logging.basicConfig` and a file handler.
3. Add unit tests for `notifier` and `db`.
