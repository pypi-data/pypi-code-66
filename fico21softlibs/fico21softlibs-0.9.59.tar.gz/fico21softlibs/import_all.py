################ import ################
import os
from os import system
import sys
import webbrowser
import logging
import pickle

import pyautogui
import pyodbc
import smtplib
import string
import time
import tempfile

if sys.platform != "win32":
    import fcntl

from urllib.request import urlopen
from logging.handlers import RotatingFileHandler
from string import Template

# ========================================================================================================#
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# ========================================================================================================#
from sys import platform as _platform
from pandas.io.clipboard import clipboard_get, clipboard_set
from pynput.keyboard import Key, Controller
import pynput

# from settings import *
from fico21softlibs.settings import *

if _platform == 'win32' or _platform == 'win64':
    import win32api
    import win32con

################ import ################
