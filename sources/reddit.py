import praw
from collections import namedtuple
from os import environ as env
from pandas import DataFrame


def get_client():
    """Returns praw.Reddit client"""
    return praw.Reddit(
        client_id=env['reddit_client_id'],
        client_secret=env['reddit_client_secret'],
        user_agent=env['reddit_user_agent']
    )

def get_subr_top(sub_name, n=None):
    """Returns the top n submissions from r/sub_name"""
    if n:
        return get_client().subreddit(sub_name).top(limit=n)
    else:
        return get_client().subreddit(sub_name).top()

def get_comment_props(comment_in):
    """Expects a praw CommentForest object, returns a named tuple"""
    Comment = namedtuple('Comment', ['id','content','children'])
    return Comment(
        comment_in.id,
        comment_in.body,
        [cmnt.id for cmnt in comment_in.replies]
    )

def main(sub, limt=None):
    """Grabs top submissions from a subreddit,
    returns their comments as a dataframe"""
    for submission in get_subr_top(sub, n=limt):
        submission.comments.replace_more(limit=0)
        comms = [get_comment_props(x) for x in submission.comments.list()]
        frame = DataFrame(comms)
    return frame
    
if __name__ == '__main__':
    main('crappydesign',10).to_csv('test_data.csv')
