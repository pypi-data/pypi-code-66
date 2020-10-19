#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests


# In[3]:


URL = "https://api.adviceslip.com/advice"


# In[5]:


def advice(name):
    json_result = requests.get(URL).json()
    advice_result = json_result["slip"]["advice"]
    return f"{name}, {advice_result}"


# In[ ]:




