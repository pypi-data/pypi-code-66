import os
from uuid import uuid4
import numpy as np
import json
import time
from .gpt2_utils import gpt2_sync_main, gpt2_async_start_main, gpt2_async_check_main


# GPT2 small
def gpt2(api_key, in_string, length = 5, temperature = 0.8, window_max = 100):
    out_list = gpt2_sync_main(
        api_key = api_key, 
        model_size = "gpt2", 
        in_string = in_string, 
        length = length, 
        temperature = temperature,  
        window_max = window_max)
    return out_list

def gpt2_async_start(api_key, in_string, length = 5, temperature = 0.8, window_max = 100):
    task_id = gpt2_async_start_main(
        api_key = api_key, 
        model_size = "gpt2", 
        in_string = in_string, 
        length = length, 
        temperature = temperature,  
        window_max = window_max)
    return task_id

def gpt2_async_check(api_key, task_id):
    dict_out = gpt2_async_check_main(api_key, task_id)
    return dict_out


# GPT2 XL
def gpt2_xl(api_key, in_string, length = 5, temperature = 0.8, window_max = 100):
    out_list = gpt2_sync_main(
        api_key = api_key, 
        model_size = "gpt2-xl", 
        in_string = in_string, 
        length = length, 
        temperature = temperature,  
        window_max = window_max)
    return out_list

def gpt2_xl_async_start(api_key, in_string, length = 5, temperature = 0.8, window_max = 100):
    task_id = gpt2_async_start_main(
        api_key = api_key, 
        model_size = "gpt2-xl", 
        in_string = in_string, 
        length = length, 
        temperature = temperature,  
        window_max = window_max)
    return task_id

def gpt2_xl_async_check(api_key, task_id):
    dict_out = gpt2_async_check_main(api_key, task_id)
    return dict_out