Implement Instagram monitor

Goal: Monitor Instagram accounts for job posts; prefer Graph API, fallback to `instaloader` when necessary.

Inputs:
- List of Instagram accounts or business account credentials

Outputs:
- `insta_monitor.py` that returns recent posts with captions and media links
- Acceptance criteria: Able to detect new posts and extract caption text

Steps:
1. If using Graph API, outline required Facebook App permissions and token retrieval.
2. If using `instaloader`, implement account-post fetching with rate limiting.

Notes: Using scraping tools may violate Instagram terms; prefer API.
