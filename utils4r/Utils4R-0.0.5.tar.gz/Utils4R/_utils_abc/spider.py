from abc import ABCMeta
from abc import abstractmethod


class SingleSpider(metaclass=ABCMeta):
    """简单单线程爬虫的抽象基类"""

    @abstractmethod
    def run(self, name):
        """执行爬虫"""
