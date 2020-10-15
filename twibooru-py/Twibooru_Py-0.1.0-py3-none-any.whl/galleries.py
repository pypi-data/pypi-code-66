# -*- coding: utf-8 -*-

# Copyright (c) 2014, Joshua Stone
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from .request import get_galleries, url_galleries
from .gallery import Gallery
from .helpers import api_key, join_params, set_limit, sort_format_galleries

__all__ = [
  "Galleries"
]

class Galleries(object):
  """
  All properties are read-only, and every method returns a new instance of
  Galleries() to avoid mutating state in ongoing search queries. This makes object
  interactions predictable as well as making versioning of searches relatively
  easy.
  """
  def __init__(self, title="", description="", include_image=None,
               sf="created_at", sd="desc", user="",
               key="", limit=50, perpage=25, page=1,
               url_domain="https://twibooru.org", proxies={}):
    """
    By default initializes an instance of Galleries with the parameters to get
    the first 25 galleries on Twibooru's galleries page.
    """
    self.proxies = proxies
    self.url_domain = url_domain
    self._params = {
      "key": api_key(key),
      "title": title,
      "description": description,
      "include_image": set_limit(include_image),
      "sf": sort_format_galleries(sf),
      "sd": sd,
      "perpage": set_limit(perpage),
      "page": set_limit(page),
      "user": user,
    }
    self._limit = set_limit(limit)
    self._search = get_galleries(self._params, self._limit,
                                 url_domain=self.url_domain, proxies=self.proxies)
  
  def __iter__(self):
    """
    Make Galleries() iterable so that new search results can be lazily generated
    for performance reasons.
    """
    return self

  @property
  def parameters(self):
    """
    Returns a list of available parameters; useful for passing state to new
    instances of Galleries().
    """
    return self._params

  @property
  def url(self):
    """
    Returns a search URL built on set parameters. Example based on default
    parameters:

    https://twibooru.org/galleries?title=*&description=&creator=&include_image=&sf=created_at&sd=desc
    """
    return url_galleries(self.parameters, url_domain=self.url_domain)

  def key(self, key=""):
    """
    Takes a user's API key string which applies content settings. API keys can
    be found at <https://twibooru.org/registration/edit>.
    """
    params = join_params(self.parameters, {"key": key,
                                           "limit": self._limit,
                                           "url_domain": self.url_domain,
                                           "proxies": self.proxies}
                        )

    return self.__class__(**params)

  def title(self, title=""):
    """
    Takes string for searching by title.
    """
    params = join_params(self.parameters, {"title": title,
                                           "limit": self._limit,
                                           "url_domain": self.url_domain,
                                           "proxies": self.proxies}
                        )

    return self.__class__(**params)

  def description(self, description=""):
    """
    Takes string for searching by description.
    """
    params = join_params(self.parameters, {"description": description,
                                           "limit": self._limit,
                                           "url_domain": self.url_domain,
                                           "proxies": self.proxies}
                        )

    return self.__class__(**params)

  def include_image(self, include_image=None):
    """
    Takes image ID for searching by include image.
    """
    params = join_params(self.parameters, {"include_image": include_image,
                                           "limit": self._limit,
                                           "url_domain": self.url_domain,
                                           "proxies": self.proxies}
                        )

    return self.__class__(**params)

  def user(self, user=""):
    """
    Takes string for searching by user.
    """
    params = join_params(self.parameters, {"user": user,
                                           "limit": self._limit,
                                           "url_domain": self.url_domain,
                                           "proxies": self.proxies}
                        )

    return self.__class__(**params)

  def sort_by(self, sf):
    """
    Determines how to sort search results. Available sorting methods are
    sort.SCORE, sort.COMMENTS, sort.HEIGHT, sort.RELEVANCE, sort.CREATED_AT,
    and sort.RANDOM; default is sort.CREATED_AT.
    """
    params = join_params(self.parameters, {"sf": sf,
                                           "limit": self._limit,
                                           "url_domain": self.url_domain,
                                           "proxies": self.proxies}
                        )

    return self.__class__(**params)

  def descending(self):
    """
    Order results from largest to smallest; default is descending order.
    """
    params = join_params(self.parameters, {"sd": "desc",
                                           "limit": self._limit,
                                           "url_domain": self.url_domain,
                                           "proxies": self.proxies}
                        )

    return self.__class__(**params)

  def ascending(self, sd="asc"):
    """
    Order results from smallest to largest; default is descending order.
    """
    params = join_params(self.parameters, {"sd": sd,
                                           "limit": self._limit,
                                           "url_domain": self.url_domain,
                                           "proxies": self.proxies}
                        )

    return self.__class__(**params)

  def limit(self, limit):
    """
    Set absolute limit on number of galleries to return, or set to None to return
    as many results as needed; default 50 galleries. This limit on app-level.
    """
    params = join_params(self.parameters, {"limit": limit,
                                           "url_domain": self.url_domain,
                                           "proxies": self.proxies})

    return self.__class__(**params)

  def get_page(self,page):
    """
    Set page for gets result of search.
    """
    params = join_params(self.parameters, {"page": set_limit(page),
                                           "limit": self._limit,
                                           "url_domain": self.url_domain,
                                           "proxies": self.proxies}
                        )

    return self.__class__(**params)

  def perpage(self,limit):
    """
    Set absolute limit on number of galleries to get, or set to None to return
    defaulting 25 galleries; max 50 galleries. This limit on API-level.
    """
    params = join_params(self.parameters, {"perpage": set_limit(limit),
                                           "limit": self._limit,
                                           "url_domain": self.url_domain,
                                           "proxies": self.proxies}
                        )

    return self.__class__(**params)

  def __next__(self):
    """
    Returns a result wrapped in a new instance of Gallery().
    """
    return Gallery(next(self._search), search_params=self.parameters,
                   url_domain=self.url_domain, proxies=self.proxies)