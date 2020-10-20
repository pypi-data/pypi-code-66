#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[ ]:


class MagicEightBall:
    def __init__(self):
        self.url = "https://api.adviceslip.com/advice"

    def advice(self, name):
        json_result = requests.get(self.url).json()
        advice_result = json_result["slip"]["advice"]
        return f"{name}, {advice_result}."

