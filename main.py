import praw
from decouple import config

client_id = config('client_id')
client_secret = config('client_secret')
user_agent = config('user_agent')

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
praw==7.1.0