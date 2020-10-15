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

import requests
from urllib.parse import urlencode
from .helpers import format_params, slugging_tag

__all__ = [
  "url", "request", "get_images", "get_image_data",
  "url_related", "request_related", "get_related",
  "post_image",
  "url_tags", "request_tags", "get_tags", "get_tag_data",
  "get_user_data",
  "request_filters",
  "get_filters", "get_filter_data",
  "url_galleries", "request_galleries", "get_galleries", "get_gallery_data",
  "url_topics", "request_topics", "get_topics", "get_topic_data",
  "url_search_posts",
  "url_posts", "request_posts", "get_posts",
  "vote", "fave",
  "add_image_to_gallery", "remove_image_from_gallery"
]

def request_content(search, p, items_name, post_request=False, proxies={}):
  if post_request:
    request = requests.post(search, params=p, proxies=proxies)
  else:
    request = requests.get(search, params=p, proxies=proxies)
  if "perpage" not in p:
    p["perpage"] = 50
  while request.status_code == requests.codes.ok and 'application/json' in request.headers.get('Content-Type'):
    if items_name:
      items, item_count = request.json()[items_name], 0
    else:
      items, item_count = request.json(), 0
    for item in items:
      yield item
      item_count += 1
    if item_count < p["perpage"]:
      break
    p["page"] += 1
    request = requests.get(search, params=p, proxies=proxies)

def get_content(request_func, *request_args, limit=50, **request_kwargs):
  if limit is not None:
    if limit > 0:
      r = request_func(*request_args, **request_kwargs)
      for index, content_item in enumerate(r, start=1):
        yield content_item
        if index >= limit:
          break
  else:
    r = request_func(*request_args, **request_kwargs)
    for content_item in r:
      yield content_item

def url(params, url_domain="https://twibooru.org"):
  p = format_params(params)
  url = f"{url_domain}/search?{urlencode(p)}"
  return url

def request(params, url_domain="https://twibooru.org", proxies={}):
  if "reverse_url" in params and params["reverse_url"]:
    search, p = f"{url_domain}/search/reverse.json", format_params(params)
    p = {i:p[i] for i in p if i in ('scraper_url','fuzziness','key')}
    post_request = True
  else:
    search, p = f"{url_domain}/search.json", format_params(params)
    p = {i:p[i] for i in p if i not in ('scraper_url','fuzziness')}
    post_request = False
  for image in request_content(search, p, "search", post_request=post_request, proxies=proxies):
    yield image

def get_images(params, limit=50, url_domain="https://twibooru.org", proxies={}):
  for image in get_content(request, params, limit=limit, url_domain=url_domain, proxies=proxies):
    yield image

def get_image_data(id_number, params={}, url_domain="https://twibooru.org", proxies={}):
  url, p = f"{url_domain}/{id_number}.json", format_params(params)

  request = requests.get(url, params=p, proxies=proxies)

  if request.status_code == requests.codes.ok:
    data = request.json()

    if "duplicate_of" in data and data["duplicate_of"]:
      return get_image_data(data["duplicate_of"], url_domain=url_domain, proxies=proxies)
    else:
      return data

def url_related(id_number, params, url_domain="https://twibooru.org"):
  p = format_params(params)
  url = f"{url_domain}/images/{id_number}/related?{urlencode(p)}"
  return url

def request_related(id_number, params, url_domain="https://twibooru.org", proxies={}):
  search, p = f"{url_domain}/images/{id_number}/related.json", format_params(params)
  request = requests.get(search, params=p, proxies=proxies)

  for image in request_content(search, p, "images", proxies=proxies):
    yield image

def get_related(id_number, params, limit=50, url_domain="https://twibooru.org", proxies={}):
  for image in get_content(request_related, id_number, params,
                           limit=limit, url_domain=url_domain, proxies=proxies):
    yield image

