import praw

reddit = praw.Reddit(client_id='P3FtIvElljRLtg', client_secret='QQ18Nf-O9q8VWmqAR-pEhpThPr8', user_agent='hardwareswapscraper')


# while True:
new_posts = reddit.subreddit('hardwareswap').new(limit=10)
item = "asus"
results = []
for post in new_posts:
    # print(post.title)
    if item in post.title.lower():
        if post.title.lower() not in results:
            results.append(post.title)
            print(results[-1])
            

