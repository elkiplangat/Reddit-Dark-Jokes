import praw
from decouple import config
import os

client_id = config('client_id')
client_secret = config('client_secret')
user_agent = config('user_agent')


reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

new_posts = reddit.subreddit('darkjokes').new(limit=200)
for post in new_posts:
    formated_string = f'"{post.title} {post.selftext}"\n -- {post.author}\n.\n'
    print(formated_string)


'''
Uncomment this block of code if you have variety installed in your computer and would like to fetch the
jokes and add them as variety quotes on your desktop.
Variety fetches user defined quotes from the file home/username/.config/variety/pluginconfig/quotes/quotes.txt
'''
# username = os.getlogin()
#
# with open(f'/home/{username}/.config/variety/pluginconfig/quotes/quotes.txt', 'w') as fp:
#     for post in new_posts:
#
#         formated_string = f'"{post.title} {post.selftext}"\n -- {post.author}\n.\n'
#
#         fp.write(formated_string)





