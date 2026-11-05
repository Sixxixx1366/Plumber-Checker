import time
import praw

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
USER_AGENT = "plumber-checker by u/YOUR_USERNAME"

SUBREDDITS = ["philadelphia", "philly"]
KEYWORDS = ["leak", "clogged", "plumber", "plumbing", "burst pipe", "drain"]
MAX_AGE_SECONDS = 60 * 60  # last hour

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
)

now = time.time()

for name in SUBREDDITS:
    for post in reddit.subreddit(name).new(limit=100):
        if now - post.created_utc > MAX_AGE_SECONDS:
            continue
        text = (post.title + " " + post.selftext).lower()
        if any(word in text for word in KEYWORDS):
            print(post.title)
            print("https://reddit.com" + post.permalink)
            print()
            time.sleep(2)  # be polite to Reddit's rate limit