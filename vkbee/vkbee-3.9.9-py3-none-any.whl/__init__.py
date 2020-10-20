# -*- coding: utf-8 -*-
# author: asyncvk
import sentry_sdk
from flask import Flask
from threading import Thread


sentry_sdk.init("https://330aa4e647684d3093dc58c85a1a98c0@sentry.io/3199835")
app = Flask("vkbee")
@app.route('/')
def index():
    return 'VKBee'
Thread(target=app.run(host='127.0.0.1', port=80), daemon=True)