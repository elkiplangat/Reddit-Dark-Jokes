import ctypes
import os
import random
import sys
import textwrap
import time

import praw
import schedule
from PIL import Image, ImageFont, ImageDraw
from decouple import config

client_id = config('client_id')
client_secret = config('client_secret')
user_agent = config('user_agent')

args = sys.argv
sorted_lines = []


def fetch_jokes():
    global new_posts
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    new_posts = reddit.subreddit('darkjokes').new(limit=2000)


# fetch_jokes()


def print_jokes():
    for post in new_posts:
        formatted_string = f'"{post.title} {post.selftext}"\n -- {post.author}\n.\n'
        print(formatted_string)


def write_jokes_to_txt():
    with open(f'quotes.txt', 'w') as fp:
        for post in new_posts:
            formatted_string = f'"{post.title} {post.selftext}"\n -- {post.author}\n.\n'

            fp.write(formatted_string)


def clear_sorted_jokes_array():
    global sorted_lines
    sorted_lines = []


def select_random_joke():
    global sorted_lines

    if not sorted_lines:
        print("sorted_lines is empty")
        with open('quotes.txt', 'r') as fp:
            lines = fp.readlines()
            selected_line = ''
            count = 0
            for line in lines:
                if line == '.\n':
                    count += 1
                    sorted_lines.append(selected_line)
                    selected_line = ''
                    continue
                else:
                    selected_line += line

    elif len(sorted_lines) > 0:
        print("sorted lines is not empty")
        pass

    return sorted_lines[random.randint(0, len(sorted_lines))]


def add_joke_text_to_image():
    #
    image = Image.open('images/image1.jpg')
    font = ImageFont.truetype('fonts/Montserrat-Bold.ttf', 30)
    image_width, image_height = image.size
    print(f'image width: {image_width}')
    print(f'image height: {image_height}')
    text_location = (image_width * 0.05, image_height * 0.3)
    joke_text = select_random_joke()
    wrapped = textwrap.wrap(joke_text, width=50)
    wrapped_text = "\n".join(wrapped)

    print(wrapped_text)
    image_editable = ImageDraw.Draw(image)
    image_editable.text(text_location, wrapped_text, (237, 230, 211), font=font)
    image.save('wallpaper.jpg')


def change_wallpaper_for_windows():
    PATH = os.path.abspath() + '\wallpaper.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20, 0, PATH, 3)


def write_jokes_to_variety_txt():
    username = os.getlogin()
    print("Sjokes to variety quotes file.")
    with open(f'/home/{username}/.config/variety/pluginconfig/quotes/quotes.txt', 'w') as fp:
        for post in new_posts:
            formatted_string = f'"{post.title} {post.selftext}"\n -- {post.author}\n.\n'
            fp.write(formatted_string)
    print("Successfully written jokes to variety quotes file.")


if os.name == 'posix':
    if len(args) > 1:
        pass  # checks whether user added a command line argument while running the script.
        # variety_selected = bool(args[1])
        # '''
        # add a command line argument if you have variety installed in your computer and would like to fetch the
        # jokes and add them as variety quotes on your desktop.
        # Variety fetches user defined quotes from the file home/username/.config/variety/pluginconfig/quotes/quotes.txt
        # '''
        # if variety_selected:
        #     username = os.getlogin()
        #
        #     with open(f'/home/{username}/.config/variety/pluginconfig/quotes/quotes.txt', 'w') as fp:
        #         for post in new_posts:
        #             formatted_string = f'"{post.title} {post.selftext}"\n -- {post.author}\n.\n'
        #
        #             fp.write(formatted_string)
        #     print("Successfully written jokes to variety quotes file.")
    else:

        schedule.every(60).minutes.do(clear_sorted_jokes_array)
        schedule.every(60).minutes.do(fetch_jokes)
        schedule.every(60).minutes.do(write_jokes_to_variety_txt)
        schedule.every(1).minutes.do(add_joke_text_to_image)

        while True:
            schedule.run_pending()
            time.sleep(1)

elif os.name == 'nt':
    print("Looks like you're on windows... ")
    schedule.every(60).minutes.do(clear_sorted_jokes_array)
    schedule.every(60).minutes.do(fetch_jokes)
    schedule.every(60).minutes.do(write_jokes_to_txt)
    schedule.every(2).minutes.do(add_joke_text_to_image)
    schedule.every(2).minutes.do(change_wallpaper_for_windows())

    while True:
        schedule.run_pending()
        time.sleep(1)
