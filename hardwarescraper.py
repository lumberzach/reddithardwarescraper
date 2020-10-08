import praw
import gspread
from dotenv import load_dotenv
import os
import datetime
import time

# Dotenv
load_dotenv()
clientcreds = os.getenv('client_creds')
secretcreds = os.getenv('secret_creds')


# PRAW
reddit = praw.Reddit(client_id=clientcreds, client_secret=secretcreds, user_agent='hardwareswapscraper')


# Google Spreadsheets auth
scope = ['https://spreadsheets.google.com/feeds']
gc = gspread.service_account(filename='client_secret.json')
sh = gc.open_by_key("1Wch_VKB2Hop_QtRC0_0VLuMxlYSrZ6Ac5CHLHSNa42U")  # ID in URL of sheet
sheet = sh.sheet1


# Setting empty string to append results to
results = []


# Item we are searching for
item = input("What are you searching for?")





# Checking the 10 newest posts and printing any matches for the item
while True:
    new_posts = reddit.subreddit('hardwareswap').new(limit=10)
    for post in new_posts:
        if item in post.title.lower():
            if post.title not in results:
                results.append(post.title)
                row = [datetime.datetime.now().strftime('%m-%d %H:%M'), post.title, post.url]
                index = 1
                sheet.insert_row(row, index)
                print(post.title)
                print(post.url)
                time.sleep(30)


            

