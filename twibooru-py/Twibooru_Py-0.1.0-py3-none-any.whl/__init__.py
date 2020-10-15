# -*- coding: utf-8 -*-

"""
Twibooru API bindings
~~~~~~~~~~~~~~~~~~~~~~~

Python bindings for Twibooru's API

Typical usage:

>>> from twibooru import Search, sort
>>> for image in Search().sort_by(sort.SCORE):
...   print(image.url)

Full API Documentation is found at <https://twibooru.org/pages/api>.

Library documentation is found at <https://github.com/Atronar/Twibooru-Py

"""

__title__ = "Twibooru-Py"
__version__ = "0.1.0"
__author__ = "Joshua Stone"
__license__ = "Simplified BSD Licence"
__copyright__ = "Copyright (c) 2014, Joshua Stone; 2020, ATroN"

from .search import Search, Related
from .image import Image
from .post_image import PostImage
from .tags import Tags
from .tag import Tag
from .profile import Profile
from .filters import Filters, Filter
from .galleries import Galleries
from .gallery import Gallery
from .posts import SearchPosts
from .post import Post
from .forums import Topics, Topic, Posts
from .query import query
from .sort import sort
from .user import user

__all__ = [
  "Search", "Related",
  "Image",
  "PostImage",
  "Tags",
  "Tag",
  "Profile",
  "Filters", "Filter",
  "Galleries",
  "Gallery",
  "SearchPosts",
  "Post",
  "Topics", "Topic", "Posts",
  "query",
  "sort",
  "user"
]