def post_image(key, image_url, description="", tag_input="", source_url="", anon=1,
               url_domain="https://twibooru.org", proxies={}):
  '''
  You must provide the direct link to the image in the image_url parameter.
  Abuse of the endpoint will result in a ban.
  '''
  search = f"{url_domain}/images.json"
  json = {
     "image": {
        "description": description, 
        "tag_input": ", ".join(tag_input), 
        "source_url": source_url,
        "anonymous": anon
     },
     "scraper_url": image_url
  }
  request = requests.post(search, params={"key": key}, json=json, proxies=proxies)
  if request.status_code == requests.codes.ok or request.status_code == requests.codes.created:
    data = request.json()
    return data

def url_tags(params, url_domain="https://twibooru.org"):
  p = format_params(params)
  p["tq"]=p["q"]
  del(p["q"])
  url = f"{url_domain}/tags?{urlencode(p)}"
  return url

def request_tags(params, url_domain="https://twibooru.org", proxies={}):
  search, p = f"{url_domain}/tags.json", format_params(params)
  if 'q' in p and p['q']:
    p["tq"]=p["q"]
    del(p["q"])
  for tag in request_content(search, p, None, proxies=proxies):
    yield tag

def get_tags(params, limit=50, url_domain="https://twibooru.org", proxies={}):
  for tag in get_content(request_tags, params, limit=limit, url_domain=url_domain, proxies=proxies):
    yield tag

def get_tag_data(tag, url_domain="https://twibooru.org", proxies={}):
  url = f"{url_domain}/tags/{tag}.json"

  request = requests.get(url, proxies=proxies)

  if request.status_code == requests.codes.ok:
    data = request.json()
    if "aliases" in data:
      data["tag"]["aliases"] = data["aliases"]

    return data["tag"]

def get_user_data(user_id=0, username="", url_domain="https://twibooru.org", proxies={}):
  if username:
    url = f"{url_domain}/profiles/{slugging_tag(username)}.json"
  else:
    url = f"{url_domain}/profiles/{user_id}.json"

  request = requests.get(url, proxies=proxies)

  if request.status_code == requests.codes.ok:
    data = request.json()

    return data

def request_filters(filter_id, params, url_domain="https://twibooru.org", proxies={}):
  '''filter_id can be "system"'''
  search, p = f"{url_domain}/filters.json", format_params(params)
  if filter_id=="system":
    for filter_item in request_content(search, p, "system_filters", proxies=proxies):
      yield filter_item
  elif 'q' in p and p['q']:
    p["fq"]=p["q"]
    del(p["q"])
    for filter_item in request_content(search, p, "search_filters", proxies=proxies):
      yield filter_item
  else:
    for filter_item in request_content(search, p, "user_filters", proxies=proxies):
      yield filter_item

def get_filters(filter_id, params, url_domain="https://twibooru.org", limit=50, proxies={}):
  for filter_item in get_content(request_filters, filter_id, params,
                                 limit=limit, url_domain=url_domain, proxies=proxies):
    yield filter_item

def get_filter_data(filter_id, url_domain="https://twibooru.org", proxies={}):
  url = f"{url_domain}/filters/{filter_id}.json"

  request = requests.get(url, proxies=proxies)

  if request.status_code == requests.codes.ok:
    data = request.json()

    return data

def url_galleries(params, url_domain="https://twibooru.org"):
  p = format_params(params)
  url = f"{url_domain}/galleries?{urlencode(p)}"
  return url

def request_galleries(params, url_domain="https://twibooru.org", proxies={}):
  search, p = f"{url_domain}/galleries.json", format_params(params)
  for gallery in request_content(search, p, None, proxies=proxies):
    yield gallery

def get_galleries(params, limit=50, url_domain="https://twibooru.org", proxies={}):
  for gallery in get_content(request_galleries, params, limit=limit, url_domain=url_domain, proxies=proxies):
    yield gallery

def get_gallery_data(gallery_id, url_domain="https://twibooru.org", proxies={}):
  url = f"{url_domain}/galleries/{gallery_id}.json"

  request = requests.get(url, proxies=proxies)

  if request.status_code == requests.codes.ok:
    data = request.json()

    return data["gallery"]

