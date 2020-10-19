import requests
import random
from memelib.errors import *

class DankMemeClient:
    def __init__(self, use_reddit_for_memes: bool = True):
        self.memes = {
            "random":"meme()"
        }
        self.meme_subreddits = [
            "/dankmemes",
            "/memes",
            "/wholesomememes"
        ]
        self.usereddit = use_reddit_for_memes
    def meme(self, subreddit = None):
        if self.usereddit and subreddit:
            r = requests.request("GET", f"https://reddit.com/r/{subreddit}/random.json")
            return r
        elif self.usereddit and not subreddit:
            subreddit = random.choice(self.meme_subreddits)
            r = requests.request("GET", f"https://reddit.com/r/{subreddit}/random.json")
        elif not self.usereddit:
            return("Still in progress")
            raise SubredditNotFoundError("You didn't specify a subreddit")