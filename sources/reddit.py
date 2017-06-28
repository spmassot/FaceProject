import praw
from os import environ as env

reddit = praw.Reddit(
    client_id=env['reddit_client_id'],
    client_secret=env['reddit_client_secret'],
    user_agent=env['reddit_user_agent']
)

if __name__ == '__main__':
    for submission in reddit.subreddit('learnpython').hot(limit=10):
        print(submission.title)
