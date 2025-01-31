import os

TWITTER_CONSUMER_KEY = os.environ.get("API_KEY") or ""
TWITTER_CONSUMER_SECRET = os.environ.get("API_KEY_SECRET") or ""
TWITTER_ACCESS_TOKEN_KEY = os.environ.get("ACCESS_TOKEN_KEY") or ""
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET") or ""

GITHUB_ACCESS_KEY = ""
GITHUB_REPO_URL = "leeyoungseok/twitter-lyric-bot"
GITHUB_ISSUE_ID = 1
TWEET_LENGTH_LIMIT = 140

DEBUG = bool(os.environ.get("LYRIC_BOT_DEBUG") or "TRUE")
