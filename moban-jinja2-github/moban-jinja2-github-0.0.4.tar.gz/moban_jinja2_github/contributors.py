from gease.exceptions import UrlNotFound
from gease.contributors import EndPoint


def get_contributors(user, repo, exclude_contributors=()):
    repo = EndPoint(user, repo)
    try:
        user_list = repo.get_all_contributors()
        user_list = [
            detail
            for detail in user_list
            if "login" in detail
            and detail["login"] not in exclude_contributors
        ]
        return user_list
    except UrlNotFound:
        return []
