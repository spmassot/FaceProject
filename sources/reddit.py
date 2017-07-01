import praw
from collections import namedtuple
from os import environ as env


def get_client():
    """Returns praw.Reddit client"""
    return praw.Reddit(
        client_id=env['reddit_client_id'],
        client_secret=env['reddit_client_secret'],
        user_agent=env['reddit_user_agent']
    )

def get_subr_top(sub_name, n):
    """Returns the top n submissions from r/sub_name"""
    return get_client().subreddit(sub_name).top(limit=n)

def get_comment_props(comment_in):
    """Expects a praw CommentForest object, returns a named tuple"""
    Comment = namedtuple('Comment', ['id','content','children'])
    return Comment(
        comment_in.id,
        comment_in.body,
        [cmnt.id for cmnt in comment_in.replies]
    )

if __name__ == '__main__':
    from pandas import DataFrame
    for submission in get_subr_top('crappydesign', 1):
        submission.comments.replace_more()
        comms = [get_comment_props(x) for x in submission.comments.list()]
        frame = DataFrame(comms)
    frame.to_csv('test_data.csv')