def url_topics(forum_short_name, params, url_domain="https://twibooru.org"):
  p = format_params(params)
  url = f"{url_domain}/{forum_short_name}?{urlencode(p)}"
  return url

def request_topics(forum_short_name, params, url_domain="https://twibooru.org", proxies={}):
  search, p = f"{url_domain}/{forum_short_name}.json", format_params(params)
  for topic in request_content(search, p, "topics", proxies=proxies):
    yield topic

def get_topics(forum_short_name, params, limit=50, url_domain="https://twibooru.org", proxies={}):
  for topic in get_content(request_topics, forum_short_name, params,
                           limit=limit, url_domain=url_domain, proxies=proxies):
    yield topic

def get_topic_data(forum_short_name, topic_slug, url_domain="https://twibooru.org", proxies={}):
  url = f"{url_domain}/{forum_short_name}/{topic_slug}.json"

  request = requests.get(url, proxies=proxies)

  if request.status_code == requests.codes.ok:
    data = request.json()
    return data[0]

def url_search_posts(params, url_domain="https://twibooru.org"):
  p = format_params(params)
  url = f"{url_domain}/posts?{urlencode(p)}"
  return url

def url_posts(forum_short_name, topic_slug, params, url_domain="https://twibooru.org"):
  import math
  p = format_params(params)
  api_page = p['page']
  api_perpage = p['perpage']
  web_perpage = 25
  api_last_post_on_page = api_page * api_perpage
  api_first_post_on_page = api_last_post_on_page - api_perpage + 1 
  p['page'] = math.ceil(api_first_post_on_page / 25)
  del(p['perpage'])
  url = f"{url_domain}/{forum_short_name}/{topic_slug}?{urlencode(p)}"
  return url

def request_posts(params, forum_short_name="", topic_slug="", url_domain="https://twibooru.org", proxies={}):
  if forum_short_name and topic_slug:
    search, p = f"{url_domain}/{forum_short_name}/{topic_slug}.json", format_params(params)
  else:
    search, p = f"{url_domain}/posts.json", format_params(params)
  for post in request_content(search, p, None, proxies=proxies):
    yield post

def get_posts(params, forum_short_name="", topic_slug="", limit=50, url_domain="https://twibooru.org", proxies={}):
  for post in get_content(request_posts, params,
                          limit=limit, forum_short_name=forum_short_name,
                          topic_slug=topic_slug, url_domain=url_domain, proxies=proxies):
    yield post

def vote(image_id, key, value, url_domain="https://twibooru.org", proxies={}):
  url = f"{url_domain}/api/v2/interactions/vote.json?key={key}"
  json = {
    "value": value, # 'up', 'down' or 'false'
    "id": image_id,
  }

  request = requests.put(url, json=json, proxies=proxies)

  if request.status_code == requests.codes.ok:
    data = request.json()
    return data

def fave(image_id, key, value, url_domain="https://twibooru.org", proxies={}):
  url = f"{url_domain}/api/v2/interactions/fave.json?key={key}"
  json = {
    "value": value, # 'true' or 'false'
    "id": image_id,
  }

  request = requests.put(url, json=json, proxies=proxies)

  if request.status_code == requests.codes.ok:
    data = request.json()
    return data

def add_image_to_gallery(image_id, gallery_id, key, url_domain="https://twibooru.org", proxies={}):
  url = f"{url_domain}/galleries/{gallery_id}/images.json"
  p = {"id": image_id, "key": key}
  request = requests.post(url, params=p, proxies=proxies)
  if request.status_code == requests.codes.ok:
    return True

def remove_image_from_gallery(image_id, gallery_id, key, url_domain="https://twibooru.org", proxies={}):
  url = f"{url_domain}/galleries/{gallery_id}/images/{image_id}.json"
  p = {"key": key}
  request = requests.delete(url, params=p, proxies=proxies)
  if request.status_code == requests.codes.ok:
    return True
   