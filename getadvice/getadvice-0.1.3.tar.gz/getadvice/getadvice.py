#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[4]:


Advice_URL = "https://api.adviceslip.com/advice"


# In[3]:


# class GetAdvice:
#     def __init__(self, url):
#         self.url = url

#     def advice(self, name):
#         json_result = requests.get(self.url).json()
#         advice_result = json_result["slip"]["advice"]
#         return f"{name}, {advice_result}"


# In[1]:


def advice(self, name):
    json_result = requests.get(self.url).json()
    advice_result = json_result["slip"]["advice"]
    return f"{name}, {advice_result}"

