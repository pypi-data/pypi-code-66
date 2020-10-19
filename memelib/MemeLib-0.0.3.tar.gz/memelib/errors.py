class MemeLibExeception(Exception):
    """MemeLib's base exception"""
    pass
class RedditApiError(MemeLibExeception):
    """An error occured when getting data from Reddit"""
    pass
class SubredditNotFoundError(RedditApiError):
    """That subreddit wasn't found"""
    pass