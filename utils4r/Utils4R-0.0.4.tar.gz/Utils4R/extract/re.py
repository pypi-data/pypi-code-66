import re


def get(regex: str, string, default=None):
    """使用正则表达式提取数据"""
    if string:
        if pattern := re.search(regex, string):
            return pattern.group()
    return default
