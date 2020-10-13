import praw
import gspread
from dotenv import load_dotenv
import os
import datetime
import time
from twilio.rest import Client


load_dotenv()


# PRAW
clientcreds = os.getenv('client_creds')
secretcreds = os.getenv('secret_creds')
reddit = praw.Reddit(client_id=clientcreds, client_secret=secretcreds, user_agent='hardwareswapscraper')


# Twilio
account_sid = os.getenv('sid')
auth_token = os.getenv('token')
client = Client(account_sid, auth_token)


# Google Spreadsheets auth
scope = ['https://spreadsheets.google.com/feeds']
gc = gspread.service_account(filename='client_secret.json')
sh = gc.open_by_key("1Wch_VKB2Hop_QtRC0_0VLuMxlYSrZ6Ac5CHLHSNa42U")  # ID in URL of sheet
sheet = sh.sheet1


# Send SMS with url to post once item is found
def sms_alert():
    client.messages.create(
        to=number,
        from_="+12566678863",
        body=post.url)


# Setting empty string to append results to
results = []


# Item(s) we are searching for
search_items = []


# Find out how many items we are searching for and add them to a list.
num = int(input("How many items are you searching for?"))
count = 1
for i in range(num):
    search_items.append(input(f"Enter item # {count}: "))
    print(search_items)
    count += 1


# Phone number to send sms alert to
number = int(input("Enter your phone number: "))


# Loop checking the 10 newest posts on specified subreddit
while True:
    new_posts = reddit.subreddit('hardwareswap').new(limit=10)
    for post in new_posts:
        match = any(item in post.title.lower() for item in search_items)
        if match and post.title not in results:
            results.append(post.title)
            row = [datetime.datetime.now().strftime('%m-%d %H:%M'), post.title, post.url]
            index = 1
            sheet.insert_row(row, index)
            # sms_alert()
            print(post.title)
            print(post.url)
