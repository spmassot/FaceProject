import basc_py4chan
from pandas import DataFrame

def get_board(board):
    return [
        get_thread(x) for x in basc_py4chan.Board(board).get_threads()
    ]
    for thread in threads:
        posts = thread.all_posts
        for post in posts:
            print(post.post_id)
            print(post.text_comment)

def get_thread(thread):
    return [
        get_post(x) for x in thread.all_posts
    ]
    

def get_post(post):
    return (post.post_id,post.text_comment)

if __name__ == '__main__':
    get_board('b')
