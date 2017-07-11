import re
import basc_py4chan
from pandas import DataFrame

def get_board(board):
    return [
        get_thread(x) for x in basc_py4chan.Board(board).get_threads()
    ]

def get_thread(thread):
    return [
        get_post(x) for x in thread.all_posts
    ]

def get_post(post):
    reply = re.compile('>>\d+')
    txt = post.text_comment.strip().replace('\n', ' ')
    if not txt:
        return None
    
        return (post.post_id,post.text_comment.strip().replace('\n',''),)

if __name__ == '__main__':
    print(get_board('b'))
