import os
import sys

import praw
from decouple import config

client_id = config('client_id')
client_secret = config('client_secret')
user_agent = config('user_agent')

args = sys.argv

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

new_posts = reddit.subreddit('darkjokes').new(limit=200)
if len(args) > 1: #checks whether user added a command line argument while running the script.
    variety_selected = bool(args[1])
    '''
    add a command line argument if you have variety installed in your computer and would like to fetch the
    jokes and add them as variety quotes on your desktop.
    Variety fetches user defined quotes from the file home/username/.config/variety/pluginconfig/quotes/quotes.txt
    '''
    if variety_selected:
        username = os.getlogin()

        with open(f'/home/{username}/.config/variety/pluginconfig/quotes/quotes.txt', 'w') as fp:
            for post in new_posts:
                formatted_string = f'"{post.title} {post.selftext}"\n -- {post.author}\n.\n'

                fp.write(formatted_string)
        print("Successfully written jokes to variety quotes file.")
else:
    for post in new_posts:
        formatted_string = f'"{post.title} {post.selftext}"\n -- {post.author}\n.\n'
        print(formatted_string)
