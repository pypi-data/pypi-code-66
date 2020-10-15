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

from .request import get_galleries, get_gallery_data, \
                     add_image_to_gallery, remove_image_from_gallery
from .search import Search

__all__ = [
  "Gallery"
]

class Gallery(object):
  """
  This class provides a thin wrapper around JSON data, mapping each value to
  its own property. Once instantiated the data is immutable so as to reflect
  the stateless nature of a REST API.
  """
  def __init__(self, data, gallery_id=None, search_params={},
               url_domain="https://twibooru.org", proxies={}):
    self.proxies = proxies
    self.url_domain = url_domain
    self._params = search_params

    if data is None and gallery_id:
      self._data = data = get_gallery_data(gallery_id, 
                                           url_domain=url_domain,
                                           proxies=proxies)
    else:
      self._data = data

    for field, body in data.items():
      if not hasattr(self, field):
        setattr(self, field, body) 

  def __str__(self):
    return f"Gallery({self.id})"
       
  @property
  def url(self):
    return f"{self.url_domain}/galleries/{self.id}"

  @property
  def data(self):
    return self._data

  def update(self):
    data = next(get_galleries(self._params, limit=1,
                              url_domain=self.url_domain, proxies=self.proxies))

    if data:
      self._data = data
  
  def images(self, key="", sf=None, sd="desc", limit=50,
             filter_id="", per_page=25, page=1):
    if sf is None:
      sf=f"gallery_id:{self.id}"
    if not key:
      key=self._params["key"] if "key" in self._params else ""
    return Search(key=key, 
                  q=(f"gallery_id:{self.id}",), sf=sf, sd=sd, limit=limit,
                  filter_id=filter_id, per_page=per_page, page=page,
                  url_domain=self.url_domain, proxies=self.proxies)

  def add_image(self, image_id, key=""):
    if not key:
      key=self._params["key"] if "key" in self._params else ""
    if add_image_to_gallery(image_id, self.id, key, url_domain=self.url_domain, proxies=self.proxies):
      return True
    else:
      return False

  def remove_image(self, image_id, key=""):
    if not key:
      key=self._params["key"] if "key" in self._params else ""
    if remove_image_from_gallery(image_id, self.id, key, url_domain=self.url_domain, proxies=self.proxies):
      return True
    else:
      return False