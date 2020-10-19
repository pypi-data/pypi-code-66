"""
Channeling - a Discord bot.
"""
__version__ = "0.0.13"
__license__ = "BSD"
__year__ = "2020"
__author__ = "Predrag Mandic"
__author_email__ = "predrag@nul.one"
__copyright__ = "Copyright {} {} <{}>".format(
    __year__, __author__, __author_email__)


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

class ChannelingException(Exception):
    "Generic channeling exception."
    pass

